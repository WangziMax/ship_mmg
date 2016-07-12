# coding: utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import sys,os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/calc')

from flask import Flask, render_template, request, redirect, url_for
import numpy as np
import maneuver

project_name = 'Ship MMG'
error_message = 'Value error. Please try again.'

app = Flask(__name__) # Flask setting


#############################################
# Routing setting for web application
#############################################

@app.route('/')
def index():
    title = project_name
    return render_template('index.html', title=title) # rendering 'index.html'


@app.route('/fsr', methods=['Get','POST'])
def fixed_speed_and_rudder():
    title = project_name + " ( Fixed Speed and Rudder ) "

    if request.method == 'POST': # POST

    	########################################################
    	# 1. Get form value
    	########################################################
        x0 = request.form.get('x0', None)
        y0 = request.form.get('y0', None)
        psi0 = request.form.get('psi0', None)
    	u0 = request.form.get('u0', None)
    	v0 = request.form.get('v0', None)
        r0 = request.form.get('r0', None)
        dr0 = request.form.get('dr0', None)
    	delta0 = request.form.get('delta0', None)
        w0 = request.form.get('w0', 0.0)
        theta0 = request.form.get('theta0', 90.00)
    	T1 = request.form.get('T1', None)
    	T2 = request.form.get('T2', None)
    	T3 = request.form.get('T3', None)
        T3v = request.form.get('T3v', None)
    	K = request.form.get('K', None)
        Kv = request.form.get('Kv', None)
    	sampling = request.form.get('sampling', 1001)
    	duration = request.form.get('duration', 1000)
    	
    	# Error check
        # 1. 'T1 == 0.00' cannot be calculate
        errorFlag = False
        if float(T1) == 0.00:
            errorFlag = True

        if errorFlag:
            return render_template('fixed_speed_and_rudder.html',title=title, message=error_message,
                delta0=delta0, u0=u0, v0=v0, r0=r0, dr0=dr0, T1=T1, T2=T2, T3=T3, T3v=T3v, K=K, Kv=Kv, x0=x0, y0=y0, psi0=psi0, sampling=sampling, duration=duration)


    	########################################################
    	# 2. Calculate
    	########################################################
    	T, X = maneuver.maneuvering_by_fixed_speed_and_rudder(__rad(delta0), __rad(w0), __rad(theta0), u0, v0, r0, dr0, T1, T2, T3, T3v, K, Kv, x0, y0, __rad(psi0), sampling, duration)

    	return render_template('fixed_speed_and_rudder.html', title=title, result=zip(T,X),
                delta0=delta0, u0=u0, v0=v0, r0=r0, dr0=dr0, T1=T1, T2=T2, T3=T3, T3v=T3v, K=K, Kv=Kv, x0=x0, y0=y0, psi0=psi0, sampling=sampling, duration=duration)


    else: # other
		
		########################################################
        # 1. Get form value
    	########################################################
        x0 = request.args.get('x0', 0.00)
        y0 = request.args.get('y0', 0.00)
        psi0 = request.args.get('psi0', 0.00)
    	u0 = request.args.get('u0', 10.29)
    	v0 = request.form.get('v0', 0.00)
        r0 = request.form.get('r0', 0.00)
        dr0 = request.form.get('dr0', 0.00)
    	delta0 = request.form.get('delta0', 5.00)
        w0 = request.form.get('w0', 0.00)
        theta0 = request.form.get('theta0', 90.00)
    	T1 = request.form.get('T1', 80.50)
    	T2 = request.form.get('T2', 5.29)
    	T3 = request.form.get('T3', 12.02)
        T3v = request.form.get('T3v', 0.00)
    	K = request.form.get('K', 0.155)
        Kv = request.form.get('Kv', 0.0155)
    	sampling = request.form.get('sampling', 1001)
    	duration = request.form.get('duration', 1000)

    	return render_template('fixed_speed_and_rudder.html', title=title,
                delta0=delta0, u0=u0, v0=v0, r0=r0, dr0=dr0, T1=T1, T2=T2, T3=T3, T3v=T3v, K=K, Kv=Kv, x0=x0, y0=y0, psi0=psi0, sampling=sampling, duration=duration)

