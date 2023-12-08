# PasswordCracking
Command Line Arguments:  
-p = PlainText  
-m = MD5  
-s = SHA-256  
-b = BCrypt  
-d = Dictionary  
-B = Brute Force 

Formatting:  
-Python3 Code.py superS3curePa5sw0Rd -p -B  
-Python3 Code.py 276f8db0b86edaa7fc805516c852c889 -d -m  
-Python3 Code.py 5E884898DA28047151D0E56F8DC6292773603D0D6AABBDD62A11EF721D1542D8 -s -d  

Dependencies:  
-Brute Force can only be used with PlainText, and if it isn't then the program won't run  
-If no arguments are passed into the command line then the program will default to PlainText and Brute Force
