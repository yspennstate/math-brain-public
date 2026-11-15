#!/usr/bin/env python3
"""Check archived source identity and frozen definitions; does not run Lean."""
import hashlib
import json
import os
from pathlib import Path
import re
import resource
import signal
import sys

assert os.environ.get('OMP_NUM_THREADS') == '1'
signal.alarm(30)
BASE = Path(__file__).resolve().parent


def blob_sha(data):
    return hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()


def uncomment(s):
    # Lean block comments nest; a regexp alone is insufficient.
    out, i, depth = [], 0, 0
    while i < len(s):
        if s.startswith('/-', i):
            depth += 1
            i += 2
        elif depth and s.startswith('-/', i):
            depth -= 1
            i += 2
            if not depth:
                out.append(' ')
        elif depth:
            i += 1
        elif s.startswith('--', i):
            end = s.find('\n', i)
            i = len(s) if end < 0 else end
        else:
            out.append(s[i])
            i += 1
    assert depth == 0
    return ''.join(out)


def definition(s, name):
    s = uncomment(s)
    match = re.search(r'^(?:noncomputable )?(?:def|abbrev) ' + re.escape(name)
                      + r'\b', s, re.M)
    assert match, name
    start = match.start()
    boundary = re.search(r'\n(?:noncomputable |public )?(?:def|abbrev|theorem|lemma|'
                         r'instance|variable|section|end|open|namespace|@\[)\b',
                         s[match.end():])
    end = match.end() + boundary.start() if boundary else len(s)
    return re.sub(r'\s+', '', s[start:end])


def main():
    manifest = json.loads((BASE/'outside_manifest.json').read_text())
    print('commit:', manifest['commit'])
    repaired = 0
    for entry in manifest['files']:
        p = BASE/'outside'/entry['path']
        data = p.read_bytes()
        if blob_sha(data) != entry['sha']:
            # apply_patch added one terminal LF when saving a split ending in LF.
            assert data.endswith(b'\n') and blob_sha(data[:-1]) == entry['sha'], entry['path']
            p.write_bytes(data[:-1])
            data = data[:-1]
            repaired += 1
        assert blob_sha(data) == entry['sha'], entry['path']
    print('Git blob SHA-1 checks:', len(manifest['files']), 'PASS; terminal LF repairs:', repaired)
    read = lambda p: (BASE/'outside'/p).read_text()
    defs = read('FrogModel/Defs.lean')
    names = ['Vertex', 'root', 'tree', 'Step', 'step', 'walk', 'stepLaw',
             'Sample', 'frogMeasure', 'paths', 'wake', 'visits', 'Transient']
    for challenge in ['FrogModel/Challenge.lean', 'FrogModel/ChallengeRecurrent.lean']:
        text = read(challenge)
        compared = names if challenge.endswith('/Challenge.lean') else names[:-1]
        for name in compared:
            assert definition(defs, name) == definition(text, name), (challenge, name)
        print(challenge + ':', len(compared), 'definitions equal after comment/whitespace removal')
    assert definition(read('FrogModel/D3/Defs.lean'), 'Recurrent') == definition(
        read('FrogModel/ChallengeRecurrent.lean'), 'Recurrent')
    print('Recurrent definition equals recurrence challenge: PASS')
    for path in ['FrogModel/Defs.lean', 'FrogModel/D3/Defs.lean',
                 'FrogModel/Solution.lean', 'FrogModel/SolutionRecurrent.lean']:
        text = uncomment(read(path))
        assert not re.search(r'\b(sorry|axiom|native_decide)\b', text), path
    print('No sorry/axiom/native_decide in four inspected development files: PASS')
    print('Other imported modules and certificates are NOT checked by this script.')
    size = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    size = size if sys.platform == 'darwin' else size*1024
    assert size < 1024**3
    print('peak_RSS_bytes:', size)


if __name__ == '__main__':
    main()
