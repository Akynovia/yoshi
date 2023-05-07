Yoshi - Virtual Assistant

The Yoshi project is a command-line assistant that allows the user to browse the internet and search for information on Wikipedia. It is written in Python and is compatible with both Windows and Linux. It was developed to be simple and intuitive.

Installation:

Clone the repository: git clone https://github.com/Akynovia/yoshi

To install the necessary dependencies, run the install.sh file on Linux or the install.bat file on Windows. Make sure you are in the root directory of the project when running the installation file.

How to use:
After installation, execute the main.py file to start the assistant. Then follow the on-screen instructions to browse the internet or search for information on Wikipedia.

The following options are available:

navegar: allows the user to browse the internet. Type the navegar command followed by the URL you want to access.
wiki: allows the user to search Wikipedia. Type the wiki command followed by the topic you want to search.
limpar: clears the console screen.
ajuda: displays the help screen.
sair: exits the assistant.

Project Structure:
The project structure is as follows:

yoshi/
├── app/
│ ├── main.py
│ ├── lib/
│ │ ├── init.py
│ │ ├── help.py
│ │ ├── web.py
│ │ └── wikipedia.py
│ └── tests/
├── config/
│ ├── install.bat
│ ├── install.sh
│ └── requirements.txt
├── Leiame (or morra)
└── Readme (or die)

The app folder contains the main.py file, which is the main file of the project, and two subfolders:

lib, which contains the Python modules for web and Wikipedia interaction, as well as an init.py file that is executed when the subfolder is imported;
tests and a Python module that tests the functionality of the web.py module.
The config folder contains project configuration and installation files:

install.bat, a batch script for installing the project dependencies on Windows;
install.sh, a shell script for installing the project dependencies on Linux;
requirements.txt, a file that lists the project dependencies to be installed with pip.
The Leiame and Readme (or die) files are project documentation files.

In summary, the project is a Python application that allows web browsing and Wikipedia searching through a command-line assistant. It is composed of specific Python modules, configuration files, and installation scripts.