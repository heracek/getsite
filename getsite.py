#!/usr/bin/env python
import os
import sys
import urllib

USAGE = ''' getsite.py <input_file> <home_url>'''

def main():
    if len(sys.argv) == 3:
        input_file, home_url = sys.argv[1:3]
        
        f = open(input_file)
        for url in f:
            url = url[:-1]
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