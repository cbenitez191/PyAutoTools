import fitz  # PyMuPDF
import os

def compress_pdf(input_pdf_path, output_pdf_path, quality=50):
    pdf = fitz.open(input_pdf_path)
    pdf_writer = fitz.open()
    
    for page_num in range(pdf.page_count):
        page = pdf[page_num]
        
        pix = page.get_pixmap(matrix=fitz.Matrix(1, 1), alpha=False)
        
        pix.save(f"temp_img.png", dpi=quality)
        img_pdf = fitz.open("temp_img.png")
        pdf_writer.insert_pdf(img_pdf)
        img_pdf.close()
    
    pdf_writer.save(output_pdf_path)
    pdf_writer.close()
    pdf.close()
    
    os.remove("temp_img.png")
    print(f"PDF comprimido guardado como {output_pdf_path}")

input_pdf_path = "archivo_original.pdf"
output_pdf_path = "archivo_comprimido.pdf"
compress_pdf(input_pdf_path, output_pdf_path, quality=70)
