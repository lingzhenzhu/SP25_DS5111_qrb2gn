.PHONY: default lint test check update

default:
	@cat makefile

env:
	python3 -m venv env; . env/bin/activate; pip install --upgrade pip

update: env
	. env/bin/activate; pip install -r requirements.txt

ygainers.html:
	sudo google-chrome-stable --headless --disable-gpu --dump-dom --no-sandbox --timeout=5000 'https://finance.yahoo.com/markets/stocks/gainers/?start=0&count=200' > ygainers.html

ygainers.csv: ygainers.html
	python -c "import pandas as pd; raw = pd.read_html('ygainers.html'); raw[0].to_csv('ygainers.csv')"

wsjgainers.html:
	@echo "import os, time, subprocess, pandas as pd\n\
while True:\n\
    if os.path.exists('wsjgainers.html'):\n\
        os.remove('wsjgainers.html')\n\
    subprocess.run(['google-chrome-stable', '--headless', '--disable-gpu', '--dump-dom', '--no-sandbox', '--timeout=5000', 'https://www.wsj.com/market-data/stocks/us/movers'], stdout=open('wsjgainers.html', 'w'), check=True)\n\
    try:\n\
        tables = pd.read_html('wsjgainers.html')\n\
        if tables:\n\
            print('✅ Table detected in HTML.')\n\
            break\n\
    except Exception:\n\
        pass\n\
    print('❌ No tables found in HTML, retrying download...')\n\
    time.sleep(2)" | python

wsjgainers.csv: wsjgainers.html
	python -c "import pandas as pd; raw = pd.read_html('wsjgainers.html'); raw[0].to_csv('wsjgainers.csv')"

gainers:
	. env/bin/activate && python get_gainer.py $(SRC)

lint:
	env/bin/pylint $(or $(file),bin/*.py)

test:
	@echo "Running Linter..."
	@env/bin/pylint $(or $(file),bin/*.py)|| true
	@echo "Running Tests..."
	@env/bin/pytest -vv $(or $(file),tests)
	@echo "Check Completed."
