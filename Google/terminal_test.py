
from __future__ import print_function

import json
from asciimatics.event import KeyboardEvent
from asciimatics.widgets import Frame, Layout, MultiColumnListBox, Widget, Label, TextBox, ListBox, Divider, Button
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError, StopApplication
from asciimatics.parsers import AsciimaticsParser
import sys
from collections import defaultdict

from asciimatics.widgets.popupdialog import PopUpDialog

import glob
import os

choosen = None

def get_json_files(path):
    jsons = []
    for idx, value in enumerate(glob.glob(os.path.join(path,"*.json"))):
        jsons.append((value, idx))
    return jsons

jsons = get_json_files("./")

class DemoFrame(Frame):
    def __init__(self, screen):
        super(DemoFrame, self).__init__(screen,
                                        screen.height,
                                        screen.width,
                                        has_border=False,
                                        name="My Form")
        layout = Layout([1])
        self.add_layout(layout)

        layout.add_widget(
            Label("Press `up`/`down` to choose json file or `q` to quit."))
        layout.add_widget(Divider(height=1))
        
        self._details = ListBox(
            height=5,
            options=jsons,
            on_select=self._on_select,
            name="listbox")
        
        layout.add_widget(self._details)
        layout.add_widget(Divider(height=2))        
        self.fix()
        
        self.palette = defaultdict(
            lambda: (Screen.COLOUR_WHITE, Screen.A_NORMAL, Screen.COLOUR_BLACK))
        for key in ["selected_focus_field"]:
            self.palette[key] = (Screen.COLOUR_WHITE, Screen.A_REVERSE, Screen.COLOUR_BLACK)

        
    def process_event(self, event):
        if isinstance(event, KeyboardEvent):
            if event.key_code in [ord('q'), ord('Q'), Screen.ctrl("c")]:
                raise StopApplication("User quit")
            self._last_frame = 0
        return super(DemoFrame, self).process_event(event)

    def _on_select(self):
        self.save()
        
        global choosen
        choosen = self.data
        if True:
            raise StopApplication("testing")

    def _quit(self):
        self._scene.add_effect(
            PopUpDialog(self._screen,
                        "Are you sure?",
                        ["Yes", "No"],
                        has_shadow=True,
                        on_close=self._quit_on_yes))

    def _on_change(self):
        changed = False
        self.save()
        for key, value in self.data.items():
            # print(key, value)
            if value == 2:
                raise StopApplication("Exiting")

    @staticmethod
    def _quit_on_yes(selected):
        # Yes is the first button
        if selected == 0:
            raise StopApplication("User requested exit")

def userinterface(screen, scene):
    screen.play([Scene([
        DemoFrame(screen)
    ], -1)], stop_on_resize=True, start_scene=scene, allow_int=True)

last_scene = None
while True:
    try:
        Screen.wrapper(userinterface, catch_interrupt=False, arguments=[last_scene])
        break
    except ResizeScreenError as e:
        last_scene = e.scene

json_file =(jsons[choosen["listbox"]][0])


import datetime
import os.path
import glob

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']



def main():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None

    if os.path.exists(json_file):
        creds = Credentials.from_authorized_user_file(json_file, SCOPES)
    


    try:
        service = build('calendar', 'v3', credentials=creds)

        today = (datetime.datetime.today())
        start = today - datetime.timedelta(days=5)

        today = today.isoformat() + 'Z'  # 'Z' indicates UTC time
        start = start.isoformat() + 'Z'  # 'Z' indicates UTC time

        new = f'{start.split("T")[0][-5:]} ~ {today.split("T")[0][-5:]}'

        events_result = service.events().list(calendarId='primary', timeMin=start,
                                              timeMax=today,
                                              maxResults=10, singleEvents=True,
                                              orderBy='startTime').execute()
        events = events_result.get('items', [])

        if not events:
            print('No upcoming events found.')
            return

        # Prints the start and name of the next 10 events
        dates, tmp = [], []
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            dates.append(start.split("T")[0][-5:])
            
            tmp.append(f'・{start.split("T")[0][-5:]} {event["summary"]}')
            
    except HttpError as error:
        print('An error occurred: %s' % error)
    
    
    
    with open("assets/sample.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    
    
    
    with open("test.txt", "w", encoding="utf-8") as f:

        for line in lines:
            if "{name}" in line:
                f.write(line.replace("{name}", "Adrian"))
            elif "{office}" in line:
                f.write(line.replace("{office}", new))
            elif "{clients}" in line:
                for day in tmp:
                    f.write(f"{day}\n")
            else:
                f.write(line)
    #     # if "{client}" in lines


    
    # print(lines[0])
    
    # print(["\n".join(tmp)])
    # print(dates)

main()