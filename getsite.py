#!/usr/bin/env python
import os
import sys
import urllib

USAGE = '''Usage: getsite.py <INPUT_FILE> <HOME_URL>

    For each URL form INPUT_FILE that starts with HOME_URL getsite.py gets
    data from URL and saves it to appropriate file and directory.

    INPUT_FILE ... file with URL (one for each line) 
                   you can get URLs by copy-pasting Safari's Activity window
    HOME_URL   ... e.g.: http://site.com/dir/
'''

def main():
    if len(sys.argv) == 3:
        input_file, home_url = sys.argv[1:3]
        
        f = open(input_file)
        for url in f:
            url = url[:-1] # remove \n
            if url.startswith(home_url):
                if url.endswith('/'):
                    filename = 'index.html'
                    dirname = os.path.join(*url[len(home_url):-1].split('/'))
                else:
                    filename = url.rsplit('/', 1)[1]
                    dirname = os.path.join(*url[len(home_url):-len(filename) - 1 ].split('/'))
                
                print url
                print ' ' * len(home_url) + os.path.join(dirname, filename)
                if len(dirname) > 0:
                    try:
                        os.makedirs(dirname)
                    except OSError:
                        pass
                urllib.urlretrieve(url, os.path.join(dirname, filename))
                
    else:
        print USAGE
        sys.exit(1)

if __name__ == '__main__':
    main()