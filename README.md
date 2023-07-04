# NBA Daily Stat Leaders App
The NBA Daily Stat Leaders App is a Python-based application that scrapes an NBA statistics website to retrieve daily stat leader data. It then sends automated emails to users every day, providing them with updates on the daily NBA stat leaders.

## Features

* Scrapes NBA statistic website to retrieve daily stat leader data.
* Stores and retrieves users' email addresses from a Microsoft SQL Server database.
* Sends automated emails at 10:00 PM every day to update users on the daily NBA stat leaders.

## Installation

1. Clone or download this repository to your local machine.
2. Install the required Python packages by running the following command:
  `pip install -r requirements.txt"`
3. Set up the Microsoft SQL Server database:
   * Create the database to store the user email addresses.
   * Update the database connection details in the 'app.py' file.
4. Configure email settings:
   * Update the email configuration in the 'app.py' file, including the SMTP server, email credentials, and email content.

## Usage

1. Run the Flask app with the following command:
   `python app.py`
2. Access the application by navigating to 'http://localhost:5000' in your web browser.
3. Use the web interface to subscribe with your email address to receive the daily NBA stat leader updates.
4. At 10:00 PM every day, the app will automatically scrape the NBA statistics website, retrieve the latest daily stat leader data, and send an email to all subscribed users.
