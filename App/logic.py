import time

import csv

import os

from DataStructures.List import single_linked_list as sl
from DataStructures.List import array_list as al


data_dir = os.path.dirname(os.path.realpath('__file__')) + '/Data/'

csv.field_size_limit(2147483647)

def new_logic():
    """
    Crea el catalogo para almacenar las estructuras de datos
    """
    #TODO: Llama a las funciónes de creación de las estructuras de datos
    
    catalog = {'source': None,
               'commodity': None,
               'statical_category': None,
               'unit_measurement': None,
               'state_name': None,
               'location': None,
               'year_collection': None,
               'freq_collection': None,
               'reference_period': None,
               'load_time': None,
               'value': None}

    catalog['source'] = al.new_list()
    catalog['commodity'] = al.new_list()
    catalog['statical_category'] = al.new_list()
    catalog['unit_measurement'] = al.new_list()
    catalog['state_name'] = al.new_list()
    catalog["location"] = al.new_list()
    catalog["year_collection"] = al.new_list()
    catalog["freq_collection"] = al.new_list()
    catalog["reference_period"] = al.new_list()
    catalog["load_time"] = al.new_list()
    catalog["value"] = al.new_list()
    return catalog

def datos():
    """
    Crea una lista nativa de python por columna del archivo CSV, y la añade a un diccionario base, desde el cual se va a 
    pasar a llenar el catálogo.
    """
    
    doc=(data_dir+"agricultural-100.csv")
    
    diccionario_base={}
    
    datos=open(doc,encoding="utf-8")
    lector=csv.reader(datos)
    columnas=next(lector)
    
    for columna in columnas:
        diccionario_base[columna]=[]
    
    for fila in lector:
        for i in range (len(columnas)):
            llave=columnas[i]
            dato=fila[i]
            diccionario_base[llave].append(dato)
            
    datos.close()
    
    return diccionario_base

# Funciones para la carga de datos
def carga(datos,catalog,columna:str):
    for i in datos[columna]:
        al.add_last(catalog[columna],i)

def load_data(catalog, datos):
    """
    Carga los datos del DataFrame en el catálogo.
    """
    carga(datos, catalog, 'source')
    
    source_size = catalog["source"]["size"]
    
    carga(datos, catalog, 'commodity')
    carga(datos, catalog, 'statical_category')
    carga(datos, catalog, 'unit_measurement')
    carga(datos, catalog, 'state_name')
    carga(datos, catalog, 'location')
    carga(datos, catalog, 'year_collection')
    carga(datos, catalog, 'freq_collection')
    carga(datos, catalog, 'reference_period')
    carga(datos, catalog, 'load_time')
    carga(datos, catalog, 'value')
    
    return source_size

def lesser_year(catalog):
    año=catalog["year_collection"]["elements"][0]
    for i in catalog["year_collection"]["elements"]:
        if i < año:
            año = i
    return año

def greater_year(catalog):
    año=catalog["year_collection"]["elements"][0]
    for i in catalog["year_collection"]["elements"]:
        if i > año:
            año = i
    return año

