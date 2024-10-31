"""
Create camera

This script allows the user to select a camera from a list of options and will create a matching camera in the scene.
"""
import maya.cmds as cmds
import csv
from csv import DictReader
from functools import partial

def createCam(camStats,*args):
    """
    Creates a camera based on the selected camera's data
    
    Args:
        camStats (list): list containing selected camera stats ordered horizontal apeture, vertical apeture, focal length
    
    Returns:
        None
    """
    print("Creating camera.")
    cmds.camera(hfa=camStats[0],vfa=camStats[1],fl=camStats[2])
    print("Camera created successfully.")
    
def loadList():
    """
    Loads camera csv located in project workspace
    
    Args:
        None
    
    Returns:
        CamList: csv file containing camera options and their specs
    """
    print("Loading camera options.")
    wksp = cmds.workspace(q=True, dir=True)
    print(wksp)
    camList = open(r"{}\cameras.csv".format(wksp))
    print("Camera options successfully loaded.")
    return camList
    
def createWindow(camList):
    """
    Creates maya UI containing dynamic buttons based on loaded csv
    
    Args:
        camList (file): list of cameras
    
    Returns:
        None
    """
    mainWin = cmds.window(title="Create camera")
    col_layout = cmds.columnLayout(parent=mainWin)
    cmds.text(parent=col_layout,label="Choose your camera:")
    camData = {}
    for row in DictReader(camList):
        camData[row.get("camera")] = [float(row.get("horizontal aperture (mm)")),float(row.get("vertical aperture (mm)")),float(row.get("focal length (mm)"))]
        cmds.button(parent=col_layout,label=row.get("camera"),command=partial(createCam,camData[row.get("camera")]))
    cmds.showWindow(mainWin)

camList = loadList()
createWindow(camList)
    