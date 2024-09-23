import requests
from bs4 import BeautifulSoup
import dataprocessing  # Importa o arquivo com a função de processamento

# URL da página que você quer acessar
url = 'https://portodemanaus.com.br/nivel-do-rio-negro/'

# Cabeçalhos para simular um navegador real
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

# Envia a requisição GET para pegar o conteúdo da página com o User-Agent
response = requests.get(url, headers=headers)

# Verifica se a requisição foi bem-sucedida
if response.status_code == 200:
    # Faz o parsing do HTML usando o BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Procura a div específica que contém a tabela
    div = soup.find('div', {
        'class': 'elementor-element elementor-element-5bb124b elementor-widget elementor-widget-jet-listing-dynamic-repeater',
        'data-id': '5bb124b',
        'data-element_type': 'widget',
        'data-widget_type': 'jet-listing-dynamic-repeater.default'
    })

    if div:
        # Dentro da div, procuramos pela tabela
        table = div.find('table')
        rows = []

        # Itera por cada linha da tabela (cada 'tr')
        for tr in table.find_all('tr')[1:]:  # Ignora o cabeçalho (primeira linha)
            tds = tr.find_all('td')
            row = [td.text.strip() for td in tds]  # Extrai o texto das células
            rows.append(row)  # Adiciona a linha completa na lista de linhas

        # Processa os dados extraídos usando a função do arquivo dataprocessing.py
        df = dataprocessing.process_table_data(rows)

        # Exibe o DataFrame
        print(df)

        # Salva o DataFrame em um arquivo CSV
        dataprocessing.save_to_csv(df)

    else:
        print("Div específica não encontrada!")
else:
    print(f"Falha ao acessar a página. Código de status: {response.status_code}")
