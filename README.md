# wxPython-OpenCV
A template/boilerplate application combining wxPython with OpenCV. This application can be used as a base for integrating your OpenCV module into a cross-platform GUI framework.
It also includes a Pyinstallers platform specific .spec file to compile the project into a distributable application.

# Requirements

* Numpy
* wxPython
* OpenCV
* Pyinstaller

# Usage

Download the project and modify it to your needs. Use **run.py** to start the application.

[**wxFormBuilder**](http://sourceforge.net/projects/wxformbuilder/) was used to generate the layout of the GUI.
I highly recommend using this application to visually create your GUI. Then export the Python code from it and load it into the application similar to the **VideoFrame** class.

The following Pyinstallers command can be used to generate a distributable application:
```
pyinstaller pyinstaller_(win/mac).spec
```

# License

This template/boilerplate application is licensed under the MIT license. For more info see LICENSE.md
