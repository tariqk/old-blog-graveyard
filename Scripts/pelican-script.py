#!C:\Python\old-blog-graveyard\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'pelican==3.1.1','console_scripts','pelican'
__requires__ = 'pelican==3.1.1'
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.exit(
        load_entry_point('pelican==3.1.1', 'console_scripts', 'pelican')()
    )
