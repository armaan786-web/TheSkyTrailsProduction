import requests


def send_whatsapp_message(api_key, mobile_number, message):
    url = "https://api.bulkwhatsapp.net/wapp/api/send"

    payload_data = {
        "apikey": api_key,
        "mobile": mobile_number,
        "msg": message,
        # Add other payload parameters as needed
    }

    response = requests.post(url, data=payload_data)

    return response