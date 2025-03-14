import pandas as pd

from utils.data_preocessing import *

def preprocess_data():
    SONGS_FILE_PATH = '../data/01_raw/1-2025-6004.xlsx'
    PLACES_FILE_PATH = '../data/01_raw/Departamentos  municipios de Colombia.xlsx'
    OUTPUT_FILE_PATH = '../data/02_intermediate/canciones_limpias.xlsx'

    # Cargar los dataframes de las canciones
    df = load_excel(SONGS_FILE_PATH)  # Asegúrate de que esta función está definida correctamente
    df_dep = pd.read_excel(PLACES_FILE_PATH, sheet_name='Departamentos')
    df_mun = pd.read_excel(PLACES_FILE_PATH, sheet_name='Municipios')
    
    # Selecionar las columnas ['TITULO','AÑO','COMPOSITOR','UBICACIÓN']
    df = df[['TITULO','AÑO','COMPOSITOR','UBICACIÓN']]

    # Limpiar las columnas de texto
    df['TITULO'] = df['TITULO'].apply(lambda x: clean_text(str(x)))
    df['AÑO'] = df['AÑO'].apply(lambda x: clean_text(str(x)))
    df['COMPOSITOR'] = df['COMPOSITOR'].apply(lambda x: clean_text(str(x)))
    df['UBICACIÓN'] = df['UBICACIÓN'].apply(lambda x: clean_text(str(x)))

    # Filtrar los años entre 1990 y 2023
    df['AÑO'] = df['AÑO'].apply(lambda x: x[0:4] if len(str(x)) == 5 else x)
    df['AÑO'] = df['AÑO'].apply(lambda x: 0 if len(str(x)) != 4 else x)
    df['AÑO'] = pd.to_numeric(df['AÑO'], errors='coerce')
    df = df.dropna(subset=['AÑO'])
    df['AÑO'] = df['AÑO'].astype(int)
    df = df.query('AÑO >= 1990')
    df = df.query('AÑO <= 2023')

    df = df.query('UBICACIÓN != "-"')
    df.loc[: , 'UBICACIÓN'] = df['UBICACIÓN'].str.strip() #Eliminar espacios extra
    df.loc[: , 'COMPOSITOR'] = df['COMPOSITOR'].str.replace(r'\s+', ' ', regex=True).str.strip() #Eliminar espacios extra, tabulaciones

    df = df.copy()

    df['UBICACIÓN'] = df['UBICACIÓN'].str.strip().replace({'SANTIAGO DE CALI':'CALI'})
    df['UBICACIÓN'] = df['UBICACIÓN'].str.strip().replace({'ARMERO GUAYABAL':'ARMERO'})
    df['UBICACIÓN'] = df['UBICACIÓN'].str.strip().replace({'BUGA':'GUADALAJA DE BUGA'})
    df['UBICACIÓN'] = df['UBICACIÓN'].str.strip().replace({'CARMEN DE BOLIVAR':'EL CARMEN DE BOLIVAR'})
    df['UBICACIÓN'] = df['UBICACIÓN'].str.strip().replace({'CARMEN DE VIBORAL':'EL CARMEN DE VIBORAL'})
    df['UBICACIÓN'] = df['UBICACIÓN'].str.strip().replace({'CODAZZI':'AGUSTIN CODAZZI'})
    df['UBICACIÓN'] = df['UBICACIÓN'].str.strip().replace({'DARIEN':'CARMEN DEL DARIEN'})
    df['UBICACIÓN'] = df['UBICACIÓN'].str.strip().replace({'EL PITAL':'PITAL'})
    df['UBICACIÓN'] = df['UBICACIÓN'].str.strip().replace({'EL RETIRO':'RETIRO'})
    df['UBICACIÓN'] = df['UBICACIÓN'].str.strip().replace({'FINLANDIA':'FILANDIA'})
    df['UBICACIÓN'] = df['UBICACIÓN'].str.strip().replace({'HATO NUEVO':'HATONUEVO'})
    df['UBICACIÓN'] = df['UBICACIÓN'].str.strip().replace({'GUAIPI':'GUAPI'})
    df['UBICACIÓN'] = df['UBICACIÓN'].str.strip().replace({'MOMPOX':'MOMPOS'})
    df['UBICACIÓN'] = df['UBICACIÓN'].str.strip().replace({'SABANA GRANDE':'SABANAGRANDE'})
    df['UBICACIÓN'] = df['UBICACIÓN'].str.strip().replace({'SALADO BLANCO':'SALADOBLANCO'})
    df['UBICACIÓN'] = df['UBICACIÓN'].str.strip().replace({'SAN FRANCISCO .':'SAN FRANCISCO'})
    df['UBICACIÓN'] = df['UBICACIÓN'].str.strip().replace({'SAN JUAN DE GIRON':'GIRON'})
    df['UBICACIÓN'] = df['UBICACIÓN'].str.strip().replace({'SAN JUAN DE PASTO':'PASTO'})
    df['UBICACIÓN'] = df['UBICACIÓN'].str.strip().replace({'SANTA FE DE ANTIOQUIA':'SANTAFE DE ANTIOQUIA'})
    df['UBICACIÓN'] = df['UBICACIÓN'].str.strip().replace({'ANTIOQUIA':'SANTAFE DE ANTIOQUIA'})
    df['UBICACIÓN'] = df['UBICACIÓN'].str.strip().replace({'TOLU':'SANTIAGO DE TOLU'})
    df['UBICACIÓN'] = df['UBICACIÓN'].str.strip().replace({'TOLUVIEJO':'TOLU VIEJO'})
    df['UBICACIÓN'] = df['UBICACIÓN'].str.strip().replace({'TUMACO':'SAN ANDRES DE TUMACO'})
    df['UBICACIÓN'] = df['UBICACIÓN'].str.strip().replace({'UBATE':'VILLA DE SAN DIEGO DE UBATE'})
    df['UBICACIÓN'] = df['UBICACIÓN'].str.strip().replace({'SINCE':'SINCELEJO'})
    df['UBICACIÓN'] = df['UBICACIÓN'].str.strip().replace({'GUADALAJA DE BUGA':'GUADALAJARA DE BUGA'})
    df['UBICACIÓN'] = df['UBICACIÓN'].str.strip().replace({'MANRIQUE':'MEDELLIN'})
    df['UBICACIÓN'] = df['UBICACIÓN'].str.strip().replace({'SAN ANTONIO DE PRADO':'MEDELLIN'})
    df['UBICACIÓN'] = df['UBICACIÓN'].str.strip().replace({'EL BORDO':'PATIA'})
    df['UBICACIÓN'] = df['UBICACIÓN'].str.strip().replace({'BORDO':'PATIA'})
    df['UBICACIÓN'] = df['UBICACIÓN'].str.strip().replace({'EL DIFICIL':'ARIGUANI'})
    df['UBICACIÓN'] = df['UBICACIÓN'].str.strip().replace({'SAN PEDRO DE LOS MILAGROS':'SAN PEDRO'})
    df['UBICACIÓN'] = df['UBICACIÓN'].str.strip().replace({'SAN JOSE DE CUCUTA':'CUCUTA'})
    df['UBICACIÓN'] = df['UBICACIÓN'].str.strip().replace({'CHICORAL':'ESPINAL'})
    df['UBICACIÓN'] = df['UBICACIÓN'].str.strip().replace({'VILLA GORGONA':'CANDELARIA'})
    df['UBICACIÓN'] = df['UBICACIÓN'].str.strip().replace({'RIO GRANDE':'DON MATIAS'})
    df['UBICACIÓN'] = df['UBICACIÓN'].str.strip().replace({'PUERTO RENDON':'PUERTO RONDON'})
    df['UBICACIÓN'] = df['UBICACIÓN'].str.strip().replace({'LA MINA':'VALLEDUPAR'})
    df['UBICACIÓN'] = df['UBICACIÓN'].str.strip().replace({'CASABLANCA': 'CASABIANCA'})
    df['UBICACIÓN'] = df['UBICACIÓN'].str.strip().replace({'CERREJON': 'BARRANCAS'})
    df['UBICACIÓN'] = df['UBICACIÓN'].str.strip().replace({'LA HORMIGA': 'VALLE DEL GUAMUEZ'})
    df['UBICACIÓN'] = df['UBICACIÓN'].str.strip().replace({'SAN JUAN': 'SAN JUAN DEL CESAR'})
    df['UBICACIÓN'] = df['UBICACIÓN'].str.strip().replace({'DADEIBA': 'DABEIBA'})
    df['UBICACIÓN'] = df['UBICACIÓN'].str.strip().replace({'COCOTIQUICIO': 'TIQUISIO'})
    df['UBICACIÓN'] = df['UBICACIÓN'].str.strip().replace({'PUERTO CALDAS': 'PEREIRA'})
    df['UBICACIÓN'] = df['UBICACIÓN'].str.strip().replace({'VILLA GUAMEZ': 'VALLE DEL GUAMUEZ'})
    df['UBICACIÓN'] = df['UBICACIÓN'].str.strip().replace({'GUACAMAYAL': 'ZONA BANANERA'})
    df['UBICACIÓN'] = df['UBICACIÓN'].str.strip().replace({'EL RODADERO': 'SANTA MARTA'})
    df['UBICACIÓN'] = df['UBICACIÓN'].str.strip().replace({'LA LOMA': 'EL PASO'})
    df['UBICACIÓN'] = df['UBICACIÓN'].str.strip().replace({'LA JAGUA': 'NEIVA'})
    df['UBICACIÓN'] = df['UBICACIÓN'].str.strip().replace({'BOQUERON': 'TIBACUY'})
    df['UBICACIÓN'] = df['UBICACIÓN'].str.strip().replace({'CARTAGENITA': 'CARTAGENA'})
    df['UBICACIÓN'] = df['UBICACIÓN'].str.strip().replace({'CARRETO': 'CANDELARIA'})
    

    df = df[~df['TITULO'].str.contains(r'\(SAL\.|\(SALMO', na=False, case=False)]
    #print(df.info())

    export_excel(df, OUTPUT_FILE_PATH)