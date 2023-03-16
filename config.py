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
Type your license key into a private message and I will check the license server. 
If the license is valid you will be promoted to a Pro User.
"""

# Unknown message
UNKNOWN_MESSAGE = """\
Hi! I am the license verification bot. I can verify your license key for access to the '{GUILD}' Discord Server. 
Please send me your license key in a private message. DO NOT type your license key in the public channel.
"""

# Successfull setting role
SUCCESS_SETTING_ROLE = """\
You have been verified. You now have access to the Pro User chat."""

ERROR_SETTING_ROLE = """\
Could not set role, please try again or contact an admin."""

ERROR_LICENSE_NOT_VALID = """\
Your license key is not valid. Please try again or contact an admin."""

ERROR_LICENSE_SERVER_DOWN = """\
I could not contact the license server, please try again in a moment or contact an admin."""

ERROR_LICENSE_SERVER_ERROR = """\
There was an error."""

VERIFING_LICENSE = """\
Verifying license. One moment please..."""
