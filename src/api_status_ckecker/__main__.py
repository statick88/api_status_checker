from api_status import check_status

if __name__ == "__main__":
    url = input('Ingrese la URL de la API: ')
    status = check_status(url)
    print(f'El status de la API es: {status}')
