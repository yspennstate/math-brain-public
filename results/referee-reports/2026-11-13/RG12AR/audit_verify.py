"""Cross-check report tables, output assertions, and resource limits."""
import json
import re
from pathlib import Path

root = Path('.')
exact = json.loads(Path('audit_exact_results.json').read_text())
assert len(exact) == 4
for name, result in exact.items():
    assert float(result['max_kernel_relative']) < 1e-61
    if name.startswith('sibuya'):
        assert result['harmonic_exact'] is True
assert float(exact['lacunary']['max_harmonic_residual']) < 1e-64
assert float(exact['lacunary']['omitted_beta_mass']) < 2.24e-68

paths = json.loads(Path('audit_simulation_results.json').read_text())
assert len(paths) == 12
lookup = {(row['model'], row['seed']): row for row in paths}
for row in paths:
    checkpoints = row['checkpoints']
    assert [a['n'] for a in checkpoints] == [100, 1000, 10000, 50000]
    for a, b in zip(checkpoints, checkpoints[1:]):
        assert a['sum_p_nu_negative'] < b['sum_p_nu_negative']
        assert a['sum_R'] < b['sum_R']
    for item in checkpoints:
        assert item['P'] > 0
        assert .25*item['sum_R'] <= item['sum_p_nu_negative'] <= item['sum_R']

report = Path('REPORT.md').read_text()
assert report.splitlines()[0] == 'Overall verdict: MINOR'
for heading in ['Theorem 1.1', 'Proposition 3.1', 'Lemma 3.2', 'Lemma 4.1',
                'Proposition 4.2', 'Lemma 4.3', 'Proposition 4.4', 'Remark 4.5',
                'Lemma 5.1', 'Lemma 5.2', '(R)']:
    assert '## '+heading in report
path_table = report.split('| Model | Seed |')[1].split('\n\n')[0]
names = {'type 2':'type_2', 'type 2.45':'type_2.45', 'type 2.5':'type_2.5', 'lacunary':'lacunary'}
count = 0
for line in path_table.splitlines():
    cells = [c.strip() for c in line.split('|')[1:-1]]
    if len(cells) != 7 or cells[0] not in names:
        continue
    model, seed, s1, s2, s3, perimeter, sumr = cells
    row = lookup[names[model], int(seed)]
    cp = row['checkpoints']
    for claimed, actual in zip([s1, s2, s3], [x['sum_p_nu_negative'] for x in cp[1:]]):
        assert abs(float(claimed)-actual) <= .50001e-6
    assert int(perimeter.replace(',', '')) == cp[-1]['P']
    assert abs(float(sumr)-cp[-1]['sum_R']) <= .50001e-6
    count += 1
assert count == 12

assert 'exact rational intervals disjoint: True' in Path('audit_pathologies_out.txt').read_text()
for stem in ['audit_exact', 'audit_simulate', 'audit_pathologies']:
    output = Path(stem+'_out.txt').read_text()
    match = re.search(r'seconds ([\d.]+) peak_rss_bytes (\d+)', output)
    assert match and float(match[1]) < 300 and int(match[2]) < 1_000_000_000
    assert 'Traceback' not in output

new_files = [p for p in root.iterdir() if p.is_file() and (p.name.startswith('audit_') or p.name == 'REPORT.md')]
size = sum(p.stat().st_size for p in new_files)
assert size < 200_000_000
print('PASS: all ten numbered-result sections and (R) are present')
print('PASS: four laws; exact harmonicity and high-precision disk/kernel checks')
print('PASS: twelve infinite-support paths; every numerical path-table entry verified')
print('PASS: accumulated (R) and R sums satisfy the universal factor bounds')
print('PASS: rationally certified nonregular lacunary phase ratios')
print('PASS: recorded runtime/RSS and total new artifact size below requested limits')
print('new_artifact_bytes', size)
