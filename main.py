# Instalar as Bibliotecas que serão utilizados
# Usar no Terminal o Comando no CMD:
# pip install pandas pyautogui pywhatkit

import pandas as pd
import pyautogui as pa
import pywhatkit
from datetime import datetime
import time

def send_whatsapp_message(phone, message):
    try:
        # Envia a mensagem
        now = datetime.now()
        pywhatkit.sendwhatmsg(phone, message, now.hour, now.minute + 2)
        print(f"Mensagem enviada para {phone}")
    except Exception as e:
        print(f"Erro ao enviar mensagem para {phone}: {e}")

def main():
    # Lê o arquivo CSV
    try:
        contacts = pd.read_csv("novo_arquivo_processado_atualizado.csv")
    except FileNotFoundError:
        print("O arquivo novo_arquivo_processado_atualizado.csv não foi encontrado!")
        return

    if "Full_Name" not in contacts.columns or "Phone" not in contacts.columns:
        print("O arquivo CSV precisa ter as colunas 'Full_Name' e 'Phone'!")
        return

    # Definição das mensagens
    message1 = (
        "MENSAGEM 1"
    )

    message2 = (
        "MENSAGEM 2"
    )

    # Alterna entre as mensagens
    messages = [message1, message2]

    for index, row in contacts.iterrows():
        full_name = row["Full_Name"].strip().split()[0]  # Pega apenas o primeiro nome
        phone = row["Phone"].strip()

        # Verifica se o número tem o formato correto
        if not phone.startswith("+"):
            print(f"Número inválido para {full_name}: {phone}. Certifique-se de que inclui o código do país.")
            continue

        # Seleciona a mensagem alternadamente
        message = messages[index % 2].format(name=full_name)

        # Envia a mensagem
        send_whatsapp_message(phone, message)
        time.sleep(25)  # Aguarda para evitar bloqueio
        pa.press("enter")
        time.sleep(10)
        pa.hotkey("alt", "f4")  # Aperta a combinação de tecla Alt + f4 para fechar a janela
        time.sleep(10)  # Aguarda mais tempo entre os envios

if __name__ == "__main__":
    main()