def primeros(catalog):
    lista_retorno=al.new_list()
    ordenados = al.new_list()
    ordenados2 = al.new_list()
    
    for i in range(0, 5):
        al.add_last(ordenados, catalog["load_time"]["elements"][i])
    al.merge_sort(ordenados, False)
    for j in range(0, 5):
        if j < ordenados["size"]-1 and ordenados["elements"][j] == ordenados["elements"][j+1]:
            for i in range(0, 5):
                if ordenados["elements"][j] == catalog["load_time"]["elements"][i]:
                    al.add_last(ordenados2, catalog["state_name"]["elements"][i])
            al.merge_sort(ordenados2, True)
            for l in range(ordenados2["size"]-1):
                for k in range(0, 5):
                    if ordenados2["elements"][l] == catalog["state_name"]["elements"][k]:
                        info = { 
                            "source": catalog["source"]["elements"][j],
                            "unit_measurement": catalog["unit_measurement"]["elements"][j],
                            "state_name": catalog["state_name"]["elements"][j],
                            "year_collection": catalog["year_collection"]["elements"][j],
                            "freq_collection": catalog["freq_collection"]["elements"][j],
                            "load_time": catalog["load_time"]["elements"][j],
                            "value": catalog["value"]["elements"][j]
                            }
                        if info not in lista_retorno["elements"]:
                            al.add_last(lista_retorno, info)
            j += ordenados2["size"] 
            ordenados2 = al.new_list()

        else:
            for i in range(0, 5):
                if ordenados["elements"][j] == catalog["load_time"]["elements"][i]:
                    info = { 
                        "source": catalog["source"]["elements"][j],
                        "unit_measurement": catalog["unit_measurement"]["elements"][j],
                        "state_name": catalog["state_name"]["elements"][j],
                        "year_collection": catalog["year_collection"]["elements"][j],
                        "freq_collection": catalog["freq_collection"]["elements"][j],
                        "load_time": catalog["load_time"]["elements"][j],
                        "value": catalog["value"]["elements"][j]
                    }
                    if info not in lista_retorno["elements"]:
                        al.add_last(lista_retorno, info)   
    return lista_retorno

def ultimos(catalog):
    lista_retorno = al.new_list()
    ordenados = al.new_list()
    ordenados2 = al.new_list()
    tamaño = catalog["load_time"]["size"]
    
    for i in range(tamaño - 5, tamaño):
        al.add_last(ordenados, catalog["load_time"]["elements"][i])
    al.merge_sort(ordenados, False)  
    for j in range(0, 5):
        if j < ordenados["size"] - 1 and ordenados["elements"][j] == ordenados["elements"][j + 1]:
            for i in range(tamaño - 5, tamaño):
                if ordenados["elements"][j] == catalog["load_time"]["elements"][i]:
                    al.add_last(ordenados2, catalog["state_name"]["elements"][i])
            al.merge_sort(ordenados2, True)  
            for l in range(0, ordenados2["size"]):
                for k in range(tamaño - 5, tamaño):
                    if catalog["state_name"]["elements"][k] == ordenados2["elements"][l]:
                        info = {
                            "source": catalog["source"]["elements"][k],
                            "unit_measurement": catalog["unit_measurement"]["elements"][k],
                            "state_name": catalog["state_name"]["elements"][k],
                            "year_collection": catalog["year_collection"]["elements"][k],
                            "freq_collection": catalog["freq_collection"]["elements"][k],
                            "load_time": catalog["load_time"]["elements"][k],
                            "value": catalog["value"]["elements"][k]
                        }
                        if info not in lista_retorno["elements"]:
                            al.add_last(lista_retorno, info)
            j += ordenados2["size"] - 1
            ordenados2 = al.new_list()
        
        else:
            for i in range(tamaño - 5, tamaño):
                if ordenados["elements"][j] == catalog["load_time"]["elements"][i]:
                    info = {
                        "source": catalog["source"]["elements"][i],
                        "unit_measurement": catalog["unit_measurement"]["elements"][i],
                        "state_name": catalog["state_name"]["elements"][i],
                        "year_collection": catalog["year_collection"]["elements"][i],
                        "freq_collection": catalog["freq_collection"]["elements"][i],
                        "load_time": catalog["load_time"]["elements"][i],
                        "value": catalog["value"]["elements"][i]
                    }
                    if info not in lista_retorno["elements"]:
                        al.add_last(lista_retorno, info)
    
    return lista_retorno
# Funciones de consulta sobre el catálogo

def get_data(catalog, id):
    """
    Retorna un dato por su ID.
    """
    #TODO: Consulta en las Llamar la función del modelo para obtener un dato
    pass


