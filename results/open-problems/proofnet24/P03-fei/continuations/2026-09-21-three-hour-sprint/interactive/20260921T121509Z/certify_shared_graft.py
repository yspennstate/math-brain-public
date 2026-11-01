"""Construct and rigorously score shared-core grafts improving the recovered seed.

The 162-bit function is defined compositionally; its sparse Fourier histogram
is derived exactly, without pretending to enumerate its truth table. A 19-bit
majority graft is separately enumerated to test the compression code.
"""
from __future__ import annotations
from collections import Counter
from fractions import Fraction as F
from pathlib import Path
import hashlib, json
import numpy as np
from cancellation_composition import fwht
from reconstruct_external_seed import core_and_hosts, make_table, check, EXPECTED_SHA
from rational_entropy_certificate import log2_interval, interval_json, decimal_out, entropy_from_squares


def core_data():
    base,hosts=core_and_hosts()
    a=np.array([-1 if (base>>x)&1 else 1 for x in range(512)],dtype=np.int64)
    owner={x:j for j,h in enumerate(hosts) for x in h}
    for h in hosts: a[h]=0
    pivots=[];P=[];Q=[]
    for lo,hi in hosts:
        assert lo.bit_count()==4 and hi.bit_count()==5 and (lo^hi).bit_count()==1
        pivots.append((lo^hi).bit_length()-1)
        p=np.zeros(512,dtype=np.int64);p[[lo,hi]]=1
        q=np.zeros(512,dtype=np.int64);q[lo]=1;q[hi]=-1
        P.append(fwht(p));Q.append(fwht(q))
    tested=0
    for x in range(512):
        for t in range(9):
            if x>>t&1: continue
            y=x|(1<<t); ox,oy=owner.get(x),owner.get(y);tested+=1
            if ox is not None and oy is not None:
                assert ox==oy and pivots[ox]==t
            elif ox is not None: assert a[y]==-1
            elif oy is not None: assert a[x]==1
            else: assert a[x]>=a[y]
    assert int(a.sum())==0
    return a,np.array(P),np.array(Q),hosts,pivots,tested


