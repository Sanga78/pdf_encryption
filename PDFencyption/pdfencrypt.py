import PyPDF2
import securepassword
def pdfEncrypt(pdfFile):
    file = open(pdfFile, 'rb')
    reader = PyPDF2.PdfReader(file)
    writer = PyPDF2.PdfWriter()

    for page_number in range(len(reader.pages)):
        writer.add_page(reader.pages[page_number])

    #add password
    password = securepassword.get_secure_password("Enter your password: ")
    print("You entered:", password)
    writer.encrypt(password)

    #Secured.pdf is the name of the encrpted pdf file
    encryptedPdf = open('Secured.pdf', 'wb')   
    writer.write(encryptedPdf)
    encryptedPdf.close()
    print('File was encrypted successfully')

#replace NAME.pf with the pdf file you want to be encrypted

if __name__ == "__main__":
    pdfEncrypt('NAME.pdf')
