import os

import dscord


dscord.load('system')
dscord.load('whitelist')
dscord.run(os.environ['TOKEN'])
