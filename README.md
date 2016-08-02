# ship_mmg
"ship_mmg" is a web-based simulator based on Maneuvering Modeling Group (MMG) model for ship maneuvering.

## Description
This software can simulate the state of ship maneuvering from the time-series information of rudder angle(&delta;[rad]).

Example of the state of ship maneuvering is as follows:
- &Psi; [rad]
- Velocity and acceleration by ship coordinate system (X[m], Y[m], r[rad/s], etc.)
- etc.

You can change the simulation condition and the specification of target ship. In addition, you can get the simulation result of ship maneuvering by CSV data from web.
This is a web-based application by using Flask and Python. Simulator is implemented based on Python, Numpy and Scipy.

## Demo
![Interface](https://github.com/taiga4112/ship_mmg/wiki/images/demo_readme.png "Interface")

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
Update soon...


### for Developer
#### Mac or Linux
1. Fork it ([http://github.com/taiga4112/ship_mmg/fork](http://github.com/taiga4112/ship_mmg/fork))

2. Set developing environment
	```bash
	$ cd 'yourworkspace'
	$ git clone git@github.com:youraccount/ship_mmg.git
	$ virtualenv ship_mmg
	$ source ship_mmg/bin/activate
	$ pip install Flask numpy scipy
	```

3. Start Flask app
	```bash
	$ python ship_mmg/__init__.py
	```

4. [Access](http://localhost:5000/)


#### Windows
1. Fork it ([http://github.com/taiga4112/ship_mmg/fork](http://github.com/taiga4112/ship_mmg/fork))

2. Set developing environment
	```bash
	$ dir 'yourworkspace'
	$ git clone git@github.com:youraccount/ship_mmg.git
	```
3. Install [requirement packages](http://github.com/taiga4112/ship_mmg#requirement)

4. Start Flask app
	```bash
	$ python ship_mmg/__init__.py
	```
5. [Access](http://localhost:5000/)

## Contribution
1. Fork it ( http://github.com/taiga4112/ship_mmg/fork )
2. Create your feature branch (git checkout -b my-new-feature)
3. Commit your changes (git commit -am 'Add some feature')
4. Push to the branch (git push origin my-new-feature)
5. Create new Pull Request

## Author

[taiga4112](https://github.com/taiga4112)

