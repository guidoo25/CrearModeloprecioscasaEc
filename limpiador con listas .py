import pandas as pd
import numpy as np
from ast import literal_eval
import re


df_casa = pd.read_csv('casa.csv')
df_casa = pd.read_csv('casa.csv', sep=';')
df_casas2 = pd.read_csv('casa.csv', sep=';', converters={'detalle_adicional':literal_eval})
df_casa.head()

#funcion para identifciar en los detalles si tiene baños dormitorios  etc
def match_property (property,patterns):
    for pat in patterns:
        match_prop = re.search(pat,property)
        if match_prop:
            return True
        return False
    
def check_property (property,patterns):
   for pat in patterns:
        check = re.search(pat,property)
        if check:
            return 1
        return 0
   
def get_number(property):
    nums = re.findall(r'\d+',property)
    if len(nums) == 2:
        return int(nums[0]+nums[1])
    else:
        return int(nums[0])
    
def get_seguridad(fetaures):
    for prop in fetaures:
        if match_property(prop.lower().strip(),['seguridad','guardianía','guardia']):
            return (check_property(prop.lower().strip(),['seguridad','guardianía','guardia']))

def get_piscina(fetaures):
    for prop in fetaures:
        if match_property(prop.lower().strip(),['piscina']):
            return (check_property(prop.lower().strip(),['piscina']))
def get_banos(fetaures):
    for prop in fetaures:
        if match_property(prop.lower().strip(),['baño','baños']):
            return (get_number(prop.lower().strip()))
def get_terraza(fetaures):
    for prop in fetaures:
        if match_property(prop.lower().strip(),['terraza']):
            return (check_property(prop.lower().strip(),['terraza']))
        

df_casa['detalle_adicional;;;;;'] = df_casa['detalle_adicional;;;;;'].fillna('')
df_casa['seguridad'] = df_casa['detalle_adicional;;;;;'].apply(get_seguridad)  
df_casa['piscina'] = df_casa['detalle_adicional;;;;;'].apply(get_piscina)     
df_casa['terraza'] = df_casa['detalle_adicional;;;;;'].apply(get_terraza)
df_casa['baños'] = df_casa['detalle_adicional;;;;;'].apply(get_banos)

df_casa.drop(['detalle_adicional;;;;;'], axis=1, inplace=True)