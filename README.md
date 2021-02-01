# eidolonrp
A rich presence selfbot.
All changes will now have to be done manually on the script directly instead of using an env file.

<table>
<tr><th>placeholder</th><th>what to replace with</th></tr>
<tr><td>token</th><td>user account token</td></tr>
<tr><td>appid</td><td>the application's id to use with its rich presence assets</td></tr>
<tr><td>name</td><td>header of the rich presence</td></tr>
<tr><td>url</td><td>twitch stream url (only used when type=1)(The input is there, just remove the #s)</td></tr>
<tr><td>type</td><td>(int) type of the activity. 0: playing, 1: streaming, 2: listening, 3: watching</td></tr>
<tr><td>state</td><td>second line of the rich presence</td></tr>
<tr><td>details</td><td>third line of the rich presence</td></tr>
<tr><td>largeimageID,NOTKEY</td><td>rich presence asset large image id</td></tr>
<tr><td>largetext</td><td>text tip for the large image</td></tr>
<tr><td>smallimageID,NOTKEY</td><td>rich presence asset small image id</td></tr>
<tr><td>smalltext</td><td>text tip for the small image</td></tr>
</table>

## Preview
![pv](pv.png)


## Termux instructions
1. Download Termux from F-Droid (you can also download from the play store but that's outdated)
Optional: download hacker keyboard from playstore so that moving is easier, though, vim has touch support so only use hacker keyboard if you are going to use nano instead
2. Launch Termux and do `pkg upgrade && pkg install python git vim`
3. Do `git clone https://github.com/vbajs/eidolonrp` to download this
4. Then do `cd eidolonrp && pip install -r requirements.txt`
5. Then proceed to edit the script with `vim index.py` or if you are going to use hacker keyboard, `nano index.py`. Replace all the placeholder text with your input
6. Finally, run the script with `python index.py`
To exit, do CRTL+C or simply exit Termux
