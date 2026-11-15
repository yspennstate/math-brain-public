#!/usr/bin/env python3
"""Render reports from saved measurements. No experiment is rerun."""
import json,math,os
from decimal import Decimal

def load(p):return json.load(open(p))
def table(headers,rows):
    return '\n'.join(['| '+' | '.join(headers)+' |','| '+' | '.join(['---']*len(headers))+' |']+['| '+' | '.join(map(str,r))+' |' for r in rows])
def run():
    raw=load('rows.json');audits=load('decimal_audit.json')+load('decimal_small.json')+load('decimal_large.json')
    key=lambda x:(x['w'],x['coordinate'],x['order'])
    gold={key(x):x for x in audits}
    assert len(gold)==len(raw)==64, (len(gold),len(raw))
    assert all(Decimal(x['min_step'])>=Decimal('-1e-55') for x in audits)
    rows=[]
    for x in raw:
        y=x.copy();y['ratio']=gold[key(x)]['decimal_ratio'];y['inf']=gold[key(x)]['decimal_inf'];rows.append(y)
    with open('rows_verified.json','w') as f:json.dump(rows,f,indent=2)
    checks=load('proof_checks.json');P={x['w']:x for x in checks['rows'] if x['w']>=10}
    mc=load('erasure.json');hill=load('hill.json');resources=load('resources.json');sv=load('sampler_validation.json')
    ws=sorted(P);coords=['root','mate','leaf'];kinds=['leaves_first','mates_first','clause','block','random']
    def val(w,c,k):return next(x['ratio'] for x in rows if key(x)==(w,c,k))
    best={(w,c):min((x for x in rows if x['w']==w and x['coordinate']==c),key=lambda x:x['ratio']) for w in ws for c in coords}
    maxdiff=max(abs(x['float_ratio_difference']) for x in audits)
    dimension=table(['w','D','n','D² L 2^-L','Inf root','Inf mate','Inf leaf'],[[w,P[w]['D'],P[w]['n'],f"{P[w]['lambda']:.6f}",f"{P[w]['root_inf']:.9g}",f"{P[w]['mate_inf']:.9g}",f"{P[w]['leaf_inf']:.9g}"] for w in ws])
    orders=table(['w','coordinate','leaves first','mates first','clause','block','random','private last'],[[w,c]+[f'{val(w,c,k):.6f}' for k in kinds]+([f'{val(w,c,"private_last"):.6f}'] if c=='leaf' else ['—']) for w in ws for c in coords])
    entrows=[]
    for w in ws:
        rr=next(x for x in mc if x['w']==w and x['coordinate']=='root');mm=next(x for x in mc if x['w']==w and x['coordinate']=='mate')
        lower=math.floor(P[w]['leaf_E_lower']*1e6)/1e6;upper=math.ceil(P[w]['leaf_witness_general_upper']*1e6)/1e6
        entrows.append([w,f"{rr['E_ratio']:.4f} ± {rr['E_se_ratio']:.4f}",f"{mm['E_ratio']:.4f} ± {mm['E_se_ratio']:.4f}",f'[{lower:.6f}, {upper:.6f}]'])
    entropy=table(['w','root E/Inf (MC ± SE)','mate E/Inf (MC ± SE)','leaf E/Inf (proven bounds)'],entrows)
    besttable=table(['w','D','best tested root','best tested mate','leaf private order'],[[w,P[w]['D'],f"{best[w,'root']['ratio']:.6f}",f"{best[w,'mate']['ratio']:.6f}",f'{val(w,"leaf","private_last"):.6f}'] for w in ws])
    pred=table(['w','c=P[no leaf in U | root in U]','(1-c) log2(1/Inf)','mates-first L/Inf','difference'],[[w,f"{P[w]['root_c']:.6f}",f"{P[w]['mates_first_leading_prediction']:.6f}",f'{val(w,"root","mates_first"):.6f}',f'{val(w,"root","mates_first")-P[w]["mates_first_leading_prediction"]:.6f}'] for w in ws])
    small=[];smalltypes=[]
    for n in sorted({x['n'] for x in hill}):
        hh=[x for x in hill if x['n']==n];win=min(hh,key=lambda x:x['hill_ratio']);exact=min((x['exact_min_ratio'] for x in hh),default=None) if n==13 else None
        small.append([n,f"{min(x['E_ratio'] for x in hh):.10f}",f"{win['hill_ratio']:.10f}",f'{exact:.10f}' if exact else 'not computed',win['type']])
        for c in coords:
            aa=[x for x in hh if x['type']==c]
            smalltypes.append([n,c,len(aa),f"{min(x['E_ratio'] for x in aa):.10f}",f"{min(x['hill_ratio'] for x in aa):.10f}",f"{min(x['exact_min_ratio'] for x in aa):.10f}" if n==13 else 'not computed'])
    smalltable=table(['n','min_i E/Inf','best hill min L/Inf','exact min L/Inf','winning type'],small)
    smalltypetable=table(['n','type','coordinates searched','E/Inf','best hill L/Inf','exact min L/Inf'],smalltypes)
    gap=max(x['hill_ratio']-x['exact_min_ratio'] for x in hill if x['n']==13)
    proof='''For integers D≥2 and L=w−1≥2 with D² L 2^-L≤2, choose a terminal leaf i. Reveal every variable outside its terminal clause first, then the other L−1 private leaves of that clause. With δ=Inf_i, this gives

    2(1−2^{−(L−1)}) ≤ E_i/δ ≤ L_i^π/δ
      ≤ 2 + 2^{−(L−1)}(2L−2+4 log2 e) < 6.

The chosen witness and the optimal leaf witness both tend to 2 as L grows in this regime. Therefore min_{i,π} L_i^π/Inf_i≤2+o(1) along the balanced family, even with D→∞. The tree model cannot give a positive-c log D lower bound for every coordinate and every order. Its terminal leaves have degree one. The proof does not extend to a D-regular hypergraph.'''
    results=f'''# FEIB20 results

Alternative (a) is proved on the balanced tree family. A leaf and an explicit order give a bounded nested witness. This does not solve the general FEI conjecture.

## Proven statement

{proof}

The full argument is in [PROOF.md](PROOF.md). It first proves a private-clause lemma, then derives the leaf influence exactly and bounds it below. The general resampling identities are in [MOMENTS.md](MOMENTS.md).

## Dimensions and influences

{dimension}

Source: `python3 proof_checks.py`, `proof_checks.json`. Influences are probabilities, and every witness/erasure ratio below is bits per unit influence. The brief's proposed second truth table w=4,D=2 has n=25, not n=22. The model's count is n=1+DL+D(D−1)L². We validated the actual 25-variable function and used n=13 and n=17 for searches restricted to n≤22.

## All requested orders

{orders}

Source: `python3 nested.py rows` and the Decimal audits, combined by `python3 build_report.py` into `rows_verified.json`. Values displayed to six decimal places. Every listed witness includes all variables and their actual last-element labels.

The orders are defined as follows, with the target i deleted from each full list. Except for random, the root is first when it is not the target. Mates and blocks use increasing indices.

- Leaves first: all leaves in mate/clause/leaf index order, then all mates.
- Mates first: all mates, then all leaves in that index order.
- Clause: each mate is immediately followed by its Q clauses, each clause's leaves consecutive.
- Block: each block's leaves, followed by that block's mates, then the next block.
- Random: NumPy permutation with seed 20261110, same full permutation for the three target types.
- Private last: the clause order with the target leaf's other L−1 private clause leaves moved to the end.

The existing `tree_dnf.py` mates-only witness merges all cells with no spectral mate into one cell. Our full-order leaves-first witness resolves their leaf labels, so it can be slightly smaller. The exact truth-table comparisons use the full statistic.

{besttable}

These are best among the tested orders, not all-order minima. Root winners use clause order and mate winners use the one seeded random order. The proof bounds the all-order optimum by the explicit leaf construction.

## Erasure entropy

{entropy}

Source: `python3 erasure.py`, `erasure.json`; leaf bounds use the proved private-clause inequality and exact influences in `proof_checks.json`. The leaf bounds are rounded outward. Root and mate entries are importance-sampling estimates, with one standard error, 400000 samples per entry and seed 20261110. They are measurements, not proofs of a root/mate limit. The derivative normalization and total spectral mass checks are saved with every estimate.

The mate sampler sums six separable tensor terms plus the constant atom. It collapses nonempty Q Fourier supports into their normalized centered-Q factor; homogeneity of Phi makes this collapse exact. It is checked against exact mate E/Inf at w=3,D=2 and w=4,D=2 (`erasure.json`, `sampler_validation.json`). The latter discrepancy is {sv['difference_in_standard_errors']:.3f} standard errors.

## Mates-first prediction

{pred}

Source: `proof_checks.json`, `rows_verified.json`. Here c is computed exactly from root resampling moments after resampling every leaf. The difference remains about 2.5 bits per unit influence in these rows. This is compatible with the proposed leading logarithmic term plus a bounded additive term, but four finite rows do not prove that asymptotic statement. The leading term alone substantially underestimates the observed witness.

## Small-instance search

{smalltable}

{smalltypetable}

Source: `python3 hill.py`, `hill.json`. Every coordinate was searched. Each hill run uses six preset starts (including one seeded random order) and ten additional random starts, exhaustive pair swaps per sweep, at most twenty sweeps per start, with fixed seed 20261110. The objective is evaluated from exact-spectrum subset zeta sums. At n=13 a separate shortest-path dynamic program checks every order implicitly for every coordinate. Hill climbing reaches the global exact minimum, but can miss a particular coordinate's optimum: the largest gap is {gap:.12g}. At n=17 the hill result is only an upper bound; the true global minimum lies between the displayed min E and best hill values.

## Checks and resources

`tree_dnf.py selftest` passed (`baseline_selftest.txt`). `python3 nested.py validate` compared arbitrary-mask correlations and all six full orders for root/mate/leaf representatives with exact truth tables at n=13 and n=25 (`validation.jsonl`). Maximum correlation errors were zero at the printed precision; maximum witness ratio errors were 3.11e−15 and 8.88e−16 respectively.

All {len(rows)} large-row witnesses were reevaluated using 70-digit Decimal moments, with ordinary double precision only for the final stable Phi logarithms and summation. Sources: `decimal_audit.json`, `decimal_small.json`, `decimal_large.json`. Every resampling cell difference was nonnegative to a tolerance of 1e−55. The largest change from the first floating run was {maxdiff:.9g} bits per unit influence. The largest leaf private-order value changed from {next(x['ratio'] for x in raw if key(x)==(16,'leaf','private_last')):.12f} to {val(16,'leaf','private_last'):.12f}. The proof is independent of these numerical differences. `proof_checks.json` independently compares the conditioning formulas for all three influences against Decimal correlation differences, agreeing within 1.8e−69.

`resources.json` records inherited nice {resources['inherited_nice']}. The sandbox refused the redundant nice wrapper's setpriority call; direct priority inspection confirms the requested inherited value. Commands set one BLAS/OMP thread and used at most two compute processes concurrently. The n=25 independent sampler validation measured {sv['maxrss_bytes']} bytes ({sv['maxrss_bytes']/1024**3:.3f} GiB) peak RSS. No truth tables or large arrays were saved. The folder-byte count at the resource check was {resources['folder_bytes_at_check']} bytes, far below 200 MB; final size is recorded in `final_audit.json`.

Brain recall supplied orientation and older FEI pointers; the mathematical result came from FLOW, the supplied code, and the derivations here. No external files, mesh messages, memory entries, or fleet board entries were written, as required by RULES.md.

## Still open

The general FEI conjecture and universality of the window-one witness remain open here. We have not found exact all-order root/mate minima at large size, proved a logarithmic bound on regular hypergraphs, or proved a uniform witness bound for every unbalanced choice of D,w. The proved regime is D² L 2^-L≤2, which covers the requested balanced rows. There is no remaining blocker to the assigned alternative (a).

Task: “solve the Fourier Entropy-Influence conjecture” — the author's 9 Nov 22:20 ask; FEIB20 nested-witness brief.
'''
    open('RESULTS.md','w').write(results)
    report=f'''# FEIB20 report

The balanced tree family has a bounded nested witness. Its degree-one terminal leaves prevent the proposed all-coordinate logarithmic lower bound.

{proof}

[PROOF.md](PROOF.md) gives the private-clause Fourier argument and exact influence formula. [MOMENTS.md](MOMENTS.md) extends the block resampling moments to arbitrary interleavings, for root, mate, and leaf targets.

{besttable}

Ratios are bits per unit influence. Source: `rows_verified.json`, generated by `python3 nested.py rows`, the Decimal audits, and `python3 build_report.py`. Root and mate columns are best tested orders; they are not certified all-order minima. The leaf column is the explicit order from the proof.

{entropy}

Source: `erasure.json` from `python3 erasure.py` and proven leaf bounds evaluated in `proof_checks.json`. The Monte Carlo errors are one standard error from 400000 samples per entry. The leaf interval is a bound, not a point estimate.

{smalltable}

Source: `hill.json` from `python3 hill.py`. All coordinates were hill-climbed. The n=13 minimum is independently certified by dynamic programming over all orders. The n=17 hill result is an upper bound only. The requested w=4,D=2 truth table actually has n=25, not n=22; we validated it and used the n=17 case for the second order search within n≤22.

The supplied selftest passed. Exact truth tables check all coordinate types and arbitrary interleaving moments at n=13 and n=25. All {len(rows)} balanced-row witnesses were checked with 70-digit Decimal moments. The floating implementation's largest correction was {maxdiff:.9g} bits per unit influence; tables use the Decimal values. The exact influence formulas were also checked by resampling correlations. The mate entropy sampler agrees with two exact truth tables within two standard errors.

The mates-first root measurements are consistent with the proposed (1−c)log2(1/Inf) term plus an additive term near 2.5 in these rows; this asymptotic interpretation remains heuristic. [RESULTS.md](RESULTS.md) contains every requested order, influences, checks, commands, and limitations.

Computations inherited nice {resources['inherited_nice']}, used one thread per process and at most two compute processes. The largest directly measured validation peak was {sv['maxrss_bytes']/1024**3:.3f} GiB. The folder remains below its 200 MB limit (`final_audit.json`). Brain recall helped with orientation, not the new proof. All writes stayed in this folder.

This completes alternative (a) for the balanced family. General FEI, general FWC, regular-hypergraph lower bounds, exact large root/mate minima, and arbitrary unbalanced regimes remain unresolved.

Task: “solve the Fourier Entropy-Influence conjecture” — the author's 9 Nov 22:20 ask; FEIB20 nested-witness brief.
'''
    open('REPORT.md','w').write(report)
    print(json.dumps({'witness_rows':len(rows),'audited_rows':len(audits),'max_float_correction':maxdiff,'hill_coordinates':len(hill),'reports':['RESULTS.md','REPORT.md']}))
if __name__=='__main__':run()
