import math
import os
import re
import sys
from rule34 import Rule34, Sync
import gui
import urllib.request
import concurrent.futures
from queue import Queue
from timeit import default_timer as timer
from time import sleep
from PyQt5 import QtCore, QtGui, QtWidgets

class r34DwnldrGUI:
    def __init__(self, _app: QtWidgets.QApplication):
        self.searchTerm = None  # The currently entered search term
        self.directory = None  # The save directory
        self.downloadImages = False
        self.downloadVideos = False
        self.saveURLS = False
        self.createSubfolder = False
        self.downloadLimit = -1

        self.tagiiterator = 0
        self.OryginalnysearchTerm = None

        # API KEY LOAD IN
        self.api_key = None
        self.user_id = None
        # load the single line from txt
        with open("api.txt", "r", encoding="utf-8") as f:
            line = f.read().strip()
        if "&api_key=" in line and "&user_id=" in line:
            parts = line.split("&")
            for part in parts:
                if part.startswith("api_key="):
                    self.api_key = part.split("=", 1)[1]
                elif part.startswith("user_id="):
                    self.user_id = part.split("=", 1)[1]
        # API KEY LOAD IN END
        self.r34 = Sync(self.api_key, self.user_id)

        self.totalExpected = 0  # How many posts are expected
        self.postList = []

        self.stopFlag = False  # Tells the currently running threads to stop
        self.done = False  # Set to true when the download completes

        self.executor = concurrent.futures.ThreadPoolExecutor(max_workers=2)

        self.progBarQueue = Queue()
        self.etaQueue = Queue()
        self.lcdQueue = Queue()
        self.currentTaskQueue = Queue()

        self.app = _app
        self.uiWindow = QtWidgets.QMainWindow()
        self.ui = gui.Ui_Rule34Downloader()

    @staticmethod
    def processQueue(queue: Queue, uiSetFunc, name="unnamed"):
        """
        Processes a queue for ui events. Necessary to avoid access violations with PyQT (only main thread can set ui)

        :param queue: a queue of ui values to be set
        :param uiSetFunc: the function to handle setting these ui values
        :param name: optional, the name of this queue (for debugging)
        :return:
        """
        while not queue.empty():
            value = queue.get()
            # print(f"Processing {name} queue: {job}")
            if value is not None:
                uiSetFunc(value)

    def clearExecutor(self, wait=True):
        """Clears the executor, to avoid access violations
        These tend to occur when the user tries to run 2 downloads without closing"""
        print("s t o p")
        self.stopFlag = True
        self.executor.shutdown(wait=wait)
        self.executor = concurrent.futures.ThreadPoolExecutor(max_workers=2)

    def runInExecutor(self, function, *args, **kwargs):
        """Run a provided function in executor"""
        future = self.executor.submit(function, *args, **kwargs)
        while not future.done():
            if self.stopFlag or self.uiWindow.isHidden():
                # if uiWindow hidden, then the X button has been pressed
                self.stopFlag = True
                future.cancel()

            # process any pending ui sets
            self.processQueue(self.progBarQueue, self.ui.searchProgBar.setValue, name="ProgBar")
            self.processQueue(self.etaQueue, self.ui.ETA.setText, name="ETA")
            self.processQueue(self.lcdQueue, self.ui.searchLCD.display, name="LCD")
            self.processQueue(self.currentTaskQueue, self.ui.currentTask.setText, name="CurrentTask")

            # allow the ui system to process events
            self.app.processEvents()
        result = future.result()
        return result


    def _runAfterTask(self):
        self.checkCanBegin()
        self.ui.currentTask.setText("Idle")

    def setupUI(self):
        """Sets-up the ui"""
        self.app.setStyle("Fusion")
        self.ui.setupUi(self.uiWindow)
        self.uiWindow.resize(500, 450)

        self.ui.searchProgBar.setValue(0)
        self.ui.destinationLine.setEnabled(False)
        self.ui.ETA.setText("0 seconds")
        self.ui.currentTask.setText("Idle")

        # setup events
        self.app.aboutToQuit.connect(self.quit)
        self.ui.browseButton.clicked.connect(self.browse)
        self.ui.searchButton.clicked.connect(self.search)
        self.ui.beginButton.clicked.connect(self.begin)
        self.ui.quitButton.clicked.connect(self.quit)
        self.ui.cancelButton.clicked.connect(self.cancel)
        self.ui.ckBoxSaveURLs.clicked.connect(self.checkCanBegin)
        self.ui.ckboxDownloadImages.clicked.connect(self.checkCanBegin)
        self.ui.ckBoxDownloadVideos.clicked.connect(self.checkCanBegin)

        self.uiWindow.show()

    def clearUI(self):
        """Clears all ui elements"""
        #self.ui.searchInput.setText(self.searchTerm)
        #self.ui.destinationLine.setText(self.directory)
        #self.ui.ckboxDownloadImages.setChecked(False)
        #self.ui.ckBoxDownloadVideos.setChecked(False)
        #self.ui.ckBoxSaveURLs.setChecked(False)
        self.ui.searchLCD.display(0)
        self.ui.ETA.setText("0 seconds")
        self.ui.searchProgBar.setValue(0)
        # self.setProgBar()

    def toggleUI(self, state: bool):
        """Allows you to disable all input ui, useful when downloading"""
        self.ui.searchButton.setEnabled(state)
        self.ui.browseButton.setEnabled(state)
        self.ui.beginButton.setEnabled(state)
        self.ui.ckBoxSaveURLs.setEnabled(state)
        self.ui.ckboxDownloadImages.setEnabled(state)
        self.ui.ckBoxSubfolder.setEnabled(state)
        self.ui.ckBoxDownloadVideos.setEnabled(state)
        self.ui.downloadLimit.setEnabled(state)

    def checkCanBegin(self):
        """Checks if the program has all the information needed to download"""
        if self.searchTerm is not None and self.directory is not None:
            # if user has given a search term and a directory
            if self.ui.ckBoxSaveURLs.isChecked() or self.ui.ckBoxDownloadVideos.isChecked() or self.ui.ckboxDownloadImages.isChecked():
                # if the user has chosen at least 1 task
                return self.ui.beginButton.setEnabled(True)
        return self.ui.beginButton.setEnabled(False)  # Disables the begin button

    def cacheUI(self):
        """Caches the currently set options in the ui, so the threads dont need to access ui"""
        self.search()
        self.downloadImages = self.ui.ckboxDownloadImages.isChecked()
        self.downloadVideos = self.ui.ckBoxDownloadVideos.isChecked()
        self.saveURLS = self.ui.ckBoxSaveURLs.isChecked()
        self.createSubfolder = self.ui.ckBoxSubfolder.isChecked()
        self.downloadLimit = self.ui.downloadLimit.value()

    def _gatherPosts(self):
        """Gathers posts from rule34 for a given tag"""
        postList = []

        if self.totalExpected == 0:
            #add
            #self.tagi()
            print("Debug1")
            #self.search()
        estimatedPages = math.ceil(self.totalExpected/100)
        times = []

        # you could just gather all images at once, but because i want a progress bar, i have to do it manually
        for i in range(estimatedPages):
            start = timer()
            if self.stopFlag:
                return
            self.progBarQueue.put(int(
                (i / estimatedPages) * 100
            ))
            averageTime = sum(times) / len(times) if len(times) != 0 else 0.423
            eta = (estimatedPages-i) * averageTime
            if eta < 60:
                self.etaQueue.put(
                    f"{float(eta):.3} seconds"
                )
            else:
                self.etaQueue.put(
                    f"{float(eta)/60:.3} minutes"
                )
            page = self.r34.getImages(singlePage=True, OverridePID=i, tags=self.searchTerm)

            # process this page
            for post in page:
                video = (post.file_url.endswith("mp4") or post.file_url.endswith("webm"))  # is this a video?
                if self.downloadImages or self.downloadVideos:
                    if not self.downloadVideos:
                        # if user doesnt want videos
                        if video:
                            continue
                    elif self.downloadVideos and not self.downloadImages:
                        # if user wants videos, but not images
                        if not video:
                            continue
                postList.append(post)

            self.lcdQueue.put(len(postList))

            # apply download limit if set
            if self.downloadLimit != -1:
                postList = postList[:self.downloadLimit]

            self.postList = postList
            end = timer()
            times.append(end-start)
            times = times[-100:]
        average = sum(times) / len(times)
        print(f"Average time: {average}")
        self.progBarQueue.put(100)
        return

    def _download(self):
        """Downloads all posts in postList"""
        self.currentTaskQueue.put(f"Downloading {len(self.postList)} posts")
        # process directory
        directory = self.directory
        if self.createSubfolder:
            tempTag = re.compile('[^a-zA-Z]').sub('_', self.searchTerm)  # clear non alpha-numeric characters
            newPathName = '_'.join(tempTag.split(" "))  # clear spaces
            directory += f"/{newPathName}"
            if not os.path.isdir(directory):
                print("creating sub-folder")
                os.mkdir(directory)

        numDownloaded = 0  # How many posts have been downloaded
        ETA = 0  # how many seconds estimated left
        times = []  # stores a list of execution times
        urlFile = None  # the file for saving urls, if used

        if self.saveURLS:
            # if the user wants urls saved, create the file here
            print("Creating url file")
            urlFileDir = f"{directory}/urls.txt"
            urlFile = open(urlFileDir, "w")
            urlFile.write(f"### URLs for search: {self.searchTerm} ###\n")

        for post in self.postList:
            average = (sum(times) / len(times)) if len(times) != 0 else 5
            ETA = average * (len(self.postList) - numDownloaded)
            if ETA < 60:
                self.etaQueue.put(
                    f"{float(ETA):.3} seconds"
                )
            else:
                self.etaQueue.put(
                    f"{float(ETA)/60:.3} minutes"
                )

            self.progBarQueue.put(int(
                numDownloaded/len(self.postList)*100
            ))

            start = timer()
            if self.stopFlag:
                self.stopFlag = False
                if urlFile:
                    urlFile.close()
                self.done = True
                return

            name = "{}/{}.{}".format(directory, post.id.split("/")[-1], post.file_url.split(".")[-1])
            video = ("webm" in name or "mp4" in name)

            try:
                if self.saveURLS:
                    print("Writing to file")
                    urlFile.write("\n" + post.file_url)

                if self.downloadImages or self.downloadVideos:
                    if video and not self.downloadVideos:
                        continue
                    if not video and not self.downloadImages:
                        continue

                    if not os.path.isfile(name):
                        with urllib.request.urlopen(post.file_url) as f:
                            imageContent = f.read()
                            # i use a download temp file because if the download is interrupted,
                            # its obvious which is the garbled file
                            with open(f"{directory}/download.temp", "wb") as _f:
                                _f.write(imageContent)
                            os.rename(f"{directory}/download.temp", name)

                numDownloaded += 1
                self.lcdQueue.put(numDownloaded)
            except Exception as e:
                print(f"Skipping post due to error: {e}")

            end = timer()
            times.append(end-start)
            times = times[-100:]
        if urlFile:
            urlFile.close()

        self.done = True
        return

