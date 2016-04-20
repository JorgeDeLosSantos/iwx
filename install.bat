@echo off
echo Building iwx, wxPython required.
REM set "distpath=dist"
REM set "nanchiversion=0.1.0"
REM set "sdisttype=zip"
python setup.py sdist
REM cd %distpath%
REM pip install nanchi-%nanchiversion%.%sdisttype%
pause
exit
