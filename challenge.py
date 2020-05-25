
import requests
import json
import hashlib

def extract_json(url_input, name_answer):
    '''
    :param url_input: Url que realizará a busca de uma estrutura json do site Codenation para realizar a descriptografia.
    :param name_answer: Nome do arquivo json que será criado.
    '''

    res = requests.get(url_input)
    arquivo_json = res.json()

    with open(name_answer, 'w') as json_file:
       json.dump(arquivo_json, json_file, indent=4)

def descriptar_json(name_answer):
    '''
    :param name_answer: Nome do arquivo json criado.
    '''
    with open(name_answer, 'r') as json_file:
        dados = json.load(json_file)

    string = dados['cifrado']
    string.split()

    alfa = 'abcdefghijklmnopkrstuvwxyz'

    new = list()
    word = ''

    for i in string:
        if i in alfa:
            num = alfa.find(i)
            num += -7
            new.append(alfa[num])
        elif i in ' ':
            new.append(' ')
        elif i in '()':
            new.append(i)
        elif i in '-,.':
            new.append(i)
        elif i in '0123456789':
            new.append(i)

    for j in new:
        word += j

    dados['decifrado'] = word

    with open(name_answer, 'w') as json_file:
        json.dump(dados, json_file, indent=4)


def hash(name_answer):
    '''
    :param name_answer: Nome do arquivo json criado.
    '''

    with open(name_answer, 'r') as json_file:
        dados = json.load(json_file)

        enconding = json_file.encoding

    data = hashlib.sha1(dados['decifrado'].encode(enconding)).hexdigest()
    dados['resumo_criptografico'] = data

    with open(name_answer, 'w') as json_file:
        json.dump(dados, json_file, indent=4)

def send_arq(path_answer, url_output):
    '''
    :param path_answer: Caminho do arquivo json criado que será enviado para o Codenation para avaliação do desafio.
    :param url_output: Url que saída que será encaminhado o arquivo json descriptografado.
    '''
    path = path_answer
    url = url_output
    files = {'answer': open(path, 'rb')}

    send = requests.post(url, files=files)

    send.text
    print(send.status_code)
    print(send.text)