@echo off
docker run -it -p 9999:8888 -v C:/Users/Vlad/Desktop/DockerFiles/work:/home/jovyan/work jupyter/pyspark-notebook start.sh jupyter lab --LabApp.token='' --LabApp.disable_check_xsrf=True --net=host --pid=host -e TINI_SUBREAPER=true
cmd /K
