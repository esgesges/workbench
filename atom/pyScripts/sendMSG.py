import network
import urequests
import time

def connect_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while not wlan.isconnected():
        print('Connecting to WiFi...')
        time.sleep(1)
    print('Connected to WiFi:', wlan.ifconfig())

def sendToTelegram(botToken, chat_id, text):
    url = f'https://api.telegram.org/bot{botToken}/sendMessage?chat_id={chat_id}&text={text}'
    try:
        response = urequests.get(url)
        if response.status_code != 200:
            print("Error sending message to Telegram, status code:", response.status_code)
        else:
            print("Message sent successfully")
    except Exception as e:
        print("Exception occurred:", e)
    finally:
        if 'response' in locals():
            response.close()

def main():
    ssid = 'your_wifi_ssid'
    password = 'your_wifi_password'
    connect_wifi(ssid, password)

    botToken = "7090375373:AAHN8HKUGn40dg5FYJb30nQ0K63TJW4dwOE"
    chat_id = "your_chat_id"
    text = "server active."

    while True:
        sendToTelegram(botToken, chat_id, text)
        time.sleep(10)  # Delay to avoid overwhelming the network or server

if __name__ == "__main__":
    main()