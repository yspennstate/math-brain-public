#!/usr/bin/env python3
"""Reconstruct the two original source files, with their actual original hashes.
The archived execution was NOT_CONFIRMED. This restores history; it does not run it.
"""
from pathlib import Path
import hashlib

root = Path(__file__).resolve().parent
old_display = 'def str_interval(a):return [str(a[0]),str(a[1])]'
new_display = '''def str_interval(a):
    # Preserve an outward rational enclosure without serializing huge exact denominators.
    grid=1<<96
    lo=a[0].numerator*grid//a[0].denominator
    hi=-((-a[1].numerator*grid)//a[1].denominator)
    return [str(F(lo,grid)),str(F(hi,grid))]'''
checker = (root / 'verify_remainder.py').read_text()
if checker.count(new_display) != 1:
    raise ValueError('The repaired source no longer has the expected display routine')
checker = checker.replace(new_display, old_display).encode()
report = (root / 'REPORT.md').read_bytes()
needle = b'\\frac12h_2(4\\delta)'
if report.count(needle) != 1:
    raise ValueError('Unexpected report revision')
report = report.replace(needle, b'\x0crac12h_2(4\\delta)')
originals = {
    'verify_remainder.py': (checker, '3dd9afec4638561cd88289c461ba1eca839cd9149597eb10e5f229df2ac2d662'),
    'REPORT.md': (report, '154304f47519385e5211458b223cf798ce3da14ae6e9f842c283119b8837ceb8'),
}
for name, (content, expected) in originals.items():
    if hashlib.sha256(content).hexdigest() != expected:
        raise ValueError('Original source reconstruction failed: ' + name)
    target = root / 'recovered' / name
    if target.exists() and target.read_bytes() != content:
        raise ValueError('Refusing to overwrite another historical version: ' + str(target))
    target.parent.mkdir(exist_ok=True)
    target.write_bytes(content)
    print(name, expected)
