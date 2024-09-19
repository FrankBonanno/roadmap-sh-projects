# GitHub Activity Tracker
This is a Python-based Command Line Interface (CLI) tool that allows users to fetch recent GitHub activity for any user, such as commits, issues, pull requests, stars, forks, and more.

## Project Page URL
https://roadmap.sh/projects/github-user-activity

## Features
- Fetches the most recent events for a given GitHub user using the GitHub API.
- Supports the use of a GitHub Personal Access Token (PAT) for authenticated requests to avoid rate limits.
- Displays event details like push events, issues created, forks, pull requests, and more.

## Prerequisites
Before you can run the project on your local machine, you need to have the following installed:

- **Python 3.x**: [Download and Install Python](https://www.python.org/downloads/)
- **pip**: This should come pre-installed with Python, but you can install it separately if needed.

### Optional:
- **Git**: [Download and Install Git](https://git-scm.com/downloads) for cloning the repository.

## Installation Guide

### 1. Clone the Repository
First, clone the project to your local machine using the following command:

```bash
git clone https://github.com/your-username/github-activity-tracker.git
cd github-activity-tracker
```

### 2. Set Up a Virtual Environment
It's recommended to use a virtual environment to manage your project dependencies. You can create and activate a virtual environment as follows:

```bash
# Create a virtual environment (optional, but recommended)
python -m venv venv

# Activate the virtual environment
# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### 3. Install the Dependencies
Once inside the project directory and with the virtual environment activated, install the required dependencies using `pip`:

```bash
pip install -e .
```

This command installs the project in **editable mode**, making the `github-activity` CLI available to use globally on your system.

### 4. Run the CLI Tool
You can now use the tool to fetch GitHub activity. Run the following command:

```bash
github-activity <username>
```

For example, to fetch recent activity for a GitHub user named `FrankBonanno`, run:

```bash
github-activity FrankBonanno
```

### 5. Using a Personal Access Token (PAT)
To avoid hitting GitHub's API rate limits, you can use a GitHub Personal Access Token (PAT). You can pass the token with the `--token` argument:

```bash
github-activity <username> --token <your_github_token>
```

To generate a Personal Access Token, follow these steps:
1. Go to [GitHub Personal Access Tokens](https://github.com/settings/tokens).
2. Generate a new token and copy it.
3. Use it with the `--token` flag.

### 6. Deactivate the Virtual Environment (Optional)
If you are done working on the project and want to deactivate the virtual environment, simply run:

```bash
# On Windows
venv\Scripts\deactivate

# On macOS/Linux
deactivate
```

## Contributing
Feel free to fork the project and submit pull requests! If you find any bugs or have suggestions, please open an issue on GitHub.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
