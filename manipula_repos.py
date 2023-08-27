import requests
import base64

class ManipulaRepositorios:
    def __init__(self, username):
        self.username = username
        self.endpoint = 'https://api.github.com'
        self.access_token = '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'
        self.headers = {'X-GitHub-Api-Version': '2022-11-28', 'Authorization': 'Bearer ' + self.access_token}

    def criaRepo(self, nome_repo):
        data = {
            'name': nome_repo,
            'description': 'Repositório com as linguagens utilizadas',
            'private': False
        }
        response = requests.post(f'{self.endpoint}/user/repos', json=data, headers=self.headers)
        print(f'status_code criação do repositório: {response.status_code}')

    def add_arquivo(self, nome_repo, nome_arquivo, caminho_arquivo):
        
        # Codificação dos arquivos
        with open(caminho_arquivo, "rb") as file:
            file_content = file.read()
        encoded_content = base64.b64encode(file_content)

        # Realizando o upload
        url_upload = f'{self.endpoint}/repos/{self.username}/{nome_repo}/contents/{nome_arquivo}'
        data = {
            'message': 'Adicionando um novo arquivo',
            'content': encoded_content.decode('utf-8')
        }

        response = requests.put(url_upload, json=data, headers=self.headers)
        print(f'status_code upload do arquivo: {response.status_code}')

# Instanciando um objeto
username = 'felipesbreve'
novo_repo = ManipulaRepositorios(username)

# Criando um repositório
nome_repo = 'linguagens-utilizadas'
novo_repo.criaRepo(nome_repo)

# Adicionando arquivos salvos
novo_repo.add_arquivo(nome_repo, 'linguagens_consolidado.csv', 'dados/linguagens_consolidado.csv')