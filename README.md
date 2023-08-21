### This is fork of deleted repository
This is copy of deleted repository containing some improvements and new versions of program that include functionalities that I wanted. It contains three versions of the program. Every version have fixed some bugs and every version now have also selected download checkboxes on the program startup, it was not the case in original one. It just saves time on clicking them. Also at the start program enters -futanari tag in the search field. You can change it in source code in gui.py line 51: self.searchInput.setText(" -futanari")
- MAIN version is the basic downloader with some fixes THIS VERSION IS AN EXE FILE IN ROOT OF THE REPOSITORY >>>  Rule34-Downloader-MAIN.exe
- TAGSWITCH version will switch between tags (ADD THEM) that you provide in mainGUI.py after finishing download but will not start downloading. If certain tag have 0 matches, program will move to next one. If you want to download images every time with defined variety: have black_hair, short_hair, ponytail - this version of the programm will add those tags to original term - original tag so you don't have to type them manually every time you wanna download new for example character. YOU HAVE TO INSERT YOUR TAGS AND PACK EXE YOUR SELF
- AUTOMATED works like TAGSWITCH but downloads everything automatically. Version will switch (add certain tag to original search term) between tags that you provide in mainGUI.py and automatically download all of them. If certain tag have 0 matches, program will move to next one. For example you entered "princess_peach" and your mainGUI have tags set to "long_hair, short_hair, ponytail" - program will download - "princess_peach long_hair". "princess_peach short_hair" and "princess_peach ponytail" YOU HAVE TO INSERT YOUR TAGS AND PACK EXE YOUR SELF
TAGSWITCH AND AUTOMATED ARE WORKING AS FOLLOWS
- you add your tag/tags for example: "princess_peach" / "princess_peach solo black_hair blue_eyes" into txt search field
- after clicking SEARCH and seeing that there are some images matching your tags you click DOWNLOAD
- in TAGSWITCH version program will ADD the tag and you can click SEARCH to check if it returns some images. If not program will switch to the next one. For example from "princess_peach" to "princess_peach long_hair".
- in AUTOMATED version program will check if your second/next tag/tags are returning some images, if yes program  will download them and repeat process until all tags ware check and downloaded/skipped
- in booth versions default 3 tags  are set to: long_hair, ponytail and hime_cut /by searching those (ctrl+F) you will easily replace them to your linking
I wrote those changes for my self so you should modify it to your liking. In case of AUTOMATED version there is slight problem that it search for tags at the end of downloading but I don't see it as a problem and don't bother to fix it. If you want you can do it your self. Version contain some minor bugs but all of them are functional.

### BELOW ORIGINAL README

![Image](https://i.imgur.com/bGs9kps.png)

### What does it do?
Downloads every image it can find on Rule34 that matches the tags you search for. 

## Dependencies
- Python3.5+
- [My Rule34 API wrapper](https://github.com/LordOfPolls/Rule34-API-Wrapper)
- [PyQT5](https://github.com/pyqt/python-qt5)

## How do i use it?

Windows Executable: https://github.com/LordOfPolls/Rule34-Downloader/blob/master/dist/main.exe?raw=true

**Or**

- Clone the repository
- Navigate to the root directory (the one with ``requirements.txt`` in)
- Run ``pip install -r requirements.txt``
  - This will install all dependencies
  
**then**

- Run main.py / main.exe and follow the on screen instructions
- If you get stuck, hover over each field for a description of what it does
- Enjoy your excessive amount of porn

### FAQ

**Can I search for more than one tag at once?**

>Yes, the program treats each word as a tag; so ``gay mario`` is
> treated as two tags; ``gay`` and ``mario``

**What about multi_word tags?** 

>The program treats them the same way rule34 does, usually with
>underscores. I'd suggest searching on rule34 first to make sure it's a
>real tag. 

**Can I download a specific amount of posts?**

> Yes, there is a field to enter a specific limit

**Can I save a list of URLs?**

>Yes there's a checkbox for that

**[Insert antivirus here] says this is a virus**

> I can assure you, this is not a virus. I'm not entirely sure why anti-viruses sometimes flag this as a virus,
> at a guess, I assume its because of how many requests it makes. Either way, if you're worried, you can see the source
> code, and run straight from the py file
# Like what I do?

Why not buy me a coffee? [https://paypal.me/LordOfPolls](https://paypal.me/LordOfPolls)
