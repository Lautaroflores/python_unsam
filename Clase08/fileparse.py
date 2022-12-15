import csv
import gzip


def parse_csv(f,select = None, types = None,  has_headers=True, silence_errors = False):
    """
    Parsea un archivo CVS en una lista de reigstros
    Parsear: analizar separando en sus partes constitutivas
    """
    
    rows = csv.reader(f)
    indices = []
    if select and not has_headers:
            raise RuntimeError("Para seleccionar, necesito encabezados.")
    if has_headers:
       
            headers = next(rows)
        
       
            if select:
                indices = [headers.index(nombre_columna) for nombre_columna in select]
                headers = select
            if select:
                indices = [headers.index(nombre_columna) for nombre_columna in select]
                headers = select
            else:
                indices = []
            registros = []
            for r,row in enumerate(rows):
        
                if not row:
                    continue
                if indices:
                
                    row = [row[index] for index in indices]
                try:
                    
                    if types:
                        row = [func(val) for func, val in zip(types, row) ]
                except ValueError as e:
                    if not silence_errors:
                        print(f'Fila {r+1}: No puede convertir {row}\ntMotivo: {e}')
                    
                registro = dict(zip(headers, row))
                registros.append(registro)
                    
                
                    
    else:
            registros = []
            for r,row in enumerate(rows):

                try:
                    if types:
                        row = tuple([func(val) for func, val in zip(types,row)])
                  
                except ValueError as e:
                    if not silence_errors:
                        print(f'Fila {r+1}: No puede convertir {row}\ntMotivo: {e}')
                        
                registros.append(row)
     
           
    return registros


    