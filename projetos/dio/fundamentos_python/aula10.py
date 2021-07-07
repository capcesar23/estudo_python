'''
    Como recuperar a data atual(date)
    Como trabalhar com a data, alterando sua formatação
    Como gerar um horario(time)
    retorna dara e hora atual(datetime)
    Alterando formação do datetime
    Realizar soma e subtração de datas com timedelta
'''
from datetime import date, time, datetime, timedelta

def trabalhando_com_datetime():
    data_atual = datetime.now
    print(data_atual)
    print(data_atual.strftime("%d/%m/%Y"))

def trabalhando_com_date():
    data_atual = date.today()
    data_atual_str = data_atual.strftime("%A %B %Y")
    print(data_atual.strftime("%d / %m / %Y"))# usar aspas duplas
    print(data_atual_str)


if __name__ == '__main__':
    trabalhando_com_date()