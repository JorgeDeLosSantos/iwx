@echo off
set "distpath=dist"
set "nanchiversion=0.1.0"
set "sdisttype=zip"
python setup.py sdist
REM cd %distpath%
REM pip install nanchi-%nanchiversion%.%sdisttype%^
pause
exit
