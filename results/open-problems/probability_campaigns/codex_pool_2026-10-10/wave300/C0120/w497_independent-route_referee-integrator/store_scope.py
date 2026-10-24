"""Read-only schema probe for the scoped C0120 store status check."""

import sqlite3
from pathlib import Path


path = Path("~/math-brain-build/local/population/brain.sqlite3")
connection = sqlite3.connect("file:" + path.as_posix() + "?mode=ro", uri=True, timeout=10)
for (name,) in connection.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name"):
    if name.startswith("sqlite_"):
        continue
    columns = [row[1] for row in connection.execute(f"PRAGMA table_info({name})")]
    print(name, columns)
