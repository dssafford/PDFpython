from fpdf import FPDF
import pandas as pd


pdf = FPDF(orientation="P", unit="mm", format="A4")
df = pd.read("topics.csv")


pdf.add_page()
pdf.set_font(family="Times", style="B", size=14)
pdf.cell(w=0,h=12,txt="eat shit douglas", align="L",ln=1, border=1)

pdf.set_font(family="Times", style="B", size=8)
pdf.cell(w=0,h=12,txt="take the package douglas", align="L",ln=1, border=1)


pdf.add_page()
pdf.set_font(family="Times", style="B", size=12)
pdf.cell(w=0,h=12,txt="eat shit douglas", align="L",ln=1, border=1)

pdf.set_font(family="Times", style="B", size=8)
pdf.cell(w=0,h=12,txt="take the package douglas", align="L",ln=1, border=1)

pdf.output("output.pdf")