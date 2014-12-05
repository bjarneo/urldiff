urldiff
=======

Python tool using diff and curl to check different content on webpages. Note: This doesn't apply SPAs.
<br />
I do recommend installing colordiff (apt-get install colordiff).
<br />
This tool is only tested in mint and ubuntu.

Usage:
```bash
chmod +x check.py
./check.py
```

or

```bash
python check.py "http://www.web.com/::http://www.web.com/?param=true"
```

or

```bash
ln -s /your/folder/urldiff/check.py /usr/local/bin/urldiff

urldiff "url::url"
```

