import tkinter as tk
from tkinter import messagebox
import sqlite3

# Function to handle the submit button click
def submit_data():
    # Get values from entry widgets
    nama_siswa = entry_nama.get()
    biologi = int(entry_biologi.get())
    fisika = int(entry_fisika.get())
    inggris = int(entry_inggris.get())

    # Calculate predicted faculty based on highest score
    if biologi > fisika and biologi > inggris:
        prediksi_fakultas = 'Kedokteran'
    elif fisika > biologi and fisika > inggris:
        prediksi_fakultas = 'Teknik'
    else:
        prediksi_fakultas = 'Bahasa'

    # Insert data into SQLite database
    conn = sqlite3.connect('D:\SMT 3\Multiplatform\Hasil Prediksi Fakultas\Hasil_prediksi.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS nilai_siswa (
            id INTEGER PRIMARY KEY,
            nama_siswa TEXT,
            biologi INTEGER,
            fisika INTEGER,
            inggris INTEGER,
            prediksi_fakultas TEXT
        )
    ''')
    cursor.execute('''
        INSERT INTO nilai_siswa (nama_siswa, biologi, fisika, inggris, prediksi_fakultas)
        VALUES (?, ?, ?, ?, ?)
    ''', (nama_siswa, biologi, fisika, inggris, prediksi_fakultas))
    conn.commit()
    conn.close()

    messagebox.showinfo('Info', 'Data submitted successfully!')

# Create the main window
root = tk.Tk()
root.title('Student Data Entry')

# Create labels and entry widgets
label_nama = tk.Label(root, text='Nama Siswa:')
label_nama.grid(row=0, column=0, padx=10, pady=10)
entry_nama = tk.Entry(root)
entry_nama.grid(row=0, column=1, padx=10, pady=10)

label_biologi = tk.Label(root, text='Biologi:')
label_biologi.grid(row=1, column=0, padx=10, pady=10)
entry_biologi = tk.Entry(root)
entry_biologi.grid(row=1, column=1, padx=10, pady=10)

label_fisika = tk.Label(root, text='Fisika:')
label_fisika.grid(row=2, column=0, padx=10, pady=10)
entry_fisika = tk.Entry(root)
entry_fisika.grid(row=2, column=1, padx=10, pady=10)

label_inggris = tk.Label(root, text='Inggris:')
label_inggris.grid(row=3, column=0, padx=10, pady=10)
entry_inggris = tk.Entry(root)
entry_inggris.grid(row=3, column=1, padx=10, pady=10)

# Create a submit button
submit_button = tk.Button(root, text='Submit', command=submit_data)
submit_button.grid(row=4, column=0, columnspan=2, pady=10)

# Run the Tkinter main loop
root.mainloop()