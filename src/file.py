# External Python Modules
import os
import pathlib as pl
import requests as rq
import zipfile as zf
import tempfile as tf
import io
import subprocess as sp
import shutil as st

# Program Modules
import main

# Variables
parentdir = parentdir = str(pl.Path(__file__).parent)
wrapper_downloads = {
    "wine": "stub", "box64": "stub", "box86": "stub",
    "dxvk": "stub", "vkd3d-proton": "stub"}

# Functions
def dircreate(target) -> bool:
    if not os.path.isdir(parentdir + target):
        os.makedirs(parentdir + target)
        return True
    else:
        return False
        
def downloadver(wrapper):
    # Check if a valid wrapper is chosen
    raise NotImplemented("Downloading releases officially from the used wrappers will come at a later time")

def removedirectory(dir) -> str:
    while True:
        try:
            slashindex = dir.index("/")
            dir = dir[slashindex + 1:]
        except:
            return dir
            
def copybuild(wrapper, project):
    st.copytree(wrapper, project, dirs_exist_ok=True)