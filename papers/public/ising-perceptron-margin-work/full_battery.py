"""End-to-end meta-verification battery on the final committed tree:
sympy identities, then per certified margin the assembler, the
portable checker, every Lean kernel file, and the mutation battery.
One ledger, every exit code captured unmasked."""
import os
import shutil
import subprocess
import sys

REPO = os.path.dirname(os.path.abspath(__file__))


def _find_lean():
    # resolve the Lean binary from the environment rather than pinning
    # a toolchain version: PATH first (the elan shim, which also sets
    # up the toolchain env), then the elan default-toolchain bin.  Set
    # LEAN=/path/to/lean to override.
    env = os.environ.get('LEAN')
    if env and os.path.exists(env):
        return env
    onpath = shutil.which('lean')
    if onpath:
        return onpath
    shim = os.path.expanduser('~/.elan/bin/lean')
    if os.path.exists(shim) or os.path.exists(shim + '.exe'):
        return shim
    return 'lean'  # last resort; run() will report the failure


LEAN = _find_lean()
results = []


def run(name, args, cwd=REPO):
    r = subprocess.run(args, cwd=cwd, capture_output=True, text=True)
    ok = r.returncode == 0
    results.append((name, ok))
    tail = (r.stdout or r.stderr).strip().splitlines()
    print('%-42s %s   %s' % (name, 'PASS' if ok else 'FAIL',
                             tail[-1][:60] if tail else ''), flush=True)
    return ok


# the battery is background verification: demote ourselves so the
# machine never feels it (and the lean kernel checks stop
# dying to memory pressure we ourselves aggravate)
if sys.platform == 'win32':
    try:
        import ctypes
        ctypes.windll.kernel32.SetPriorityClass(
            ctypes.windll.kernel32.GetCurrentProcess(), 0x4000)
    except Exception:
        pass

run('sympy identity battery', [sys.executable, 'sympy_identities.py'])
# the negative lane's record-level acceptance (209 slabs, coverage
# [-1.05, -0.9455] abutting the rectangle strip edge, every check's
# serialized endpoints re-tested against its want direction)
run('negative lane acceptance', [sys.executable, 'verify_lane1.py'])
# the certified margin registry: discovery from the directory listing
# alone would let a missing tag pass silently, so the expected set is
# pinned here and its absence is a failure, not a smaller loop
EXPECTED_TAGS = ['0p02', '0p05', '0p0995', '0p08', '0p115', '0p13',
                 '0p16', 'n0p05', 'n0p15', 'n0p25', 'n0p35', 'n0p45']
tags = sorted(d for d in os.listdir(
    os.path.join(REPO, 'lean_skeleton', 'generated'))
    if os.path.isdir(os.path.join(REPO, 'lean_skeleton',
                                  'generated', d)))
missing = sorted(set(EXPECTED_TAGS) - set(tags))
extra = sorted(set(tags) - set(EXPECTED_TAGS))
results.append(('expected margin registry (%d tags)' % len(EXPECTED_TAGS),
                not missing))
print('%-42s %s%s%s' % ('expected margin registry',
      'PASS' if not missing else 'FAIL',
      ('   missing: %s' % ','.join(missing)) if missing else '',
      ('   (extra present: %s)' % ','.join(extra)) if extra else ''),
      flush=True)
for tag in tags:
    run('assembler %s' % tag, [sys.executable, 'assemble_2varfn.py', tag])
    run('portable %s' % tag,
        [sys.executable, 'portable_check.py', '--tag', tag])
    gen = os.path.join(REPO, 'lean_skeleton', 'generated', tag)
    for f in sorted(os.listdir(gen)):
        if f.endswith('.lean'):
            ok = run('lean %s/%s' % (tag, f), [LEAN, os.path.join(gen, f)])
            if not ok:
                # kernel checks of the big Int lists die on transient
                # memory pressure (four confirmed OOM artifacts on
                # byte-identical green files, 07-17/18); one quiet
                # retry separates that from a real rejection
                import time as _t
                _t.sleep(20)
                results.pop()
                run('lean %s/%s (retry)' % (tag, f),
                    [LEAN, os.path.join(gen, f)])
    run('mutants %s' % tag,
        [sys.executable, 'mutate_margin.py', '--lean', LEAN, '--tag', tag],
        cwd=os.path.join(REPO, 'lean_skeleton'))

n_ok = sum(1 for _, ok in results if ok)
print('\nBATTERY: %d/%d PASS%s' % (n_ok, len(results),
      '' if n_ok == len(results) else '  <-- FAILURES ABOVE'), flush=True)
sys.exit(0 if n_ok == len(results) else 1)
