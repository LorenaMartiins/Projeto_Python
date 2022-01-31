import os
import pandas as pd
from fpdf import FPDF
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

planilha = pd.read_excel("Dados-covid-19-SP.xlsx")

# ---------- GRAFICO DA TABELA TOTAL SOMA = 12 A 60 ---------

# ---------- Gráfico Total --------------

ayes_x = [2020, 2021]
x_indexe = np.arange(len(ayes_x))
width = 0.10

total_y = [17906499200,  124227183500]
plt.axhline(y=17906499200, color="black", linestyle=":")
plt.axhline(y=124227183500, color="black", linestyle=":")
plt.bar(x_indexe, total_y, width=width, color='#FF7F50')
plt.xticks(ticks=x_indexe, labels=ayes_x)

plt.title("Casos Totais")
plt.xlabel("Ano")
plt.ylabel("Totais")

plt.savefig("grafico_total.png")
plt.close()

# ----------- Gráfico total de casos de dias ---------

ayes_x = [2020, 2021]
x_index3 = np.arange(len(ayes_x))
width = 0.10

casosd_y = [177736800, 299381100]

plt.axhline(y=177736800, color="black", linestyle=":")
plt.axhline(y=299381100, color="black", linestyle=":")
plt.bar(x_index3, casosd_y, width=width, color='#FC5A50')
plt.xticks(ticks=x_index3, labels=ayes_x)

plt.title("Casos/dia ")
plt.xlabel("Ano")
plt.ylabel("Totais")

plt.savefig("grafico_casosdia.png")
plt.close()

# ----------- Gráfico Óbitos/dia ---------

anos_x = [2020, 2021]
x_index4 = np.arange(len(anos_x))
width = 0.10

obito_y = [4671700, 10848800]
plt.axhline(y=4671700, color="black", linestyle=":")
plt.axhline(y=10848800, color="black", linestyle=":")
plt.bar(x_index4, obito_y, width=width, color='#808080')
plt.xticks(ticks=x_index4, labels=anos_x)

plt.title("Óbito/dia")
plt.xlabel("Ano")
plt.ylabel("Totais")

plt.savefig("grafico_obitodia.png")
plt.close()

# ------- Gráfico média -----------

plt.style.use("fivethirtyeight")

ayes_x = [2020, 2021]
x_indexes = np.arange(len(ayes_x))
width = 0.25

dev_y = [577630, 3403484]
plt.bar(x_indexes - width, dev_y, width=width,
        color="#444444", label="Média de casos")

py_dev_y = [471709, 820222]
plt.bar(x_indexes, py_dev_y, width=width,
        color="#008fd5", label="Média de casos/dia")

js_dev_y = [161000, 297000]
plt.bar(x_indexes + width, js_dev_y, width=width,
        color="#e5ae38", label="Óbitos")

plt.legend()

plt.xticks(ticks=x_indexes, labels=ayes_x)

plt.title("Médias totais")
plt.xlabel("Ano")
plt.ylabel("Media")

plt.tight_layout()

plt.savefig('grafico_media.png')
plt.close()

# --------- Gráfico porcentagem ---------

data = {'Casos/totais': 694, 'Casos/dia': 168, 'Óbito/dia': 232}

courses = list(data.keys())
values = list(data.values())

fig = plt.subplots(figsize=(20, 10))

plt.barh(courses, values, color='#008080')

plt.xlabel("Porcentagem(%)")
plt.title("Total %")
plt.savefig('grafico_totalporc.png')
plt.close()

# -------------- PDF ----------------


class PDF(FPDF):
    def header(self):
        self.image('kick.png', 10, 8, 33)
        self.set_font('Arial', 'B', 15)
        self.cell(80)
        self.cell(
            30, 10, 'PROJETO PYTHON', 0, 0, 'C')
        self.ln(10)
        self.line(75, 20, 135, 20)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')


pdf = PDF()
pdf.add_page()
texto_1 = 'A evolução do COVID-19 nos anos de 2020 e 2021 no estado de São Paulo.'
pdf.cell(w=0, h=120, txt=texto_1, align='C')
pdf.image(name='medico_covid.png', x=30, y=120, w=150)

pdf.set_font('Times', '', 17)

# ----------- Text -------------

pdf.add_page()
pdf.set_font('Times', '', 15)
texto = '\n   No final de dezembro de 2019 o mundo se deparou com um novo desafio, uma nova realidade que viria ser nos anos seguintes. A sociedade se deparou com um virús mortal chamado coronavírus, foi denominada oficialmente como COVID-19, (sigla em inglês para coronavirus disease 2019) .\n - É um vírus que causa doença respiratória pelo agente coronavírus, com casos recentes registrados em várias partes do mundo. Em casos extremos, pode levar a óbito.\n   A seguir veremos alguns gráficos que mostrará a evolução do COVID-19 no estado de São Paulo: '
pdf.multi_cell(w=185, h=8, txt=texto, align='J')

# ------- Tabelas e imagens ------
pdf.image(name='total_soma.png', x=30, y=120, w=150)
pdf.image(name='grafico_total.png', x=30, y=160, w=150)

pdf.add_page()
pdf.set_font('Times', '', 15)
pdf.image(name='grafico_casosdia.png', x=30, y=40, w=150)
pdf.image(name='grafico_obitodia.png', x=30, y=150, w=150)

pdf.add_page()
pdf.image(name='Total%.png', x=30, y=50, w=150)
pdf.image(name='grafico_totalporc.png', x=5, y=100, w=200)

pdf.add_page()
pdf.image(name='media.png', x=30, y=50, w=150)
pdf.image(name='grafico_media.png', x=30, y=120, w=150)

pdf.add_page()
pdf.set_font('Arial', 'B', 18)
pdf.image(name='covid.png', x=30, y=100, w=150)
nome = 'Lorena Martins de Farias - TURMA B - 2021/2022'
pdf.cell(w=0, h=80, txt=nome, align='C')

pdf.output('Covid-SP.pdf', 'F')

print("O PDF foi criado com sucesso!!")

os.system("pause")
