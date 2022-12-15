import csv

def parse_csv(nombre_archivo, select = None, types = None,  has_headers=False):
    """
    Parsea un archivo CVS en una lista de reigstros
    Parsear: analizar separando en sus partes constitutivas
    """
    with open(nombre_archivo) as f:
        rows = csv.reader(f)
       
        indices = []
        
        if has_headers:
        # Lee los encabezados
            headers = next(rows)
        
        # Selector de columnas
            if select:
                indices = [headers.index(nombre_columna) for nombre_columna in select]
                headers = select
            if select:
                indices = [headers.index(nombre_columna) for nombre_columna in select]
                headers = select
            else:
                indices = []
            registros = []
            for row in rows:
        
                if not row:
                    continue
            
                if types:
                    row = [func(val) for func, val in zip(types, row) ]
            
                if indices:
                
                    row = [row[index] for index in indices]
                    
                registro = dict(zip(headers, row))
                registros.append(registro)
        else:
            registros = []
            for row in rows:
                if not row:
                    continue
                if types:
                  
                    row = tuple([func(val) for func, val in zip(types,row)])
                registros.append(row)
     
           
    return registros

        