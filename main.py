import openai

#api key é individual e encontrada no site da openai, caso pare de pegar, gere uma nova key e substitua
openai.api_key = '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'

#digite nessa var a imagem a ser gerada
img = "tijolo com chapeu mexicano"

response = openai.Image.create(prompt=img, n=1, size='1024x1024')

img_url = response['data'][0]['url']
print(f'URL da imagem gerada: {img_url}')
