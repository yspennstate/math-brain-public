"""Driver for the exact balanced-fusion evaluator (binary fusion, d >= 6)."""
import argparse
import hashlib
import json
import pathlib
import struct
import subprocess
import time
from fractions import Fraction as F
from universal_fusion import edge_table, balanced_step, signal
from fourth_polynomial_certificate import memory_check

ROOT = pathlib.Path(__file__).resolve().parent
CSC = 'C:/Windows/Microsoft.NET/Framework64/v4.0.30319/csc.exe'


def run(d, N, eta, steps, bits, seconds, radius, resume, validate):
    memory_check()
    assert 2 <= d <= 1000 and N % 3 == 0 and N <= 96
    assert 0 <= eta <= 1 and 1 <= bits <= 40 and seconds <= 360
    core = ROOT/'TernaryBp.cs'
    assert hashlib.sha256(core.read_bytes()).hexdigest() == 'a508360d91fea9162562925ee251e6ac8b72c253d217dce562e37192dadbe2a9'
    sources = [core, ROOT/'BalancedBp.cs']
    exe = ROOT/'BalancedBp.exe'
    flags = subprocess.CREATE_NO_WINDOW
    if not exe.exists() or any(p.stat().st_mtime > exe.stat().st_mtime for p in sources):
        subprocess.run([CSC, '/nologo', '/optimize+', '/target:exe',
                        '/main:BalancedProgram', '/out:'+str(exe),
                        '/r:System.Numerics.dll', *map(str, sources)],
                       check=True, cwd=ROOT, timeout=60, creationflags=flags)
    stem = ROOT/f'universal_unit_N{N}_1'
    meta = json.loads(stem.with_suffix('.json').read_text())
    assert meta['grid'] == N and meta['left_strength'] == meta['right_strength'] == '1'
    assert meta['byteorder'] == 'little'
    for name, item in meta['files'].items():
        data = pathlib.Path(str(stem)+'_'+name+'.bin').read_bytes()
        assert len(data) == item['bytes']
        assert hashlib.sha256(data).hexdigest() == item['sha256']
    del data
    keys = [tuple(v) for v in meta['keys']]
    common = int(meta['common'])
    scale = 1 << bits
    assert scale * scale * common < 2**128
    edge = edge_table(N, eta, keys)
    assert scale * edge[0] < 2**64
    tag = f'd{d}_N{N}_{str(eta).replace("/", "-")}'
    outpath = ROOT/f'balanced_bp_fast_{tag}.json'
    vertex = keys.index((0, 0, N))
    masses = [0] * len(keys)
    masses[vertex] = scale
    initial, rows = 0, []
    if resume and outpath.exists():
        old = json.loads(outpath.read_text())
        assert (old['degree'], old['grid'], old['eta'], old['bits']) == (d,N,str(eta),bits)
        assert old['source_sha256'] == {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in sources}
        rows = old['rows']
        initial = rows[-1]['depth']
        masses = list(map(int, old['final_integer_masses']))
    assert sum(masses) == scale
    if initial >= steps:
        print('Already complete at', initial, flush=True)
        return
    before = masses[:]
    edgepath = ROOT/f'balanced_{tag}_edge.txt'
    edgepath.write_text('\n'.join(','.join(f'{k}:{v}' for k,v in sorted(row.items()))
                                  for row in edge[1])+'\n', encoding='utf-8')
    inp, state = ROOT/f'balanced_{tag}_input.bin', ROOT/f'balanced_{tag}_state.bin'
    inp.write_bytes(struct.pack('<i', initial)+struct.pack('<'+'Q'*len(keys), *masses))
    chi = ROOT/f'balanced_{tag}_chi.txt'
    chi.write_text('\n'.join(str(3*sum(v*v for v in k)-N*N) for k in keys)+'\n', encoding='utf-8')
    tsv, config = ROOT/f'balanced_{tag}_rows.tsv', ROOT/f'balanced_{tag}_config.txt'
    config.write_text('\n'.join(map(str, [stem, edgepath, N, bits, len(keys), vertex,
        d, steps, seconds, common, edge[0], inp, chi, tsv, state,
        radius.numerator, radius.denominator]))+'\n', encoding='utf-8')
    started = time.monotonic()
    subprocess.run([str(exe), str(config)], cwd=ROOT, check=True,
                   timeout=seconds+90, creationflags=flags)
    raw = state.read_bytes()
    depth = struct.unpack_from('<i', raw)[0]
    assert len(raw) == 4+8*len(keys)
    masses = list(struct.unpack_from('<'+'Q'*len(keys), raw, 4))
    assert sum(masses) == scale
    newrows = []
    for line in tsv.read_text(encoding='utf-8-sig').splitlines():
        dep, x, losses = line.split('\t')
        dep = int(dep)
        assert dep == initial+len(newrows)+1
        newrows.append({'depth': dep, 'second_moment_upper': x,
                        'node_rounding_masses': losses.split(',')})
    assert newrows[-1]['depth'] == depth
    assert signal(keys, masses, N, scale) == F(newrows[-1]['second_moment_upper'])
    rows += newrows
    result = {'status': 'exact finite-depth evaluation',
        'degree': d, 'grid': N, 'eta': str(eta), 'bits': bits, 'rows': rows,
        'final_integer_masses': list(map(str, masses)), 'orbit_keys': keys,
        'stopping_radius': str(radius),
        'grouping': 'physical one-body edge, independent groups by binary powers; root revelation after each node',
        'source_sha256': {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in sources},
        'universal_table_sha256': hashlib.sha256(stem.with_suffix('.json').read_bytes()).hexdigest(),
        'native_wall_seconds': time.monotonic()-started}
    outpath.write_text(json.dumps(result, indent=2), encoding='utf-8')
    if validate:
        from universal_fusion import unit_table
        table = unit_table(N)
        check = before
        for row in newrows:
            check, losses = balanced_step(table, edge, check, scale, d)
            assert list(map(str, losses)) == row['node_rounding_masses']
            assert signal(keys, check, N, scale) == F(row['second_moment_upper'])
        assert check == masses
        verdict = {'status': 'PASS', 'degree': d, 'grid': N, 'eta': str(eta),
                   'start_depth': initial, 'end_depth': depth,
                   'all_rows_and_final_masses_match': True,
                   'source_sha256': result['source_sha256']}
        (ROOT/f'balanced_reference_{tag}.json').write_text(json.dumps(verdict, indent=2), encoding='utf-8')
        print(json.dumps(verdict), flush=True)
    print(json.dumps({'depth': depth, 'signal': rows[-1]['second_moment_upper'],
                      'artifact': str(outpath)}), flush=True)


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--degree', type=int, required=True)
    p.add_argument('--grid', type=int, default=6)
    p.add_argument('--eta', default='53/237')
    p.add_argument('--steps', type=int, default=4)
    p.add_argument('--bits', type=int, default=32)
    p.add_argument('--seconds', type=float, default=30)
    p.add_argument('--radius', default='0')
    p.add_argument('--resume', action='store_true')
    p.add_argument('--validate', action='store_true')
    a = p.parse_args()
    run(a.degree,a.grid,F(a.eta),a.steps,a.bits,a.seconds,F(a.radius),a.resume,a.validate)
