# Lock_Keyboard_Mouse
Lock Keyboard & Mouse , An app to lock your keyboard and mouse after "time" of inactivity.. This is fun project to made for those who want to lock thier keyboard and mouse until they insert an USB to unlock.. 

Follow these steps to setup this application for your machine.

Step 1. Clone
  git clone https://github.com/pyDashNinja/Lock_Keyboard_Mouse.git
  cd Lock_Keyboard_Mouse
 
Step 2. Make Virtual Env
  Python3 -m venv venv
  source venv/bin/activate
  pip install -r requirements.txt
  
Step 3. Now every thing is installed, Now we need to change the code in few lines
  Now if you see in the code you can set 'threshold' which is the time it takes to lock the keyboard and mouse, I have set to 300 seconds.
  threshold = 300
  After that we need to ser DISPLAY using os.environ, My number is ':1' you can check yours by using 'echo $DISPLAY'
  
os.environ['DISPLAY'] = ':1'
  
Now using 'xinput' command in terminal, find out your keyboard and mouse name like mine is, also note its masters id which we will use to unlock it later
 
keyboard_string = "keyboard:ITE Tech. Inc. ITE Device(8910) Keyboard" 
touchpad_string = "pointer:MSFT0001:01 06CB:CE2D Touchpad"
            
After finding that replace keyboard_string according to that like for keyboard, i have used above, If you can see String start with keyboard:{name} this is because, the keyboard name is taken from keyboard section if it exits same name in both mouse and keyboard section it will not conflict so it is better to find section like keybaord and pointer and then connect name of the keyboar and pointer using " : " like i have.

after that replace , here yoy will just replace the name, after floating:{name} , do not change floating.. 
keyboard_string_f = "floating:ITE Tech. Inc. ITE Device(8910) Keyboard"
touchpad_string_f = "floating:MSFT0001:01 06CB:CE2D Touchpad"

