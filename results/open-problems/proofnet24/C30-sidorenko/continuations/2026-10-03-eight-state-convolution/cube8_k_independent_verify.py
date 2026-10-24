"""Exact independent coverage and flow generation; compare complete polynomials.

The graph route is C10 plus five diameters, with a fundamental-cycle basis.
The author's primary generator uses a different bipartite labeling and tests
all 2^15 subsets for even degree.  This script never invokes that generator.
Run 'generate' first, then the independent C++ reconstructor, then 'compare'.
"""
from collections import Counter
from itertools import permutations
from pathlib import Path
import hashlib
import json
import sys

D=Path(__file__).parent
PFX='continuation_20261002_cube8_'

def coverage():
    # Derive the affine permutation group from its ternary preservation law,
    # without separately enumerating binary matrices.
    affine=[a for a in permutations(range(8))
            if all(a[x^y]==(a[x]^a[y]^a[0]) for x in range(8) for y in range(8))]
    assert len(affine)==1344
    counts=Counter();bad=set()
    for rho in permutations(range(8)):
        good=0
        for a in range(1,8):
            # Numeric minimum selects a highest-pivot transversal, unlike
            # the author's lowest-pivot transversal.
            parity=sum(rho[x]<rho[x^a] for x in range(8) if x<(x^a))%2
            good+=parity==0
        counts[good]+=1
        if good==0:bad.add(rho)
    representative=(0,1,2,7,3,6,5,4)
    orbit={tuple(representative[a[x]] for x in range(8)) for a in affine}
    assert orbit==bad and len(bad)==1344
    assert [counts[i] for i in range(8)]==[1344,4032,6720,8064,8064,6720,4032,1344]
    return {'status':'PASS','strict_orders':40320,'affine_maps':len(affine),
            'bad_orders':len(bad),'good_direction_distribution':[counts[i] for i in range(8)],
            'bad_order_set_sha256':hashlib.sha256(repr(sorted(bad)).encode()).hexdigest()}

def flows():
    # C10 edges first, then its five diameters. The first nine cycle edges
    # form a spanning tree. Every remaining edge closes a fundamental cycle.
    edges=[(i,(i+1)%10) for i in range(10)]+[(i,i+5) for i in range(5)]
    basis=[]
    for j in range(9,15):
        u,v=edges[j]
        basis.append((1<<j) | sum(1<<k for k in range(min(u,v),max(u,v))))
    cycles=[]
    for mask in range(64):
        z=0
        for j in range(6):
            if mask>>j&1:z^=basis[j]
        cycles.append(z)
    assert len(set(cycles))==64
    assert all(all(sum((z>>j)&1 for j,(u,v) in enumerate(edges) if x in (u,v))%2==0
                       for x in range(10)) for z in cycles)
    # Explicit source graph isomorphism: left i -> 4i mod10,
    # right j -> (4j+5) mod10.
    expected={frozenset((4*i%10,(4*j+5)%10)) for i in range(5) for j in range(5)
              if (j-i)%5 in (0,1,4)}
    assert expected=={frozenset(e) for e in edges}
    out=Counter()
    for a in cycles:
        for b in cycles:
            for c in cycles:
                n=[0]*8
                for i in range(15):n[((a>>i)&1)+2*((b>>i)&1)+4*((c>>i)&1)]+=1
                out[tuple(n)]+=1
    assert len(out)==3964 and sum(out.values())==262144
    return edges,basis,out

def jsonpoly(path,field):
    obj=json.loads(path.read_text())
    return {tuple(map(int,k.split(','))):int(v) for k,v in obj[field].items()}

def tsvpoly(path,bits=None):
    out={}
    for line in path.read_text().splitlines():
        k,c=line.split('\t')
        if bits is None:n=tuple(map(int,k.split(',')))
        else:n=tuple((int(k)>>(bits*i))&((1<<bits)-1) for i in range(8))
        assert n not in out
        out[n]=int(c)
    return out

def generate():
    cov=coverage();(D/'cube8_k_independent_coverage.json').write_text(json.dumps(cov,indent=2)+'\n')
    edges,basis,poly=flows()
    original=jsonpoly(D/(PFX+'flow_and_smoothing.json'),'Fourier_polynomial')
    walsh=tsvpoly(D/(PFX+'walsh_audit.tsv'),4)
    assert poly==original==walsh
    (D/'cube8_k_independent_flow.tsv').write_text(''.join(','.join(map(str,n))+'\t'+str(c)+'\n'
                                                       for n,c in sorted(poly.items())))
    out={'status':'PASS','graph_edges':edges,'fundamental_cycle_masks':basis,
         'binary_cycles':64,'character_flows':262144,'Fourier_terms':len(poly),
         'entire_Fourier_polynomial_equals_both_author_routes':True,
         'flow_tsv_sha256':hashlib.sha256((D/'cube8_k_independent_flow.tsv').read_bytes()).hexdigest()}
    (D/'cube8_k_independent_flow_checks.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))

def compare():
    density=tsvpoly(D/'cube8_k_independent_density.tsv')
    author={n:c*8**6 for n,c in tsvpoly(D/(PFX+'vertex_polynomial.tsv'),4).items()}
    assert density==author
    assert sum(density.values())==8**15 and all(sum(n)==15 and c>0 for n,c in density.items())
    raw=tsvpoly(D/'cube8_k_independent_raw_gap.tsv')
    raw_author=jsonpoly(D/(PFX+'last_chamber.json'),'gap_coefficients')
    assert raw==raw_author
    certificate=tsvpoly(D/'cube8_k_independent_multiplier.tsv')
    certificate_author=jsonpoly(D/(PFX+'last_chamber_polya.json'),'certificate_coefficients')
    cpp_author=tsvpoly(D/(PFX+'polya_cpp_audit.tsv'),6)
    assert certificate==certificate_author==cpp_author
    assert len(certificate)==345312 and all(sum(n)==17 and c>0 for n,c in certificate.items())
    pure=[certificate[tuple(17 if j==i else 0 for j in range(8))] for i in range(7)]
    assert pure==[262143,134184960,1134628245,3221225472,60175070835,118091317248,72749439945]
    out={'status':'PASS','normalized_density_terms':len(density),'normalized_density_coefficient_sum':sum(density.values()),
         'density_whole_map_equal':True,'raw_gap_terms':len(raw),'raw_gap_negatives':sum(c<0 for c in raw.values()),
         'raw_gap_whole_map_equal':True,'multiplier_terms':len(certificate),'multiplier_whole_map_equal':True,
         'minimum_multiplier_coefficient':min(certificate.values()),'maximum_multiplier_coefficient':max(certificate.values()),
         'pure_coefficients':pure,'route':'fundamental cycles -> Fourier flows -> inverse Walsh -> chamber -> direct L^2'}
    (D/'cube8_k_independent_polynomial_checks.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))

if __name__=='__main__':
    if sys.argv[1]=='generate':generate()
    elif sys.argv[1]=='compare':compare()
    else:raise ValueError('expected generate or compare')
