# Deprecation Notice
This modified fork is now deprecated and no longer will be maintained. Any support for using this fork and not the [origin](https://github.com/kairusds/eidolonrp) will be ignored.

## Termux instructions
1. Download Termux from F-Droid (you can also download from the play store but that's outdated)
Optional: download hacker keyboard from playstore so that moving is easier, though, vim has touch support so only use hacker keyboard if you are going to use nano instead
2. Launch Termux and do `pkg upgrade && pkg install python git vim`
3. Do `git clone https://github.com/vbajs/eidolonrp` to download this
4. Then do `cd eidolonrp && pip install -r requirements.txt`
5. Then proceed to edit the script with `vim index.py` or if you are going to use hacker keyboard, `nano index.py`. Replace all the placeholder text with your input
6. Finally, run the script with `python index.py`
To exit, do CRTL+C or simply exit Termux
