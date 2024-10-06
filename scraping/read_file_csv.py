# read_file_csv.py

import csv
import os
from models import Comercio
from datetime import datetime
from db import get_session


"""
Function to read the comercio.csv file
"""
def read_file_comercio_csv(path_archivo):
    session = get_session()
    with open(path_archivo, newline='') as file_csv:
        reader = csv.reader(file_csv, delimiter='|')  # Specify the delimiter as '|'
        encabezados = next(reader)
        print(f"Encabezados: {encabezados}")
        input("Press Enter to continue...")

        for num_fila, fila in enumerate(reader, start=1):
            now = datetime.now()
            formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")

            print(f"Fila {num_fila}: ", end="")
            if fila and len(fila) == 8:  # Ensure the row has 8 columns
                print('f filea {fila}')
                id_comercio = fila[0]
                id_bandera = fila[1]
                comercio_cuit = fila[2]
                comercio_razon_social = fila[3]
                comercio_bandera_nombre = fila[4]
                comercio_bandera_url = fila[5]
                comercio_ultima_actualizacion = fila[6]
                comercio_version_sepa = fila[7]

                print(f"id_comercio: {id_comercio}")
                print(f"id_bandera: {id_bandera}")
                print(f"comercio_cuit: {comercio_cuit}")
                print(f"comercio_razon_social: {comercio_razon_social}")
                print(f"comercio_bandera_nombre: {comercio_bandera_nombre}")
                print(f"comercio_bandera_url: {comercio_bandera_url}")
                print(f"comercio_ultima_actualizacion: {comercio_ultima_actualizacion}")
                print(f"comercio_version_sepa: {comercio_version_sepa}")
                # fecha_alta = formatted_date
                comercio = Comercio()
                comercio.id_comercio =id_comercio 
                comercio.id_bandera = id_bandera 
                comercio.comercio_cuit = comercio_cuit
                comercio.comercio_razon_social = comercio_razon_social
                comercio.comercio_bandera_nombre = comercio_bandera_nombre
                comercio.comercio_bandera_url = comercio_bandera_url
                comercio.comercio_ultima_actualizacion = comercio_ultima_actualizacion
                comercio.comercio_version_sepa = comercio_version_sepa
                #comercio.fecha_alta = fecha_alta
                print(comercio)

                ##Insertar en la base de datos 
                comercio.insert_comercio(session)

            print()  # Salto de línea después de cada fila


""" Funcion que permite leer archivo csv producto """
def read_file_producto_csv(path_archivo):
    print("=================")
    print('Read csv Producto : {path_archivo}')
    session = get_session()
    with open(path_archivo, newline='') as file_csv:
        reader = csv.reader(file_csv, delimiter='|')  # Specify the delimiter as '|'
        encabezados = next(reader)
        print("Encabezados:", encabezados)
        #input("Press Enter to continue...")

        for num_fila, fila in enumerate(reader, start=1):
            now = datetime.now()
            formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")

            print(f"Fila {num_fila}: ", end="")
            if fila and len(fila) == 17:  # Ensure the row has 17 columns
                print(f'Fila {fila}')
                id_comercio = fila[0]
                id_bandera = fila[1]
                id_sucursal = fila[2]
                id_producto = fila[3]
                productos_ean = fila[4]
                productos_descripcion = fila[5]
                productos_cantidad_presentacion = fila[6]
                productos_unidad_medida_presentacion = fila[7]
                productos_marca = fila[8]
                productos_precio_lista = fila[9]
                productos_precio_referencia = fila[10]
                productos_cantidad_referencia = fila[11]
                productos_unidad_medida_referencia = fila[12]
                productos_precio_unitario_promo1 = fila[13]
                productos_leyenda_promo1 = fila[14]
                productos_precio_unitario_promo2 = fila[15]
                productos_leyenda_promo2 = fila[16]

                print(f"id_comercio: {id_comercio}")
                print(f"id_bandera: {id_bandera}")
                print(f"id_sucursal: {id_sucursal}")
                print(f"id_producto: {id_producto}")
                print(f"productos_ean: {productos_ean}")
                print(f"productos_descripcion: {productos_descripcion}")
                print(f"productos_cantidad_presentacion: {productos_cantidad_presentacion}")
                print(f"productos_unidad_medida_presentacion: {productos_unidad_medida_presentacion}")
                print(f"productos_marca: {productos_marca}")
                print(f"productos_precio_lista: {productos_precio_lista}")
                print(f"productos_precio_referencia: {productos_precio_referencia}")
                print(f"productos_cantidad_referencia: {productos_cantidad_referencia}")
                print(f"productos_unidad_medida_referencia: {productos_unidad_medida_referencia}")
                print(f"productos_precio_unitario_promo1: {productos_precio_unitario_promo1}")
                print(f"productos_leyenda_promo1: {productos_leyenda_promo1}")
                print(f"productos_precio_unitario_promo2: {productos_precio_unitario_promo2}")
                print(f"productos_leyenda_promo2: {productos_leyenda_promo2}")

                # fecha_alta = formatted_date
                # producto = Producto()
                # Asignar los valores a los atributos del objeto producto
                # ...

                # Insertar en la base de datos 
                #producto.insert_producto(session)

            print()  # Salto de línea después de cada fila


