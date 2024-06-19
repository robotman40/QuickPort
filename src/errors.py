class InvalidParametersError(Exception):
    def __init__(self, parameters = None):
        message = "Your program did not run due to the following errors in your parameters:\n"
        
        if parameters != None and (len(parameters) < 2):
            message += "- You did not put in any parameters"
        
        if not parameters == None:
            super().__init__(message)
        else:
            super().__init__("No parameters were properly specified")
        
class NoWrappersFoundError(Exception):
    def __init__(self, dir):
        super().__init__(f"No wrappers were found in ~{dir}")
        
class ProjectNotSpecifiedError(Exception):
    def __init__(self):
        super().__init__(f"A project was not specified for the testing environment")
        
class NoProjectNameSpecifiedError(Exception):
    def __init__(self):
        super().__init__(f"No project name was specified for creation")
        
class InvalidProjectNameError(Exception):
    def __init__(self, name):
        super().__init__(f"The name \"{name}\" is not valid for a project")
        
class NoBuildsFoundError(Exception):
    def __init__(self, dir):
        super().__init__(f"No builds for in {dir} could be found")
        
class ProjectAlreadyExistsError(Exception):
    def __init__(self, name):
        super().__init__(f"The project \"{name}\" already exists")
        
class UnknownCommandError(Exception):
    def __init__(self, command):
        super().__init__(f"\"{command}\" is not a valid command")
        
class NoCommandsInputtedError(Exception):
    def __init__(self):
        super().__init__("No commands were inputted")
        
class TargetNotFoundError(Exception):
    def __init__(self, target):
        super().__init__(f"The inputted target {target} does not exist")
        
class ProjectCreationError(Exception):
    def __init__(self, message):
        super().__init__(f"An error occurred during project creation. Error: {message}")
        
class ProjectNotFoundError(Exception):
    def __init__(self, proj):
        super().__init__(f"The project \"{proj}\" was not found. Perhaps you misspelled the project you are looking for?")
        
class WrapperNotCurrentlyImplementedError():
    def __init__(self):
        super().__init__("Support for DXVK and vkd3d-proton are not currently implemented")