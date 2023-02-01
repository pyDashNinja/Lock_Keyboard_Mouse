import time
import subprocess
import os
import gc


threshold = 300
os.environ['DISPLAY'] = ':1'
import pyautogui


# Get the current time
last_event_time = time.time()
last_event_position = pyautogui.screenshot(region=(0, 40, 1920, 1080))

while True:
    usb = subprocess.run(["lsusb"], stdout=subprocess.PIPE).stdout.decode("utf-8")

    if 'Corsair Voyager 3.0' not in usb:
        # Get the current mouse position
        try:
            del usb
        except:
            pass
        current_position = pyautogui.screenshot(region=(0, 40, 1920, 1080))

        if current_position != last_event_position:
            try:
                del last_event_position
                del last_event_time
            except:
                pass
            # Update the last event position and time
            last_event_position = current_position
            try:
                del current_position
            except:
                pass
            last_event_time = time.time()

        # Check if the threshold has been exceeded
        if time.time() - last_event_time > threshold:
            # Lock the laptop
            try:
                del last_event_position
                del last_event_time
                del current_position
            except:
                pass

            keyboard_string = "keyboard:ITE Tech. Inc. ITE Device(8910) Keyboard"
            touchpad_string = "pointer:MSFT0001:01 06CB:CE2D Touchpad"

            keyboard_string_f = "floating:ITE Tech. Inc. ITE Device(8910) Keyboard"
            touchpad_string_f = "floating:MSFT0001:01 06CB:CE2D Touchpad"


            keyboard_id = subprocess.run(["xinput", "list", "--id-only", keyboard_string], stdout=subprocess.PIPE).stdout.decode("utf-8")
            touchpad_id = subprocess.run(["xinput", "list", "--id-only", touchpad_string], stdout=subprocess.PIPE).stdout.decode("utf-8")

            if keyboard_id == '' or touchpad_id == '':
                keyboard_id = subprocess.run(["xinput", "list", "--id-only", keyboard_string_f], stdout=subprocess.PIPE).stdout.decode("utf-8")
                touchpad_id = subprocess.run(["xinput", "list", "--id-only", touchpad_string_f], stdout=subprocess.PIPE).stdout.decode("utf-8")

            try:
                del keyboard_string
                del touchpad_string
                del keyboard_string_f
                del touchpad_string_f
            except:
                pass

            keyboard_id = int(keyboard_id)
            touchpad_id = int(touchpad_id)

            
            subprocess.run(["xinput", "float", f"{keyboard_id}"])
            subprocess.run(["xinput", "float", f"{touchpad_id}"])


            while True:

            

                # Initialize recognizer class (for recognizing the speech)
                usb = subprocess.run(["lsusb"], stdout=subprocess.PIPE).stdout.decode("utf-8")

                if 'Corsair Voyager 3.0' in usb:
                    try:
                        del usb
                    except:
                        pass
                    print("opened")
                    subprocess.run(["xinput", "reattach", f"{keyboard_id}", "3"])
                    subprocess.run(["xinput", "reattach", f"{touchpad_id}", "2"])
                    last_event_time = time.time()
                    try:
                        del keyboard_id
                        del touchpad_id
                    except:
                        pass

                    break
                
                time.sleep(10)
                gc.collect()
    try:
        del usb
    except:
        pass
    gc.collect()    
    time.sleep(300)
