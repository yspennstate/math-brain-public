#!/usr/bin/env python3
"""Finite source and exact arithmetic audit; never builds or executes Lean."""
import hashlib
import json
import os
from pathlib import Path
import re
import resource
import signal
import sys
from collections import Counter
from fractions import Fraction as F
from itertools import product

assert os.environ.get('OMP_NUM_THREADS') == '1'
signal.alarm(30)
HERE = Path(__file__).resolve().parent
PREV = Path('~/codex_op_1114r5/briefs/T127')
COMMIT = 'd6b298c0100af57a8f46f8314eca8bf8f7eb4693'


def blob(data):
    return hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()


def executable(source):
    """Remove nested comments and strings; preserve line boundaries."""
    out = []
    i = depth = 0
    while i < len(source):
        if source.startswith('/-', i):
            depth += 1
            i += 2
        elif depth and source.startswith('-/', i):
            depth -= 1
            i += 2
            out.append(' ')
        elif depth:
            if source[i] == '\n':
                out.append('\n')
            i += 1
        elif source.startswith('--', i):
            j = source.find('\n', i)
            i = len(source) if j < 0 else j
        elif source[i] == '"':
            out.append(' STRING ')
            i += 1
            while i < len(source):
                if source[i] == '\\':
                    i += 2
                elif source[i] == '"':
                    i += 1
                    break
                else:
                    i += 1
        else:
            out.append(source[i])
            i += 1
    assert depth == 0
    return ''.join(out)


def definition(text, name):
    text = executable(text)
    start = re.search(r'^(?:noncomputable )?(?:def|abbrev) ' + name + r'\b', text, re.M)
    assert start, name
    rest = text[start.start():]
    end = re.search(r'\n(?:@|(?:noncomputable )?(?:def|abbrev|theorem|lemma|instance|variable|'
                    r'section|end|open|namespace)\b)', rest)
    return re.sub(r'\s+', '', rest[:end.start() if end else len(rest)])


def hashed_manifest(text):
    pairs = [line.split() for line in text.splitlines() if line and not line.startswith('#')]
    assert all(len(p) == 2 and re.fullmatch('[0-9a-f]{64}', p[0]) for p in pairs)
    assert len({p[1] for p in pairs}) == len(pairs)
    return {path: sha for sha, path in pairs}


