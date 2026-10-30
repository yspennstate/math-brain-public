#!/usr/bin/env python3
"""
Exact finite verifier for B16's balanced 9-variable direct-restriction theorem.

Source: the exact 18-variable balanced monotone seed already reconstructed in
the FEI archive.  The checker:
  * reconstructs the source and verifies its SHA-256;
  * enumerates every restriction leaving exactly 9 of the 18 variables free;
  * uses an exact balance identity to retain exactly the balanced restrictions;
  * applies integer Walsh transforms to every balanced restriction;
  * certifies H/(I-1) < 6.365 for every non-dictator by an integer logarithm
    lower bound, with no floating-point sign decision.

NumPy is used only for exact int64 array arithmetic. All transformed integers
are at most 512, and all accumulated int64 quantities stay far below 2^63.
"""
import hashlib, itertools, json, time
import numpy as np

EXPECTED_SHA = "f8a7bb2c738d86368305111633376b1a3a83d8ee1f1abcc9a37d841b0f9c7839"
TOP = "fefefeeefefafc00feaafeaafeaafc00fefeccccfefacc00eeaacc00eeaacc00"
BOT = "fefefeeef0f0f000faaafaaaf000f000fcfcccccf0f000000000000000000000"
SLICES = [
 (TOP, BOT),
 (TOP, "fefefeeef0f0f000faaafaaaf000f000fcfcccccf0f0c0000000000000000000"),
 (TOP, "fefefeeef0f0f000faaafaaaf000f000fefeccccf0f000000000000000000000"),
 ("fefefefefefafc00feaafeaafeaafc00fefeccccfefacc00eeaacc00eeaacc00", "fefefefef0f0f000faaafaaaf000f000fcfcccccf0f000000000000000000000"),
 (TOP, "fefefeeef0f0f000feaafeaaf000f000fcfcccccf0f000000000000000000000"),
 (TOP, "fefefeeef0f0f000faaafaaaf0a0f000fcfcccccf0f000000000000000000000"),
 ("fefefeeefefefc00feaafeaafeaafc00fefeccccfefecc00eeaacc00eeaacc00", BOT),
 ("fefefeeefefafc00feaafeaafeaafc00fefeccccfefacc00feaacc00feaacc00", BOT),
 ("fefefeeefefafc00feaafeaafeaafc00fefeccccfefacc00eeaacc88eeaacc00", BOT),
 ("fefefeeefefafe00feaafeaafeaafe00fefeccccfefacc00eeaacc00eeaacc00", BOT),
]
N = 512
N2 = N*N
Q = 1 << 16
TH_NUM, TH_DEN = 1273, 200  # 6.365 exactly
EXPECTED_COUNTS = {0:18, 1:8226, 2:150912, 3:588672, 4:703584,
                   5:270144, 6:133056, 7:0, 8:0, 9:0}
EXPECTED_NOND = {0:0,1:0,2:0,3:0,4:90720,5:124992,6:133056,7:0,8:0,9:0}
EXPECTED_MIN_MARGIN = {4:38503710720, 5:38503710720, 6:2301034496}

def reconstruct():
    base = int("".join(SLICES[0]), 16)
    masks = [int("".join(row),16)^base for row in SLICES[1:]]
    assert all((m & base)==0 and m.bit_count()==2 for m in masks)
    seen=base; hosts=[]
    for m in masks:
        assert not (seen & m); seen |= m
        hosts.append([x for x in range(512) if (m>>x)&1])
    core=[-1 if (base>>x)&1 else 1 for x in range(512)]
    table=[]
    for y in range(512):
        row=core.copy()
        for j,cells in enumerate(hosts):
            if (y>>j)&1:
                for x in cells: row[x]=-1
        table.extend(row)
    digest=hashlib.sha256(",".join(map(str,table)).encode()).hexdigest()
    assert digest==EXPECTED_SHA and sum(table)==0
    return (np.asarray(table,dtype=np.int8).reshape(512,512),
            np.asarray([1 if v==-1 else 0 for v in core],dtype=np.int8), hosts, digest)

def indices_from_free(free, fixed_assign):
    free=tuple(free); fixed=[j for j in range(9) if j not in free]
    base=sum(((fixed_assign>>t)&1)<<j for t,j in enumerate(fixed))
    arr=np.zeros(1<<len(free),dtype=np.int64)
    for z in range(1<<len(free)):
        idx=base
        for t,j in enumerate(free): idx |= ((z>>t)&1)<<j
        arr[z]=idx
    return arr

def fwht_batch(A):
    A=A.copy(); h=1
    while h<A.shape[1]:
        A=A.reshape(A.shape[0],-1,2*h)
        x=A[:,:,:h].copy(); y=A[:,:,h:].copy()
        A[:,:,:h]=x+y; A[:,:,h:]=x-y
        A=A.reshape(A.shape[0],-1); h*=2
    return A

