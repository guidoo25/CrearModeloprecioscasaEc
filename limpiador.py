#LIMPIADOR CON CADENAS DE TEXTO

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
    nums = re.findall(r'\d+', property)
    if len(nums) == 2:
        return int(nums[0]+nums[1])
    elif len(nums) == 1:
        return int(nums[0])
    else:
        return 0
    
def get_numberba(property):
    nums = re.findall(r'\d+', property)
    if nums: 
        return int(nums[0])  
    else:
        return 0  
    
def get_seguridad(features):
    features = features.lower().strip()
    if match_property(features, ['seguridad', 'guardianía', 'guardia']):
        return 1
    else:
        return 0
def get_banos(features):
    features = features.lower().strip()
    if match_property(features, ['baño', 'baños']):
        return get_numberba(features)
    else:
        return 0


def get_piscina(fetaures):
    for prop in fetaures:
        if match_property(prop.lower().strip(),['piscina']):
              return 1
        else:
            return 0
def get_parqueo(fetaures):
    for prop in fetaures:
        if match_property(fetaures,['parqueo','garaje']):
           return 1
        else:
            return 0

def get_terraza(fetaures):
    for prop in fetaures:
        if match_property(fetaures,['terraza']):
           return 1
        else:
            return 0
        
def get_financiamiento(fetaures):
    for prop in fetaures:
        if match_property(fetaures,['financiamiento','credito',]):
           return 1
        else:
            return 0
def get_zon_comercial(fetaures):
    for prop in fetaures:
        if match_property(fetaures,['comercial','zona comercial']):
           return 1
        else:
            return 0

df_casa['detalle_adicional;;;;;'] = df_casa['detalle_adicional;;;;;'].fillna('')
df_casa['seguridad'] = df_casa['detalle_adicional;;;;;'].apply(get_seguridad)  
df_casa['piscina'] = df_casa['detalle_adicional;;;;;'].apply(get_piscina)     
df_casa['terraza'] = df_casa['detalle_adicional;;;;;'].apply(get_terraza)
df_casa['baños'] = df_casa['detalle_adicional;;;;;'].apply(get_banos)
df_casa['parqueo'] = df_casa['detalle_adicional;;;;;'].apply(get_parqueo)
df_casa['financiamiento'] = df_casa['detalle_adicional;;;;;'].apply(get_financiamiento)
df_casa['zon_comercial'] = df_casa['detalle_adicional;;;;;'].apply(get_zon_comercial)

df_casa.drop(['detalle_adicional;;;;;'], axis=1, inplace=True)

df_casa = df_casa[df_casa['metrajeconstruc'] != '']