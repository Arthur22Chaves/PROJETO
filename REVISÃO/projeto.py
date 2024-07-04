from google.cloud import vision
from google.oauth2 import service_account

# Carrega as credenciais da conta de serviço
credentials = service_account.Credentials.from_service_account_file(
    'caminho/para/seu/arquivo-de-credenciais.json')

# Cria o cliente da API do Google Vision AI
vision_client = vision.ImageAnnotatorClient(credentials=credentials)

# Carrega a imagem
with open('image.jpg', 'rb') as image_file:
    image = vision.Image(content=image_file.read())

# Chama a API de reconhecimento de texto
response = vision_client.text_detection(image=image)
texts = response.text_annotations

# Extrai o texto reconhecido
for text in texts:
    print(text.description)