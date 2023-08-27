import requests
import pandas as pd
import base64

class DadosRepositorios:
    def __init__(self, owner):
        self.owner = owner
        self.endpoint = 'https://api.github.com'
        self.access_token = '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'
        self.headers = {'X-GitHub-Api-Version': '2022-11-28', 'Authorization': 'Bearer ' + self.access_token}

    def lista_repositorios(self):
        repos_list = []
        for page_num in range(1, 20):
            try:
                url_page = f'{self.endpoint}/users/{self.owner}/repos?page={page_num}'
                response = requests.get(url_page, headers=self.headers)
                repos_list.append(response.json())
            except:
                repos_list.append(None)
        return repos_list

    def nomes_repos(self, repos_list):
        repos_name = []
        for page in repos_list:
            for repo in page:
                repos_name.append(repo['name'])
        return repos_name

    def nomes_linguagens(self, repos_list):
        repos_language = []
        for page in repos_list:
            for repo in page:
                repos_language.append(repo['language'])
        return repos_language
    
    def cria_df_linguagens(self):

        repositorios = self.lista_repositorios()
        nomes = self.nomes_repos(repositorios)
        linguagens = self.nomes_linguagens(repositorios)

        df = pd.DataFrame()
        df['repository_name'] = nomes
        df['language'] = linguagens
        df['owner'] = self.owner

        return df

lista_owners = ['amzn', 'netflix', 'spotify']

df = pd.DataFrame()

for i in lista_owners:
    rep = DadosRepositorios(i)
    ling_usadas = rep.cria_df_linguagens()
    path_i = 'dados/linguagens_' + i +'.csv'
    df.to_csv(path_i)
    df = pd.concat([df, ling_usadas], ignore_index = True)

path = 'dados/linguagens_consolidado.csv'
df.to_csv(path)
