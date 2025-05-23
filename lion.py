import requests
import hashlib
import sys
from colorama import Fore, Style

# 🔑 Substitua pela sua chave da API AbuseIPDB
api_key_numverify = "8ff2f59742cf2cf49060ead6a03b8222"
api_key_abuseipdb = "25b0407cdaa6ebacdfa21b57babb17edaa5470d272fcc2a3f012d60573d77e24f58adb2974be1e05"

def banner():
    print(f'{Fore.YELLOW}||              ||     ||||||||     ||       ||  {Style.RESET_ALL}')
    print(f'{Fore.YELLOW}||              ||     ||    ||     || ||    || {Style.RESET_ALL}')
    print(f'{Fore.YELLOW}||              ||     ||    ||     ||  ||   || {Style.RESET_ALL}')
    print(f'{Fore.YELLOW}||              ||     ||    ||     ||   ||  || {Style.RESET_ALL}')
    print(f'{Fore.YELLOW}||              ||     ||    ||     ||    || || {Style.RESET_ALL}')
    print(f'{Fore.YELLOW}\\=====          ||     ||||||||     ||     ||||   𝑺{Style.RESET_ALL}')
    print(f'{Fore.GREEN}       LIONS  I 𝙲𝙾𝙽𝚂𝚄𝙻𝚃𝙰𝚂 - 𝙱𝚢 𝙲𝚛𝚎𝚊𝚝𝚘𝚛  {Style.RESET_ALL}\n')

# O restante do código permanece o mesmo

# O restante do código permanece o mesmo

# O restante do código permanece o mesmo

def consulta_api(url, titulo):
    try:
        r = requests.get(url, timeout=10)
        r.raise_for_status()
        dados = r.json()

        print(f'\n{Fore.GREEN}== {titulo} =={Style.RESET_ALL}')
        if isinstance(dados, list):  # Verifica se é uma lista
            for item in dados:
                print(item)  # Exibe diretamente cada item da lista
        else:
            for chave, valor in dados.items():
                print(f'{chave.capitalize()}: {valor}')
    except requests.exceptions.HTTPError as e:
        print(f'{Fore.RED}Erro HTTP: {e}{Style.RESET_ALL}')
    except requests.exceptions.RequestException as e:
        print(f'{Fore.RED}Erro ao buscar informações: {e}{Style.RESET_ALL}')

def buscar_cpf():
    cpf = input('Digite o CPF (somente números): ')
    url = f'https://jsp.minerdapifoda.xyz:8080/api/typebot?cpf={cpf}'
    
    try:
        r = requests.get(url, timeout=10)
        r.raise_for_status()
        dados = r.json()

        print(f'\n{Fore.GREEN}== DADOS DO CPF (SIMPLES) =={Style.RESET_ALL}')
        for key, value in dados.items():
            print(f'{key}: {value}')
            print('-' * 40)
    except requests.exceptions.RequestException as e:
        print(f'{Fore.RED}Erro ao buscar dados:{Style.RESET_ALL}', e)

def buscar_telefone():
    tel = input('Digite o número de telefone com DDD (Ex: 5511998765432): ')
    url = f'http://apilayer.net/api/validate?access_key={api_key_numverify}&number={tel}&format=1'
    consulta_api(url, "INFORMAÇÕES DO NÚMERO")

def buscar_cep():
    cep = input('Digite o CEP (Ex: 01001000): ')
    url = f'https://brasilapi.com.br/api/cep/v1/{cep}'
    consulta_api(url, "INFORMAÇÕES DO CEP")

def buscar_cnpj():
    cnpj = input('Digite o CNPJ (Ex: 00000000000191): ')
    url = f'https://brasilapi.com.br/api/cnpj/v1/{cnpj}'
    consulta_api(url, "INFORMAÇÕES DO CNPJ")

def buscar_ddd():
    ddd = input('Digite o DDD (Ex: 11): ')
    url = f'https://brasilapi.com.br/api/ddd/v1/{ddd}'
    consulta_api(url, "INFORMAÇÕES DO DDD")

def buscar_bancos():
    url = 'https://brasilapi.com.br/api/banks/v1'
    
    try:
        r = requests.get(url, timeout=10)
        r.raise_for_status()
        bancos = r.json()  # Retorna uma lista, não um dicionário

        print(f'\n{Fore.GREEN}== LISTA DE BANCOS =={Style.RESET_ALL}')
        for banco in bancos[:10]:  # Exibe apenas os 10 primeiros para evitar flood
            print(f'Nome: {banco.get("name", "Desconhecido")}')
            print(f'Código: {banco.get("code", "Não disponível")}')
            print(f'ISPB: {banco.get("ispb", "Não disponível")}')
            print('-' * 40)
    
    except requests.exceptions.RequestException as e:
        print(f'{Fore.RED}Erro ao buscar bancos:{Style.RESET_ALL}', e)

def buscar_ibge():
    municipio = input('Digite o código do município IBGE: ')
    url = f'https://brasilapi.com.br/api/ibge/municipios/v1/{municipio}'
    consulta_api(url, "INFORMAÇÕES DO MUNICÍPIO (IBGE)")

def buscar_feriados():
    ano = input('Digite o ano (Ex: 2024): ')
    url = f'https://brasilapi.com.br/api/feriados/v1/{ano}'
    consulta_api(url, "FERIADOS NACIONAIS")

def buscar_fipe():
    url = 'https://brasilapi.com.br/api/fipe/marcas/v1'

    try:
        r = requests.get(url, timeout=10)
        r.raise_for_status()
        marcas = r.json()  # A resposta é uma lista

        print(f'\n{Fore.GREEN}== INFORMAÇÕES DA TABELA FIPE =={Style.RESET_ALL}')
        for marca in marcas:
            print(f'Código: {marca.get("codigo", "Desconhecido")}')
            print(f'Nome: {marca.get("nome", "Não disponível")}')
            print('-' * 40)

    except requests.exceptions.RequestException as e:
        print(f'{Fore.RED}Erro ao buscar FIPE:{Style.RESET_ALL}', e)

