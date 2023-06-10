import subprocess
import os
from pathlib import Path
import glob
import pandas as pd
from datetime import datetime
from bs4 import BeautifulSoup
from html import unescape


path = "//NAS-1/Music"
start = Path(path)
lists = list(start.rglob("*.mp3"))

st_size_list = []
st_mode_list = []
st_ino_list = []
st_dev_list = []
st_nlink_list = []
st_uid_list = []
st_gid_list = []
st_atime_list = []
st_mtime_list = []
st_ctime_list = []
file_name_list = []
new_data = {}
result_list = []
name_list = []
i = 0

for item in lists:
        source_name = item.name
        fname = fname.replace(".txt", "")
        fname = fname.strip()
        fname = fname + ".txt"
        fname = BeautifulSoup(unescape(source_name), 'lxml')
        
        fstat = os.stat(item)
        
        i = i + 1

        file_name = fname.capitalize()
        file_name_list.append(file_name)
        new_data['name'] = file_name

        st_size = fstat.st_size
        st_size_list.append(st_size)
        new_data['st_size'] = st_size

        st_mode = fstat.st_mode
        st_mode_list.append(st_mode)
        
        new_data['st_mode'] = st_mode

        st_ino = fstat.st_ino
        st_ino_list.append(st_ino)
        new_data['st_ino'] = st_ino

        st_dev = fstat.st_dev
        st_dev_list.append(st_dev)
        new_data['st_dev'] = st_dev

        st_nlink = fstat.st_nlink
        st_nlink_list.append(st_nlink)
        new_data['st_nlink'] = st_nlink

        st_uid = fstat.st_uid
        st_uid_list.append(st_uid)
        new_data['st_uid'] = st_uid

        st_gid = fstat.st_gid
        st_gid_list.append(st_gid)
        new_data['st_gid'] = st_gid

        atime = fstat.st_atime
        st_atime = datetime.fromtimestamp(atime)
        st_atime_list.append(st_atime)
        new_data['st_atime'] = st_atime

        mtime = fstat.st_mtime
        st_mtime = datetime.fromtimestamp(mtime)
        st_mtime_list.append(st_mtime)
        new_data['st_mtime'] = st_mtime

        ctime = fstat.st_ctime
        st_ctime = datetime.fromtimestamp(ctime)
        st_ctime_list.append(st_ctime)
        new_data['st_ctime'] = st_ctime
        
        result_list.append(new_data)
        dict = {'name': file_name_list, 'st_size': st_size_list, 'st_mode': st_mode_list, 'st_ino': st_ino_list, 'st_dev': st_dev_list,
                'st_nlink': st_nlink_list, 'st_uid': st_uid_list, 'st_gid': st_gid_list, 'st_atime': st_atime_list, 'st_mtime': st_mtime_list, 'st_ctime': st_ctime_list}

        df = pd.DataFrame(dict)

        df.to_csv('Result_music_list.csv')
