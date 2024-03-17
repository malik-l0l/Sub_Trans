from deep_translator import GoogleTranslator
from tkinter import messagebox, filedialog, END, StringVar
from customtkinter import CTk, CTkLabel, CTkButton, CTkFrame, CTkProgressBar, CTkEntry, CTkComboBox

from lanuages import language

API_CHARACTER_LIMIT = 4999


# ========================== METHODS =================================
def select_input_file():
    # 1. Delete text inside the "Subtitle file :" entry box
    # 2. Ask to select a file
    # 3. insert file location into "Subtitle file :" entry box

    input_file_location_entry.delete(0, END)

    input_filepath = filedialog.askopenfilename(
        title="Select subtitle file.",
        filetypes=(
            ('text files', '*.txt'),
            ('srt files', '*.srt'),
            ('all files', '*.*')
        )
    )

    # print("Input_filepath : ", input_filepath)

    input_file_location_entry.insert(0, input_filepath)


def select_output_dir():
    # 1. Delete text inside the "Output locn :" entry box
    # 2. Ask to select a folder
    # 3. insert folder location into "Subtitle file :" entry box

    output_location_entry.delete(0, END)

    output_filepath = filedialog.askdirectory(
        initialdir="C:\\Users\\ACER\\Desktop",
        title="Select output folder.",
    )

    # print("Output_filepath : ", output_filepath)

    output_location_entry.insert(0, output_filepath)


def convert():
    try:
        # file location : "C:/Users/ACER/Desktop/test/srt_file.srt"
        file_locn = input_file_location_entry.get()

        # to get the file name : "srt_file"
        name = ""
        for i in range(len(file_locn) - 5, 0, -1):
            if file_locn[i] == "/":
                break
            else:
                name += file_locn[i]
        # print(name[::-1]) # -> "srt_file"

        # to divide the big_file into multiple small file with 4999 characters
        input_file = open(file_locn, "r", encoding="utf8")
        file_contents = input_file.read()
        max_chars_per_file = API_CHARACTER_LIMIT
        num_files = len(file_contents) // max_chars_per_file + 1

        # print(f"Total small_files : {num_files}")

        # Translator initialization
        t = GoogleTranslator(
            source="auto",
            target=language[variable1.get()]
        )

        # progress bar configuration
        n = num_files
        iter_step = 1 / n
        progress_step = iter_step
        progressbar.start()

        # 1. Selecting the 4999 characters (API Limit = 5000 char) in each iteration from the big_file
        # 2. translating the characters
        # 3. merging the characters into both .txt and .srt

        for i in range(num_files):
            start_index = i * max_chars_per_file
            end_index = (i + 1) * max_chars_per_file

            translated_text = t.translate(file_contents[start_index:end_index])

            if variable2.get() == "text file":
                with open(f"{output_location_entry.get()}/{name[::-1]}_translated.txt", "a+", encoding="utf8") as f:
                    f.write(str(translated_text))
            if variable2.get() == "srt file":
                with open(f"{output_location_entry.get()}/{name[::-1]}_translated.srt", "a+", encoding="utf8") as f:
                    f.write(str(translated_text))

            # print(f"({i + 1}/{num_files}) translated")

            # updating progress_bar
            completed_label.configure(text=f"({i + 1}/{num_files}) translated")
            progressbar.set(progress_step)
            progress_step += iter_step
            app.update_idletasks()

        progressbar.stop()
        input_file.close()

        # deleting texts in the entry_field.
        input_file_location_entry.delete(0, END)
        output_location_entry.delete(0, END)
        messagebox.showinfo(title="Success", message="Text translated successfully!")

    except PermissionError:
        messagebox.showerror(title="Error", message="Permission denied!")
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="File not found!")
    except KeyError:
        messagebox.showerror(title="Error", message="Invalid language!")
    except UnicodeDecodeError:
        messagebox.showerror(title="Error", message="unidecode error!")
    # except requests.exceptions.ConnectionError:
    #     messagebox.showerror(title="Error", message="No internet connection!")
    # except exceptions.RequestError:
    #     messagebox.showerror(title="Error", message="No internet connection!")
    # except exceptions.LanguageNotSupportedException:
    #     messagebox.showerror(title="Error", message="Language not supported!")
    #
    except:
        progressbar.stop()
        messagebox.showerror(title="Error", message="An error occurred\ncheck your internet connection!")


# ====================== END METHODS =================================

# ====================== MAIN WINDOW ==================================================

app = CTk()
app.config(background="#161C25")
app.resizable(False, False)
app.geometry("700x400+480+180")
app.title("Sub-Trans")

font0 = ("Bahnschrift", 20, "bold")
font1 = ("Arial", 15, "bold")
font2 = ("Arial", 13)

# NAME AREA --------------------------------------------
frame_0 = CTkFrame(app,
                   width=680,
                   height=50,
                   fg_color="#161C21",
                   bg_color="#161C25",
                   corner_radius=15,
                   border_width=4,
                   border_color="#fff"
                   )
frame_0.pack(pady=10)

name_label = CTkLabel(frame_0,
                      font=font0,
                      text="TEXT / SUBTITLE  TRANSLATOR",
                      text_color="violet",
                      bg_color="#161C21")

name_label.place(x=230, y=10)
# ------------------------------------------------------

