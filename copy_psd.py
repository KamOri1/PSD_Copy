import tkinter as tk
import customtkinter as ctk
from tkinter import filedialog as fd
import shutil
import os
from PIL import Image


class CopyPSD:
    def __init__(self):
        self.app = tk.Tk(className=' Jarvis Project - PSD Magic')
        self.src_file = ""
        self.create_is_ok = False
        self.button_open_file = ''


    def open_window(self):
        self.app.geometry('600x450')
        self.app.configure(bg="#000")
        self.app.resizable(False, False)

    def label_info(self):
        if self.src_file.endswith('psd'):
            text_src_file = self.src_file
            text_color = '#FFFFFF'

        else:
            text_src_file = "Invalid file format"
            text_color = '#FF0033'


        text_var = tk.StringVar(value=text_src_file)
        label = ctk.CTkLabel(master=self.app,
                             textvariable=text_var,
                             width=600,
                             height=50,
                             fg_color=("#000", "#000"),
                             corner_radius=8,
                             wraplength=600,
                             text_color=text_color)
        label.place(relx=0.5, rely=0.06, anchor=tk.CENTER)

    def foto(self):

        label_image = ctk.CTkImage(Image.open("matrix18.jpg"), size=(450, 450))

        image_label = ctk.CTkLabel(master=self.app, image=label_image, text="")
        image_label.place(relx=0.3, rely=0.5, anchor=tk.CENTER)



    def open_file_function(self):
        self.src_file = fd.askopenfilename()
        self.label_info()

        return self.src_file

    def button_open_file_function(self, button_text, open_file_function, x, y,text_color, b_fg_color,hover_color=None):
        self.button_open_file = ctk.CTkButton(master=self.app, text=button_text, command=open_file_function,
                                          text_color=text_color, fg_color=b_fg_color, hover_color=hover_color)
        self.button_open_file.place(relx=x, rely=y, anchor=tk.CENTER)




    def copy_psd_18x(self):
        country = ['UK', 'PL', 'DE', 'AT', 'CHDE', 'NL', 'FR', 'CHFR', 'ES', 'PT', 'IT', 'DK', 'NO', 'FI', 'SE', 'CZ',
                   'SK', 'HU', ]
        org = self.src_file
        filename = os.path.basename(org)
        if filename.endswith('.psd'):
            for name in country:
                psd_file = self.src_file.replace(filename, name.lower() + filename)
                file_catalog = psd_file.replace(name.lower() + filename, "PSD_Catalog")
                if self.create_is_ok:
                    if not os.path.exists(file_catalog):
                        os.mkdir(file_catalog)
                    if os.path.exists(file_catalog + '\\' + name.lower() + filename):

                        continue
                    else:
                        os.mkdir(file_catalog + '\\' + name.upper())
                        shutil.copy2(self.src_file, file_catalog + '\\' + name.upper() + '\\' + name.lower() + filename)

                else:
                    if os.path.exists(psd_file):
                        print(f'File: {name.lower() + filename} alredy exists')
                        continue
                    else:
                        shutil.copy2(self.src_file, self.src_file.replace(filename, name.lower() + filename))
                self.end_info('Files have been created', '#ffffff')
        else:
            self.end_info('Invalid file format', '#FF0033')


    def end_info(self, text_var_, text_color):

            text_var = tk.StringVar(value=text_var_)
            label = ctk.CTkLabel(master=self.app,
                                 font=("Arial", 16),
                                 textvariable=text_var,
                                 width=190,
                                 height=50,
                                 fg_color=("#000", "#000"),
                                 corner_radius=8,
                                 text_color=text_color)
            label.place(relx=0.838, rely=0.8, anchor=tk.CENTER)




    def folder_create(self):
        if not self.create_is_ok:
            self.create_is_ok = True
            self.button_open_file.configure(fg_color='#689F38', hover_color='#689F38')
            return True
        else:
            self.create_is_ok = False
            self.button_open_file.configure(fg_color='#283593', hover_color='#283593')
            return False



    def close(self):

        self.app.destroy()

    def start_loop(self):
        self.app.mainloop()



