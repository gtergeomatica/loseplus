# Descrizione

Script per importare i dati dai WS di TEAS su geoDB Lose+

## Dipendenze 

sudo pip3 install psycopg2


# Note 
Va creato file accessorio credenziali.py contiene credenziali di accesso a DB e WS TEAS

```
ip='localhost'
db='XXXXXXX'
user='XXXXXXX'
	@@ -15,5 +15,5 @@ port='5432'
ws_user='XXXXXXX'
ws_pwd='XXXXXXX'
```

# lettura WS TEAS
10 *    * * *  omdusr   /usr/bin/python3 /home/omdusr/loseplus/ws_telecamere.py  > /dev/null 2>&1
