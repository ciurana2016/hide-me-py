# Hide a file .py
I've been playing some [OverTheWire](http://overthewire.org/wargames/bandit/) wargames lately, and in one lvl you have to find a hidden file in a bunch of subdirectories, this script trys to do something similar.

## Disclaimer (Before running it)
IT WILL CREATE 100 FILES WITH THE SAME SIZE OF THE INPUT ONE !!!
Just tryed it on mac.

## How it works
Run:
```
python ./-.py cat.jpg
```
And it will generate a folder structure like the following (everything is random duh):
```
/output-79422d0db46e82e328ea
    /2fc01817aa0e5c095660
    /544133cd8f2fd1df1eed
        01401a3f88c495249151.gz
        1143ad9b383a1616a2cd.gz
        256fb5d5a8ab107b53bd.gz  <---- YOUR FILE
        2715debcd83439899d11.gz
        527f83c62aff8ce60182.gz
        6721ff331fe5e01c10b1.gz
        7953a3de5cc046584e17.gz
        9c0b2e3c3d6c5fe2ad03.gz
        dccd69cfc569ccc0e1ea.gz
        f20b637e79f8b2e4718b.gz
    /756fdf60e577c74b7048
    /9f0c6dbfea847168453b
    /a3c5345bf849f0aae6a1
    /a59bff232e2b0a0dbe57
    /ccc90145f797479fb4b6
    /ce764c30349d75f4101d
    /dc7ebcdff5684aaf3e75
    /e124664d555cb875493e
```
When the script ends it tells you where your file is:
```
Your file is now under output-79422d0db46e82e328ea/544133cd8f2fd1df1eed/256fb5d5a8ab107b53bd.gz
```

