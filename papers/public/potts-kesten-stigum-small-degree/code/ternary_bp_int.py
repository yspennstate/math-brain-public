"""Exact two-stage information-upgraded BP on the regular ternary tree.

Prefix: two independent eta-edge branches. Final fusion: prefix strength 1,
third-child strength eta. Each stage upgrades to the simplex grid and rounds
discarded orbit masses into full revelation. No floating arithmetic enters bounds.
"""
import argparse, array, hashlib, json, pathlib, sys, time
from fractions import Fraction as F
from itertools import product
from quantized_bp import orbits, simplex_split, round_up_mass
from quantized_bp_int import table_cache as prefix_table, reference_check
from fourth_polynomial_certificate import memory_check

ROOT = pathlib.Path(__file__).resolve().parent
ETA = F(2887, 5000)
NAMES = [('pair_i','H'),('pair_j','H'),('offsets','I'),('dest_indices','H'),('numerators','Q')]


def asymmetric_table(N, lam):
    stem = ROOT/f'ternary_asymmetric_N{N}_{str(lam).replace("/","-")}'
    header = stem.with_suffix('.json')
    if header.exists():
        meta = json.loads(header.read_text(encoding='utf-8'))
        assert meta['grid'] == N and meta['right_strength'] == str(lam) and meta['left_strength'] == '1'
        assert meta['byteorder'] == sys.byteorder
        values = []
        for name, code in NAMES:
            path = pathlib.Path(str(stem)+'_'+name+'.bin')
            assert path.stat().st_size == meta['files'][name]['bytes']
            arr = array.array(code)
            with path.open('rb') as f:
                arr.fromfile(f, meta['files'][name]['count'])
            values.append(arr)
        keys = [tuple(k) for k in meta['keys']]
        assert len(values[0]) == len(keys)**2 and len(values[2]) == len(keys)**2+1
        assert len(values[3]) == len(values[4]) == values[2][-1]
        return keys, int(meta['common']), *values
    keys, vertices = orbits(N)
    A, B = lam.numerator, lam.denominator
    common = 108*B*N*N
    assert common < 2**64 and len(keys) < 2**16
    lookup = {key:i for i,key in enumerate(keys)}
    ii, jj = array.array('H'), array.array('H')
    offsets, kk, nn = array.array('I',[0]), array.array('H'), array.array('Q')
    started = time.monotonic()
    for i, left in enumerate(keys):
        for j in range(len(keys)):
            counts = {}
            factor = 36//len(vertices[j])
            for right in vertices[j]:
                z = [3*left[a]*((B-A)*N+3*A*right[a]) for a in range(3)]
                total = sum(z)
                assert total > 0
                floors = [N*v//total for v in z]
                remainder = [N*z[a]-floors[a]*total for a in range(3)]
                missing = N-sum(floors)
                assert missing in (0,1,2)
                if missing == 0:
                    dest = lookup[tuple(sorted(floors))]
                    counts[dest] = counts.get(dest,0)+factor*total
                else:
                    for a in range(3):
                        vertex = floors.copy()
                        if missing == 1:
                            vertex[a] += 1
                            weight = remainder[a]
                        else:
                            for b in range(3):
                                vertex[b] += int(b != a)
                            weight = total-remainder[a]
                        if weight:
                            assert weight > 0
                            dest = lookup[tuple(sorted(vertex))]
                            counts[dest] = counts.get(dest,0)+factor*weight
            assert sum(counts.values()) == common
            ii.append(i); jj.append(j)
            for dest, value in sorted(counts.items()):
                kk.append(dest); nn.append(value)
            offsets.append(len(nn))
        if i % 100 == 0:
            size = sum(v.itemsize*len(v) for v in (ii,jj,offsets,kk,nn))
            assert size < 350*1024**2
            print('asymmetric N',N,'row',i,'/',len(keys),'MB',round(size/2**20,2),'seconds',round(time.monotonic()-started,1),flush=True)
        assert time.monotonic()-started < 480, 'Do not enlarge without resumable table construction'
    values = [ii,jj,offsets,kk,nn]
    meta = {'grid':N,'left_strength':'1','right_strength':str(lam),
            'common':str(common),'keys':keys,'byteorder':sys.byteorder,'files':{}}
    for (name,code), value in zip(NAMES,values):
        path = pathlib.Path(str(stem)+'_'+name+'.bin')
        with path.open('wb') as f:
            value.tofile(f)
        meta['files'][name] = {'count':len(value),'bytes':path.stat().st_size,
                              'sha256':hashlib.sha256(path.read_bytes()).hexdigest()}
    header.write_text(json.dumps(meta),encoding='utf-8')
    return keys, common, *values


def apply_table(table, left, right, scale, symmetric):
    keys, common, ii, jj, offsets, kk, nn = table
    raw = [0]*len(keys)
    for row in range(len(ii)):
        factor = left[ii[row]]*right[jj[row]]
        if symmetric and ii[row] != jj[row]:
            factor *= 2
        if factor:
            for k in range(offsets[row],offsets[row+1]):
                raw[kk[k]] += factor*nn[k]
    assert sum(raw) == scale*scale*common
    rounded = [v//(scale*common) for v in raw]
    missing = scale-sum(rounded)
    assert missing >= 0
    rounded[keys.index((0,0,sum(keys[0])))] += missing
    return rounded, missing


def reference_pair(N, lam, keys, i, j):
    _, vertices = orbits(N)
    lookup = {key:k for k,key in enumerate(keys)}
    result = {}
    for p,r in product(vertices[i],vertices[j]):
        z = [3*F(p[a],N)*(1-lam+3*lam*F(r[a],N)) for a in range(3)]
        total = sum(z)
        assert total > 0
        weight = total/(3*len(vertices[i])*len(vertices[j]))
        for vertex,w in simplex_split([v/total for v in z],N):
            k = lookup[tuple(sorted(vertex))]
            result[k] = result.get(k,F(0))+weight*w
    assert sum(result.values()) == 1
    return result


def validate(N, lam, prefix, merge):
    started = time.monotonic()
    if N <= 12:
        reference_check(N,lam,prefix)
    keys, common, ii, jj, offsets, kk, nn = merge
    if N <= 12:
        rows = list(range(len(ii)))
    else:
        rows = sorted(set([0,len(ii)-1,len(ii)//2]+[(k*7919+17)%len(ii) for k in range(28)]))
    for row in rows:
        actual = {kk[k]:F(nn[k],common) for k in range(offsets[row],offsets[row+1])}
        assert actual == reference_pair(N,lam,keys,ii[row],jj[row])
    finite = []
    if N <= 12:
        scale = 1<<40
        vertex = keys.index((0,0,N))
        masses = [0]*len(keys); masses[vertex] = scale
        ref = [F(v,scale) for v in masses]
        for depth in range(1,11):
            prefix_masses,_ = apply_table(prefix,masses,masses,scale,True)
            updated,_ = apply_table(merge,prefix_masses,masses,scale,False)
            # Independent rational loop, with exact rational rounding at each stage.
            for table,left,right,sym in ((prefix,ref,ref,True),):
                _,den,ai,aj,of,ds,ns = table
                mid = [F(0)]*len(keys)
                for row in range(len(ai)):
                    mult = left[ai[row]]*right[aj[row]]*(2 if sym and ai[row]!=aj[row] else 1)
                    for k in range(of[row],of[row+1]):
                        mid[ds[k]] += mult*F(ns[k],den)
                mid,_ = round_up_mass(mid,vertex,40)
            out = [F(0)]*len(keys)
            for row in range(len(ii)):
                dest = reference_pair(N,lam,keys,ii[row],jj[row])
                for k,w in dest.items():
                    out[k] += mid[ii[row]]*ref[jj[row]]*w
            ref,_ = round_up_mass(out,vertex,40)
            assert ref == [F(v,scale) for v in updated]
            masses = updated
            finite.append(depth)
    result = {'status':'PASS','grid':N,'asymmetric_basis_rows_checked':len(rows),
              'all_rows':N<=12,'ten_stagewise_Fraction_iterations':finite,
              'normalization':'left edge 1, right edge eta; common denominator 108*B*N^2',
              'wall_seconds':time.monotonic()-started}
    ROOT.joinpath(f'ternary_bp_validation_N{N}.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps(result),flush=True)


def run(N, steps, bits, resume, chunk_seconds, do_validate, build_only):
    memory_check()
    assert N % 3 == 0 and N <= 96
    prefix = prefix_table(N,ETA)
    merge = asymmetric_table(N,ETA)
    size = sum(a.itemsize*len(a) for table in (prefix,merge) for a in table[2:])
    assert size < 550*1024**2
    print('Two tables bytes',size,flush=True)
    if do_validate:
        validate(N,ETA,prefix,merge)
    if build_only:
        return
    keys = prefix[0]
    assert merge[0] == keys
    vertex = keys.index((0,0,N)); scale = 1<<bits
    masses = [0]*len(keys); masses[vertex] = scale
    rows = []; first = 1
    path = ROOT/f'ternary_bp_int_N{N}.json'
    if resume and path.exists():
        old = json.loads(path.read_text(encoding='utf-8'))
        assert old['grid_denominator'] == N and old['mass_rounding_bits'] == bits and old['lambda'] == str(ETA)
        masses = [int(v) for v in old['final_integer_masses']]
        assert len(masses) == len(keys) and sum(masses) == scale
        rows = old['rows']; first = rows[-1]['depth']+1
    chi = [3*sum(v*v for v in key)-N*N for key in keys]
    started = time.monotonic()
    for depth in range(first,steps+1):
        middle, missing1 = apply_table(prefix,masses,masses,scale,True)
        masses, missing2 = apply_table(merge,middle,masses,scale,False)
        upper = F(sum(m*c for m,c in zip(masses,chi)),3*N*N*scale)
        rows.append({'depth':depth,'second_moment_upper':str(upper),
                     'prefix_mass_revealed':str(F(missing1,scale)),
                     'final_mass_revealed':str(F(missing2,scale))})
        stop = time.monotonic()-started >= chunk_seconds or upper < F(37,2000)
        if depth % 5 == 0 or depth == steps or stop:
            result = {'status':'exact finite-depth information-upgraded upper bound',
                      'q':3,'d':3,'lambda':str(ETA),'grid_denominator':N,
                      'mass_rounding_bits':bits,'packed_table_bytes':size,'rows':rows,
                      'final_integer_masses':list(map(str,masses)),'orbit_keys':keys,
                      'arithmetic':'arbitrary-precision integer products and division; discarded probability assigned to full revelation at both stages',
                      'wall_iteration_seconds':time.monotonic()-started}
            path.write_text(json.dumps(result,indent=2),encoding='utf-8')
            print('ternary N',N,'depth',depth,'upper',str(upper),'approx',float(upper),'seconds',round(time.monotonic()-started,1),flush=True)
        if stop:
            print('Chunk complete, entry radius reached' if upper < F(37,2000) else 'Chunk complete, checkpoint saved',flush=True)
            break


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--grid',type=int,default=6); p.add_argument('--steps',type=int,default=500)
    p.add_argument('--bits',type=int,default=40); p.add_argument('--resume',action='store_true')
    p.add_argument('--chunk-seconds',type=float,default=70); p.add_argument('--validate',action='store_true')
    p.add_argument('--build-only',action='store_true')
    a = p.parse_args()
    run(a.grid,a.steps,a.bits,a.resume,a.chunk_seconds,a.validate,a.build_only)
