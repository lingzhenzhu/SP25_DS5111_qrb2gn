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

## GitHub Actions CI Setup for Linting and Testing

### Overview
This repository uses **GitHub Actions** to automatically run **code linting** and **unit tests** on every `push`, `pull request`, and manual trigger.  
This ensures the codebase remains clean, consistent, and functional before merging changes into the `main` branch.

---

## Setup Summary

### 1. Workflow Configuration
A GitHub Actions workflow is defined at:
```
.github/workflows/validations.yml
```

The workflow is triggered by:
```yaml
on:
  push:
  pull_request:
  workflow_dispatch:
```
- **push**: Runs tests on every push to any branch.
- **pull_request**: Automatically runs when a PR is created or updated.
- **workflow_dispatch**: Allows manual runs from the GitHub UI.

---

### 2. What the Workflow Does

The workflow consists of three main steps:
1. **Set up Python environment**  
   Using `actions/setup-python` to create a Python 3.10 environment.
   
2. **Install Dependencies**  
   Installing project dependencies using:
   ```bash
   make update
   ```
   (this sets up a virtual environment and installs packages from `requirements.txt`)

3. **Run Linter and Tests**  
   Executing:
   ```bash
   make test
   ```
   - `make lint` runs **Pylint** linter on the source code.
   - `make test` runs **Pytest** on the tests directory.
   - A detailed report is shown in the GitHub Actions log.

---

### 3. Linter and Testing Commands (Makefile)

The Makefile includes the following jobs:

| Command | Purpose |
|:---|:---|
| `make env` | Create and activate a Python virtual environment |
| `make update` | Install or update dependencies from `requirements.txt` |
| `make lint` | Run **Pylint** linter on the source code |
| `make test` | Run **Pylint** and **Pytest** together, summarize scores and results |
| `make check` | (Optional) Alias for `make test`, for a quick full check |

Example usage:

```bash
make update
make test
```

---

### 4. Test Code Structure

All test files are placed under the `tests/` directory.

- Each module has a corresponding test file starting with `test_`.
- For example, the module `bin/normalize_csv.py` has a test file:
  ```
  tests/test_normalize_csv.py
  ```

- Test functions must start with `test_` to be automatically recognized by **pytest**.

---

### 5. Badge

A **GitHub Actions badge** is added to the `README.md` to display the latest workflow status:  
(Replace `username` and `repository` with your actual GitHub account and repo name)

```markdown
![Build Status](https://github.com/<username>/<repository>/actions/workflows/validations.yml/badge.svg?branch=main)
```

- ✅ Green badge indicates that tests passed successfully.
- ❌ Red badge indicates that linting or tests failed.

---
