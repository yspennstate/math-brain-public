"""Bounded independent checks of a pinned QFORM report. No network or remote jobs.
These are finite diagnostics, not verification of the full conjecture.
"""
from itertools import combinations
from pathlib import Path
import json
import math
import numpy as np


def esym(values, k):
    c = np.zeros(k + 1); c[0] = 1.0
    for x in values:
        for j in range(k, 0, -1):
            c[j] += x * c[j-1]
    return float(c[k])


def volume_data(M):
    U, s, Vt = np.linalg.svd(M, full_matrices=False)
    lam = s*s; Z = esym(lam, 3)
    if not Z > 0:
        raise ValueError('Rank-three volume must be positive')
    p = np.array([lam[i]*esym(np.delete(lam, i), 2)/Z for i in range(len(lam))])
    return Z, (U*U)@p, (Vt.T*Vt.T)@p


def cf_intervals(t, starts, width):
    """Equal mixture of uniform intervals; caller must verify non-overlap."""
    t = np.asarray(t, dtype=float)
    return np.sinc(t*width/(2*np.pi))*np.exp(1j*t[...,None]*(np.asarray(starts)+width/2)).mean(axis=-1)


def main():
    out = {'scope':'Finite checks only; no universal proof certificate', 'status':'PASS'}
    rng = np.random.default_rng(3)
    worst = 0.; gaussian_min_ratio = float('inf')
    for _ in range(12):
        M = rng.normal(size=(5,6)); Z, a, b = volume_data(M)
        direct = 0.; aa=np.zeros(5); bb=np.zeros(6)
        for S in combinations(range(5),3):
            for T in combinations(range(6),3):
                w=np.linalg.det(M[np.ix_(S,T)])**2
                direct+=w; aa[list(S)]+=w; bb[list(T)]+=w
        err=max(abs(Z-direct)/Z, np.max(abs(a-aa/direct)), np.max(abs(b-bb/direct)))
        worst=max(worst,float(err)); assert err<1e-10
        for _ in range(8):
            d=np.exp(rng.uniform(-3,3,5)); e=np.exp(rng.uniform(-3,3,6))
            _, logdet=np.linalg.slogdet(np.diag(e)+M.T@np.diag(d)@M)
            loglower=math.log(Z)+float(a@np.log(d)+(1-b)@np.log(e))
            ratio=math.exp(logdet-loglower); gaussian_min_ratio=min(gaussian_min_ratio,ratio)
            assert logdet>=loglower-1e-10
    out['volume_sampling']={'matrices':12,'maximum_relative_or_marginal_error':worst,
        'gaussian_parameter_checks':96,'minimum_determinant_over_AMGM_lower_bound':gaussian_min_ratio}
    # Reproduce only the input-generation portion of check_fresnel_bl.py (seed 7).
    rng=np.random.default_rng(7); first=[]
    for N in [1,10,40]:
        starts=np.sort(rng.uniform(0,30*N,N)); width=1/N
        first.append({'N':N,'overlapping_adjacent_pairs':int(np.sum(np.diff(starts)<width))})
    R,_=np.linalg.qr(rng.standard_normal((40,3))); rng.uniform(-5,5,40)
    starts=np.sort(rng.uniform(0,20,(40,10)),axis=1); width=.1
    bad=np.sum(np.diff(starts,axis=1)<width,axis=1)
    out['original_seed7_interval_inputs']={'first_part':first,'second_part_bad_coordinate_count':int(np.sum(bad>0)),
        'second_part_overlapping_adjacent_pairs':int(bad.sum()), 'second_part_max_leverage':float(np.sum(R*R,axis=1).max()),
        'finding':'Overlapping intervals make the nominal density-one test violate the input cap.'}
    N=8
    out['original_claim_test_zero_frequency']={'N':N,'original_formula_at_zero':N,'required_value':1,
        'finding':'The branch base=1 at tau=0 is multiplied by a sum of N phases.'}
    # Certified-by-construction disjoint supports and stable characteristic function.
    safe=np.sort(rng.uniform(0,20,(40,10)),axis=1)+np.arange(10)*.1
    assert np.all(np.diff(safe,axis=1)>=.1-1e-14)
    assert np.allclose(cf_intervals(np.array([0.,1e-16]),safe[0],.1),1)
    out['replacement_input_checks']={'disjoint_supports':True,'unit_mass':True,'density_cap_one':True,'cf_at_zero':1}
    # Preserving cross singular values does not preserve the volume-leverage gate.
    M=np.repeat(np.eye(3),2,axis=0)/np.sqrt(2)
    Z,a,b=volume_data(M); assert np.allclose(a,.5)
    eps=.01; pert=M.copy(); pert[0]*=1+eps
    Z1,a1,b1=volume_data(pert)
    exact=(1+eps)**2/(1+(1+eps)**2)
    assert abs(a1[0]-exact)<1e-12 and a1[0]>.5
    assert np.linalg.svd(pert,compute_uv=False)[-1]>=1-1e-12
    out['leverage_perturbation']={'epsilon':eps,'initial_max_alpha':float(a.max()),
        'perturbed_max_alpha':float(a1.max()),'exact_first_alpha':exact,
        'third_singular_value':float(np.linalg.svd(pert,compute_uv=False)[-1]),
        'finding':'Theorem D requires the alpha gate to be checked after perturbation.'}
    out['density_prefactors']={'claude_D':6*math.sqrt(math.e),'sharp_HY_refinement':3*math.e,
        'relative_reduction':1-(3*math.e)/(6*math.sqrt(math.e))}
    out['full_conjecture_verified']=False
    text=json.dumps(out,indent=2)+'\n'; Path(__file__).with_name('check_results.json').write_text(text)
    print(text)


if __name__=='__main__':
    main()
