
from helper import FileManagement
import pathlib
cwd = pathlib.Path().resolve()
file_manager = FileManagement(cwd)
file_manager.run()
            

