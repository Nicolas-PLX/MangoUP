import sys
from PySide6.QtWidgets import QApplication
import Launcher.launcher as launcher
from Launcher.model import Model
from Save.configjson import load_json, save_json

try:
    if sys.argv[1] != None :
        ### TODO: version avec GUI
        pass
except IndexError:
        pass
        
        ### TODO : version sans GUI
        

app = QApplication(sys.argv)

l = launcher.Launcher(app)
l.show()
sys.exit(app.exec())

#l.launch()
"""
data = load_json("../saves/test.json")
save_json("../saves/save.json",data)
"""