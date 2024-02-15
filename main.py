import pyttsx3,PyPDF2

PdfReader=PyPDF2.PdfReader(open('Archers_Voice.pdf','rb'))
speaker = pyttsx3.init()

for page_num in range(len(PdfReader.pages)):
    text=PdfReader.pages[page_num].extract_text()
    clean_text = text.strip().replace('\n','')
    print(clean_text)

speaker.save_to_file(clean_text,'Archersvoice.mp3')
speaker.runAndWait()

speaker.stop()