import os
from datetime import datetime

import PySimpleGUI as sg


def extract_alarm_logs(app_folder: str, start_date: datetime, end_date: datetime, output_folder: str):
    """Read amd Extract contents of .alh files to excel."""

    alarm_dir = os.path.join(app_folder, "alarm")

    if not os.path.exists(alarm_dir):
        sg.popup("Error", "Alarm directory not found")
        return

    sg.popup("Success", f"Alarm logs from {start_date} to {end_date} have been extracted and saved to {output_folder}")


layout = [
    [
       sg.Text("Select Aveva app location (project.app):"),
        sg.InputText(key="-APP_FILE-", enable_events=True, size=(50, 1)),
        sg.FileBrowse(file_types=(("App Files", "*.app"),)),
    ],
    [
       sg.Text("Select start date:"),
        sg.Input(key="-START_DATE-", size=(20, 1)),
        sg.CalendarButton("Choose Date", target='-START_DATE-', format='%Y-%m-%d'),
    ],
    [
       sg.Text("Select end date:"),
        sg.Input(key='-END_DATE-', size=(20, 1)),
        sg.CalendarButton("Choose Date", target='-END_DATE-', format='%Y-%m-%d'),
    ],
    [
       sg.Text("Select destination folder for the output Excel file:"),
        sg.InputText(key='-DEST_FOLDER-', enable_events=True, size=(50, 1)),
        sg.FolderBrowse(),
    ],
    [sg.Button('Generate'), sg.Button('Cancel')],
]

window = sg.Window("Alarm Log Extractor", layout)


# Event loop
while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Cancel':
        break

    # Handle clicking generate button
    if event == 'Generate':
        app_file = values["-APP_FILE-"]
        start_date = values["-START_DATE-"]
        end_date = values["-END_DATE-"]
        dest_folder = values["-DEST_FOLDER-"]

        #input validation
        if not app_file:
            sg.popup("Error", "Please select Aveva app file (project.app).")
            continue

        if not start_date or end_date:
            sg.popup("Error", "Please select start and end dates.")
            continue

        if not dest_folder:
            sg.popup("Error", " Error please select both start and end dates")
            continue

        extract_alarm_logs(os.path.dirname(app_file), start_date, end_date, dest_folder)

# close
window.close()