# region: button actions


    def browse(self):
        """Opens the browse menu"""
        print("Browse button pressed")
        self.ui.currentTask.setText("Waiting for directory")

        # open a directory selection dialogue
        self.directory = str(QtWidgets.QFileDialog.getExistingDirectory(self.uiWindow, "Select Directory"))
        self.ui.destinationLine.setText(self.directory)

        self._runAfterTask()

    def search(self):
        #ADD 1 line below
        self.ui.searchButton.setEnabled(False)
        """Calls rule34 to search for images with given tag(s)"""
        print("Search button pressed")
        self.ui.currentTask.setText("Searching Rule34")

        self.searchTerm = self.ui.searchInput.text().replace(",", "").strip()
        self.ui.searchProgBar.setValue(25)
        # self.setProgBar(25)

        # technically this shouldn't need its own thread, but in theory it could crash the main thread, so im being safe
        self.totalExpected = self.runInExecutor(self.r34.totalImages, self.searchTerm)

        self.ui.searchProgBar.setValue(100)
        # self.setProgBar(100)
        self.ui.searchLCD.display(self.totalExpected)

        self._runAfterTask()

        #START ADD
        self.ui.searchButton.setEnabled(True)

        if self.totalExpected == 0:
            self.checkCanBegin()
            #self.tagi()
        else:
            self.checkCanBegin()

    #add
    def tagi(self):
        self.mfuta = " -futanari"
        self.t1 = " long_hair"
        self.t2 = " ponytail"
        self.t3 = " hime_cut"
    #ADD
        if self.tagiiterator == 0:
            self.OryginalnysearchTerm = self.searchTerm.replace(" -futanari", "")
            print("Oryginal string: ")
            print(self.OryginalnysearchTerm)
            print("Tag1")
            self.searchTerm = self.OryginalnysearchTerm + self.t1
            print(self.searchTerm)
            self.tagiiterator += 1
        elif self.tagiiterator == 1:
            print("Tag2")
            self.searchTerm = self.OryginalnysearchTerm + self.t2
            print(self.searchTerm)
            self.tagiiterator += 1
        elif self.tagiiterator == 2:
            print("Tag3")
            self.searchTerm = self.OryginalnysearchTerm + self.t3
            print(self.searchTerm)
            self.tagiiterator += 2 #+2 to else
        # add
        elif self.tagiiterator == 3:
            print("Canceled term = oryginal term and iterator = 0")
            self.searchTerm = self.OryginalnysearchTerm + self.mfuta
            self.tagiiterator = 0
        else:
            print("-ft return tag")
            self.searchTerm = " -futanari"
            print(self.searchTerm)
            self.tagiiterator = 0

        self.ui.searchInput.setText(self.searchTerm)


    def begin(self):
        """Prepares the postList and starts the download"""
        print("Begin button pressed")
        self.ui.currentTask.setText("Gathering and validating posts")

        # disable the ui so user cant modify anything
        self.toggleUI(False)
        self.cacheUI()
        # gathers posts from r34 in separate thread
        self.runInExecutor(self._gatherPosts)


        self.runInExecutor(self._download)

        self.totalExpected = 0
        self.imgList = []
        self.stopFlag = False
        self.ui.ETA.setText("0 seconds")
        if self.done:
            self.ui.currentTask.setText("Download Complete!")

            #add
            #self.tagi()

            #if self.totalExpected == 0:
            #    self.tagi()
            #    self.search()
            #elif self.tagiiterator != 0:
             #   self.begin()




            self.ui.searchProgBar.setValue(100)

            # flash taskbar icon, and make a notification sound
            self.app.alert(self.uiWindow, msecs=0)
            self.app.beep()

        self.done = False
        self.toggleUI(True)

    def cancel(self):
        """Clears the app, as if it had just opened
        If a download is currently running, thats stopped too"""
        print("Cancel")
        #add
        self.tagiiterator = 3

        self.toggleUI(False)  # Make sure ui is disabled while we cancel

        # clear variables
        # self.searchTerm = None
        # self.directory = None
        # self.totalExpected = 0
        # self.imgList = []
        # self.stopFlag = True
        # self.done = False

        try:
            # wait for any download tasks to end
            self.clearExecutor()
        except:
            pass
        self.stopFlag = False

        self.clearUI()
        self.ui.currentTask.setText("Cancelled!")
        self.toggleUI(True)
        self.checkCanBegin()
        #self.tagi()

    def quit(self):
        """As the name suggests"""
        print("Quit button pressed")
        self.clearExecutor(wait=False)
        self.app.exit()

# endregion




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    _r34D = r34DwnldrGUI(app)
    _r34D.setupUI()
    sys.exit(app.exec_())