def read_file_sucursales_csv(path_archivo):
    print('----------------------')
    print('Sucursales')
    session = get_session()
    with open(path_archivo, newline='') as file_csv:
        reader = csv.reader(file_csv, delimiter='|')
        encabezados = next(reader)
        print("Encabezados:", encabezados)

        for num_fila, fila in enumerate(reader, start=1):
            now = datetime.now()
            formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")

            print(f"Fila {num_fila}: ", end="")
            if fila and len(fila) == 21:  # Ensure the row has 21 columns
                print(f'Fila {fila}')
                id_comercio = fila[0]
                id_bandera = fila[1]
                id_sucursal = fila[2]
                sucursales_nombre = fila[3]
                sucursales_tipo = fila[4]
                sucursales_calle = fila[5]
                sucursales_numero = fila[6]
                sucursales_latitud = fila[7]
                sucursales_longitud = fila[8]
                sucursales_observaciones = fila[9]
                sucursales_barrio = fila[10]
                sucursales_codigo_postal = fila[11]
                sucursales_localidad = fila[12]
                sucursales_provincia = fila[13]
                sucursales_lunes_horario_atencion = fila[14]
                sucursales_martes_horario_atencion = fila[15]
                sucursales_miercoles_horario_atencion = fila[16]
                sucursales_jueves_horario_atencion = fila[17]
                sucursales_viernes_horario_atencion = fila[18]
                sucursales_sabado_horario_atencion = fila[19]
                sucursales_domingo_horario_atencion = fila[20]

                # Print or process the data as needed
                print(f"id_comercio: {id_comercio}")
                print(f"id_bandera: {id_bandera}")
                print(f"id_sucursal: {id_sucursal}")
                print(f"sucursales_nombre: {sucursales_nombre}")
                print(f"sucursales_tipo: {sucursales_tipo}")
                print(f"sucursales_calle: {sucursales_calle}")
                print(f"sucursales_numero: {sucursales_numero}")
                print(f"sucursales_latitud: {sucursales_latitud}")
                print(f"sucursales_longitud: {sucursales_longitud}")
                print(f"sucursales_observaciones: {sucursales_observaciones}")
                print(f"sucursales_barrio: {sucursales_barrio}")
                print(f"sucursales_codigo_postal: {sucursales_codigo_postal}")
                print(f"sucursales_localidad: {sucursales_localidad}")
                print(f"sucursales_provincia: {sucursales_provincia}")
                print(f"sucursales_lunes_horario_atencion: {sucursales_lunes_horario_atencion}")
                print(f"sucursales_martes_horario_atencion: {sucursales_martes_horario_atencion}")
                print(f"sucursales_miercoles_horario_atencion: {sucursales_miercoles_horario_atencion}")
                print(f"sucursales_jueves_horario_atencion: {sucursales_jueves_horario_atencion}")
                print(f"sucursales_viernes_horario_atencion: {sucursales_viernes_horario_atencion}")
                print(f"sucursales_sabado_horario_atencion: {sucursales_sabado_horario_atencion}")
                print(f"sucursales_domingo_horario_atencion: {sucursales_domingo_horario_atencion}")

                # Here you would typically create a Sucursal object and insert it into the database
                # sucursal = Sucursal()
                # Assign values to the sucursal object attributes
                # ...

                # Insert into the database 
                # sucursal.insert_sucursal(session)

            print()  # Line break after each row


def leer_directorio(path_directorio):
    """Función para leer archivos CSV en un directorio y procesarlos según su tipo"""
    print('---------------------------------------------')
    print(f"Leyendo archivos en el directorio : {path_directorio}")
    
    for directory in os.listdir(path_directorio):
        print("name directory: ", directory)
        path_directory = os.path.join(path_directorio, directory)
        if os.path.isdir(path_directory):
            print(f"Es un directorio: {directory}")
            for filecsv in os.listdir(path_directory) : 
                if filecsv.endswith('.csv'):
                    file_path = os.path.join(path_directorio, directory, filecsv)
                    print(f"Procesando archivo: {filecsv}")
                    if filecsv.endswith('comercio.csv'):
                        print("Es un archivo de comercio")
                        read_file_comercio_csv(file_path)
                    elif filecsv.endswith('productos.csv'):
                        print("Es un archivo de productos")
                        read_file_producto_csv(file_path)
                        # Aquí puedes llamar a una función para procesar archivos de productos
                    elif filecsv.endswith('sucursales.csv'):
                        print("Es un archivo de precios")
                        read_file_sucursales_csv(file_path)
                        # Aquí puedes llamar a una función para procesar archivos de precios
                    else:
                        print("No se reconoce el tipo de archivo CSV")
                    
                    print("--------------------")
            
            print("--------------------")
        else:
            print(f"No es un directorio: {directory}")
            print("--------------------")
# Uso de la función
leer_directorio('/home/manuonda/projects/project-precios-cuidados/scraping/data_files/Jueves - Precios SEPA Minoristas jueves, 2024-10-03.sepa_jueves')
# Ejemplo de uso
#leer_csv('/home/manuonda/projects/devops/precios_cuidados/data_files/Jueves - Precios SEPA Minoristas jueves, 05-09-2024.sepa_jueves/sepa_1_comercio-sepa-3_2024-09-05_09-05-12/comercio.csv')