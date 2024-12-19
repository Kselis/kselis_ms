import pandas as pd
import os

def save(file_nme,df):
    df.to_csv(file_nme,index=False)
    print("File Saved successfully")

def open(file_nme):
    df = pd.read_csv(file_nme)
    return df 

def create(file_name):
    data_crt={
        "Key":range(1,2)
    }
    df_crt=pd.DataFrame(data_crt)
    if os.path.exists(file_name):
        conf_crt=input("A file with this name already exists! wanna overwrite ? (y/n) ")
        if conf_crt.lower() == "y":
            df_crt.to_csv(file_name)
            print("File Overwritten!")
        else:
            return None
    else:
        df_crt.to_csv(file_name)
        print("File Created !")





