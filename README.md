Rematch Legends Association

A modular Python Discord bot designed to automate server administration, announcements, role management, and community functionality for the Rematch Legends Association.

Overview

Rematch Legends Association is a Python-based Discord bot built with discord.py.

The project is organized around modular cogs, allowing individual bot features and commands to be separated into manageable components. This structure makes the application easier to maintain and provides a foundation for adding new functionality as the Discord community grows.

The bot is designed to automate administrative tasks and improve server management through Discord-based commands and functionality.

Features

* Discord server automation
* Automated announcements
* Role assignment and management
* Modular command architecture
* Discord slash-command registration
* Environment-based configuration
* Asynchronous Discord functionality
* Deployable application configuration
* GitHub Actions workflow support
* Procfile-based deployment support

Technology Stack

Technology	Purpose
Python	Primary programming language
discord.py 2.3.2	Discord API and bot framework
aiohttp 3.9.1	Asynchronous HTTP functionality
python-dotenv 1.0.1	Environment variable management
Git / GitHub	Source control
GitHub Actions	Development automation
Procfile	Deployment configuration

The project’s current requirements.txt pins discord.py, aiohttp, and python-dotenv to specific versions. (GitHub)

Architecture

The project uses a modular structure to keep Discord functionality separated into individual components.

Rematch-Legends-Association/
│
├── .github/
│   └── workflows/
│       └── GitHub Actions workflows
│
├── cogs/
│   └── Modular Discord bot features
│
├── src/
│   └── Supporting application source code
│
├── config.py
│   └── Application configuration
│
├── main.py
│   └── Bot entry point
│
├── register.commands.py
│   └── Discord command registration
│
├── requirements.txt
│   └── Python dependencies
│
├── Procfile
│   └── Deployment configuration
│
├── .gitignore
├── LICENSE
└── README.md

The repository currently contains 30 commits and includes GitHub Actions, modular cogs, source code, command registration, configuration, and deployment files. (GitHub)

Modular Cogs

Bot functionality is organized using Discord.py cogs.

This approach allows individual features to be developed independently instead of placing all bot functionality inside a single Python file.

Benefits include:

* Easier feature development
* Improved code organization
* Better maintainability
* Simplified debugging
* Easier expansion of bot functionality

Discord Commands

The project includes a dedicated command-registration script:

register.commands.py

This separates command registration from the primary application entry point and supports a more organized Discord bot architecture.

Configuration

Application configuration is handled through:

config.py

The project also includes python-dotenv, allowing configuration values and environment variables to be managed outside of the application’s source code. (GitHub)

Security: Never commit Discord bot tokens, database credentials, API keys, or other secrets to GitHub.

Asynchronous Programming

The bot uses Python’s asynchronous capabilities through discord.py and aiohttp.

This allows the application to handle Discord events and asynchronous operations without unnecessarily blocking the bot’s event loop.

Deployment

The repository includes a:

Procfile

which provides deployment configuration for supported hosting environments.

The project can be deployed to a hosted environment and is structured so that the application can be migrated to other hosting infrastructure as needed.

GitHub Actions

The repository contains GitHub Actions workflow configuration under:

.github/workflows/

This provides a foundation for automating development and deployment-related tasks through GitHub.

Getting Started

Prerequisites

Before running the bot, make sure you have:

* Python 3.x
* A Discord bot application
* A Discord server where the bot can be installed
* Git

Clone the Repository

git clone https://github.com/kwasserman/Rematch-Legends-Association.git
cd Rematch-Legends-Association

Create a Virtual Environment

Windows:

python -m venv venv
venv\Scripts\activate

macOS/Linux:

python3 -m venv venv
source venv/bin/activate

Install Dependencies

pip install -r requirements.txt

Configure Environment Variables

Create the required environment configuration based on the variables expected by the application.

Do not commit sensitive credentials to source control.

Run the Bot

python main.py

Development Practices

This project demonstrates experience with:

* Python application development
* Discord API integration
* discord.py
* Asynchronous programming
* Modular application architecture
* Environment-based configuration
* Command registration
* Git and GitHub
* GitHub Actions
* Deployment configuration
* Application maintenance

Future Improvements

Potential areas for future development include:

* Expanding server-management commands
* Adding additional automated announcements
* Expanding role-management functionality
* Adding database-backed features
* Improving logging and monitoring
* Adding automated testing
* Expanding CI/CD automation
* Migrating to additional self-hosted infrastructure

License

This project is licensed under the MIT License.

See the LICENSE file for the complete license text. (GitHub)
