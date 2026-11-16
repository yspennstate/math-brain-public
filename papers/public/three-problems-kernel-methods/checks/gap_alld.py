import json,glob,os,statistics as st,math
from collections import defaultdict
import numpy as np
R = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "records")
agg=defaultdict(list)
for f in glob.glob(os.path.join(R,"p9g_*.json")):
    d=json.load(open(f,encoding="utf-8"))
    for r in d["records"]: agg[(r["d"],r["h"],r["k"])].append(r)
tot_blocks=tot_inv=tot_pairs=0; iso_mono=iso_blocks=0
for (dd,hh,k) in sorted(agg):
    by=defaultdict(list); iso=defaultdict(list); ns=defaultdict(set)
    for r in agg[(dd,hh,k)]:
        by[round(r["delta"],2)].append(r["risk_noise"]); iso[round(r["delta"],2)].append(r["tail_isotropy"]); ns[round(r["delta"],2)].add(r["n"])
    ds=sorted(by)
    if len(ds)<3: 
        print(f"d={dd} k={k} only {len(ds)} deltas {ds}"); continue
    risks=[st.mean(by[x]) for x in ds]; isos=[st.mean(iso[x]) for x in ds]
    inv=sum(1 for i in range(len(risks)) for j in range(i+1,len(risks)) if risks[i]<risks[j]); pairs=len(risks)*(len(risks)-1)//2
    tot_blocks+=1; tot_inv+=inv; tot_pairs+=pairs
    mono_i=all(isos[i]>isos[i+1] for i in range(len(isos)-1)); iso_blocks+=1; iso_mono+=mono_i
    print(f"d={dd} k={k} N_k={agg[(dd,hh,k)][0]['N_k']:.0f} deltas={ds} n={[sorted(ns[x])[0] for x in ds]} designs/cell={[len(by[x]) for x in ds]} risk={[round(x,3) for x in risks]} inv={inv}/{pairs} iso={[round(x,2) for x in isos]} iso_mono={mono_i}")
print("TOTAL blocks",tot_blocks,"inverted pairs",tot_inv,"of",tot_pairs,"; isotropy strictly monotone in",iso_mono,"of",iso_blocks)
# GOE null formula check: d*E Tr(U^4) = d(2d^3+5d^2+5d)/(4p(p+2)), p=d(d+1)/2
rng=np.random.default_rng(1)
for d in (4,6,10):
    N=200000; G=rng.standard_normal((N,d,d)); G=(G+np.swapaxes(G,1,2))/np.sqrt(2)
    fro2=np.einsum('bij,bij->b',G,G); G2=np.einsum('bij,bjk->bik',G,G); tr4=np.einsum('bij,bij->b',G2,G2)
    p=d*(d+1)/2; exact=d*(2*d**3+5*d**2+5*d)/(4*p*(p+2))
    print(f"GOE null d={d}: MC {np.mean(d*tr4/fro2**2):.5f} +- {np.std(d*tr4/fro2**2,ddof=1)/np.sqrt(N):.5f}  formula {exact:.5f}   E Tr G^4 MC {np.mean(tr4):.2f} vs 2d^3+5d^2+5d={2*d**3+5*d**2+5*d}")
