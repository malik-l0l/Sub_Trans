# 📃 Sub_Trans 🎬

Sub-Trans is a Python GUI application that allows users to translate text or subtitle files into different languages using the Google Translate API. The application splits your file into smaller files,translate and merge them back to a single translated file to overcome the API character count limitation 😉. With support for both text and subtitle files, Sub-Trans offers versatility and convenience for users seeking translation services `without API character limit`.

## 🛠️ Main Technologies

- `Python 3.x`
  - `deep_translator`
  - `tkinter`
  - `customtkinter`

## 🚦 Running the Project

To run the project in your local environment,Python must be installed on your system and follow these steps:

1. Clone the repository to your local machine.
2. Run `pip install tkinter` in the project directory to install the Tkinter library, which is usually included with Python installations.
3. Run `pip install customtkinter` in the project directory to install the Customtkinter library.
4. Run `pip install deep_translator` in the project directory to install the Translator library.
5. Run `cd Sub_Trans` to go into the project directory.
6. Run `py subtrans.py` in terminal or click on run `▶️` button to get the project started.

## 🕹️ How to Use

1. **📲 Select Input File**: Click on the "Choose" button next to "Subtitle file" to select the text or subtitle file you want to translate.
2. **📳 Select Output Location**: Click on the "Choose" button next to "Output locn" to specify the folder where translated files will be saved.
3. **🗣️ Select Target Language**: Choose the desired target language from the dropdown menu labeled "Language."
4. **✍️ Select Output Format**: Choose between translating text into a separate text file or appending translations to existing subtitle files using the dropdown menu labeled "To."
5. **💬 Initiate Translation**: Click on the "convert" button to start the translation process.
6. **🌍 Monitor Progress**: Track the progress of the translation process using the progress bar displayed on the application.
7. **🔎 View Results**: Once the translation is complete, view the translated files in the specified output location.

## 🦄 Features

- **🗺️ File Selection:**
  - Users can select input text or subtitle files for translation.
  - Supported file formats include `.txt` and `.srt`.
  
- **🧏🏻‍♂️ Output Configuration:**
  - Users can specify the output location for translated files.
  - Output files are named based on the original file name, with "_translated" appended.

- **📙 Language Selection:**
  - Sub-Trans supports translation into multiple languages, providing users with a wide range of options.
  - Users can select the target language from a dropdown menu.

- **🤹🏻 Translation Process:** 
  - `The application divides large input files into smaller segments to comply with API character limits.`
  - Progress of the translation process is displayed using a progress bar.
  - Users are notified upon successful completion of the translation.

- **🔧 Error Handling:**

  - Sub-Trans includes error handling mechanisms to address common issues such as file not found, permission denied, and invalid language selection.
  - Users receive informative error messages to guide troubleshooting.

- **🎛️ Customization Options:**
  - Users can choose between translating text into a separate text file or appending translations to existing subtitle files.
  - The application provides flexibility to tailor translation preferences according to user requirements.

## 🤔 How Can It Be Improved?

- 🧷 Enhance error handling to provide more detailed error messages and troubleshoot common issues effectively.
- 📔 Implement error logging to record errors encountered during translation for future reference and debugging.
- 🗄️ Add support for additional file formats to expand the application's compatibility and usefulness.
- 🖌️ Enhance the user interface with visual feedback, tooltips, and progress indicators to improve user experience and engagement.
- 🍴 Incorporate multi-threading to improve performance and responsiveness, especially for large files or multiple translation tasks simultaneously.


## 🐛 Current Bug

So far, I'm not really sure if there are any bugs. However, there might be some issues  related to file permissions, file not found, or invalid language selection. Ensure that files are accessible and the selected language is supported by the Google Translate API. I tested it out on my computer (Windows 10), and so far it looks good there.


## 🚀 Let's Get Started

If you want the program without GUI 🙈 [Click here!](https://github.com/malik-l0l/Sub_Trans/blob/main/assets/sub_trans_core.py)

if you need a text_file for testing 💣 [Click here!](https://github.com/malik-l0l/Sub_Trans/blob/main/assets/oppenheimer_subtitle.txt)

Let's unleash the power of a translator!,[Download Sub_Trans now!](https://github.com/malik-l0l/Sub_Trans/raw/main/assets/subtrans.exe)✨

## 🍿 Preview

![Screenshot (63)](https://github.com/malik-l0l/Sub_Trans/assets/154656931/f7048219-170b-4fa2-9875-d82e6cfdaca8)

**Copyright © malik-l0l**
