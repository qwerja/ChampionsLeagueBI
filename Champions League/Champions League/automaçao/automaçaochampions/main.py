import pandas as pd
import requests
from bs4 import BeautifulSoup


def get_first_valid_image_url(query):
    """Obtém a URL da primeira imagem válida do Google Imagens, ignorando o logo do Google."""
    search_url = f"https://www.google.com/search?tbm=isch&q={query}"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(search_url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        img_tags = soup.find_all("img")

        for img_tag in img_tags:
            img_url = img_tag.get("src")
            if img_url and not img_url.startswith("/images/branding/"):
                return img_url
    return None


# Carregar a planilha
df = pd.read_excel("logotimes.xlsx")

# Criar colunas vazias para imagens
df["Logo URL"] = ""
df["Stadium URL"] = ""

# Processar cada time
for index, row in df.iterrows():
    team_name = row["Time"]  # Ajuste conforme o nome da coluna

    # Buscar URL da logo
    df.at[index, "Logo URL"] = get_first_valid_image_url(f"{team_name} logo png sem fundo")

    # Buscar URL da imagem do estádio
    df.at[index, "Stadium URL"] = get_first_valid_image_url(f"{team_name} estádio")

# Salvar a planilha atualizada
df.to_excel("logotimes_atualizado.xlsx", index=False)
