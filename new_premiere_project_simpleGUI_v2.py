from ahk import AHK
import os
import easygui as eg
import subprocess
import time
import pymiere


ahk = AHK()

campos = ['Project Name', 'Project Path', 'Media Folder 1','Media Folder 2','Media Folder 3']
default = ['',r'D:\TOBI-PC\Descargas\3-VIDEO PROJECTS',r'F:\VIDEO MEDIA\OBS VIDEOS',r'D:\TOBI-PC\Descargas\3-VIDEO PROJECTS\1.VIDEO EDITING RESOURCES\SOUNDS\SOUND FX',r'D:\TOBI-PC\Descargas\3-VIDEO PROJECTS\1.VIDEO EDITING RESOURCES\MEDIA\EMOJIS PNG']
template = r'D:\TOBI-PC\Descargas\3-VIDEO PROJECTS\1.VIDEO EDITING RESOURCES\RESOURCES PROY TEMPLATE.prproj'

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

# open the template project
ahk.send_input('^o')
ahk.type(template)
ahk.send_input('{Enter}')


time.sleep(2.5)

# save project as
win.activate()
ahk.send_input('^+s')
time.sleep(0.5)
ahk.type(projDir)
ahk.send_input('{Enter}')
ahk.type(projName)
ahk.send_input('{Enter}')

time.sleep(0.5)

# rename the active sequence
seq = pymiere.objects.app.project.activeSequence
seq.name = projName


time.sleep(0.5)

# open the media folders
subprocess.Popen(f'explorer "{box[2]}"')
subprocess.Popen(f'explorer "{box[3]}"')
subprocess.Popen(f'explorer "{box[4]}"')



