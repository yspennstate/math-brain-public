#!/usr/bin/env python3
"""Prepare exact UTF-8/tree content and local Git blob pins for a frozen package."""
import argparse
import hashlib
import json
from pathlib import Path

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--root', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    entries, pins = [], []
    for path in sorted(args.root.rglob('*')):
        if not path.is_file():
            continue
        data = path.read_bytes()
        relative = path.relative_to(args.root).as_posix()
        git_sha = hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()
        pin = {'path': relative, 'sha': git_sha, 'sha256': hashlib.sha256(data).hexdigest(), 'bytes': len(data)}
        pins.append(pin)
        entry = {'path': relative, 'mode': '100644', 'type': 'blob'}
        if path.suffix in {'.png', '.pdf', '.zip'}:
            entry['sha'] = git_sha  # Upload the binary blob before creating the tree.
        else:
            entry['content'] = data.decode('utf-8')  # Preserve CRLF and terminal bytes exactly.
        entries.append(entry)
    payload = {'tree_elements': entries, 'pins': pins}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, ensure_ascii=True, separators=(',', ':')))
    print(json.dumps({'entries': len(entries), 'transport_bytes': args.output.stat().st_size}))

if __name__ == '__main__':
    main()
