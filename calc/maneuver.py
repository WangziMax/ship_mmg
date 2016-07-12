# coding: utf-8

import numpy as np
from scipy.integrate import ode, odeint


##########################################
# maneuvering simulation by fixed speed and rudder
##########################################
def maneuvering_by_fixed_speed_and_rudder(delta0, w0, theta0, u0, v0, r0, dr0, T1, T2, T3, T3v, K, Kv, x0, y0, psi0, sampling, duration):
	psi0 = float(psi0)
	x0 = float(x0)
	y0 = float(y0)
	u0 = float(u0)
	v0 = float(v0)
	r0 = float(r0)
	dr0 = float(dr0)
	delta0 = float(delta0)
	w0 = float(w0)
	theta0 = float(theta0)
	T1 = float(T1)
	T2 = float(T2)
	T3 = float(T3)
	T3v = float(T3v)
	K = float(K)
	Kv = float(Kv)
	sampling = int(sampling)
	duration = float(duration)


	###############
	# Definitoin of EOM(Equation of motion) from MMG model and others
	###############
	#
	# 0 : psi' = r
	# 1 : delta' = delta0 * w0 * cos(w0*t+theta0)
	# 2 : u' = 0 (fixed)
	# 3 : v' = r * Kv / K
	# 4 : r' = dr
	# 5 : dr' = - (T1 + T2)/T1/T2 * dr - 1/T1/T2 * r + K/T1/T2 * delta0( * sin(w0*t+theta0) + K*T3*w0/T1/T2*delta0*cos(w0*t+theta0)
	# 6 : x' = u * cos(psi) + v * sin(psi)
	# 7 : y' = u * sin(psi) - v * cos(psi)
	#
	# Changing EOM to use K-T model can be detected by the condition of 'T2==0' or not. 
	# If you use K-T model, change as follows:
	# 4 : r' = -1 / T1 * r + K / T1 * delta0(rad) * sin(w0*t+theta0)
	# 5 : dr' = 0
	# 
	# def __eom(t, x): # for ode
	def __eom(x, t): # for odeint
		_psi = x[4]
		_delta = delta0 * w0 * np.cos(w0 * t + theta0)
		_u = 0
		_v = x[4] * Kv / K
		
		_r = 0.0
		_dr = 0.0
		if T2 == 0: # first‐order ordinary differential equation (K-T model)
			_r = -1/T1*x[4]+K/T1*delta0*np.sin(w0*t+theta0)
		else: # second‐order ordinary differential equation
			_r = x[5]
			_dr = - (T1 + T2)/T1/T2 * x[5] - 1/T1/T2 * x[4] + K/T1/T2*delta0*np.sin(w0*t+theta0) + K*T3*w0/T1/T2*delta0*np.cos(w0*t+theta0)
		
		_x = x[2] * np.cos(x[0]) + x[3] * np.sin(x[0])
		_y = x[2] * np.sin(x[0]) - x[3] * np.cos(x[0])

		return [_psi, _delta, _u, _v, _r, _dr, _x, _y]

	time = np.linspace(0.00, duration, sampling) # Arrray including sampling data from 0.0 to duration.
	X_init = np.array([psi0, delta0*np.sin(w0*0.0+theta0), u0, v0, r0, dr0, x0, y0]) # Initial condition on X (can be a vector).
	X = odeint(__eom, X_init, time) # A sequence of time points for which to solve for X. The initial value point should be the first element of this sequence.
	return time, X


