Convert the Text or Link To QR code Image 

we can execute this using basic python modules, which we have to import 

Step 1: Setting Up the Environment

Install Python: Make sure you have Python installed. You can download it from python.org.

Step 2: import modules from PYTHON using this command 

       pip install qrcode[pil] pillow

Step 3: Save the python file using .py 
    example qr_generator.py 

Step 4: Once execute the program it is  almost ready ,.

To get .exe file or App 

Step 1: Open the Root Folder where you saved the Python File and Icon 

Step 2: Right-click and open the Terminal/command prompt / windows shell

Step 3: install this 

      pip install pyinstaller

Step 4 : Enter this Command

            pyinstaller --onefile --windowed --icon=app_icon.ico qr_generator.py
            
   Note : 1. app_icon.ico is your Icon / img name like qr-code.png
          2.qr_generator.py is your python file name 

Step 5: The dict , build and .spec files will be created in the folder 

Step 6: Open the dict folder and you can find the application with icon 

Open the icon and generate the QR image of any Text or Link 
