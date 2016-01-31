#!/usr/bin/env python

PACKAGE_NAME = 'hw0'

# Standard Python Imports
import os
import copy
import time
import numpy as np
import scipy
import math

# OpenRAVE
import openravepy
#openravepy.RaveInitialize(True, openravepy.DebugLevel.Debug)


curr_path = os.getcwd()
relative_ordata = '/models'
ordata_path_thispack = curr_path + relative_ordata

#this sets up the OPENRAVE_DATA environment variable to include the files we're using
openrave_data_path = os.getenv('OPENRAVE_DATA', '')
openrave_data_paths = openrave_data_path.split(':')
if ordata_path_thispack not in openrave_data_paths:
  if openrave_data_path == '':
    os.putenv('OPENRAVE_DATA', ordata_path_thispack)
  else:
    os.putenv('OPENRAVE_DATA', '%s:%s'%(ordata_path_thispack, openrave_data_path))


class RoboHandler:
  def __init__(self):
    self.env = openravepy.Environment()
    self.env.SetViewer('qtcoin')
    self.env.GetViewer().SetName('Tutorial Viewer')
    self.env.Load('models/%s.env.xml' %PACKAGE_NAME)    #loading the environment
    # time.sleep(3) # wait for viewer to initialize. May be helpful to uncomment
    self.robot = self.env.GetRobots()[0]
    

  #remove all the time.sleep(0) statements! Those are just there so the code can run before you fill in the functions

  # move in a straight line, depending on which direction the robot is facing
  def move_straight(self, dist):
    #TODO Fill in, remove sleep
    T=np.array([[1,0,0,dist],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
    with self.env:
        self.robot.SetTransform(np.dot(self.robot.GetTransform(),T))
    #self.save_viewer_image_topdown( "image1")


  # rotate the robot about the z-axis by the specified angle (in radians)
  def rotate_by(self, ang):
    #TODO Fill in, remove sleep
    #Tz = np.matrix('0 1 0;-1 0 0; 0 0 1')
    Tz = openravepy.matrixFromAxisAngle([0,0,ang])
    with self.env:
        self.robot.SetTransform(np.dot(self.robot.GetTransform(),Tz))
    time.sleep(0)

  # go to each of the square corners, point towards the center, and snap a photo!
  def go_around_square(self):


    # set the robot back to the initialize position after

    #with self.env:
    #Can't use self.env in this case as a sphere is present in the environment which will collide during function call.
    # uncomment the self.env file if you wish to run in an environment without the sphere in the path of the robot
    #Alternatively, set all
    d=2
    t=-135
    self.move_straight(1)
    self.rotate_by(math.radians(-90))
    time.sleep(2)
    self.move_straight(1)
    self.rotate_by(math.radians(-135))
    time.sleep(2)

    for i in range(3):
        self.rotate_by(math.radians(45))
        time.sleep(2)
        self.move_straight(d)
        time.sleep(2)
        self.rotate_by(math.radians(-135))
        time.sleep(2)


  # a function to help figure out which DOF indices correspond to which part of HERB
  def figure_out_DOFS(self):

    with self.env:

        print self.robot.GetDOFValues()
        #Method 1:
        #Enter joint number, see it move, deduce which joint it is
        '''
        while 1:

            joint=input("Enter Joint Number")
            val=0.54 #input("Enter Joint Value")
            self.robot.SetDOFValues([val],[joint])

        '''
        #Method 2
        dof=self.robot.GetDOFValues()
        for i in range(len(dof)):
                print self.robot.GetJointFromDOFIndex(i)





  
  # put herb in self collision
  def put_in_self_collision(self):

    with self.env:
        self.robot.SetDOFValues([5],[1],False)
        self.robot.SetDOFValues([5],[3],False)
        self.robot.SetDOFValues([5],[12],False)
        self.robot.SetDOFValues([5],[15],False)


  # saves an image from above, pointed straight down
  def save_viewer_image_topdown(self, imagename):
    TopDownTrans = np.array([ [0, -1.0, 0, 0], [-1.0, 0, 0, 0], [0, 0, -1.0, 5.0], [0, 0, 0, 1.0] ])
    #seems to work without this line...but its in the tutorial, so I'll keep it here in case
    self.env.GetViewer().SendCommand('SetFiguresInCamera 1') # also shows the figures in the image
    I = self.env.GetViewer().GetCameraImage(640,480,  TopDownTrans,[640,640,320,240])
    scipy.misc.imsave(imagename + '.jpg',I)
      

if __name__ == '__main__':
  robo = RoboHandler()
  t = np.array([ [0, -1.0, 0, 0], [-1.0, 0, 0, 0], [0, 0, -1.0, 5.0], [0, 0, 0, 1.0] ])
  robo.env.GetViewer().SetCamera(t)

  #robo.put_in_self_collision()
  #robo.move_straight(1)
  #robo.rotate_by(math.radians(180))
  #robo.figure_out_DOFS()
  robo.go_around_square()

  # spin forever
  while True:
    time.sleep(1)