"""
Create camera

This script allows the user to select a camera from a list of options and will create a matching camera in the scene.
"""
import maya.cmds as cmds
import csv
from csv import DictReader
from functools import partial
import logging
import time
logger = logging.getLogger(__name__)

frmt = "[%(asctime)s][%(filename)s][%(levelname)s] %(msg)s"
    
logging.basicConfig(filename='log.txt', level=logging.INFO, format=frmt)
logger.info("Started")

def createCam(camStats,*args):
    """
    Creates a camera based on the selected camera's data
    
    Args:
        camStats (list): list containing selected camera stats ordered horizontal apeture, vertical apeture, focal length
    
    Returns:
        None
    """
    logger.info("Creating camera.")
    cmds.camera(hfa=camStats[0],vfa=camStats[1],fl=camStats[2])
    logger.info("Camera created successfully.")
    
def loadList():
    """
    Loads camera csv located in project workspace
    
    Args:
        None
    
    Returns:
        CamList: csv file containing camera options and their specs
    """
    logger.info("Loading camera options.")
    wksp = cmds.workspace(q=True, dir=True)
    try:
        camList = open(r"{}\cameras.csv".format(wksp))
    except:
        logger.error("Required cameras.csv file not found at " + wksp + " Please refer to README for more information.")
        quit()
    logger.info("Camera options successfully loaded.")
    return camList
    
def createWindow(camList):
    """
    Creates maya UI containing dynamic buttons based on loaded csv
    
    Args:
        camList (file): list of cameras
    
    Returns:
        None
    """
    logger.info("Creating user interface.")
    mainWin = cmds.window(title="Create camera")
    col_layout = cmds.columnLayout(parent=mainWin)
    cmds.text(parent=col_layout,label="Choose your camera:")
    camData = {}
    for row in DictReader(camList):
        try:
            camData[row.get("camera")] = [float(row.get("horizontal aperture (mm)")),float(row.get("vertical aperture (mm)")),float(row.get("focal length (mm)"))]
            cmds.button(parent=col_layout,label=row.get("camera"),command=partial(createCam,camData[row.get("camera")]))
        except:
            logger.warning(row.get("camera") + " is missing data. Please amend csv file.")
    cmds.showWindow(mainWin)
    logger.info("User interface successfully created.")

camList = loadList()
createWindow(camList)
    