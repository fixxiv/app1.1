import requests
import json
import dict_regions
import tkinter as tk
from tkinter import ttk

dc_data = dict_regions.dict_reg.keys()
dc_data = list(dc_data)

def callback(event):
    c = lblCombo.get()
    assert isinstance(c, str)
    do_url = dict_regions.dict_reg.get(c)
    url = 'https://xn--80aesfpebagmfblc0a.xn--p1ai/covid_data.json?do=region_stats&code=' + do_url
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
    data = requests.get(url, headers=headers)
    data = json.loads(data.text)  # теперь данные - это список словарей
    new = int(data[0].get('sick')) - int(data[1].get('sick'))  # Получаем вновь выявленных

    lblData2.configure(text=c + ' ' + data[0].get('date'))
    lblData3.configure(text='Всего заболевших: ' + str(data[0].get('sick')))
    lblData4.configure(text='Вновь выявленных: ' + str(new))


window = tk.Tk()
window.iconbitmap('favicon.ico')
window.geometry('400x500')
window.resizable(False, False)
window.title('COVID-19')
window.config(bg='grey30')
ttk.Style().configure('TCombobox', padding=5)

# ttk.Style().configure('TLabel', padding=15, relief='flat')

labelTop = tk.Label(window, text='Выбрать регион', font=('Arial Bold', 14))
labelTop.grid(column=0, row=0)
labelTop.config(bg='grey30', fg='white')

lblData2 = tk.Label(window, text='', font=('Arial Bold', 12))
lblData2.grid(column=0, row=2)
lblData2.config(bg='grey30', fg='white')


lblData3 = tk.Label(window, text='', font=('bold italic', 12))
lblData3.grid(column=0, row=3)
lblData3.config(bg='grey30', fg='white')

lblData4 = tk.Label(window, text='', font=('bold italic', 12))
lblData4.grid(column=0, row=4)
lblData4.config(bg='grey30', fg='white')


lblCombo = ttk.Combobox(window, values=dc_data, height=27, width='30', state='readonly', font=('Arial Bold', 12))
lblCombo.grid(column=0, row=1)
lblCombo.current(0)
lblCombo.bind('<<ComboboxSelected>>', callback)

window.mainloop()
