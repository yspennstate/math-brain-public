"""Monte-Carlo census for larger n of the two Vu events, and attribution to the
   'two disjoint support-2 eigenvectors' structure.

   A support-2 eigenvector of a symmetric M is e_i - e_j (needs M[m,i]=M[m,j] for
   m not in {i,j} and M[i,i]=M[j,j]; eigenvalue M[i,i]-M[i,j]) or e_i + e_j (needs
   M[m,i]=-M[m,j] and M[i,i]=M[j,j]; eigenvalue M[i,i]+M[i,j]).
"""
import numpy as np, itertools, sys, time, json
import census as CN
rng = np.random.default_rng(31337)

def support2_eigvecs(M, n):
    """return list of (i,j,sign,eigenvalue) for support-2 eigenvectors."""
    out=[]
    for i in range(n):
        for j in range(i+1,n):
            if M[i,i]!=M[j,j]: continue
            others=[m for m in range(n) if m!=i and m!=j]
            if all(M[m,i]==M[m,j] for m in others):
                out.append((i,j,-1, M[i,i]-M[i,j]))      # e_i - e_j
            if all(M[m,i]==-M[m,j] for m in others):
                out.append((i,j,+1, M[i,i]+M[i,j]))      # e_i + e_j
    return out

def template_hit(M, n, want):
    """want='zero'  -> two disjoint support-2 eigenvectors with eigenvalues summing to 0
       want='equal' -> ... with EQUAL eigenvalues"""
    V = support2_eigvecs(M, n)
    for a in range(len(V)):
        for b in range(a+1, len(V)):
            i,j,_,l1 = V[a]; k,l,_,l2 = V[b]
            if len({i,j,k,l})<4: continue
            if want=='zero' and l1+l2==0: return True
            if want=='equal' and l1==l2: return True
    return False

def run_mc(n, trials, chunk=200000, thr=1e-7):
    c = dict(PAIR0=0,PAIRNZ=0,REP=0,REPNZ=0,CORANK2=0,
             PAIR0_tmpl=0,REP_tmpl=0,PAIRNZ_tmpl=0,REPNZ_tmpl=0)
    done=0; minmargin=np.inf
    iu = np.triu_indices(n,1)
    while done < trials:
        m = min(chunk, trials-done); done += m
        U = rng.integers(0,2,size=(m, n*(n+1)//2)).astype(np.int8)*2-1
        Ms = np.zeros((m,n,n))
        t=0
        for i in range(n):
            for j in range(i,n):
                Ms[:,i,j]=U[:,t]; Ms[:,j,i]=U[:,t]; t+=1
        ev = np.linalg.eigvalsh(Ms)
        S = np.abs(ev[:,iu[0]]+ev[:,iu[1]])
        mp = S.min(axis=1)
        D  = np.abs(np.diff(ev,axis=1)).min(axis=1)
        flag = (mp<thr)|(D<thr)
        if (~flag).any():
            minmargin = min(minmargin, float(min(mp[~flag].min(), D[~flag].min())))
        for r in np.nonzero(flag)[0]:
            Mi = np.rint(Ms[r]).astype(np.int64)
            p = CN.charpoly_int(Mi)
            e1,_ = CN.has_pair_sum_zero(p)
            nzp   = CN._nonzero_pair(p)
            e2,nz2= CN.has_repeated(p)
            v0 = CN.val0(p)
            if e1:
                c['PAIR0']+=1
                if template_hit(Mi,n,'zero'): c['PAIR0_tmpl']+=1
            if nzp:
                c['PAIRNZ']+=1
                if template_hit(Mi,n,'zero'): c['PAIRNZ_tmpl']+=1
            if e2:
                c['REP']+=1
                if template_hit(Mi,n,'equal'): c['REP_tmpl']+=1
            if e2 and nz2:
                c['REPNZ']+=1
                if template_hit(Mi,n,'equal'): c['REPNZ_tmpl']+=1
            if v0>=2: c['CORANK2']+=1
    return c, done, minmargin

if __name__=='__main__':
    plan = {8:2000000, 9:2000000, 10:2000000, 11:3000000, 12:4000000,
            13:6000000, 14:8000000}
    res={}
    for n,tr in plan.items():
        t0=time.time()
        c,done,mm = run_mc(n,tr)
        res[n]=dict(counts=c, trials=done, minmargin=mm)
        print(f"n={n} trials={done} ({time.time()-t0:.0f}s) minmargin={mm:.2e}")
        for k in ('PAIR0','PAIRNZ','REP','REPNZ','CORANK2'):
            P=c[k]/done
            tm = c.get(k+'_tmpl')
            frac = (tm/c[k]) if (tm is not None and c[k]) else float('nan')
            print(f"   {k:8s} {c[k]:8d}  P={P:.3e}  P*4^n/n^4={P*4**n/n**4:8.4f}   template share={frac:.3f}")
        sys.stdout.flush()
        json.dump(res, open('mc_census.json','w'), indent=1)
