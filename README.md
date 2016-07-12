# ship_mmg
"ship_mmg" is a web-based simulator based on Maneuvering Modeling Group (MMG) model for ship maneuvering.

## Description
This software can simulate the state of ship maneuvering from the time-seriese information of rudder angle(&delta;[rad]).

Example of the state of ship maneuvering is as follows:
- &Psi; [rad]
- Velocity and acceleration by ship coordinate system (X[m], Y[m], r[rad/s], etc.)
- etc.

You can change the simulation condition and the specification of target ship. In addition, you can get the simulation result of ship maneuvering by CSV data from web.
This is a web-based application by using Flask and Python. Simulator is inplemented based on Python, Numpy and Scipy.

## Demo
Update soon...

## Requirement
- Flask (0.11.1)
- Jinja2 (2.8)
- MarkupSafe (0.23)
- numpy (1.11.1)
- pip (8.1.2)
- python (2.7.10)
- scipy (0.17.1)
- setuptools (24.0.2)
- Werkzeug (0.11.10)
- wheel (0.29.0)

## Usage
Please asscess index page.

## Install
### for Developer
'''
virtualenv ship_mmg
'''


## Contribution
1. Fork it ( http://github.com/taiga4112/ship_mmg/fork )
2. Create your feature branch (git checkout -b my-new-feature)
3. Commit your changes (git commit -am 'Add some feature')
4. Push to the branch (git push origin my-new-feature)
5. Create new Pull Request

## Author

[taiga4112](https://github.com/taiga4112)

