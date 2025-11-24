from webdriver_manager.chrome import ChromeDriverManager
import os

try:
    path = ChromeDriverManager().install()
    print(f"Driver path: {path}")
    if os.path.exists(path):
        print(f"Is file: {os.path.isfile(path)}")
        print(f"Is dir: {os.path.isdir(path)}")
        if os.path.isfile(path):
             print(f"Size: {os.path.getsize(path)}")
    else:
        print("Path does not exist")
        
    # List dir of parent
    parent = os.path.dirname(path)
    print(f"Parent dir: {parent}")
    print(os.listdir(parent))

except Exception as e:
    print(f"Error: {e}")
