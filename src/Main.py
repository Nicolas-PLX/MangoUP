import sys
import Launcher.launcher as launcher
from Launcher.model import Model
from Save.configjson import load_json, save_json

try:
    if sys.argv[1] != None :
        l = launcher.Launcher()
        l.launch()
except IndexError:
        ### TODO : version sans GUI
        pass

l = launcher.Launcher()
l.launch()


"""
data = load_json("../saves/test.json")
save_json("../saves/save.json",data)
"""