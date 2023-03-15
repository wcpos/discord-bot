# Name of the Server.
GUILD = "WooCommerce POS"
# Name of the role the students should get.

PRO_ROLE = "Pro User"

# Path to log file
LOGFILE_PATH = "bot.log"

# Welcome message


def WELCOME_MSG(name):
    msg = f"""\
Hi {name}, welcome to the '{GUILD}' Discord Server."""
    return msg


# Help message
HELP_MSG = f"""\
This bot is used to verify Pro licenses for access to the '{GUILD}' Discord Server. 
"""

# Unknown message
UNKNOWN_MESSAGE = """\
I could not understand your message.
For further help use the command "help" .
"""

# Successfull setting role
SUCCESS_SETTING_ROLE = """\
You have been verified. You will be given Pro access."""

# Error setting role to student
ERROR_SETTING_ROLE = """\
Could not set role, please try again or contanct an admin."""

ERROR_LICENSE_NOT_VALID = """\
Your license key is not valid. Please try again or contact an admin."""
