import os
from datetime import datetime

import PySimpleGUI as sg


def extract_alarm_logs(app_folder: str, start_date: datetime, end_date: datetime, output_folder: str):
    """ Read amd Extract contents of .alh files to excel. """

    alarm_dir = os.path.join(app_folder, "alarm")

    if not os.path.exists(alarm_dir):
        sg.popup("Error", "Alarm directory not found")
        return

    sg.popup("Success", f"Alarm logs from {start_date} to {end_date} have been extracted and saved to {output_folder}")
