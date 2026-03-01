from datetime import date


def get_cur_date():
    """Retorna a data atual no formato YYYY-MM-DD"""
    return date.today().strftime('%Y-%m-%d')


if __name__ == "__main__":
    data = get_cur_date()
    print(data)  # Saída: 202X-XX-XX