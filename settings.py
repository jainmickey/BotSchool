# Main IRC server settings
SERVER = '127.0.0.1'
PORT = 6667

# Other settings
DEBUG = False


# Register every bot here.
BOTS = {
        'helperbot': [
            'Helper',         # Bot Type
            'HelperBot',      # Nick
            'helperbot',      # Ident
            'password',       # Password
            '#help',          # Channel alloted to this bot
            'IRC Helper Bot', # Real name of this bot
            'hostname',       # Hostname
            ],
        'teacherbot': [
            'Teacher',         # Bot Type
            'TeacherBot',      # Nick
            'teacherbot',      # Ident
            'password',       # Password
            '#Tutorials',          # Channel alloted to this bot
            'IRC Teacher Bot', # Real name of this bot
            'hostname',       # Hostname
            ],
        }


# Enable every modules here 

MODULES = (
    'irc',
)
