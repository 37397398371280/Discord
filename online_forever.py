import subprocess
import sys

def update_pip():
    """Update pip to the latest version."""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
        print("pip has been updated successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Failed to update pip: {e}")
      
