import glob
from pathlib import Path
from amit.utils import load_plug
import logging
from . import bot 
from sys import argv


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)
path = "amit/plugins/*.py"
files = glob.glob(path)
for name in files:
  with open(name) as a:
    pxt = Path(a.name)
    plugs = pxt.stem
    load_plug(plugs.replace(".py", ""))
    
print ("AMIT BOT HAS STARTED & LOADED ALL PLUGINS ")   

if __name__ == "__main__":
  if len(argv) not in (1, 3, 4):
    bot.disconnect()
  else:
    bot.run_until_disconnected()
