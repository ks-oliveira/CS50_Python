from fpdf import FPDF

class PDF(FPDF):
    def __init__(self, name):
        self._pdf = FPDF()
        self._pdf.add_page()
        self.header()
        self.shirt()
        self.content(name)

    def header(self):
        self._pdf.set_font("helvetica", "B", 16)
        self._pdf.cell(0, 60, "CS50 Shirtificate", new_x="LMARGIN", new_y="NEXT", align='C')

    def shirt(self):
        self._pdf.image("shirtificate.png", w=self._pdf.epw)

    def content(self, name):
        self._pdf.set_font_size(30)
        self._pdf.set_text_color(255,255,255)
        self._pdf.text(60, 140, text=f"{name} took CS50")

    def save(self, name):
        self._pdf.output(name)

def main():
    name = input("Name: ")
    pdf = PDF(name)
    pdf.save("shirtificate.pdf")


if __name__ == "__main__":
    main()
