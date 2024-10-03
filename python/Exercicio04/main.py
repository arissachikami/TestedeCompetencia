import pandas as pd
from datetime import datetime

def atualizar_usernames(arquivo_comum, arquivo_especial, arquivo_saida, arquivo_nao_encontrados):
    df_comum = pd.read_excel(arquivo_comum)
    df_especial = pd.read_excel(arquivo_especial)

    if 'Unnamed: 0' in df_comum.columns:
        df_comum.rename(columns={'Unnamed: 0': 'ID_Usuario'}, inplace=True)
    
    df_comum['Start Time'] = pd.to_datetime(df_comum['Start Time'], format='%d/%m/%Y %H:%M',dayfirst=True, errors='coerce')
    df_comum['End Time'] = pd.to_datetime(df_comum['End Time'], format='%Y-%m-%d %H:%M:%S',dayfirst=True, errors='coerce')

    df_especial['Hora Inicio'] = pd.to_datetime(df_especial['Data Inicio'] + ' ' + df_especial['Hora Inicio']+':00', format='%Y-%m-%d %H:%M:%S', errors='coerce')
    df_especial['Hora Termino'] = pd.to_datetime(df_especial['Data Termino'] + ' ' + df_especial['Hora Termino'], format='%Y-%m-%d %H:%M:%S', errors='coerce')


    encontrados = []
    nao_encontrados = []

    for index, row in df_comum.iterrows():
        if pd.notnull(row['Start Time']) and pd.notnull(row['End Time']):
            match = df_especial[
                (df_especial['Hora Inicio'] == row['Start Time']) & 
                (df_especial['Hora Termino'] == row['End Time'])
            ]
            
            if not match.empty:
                df_comum.at[index, 'User Name'] = match.iloc[0]['Usuario']
                encontrados.append([row['ID_Usuario'], match.iloc[0]['Usuario']])
            else:
                nao_encontrados.append([row['ID_Usuario'], row.get('User Name', 'unknown')])
        else:
            nao_encontrados.append([row['ID_Usuario'], row.get('User Name', 'unknown')])

    df_comum_ajustada = df_comum[['ID_Usuario', 'User Name', 'Start Time', 'End Time']].copy()
    df_comum_ajustada.rename(columns={'Start Time': 'Hora Inicial', 'End Time': 'Hora Final', 'User Name': 'Username'}, inplace=True)

    df_comum_ajustada.to_excel(arquivo_saida, index=False)

    df_nao_encontrados = pd.DataFrame(nao_encontrados, columns=['ID_Usuario', 'User Name'])
    df_nao_encontrados.to_excel(arquivo_nao_encontrados, index=False)


arquivo_comum = 'comum.xlsx'
arquivo_especial = 'especial.xlsx'
arquivo_saida = 'tabela_atualizada.xlsx'
arquivo_nao_encontrados = 'nao_encontrados.xlsx'

start_time = datetime.now()
atualizar_usernames(arquivo_comum, arquivo_especial, arquivo_saida, arquivo_nao_encontrados)
end_time = datetime.now()

print(f"Tempo de execução: {end_time - start_time}")
