cd %cd%
echo %cd%
pyinstaller -w %cd%\vat.py %cd%\vatgui.py %cd%\icon_rc.py -i %cd%\resource\gui\vat.ico
pause