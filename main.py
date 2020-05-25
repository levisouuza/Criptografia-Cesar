
from include.Challenge import support
import time

path_answer = '/home/levi/PycharmProjects/PyFinance/venv/include/Challenge/answer.json'
answer = '/home/levi/PycharmProjects/PyFinance/venv/include/Challenge/answer.json'
input = 'https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=36fcccf1f3177ed1742363574a17c3b4190e8b19'
output = 'https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=36fcccf1f3177ed1742363574a17c3b4190e8b19'

#função que realizará a extração dos dados da Codenation via json.
support.extract_json(input, answer)

time.sleep(1)

#função que realizará a descriptografia dos dados.
support.descriptar_json(answer)

time.sleep(1)

#função que realizará um resumo_criptografico da frase descriptografada via hash sha1.
support.hash(answer)

time.sleep(1)

#função que enviará um json para a Codenation avaliar o desafio.
support.send_arq(path_answer, output)

exit()