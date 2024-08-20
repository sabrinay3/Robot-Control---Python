Quickstart Guide:

Unity (for mac):
- Download Unity on your device
- Cloned https://github.com/Abraham190137/TeleoperationUnity/tree/main opened in unity and followed the instructions on the GitHub
- I used Unity (silicon) 2022.3.20f1 for Mac
ROS:
- Download ROS Noetic (or latest version) on Linux computer: https://wiki.ros.org/noetic 
- Follow instructions on site
LEAP Hand/Dynamixel (must have ROS downloaded at this point): https://github.com/leap-hand/LEAP_Hand_API/tree/12acca918d8b08c280a5d290f92bdd1dce6270b7 (<-- Leap hand guide)
- Download the Dynamixel Wizard for Linux using instructions: - https://emanual.robotis.com/docs/en/software/dynamixel/dynamixel_wizard2/ 
- Plug in LEAP Hand into computer and open dynamixel
- Scan using magnifying glass icon the top left hand corner of the wizard at 4000000 bps. The Wizard should read TTYUSB0 or TTYUSB1 (last digit may be different)
- If all the motors show up, connection is successful
- When running any code for the LEAP Hand, you must close the Dynamixel Wizard
- The range of values for the leap hand goes as follows: 3.00 = 0º rotation in the joint and 4.75 = 90º rotation in the joint
VS Code: https://github.com/sabrinay3/Robot-Control---Python 
- You should use VS Code on Linux computer
- Use code from both LEAP Hand API and Teleoperation Github
- When editing scripts in Unity, upload the changes to the Oculus each time. 
- “record.py” and “replay.py” are used mainly for debugging purposes. It will record messages from the oculus and replay them on command. 
- “main.py” is the script for VR teleoperation of the LEAP hand. 
