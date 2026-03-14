# Study Session Tracker

## Project Overview

The Study Session Tracker is a simple command-line Python application designed to help users record and review their study sessions. The program allows users to log study sessions with details such as the subject studied, the number of minutes spent studying, the study location, and optional notes. It also provides a summary report that displays useful statistics about the recorded sessions.

This project demonstrates Python programming concepts including functions, loops, conditional statements, and user input.

## Features

  Add Study Session – Record a new study session with subject, minutes studied, location, and optional notes.
  View All Sessions – Display all previously recorded study sessions in a formatted list.
  View Summary Report – Show statistics including:

  * Total number of study sessions
  * Total minutes studied
  * Average minutes per session
  * Longest study session
  * Shortest study session
* **Menu System** – A simple text-based menu that allows users to navigate the program until they choose to exit.


How the Program Works

The program starts in main.py, which displays a menu of options.

Based on the user's selection, the program calls functions in tracker.py.

Session information is stored in lists defined in data.py.

The user can repeatedly add sessions, view all sessions, or view a summary until they choose to exit the program.
