from ahk import AHK
import os
import easygui as eg
import subprocess
import time


ahk = AHK()

campos = ['Project Name', 'Project Path', 'Media Folder 1','Media Folder 2','Media Folder 3']
datos = []
default = ['',r'D:\TOBI-PC\Descargas\3-VIDEO PROJECTS',r'F:\VIDEO MEDIA\OBS VIDEOS',r'D:\TOBI-PC\Descargas\3-VIDEO PROJECTS\1.VIDEO EDITING RESOURCES\SOUNDS\SOUND FX',r'D:\TOBI-PC\Descargas\3-VIDEO PROJECTS\1.VIDEO EDITING RESOURCES\MEDIA\EMOJIS PNG']

# creates a window with multiple input boxes
box = eg.multenterbox(msg='Enter the name and folders:',title='New Premiere Project',fields=campos, values=default)


projName = box[0]
Dir = box[1]
projDir = Dir+f'\\{projName}'

print(projName)
print(projDir)

# creates a new directory 
os.makedirs(projDir)

print(f'se creo el proyecto: {projName}')

# checks for the window title
win = ahk.find_window(title=b'Adobe Premiere Pro')
win.activate()

# creates a new project and select the folder
ahk.send_input('^!n')
ahk.type(projName)
ahk.send_input('{Tab}{Tab}')
ahk.send_input('{Enter}')
ahk.type(projDir)
ahk.send_input('{Enter}{Enter}')
ahk.send_input('+{Tab}''+{Tab}''+{Tab}''+{Tab}')
ahk.send_input('{Enter}')

time.sleep(3)

# creates a new sequence
win.activate()
ahk.send_input('^n')
ahk.type(projName)
ahk.send_input('{Enter}')



# open the media folders
subprocess.Popen(f'explorer "{box[2]}"')
subprocess.Popen(f'explorer "{box[3]}"')
subprocess.Popen(f'explorer "{box[4]}"')