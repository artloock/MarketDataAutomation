import yfinance as yf
import pandas as pd
import smtplib
from email.message import EmailMessage 
from dotenv import load_dotenv
import os
import time

load_dotenv()

def extrair_dados(ticker, inicio, fim):
    """Extrai dados históricos usando a biblioteca yfinance."""
    if not ticker.endswith(".SA"):
        ticker += ".SA"
    
    try:
        print(f"Buscando dados para {ticker}...")
        data = yf.Ticker(ticker).history(start=inicio, end=fim)
        return data
    except Exception as e:
        print(f"Erro na extração: {e}")
        return pd.DataFrame()

def transformar_dados(data):
    """Realiza os cálculos estatísticos dos preços de fecho."""
    if data.empty:
        return None
    
    stats = {
        "max": round(data.Close.max(), 2),
        "min": round(data.Close.min(), 2),
        "mean": round(data.Close.mean(), 2)
    }
    return stats

def enviar_email(destinatario, assunto, corpo):
    """Envia o relatório via SMTP sem interrupção da interface."""
    # Configurações do servidor (Exemplo para Gmail)
    SENDER_EMAIL = os.getenv("EMAIL_USER")
    SENDER_PASSWORD = os.getenv("EMAIL_PASS")

    msg = EmailMessage()
    msg.set_content(corpo)
    msg['Subject'] = assunto
    msg['From'] = SENDER_EMAIL
    msg['To'] = destinatario

    try:
        print("A conectar ao servidor de e-mail...")
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(SENDER_EMAIL, SENDER_PASSWORD)
            smtp.send_message(msg)
        print("✅ E-mail enviado com sucesso via SMTP!")
    except Exception as e:
        print(f"❌ Falha ao enviar e-mail: {e}")

def gerar_relatorio_texto(ticker, stats):
    """Prepara o corpo da mensagem."""
    mensagem = f"""
    Análise da ação {ticker}:
    - Preço Máximo: R${stats['max']}
    - Preço Mínimo: R${stats['min']}
    - Preço Médio: R${stats['mean']}
    """
    return mensagem

if __name__ == "__main__":
    # Interface simples via terminal
    ticker_input = input("Código da ação: ")
    data_ini = input("Data início (YYYY-MM-DD): ")
    data_fim = input("Data fim (YYYY-MM-DD): ")

    # Fluxo principal
    df_precos = extrair_dados(ticker_input, data_ini, data_fim)
    
    if not df_precos.empty:
        resultados = transformar_dados(df_precos)
        relatorio = gerar_relatorio_texto(ticker_input, resultados)
        
        print("\n--- Relatório Gerado ---")
        print(relatorio)
        
        # Agora chamamos o envio de e-mail de verdade!
        enviar_email(
            destinatario="email-do-gerente@exemplo.com", 
            assunto=f"Análise de Mercado: {ticker_input}", 
            corpo=relatorio
        )
    else:
        print("Falha ao gerar análise.")