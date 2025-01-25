# After Effects Optimization Script

## Overview
This Python script is designed to optimize Adobe After Effects' performance on Windows systems. It addresses common issues like slow rendering, laggy previews, and general sluggishness by automating several system and software tweaks.

---

## Features

1. **Check After Effects Installation**: Verifies if After Effects is installed and accessible.
2. **Clear Disk Cache**: Removes After Effects' temporary and cache files.
3. **Optimize Preferences**:
   - Enables GPU acceleration.
   - Activates Fast Draft Mode.
   - Increases disk cache size.
   - Adjusts the number of render threads.
4. **Clean Temporary Files**: Deletes temporary files from the system's temp directory.
5. **Update GPU Drivers**: Checks and prompts for GPU driver updates.
6. **Set High-Performance Power Mode**: Ensures the system is set to high-performance mode.
7. **Kill Background Processes**: Terminates unnecessary background applications to free up system resources.
8. **Check System Specifications**: Displays CPU, RAM, and GPU information.
9. **Disable Startup Apps**: Opens the startup folder for manual removal of unnecessary startup applications.

---

## Installation

1. **Python**: Ensure Python 3.7 or later is installed on your system.
2. **Dependencies**: Install required Python libraries by running:
   ```bash
   pip install psutil


git clone https://github.com/your-username/ae-optimization-script.git
cd ae-optimization-script