# SETTING AREA ----------------------------------------------------------
frame_1 = CTkFrame(app,
                   width=680,
                   height=195,
                   fg_color="#161C21",
                   bg_color="#161C25",
                   corner_radius=15,
                   border_width=2,
                   border_color="#0C9295"
                   )
frame_1.pack()

# INPUT_FILE -----------------------------------------------------------
input_file_location_label = CTkLabel(frame_1,
                                     font=font1,
                                     text="Subtitle file   :",
                                     text_color="#fff",
                                     bg_color="#161C21")

input_file_location_label.place(x=10, y=10)

input_file_location_entry = CTkEntry(frame_1,
                                     font=font1,
                                     text_color="#000",
                                     fg_color="#fff",
                                     border_color="#0C9295",
                                     border_width=2,
                                     width=460)
input_file_location_entry.place(x=120, y=10)

input_file_location_browse_button = CTkButton(frame_1,
                                              font=('Sans serif', 19, 'bold'),
                                              text="choose",
                                              text_color="#fff",
                                              fg_color="#161C21",
                                              bg_color="#161C21",
                                              hover_color="#00850B",
                                              cursor="hand2",
                                              border_color="#05A312",
                                              corner_radius=8,
                                              border_width=1,
                                              width=50,
                                              command=select_input_file
                                              )
input_file_location_browse_button.place(x=587, y=10)

# OUTPUT_FILE -----------------------------------------------------------

output_location_label = CTkLabel(frame_1,
                                 font=font1,
                                 text="Output locn  :",
                                 text_color="#fff",
                                 bg_color="#161C21")

output_location_label.place(x=10, y=50)

output_location_entry = CTkEntry(frame_1,
                                 font=font1,
                                 text_color="#000",
                                 fg_color="#fff",
                                 border_color="#0C9295",
                                 border_width=2,
                                 width=460)
output_location_entry.place(x=120, y=50)

output_location_browse_button = CTkButton(frame_1,
                                          font=('Sans serif', 19, 'bold'),
                                          text="choose",
                                          text_color="#fff",
                                          fg_color="#161C21",
                                          bg_color="#161C21",
                                          hover_color="#00850B",
                                          cursor="hand2",
                                          border_color="#05A312",
                                          corner_radius=8,
                                          border_width=1,
                                          width=50,
                                          command=select_output_dir
                                          )
output_location_browse_button.place(x=587, y=50)

# LANGUAGE ------------------------------------------------------

options = language.keys()
variable1 = StringVar()

language_label = CTkLabel(frame_1,
                          font=font1,
                          text="Language     :",
                          text_color="#fff",
                          bg_color="#161C21")

language_label.place(x=10, y=90)
language_options = CTkComboBox(frame_1,
                               font=font1,
                               text_color="#000",
                               fg_color="#fff",
                               button_color="#0C9295",
                               button_hover_color="#0C9295",
                               dropdown_hover_color="#0C9295",
                               border_color="#0C9295",
                               variable=variable1,
                               values=options,
                               width=300,
                               justify="center"
                               )
language_options.set('malayalam')
language_options.place(x=120, y=90)

options_1 = ["text file", "srt file"]
variable2 = StringVar()

# TO ------------------------------------------------------
to_label = CTkLabel(frame_1,
                    font=font1,
                    text="To     :",
                    text_color="#fff",
                    bg_color="#161C21")

to_label.place(x=440, y=90)
to_options = CTkComboBox(frame_1,
                         font=font1,
                         text_color="#000",
                         fg_color="#fff",
                         button_color="#0C9295",
                         button_hover_color="#0C9295",
                         dropdown_hover_color="#0C9295",
                         border_color="#0C9295",
                         variable=variable2,
                         values=options_1,
                         width=180,
                         justify="center"
                         )
to_options.set('text file')
to_options.place(x=490, y=90)
# ---------------------------------------------------------------------

# CONVERT ----------------------------------------------------
convert_button = CTkButton(frame_1,
                           font=('Sans serif', 19, 'bold'),
                           text="convert",
                           text_color="#fff",
                           fg_color="#161C21",
                           bg_color="#161C21",
                           hover_color="red",
                           cursor="hand2",
                           border_color="red",
                           corner_radius=8,
                           border_width=1,
                           width=490,
                           command=convert
                           )
convert_button.place(x=100, y=140)
# ---------------------------------------------------------------------

# PROGRESS AREA -------------------------------------------------------
frame_2 = CTkFrame(app,
                   width=680,
                   height=100,
                   fg_color="#161C21",
                   bg_color="#161C25",
                   corner_radius=15,
                   border_width=2,
                   border_color="#0C9295"
                   )
frame_2.pack(pady=10)

completed_label = CTkLabel(frame_2,
                           text="(0/0) translated",
                           font=font1,
                           text_color="#fff",

                           width=490)

completed_label.place(x=100, y=20)

# PROGRESS_BAR ---------------------------
progressbar = CTkProgressBar(frame_2, orientation="horizontal", width=500, height=20)
progressbar.set(0)
progressbar.place(x=100, y=50)
# ---------------------------------------------------------------------

copyright_label = CTkLabel(app,
                           text="copyright © malik-l0l",
                           font=font2,
                           text_color="#fff",
                           fg_color="#161C25"
                           )
copyright_label.place(x=300, y=377)
app.mainloop()

# ====================== END MAIN WINDOW ==============================================
