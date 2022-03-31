import requests
from xml.dom import minidom
import pprint as pprint
from datetime import date
from datetime import datetime
class bbcr:
    def __init__(self):

        self.url =""

    def tipo_cambio_hoy(self):
        hoy=date.today()
        print(hoy.strftime('%d/%m/%Y'))
        fechainicial=hoy.strftime('%d/%m/%Y')
        fechafinal=hoy.strftime('%d/%m/%Y')
        url = "https://gee.bccr.fi.cr/Indicadores/Suscripciones/WS/wsindicadoreseconomicos.asmx/ObtenerIndicadoresEconomicos?Indicador=318&FechaInicio="+fechainicial+"&FechaFinal="+fechafinal+"&Nombre=Jose"
        payload={}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        root=minidom.parseString(response.text)
        valor = root.getElementsByTagName("NUM_VALOR")[0].firstChild.data
        resp={"valor":valor,"fecha":fechainicial}
        return resp

    def tipo_cambio_fecha(self,fecha):
        print(fecha)
        date_str = fecha
        format_str = '%Y/%m/%d' # The format
        datetime_obj = datetime.strptime(date_str, format_str)    
        print(datetime_obj)
        print(type(datetime_obj))
        hoy=datetime_obj
        print(hoy.strftime('%d/%m/%Y'))
        fechainicial=hoy.strftime('%d/%m/%Y')
        fechafinal=hoy.strftime('%d/%m/%Y')
        url = "https://gee.bccr.fi.cr/Indicadores/Suscripciones/WS/wsindicadoreseconomicos.asmx/ObtenerIndicadoresEconomicos?Indicador=318&FechaInicio="+fechainicial+"&FechaFinal="+fechafinal+"&Nombre=Jose"
        payload={}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        root=minidom.parseString(response.text)
        valor = root.getElementsByTagName("NUM_VALOR")[0].firstChild.data
        resp={"valor":valor,"fecha":fechainicial}
        return resp
    print(tipo_cambio_hoy)
