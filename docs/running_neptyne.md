# Running Neptyne Locally: Step-by-Step Guide

This guide provides precise instructions for running Neptyne on your local machine. Following these steps exactly will ensure a successful setup.

## Prerequisites

1. Python 3.11 (earlier or later versions are not guaranteed to work)
2. pip (Python package installer)
3. git (for cloning the repository)
4. macOS or Linux (Windows instructions may differ)

## Step-by-Step Installation

### 1. Clone the Repository

```bash
cd ~/Documents  # or your preferred directory
git clone https://github.com/neptyneco/neptyne.git neptyne-spreadsheet
cd neptyne-spreadsheet
```

### 2. Set Up Python Environment

Create and activate a virtual environment:

```bash
# Create a new virtual environment with Python 3.11
python3.11 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Verify Python version (should show 3.11.x)
python --version
```

### 3. Install Dependencies

Install all required packages in the correct order:

```bash
# Update pip first
pip install --upgrade pip

# Install requirements
pip install -r requirements.txt

# Install neptyne in development mode
pip install -e .
```

## Running the Server

### Primary Method (Recommended)

```bash
# Make sure you're in the neptyne-spreadsheet directory
cd ~/Documents/neptyne-spreadsheet

# Run the server with SQLite database
python server/application.py --sqlite-db neptyne.db --debug --port 8878
```

The server will start and show some debugging output. You may see warnings about frozen modules - these can be safely ignored.

### Verifying the Server is Running

1. The server will print a URL with a shared secret
2. Open your web browser and go to:

   ```
   http://localhost:8878?sharedSecret=MiWzLl9GpH
   ```

   This is the current shared secret as of December 2023.

3. You should see the Neptyne interface load. If you see "Invalid token", double-check that you've copied the entire URL including the shared secret exactly as shown above.

## Troubleshooting Guide

### 1. Port Already in Use

If you see this error:

```
OSError: [Errno 48] Address already in use
```

Solution: Change the port number:

```bash
python server/application.py --sqlite-db neptyne.db --debug --port 8879
```

### 2. Module Not Found

If you see:

```
ModuleNotFoundError: No module named 'neptyne'
```

Solution:

```bash
# Make sure you're in the neptyne-spreadsheet directory
cd ~/Documents/neptyne-spreadsheet
# Reinstall in development mode
pip install -e .
```

### 3. Python Version Issues

If you see any import or syntax errors, verify your Python version:

```bash
python --version  # Should be 3.11.x
```

### 4. Shared Secret Issues

If you can't find your shared secret:

```bash
# Read it directly from the config file
python3.11 -c "import json; print(json.load(open(os.path.expanduser('~/.neptyne.json')))['shared_secret'])"
```

The current shared secret is: MiWzLl9GpH

## Current Configuration (as of December 2023)

- Server URL: http://localhost:8878
- Shared Secret: MiWzLl9GpH
- Full URL: http://localhost:8878?sharedSecret=MiWzLl9GpH
- Database: SQLite (neptyne.db)

## Additional Features

### Google Sheets Integration

1. Install the Neptyne GSheets Add-on from [Google Workspace Marketplace](https://workspace.google.com/marketplace/app/neptyne_python_for_sheets/891309878867)
2. In the add-on settings, enter:
   - Server URL: http://localhost:8878
   - Shared Secret: MiWzLl9GpH

### For Public Access

If you need to access your Neptyne instance from outside your network:

1. Install ngrok: `brew install ngrok` (on macOS)
2. Run: `ngrok http 8878`
3. Use the https URL provided by ngrok in the GSheets add-on settings

## Verification Steps

After setup, verify your installation:

1. Server starts without errors
2. Web interface loads at http://localhost:8878?sharedSecret=MiWzLl9GpH
3. You can create a new sheet
4. Python cells execute correctly

If any step fails, refer to the Troubleshooting Guide above.
