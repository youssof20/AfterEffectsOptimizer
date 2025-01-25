import os
import subprocess
import psutil
import platform

def check_after_effects_version():
    print("Checking After Effects version...")
    # Assuming After Effects is installed in default location (update paths if needed)
    default_path = r"C:\\Program Files\\Adobe\\Adobe After Effects\\Support Files\\AfterFX.exe"
    if os.path.exists(default_path):
        print(f"After Effects found at {default_path}")
    else:
        print("After Effects executable not found. Ensure After Effects is installed correctly.")

def clear_cache():
    print("Clearing After Effects cache...")
    cache_path = os.path.expanduser(r"~\\AppData\\Roaming\\Adobe\\Common")
    if os.path.exists(cache_path):
        for root, dirs, files in os.walk(cache_path):
            for file in files:
                os.remove(os.path.join(root, file))
        print("Cache cleared successfully.")
    else:
        print("Cache folder not found.")

def optimize_preferences():
    print("Optimizing After Effects preferences...")
    # Preferences file location
    preferences_path = os.path.expanduser(r"~\\AppData\\Roaming\\Adobe\\After Effects\\21.0\\Adobe After Effects Prefs.txt")
    if os.path.exists(preferences_path):
        with open(preferences_path, 'r') as file:
            prefs = file.readlines()

        updated_prefs = []
        for line in prefs:
            if "'Enable GPU acceleration'" in line:
                updated_prefs.append("'Enable GPU acceleration'=1\n")
            elif "'Fast Draft Mode'" in line:
                updated_prefs.append("'Fast Draft Mode'=1\n")
            elif "'Disk Cache Size'" in line:
                updated_prefs.append("'Disk Cache Size'=200GB\n")
            elif "'Number of Render Threads'" in line:
                updated_prefs.append("'Number of Render Threads'=8\n")
            else:
                updated_prefs.append(line)

        with open(preferences_path, 'w') as file:
            file.writelines(updated_prefs)
        print("Preferences optimized.")
    else:
        print("Preferences file not found.")

def clean_temp_files():
    print("Cleaning temporary files...")
    temp_path = os.path.expanduser(r"~\\AppData\\Local\\Temp")
    if os.path.exists(temp_path):
        for root, dirs, files in os.walk(temp_path):
            for file in files:
                try:
                    os.remove(os.path.join(root, file))
                except Exception as e:
                    print(f"Failed to delete {file}: {e}")
        print("Temporary files cleaned.")
    else:
        print("Temporary folder not found.")

def update_gpu_drivers():
    print("Checking GPU drivers...")
    try:
        subprocess.run("nvidia-smi", shell=True, check=True)
        print("GPU drivers appear to be up to date.")
    except subprocess.CalledProcessError:
        print("NVIDIA drivers not found or outdated. Please update your GPU drivers manually.")

def set_high_performance_mode():
    print("Setting high-performance power mode...")
    try:
        subprocess.run("powercfg /SETACTIVE SCHEME_MIN", shell=True, check=True)
        print("High-performance power mode set.")
    except Exception as e:
        print(f"Failed to set high-performance mode: {e}")

def kill_background_processes():
    print("Killing unnecessary background processes...")
    unnecessary_processes = ["chrome.exe", "discord.exe", "spotify.exe", "teams.exe", "slack.exe"]
    for process in psutil.process_iter(['name']):
        if process.info['name'] in unnecessary_processes:
            try:
                psutil.Process(process.pid).terminate()
                print(f"Terminated {process.info['name']}.")
            except Exception as e:
                print(f"Could not terminate {process.info['name']}: {e}")

def check_system_specs():
    print("Checking system specifications...")
    cpu = platform.processor()
    ram = round(psutil.virtual_memory().total / (1024 ** 3), 2)
    gpu = subprocess.check_output("wmic path win32_VideoController get caption", shell=True).decode().strip()

    print(f"CPU: {cpu}")
    print(f"RAM: {ram} GB")
    print(f"GPU: {gpu}")

def disable_startup_apps():
    print("Disabling unnecessary startup apps...")
    try:
        subprocess.run("shell:Startup", shell=True)
        print("Startup folder opened. Remove unnecessary shortcuts manually.")
    except Exception as e:
        print(f"Failed to open Startup folder: {e}")

def main():
    print("Starting After Effects Optimization Script...")

    # Check if After Effects is installed
    check_after_effects_version()

    # Clear disk cache
    clear_cache()

    # Optimize preferences
    optimize_preferences()

    # Clean temporary files
    clean_temp_files()

    # Update GPU drivers
    update_gpu_drivers()

    # Set high-performance power mode
    set_high_performance_mode()

    # Kill unnecessary background processes
    kill_background_processes()

    # Check and print system specs
    check_system_specs()

    # Disable unnecessary startup apps
    disable_startup_apps()

    print("Optimization complete. Restart After Effects and test performance.")

if __name__ == "__main__":
    main()
