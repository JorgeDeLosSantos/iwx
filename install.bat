@echo off
echo Building iwx, wxPython required.
set "packname=iwx"
set "distpath=dist"
set "packversion=0.1.0"
set "sdisttype=zip"
python setup.py sdist
pip install -U %cd%/%distpath%/%packname%-%packversion%.%sdisttype%
pause
exit
