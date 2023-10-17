import openai
import os

# Carga las variables de entorno desde el archivo .env
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

# Configura tu clave de API de OpenAI desde la variable de entorno
openai.api_key = os.getenv("OPENAI_API_KEY")

# Función para obtener una respuesta del modelo
def get_gpt3_response(input_text):
    response = openai.Completion.create(
        engine="text-davinci-002",  # Puedes elegir el modelo apropiado
        prompt=input_text,
        max_tokens=50  # Límite de longitud de la respuesta
    )
    return response.choices[0].text

while True:
    # Obtener la entrada del usuario
    user_input = input("Pregunta al chatbot (o escribe 'salir' para terminar): ")

    if user_input.lower() == 'salir':
        break

    # Obtener la respuesta del modelo GPT-3
    response = get_gpt3_response(user_input)

    # Mostrar la respuesta en la interfaz del chatbot
    print("Respuesta del chatbot:", response)