@app.route('/fstsr', methods=['Get','POST'])
def fixed_speed_and_trigonometric_function_rudder():
    title = project_name + " ( Fixed Speed and Trigonmetric Function Rudder ) "

    if request.method == 'POST': # POST

        ########################################################
        # 1. Get form value
        ########################################################
        x0 = request.form.get('x0', None)
        y0 = request.form.get('y0', None)
        psi0 = request.form.get('psi0', None)
        u0 = request.form.get('u0', None)
        v0 = request.form.get('v0', None)
        r0 = request.form.get('r0', None)
        dr0 = request.form.get('dr0', None)
        delta0 = request.form.get('delta0', None)
        w0 = request.form.get('w0', None)
        theta0 = request.form.get('theta0', None)
        T1 = request.form.get('T1', None)
        T2 = request.form.get('T2', None)
        T3 = request.form.get('T3', None)
        T3v = request.form.get('T3v', None)
        K = request.form.get('K', None)
        Kv = request.form.get('Kv', None)
        sampling = request.form.get('sampling', 1001)
        duration = request.form.get('duration', 1000)
        
        # Error check
        # 1. 'T1 == 0.00' cannot be calculate
        errorFlag = False
        if float(T1) == 0.00:
            errorFlag = True

        if errorFlag:
            return render_template('fixed_speed_and_trigonometric_function_rudder.html',title=title, message=error_message,
                delta0=delta0, u0=u0, v0=v0, r0=r0, dr0=dr0, T1=T1, T2=T2, T3=T3, T3v=T3v, K=K, Kv=Kv, x0=x0, y0=y0, psi0=psi0, sampling=sampling, duration=duration)


        ########################################################
        # 2. Calculate
        ########################################################
        T, X = maneuver.maneuvering_by_fixed_speed_and_rudder(__rad(delta0), __rad(w0), __rad(theta0), u0, v0, r0, dr0, T1, T2, T3, T3v, K, Kv, x0, y0, __rad(psi0), sampling, duration)
        
        return render_template('fixed_speed_and_trigonometric_function_rudder.html', title=title, result=zip(T,X),
                delta0=delta0, w0=w0, theta0=theta0, u0=u0, v0=v0, r0=r0, dr0=dr0, T1=T1, T2=T2, T3=T3, T3v=T3v, K=K, Kv=Kv, x0=x0, y0=y0, psi0=psi0, sampling=sampling, duration=duration)


    else: # other
        
        ########################################################
        # 1. Get form value
        ########################################################
        x0 = request.args.get('x0', 0.00)
        y0 = request.args.get('y0', 0.00)
        psi0 = request.args.get('psi0', 0.00)
        u0 = request.args.get('u0', 10.29)
        v0 = request.form.get('v0', 0.00)
        r0 = request.form.get('r0', 0.00)
        dr0 = request.form.get('dr0', 0.00)
        delta0 = request.form.get('delta0', 5.00)
        w0 = request.form.get('w0', 14.4)
        theta0 = request.form.get('theta0', 0.00)
        T1 = request.form.get('T1', 80.50)
        T2 = request.form.get('T2', 5.29)
        T3 = request.form.get('T3', 12.02)
        T3v = request.form.get('T3v', 0.00)
        K = request.form.get('K', 0.155)
        Kv = request.form.get('Kv', 0.0155)
        sampling = request.form.get('sampling', 1001)
        duration = request.form.get('duration', 1000)

        return render_template('fixed_speed_and_trigonometric_function_rudder.html', title=title,
                delta0=delta0, w0=w0, theta0=theta0, u0=u0, v0=v0, r0=r0, dr0=dr0, T1=T1, T2=T2, T3=T3, T3v=T3v, K=K, Kv=Kv, x0=x0, y0=y0, psi0=psi0, sampling=sampling, duration=duration)

