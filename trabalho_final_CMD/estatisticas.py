from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Crie um arquivo PDF em branco
pdf_estatisticas = canvas.Canvas("estatisticas.pdf", pagesize=letter)

# Defina o título do documento
pdf_estatisticas.setTitle("Documento PDF de Estatísticas")

# Adicione texto ao PDF
pdf_estatisticas.drawString(100, 750, evento, participante)

# Salve o arquivo PDF
pdf_estatisticas.showPage()
pdf_estatisticas.save()
print("PDF criado com sucesso.")