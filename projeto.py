import os
import pandas as pd
from fpdf import FPDF

planilha = pd.read_excel("Dados-covid-19-SP.xlsx")
casos_total = planilha["MEDIA DE CASOS"]

print(casos_total[0])

# titulo


class PDF(FPDF):
    def header(self):
        self.image('kick.png', 10, 8, 33)
        self.set_font('Arial', 'B', 15)
        self.cell(80)
        self.cell(
            30, 10, 'PROJETO PYTHON', 0, 0, 'C')
        self.ln(10)
        self.line(75, 20, 135, 20)


pdf = PDF()
pdf.add_page()
pdf.image(name='covid.png', x=30, y=150, w=150)
pdf.set_font('Times', '', 15)

# text
pdf.cell(20, 120, 'A evolução do COVID-19 nos anos 2020 e 2021 em São Paulo.')
pdf.cell(40, 500, ' No começo de 2020 a sociedade se deparou com um movo desafio, um novo começo de uma nova realidade. "O COVID-19" um virús')


pdf.output('Covid-SP.pdf', 'F')

os.system("pause")
