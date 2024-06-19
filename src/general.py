# External Python Modules
import os

# Program Modules
import file
import errors
import subprocess as sp

def buildselect(wrapperdirname):
    # Check if the directory is empty
    builds = {}
    
    index = 0
    for items in os.listdir(f"{file.parentdir}/{wrapperdirname}/"):
        builds[index] = f"{file.parentdir}/{wrapperdirname}/{items}"
        index += 1
        
    if len(builds) == 0:
        raise errors.NoBuildsFoundError(f"{file.parentdir}/{wrapperdirname}/")
    
    for options in builds.keys():
        buildoption = file.removedirectory(builds[options])
        print(f"{options}: {buildoption}")

    while True:
        prefbuild = int(input("Select your build using your keyboard by entering your preferred build's associated index: "))
        if prefbuild < 0 or prefbuild > len(builds) - 1:
            print("You entered an invalid option. Please try again")
            continue
        else:
            return builds[prefbuild]