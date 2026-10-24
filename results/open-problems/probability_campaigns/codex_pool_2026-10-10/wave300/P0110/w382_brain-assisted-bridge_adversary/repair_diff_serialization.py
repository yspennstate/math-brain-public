"""Regenerate the diff from frozen copies without Windows text-mode translation."""
from pathlib import Path
import difflib
import json

ROOT=Path(__file__).resolve().parent
before=(ROOT/'copies'/'brain.before.py').read_bytes()
after=(ROOT/'copies'/'brain.after.py').read_bytes()
path=ROOT/'patches'/'01_recall_retracted_tag_override.diff'
old=path.read_bytes()
patch=''.join(difflib.unified_diff(before.decode('utf-8').splitlines(True),
    after.decode('utf-8').splitlines(True),fromfile='a/.claude/dreaming/brain.py',tofile='b/.claude/dreaming/brain.py'))
path.write_bytes(patch.encode('utf-8'))
print(json.dumps({'baseline_CRLF':before.count(b'\r\n'),'baseline_LF':before.count(b'\n'),
    'old_diff_CRLF':old.count(b'\r\n'),'old_diff_CRCRLF':old.count(b'\r\r\n'),
    'new_diff_CRLF':path.read_bytes().count(b'\r\n'),'copies_changed':False}))
