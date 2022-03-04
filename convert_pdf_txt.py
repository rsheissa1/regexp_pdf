import pdftotext

# Load your PDF file
with open("CVU_Completo.pdf",  'rb') as f1:
    pdf = pdftotext.PDF(f1)

# Save all text to a txt file
with open('output.txt', 'w') as f2:
    f2.write("\n\n".join(pdf))

f2.close()
f1.close()
