import PySimpleGUI as sg
sg.theme("DarkGreen4")
sg.theme_text_color("#FFFF00")
window = sg.Window(title="Profile", layout=[[sg.Text("SELAMAT DATANG DI KELAS", font=("Arial",25,"italic","bold","underline"))],
                                            [sg.Text("NPM       : 2210010049")],
                                            [sg.Text("NAMA    : DIAH KURNIAWATI")],
                                            [sg.Text("Kelas       : 5E Reguler Banjarmasin")],
                                            [sg.Text("Matkul     : Pemograman Visual 3")],
                                            ],
                                    size=(510,200),
                                    font=("Times", 18))
window()
window.close()