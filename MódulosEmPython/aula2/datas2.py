from datetime import datetime
from calendar import monthrange

ultimos_dias_de_meses_do_ano_atual = [
    monthrange(datetime.now().year, mes)[1] for mes in range(1, 13)
]
print('Ultimos dias de cada mês do ano do ano', ultimos_dias_de_meses_do_ano_atual)