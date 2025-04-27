# Sentiment analysis

This project is created to analyze sentiment of textual data from X (ex. Twitter) in days of high volatility on US stock market measured by VIX index.
It utilizes data science techniques including sentiment analysis with DistilBERT model, word frequency exploration, and data visualization (charts, wordclouds, UMAP).
The project adheres to Reproducible Research standards and software engineering best practices.

> [!TIP]
> In SRS.md file you can check the Software Requirements Specification of the project.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

- [Functionalities](#functionalities)
- [Technologies](#technologies)
- [Setup](#setup)
- [Installation](#installation)
- [View](#view)
- [Contact](#contact)

## Functionalities

## Technologies
- Python 3.13
- Jupyter Notebook
- DistilBERT

## Setup
> [!NOTE]
> In `controller.py` you can customize input data (different timeframe, stock etc.)

### Setup of Reddit API

1. Log into Reddit
Go to Reddit and log in with your account. If you don’t have one, create a new account.

2. Create a New Reddit Application
Navigate to the Reddit developer apps page by going to https://www.reddit.com/prefs/apps.

3. Scroll down to the "Developed Applications" section and click "Create App" or "Create Another App".

Fill in the required fields:
- Name: Choose a name for your app, e.g., reddit-sentiment-analyzer.
- App type: Select "script". This is because we are creating a personal script to interact with Reddit's API.
- Description: (Optional) Write a brief description of what the app does (e.g., "Analyzing sentiment of comments from Reddit").
- Redirect URI: Enter http://localhost:8080 (or any valid URL, but it must match the one you’ll use in your script).
- Permissions: You can leave these as default for now.

Click "Create app" to save the application.

4. Find Your Client ID and Client Secret
Once the application is created, you will see the following information on the app's details page:

- Client ID: This is the unique identifier for your app, located directly under the name of the app (usually a 14-character string).
- Client Secret: This is the secret key, located next to the "secret" label.

5. Store Your Credentials Safely
Open a text editor or your project's configuration and create a .env file (if it doesn't exist).

Inside the `.env` file, add your REDDIT_CLIENT_ID and REDDIT_CLIENT_SECRET as follows:

```
REDDIT_CLIENT_ID=your_client_id_here
REDDIT_CLIENT_SECRET=your_client_secret_here
```

> [!CAUTION]
> Never commit your .env file to a public repository! Add `.env` to your `.gitignore` file as follows to keep it private:

```
.env
```

## Installation

### 1. Install Python (3.13 recommended)
If Python is not installed on your system, follow the installation instructions on the [official Python website](https://www.python.org/downloads/).
### 2. Clone the Project Repository using Git and navigate to the project directory:
```
git clone https://github.com/damianlebiedz/sentiment-analysis.git
cd sentiment-analysis
```
### 3. Install the required Python packages:
```
pip install -r requirements.txt
```
### 4. Run the Project:
```
python main.py
```
### Alternatively you can run the Project via Jupyter Notebook:

1. Install Jupyter Notebook:
```
pip install notebook
```
2. Launch the notebook:
```
jupyter notebook
```
> [!IMPORTANT]
> You must be inside the project directory to launch `jupyter notebook`!

## View

## Contact
Damian Lebiedź | https://damianlebiedz.github.io/contact.html


