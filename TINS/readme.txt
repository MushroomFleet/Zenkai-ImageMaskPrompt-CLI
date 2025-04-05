we can create a dataset creation system called "Zenkai_IMP_prepare" which will use user defined paths in .json format to define the path to several folders which contain images.
example:
/path/to/images (user set folder path)
/path/to/images/images/
/path/to/images/prompts/
/path/to/images/mask/


1. the system must create a new "dataset" folder name appended with a timestamp.
2. copy the contents of /images/ into /dataset/
3a. If there is only one .txt file in the /prompts/ path, duplicate the single text file until a copy exists renamed to match every filename in /images/, copy the renamed text files into /dataset/
3b. If there is more than one .txt file in the path, copy the contents of /prompts/ into /dataset/
4. copy the contents of /mask/ into /dataset/ , appending each filename with "_M" into dataset



This should provide us with the "IMP Dataset", which is the product of this system.
we can do this in python, with a "requirements.txt" listing the package dependencies, create an install.bat which will create the venv, install dependencies listed inside "requirements.txt" and finally, create a run.bat which will activate the venv and start the main python script.

When the scripts are fully functional and written in this project, we can create the README.md for the Github release, which will:
- explain what this system does
- explain how to install
- explain the .json configuration with a full example
- step by step user instructions for use
