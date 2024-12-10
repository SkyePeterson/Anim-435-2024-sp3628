# Create Camera Tool
## Overview
This tool creates a new camera in the scene that emulates the filmback size and focal length of a selected type of camera.

## Usage
Running the python script in maya will create a UI containing a list of camera options. Select the camera used in your shoot and the script will create a new camera at 0x0x0 emulating the the selected camera. The folder this README is in also contains a maya scene, a maya workspace file, and a csv file for testing purposes.

A csv file by the name of "cameras.csv" must be in the root of your maya workpace, and that csv must contain the headers "camera", "horizontal aperture (mm)", "vertical aperture (mm)", and "focal length (mm)". The camera options listed in "cameras.csv" may be freely modified as long as they follow the formatting specified by the headers.

## Potential bugs
The script may get directed to the wrong folder for your workspace. I'm not sure why this happens. You can either move "cameras.csv" to the folder directory listed in the error message and rerun the script, or open a menu that contains a file explorer such as "file > save as..." and navigate to the workspace root before closing. I'm not sure why that works.
