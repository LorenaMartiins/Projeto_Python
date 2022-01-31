import os
import pandas as pd
from fpdf import FPDF
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

planilha = pd.read_excel("Dados-covid-19-SP.xlsx")


plt.style.use("fivethirtyeight")

ages_x = [2020, 2021]
x_indexes = np.arange(len(ages_x))
width = 0.25

dev_y = [577629.01, 3403484.48]
plt.bar(x_indexes - width, dev_y, width=width,
        color="#444444", label="Media de casos")

py_dev_y = [471097, 820222]
plt.bar(x_indexes, py_dev_y, width=width,
        color="#008fd5", label="Media de casos/dia")

js_dev_y = [161000, 297000]
plt.bar(x_indexes + width, js_dev_y, width=width,
        color="#e5ae38", label="Obitos")

plt.legend()

plt.xticks(ticks=x_indexes, labels=ages_x)

plt.title("Median Salary (USD) by Age")
plt.xlabel("Ano")
plt.ylabel("Media")


plt.tight_layout()

plt.savefig('grafico_media.png')
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
texto_1 = 'A evolução do COVID-19 nos anos 2020 e 2021 em São Paulo.'
pdf.cell(w=0, h=120, txt=texto_1, align='C')
pdf.image(name='covid.png', x=30, y=150, w=150)
pdf.set_font('Times', '', 17)

# ----------- Text -------------
pdf.add_page()
pdf.set_font('Times', '', 15)
pdf.set_margins(10, 40, 0)
texto = '   No final de dezembro de 2019 o mundo se deparou com um novo desafio, uma nova realidade que viria ser nos anos seguintes. A sociedade se deparou com um virús mortal chamado coronavírus, foi denominada oficialmente como COVID-19, (sigla em inglês para coronavirus disease 2019) .\n   - É um vírus que causa doença respiratória pelo agente coronavírus, com casos recentes registrados em várias partes do mundo. Em casos extremos, pode levar a óbito. '
pdf.multi_cell(w=185, h=8, txt=texto, align='J')

pdf.image()

pdf.output('Covid-SP.pdf', 'F')

plt.show()

os.system("pause")