@app.route('/zigzag', methods=['Get','POST'])
def fixed_speed_and_zig_zag():
    title = project_name + " ( Fixed Speed and Zig-Zag test ) "

    if request.method == 'POST': # POST

        ########################################################
        # 1. Get form data
        ########################################################
        x0 = request.form.get('x0', None)
        y0 = request.form.get('y0', None)
        psi0 = request.form.get('psi0', 0.00) # initial condition
        psia = request.form.get('psia', None)
        u0 = request.form.get('u0', None)
        v0 = request.form.get('v0', None)
        r0 = request.form.get('r0', 0.00) # initial condition
        dr0 = request.form.get('dr0', 0.00) # initial condition
        delta0 = request.form.get('delta0', None) # initial condition
        t1 = request.form.get('t1', None)
        T1 = request.form.get('T1', None)
        T2 = request.form.get('T2', None)
        T3 = request.form.get('T3', None)
        T3v = request.form.get('T3v', None)
        K = request.form.get('K', None)
        Kv = request.form.get('Kv', None)
        sampling = request.form.get('sampling', 1001)
        duration = request.form.get('duration', 1000)
        
        # Error check
        # 1. 'T1 == 0.00' cannot be calculate
        errorFlag = False
        if float(T1) == 0.00:
            errorFlag = True

        if errorFlag:
            return render_template('fixed_speed_and_zig_zag.html',title=title, message=error_message,
                delta0=delta0, psia=psia, t1=t1, u0=u0, v0=v0, T1=T1, T2=T2, T3=T3, T3v=T3v, K=K, Kv=Kv, x0=x0, y0=y0, sampling=sampling, duration=duration)


        ########################################################
        # 2. Calculate
        ########################################################
        T, X = maneuver.maneuvering_by_fixed_speed_and_zig_zag(__rad(delta0), __rad(psia), t1, u0, v0, r0, dr0, T1, T2, T3, T3v, K, Kv, x0, y0, __rad(psi0), sampling, duration)
        
        return render_template('fixed_speed_and_zig_zag.html', title=title, result=zip(T,X),
                delta0=delta0, psia=psia, t1=t1, u0=u0, v0=v0, T1=T1, T2=T2, T3=T3, T3v=T3v, K=K, Kv=Kv, x0=x0, y0=y0, sampling=sampling, duration=duration)


    else: # other
        
        ########################################################
        # 1. Get initial value
        ########################################################
        x0 = request.args.get('x0', 0.00)
        y0 = request.args.get('y0', 0.00)
        psi0 = request.args.get('psi0', 0.00)
        psia = request.form.get('psia', 10.00)
        u0 = request.args.get('u0', 10.29)
        v0 = request.form.get('v0', 0.00)
        delta0 = request.form.get('delta0', 10.00)
        w0 = request.form.get('w0', 14.4)
        theta0 = request.form.get('theta0', 0.00)
        t1 = request.form.get('t1', 1.00)
        T1 = request.form.get('T1', 80.50)
        T2 = request.form.get('T2', 0.00)
        T3 = request.form.get('T3', 0.00)
        T3v = request.form.get('T3v', 0.00)
        K = request.form.get('K', 0.155)
        Kv = request.form.get('Kv', 0.0155)
        sampling = request.form.get('sampling', 2002)
        duration = request.form.get('duration', 200)

        return render_template('fixed_speed_and_zig_zag.html', title=title,
                delta0=delta0, psia=psia, t1=t1, u0=u0, v0=v0, T1=T1, T2=T2, T3=T3, T3v=T3v, K=K, Kv=Kv, x0=x0, y0=y0, sampling=sampling, duration=duration)


# Get angle(rad) from angle(degree)
def __rad(delta_degree):
    delta_rad = float(delta_degree) * np.pi / 180
    return delta_rad


#######################################
# main setting
#######################################
if __name__ == '__main__':
    # app.debug = True # for DEBUG
    app.run(host='0.0.0.0') # for all access