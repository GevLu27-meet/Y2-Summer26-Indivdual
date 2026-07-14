# memory.py — save and load conversation history as a JSON file

import json
import os

HISTORY_FILE = 'history.json'

def save_history(history):
    with open(HISTORY_FILE, 'w') as f:
        json.dump(history, f)        # write list to file

def load_history():
    if not os.path.exists(HISTORY_FILE):
        return []                    # first run: no file yet
    with open(HISTORY_FILE, 'r') as f:
        return json.load(f)          # read list from file

# ─── How to use it in app.py ────────────────────────────
# history = load_history()           # load at start
# ... chat loop ...
# save_history(history)              # save after every turn