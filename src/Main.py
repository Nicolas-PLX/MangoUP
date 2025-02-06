import sys
import Launcher.launcher as launcher
from Launcher.model import Model


try:
    if sys.argv[1] != None :
        l = launcher.Launcher()
        l.launch()
except IndexError:
        ### TODO : version sans GUI
        pass

l = launcher.Launcher()
l.launch()
print("popo")