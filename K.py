import os, platform
try:
    import requests
except:
    os.system('pip install requests')
import requests
bit = platform.architecture()[0]
if bit == '64bit':
    from Kashif import Jadugar
    Jadugar()
elif bit == '32bit':
    print("\033[1;31mSORRY YOUR DEVICE IS NOT SUPPORT THIS TOOL")
