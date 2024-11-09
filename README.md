# file-syncer
File Syncer is a simple Python tool for comparing and synchronizing content between two text files, typically used for security or pentesting purposes. It compares a new file containing payloads, usernames, passwords, or a wordlist against an old file and ensures that any new content is appended to the old file. If the content already exists in the old file, it will not be added again. The tool also prints the changes in color for easy visualization.
# Usage
1. Clone the Repository (or download the script):
git clone https://github.com/ys0rk/file-syncer.git
cd file-syncer
2. Install Python Dependencies: Ensure that you have Python installed (version 3.x recommended). You don't need any additional libraries to run this tool, as it only uses built-in Python functionality.
3. Run the Script: Execute the script by running the following command:
python file_syncer.py
4.Follow the Prompts: The script will ask you to enter the paths of the two text files (old file and new file). The new file should contain the content to be synced, and the old file is the file where the new content will be added if it doesn't already exist.