##########################################
# maneuvering simulation by fixed speed and zig-zag
##########################################
def maneuvering_by_fixed_speed_and_zig_zag(delta0, psia, t1, u0, v0, r0, dr0, T1, T2, T3, T3v, K, Kv, x0, y0, psi0, sampling, duration):
	delta0 = float(delta0)
	psia = float(psia)
	t1 = float(t1)
	psi0 = float(0.00) # initial condition
	x0 = float(x0)
	y0 = float(y0)
	u0 = float(u0)
	v0 = float(v0)
	r0 = 0.00 # initial condition
	dr0 = 0.00 # initial condition
	T1 = float(T1)
	T2 = float(T2)
	T3 = float(T3)
	T3v = float(T3v)
	K = float(K)
	Kv = float(Kv)
	sampling = int(sampling)
	duration = float(duration)


	###############
	# Definitoin of EOM(Equation of motion) from MMG model and others
	###############
	#
	# 0 : psi' = r
	# 1 : delta(degree)'  *zig-zag maneuvering
	# 2 : u' = 0 (fixed)
	# 3 : v' = r * Kv / K
	# 4 : r' = dr
	# 5 : dr' = - (T1+T2)/T1/T2 * dr - 1/T1/T2 * r + K/T1/T2 * delta + K*T3*w0/T1/T2 * delta'
	# 6 : x' = u * cos(psi) + v * sin(psi)
	# 7 : y' = u * sin(psi) - v * cos(psi)
	#
	# zig-zag maneuvering
	# a) From 0<=t<=t1, delta=delta0/t1*t 
	# b) From t1<=t and psi<=psia, delta=delta0
	# c) If psi=psi0 (t=t2), delta=delta0/t1*(t1+t2-t) until delta=-delta0 (t=t3)
	# d) From t3<=t and psi>=-psia, delta=-delta0
	# e) If psi=-psia (t=t4), delta=delta0/t1*(t-t1-t4) until delta=delta0(t=t5)
	# f) return b)
	# 
	# Changing EOM to use K-T model can be detected by the condition of 'T2==0' or not. 
	# If you use K-T model, change as follows:
	# 4 : r' = -1 / T1 * r + K / T1 * delta
	# 5 : dr' = 0
	# 
	def __eom(x, t):
		_psi = x[4]

		# zig-zag
		_delta = 0
		if t <= t1: # 0 - t1
			_delta = delta0/t1
		elif np.fabs(x[0]) <= psia:
			# -psia < psi < psia
			_delta = 0 # t1 - t2
		else:
			# psi < -psia or psis < psi
			if x[0] > 0:
				if x[1] > -delta0:
					_delta = -delta0/t1# t2 - t3 & t6 - t7
				else:
					_delta = 0 # t3 - t4
			elif x[0] <0 :
				if x[1] < delta0:
					_delta = delta0/t1 # t4 - t5
				else:
					_delta = 0 # t5 - t6
		
		_u = 0
		_v = x[4] * Kv / K
		
		_r = 0.0
		_dr = 0.0
		if T2 == 0: # first‐order ordinary differential equation (K-T model)
			_r = -1/T1*x[4]+K/T1*x[1]
		else: # second‐order ordinary differential equation
			_r = x[5]
			_dr = - (T1 + T2)/T1/T2 * x[5] - 1/T1/T2 * x[4] + K/T1/T2*x[1] + K*T3/T1/T2*_delta
		
		_x = x[2] * np.cos(x[0]) + x[3] * np.sin(x[0])
		_y = x[2] * np.sin(x[0]) - x[3] * np.cos(x[0])

		return [_psi, _delta, _u, _v, _r, _dr, _x, _y]

	X_init = np.array([psi0, 0.00, u0, v0, r0, dr0, x0, y0]) # Initial condition on X (can be a vector).
	

	#################
	# Following code is for using odeint
	#################
	time = np.linspace(0.00, duration, sampling) # Arrray including sampling data from 0.0 to duration.
	X = odeint(__eom, X_init, time ,mxstep=5000) # A sequence of time points for which to solve for X. The initial value point should be the first element of this sequence.
	#################
	
	##################
	# Following code is for using ode. But, this code has some wrong bug and speed is very slow...
	# If you want to use this, please change '__eom(x,t)' to '__eom(t,x)'
	##################
	# solver =  ode(__eom).set_integrator('vode',method='bdf',nsteps=50000)
	# solver.set_initial_value(X_init,0.0)
	# time = []
	# X = []
	# while solver.successful() and solver.t < duration:
	# 	print solver.t
	# 	print solver.successful()
	# 	solver.integrate(solver.t + (duration - 0.00)/sampling)
	# 	time.append(solver.t)
	# 	X.append(solver.y)
	###################

	return time, X
