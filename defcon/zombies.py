#! /usr/bin/python
import socket
import math

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

RIFLE_V = 853
PISTOL_V = 350
GRAVITY = -9.81
PI = 3.14159
HOST = 'zombies_8977dda19ee030d0ea35e97ad2439319.2014.shallweplayaga.me'
PORT = 20689
s.connect((HOST, PORT));
i = 0; 
s.recv(1024)
s.send('1\n')
s.recv(1024)
s.send('2\n')

def calDist(x,y):
	return (x*x + y*y)**0.5
def detWeapon(x,y):
	dist = calDist(x,y)
	if dist < 50:
		return 'p'
	else:
		return 'r'
def detVelocity(x,y):
	dist = calDist(x,y)
	if dist<50:
		return PISTOL_V
	else:
		return RIFLE_V

def detAngle(x,y, t=0):
	v = detVelocity(x,y);
	if t != 0:
		return math.acos(x/(t*u)) * 180 /PI

	a = 0.5 * GRAVITY * x * x
	b = v*v*x
	c = -y*v*v + a

	D = b*b - 4.0 * a * c
	sol = (-b + D**0.5)/ (2.0 * a)
	return (math.atan(sol))* 180 /PI

def getY(x,y,t,theta):
	v = detVelocity(x,y)
	y = v * math.sin(theta*PI/180) * t + 0.5 * GRAVITY * t * t	

def parseInput(buf):
  x = 0
  y = 0
  t = 0
  prev = ''
  lines = buf.split('\n')
  for line in lines:
    if 'above your van' in line:
      parts = line.split(' ')
      for part in parts:
        if part == 'from':
          x = prev[0:-1]
        elif part == 'above':
          y = prev[0:-1]
        prev = part
    elif 'frozen in terror' in line:
      parts = line.split(' ')
      for part in parts:
        if 	part == 'terror':
          x = prev[0:-1]
        elif part == 'and':
          y = prev[0:-1]
        elif part == 'have':
          t = prev[0:-1]  
        theta = detAngle(x, y, t)
        y = getY(x,y, t, theta)    		    
  return (x, y, t)

i =0 
while s:
	data = s.recv(1024)
	print data
	coord = parseInput(data)
	x = int(coord[0])
	y = int(coord[1])
	t = int(coord[2])
	weapon = detWeapon(x, y)
	angle = detAngle(x, y, t)
	resp = weapon + ', ' + str(angle) + ', ' + str(x) + ', ' + str(y) + '\n'
	print resp
	s.send(resp)