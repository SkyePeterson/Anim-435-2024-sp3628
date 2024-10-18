import maya.cmds as cmds
from functools import partial

def createPlanet(diam,colorR,colorG,colorB):
    planet = cmds.polySphere(radius=diam, n='newPlanet')
    planetLambert = cmds.shadingNode('lambert', asShader=True)
    cmds.setAttr((planetLambert + '.color'), (colorR/255),(colorG/255),(colorB/255), type = 'double3')
    cmds.select(planet)
    cmds.hyperShade(assign=planetLambert)
    
def buttonPress(size_input, colorR, colorG, colorB, *args):
    diam = cmds.intField(size_input,q=True,v=1)
    R = cmds.intField(colorR,q=True,v=1)
    G = cmds.intField(colorG,q=True,v=1)
    B = cmds.intField(colorB,q=True,v=1)
    createPlanet(diam,R,G,B)

def createWindow():
    mainWin = cmds.window(title="Create Planet")
    col_layout = cmds.columnLayout(parent=mainWin)
    size_row_layout = cmds.rowLayout(numberOfColumns=2,parent=col_layout)
    size_label = cmds.text(parent=size_row_layout,label="Diameter of planet: ")
    size_input = cmds.intField(parent=size_row_layout)
    color_row_layout_header = cmds.rowLayout(numberOfColumns=1,parent=col_layout)
    color_label_header = cmds.text(parent=color_row_layout_header,label="Color")
    color_row_layout_R = cmds.rowLayout(numberOfColumns=2,parent=col_layout)
    color_label_R = cmds.text(parent=color_row_layout_R,label="R:")
    color_input_R = cmds.intField(parent=color_row_layout_R)
    color_row_layout_G = cmds.rowLayout(numberOfColumns=2,parent=col_layout)
    color_label_G = cmds.text(parent=color_row_layout_G,label="G:")
    color_input_G = cmds.intField(parent=color_row_layout_G)
    color_row_layout_B = cmds.rowLayout(numberOfColumns=2,parent=col_layout)
    color_label_B = cmds.text(parent=color_row_layout_B,label="B:")
    color_input_B = cmds.intField(parent=color_row_layout_B)
    button_row_layout = cmds.rowLayout(numberOfColumns=1,parent=col_layout)
    submit_button = cmds.button(parent=button_row_layout,label="Submit",command=partial(buttonPress, size_input, color_input_R, color_input_G, color_input_B))
    cmds.showWindow(mainWin)
    
createWindow()