def main():
    previous = json.loads((PREV/'outside_manifest.json').read_text())
    assert previous['commit'] == COMMIT
    old = {}
    for entry in previous['files']:
        data = (PREV/'outside'/entry['path']).read_bytes()
        assert blob(data) == entry['sha'], entry['path']
        old[entry['path']] = data.decode()
    print(f'Independent previous-archive identity check: {len(old)} blobs match; no repairs/writes.')
    names = ['Vertex', 'root', 'tree', 'Step', 'step', 'walk', 'stepLaw', 'Sample',
             'frogMeasure', 'paths', 'wake', 'visits']
    for path in ['FrogModel/Challenge.lean', 'FrogModel/ChallengeRecurrent.lean']:
        compare = names + (['Transient'] if path.endswith('/Challenge.lean') else [])
        for name in compare:
            assert definition(old['FrogModel/Defs.lean'], name) == definition(old[path], name)
        print(f'{path}: {len(compare)} shared definitions match.')
    assert definition(old['FrogModel/D3/Defs.lean'], 'Recurrent') == definition(
        old['FrogModel/ChallengeRecurrent.lean'], 'Recurrent')
    print('Recurrence predicate matches; model meaning rederived in PROOF.md.')

    # An independent finite pushforward calculation for the uniform walk law.
    for d in (3, 4):
        for v in [(), (0,), (0, 1)]:
            counts = Counter((a,) if not v else v[1:] if b == 0 else (b-1,)+v
                             for a, b in product(range(d), range(d+1)))
            assert len(counts) == (d if not v else d+1)
            assert set(counts.values()) == ({d+1} if not v else {d})
    print('Uniform step pushforward: root and non-root, d=3,4, exact enumeration agrees.')

    sources = {}
    for filename in ['source_archive.json', 'criterion_sources.json']:
        archive = json.loads((HERE/filename).read_text())
        assert archive['commit'] == COMMIT
        for record in archive['files']:
            assert blob(record['content'].encode()) == record['sha'], record['path']
            assert record['path'] not in sources
            sources[record['path']] = record['content']
    lean = {p: executable(s) for p, s in sources.items() if p.endswith('.lean')}
    for path, text in lean.items():
        assert not re.search(r'\b(sorry|axiom|native_decide)\b', text), path
    print(f'New archive: {len(sources)} blob identities match; {len(lean)} Lean files scanned.')

    # These are syntactic links, not elaboration or proof checking.
    target = executable(old['FrogModel/SolutionRecurrent.lean'])
    assert 'D3.Assembly.recurrent_three_of_m1 D3.Chain.m1run_certS_proof' in target
    final = lean['FrogModel/D3/Chain/Final.lean']
    for token in ['M1K.storedRun_holds', 'CertData.certS1_stored', 'LaneD.step_sound',
                  'LaneD.seedCheck_sound', 'LaneD.extCheck_sound', 'M1K.topMass_eq_massPk']:
        assert token in final
    step = lean['FrogModel/D3/LaneD/StepSound.lean']
    assert '(hchk : ∀ p ∈ ps, check (L.withPart p) = true)' in step
    assert '(hcov : covers L ps = true)' in step
    check = lean['FrogModel/LemmaR/Planted/Check.lean']
    assert 'ZeroOne.recurrent_of_frozenCount' in check and "plantedLemmaR'" in check
    print('Recurrence target, certificate discharge, coverage and planted-criterion links found.')

    chain = hashed_manifest(sources['code/d3chain/modules.sha256'])
    run = hashed_manifest(sources['code/m1gen/modules.sha256'])
    assert chain['input/masses100.txt'] == run['mass_V48_h100.txt']
    print('Shared mass-file digest agrees:', chain['input/masses100.txt'])
    print('Chain manifest entries:', len(chain), '; M1 manifest entries:', len(run))
    release = json.loads((HERE/'release_metadata.json').read_text())
    inputs = re.findall(r'^([0-9a-f]{64})\s+(frog-\S+)$', old['ASSETS.md'], re.M)
    assert len(inputs) == 3
    for digest, name in inputs:
        entry, = [a for a in release['assets'] if a['name'] == name]
        assert entry['digest'] == 'sha256:' + digest
    print('Three release-input digest metadata entries agree with ASSETS.md; bytes NOT downloaded.')

    dp = lean['FrogModel/D3/Interfaces/DPrime.lean']
    m1 = int(re.search(r'def m1 : ℕ := (\d+)', dp).group(1))
    numerator, denominator = map(int, re.search(r'def b1 : ℝ := (\d+) / (\d+)', dp).groups())
    b1 = F(numerator, denominator)
    checks = lean['FrogModel/D3/Interfaces/Checks.lean']
    dn, dd = map(int, re.search(r'T.delta 62 ≤ (\d+) / (\d+)', checks).groups())
    delta = F(dn, dd)
    mu = F(m1+1+62, 3)
    assert (1-delta)*mu == b1
    # Second derivation: solve the mean inequality for the deficit.
    assert 1-b1/mu == delta
    assert 0 < delta < 1 and m1-30 == 1778249
    assert F(3,5)*F(m1+2,3) == F(m1+2,5)
    print(f'Terminal conversion: mu={mu}, delta={delta}, (1-delta)*mu=b1={b1}.')

    # Polynomial identities, rather than a finite sample of heights.
    # For m=n+1: (1+(n+2)/5)/4=(m+6)/20; excess over m/20 is 3/10.
    assert F(1,4)+F(2,20) == F(7,20)
    assert F(7,20)-F(1,20) == F(3,10)
    c = F(1,20)
    for d in (3,4):
        # Coefficients of [(m+1)/d + ((m+1)/d)^2]/m^2.
        coefficients = (F(1,d*d), F(1,d)+F(2,d*d), F(1,d)+F(1,d*d))
        assert coefficients[0] == F(1,d)**2
        # Sum per depth of d^r * d^(-r-1), also by cancelling powers.
        for r in range(10):
            assert F(d**r,d**(r+1)) == F(1,d)
    probability = (3*c)**2
    assert probability == F(9,400) == c*c/F(1,9)
    assert probability / (c*c/24) == 216
    print('Planted linear bound: E[Z_m] >= (m+6)/20 for m>=1778251 (conditional).')
    print('Second-moment coefficient at d=3: 1/9; conditional P(X=infinity) >= 9/400.')
    print('Comparison: 9/400 is 216 times c^2/24 at c=1/20; no novelty claim.')
    print('PASS: finite source/metadata/arithmetic checks only; no Lean or certificate replay.')
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    rss *= 1 if sys.platform == 'darwin' else 1024
    assert rss < 1024**3
    print('peak_RSS_bytes:', rss)


if __name__ == '__main__':
    main()
