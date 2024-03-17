"""
MAIN IDEA :
    take a srt file
    translate everything init  [require google api][require internet][free api -> 50k words/month]
    create a new translated subtitle file and save it
    any lang --> any language

PROBLEM WITH THIS CODE:
    This code works, but it is
    not good if the file size increase translation takes time

SOLUTIONS:
     1:
       take subtitle file ,divide it into multiple files
        then translate everything in parallel
         then join them into single file

"""
import requests
from deep_translator import GoogleTranslator, exceptions

try:
    # SPLITTING FILES
    input_file = open("C:\\Users\\ACER\\Desktop\\test\\y.txt", "r")
    file_contents = input_file.read()
    max_chars_per_file = 4999
    num_files = len(file_contents) // max_chars_per_file + 1

    print(f"Total files : {num_files}")

    t = GoogleTranslator(
        source="auto",
        target="ml"
    )

    for i in range(num_files):
        start_index = i * max_chars_per_file
        end_index = (i + 1) * max_chars_per_file

        translated_text = t.translate(file_contents[start_index:end_index])

        with open(f"C:\\Users\\ACER\\Desktop\\test\\output.txt", "a+", encoding="utf8") as f:
            f.write(str(translated_text))

        print(f"({i + 1}/{num_files}) files translated")

    input_file.close()

except requests.exceptions.ConnectionError:
    print("No internet connection")
except exceptions.LanguageNotSupportedException:
    print("Language not supported")
