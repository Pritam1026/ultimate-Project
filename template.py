import os
import sys
from pathlib import Path
import logging

while True:
    project_name=input("Please enter your project name: ")
    if project_name!="":
        break

file_name_list=[
        f"{project_name}/__init__.py",
        f"{project_name}/components/__init__.py",
        f"{project_name}/config/__init__.py",
        f"{project_name}/constants/__init__.py",
        f"{project_name}/entity/__init__.py",
        f"{project_name}/exception/__init__.py",
        f"{project_name}/logger/__init__.py",
        f"{project_name}/pipelines/__init__.py",
        f"{project_name}/utils/__init__.py",
        "config/config.yaml",
        "schema.yaml",
        "app.py",
        "main.py",
        "logs.py",
        "exception.py",
        "requiremnets.txt",
        "setup.py"

]
try:
    for filepath in file_name_list:
        filepath=Path(filepath)
        filedir,file_name=os.path.split(filepath)
        
        if filedir!="":
            os.makedirs(filedir,exist_ok=True)
        
        if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
            with open(filepath,"w") as f:
                pass
        
        else:
            logging.info("file already exists")
except Exception as e:
    print(e)