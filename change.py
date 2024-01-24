from spire.pdf import PdfDocument, FileFormat
from tkinter import filedialog, Tk, StringVar, Label, Button
from os import path

def convert_to_svg():
    # Ielādēt PDF failu
    files = filedialog.askopenfilenames(filetypes=[("PDF Files", "*.pdf")])
    i = 0
    for file_path in files:
        countVar.set(f"Konvertētie faili: {i} no {len(files)}")
        amount_label.update()
        if file_path:
            print(file_path)
            # Create a PdfDocument object
            doc = PdfDocument()
            # Load an SVG file
            doc.LoadFromFile(file_path)
            head, tail = path.split(file_path)
            textVar.set(f"Konvertēju: {tail}")
            status_label.update()

            tail = tail.replace(".pdf", ".svg")            
            # Save the SVG file to PDF format
            doc.SaveToFile(f"{head}/{tail}", FileFormat.SVG)
            # Close the PdfDocument object
            doc.Close()
            i = i+1
            countVar.set(f"Konvertētie faili: {i} no {len(files)}")
            amount_label.update()

    # Paziņot par veiksmīgu konvertāciju
    textVar.set("Konvertācija veiksmīga!")

# Izveidot Tkinter logrīku
root = Tk()
root.title("PDF uz SVG konvertācija")

textVar = StringVar()
textVar.set("Konvertētājs ir gatavs")

status_label = Label(root, textvariable=textVar)
status_label.pack(pady=20, padx=40)

countVar = StringVar()
amount_label = Label(root, textvariable=countVar)
amount_label.pack(pady=20, padx=20)

# Pievienot pogu un teksta etiķeti
convert_button = Button(root, text="Konvertēt uz SVG", command=convert_to_svg)
convert_button.pack(pady=20, padx=20)

# Palikt logrīka main loop
root.mainloop()