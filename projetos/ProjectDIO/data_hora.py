# Exibindo data:
from datetime import date, time, datetime, timedelta

def trabalhando_com_datetime():
    data_atual = datetime.now()
    print(data_atual)
    print(data_atual.strftime('%d/%m/%Y %H:%M:%S'))
    print(data_atual.strftime('%c'))
    print(data_atual.day)
    print(data_atual.year)
    print(data_atual.hour)
    print(data_atual.minute)
    print(data_atual.weekday())
    print(data_atual.month)
    #Traduzindo o datetime:
    #tupla no mesmo formato e sequencia que weekday
    tupla = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo')
    print(tupla[data_atual.weekday()])
    data_criada = datetime(2018, 6, 20, 15, 30, 20)
    print(data_criada)
    print(data_criada.strftime('%c'))
    data_string = '02/02/2021 12:12:21'
    data_convertida = datetime.strptime(data_string, '%d/%m/%Y %H:%M:%S')
    print(data_convertida)
    print(type(data_convertida))
    print(data_convertida.weekday())

    #subtrando data com timedelta
    nova_data = data_convertida - timedelta(days=365, hours=2, minutes=15)
    print(nova_data)


def trabalhando_com_date():
    data_atual = date.today()
    data_atual_str = data_atual.strftime('%A %B %Y')
    print(data_atual)
    # alterando para padrão brasileiro:
    print(data_atual.strftime('%d/%m/%Y'))
    print(data_atual.strftime('%d-%m-%y'))
    #docs.python.org (datetime)
    print(type(data_atual))
    print(data_atual_str)
    print(type(data_atual_str))

def trabalhando_com_time():
    horario = time(hour=15, minute=18, second=30)
    print(horario)
    print(type(horario))
    horario_str = horario.strftime('%H:%M:%S')
    print(horario_str)
    print(type(horario_str))

if __name__ == '__main__':
    trabalhando_com_datetime()
    # trabalhando_com_time()
    # trabalhando_com_date()
