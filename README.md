# **Joystick Gremlin**

Joystick Gremlin is a program that allows the configuration of joystick like
devices, similar to what CH Control Manager and Thrustmaster's T.A.R.G.E.T. do
for their respectively supported joysticks. However, Joystick Gremlin works
with any device be it from different manufacturers or custom devices that
appear as a joystick to Windows. Joystick Gremlin uses the virtual joysticks
provided by vJoy to map physical to virtual inputs and apply various other
transformations such as response curves to analogue axes. In addition to
managing joysticks, Joystick Gremlin also provides keyboard macros, a flexible
mode system, scripting using Python, and many other features.

The main features are:
  - Works with arbitrary joystick like devices
  - User interface for common configuration tasks
  - Merging of multiple physical devices into a single virtual device
  - Axis response curve and dead zone configuration
  - Arbitrary number of modes with inheritance and customizable mode switching
  - Keyboard macros for joystick buttons and keyboard keys
  - Python scripting

Joystick Gremlin provides a graphical user interface which allows commonly
performed tasks, such as input remapping, axis response curve setups, and macro
recording to be performed easily. Functionality that is not accessible via the
UI can be implemented through custom modules.


# **Used Software**
Joystick Gremlin uses the following software and resources:

- [pyinstaller](http://www.pyinstaller.org/)
- [PyQt5](http://www.riverbankcomputing.co.uk/software/pyqt/intro)
- [PyWin32](http://sourceforge.net/projects/pywin32)
- [vJoy 2.1.9](https://github.com/jshafer817/vJoy/releases/download/v2.1.9.1/vJoySetup.exe)
- [Python 3.6.8](https://www.python.org)
- [Modern UI Icons](http://modernuiicons.com/)
- [Microsoft Visual Studio Build Tools (Visual C++ 14.0)](https://az764295.vo.msecnd.net/stable/441438abd1ac652551dbe4d408dfcec8a499b8bf/VSCodeUserSetup-x64-1.75.1.exe) <!-- TODO: add tutorial -->

# **Building from Source**

Currently the 32-bit version of Python (3.6.8) is needed and the following packages should be installed via PiP to get the source running:

```shell
> pip install pyinstaller PyQt5==5.13.2 pypiwin32 reportlab
```

The job of turning the Python code in a windows executable and
packaging everything up into an installable MSI file is performed
by [pyinstaller](http://www.pyinstaller.org/) and
[wix](http://wixtoolset.org/). The steps needed to build the code
and assemble it into the installer is automated using a batch
script and can be run as:

```shell
> deploy.bat
```

To simply generate the executable code without the MSI installer the
following command can be used:

```shell
> pyinstaller -y --clean joystick_gremlin.spec
```