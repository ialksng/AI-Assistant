import os

def camera():
    try:
        # Command to open Windows Camera
        os.system("start microsoft.windows.camera:")
        print("Opened Windows Camera.")
    except Exception as e:
        print(f"Error: {e}")
