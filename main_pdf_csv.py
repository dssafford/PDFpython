from fpdf import FPDF
import pandas as pd


pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)
df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()

    # Header
    pdf.set_font(family="Times", style="B", size=14)
    pdf.set_text_color(0,0,254)
    pdf.cell(w=0,h=12,txt=row["Topic"], align="L",ln=1)
    pdf.line(x1=10,y1=21,x2=200,y2=21)

    # Footer
    pdf.ln(265)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(0, 254, 0)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R", ln=1)

    for i in range(row["Pages"]-1):
        pdf.add_page()

        # Footer
        pdf.ln(277)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(0, 254, 0)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R", ln=1)


pdf.output("output1.pdf")