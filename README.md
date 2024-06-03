# School-Management-with-Mpesa-Integration
Django School Management system with STK  push integration
Overview
This project contains Django management commands to run the server and perform scheduled tasks via cron jobs. The following management commands and cron jobs are included:

Running the Server: python manage.py runserver
Cron Job to Check Callbacks: check_callbacks.py
Cron Job to Top Up Member Fund: check_registration_payments.py
Cron Job to Process Registrations: process_transactions.py
Prerequisites
Before running the commands and setting up cron jobs, ensure you have the following installed:

Python 3.x
Django
A virtual environment (optional but recommended)
Setup
Clone the Repository:

bash
Copy code
git clone <repository_url>
cd <repository_name>
Create and Activate a Virtual Environment:

bash
Copy code
python -m venv venv
source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
Install Dependencies:

bash
Copy code
pip install -r requirements.txt
Run Migrations:

bash
Copy code
python manage.py migrate
Start the Development Server:

bash
Copy code
python manage.py runserver
Running the Server
To run the Django development server, use the following command:

bash
Copy code
python manage.py runserver
Management Commands
The project includes custom management commands located in the management/commands directory. These commands can be executed manually or scheduled as cron jobs.

Check Callbacks
To run the command that checks for callbacks:

bash
Copy code
python manage.py check_callbacks
Top Up Member Fund
To run the command that checks and tops up member funds:

bash
Copy code
python manage.py check_registration_payments
Process Registrations
To run the command that processes registration transactions:

bash
Copy code
python manage.py process_transactions
Setting Up Cron Jobs
To automate the execution of these commands, set up cron jobs as follows:

Open the Crontab:

bash
Copy code
crontab -e
Add Cron Job Entries:

Add the following lines to schedule the tasks at your desired intervals:

bash
Copy code
# Check callbacks every 5 minutes
*/5 * * * * /path/to/venv/bin/python /path/to/project/manage.py check_callbacks >> /path/to/project/logs/check_callbacks.log 2>&1

# Top up member fund every hour
0 * * * * /path/to/venv/bin/python /path/to/project/manage.py check_registration_payments >> /path/to/project/logs/check_registration_payments.log 2>&1

# Process registration transactions daily at midnight
0 0 * * * /path/to/venv/bin/python /path/to/project/manage.py process_transactions >> /path/to/project/logs/process_transactions.log 2>&1
Ensure you replace /path/to/venv and /path/to/project with the actual paths to your virtual environment and project directory.

Logs
Logs for each cron job are saved in the logs directory. Ensure this directory exists or create it using:

bash
Copy code
mkdir logs
Troubleshooting
Virtual Environment Issues: Ensure your virtual environment is activated when running commands.
Permissions: Make sure the cron jobs have the necessary permissions to execute the scripts and write logs.
Dependencies: Verify that all dependencies are installed by checking the requirements.txt file.
Contributing
If you want to contribute to this project, please fork the repository and submit a pull request.

License
This project is licensed under the MIT License.
