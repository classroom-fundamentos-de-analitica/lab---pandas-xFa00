"""
Laboratorio - Manipulación de Datos usando Pandas
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

Utilice los archivos `tbl0.tsv`, `tbl1.tsv` y `tbl2.tsv`, para resolver las preguntas.

"""
import pandas as pd

tbl0 = pd.read_csv("tbl0.tsv", sep="\t")
tbl1 = pd.read_csv("tbl1.tsv", sep="\t")
tbl2 = pd.read_csv("tbl2.tsv", sep="\t")


def pregunta_01():
    """
    ¿Cuál es la cantidad de filas en la tabla `tbl0.tsv`?
    Rta/
    40
    """
    return len(tbl0.index)
def pregunta_02():
    """
    ¿Cuál es la cantidad de columnas en la tabla `tbl0.tsv`?
    Rta/
    4
    """
    return len(tbl0.columns)
def pregunta_03():
    """
    ¿Cuál es la cantidad de registros por cada letra de la columna _c1 del archivo
    `tbl0.tsv`?
    Rta/
    A     8
    B     7
    C     5
    D     6
    E    14
    Name: _c1, dtype: int64
    """
    return tbl0["_c1"].groupby(tbl0["_c1"]).size()
def pregunta_04():
    """
    Calcule el promedio de _c2 por cada letra de la _c1 del archivo `tbl0.tsv`.
    Rta/
    A    4.625000
    B    5.142857
    C    5.400000
    D    3.833333
    E    4.785714
    Name: _c2, dtype: float64
    """
    return tbl0[["_c1","_c2"]].groupby(by=["_c1"]).mean().squeeze()
def pregunta_05():
    """
    Calcule el valor máximo de _c2 por cada letra en la columna _c1 del archivo
    `tbl0.tsv`.
    Rta/
    _c1
    A    9
    B    9
    C    9
    D    7
    E    9
    Name: _c2, dtype: int64
    """
    return tbl0[["_c1","_c2"]].groupby(by=["_c1"]).max().squeeze()
def pregunta_06():
    """
    Retorne una lista con los valores unicos de la columna _c4 de del archivo `tbl1.csv`
    en mayusculas y ordenados alfabéticamente.
    Rta/
    ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    """
    lst = []
    for item in tbl1["_c4"]:
        if item.upper() not in lst:
            lst.append(item.upper())
    lst.sort()
    
    return lst
def pregunta_07():
    """
    Calcule la suma de la _c2 por cada letra de la _c1 del archivo `tbl0.tsv`.
    Rta/
    _c1
    A    37
    B    36
    C    27
    D    23
    E    67
    Name: _c2, dtype: int64
    """
    return tbl0[["_c1","_c2"]].groupby(by=["_c1"]).sum().squeeze()
def pregunta_08():
    """
    Agregue una columna llamada `suma` con la suma de _c0 y _c2 al archivo `tbl0.tsv`.
    Rta/
        _c0 _c1  _c2         _c3  suma
    0     0   E    1  1999-02-28     1
    1     1   A    2  1999-10-28     3
    2     2   B    5  1998-05-02     7
    ...
    37   37   C    9  1997-07-22    46
    38   38   E    1  1999-09-28    39
    39   39   E    5  1998-01-26    44
    """
    tbl0["suma"] = tbl0["_c0"] + tbl0["_c2"]
    return tbl0
def pregunta_09():
    """
    Agregue el año como una columna al archivo `tbl0.tsv`.
    Rta/
        _c0 _c1  _c2         _c3  year
    0     0   E    1  1999-02-28  1999
    1     1   A    2  1999-10-28  1999
    2     2   B    5  1998-05-02  1998
    ...
    37   37   C    9  1997-07-22  1997
    38   38   E    1  1999-09-28  1999
    39   39   E    5  1998-01-26  1998
    """
    tbl0['year'] = tbl0['_c3'].str.slice(0, 4)
    
    return tbl0
def pregunta_10():

    tablaN = tbl0[["_c1", "_c2"]].copy().set_index("_c2").groupby("_c1")
    proc = {g:":".join(sorted([str(x) for x in c])) for g,c in tablaN.groups.items()}
    
    
    return pd.DataFrame({"_c1":proc.keys(), "_c2":proc.values()}).set_index("_c1")

def pregunta_11():
    
    dataf = pd.DataFrame()
    for letra in tbl1["_c0"].unique():
        df = np.where(tbl1["_c0"]==letra,tbl1["_c4"],"")
        df = np.delete(df, np.where(df == ""))
        string = ""
        for item in list(np.sort(df, axis=0)):
            string = string + str(item) + ","
        string = string[:-1]
        temp = pd.DataFrame({"_c0":[letra], "_c4": string})
        dataf = dataf.append(temp, ignore_index=True)
    return dataf

def pregunta_12():
    """
    Construya una tabla que contenga _c0 y una lista separada por ',' de los valores de
    la columna _c5a y _c5b (unidos por ':') de la tabla `tbl2.tsv`.
    Rta/
        _c0                                  _c5
    0     0        bbb:0,ddd:9,ggg:8,hhh:2,jjj:3
    1     1              aaa:3,ccc:2,ddd:0,hhh:9
    2     2              ccc:6,ddd:2,ggg:5,jjj:1
    ...
    37   37                    eee:0,fff:2,hhh:6
    38   38                    eee:0,fff:9,iii:2
    39   39                    ggg:3,hhh:8,jjj:5
    """
    diccionario = {}
    for i in range (len(tbl2)):
        if tbl2.loc[i]["_c0"] in diccionario:
            diccionario[tbl2.loc[i]["_c0"]] = diccionario[tbl2.loc[i]["_c0"]] + "," + tbl2.loc[i]["_c5a"] + ":" + str(tbl2.loc[i]["_c5b"])
        else:
            diccionario[tbl2.loc[i]["_c0"]] = tbl2.loc[i]["_c5a"] + ":" + str(tbl2.loc[i]["_c5b"])
            
    for k,v in diccionario.items():
        lista = v.split(",")
        lista.sort()
        diccionario[k] = lista
    df = pd.DataFrame({"_c0": diccionario.keys(),
            "_c5a" : diccionario.values()})
    lista = []
    for valor in df["_c5a"]:
        string = "hola"
        for i in valor:
            string = string + ',' + i
        lista.append(string)
    df['_c5'] = lista
    df['_c5'] = df['_c5'].str.replace('hola,','')
    del df['_c5a']
    return df
def pregunta_13():
    """
    Si la columna _c0 es la clave en los archivos `tbl0.tsv` y `tbl2.tsv`, compute la
    suma de tbl2._c5b por cada valor en tbl0._c1.
    Rta/
    _c1
    A    146
    B    134
    C     81
    D    112
    E    275
    Name: _c5b, dtype: int64
    """
    return tbl0.merge(tbl2, right_on = '_c0', left_on = '_c0').groupby('_c1').sum()['_c5b']
