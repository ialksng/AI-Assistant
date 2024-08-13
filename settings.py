import os

def settings():
    try:
        # Command to open Windows Settings
        os.system('start ms-settings:')
        print("Opened Windows Settings.")
    except Exception as e:
        print(f"Error: {e}")
