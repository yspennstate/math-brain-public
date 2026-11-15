"""Audit source quotations and elementary constants; not a BEC proof checker."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import re

root = Path(__file__).resolve().parent
dossier = (root / 'VERIFY.md').read_text()
for i in range(3):
    source = (root / 'sources' / f'introduction-{i}.tex').read_text()
    theorem = re.search(r'\\begin\{theorem\}[\s\S]*?\\end\{theorem\}', source)[0]
    assert dossier.count(theorem) == 1, f'theorem quotation {i}'
print('PASS: all three main theorem quotations exactly match freshly opened sources')

for radius, expected in [(21, 79507), (20, 68921)]:
    count = sum(1 for _ in product(range(-radius, radius + 1), repeat=3))
    assert count == (2 * radius + 1) ** 3 == expected
assert 2 * 79507 == 159014
assert 2 * 68921 == 137842 < 159014
assert 30 - 2 * 11 == 8 > 1
print('PASS: independent anchor enumeration 79507 and 68921; two-copy constant 159014; separation gap 8 > r')

assert F(99, 100) * F(9, 10) == F(891, 1000)
assert F(98, 100) * F(9, 10) == F(441, 500)
assert 2 * F(99, 100) - 1 == F(98, 100)
assert -1 + 3 * F(1, 12) + F(1, 2) == -F(1, 4)
assert F(5, 2) + F(3, 4) * F(7, 4) == F(61, 16) < 4
assert F(7, 4) ** 2 > 3  # sqrt(3) < 7/4
print('PASS: normalization costs 891/1000 and 441/500; D exponent -1/4; midpoint distance < 4')

# Exponents are in the order (a, rho, alpha0).
s2 = (-1, -1, 1)
density = (-F(3, 2), -F(1, 2), F(3, 2))
temperature = (F(5, 2), F(3, 2), -F(5, 2))
assert tuple(x + y + z for x, y, z in zip(s2, density, temperature)) == (0, 0, 0)
assert tuple(-x - y for x, y in zip(s2, density)) == temperature
print('PASS: independent dimensional exponents give Ds^2*T0 = 1/4')

main = (root / 'sources' / '0' / 'build' / 'main.tex').read_text()
sections = re.findall(r'\\input\{sections/([^}]+)\}', main)
assert sections.index('bridges') + 1 == 6
assert sections.index('groups') + 1 == 7
assert sections.index('comparison') + 1 == 9
for section, label, expected in [('bridges', 'lem:single-hit', 3),
                                  ('groups', 'lem:conditional-law', 2),
                                  ('comparison', 'lem:cancellation', 3)]:
    source = (root / 'sources' / f'{section}.tex').read_text()
    prefix = source.split(r'\label{' + label + '}')[0]
    number = len(re.findall(r'\\begin\{(?:theorem|lemma|proposition|corollary|definition|remark)\}', prefix))
    assert number == expected, (section, number)
print('PASS: source order and shared theorem counter give Lemmas 6.3, 7.2 and 9.3')

assert (root / 'REPORT.md').read_text().startswith('VERDICT: PARTIAL ')
assert 'conditional' in (root / 'REPORT.md').read_text().splitlines()[0]
assert dossier.count('```') % 2 == 0
print('PASS: report format and dossier code fences')
