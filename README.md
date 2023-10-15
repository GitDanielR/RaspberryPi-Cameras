This was work done for the Advanced Flow Diagnostics Laboratory. I worked in the lab on the GUI and cameras for about a month.
This was a totally new venture for me and I enjoyed it a lot. I had limited experience with MATLAB and none with Raspberry Pis 
but I think the GUI and pi work ended up relatively good.

1. Setup
   a. MATLAB GUI
     I.   Raspberry Pi Cameras
     II.  Image Folder
     III. Python script
     IV.  On Startup
   b. Raspberry Pi
     I.   Setting Up Pis
     II.  Image Files on Pis
2. Functionality
   a. Properties
   b. Functions
   c. Callback Functions (occur when button/checkbox pushed/changed)
4. Pitfalls

1. Setup
   a. MATLAB Side:
     I. Raspberry Pi Cameras
        To set up the MATLAB GUI so that it is ready to use there are a few things that need to be edited. Make sure to set up Raspi
        connections to all cameras at the top of the GUI as app.pi_n = raspi('ip', 'username/hostname', 'password'). Then make sure that all lines
        containing the array of cameras (cameras = {app.pi1, ..., app.pi_n};) contains all cameras being currently used. As of right now,
        the array can be seen on lines 91, 139, and 319. Also, the order that the Raspi objects are placed in the cameras array matters.
        When selecting the camera number the index of your Raspi object is used. So camera #1 will correspond with the first camera in your cameras list.
     II. Image Folder
        Make sure that you have created a folder (it can be anywhere) that you want to store the images in. You will need this folder for storing
        the images taken during the execution of calibration/experiment runs.
     III. Python Script
         Make sure that the computer being used has the Python from the Microsoft store downloaded. Make sure that the opencv library is installed on
         the computer. This can be done in the command prompt with 'python' (to install python from the MS store), and then 'pip install opencv-python'.
         The python script should be named 'showImg.py' and in the same directory as the cameras.mlapp (MATLAB GUI). If this is not the case, please provide
         the custom file local under the py_script variable on line 66.
     IV. On Startup
         Provide the image folder path under the "image directory" box and press "Go". Do not have any whitespace or quotation marks surrounding your file
         path. If the app successfully launched and you have entered an image directory then the app is ready to go.
  b. Raspberry Pi Side:
    I. Setting Up Pis
       Getting the Pis to work with MATLAB and the Raspi library might provide difficulties at first. Just keep on installing those libraries when it throws
       errors until it doesn't anymore. Run 'pip install $library_name' on the Raspberry Pi to install the library MATLAB wants. For the setup that is used with
       the app, the Raspberry Pi camera should be using the pixel format Y10, with a width of 1280 and a height of 800. There should also be directories named "Live",
       "Cylinder", and "Experiment" inside of the "/home/afdl/Documents" folder on the Pis. If there are not, log into the Pi then run "cd ~/Documents" followed by
       "mkdir Live", "mkdir Cylinder" and "mkdir Experiment".
   II. Image Files on Pis
       The Pis store images taken from the camera either in the "Live", "Cylinder", or "Experiment" folder based on what is being used. During the live camera
       view of the app the image is stored in "/home/afdl/Documents/Live" as "test.tif". During checkerboard, the same system is used, but the files are saved
       after retrieval from the "Live" directory on the Pi. For Cylinder and Experiment, there is a set number of photos streamed to a RAW file. The file is saved
       as "camera.raw" under the respective directory.
   
2. Functionality
   a. Properties
       The app comes with many properties, each stored from lines 4 through 85. There are properties that correspond to app components which just establish all visual aspects
       of the app. Next, there are all the properties that correspond to the live view popout or underlying components. The first 'matlab.ui' properties establish the popout
       and the ability to close it. Then there are different default values for the root file node, screen/button/image/exposure/gain/path values. Then image and python
       script path and all cameras labeled as pi1 -> pi(n).
   b. Functions
       For all functions, ignore the app input in the function call. This just allows for anything placed on the app to be modified (that is basically everything). It is only
       needed to reference things. Think of it as like this._ in Java or self._ in python or this->_ in c++. Just required to access the properties of the app.
       I. rpi = GetPi(app, index)
           Used to get a Raspi object.
           Input: index - position of the camera in the cameras list
           Return: rpi - Raspi object of camera at the given index in the cameras list
       II. createClose(app)
           No input or return values. Just used to create the close button on a live view popout after the "Live View" button has been pushed.
       III. ClosePopout(app, ~)
           No input or return values. Just closes the live view popout after the close button has been pushed.
       IV. img = GetImage(app, index)
           Get live TIF image.
           Input: index - position of the camera in the cameras list
           Return: img - TIF image file representing the TIF image inside of the "Live" directory on the Raspberry Pi.
           * Used for checkerboard test type and live images.
       V. DisplayLiveFeed(app)
           No input or output. Just runs the GetImage function and displays the image while a live image popout is active. Also displays the max image intensity.
       VI. SetExposureAndGain(app, exposure, gain, type)
           Set exposure and gain for all/one camera.
           Input: exposure - Desired exposure.
           Input: gain - Desired gain.
           Input: type - 0 means only updated the "live camera" camera (this is the camera value currently in the "Camera #" edit field. 1 means to update all cameras in the cameras list.
       VII. popTree(app, start_point)
           Populate the file tree with the entered image directory.
           Input: start_point - This is the starting point of the file tree. The start_point is going to be whatever image directory is entered in the "Images Directory" edit field.
       VIII. popDir(app, dirNode, folder, dirName)
           Get information on directories inside of the parent directory.
           Input: dirNode - the directory you want to populate
           Input: folder - parent folder of directory
           Input: dirName - name of folder
       IX. dirchk(app, fullpath)
           Checks if a directory exists and if it doesn't the directory is created.
           Input: fullpath - absolute path of directory
       X. EnterImageDir(app)
           No inputs or outputs. Highlights the image directory edit field in red for 1 second to remind user to enter an images directory before proceeding with app.
