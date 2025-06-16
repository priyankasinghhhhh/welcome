import os
import platform
import subprocess

def get_system_uptime():
    """
    Returns the system uptime as a string.
    """
    try:
        if platform.system() == "Windows":
            # Using 'net stats srv' for Windows
            output = subprocess.check_output("net stats srv", shell=True, text=True)
            for line in output.splitlines():
                if "Statistics since" in line:
                    return f"System uptime since: {line.split('since')[1].strip()}"
            return "Could not determine uptime on Windows."
        elif platform.system() == "Linux":
            # Using /proc/uptime for Linux
            with open("/proc/uptime", "r") as f:
                uptime_seconds = float(f.readline().split()[0])
                hours = int(uptime_seconds // 3600)
                minutes = int((uptime_seconds % 3600) // 60)
                seconds = int(uptime_seconds % 60)
                return f"System uptime: {hours} hours, {minutes} minutes, {seconds} seconds"
        elif platform.system() == "Darwin":
            # macOS: use 'uptime' command
            output = subprocess.check_output("uptime", shell=True, text=True)
            return f"System uptime: {output.strip()}"
        else:
            return "Unsupported OS."
    except Exception as e:
        return f"Error retrieving uptime: {e}"

if __name__ == "__main__":
    print(get_system_uptime())
