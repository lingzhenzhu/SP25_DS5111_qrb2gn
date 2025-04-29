[![Feature Validation](https://github.com/lingzhenzhu/SP25_DS5111_qrb2gn/actions/workflows/validations.yml/badge.svg)](https://github.com/lingzhenzhu/SP25_DS5111_qrb2gn/actions/workflows/validations.yml)
# Repo for DS 5111
## Project Setup Guide for a New Virtual Machine (VM)

This guide provides step-by-step instructions to set up a new virtual machine (VM) for this project, ensuring all dependencies are installed and configured properly.

---

## **Step 1: Manually Update System Packages**
Before running any scripts, manually update the system package list:

```bash
sudo apt update -y
```

This step is necessary to ensure that all packages are up to date before installing dependencies.

---

## **Step 2: Configure Git Credentials and SSH Key**
To interact with the repository, configure your Git credentials:

```bash
./global_creds
```

If you have not set up an SSH key before, generate one:

```bash
ssh-keygen -t rsa -b 4096 -C "your-email@example.com"
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_rsa
```

Then, add the public key to your GitHub account:

```bash
cat ~/.ssh/id_rsa.pub
```

Copy the output and add it to GitHub → Settings → SSH and GPG Keys.

To verify the connection:

```bash
ssh -T git@github.com
```

---

## **Step 3: Clone the Repository**
After setting up Git credentials and SSH key, clone this repository:

```bash
git clone git@github.com:your-username/your-repo.git
cd your-repo
```

Make sure you replace `your-username` and `your-repo` with your actual GitHub repository details.

---

## **Step 4: Run Initialization Script**
Run the `init.sh` script to install all necessary dependencies:

```bash
./init.sh
```

This script will:

- Install `make` (for handling build automation)
- Install `python3.12-venv` (for creating Python virtual environments)
- Install `tree` (a useful tool for listing files in a tree format)
- Ensure your system is updated

---

## **Step 5: Verify the Setup**
After running `init.sh`, confirm that everything is correctly installed:

```bash
git --version
make --version
python3 --version
tree --version
```

If all commands return valid outputs, the setup is complete!

---

## **Troubleshooting**

### Git authentication error?
Run the following command to check if SSH authentication works:

```bash
ssh -T git@github.com
```

Ensure your SSH key is added to GitHub.

### Permission issues when running scripts?
Ensure the scripts have execution permissions:

```bash
chmod +x global_creds init.sh
```

### Missing dependencies?
Manually rerun:

```bash
sudo apt update -y && sudo apt install make python3.12-venv tree -y
```

## Web Scraping with Headless Chrome

This project demonstrates how to set up a virtual machine (VM) for web scraping using headless Chrome.

---

## **Step 1: Install Chrome Headless**
Run the following command to install Chrome:

```bash
./install_chrome_headless.sh
```

To verify installation, run:

```bash
google-chrome-stable --version
google-chrome-stable --headless --disable-gpu --dump-dom https://example.com/
```

---

## **Step 2: Set Up Python Environment**

This project requires `pandas` and `lxml`. To set up:

```bash
python3 -m venv env
source env/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

---

## **Step 3: Using the Makefile**

Instead of manually setting up the environment, you can use `Makefile`:

```bash
make update
```

This will create a virtual environment and install dependencies.

---

## **Step 4: Scraping Data**

To scrape Yahoo Finance gainers:

```bash
make ygainers.csv
```

To scrape Wall Street Journal gainers:

```bash
make wjsgainers.csv
```

---

## **Step 5: Project Structure**

Run the following command to display the project structure:

```bash
tree <your project-repo> -I env
```

Example output:

```
.
├── install_chrome_headless.sh
├── Makefile
├── README.md
├── requirements.txt
├── ygainers.html
├── ygainers.csv
├── wjsgainers.html
└── wjsgainers.csv
```

---

## **Next Steps**

Now that your environment is set up, you can expand this project by:

- Scraping additional stock market data
- Automating execution with cron jobs
- Analyzing and visualizing stock trends


