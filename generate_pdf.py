from fpdf import FPDF
import os

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 15)
        self.cell(0, 10, 'Engagement Level Prediction Report', 0, 1, 'C')
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.set_fill_color(200, 220, 255)
        self.cell(0, 6, title, 0, 1, 'L', 1)
        self.ln(4)

    def chapter_body(self, body):
        self.set_font('Arial', '', 11)
        self.multi_cell(0, 5, body)
        self.ln()

    def add_image(self, image_path, title):
        if os.path.exists(image_path):
            self.add_page()
            self.chapter_title(title)
            self.image(image_path, x=10, y=None, w=190)
        else:
            print(f"Warning: Image not found at {image_path}")

def create_pdf():
    pdf = PDF()
    pdf.add_page()

    # 1. Metin Raporunu Ekle
    pdf.chapter_title("Model Performance Summary")
    
    text_content = ""
    try:
        with open('model_performance_report.txt', 'r') as f:
            text_content = f.read()
    except FileNotFoundError:
        text_content = "Performance report file not found."
    
    pdf.chapter_body(text_content)

    # 2. Resimleri Ekle
    pdf.add_image('confusion_matrix.png', 'Confusion Matrix')
    pdf.add_image('feature_importance.png', 'Feature Importance')

    # Kaydet
    output_path = 'Engagement_Analysis_Report.pdf'
    pdf.output(output_path, 'F')
    print(f"PDF Report generated successfully: {output_path}")

if __name__ == '__main__':
    create_pdf()
