from fpdf import FPDF
import pandas as pd


pdf = FPDF(orientation="P", unit="mm", format="A4")

df = pd.read_csv("topics.csv")
for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L",
             ln=1)  # Height and Text size keep same or near to each other
    pdf.line(10, 21, 200, 21)

pdf.output("output.pdf")

# Below code is for creating page manually
# pdf.set_font(family="Times", style="B", size=12)
#     # pdf.cell(w=0, h=12, txt="Hi There", align="L",
#     #          ln=1, border=1)