def compressed(table:np.ndarray, distinguished:int, selected:list[int]):
    a,P,Q,hosts,pivots,tested=core_data()
    ng=len(table);m=ng.bit_length()-1
    if m>22: raise ValueError('Explicit int64 compression is restricted to gadget dimensions <=22')
    if not np.all((table==1)|(table==-1)): raise ValueError('Gadget must be Boolean +/-1')
    assert 0<=distinguished<m and len(set(selected))==len(selected)
    assert all(0<=j<9 for j in selected)
    W=fwht(table); assert W[0]==0
    Ig=F(sum(u.bit_count()*int(v)**2 for u,v in enumerate(W)),ng*ng)
    bnum=int(W[1<<distinguished]);b=F(bnum,ng)
    # Source coefficients scaled by D=512*ng. All operations here are exact.
    D=512*ng
    core=fwht(a)*ng+bnum*np.sum(Q[selected],axis=0) if selected else fwht(a)*ng
    assert int(core[0])==0
    hist=Counter(int(v)**2 for v in core if v)
    k=len(selected)
    for u,v in enumerate(W):
        if not v or u in (0,1<<distinguished):continue
        hist[(2*int(v))**2]+=256*k
    if k<9:hist[(D//256)**2]+=256*(9-k)
    assert sum(s*c for s,c in hist.items())==D*D
    # Independent influence accumulation by exact spectral degrees.
    Icore=F(sum(u.bit_count()*int(v)**2 for u,v in enumerate(core)),D*D)
    Itail=F(k,256)*sum((F((u.bit_count()+4)*int(v)**2,ng*ng)
        for u,v in enumerate(W) if v and u not in (0,1<<distinguished)),F(0))
    I=Icore+Itail+F(5*(9-k),256)
    assert I==F(261,128)+F(k,256)*(Ig-1)
    return {'histogram':hist,'normalizer':D*D,'I':I,'Ig':Ig,'b':b,
      'core_numerators':core,'gadget_W':W,'gadget_n':m,
      'core_edges_checked':tested,'pivots':pivots,'selected':selected,
      'n':9+(9-k)+k*(m-1)}


def enclose_hist(hist,norm):
    lo=F(0);hi=F(0)
    for s,c in hist.items():
        a,b=log2_interval(F(norm,s));weight=F(s*c,norm)
        lo+=weight*a;hi+=weight*b
    return lo,hi


def small_regression():
    g=np.array([1 if x.bit_count()<2 else -1 for x in range(8)],dtype=np.int64)
    c=compressed(g,0,[0]);a,P,Q,hosts,pivots,tested=core_data()
    x=np.arange(1<<19,dtype=np.int64);core=x&511
    vals=a[core].copy()
    # Eight old auxiliary dictators occupy bits 9..16.
    for j in range(1,9):
        mask=np.isin(core,hosts[j]);vals[mask]=1-2*((x[mask]>>(8+j))&1)
    mask=np.isin(core,hosts[0]);pivot=pivots[0]
    gi=((x>>pivot)&1)|(((x>>17)&1)<<1)|(((x>>18)&1)<<2)
    vals[mask]=g[gi[mask]]
    assert np.all(np.abs(vals)==1) and int(vals.sum())==0
    W=fwht(vals);factor=(1<<19)//(512*8)
    assert np.all(W%factor==0)
    actual=Counter(int(v//factor)**2 for v in W if v)
    assert actual==c['histogram']
    I=F(sum(u.bit_count()*int(v)**2 for u,v in enumerate(W)),1<<38)
    assert I==c['I']
    return {'dimension':19,'truth_table_values_enumerated':1<<19,
      'exact_sparse_fourier_histogram_match':True,'I_exact':str(I),
      'truth_table_sha256':hashlib.sha256(','.join(map(str,vals)).encode()).hexdigest()}


def main():
    source,table=check()
    g=compressed(table,9,list(range(9)))
    lo,hi=enclose_hist(g['histogram'],g['normalizer'])
    oldlo,oldhi=entropy_from_squares(fwht(table)**2,len(table)**2)
    oldI=F(261,128); I=g['I']
    clo,chi=lo/(I-1),hi/(I-1)
    rlo,rhi=oldlo/(oldI-1),oldhi/(oldI-1)
    assert clo>rhi
    floor=F('6.521850083658')
    assert clo>floor
    # A finite amplification that already exceeds the old limiting record.
    depth=25
    finite_lo=clo*(1-I**(-depth));finite_hi=chi*(1-I**(-depth))
    assert finite_lo>rhi
    out={'status':'PROVED_CONSTRUCTION_WITH_RATIONAL_NUMERICAL_CERTIFICATE; NOT_FULL_FEI',
      'source_seed':'Numaro July 2026, independently recovered; no attribution transfer',
      'source_sha256':EXPECTED_SHA,'gadget_distinguished_input_zero_based':9,
      'selected_hosts':list(range(9)),'core_pivot_inputs_zero_based':g['pivots'],
      'function_definition':'On each of the nine core host edges use a fresh copy of the recovered balanced 18-bit seed, mapping its input 9 to that edge coordinate and its other 17 inputs to fresh variables; elsewhere use the fixed core value.',
      'dimension':g['n'],'balance':'exact by mean-zero core and balanced grafts',
      'monotonicity':'proved from free-edge inequalities and monotone source; 2304 core covering edges checked exactly',
      'I_exact':str(I),'I_source_exact':str(oldI),'distinguished_influence_exact':str(g['b']),
      'sparse_nonzero_coefficients':sum(g['histogram'].values()),
      'square_normalizer_exact':str(g['normalizer']),
      'histogram_parseval':'exact integer equality',
      'H':interval_json(lo,hi),'new_amplified_FEI_lower':interval_json(clo,chi),
      'old_amplified_FEI_lower':interval_json(rlo,rhi),
      'strict_improvement_lower':decimal_out(clo-rhi),
      'safe_strict_FEI_lower_bound':str(floor),
      'finite_amplification':{'depth':depth,'dimension_exact':str(g['n']**depth),
         'H_over_I':interval_json(finite_lo,finite_hi),'exceeds_old_limit':True},
      'compressed_spectrum_regression':small_regression(),
      'log_enclosure':'exact rational atanh series, 80 terms after dyadic reduction',
      'novelty_priority':'NOT_CLAIMED; improves the independently reproduced public baseline',
      'full_FEI_status':'OPEN'}
    root=Path(__file__).resolve().parent
    (root/'shared_graft_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
    hist={'normalizer':str(g['normalizer']), 'multiplicities':[[str(s),c] for s,c in sorted(g['histogram'].items())]}
    (root/'shared_graft_spectrum_histogram.json').write_text(json.dumps(hist,indent=2)+'\n')
    print(json.dumps(out,indent=2))

if __name__=='__main__':main()
