#Dependencies script file
python3 -m venv venv

if [[ "$OSTYPE" == "darwin"* ]]; then
    source venv/bin/activate
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    source venv/bin/activate
elif [[ "$OSTYPE" == "cygwin" || "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    source venv/Scripts/activate
else
    echo "Unknown OS"
    exit 1
fi

# Create a virtual environment with Python 3.11
python3.11 -m venv myenv
source myenv/bin/activate
pip install playsound
python3 scraper.py