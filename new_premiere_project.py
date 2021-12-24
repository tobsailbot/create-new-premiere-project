from ahk import AHK
import os
import sys

ahk = AHK()

cmd = sys.argv[1:] # tomar argumento

projName = ' '.join(cmd)
projDir = f'D:\\TOBI-PC\\Descargas\\3-VIDEO PROJECTS\\{projName}'

os.makedirs(projDir)
# print(f'se creo el proyecto: {projName}')

win = ahk.find_window(title=b'Adobe Premiere Pro')
win.activate()

ahk.send_input('^!n')
ahk.type(projName)
ahk.send_input('{Tab}{Tab}')
ahk.send_input('{Enter}')
ahk.type(projDir)
ahk.send_input('{Enter}{Enter}')
ahk.send_input('+{Tab}''+{Tab}''+{Tab}''+{Tab}')
ahk.send_input('{Enter}')

