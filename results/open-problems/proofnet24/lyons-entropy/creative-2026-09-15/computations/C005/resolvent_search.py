from exterior_search import *

def main():
    rng=np.random.default_rng(51205)
    records=[]
    for complex_ in [False,True]:
        low=1e100;negative=0
        for t in range(100):
            n=6;K=random_K(rng,n,complex_)
            L=np.linalg.solve(np.eye(n)-K,K)
            data=atom_data(K)
            coeff=np.array([p*exterior2(Qi) for p,Qi in data])
            for s in [0.,.01,.1,1.,10.,100.]:
                f=np.array([np.linalg.inv(L[np.ix_(S,S)]+s*np.eye(len(S))).trace().real if len(S) else 0. for S in subsets(n)])
                f0=f.copy()
                for m in range(1<<n):f[m]-=sum(f0[1<<i] for i in range(n) if m>>i&1)
                T=np.einsum('s,sij->ij',f,coeff);T=(T+T.conj().T)/2
                e=float(np.linalg.eigvalsh(T)[0]);low=min(low,e)
                records.append({'complex':complex_,'trial':t,'s':s,'mineig_T':e})
                if e<-1e-9:
                    negative+=1
                    q,U=rank2_min(T,n,rng,trials=2,complex_=complex_)
                    np.savez(OUT/f'negative_resolvent_{complex_}_{t}_{s}.npz',T=T,K=K,L=L,s=s,q=q,U=U)
                    print('NEGATIVE',complex_,t,s,e,'q',q,flush=True)
                    break
            if negative:break
        print('resolvent',complex_,'min eig',low,'negative',negative,flush=True)
    (OUT/'resolvent_search_results.json').write_text(json.dumps(records,indent=2))

if __name__=='__main__':main()