def req_1(catalog,anno):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    
    start_time=get_time()
    
    lista_fechas=al.new_list()
    info = {'source': None,
            'commodity': None,
               'unit_measurement': None,
               'state_name': None,
               'year_collection': None,
               'load_time': None,
               'value': None,}
    
    for i in range(catalog["year_collection"]["size"]):
        if catalog["year_collection"]["elements"][i] == str(anno):
            al.add_last(lista_fechas, catalog["load_time"]["elements"][i])
    al.merge_sort(lista_fechas, False)
    pasaron=al.size(lista_fechas)
    ultima=lista_fechas["elements"][0]
    
    for k in range(catalog["load_time"]["size"]):
        if (str(ultima) == catalog["load_time"]["elements"][k]) and (str(anno)==catalog["year_collection"]["elements"][k]):
            info["source"]=catalog["source"]["elements"][k]
            info["commodity"]=catalog["commodity"]["elements"][k]
            info["unit_measurement"]=catalog["unit_measurement"]["elements"][k]
            info["state_name"]=catalog["state_name"]["elements"][k]
            info["year_collection"]=catalog["year_collection"]["elements"][k]
            info["load_time"]=catalog["load_time"]["elements"][k]
            info["value"]=catalog["value"]["elements"][k]
    
    end_time=get_time()
    
    req_1_time=delta_time(start_time,end_time)
    
    return(info,req_1_time,pasaron)


def req_2(catalog):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    pass


def req_3(catalog, dep, year0, year):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    start_time = get_time()
    if year<year0:
        return "Por favor introduzca un intervalo de tiempo valido..."    
    lista_info = al.new_list()
    alt_info = al.new_list()
    ordenada = al.new_list()
    survey = 0
    census = 0
    info = {'source': None,
            'commodity': None,
               'unit_measurement': None,
               'year_collection': None,
               'freq_collection': None,
               'load_time': None}
    
    for i in range(catalog["state_name"]["size"]):
        if catalog["state_name"]["elements"][i] == str(dep) and year0 <= catalog["year_collection"]["elements"][i] <= year:
            if catalog["load_time"]["elements"][i] not in ordenada["elements"]:
                al.add_last(ordenada, catalog["load_time"]["elements"][i])
    al.merge_sort(ordenada, False)
    for j in range(ordenada["size"] - 1):    
        for i in range(catalog["load_time"]["size"] - 1):
            if catalog["load_time"]["elements"][i] == ordenada["elements"][j]:
                if catalog["state_name"]["elements"][i] == str(dep) and year0 <= catalog["year_collection"]["elements"][i] <= year:
                    info = { 
                    "source": catalog["source"]["elements"][i],
                    "commodity": catalog["commodity"]["elements"][i],
                    "unit_measurement": catalog["unit_measurement"]["elements"][i],
                    "year_collection": catalog["year_collection"]["elements"][i],
                    "freq_collection": catalog["freq_collection"]["elements"][i],
                    "load_time": catalog["load_time"]["elements"][i]
                    }
                    al.add_last(lista_info, info)
                    if catalog["source"]["elements"][i] == "CENSUS":
                        census += 1
                    if catalog["source"]["elements"][i] == "SURVEY":
                        survey += 1
    tamaño = al.size(lista_info)
    if tamaño > 20:
        for i in range(0, 5):
            al.add_last(alt_info, lista_info["elements"][i])
        for k in range(tamaño - 5, tamaño):
            al.add_last(alt_info, lista_info["elements"][k])
        end_time=get_time()
        req_3_time=delta_time(start_time,end_time)
        return (alt_info, survey, census, tamaño, req_3_time)
    else:
        end_time=get_time()
        req_3_time=delta_time(start_time,end_time)
        return (lista_info, survey, census, tamaño, req_3_time)


