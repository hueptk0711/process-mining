import os, sys
import pandas as pd
from profit.process_map import ProcessMap 

path = "Data\PermitLog.xes"

def main():
    
    pm = ProcessMap()
    pm.set_log(FILE_PATH=path)
    pm.set_rates(90, 15)
    pm.set_params(optimize=False, aggregate=False)
    pm.update()
    pm.render(show_only=True, save_path= "Result/PermitLog.png")

main()