import pyttsx3
import PyPDF2

book = open('Loremipsum.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
engine = pyttsx3.init()

for num in range(8, pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    voices = engine.getProperty('voices') 
    engine.setProperty('voice', voices[1].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 125)
    engine.say(text)
    engine.runAndWait() 