def req_4(catalog, product, ai, af):
    """
    Retorna el resultado del requerimiento 4
    """
    start_time = get_time()
    
    if af < ai:
        return "Ingrese un intervalo de tiempo válido"
    
    filtro = al.new_list()
    ans = al.new_list()
    registros = 0
    survey = 0
    census = 0
    
    for i in range(catalog["commodity"]["size"]):
        if (catalog["commodity"]["elements"][i] == product and ai <= catalog["year_collection"]["elements"][i] <= af):
            year = catalog["year_collection"]["elements"][i]
            if year not in filtro["elements"]:
                al.add_last(filtro, year)
    
    al.selection_sort(filtro, False) 
    
    for year in filtro["elements"]:
        for i in range(catalog["commodity"]["size"]):
            if (catalog["commodity"]["elements"][i] == product and ai <= catalog["year_collection"]["elements"][i] <= af and catalog["year_collection"]["elements"][i] == year):
                info = {
                    "source": catalog["source"]["elements"][i],
                    "year_collection": catalog["year_collection"]["elements"][i],
                    "load_time": catalog["load_time"]["elements"][i],
                    "freq_collection": catalog["freq_collection"]["elements"][i],
                    "state_name": catalog["state_name"]["elements"][i],
                    "unit_measurement": catalog["unit_measurement"]["elements"][i]
                }
                
                al.add_last(ans, info)
                
                if catalog["source"]["elements"][i] == "SURVEY":
                    survey += 1
                else:
                    census += 1
                registros += 1
    
    if ans["size"] > 20:
        sub_list = al.new_list()
        for i in range(0,5):
            al.add_last(sub_list,ans["elements"][i])
        for i in range(ans["size"]-5,ans["size"]):
            al.add_last(sub_list,ans["elements"][i])
        end_time = get_time()
        time = delta_time(start_time,end_time)
        return sub_list["elements"],survey,census,registros,time
        
    
    
    end_time = get_time()
    time = delta_time(start_time,end_time)
    return ans["elements"],survey,census,registros,time

def req_5(catalog):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    pass

def req_6(catalog, dep, ai, af):
    """
    Retorna el resultado del requerimiento 6
    """
    start_time = get_time()
    organized = al.new_list()
    ans = al.new_list()
    registros = 0
    survey = 0
    census = 0
    
    for i in range(catalog["load_time"]["size"]):
        load_time = catalog["load_time"]["elements"][i][:10]
        if (catalog["state_name"]["elements"][i] == dep and ai <= load_time <= af):
            if load_time not in organized["elements"]:
                al.add_last(organized, load_time)
                
    al.merge_sort(organized, False)
    
    for load_time in organized["elements"]:
        for i in range(catalog["load_time"]["size"]):
            current_time = catalog["load_time"]["elements"][i][:10]
            if (catalog["state_name"]["elements"][i] == dep and ai <= current_time <= af and current_time == load_time):
                info = {
                    "source": catalog["source"]["elements"][i],
                    "year_collection": catalog["year_collection"]["elements"][i],
                    "load_time": catalog["load_time"]["elements"][i],
                    "freq_collection": catalog["freq_collection"]["elements"][i],
                    "state_name": catalog["state_name"]["elements"][i],
                    "unit_measurement": catalog["unit_measurement"]["elements"][i],
                    "commodity": catalog["commodity"]["elements"][i]
                }
                al.add_last(ans, info)
                
                if catalog["source"]["elements"][i] == "SURVEY":
                    survey += 1
                else:
                    census += 1
                registros += 1
    
    if ans["size"] > 20:
        sub_list = al.new_list()
        for i in range(0,5):
            al.add_last(sub_list,ans["elements"][i])
        for i in range(ans["size"]-5,ans["size"]):
            al.add_last(sub_list,ans["elements"][i])
        end_time = get_time()
        time = delta_time(start_time,end_time)
        return sub_list["elements"],survey,census,registros,time

    end_time = get_time()
    time = delta_time(start_time,end_time)
    return ans["elements"],survey,census,registros,time
                
