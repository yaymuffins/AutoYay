#!/usr/bin/python2

import sys, os, hashlib, StringIO
import bencode



def main():
    # Open torrent file
    torrent_file = open(sys.argv[1], "rb")
    metainfo = bencode.bdecode(torrent_file.read())
    info = metainfo['info']
    print hashlib.sha1(bencode.bencode(info)).hexdigest()    

if __name__ == "__main__":
    main()
