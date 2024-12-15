import base64

def create_basic_authentication_header(phone, password):
    value = f'{phone}:{password}'
    encoded_value = base64.b64encode(value.encode()).decode()
    return f'Basic {encoded_value}'

