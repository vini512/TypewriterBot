# Typewriter Bot

An automated Python script designed to handle typing lessons on `typewriter.at`. The bot automates the entire process: bypassing cookie consents, logging into your account, starting a lesson, typing out the text with simulated human-like delays, intentionally making a realistic percentage of mistakes, and looping back to the home screen for the next lesson.

## Features

* **Fully Automated Flow:** Handles cookie consent, secure login, lesson launching, typing execution, and automatic navigation back to the dashboard.
* **Smart Error Generation:** Dynamically calculates the total character count and injects intentional typos (`{`) at mathematically calculated intervals to maintain a realistic `MISTAKE_PERCENT` (e.g., 2%).
* **Dynamic Text Extraction:** Scrapes active target characters in real-time from the DOM to adapt to the typing interface.
* **Emergency Brake:** Tracks a global hotkey (`strg` / `ctrl`) to safely kill the script and close the browser instantly.
* **Robust Element Detection:** Employs explicit wait conditions (`WebDriverWait`) to prevent crashes caused by slow network requests or layout shifting.

## Installation

1. **Download the project:**
   Simply download the ZIP file from GitHub, extract it, and open the directory.

2. **Install dependencies:**
   Make sure you have Python 3 installed, then install the required packages via your terminal:
   ```bash
   pip install selenium keyboard
   ```

3. **WebDriver Setup:**
   Ensure you have Google Chrome installed. Selenium will automatically manage your ChromeDriver binary in modern versions.

## Configuration

Open the script file and fill in your credentials and preferences at the top:

```python
NAME = "your_username"       # Your typewriter.at username
PASSWORT = "your_password"   # Your typewriter.at password
EXIT_KEY = "strg"            # The panic key to stop the bot (use 'ctrl' if on non-DE layouts)
MISTAKE_PERCENTAGE = 2       # Target error rate (2%)
DELAY = uniform(0.15, 0.17)  # Keystroke delay range (in seconds)
```

## Usage

Run the script from your terminal:

```bash
python main.py
```

> **Important Operating System Note:** The `keyboard` library captures global hotkeys at the OS level. If you are running this script on Linux or macOS, you may need root/administrator privileges (`sudo python main.py`) for the emergency exit key to work correctly.

## License

This project is free to use and distribute under the MIT License.
