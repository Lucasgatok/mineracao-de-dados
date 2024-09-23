import pandas as pd

def process_table_data(rows):
    """
    Função para processar os dados extraídos da tabela HTML e organizar em um DataFrame.
    
    rows: lista de linhas com os dados extraídos (tuplas ou listas).
    """
    # Inicializando listas para cada coluna
    days = []
    quotas = []
    changes = []

    # Itera por cada linha da tabela extraída
    for row in rows:
        day = row[0]  # Primeiro valor: Dia
        quota = row[1]  # Segundo valor: Cota (m)
        change = row[2]  # Terceiro valor: Encheu/Vazou (cm)
        
        # Adiciona os dados nas listas correspondentes
        days.append(day)
        quotas.append(quota)
        changes.append(change)

    # Cria o DataFrame a partir dos dados
    df = pd.DataFrame({
        "Dia": days,
        "Cota (m)": quotas,
        "Encheu/Vazou (cm)": changes
    })

    return df

def save_to_csv(df, filename='tabela_nivel_rio_negro.xslx'):


    df.to_csv(filename, index=False)
