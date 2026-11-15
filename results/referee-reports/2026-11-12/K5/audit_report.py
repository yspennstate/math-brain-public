"""Check that the report transcribes the exact artifacts without rounding them."""
from pathlib import Path
from fractions import Fraction as F
import json
import re


def main():
    report = Path('REPORT.md').read_text()
    assert report.splitlines()[0] == 'Result: no improvement'
    assert report.count(chr(92)+'[') == report.count(chr(92)+']')
    assert all(line.count('$')%2 == 0 for line in report.splitlines())
    assert chr(92)+')' not in report
    rec = json.loads(Path('audited_search5_best.json').read_text())
    matrix_text = re.findall(r'```\n(.*?)\n```',report,re.S)[0]
    matrix = [[F(x) for x in row.split()] for row in matrix_text.splitlines()]
    assert matrix == [[F(x) for x in row] for row in rec['weights']]
    fractions = [F(int(a),int(b)) for a,b in re.findall(
        r'\\frac\{(\d+)\}\s*\{(\d+)\}',report)]
    leaf = next(r for r in json.loads(Path('leaf_exact.json').read_text())
                if r['n']==5 and r['t']==1000000)
    assert fractions == [F(leaf['original']),F(leaf['quotient']),
                         F(rec['original']),F(rec['quotient'])]
    for name in set(re.findall(r'`([A-Za-z0-9_]+\.py)`',report)):
        assert Path(name).is_file(),name
    print('PASS: report matrix and all four large rational times match exact artifacts.')
    print('PASS: result line, inline/display math delimiter checks, and program references.')


if __name__ == '__main__':
    main()
