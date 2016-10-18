from PyQt4 import uic

fin = open('TRAINcolour.ui','r')
fout = open('TRAINcolour_ui.py','w')
uic.compileUi(fin,fout,execute=False)
fin.close()
fout.close()