#!/usr/bin/env python

"""Aggiorna la vista materializzata"""

__author__      = "Roberto Marzocchi"
__copyright__   = "Gter srl"


import os    # standard library
import sys

import requests  # 3rd party packages
import json

import psycopg2
from credenziali import *
conn = psycopg2.connect("dbname={} user={} password={} host={}".format(db, user, pwd, ip))
cur=conn.cursor()



# recupero il percorso allo script python 
spath=os.path.dirname(os.path.realpath(__file__)) 
# la sottocartella log deve esserci e possibilmente inseritanel file .gitignore 

# libreria per gestione log
import logging
# inserire riferimento a data e schema 


logging.basicConfig(     
    format='%(asctime)s\t%(levelname)s\t%(message)s',
    filemode='w', # overwrite or append 
    filename='{}/log/refresh_mv.log'.format(spath),  # nome file (commentandolo viene stampato a schermo
    level=logging.DEBUG
    )



query1=u'refresh materialized view terra.mv_statistiche_totali_telecamere_100;'
try:
    cur.execute(query1)
    conn.commit()
except Exception as e1:
    logging.error(e)
    conn.rollback()
        


cur.close()
conn.close()
    


logging.info('Ho finito. refresh materialized view terra.mv_statistiche_totali_telecamere_100')
