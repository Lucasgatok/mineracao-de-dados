import requests
from bs4 import BeautifulSoup

# URL da página que você quer acessar
url = 'https://weather.com/pt-BR/forecast/air-quality/l/ebb70a47505c2e81f1fcd94e033f8772c66512a6f19efc3ed49152aede4c5aa3'

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

    # Procura pelo elemento que contém o valor de qualidade do ar
    air_quality_value = soup.find('text', class_='DonutChart--innerValue--3_iFF AirQuality--extendedDialText--1kqIb')
    
    if air_quality_value:
        print(f"Valor de qualidade do ar: {air_quality_value.text.strip()}")
    else:
        print("Valor de qualidade do ar não encontrado!")
else:
    print(f"Falha ao acessar a página. Código de status: {response.status_code}")
