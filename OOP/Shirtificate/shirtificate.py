from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("Helvetica", "B", 36)
        self.ln(10)
        self.cell(text = "CS50 Shirtificate", center = True)
        self.ln(30)
        self.image("C:/Code/trainings_center/OOP/Shirtificate/shirtificate.png", x = "C" )

def main():
    create_shirtificate(input("Your name: "))

def create_shirtificate(student_name):
    pdf = PDF()
    pdf.add_page()
    pdf.ln(-150)
    pdf.set_font("Helvetica", "B", 24)
    pdf.set_text_color(r = 255, g = 255, b = 255)
    pdf.cell(text = f"{student_name} took CS50P", center = True)
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()