def fixed_bits_assignments(weights,target):
    for bits in range(1<<len(weights)):
        if sum(weights[t] for t in range(len(weights)) if (bits>>t)&1)==target:
            yield bits

def exact_floor_log_table():
    out=np.zeros(N+1,dtype=np.int64)
    for a in range(1,N+1):
        out[a]=pow(a,Q).bit_length()-1  # exactly floor(Q log_2 a)
    return out

def scan_r(r,T,base_neg,hosts,floor_log,batchsize=2048):
    a=9-r; sizes=np.asarray([s.bit_count() for s in range(N)],dtype=np.int64)
    xcache={}; ycache={}; total=nond=failures=0
    min_margin=min_meta=min_I_num=min_Hup_num=None
    batch=[]; metas=[]
    def gate(fc,fx,fa,fy):
        k=(tuple(fc),fx); k2=(tuple(fa),fy)
        if k not in xcache: xcache[k]=indices_from_free(fc,fx)
        if k2 not in ycache: ycache[k2]=indices_from_free(fa,fy)
        return T[np.ix_(ycache[k2],xcache[k])].reshape(-1)
    def process():
        nonlocal batch,metas,nond,failures,min_margin,min_meta,min_I_num,min_Hup_num
        if not batch: return
        W=fwht_batch(np.stack(batch).astype(np.int64)); w2=W*W
        assert np.all(w2.sum(axis=1)==N2)
        Lsum=w2@sizes
        Slo=(w2*(2*floor_log[np.abs(W)])).sum(axis=1,dtype=np.int64)
        Hup_num=18*N2*Q-Slo; Dnum=Lsum-N2
        mask=Dnum>0; nond += int(mask.sum())
        margins=TH_NUM*Q*Dnum-TH_DEN*Hup_num
        failures += int((mask & (margins<0)).sum())
        idx=np.where(mask)[0]
        if idx.size:
            j=int(idx[np.argmin(margins[idx])]); m=int(margins[j])
            if min_margin is None or m<min_margin:
                min_margin=m; min_meta=metas[j]
                min_I_num=int(Lsum[j]); min_Hup_num=int(Hup_num[j])
        batch=[]; metas=[]
    for fc in itertools.combinations(range(9),r):
        fixed_core=[j for j in range(9) if j not in fc]
        for fx in range(1<<len(fixed_core)):
            X=set(map(int,indices_from_free(fc,fx)))
            b=sum(int(base_neg[x]) for x in X)
            h=[sum(1 for x in hosts[j] if x in X) for j in range(9)]
            for fa in itertools.combinations(range(9),a):
                # Exact balance identity:
                # 2b + sum_{j free} h_j + 2 sum_{j fixed-to-1} h_j = 2^r.
                rem=(1<<r)-2*b-sum(h[j] for j in fa)
                if rem<0 or rem&1: continue
                fixed_aux=[j for j in range(9) if j not in fa]
                weights=[h[j] for j in fixed_aux]
                for fy in fixed_bits_assignments(weights,rem//2):
                    g=gate(fc,fx,fa,fy); assert int(g.sum())==0
                    batch.append(g); metas.append((tuple(fc),fx,tuple(fa),fy)); total+=1
                    if len(batch)>=batchsize: process()
    process()
    assert total==EXPECTED_COUNTS[r] and nond==EXPECTED_NOND[r] and failures==0
    if r in EXPECTED_MIN_MARGIN: assert min_margin==EXPECTED_MIN_MARGIN[r]
    else: assert min_margin is None
    row={"r":r,"balanced":total,"nondictator":nond,"failures":failures,
         "minimum_integer_margin":min_margin}
    if min_margin is not None:
        row.update({"closest_meta":repr(min_meta),"closest_I":min_I_num/N2,
                    "closest_H_rigorous_upper":min_Hup_num/(N2*Q),
                    "closest_ratio_rigorous_upper":
                    (min_Hup_num/(N2*Q))/((min_I_num-N2)/N2)})
    return row

def main():
    T,base_neg,hosts,digest=reconstruct(); floor_log=exact_floor_log_table(); t0=time.time()
    rows=[]
    for r in range(9,-1,-1):
        row=scan_r(r,T,base_neg,hosts,floor_log); rows.append(row)
        print(json.dumps(row,sort_keys=True),flush=True)
    total=sum(x["balanced"] for x in rows); nond=sum(x["nondictator"] for x in rows)
    assert total==1_854_612 and nond==348_768
    print(json.dumps({"status":"PASS","source_sha256":digest,
      "balanced_9_variable_restrictions":total,
      "nondictator_balanced_restrictions":nond,
      "rigorous_ratio_bound":"H/(I-1) < 6.365 for every nondictator",
      "threshold_exact":"1273/200","log_floor_Q":Q,
      "elapsed_seconds":time.time()-t0,"rows":rows},indent=2,sort_keys=True))

if __name__=="__main__": main()
