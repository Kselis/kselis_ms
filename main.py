import pandas as pd
import argparse as arg
import functions as fn

file_nme=str()
data_frame,df=None,None

while True:
    query = input(">_ ").lower()
    
    commands = {
        "create" : "None",
        "open" : "None",
        "display" : "None",
        "delete" : "None",
        "update" : "None",
        "insert" : "None",
        "save" : "None",
        "close" : "None"
    }

    if(len(query.split())>0) and (query.split()[0] in commands.keys()):
        print(commands[query.split()[0]])
    else:
        continue