def req_7(catalog, dep, year0, year, ord):
    
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    start_time = get_time()
    if year<year0:
        return "Por favor introduzca un intervalo de tiempo valido..."
    if ord == "ASCENDENTE":
        ord = True
    else:
        ord = False
    filtro = 0
    invalid = 0
    ingresos = 0
    survey = 0
    census = 0
    t_filtro = 0
    maxx = None
    minn = None
    lista_temp = al.new_list()
    ordenados = al.new_list()
    ordenados2 = al.new_list()
    lista_retorno = al.new_list()
    alt_list = al.new_list()
    info = {
        "año": None,
        "ingresos": None,
        "filtro": None,
        "invalidos": None,
        "survey": None,
        "census": None,
        "tipo": None
    }
    anio0 = int(year0)
    anio = int(year)
    for i in range(anio0, anio):
        for j in range(catalog["year_collection"]["size"]-1):
             if int(catalog["year_collection"]["elements"][j]) == i and catalog["state_name"]["elements"][j] == str(dep):
                 if catalog["unit_measurement"]["elements"][j] == "$":
                     filtro += 1
                     if catalog["source"]["elements"][j] == "SURVEY":
                         survey += 1
                     else:
                         census +=1
                     if catalog["value"]["elements"][j] == "(D)":
                         invalid += 1
                     else:
                         ingresos = str(catalog["value"]["elements"][j])
        info = {
            "año": i,
            "ingresos": ingresos,
            "filtro": filtro,
            "invalidos": invalid,
            "survey": survey,
            "census": census,
            "tipo": None
        }
        al.add_last(lista_temp, info)
        filtro = 0
        invalid = 0
        ingresos = 0
        survey = 0
        census = 0
    for i in range(lista_temp["size"]-1):
        t_filtro += lista_temp["elements"][i]["filtro"]
        al.add_last(ordenados, str(lista_temp["elements"][i]["ingresos"]))
    al.merge_sort(ordenados, ord)
    if ord == True:
        minn = ordenados["elements"][0]
        maxx = ordenados["elements"][-1]
    else:
        maxx = ordenados["elements"][0]
        minn = ordenados["elements"][-1]
    for i in range(lista_temp["size"]-1):
        if lista_temp["elements"][i]["ingresos"] == maxx:
            lista_temp["elements"][i]["tipo"] == "MAXIMO"
        elif lista_temp["elements"][i]["ingresos"] == minn:
            lista_temp["elements"][i]["tipo"] == "MINIMO"
    for i in range(ordenados["size"]-1):
        if i < ordenados["size"] and ordenados["elements"][i] == ordenados["elements"][i+1]:
            inicio = i
            for j in range(lista_temp["size"]-1):
                if lista_temp["elements"][j]["ingresos"] == ordenados["elements"][i]:
                    al.add_last(ordenados2, lista_temp["elements"][j]["filtro"])
            al.merge_sort(ordenados2, ord)
            for l in range(inicio, ordenados2["size"]-1):
                for k in range(lista_temp["size"]-1):
                    if ordenados2["elements"][l] == lista_temp["elements"][k]["filtro"]:
                        al.add_last(lista_retorno, lista_temp["elements"][k])
            i += ordenados2["size"] - 1 
            ordenados2 = al.new_list()
        else:
            al.add_last(lista_retorno, lista_temp["elements"][i])
    pasaron = al.size(lista_retorno)
    if pasaron > 15:
        for i in range(0, 5):
            al.add_last(alt_list, lista_retorno["elements"][i])
        for i in range(pasaron - 5, pasaron):
            al.add_last(alt_list, lista_retorno["elements"][i])
        end_time = get_time()
        req_7_time = delta_time(start_time, end_time)
        return t_filtro, alt_list, req_7_time 
    else:
        end_time = get_time()
        req_7_time = delta_time(start_time, end_time)
        return t_filtro, lista_retorno, req_7_time
        

def req_8(catalog):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    pass


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed
