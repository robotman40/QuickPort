# External Python modules
import sys
import os
import subprocess as sp
import configparser as cfgp
import shutil
# Program Modules
import file
import errors
import general as gn

if __name__ == "__main__":
    """
    These checks will add the folders needed on first run
    """
    wrapperdirs = ["/winebuilds", "/box64builds", "/box86builds", "/dxvkbuilds", "/vkd3d-protonbuilds"]
    
    for dir in wrapperdirs:
        file.dircreate(dir)
        
    file.dircreate("/projects")
        
    """Pre-run error checking
    """
    
    if len(sys.argv) < 2:
        print("No commands were inputted. Please type \"-h\" or \"--help\" for a list of commands")
        exit()

    if sys.argv[1] == "-c" or sys.argv[1] == "--create":
        """
        These check for errors in the creation parameters prior to creation
        """
        if len(sys.argv) < 3:
            raise errors.ProjectNotSpecifiedError()
        if "/" in sys.argv[2]:
            raise errors.InvalidProjectNameError(sys.argv[2])
        if not "-t" in sys.argv[3] or "--target" in sys.argv[3]:
            raise errors.InvalidParametersError()
        if sys.argv[2] in os.listdir(f"{file.parentdir}/projects/"):
            raise errors.ProjectAlreadyExistsError(sys.argv[2])
        else:
            os.mkdir(f"{file.parentdir}/projects/{sys.argv[2]}/")
        
        """
        If the error checking passes, then we pass the rest of the parameters
        """
        
        """
        We are putting these in try and except clauses so in the case of an error, the project's directory gets removed
        """
        
        try:
            """
            Create the project's config file and config instance
            """
            open(f"{file.parentdir}/projects/{sys.argv[2]}/config.ini", "x")
            projectconfig = cfgp.ConfigParser()
            projectconfig["Project Config"] = {"target": "", "env": "", "arch": "", "armrunner": "", "winerunner": ""}
            
            if sys.argv[3] == "-t" or sys.argv[3] == "--target":
                if not os.path.exists(sys.argv[4]):
                    raise errors.TargetNotFoundError(sys.argv[4])
                else:
                    projectconfig["Project Config"]["target"] = sys.argv[4]
            else:
                raise errors.InvalidParametersError()
            
            parameters = sys.argv[5:]

            """
            Detect Parameters
            """
            if "--aarch64" in sys.argv:
                box64build = gn.buildselect("box64builds")
                
                if not "--armv7" in sys.argv:
                    projectconfig["Project Config"]["arch"] = "aarch64"
                    projectconfig["Project Config"]["armrunner"] = f"/{file.removedirectory(box64build)}/box64"
                    
            if "--armv7" in sys.argv:
                ignorewarning = True
                if "--wine" in sys.argv:
                    while True:
                        yesorno = input("ARMv7 should not be included due to Wow64 support in Wine. Are you sure you would like to include ARMv7 support anyway? {Y/y} {N/n}: ")
                        if yesorno.lower() == "n":
                            ignorewarning = False
                            break
                        elif yesorno.lower() == "y":
                            break
                        else:
                            print("Please enter a valid option")
                    
                if ignorewarning:
                    box86build = gn.buildselect("box86builds")
                    
                    if "--aarch64" in sys.argv:
                        projectconfig["Project Config"]["env"] = projectconfig["Project Config"]["env"] + f"/{file.removedirectory(box64build)}/box64"   
                    
                    projectconfig["Project Config"]["arch"] = "armv7"
                    projectconfig["Project Config"]["armrunner"] = f"/{file.removedirectory(box86build)}/box86"
                    
                
            if "--wine" in parameters:
                """
                Create Wine Prefix
                """
                winebuild = gn.buildselect("winebuilds")
                os.mkdir(f"{file.parentdir}/projects/{sys.argv[2]}/wineprefix")
                
                projectconfig["Project Config"]["winerunner"] = f"/{file.removedirectory(winebuild)}/bin/wine64"
                    
                os.environ["WINEPREFIX"] = f"{file.parentdir}/projects/{sys.argv[2]}/wineprefix"
                os.environ["WINEDEBUG"] = "-all"
                print("The Wine prefix will begin creating itself")
                sp.run([f"{winebuild}/bin/wine", "wineboot"])
                
            # These two functions are currently stubs and will be properly implemented at a later date
            if "--dxvk" in parameters:
                raise errors.WrapperNotCurrentlyImplementedError()
            
            if "--vkd3d-proton" in parameters:
                raise errors.WrapperNotCurrentlyImplementedError()
            
            """            
            This is when the project completes creation
            """
            with open(f"{file.parentdir}/projects/{sys.argv[2]}/config.ini", "w") as cfgfile:
                projectconfig.write(cfgfile)
                
            print("The project has been successfully created!")
        except Exception as e:
            """
            In the case the program runs into an error during project creation, we remove the project's directory
            """
            shutil.rmtree(f"{file.parentdir}/projects/{sys.argv[2]}")
            print(f"During project creation, an issue occurred: {e}")
                             
    elif sys.argv[1] == "-p" or sys.argv[1] == "--project":
        runner = cfgp.ConfigParser()
        
        if not sys.argv[2] in os.listdir(f"{file.parentdir}/projects/"):
            raise errors.ProjectNotFoundError(sys.argv[2])
        else:
            runner.read(f"{file.parentdir}/projects/{sys.argv[2]}/config.ini")
            
            runcommands = []
            
            if runner["Project Config"]["arch"] != "armv7":
                os.environ["BOX86_BOX64"] = f"{file.parentdir}/box64builds{runner["Project Config"]["armrunner"]}"
        
            if runner["Project Config"]["armrunner"] != "":
                if runner["Project Config"]["arch"] == "armv7":
                    runcommands.append(f"{file.parentdir}/box86builds{runner["Project Config"]["armrunner"]}")
                else:
                    runcommands.append(f"{file.parentdir}/box64builds{runner["Project Config"]["armrunner"]}")
                
            if runner["Project Config"]["winerunner"] != "":
                runcommands.append(f"{file.parentdir}/winebuilds{runner["Project Config"]["winerunner"]}")
                os.environ["WINEPREFIX"] = f"{file.parentdir}/projects/{sys.argv[2]}/wineprefix"
                
            runcommands.append(runner["Project Config"]["target"])
                
            sp.run(runcommands)
            
    else:
        errors.UnknownCommandError(sys.argv[1])