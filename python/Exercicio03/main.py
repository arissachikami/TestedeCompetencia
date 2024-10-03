import pandas as pd
from datetime import datetime


def processar_licencas(arquivo_entrada, arquivo_saida):

    df = pd.read_excel(arquivo_entrada)
    df.columns = df.columns.str.strip()

    if 'Unnamed: 0' in df.columns:
        df.rename(columns={'Unnamed: 0': 'ID_Usuario'}, inplace=True)

    df['Start Time'] = pd.to_datetime(df['Start Time'], format='%d/%m/%Y %H:%M', dayfirst=True, errors='coerce')
    df['End Time'] = pd.to_datetime(df['End Time'], format='%Y-%m-%d %H:%M:%S', errors='coerce')
   
    df['Dia'] = df['Start Time'].dt.date
    df['Tempo de uso'] = (df['End Time'] - df['Start Time']).dt.total_seconds()/3600

    df_resumo = df.groupby(['ID_Usuario', 'User Name', 'License Type', 'Dia'])['Tempo de uso'].sum().reset_index()

    df_resumo.to_excel(arquivo_saida, index=False)

arquivo_entrada = 'Input_Teste_Python_exercicio 3.xlsx'  
arquivo_saida = 'licenca.xlsx'  

start_time = datetime.now()
processar_licencas(arquivo_entrada, arquivo_saida)
end_time = datetime.now()

print(f"Tempo de execução: {end_time - start_time}")