def buscar_isbn():
    isbn = input('Digite o ISBN do livro: ')
    url = f'https://brasilapi.com.br/api/isbn/v1/{isbn}'
    consulta_api(url, "INFORMAÇÕES DO LIVRO (ISBN)")

def buscar_dominio():
    dominio = input('Digite o domínio .br (Ex: exemplo.com.br): ')
    url = f'https://brasilapi.com.br/api/registrobr/v1/{dominio}'
    consulta_api(url, "INFORMAÇÕES DO DOMÍNIO BR")

def buscar_taxas():
    url = 'https://brasilapi.com.br/api/taxas/v1'

    try:
        r = requests.get(url, timeout=10)
        r.raise_for_status()
        taxas = r.json()  # Retorna uma lista, não um dicionário

        print(f'\n{Fore.GREEN}== TAXAS ATUAIS =={Style.RESET_ALL}')
        for taxa in taxas:
            print(f'Nome: {taxa.get("nome", "Desconhecido")}')
            print(f'Valor: {taxa.get("valor", "Não disponível")}')
            print(f'Data: {taxa.get("data", "Não disponível")}')
            print('-' * 40)

    except requests.exceptions.RequestException as e:
        print(f'{Fore.RED}Erro ao buscar taxas:{Style.RESET_ALL}', e)

def buscar_estabelecimentos():
    municipio = input('Digite o código IBGE do município: ')
    url = f'https://dadosabertos.saude.gov.br/api/recursos/estabelecimentos?municipio={municipio}'
    consulta_api(url, "ESTABELECIMENTOS DE SAÚDE")

def buscar_weather():
    cidade = input('Digite o nome da cidade: ')
    url = f'https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid=04a97a1a1f47e6e4707c9bd554b11e95&units=metric&lang=pt_br'
    consulta_api(url, "PREVISÃO DO TEMPO")

def buscar_currency():
    url = 'https://api.exchangerate-api.com/v4/latest/BRL'
    consulta_api(url, "TAXAS DE CÂMBIO")

def buscar_pib():
    url = 'https://api.brasil.io/v1/pib'
    consulta_api(url, "INFORMAÇÕES DO PIB BRASILEIRO")

def puxada_tg():
    print(f'\n{Fore.GREEN}== LINK DO TELEGRAM =={Style.RESET_ALL}')
    print("Puxada do Telegram: https://t.me/+jusXmTstvL8xMmZh")
    
    
def verificar_ip_abuseipdb():
    ip = input('Digite o IP para verificar no AbuseIPDB: ')
    url = f'https://api.abuseipdb.com/api/v2/check?ipAddress={ip}'
    headers = {'Key': api_key_abuseipdb, 'Accept': 'application/json'}

    try:
        r = requests.get(url, headers=headers, timeout=10)
        r.raise_for_status()
        dados = r.json()["data"]

        print(f'\n{Fore.GREEN}== RESULTADO ABUSEIPDB =={Style.RESET_ALL}')
        print(f'IP: {dados["ipAddress"]}')
        print(f'Abusos reportados: {dados["totalReports"]}')
        print(f'Nível de risco: {dados["abuseConfidenceScore"]}%')
        print(f'Última denúncia: {dados["lastReportedAt"]}')
        print('-' * 40)
    except requests.exceptions.RequestException as e:
        print(f'{Fore.RED}Erro ao verificar IP:{Style.RESET_ALL}', e)

def verificar_senha_vazada():
    senha = input('Digite a senha para verificar vazamento: ')
    hash_sha1 = hashlib.sha1(senha.encode()).hexdigest().upper()
    prefixo, sufixo = hash_sha1[:5], hash_sha1[5:]

    url = f'https://api.pwnedpasswords.com/range/{prefixo}'

    try:
        r = requests.get(url, timeout=10)
        r.raise_for_status()
        hashes = r.text.splitlines()

        for linha in hashes:
            hash_fim, contagem = linha.split(':')
            if hash_fim == sufixo:
                print(f'\n{Fore.RED}⚠ ALERTA! Essa senha já vazou {contagem} vezes!{Style.RESET_ALL}')
                return

        print(f'\n{Fore.GREEN}✅ Essa senha NÃO foi encontrada em vazamentos.{Style.RESET_ALL}')
    except requests.exceptions.RequestException as e:
        print(f'{Fore.RED}Erro ao verificar senha:{Style.RESET_ALL}', e)

# Início do programa
funcoes = [
    buscar_telefone, buscar_cep, buscar_cnpj, buscar_cpf, buscar_ddd, buscar_bancos,
    buscar_ibge, buscar_feriados, buscar_fipe, buscar_isbn, buscar_dominio, buscar_taxas,
    buscar_estabelecimentos, buscar_weather, buscar_currency, buscar_pib, puxada_tg, verificar_ip_abuseipdb,
    verificar_senha_vazada
]

while True:
    banner()
    for i, func in enumerate(funcoes, 1):
        print(f'{Fore.BLUE}[{i}] {func.__name__.replace("_", " ").title()}{Style.RESET_ALL}')
    print(f'{Fore.RED}[96] Fechar{Style.RESET_ALL}')


    opcao = input('- ')
    if opcao.isdigit() and 1 <= int(opcao) <= 19:
        funcoes[int(opcao) - 1]()
    elif opcao == '96':
        sys.exit()
    else:
        print(f'{Fore.RED}Comando inválido, tente novamente.{Style.RESET_ALL}')