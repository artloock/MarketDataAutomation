import yfinance
import pyautogui
import pyperclip
import webbrowser
import time

# Ask the stock code and dates.
ticker = input("Enter the desired stock code: ")
if not ticker.endswith(".SA"):
    ticker += ".SA"
star_date = input("Desired start date (YYYY-MM-DD): ")
end_date = input("desired end date (YYYY-MM-DD): ")

# Dowload historical data
try:

    data = yfinance.Ticker(ticker).history(start = star_date, end = end_date)

    if data.empty:
        print(f"No data found for the stcok {ticker} from {star_date} to {end_date}")
    else:
        close = data.Close
        closemax = round(close.max(), 2)
        closemin = round(close.min(), 2)
        closemean = round(close.mean(), 2)

        # Email details
        destinatario = 'email@exemple.com'
        assunto = 'Stock Analysis'
        mensagem = f"""
        Dear manager,

        Here is the requested analysis for the stock {ticker}:

        Maximum closing price: R${closemax}
        Minimum closing price: R${closemin}
        Average closing price: R${closemean}

        If you have any questions, please let me know.

        Best regards,
        """

        # Acces gmail
        webbrowser.open("https://mail.google.com")
        time.sleep(4)

        # pause 3s
        pyautogui.PAUSE = 3

        # Click the compose buton
        pyautogui.click(x=120, y=257)

        # Tipe the recipient's email
        pyperclip.copy(destinatario)
        pyautogui.hotkey("ctrl", "v")
        pyautogui.hotkey("tab")

        # Tipe the email Subject
        pyperclip.copy(assunto)
        pyautogui.hotkey("ctrl", "v")
        pyautogui.hotkey("tab")

        # Tipe the email body
        pyperclip.copy(mensagem)
        pyautogui.hotkey("ctrl", "v")

        # send the email
        pyautogui.click(x=2419, y=1315)

        #close Gmail
        pyautogui.click("ctrl", "f4")

        print('Email enviado com sucesso!')
except Exception as e:
    print(f"Error feching data for the stock {ticker}: {e}")