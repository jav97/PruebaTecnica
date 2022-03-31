import pandas as pd
import requests 
from datetime import date
from datetime import datetime
import matplotlib.pyplot as plt

URL = 'https://gee.bccr.fi.cr/Indicadores/Suscripciones/WS/wsindicadoreseconomicos.asmx/ObtenerIndicadoresEconomicos'
COD_INDICADORINTERNO = 318


hoy=date.today()
fechaInicio=hoy.strftime('01/01/2022')
fechaFin=hoy.strftime('31/12/2022')
url = URL+"&fechaInicio="+fechaInicio+"&fechaFin="+fechaFin+"&Nombre=Javier+Chavez"
payload={}
headers = {}
response = requests.get(f"{URL}", headers= headers, data=payload)



# DES_FECHA, NUM_VALOR = plt.subplots()
# NUM_VALOR.plot([], [])

# plt.show()

print(response.json())
print(response.status_code)