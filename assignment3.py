import argparse
import maya.standalone
maya.standalone.initialize()
import maya.cmds

parser = argparse.ArgumentParser()
parser.add_argument('-r', '--radius')
parser.add_argument('-c', '--Rcolor')
parser.add_argument('-g', '--Gcolor')
parser.add_argument('-b', '--Bcolor')

args = parser.parse_args()

print("Creating a planet.")

if not args.radius:
	size=input("What size planet do you want?")
if not args.Rcolor:
	color1=input("What percentage of red do you want?")
if not args.Gcolor:
	color2=input("What percentage of green do you want?")
if not args.Bcolor:
	color3=input("What percentage of blue do you want?")

args.radius = float(size)
args.Rcolor = float(color1)
args.Gcolor = float(color2)
args.Bcolor = float(color3)
planetLambert = cmds.shadingNode('lambert', asShader=True)
maya.cmds.setAttr((planetLambert + '.color'), (args.Rcolor),(args.Gcolor),(args.Bcolor), type = 'double3')
maya.cmds.polySphere(radius=args.radius)
maya.cmds.hyperShade(assign=planetLambert)
maya.cmds.file(rename=r"C:\Users\starr\Desktop\School\Animation\Anim435\anim-435-2024-sp3628\example.mb")
maya.cmds.file(save=True)

print("Created a planet.")