from exterior_search import *

def main():
    rng=np.random.default_rng(505)
    records=[]
    for complex_ in [False,True]:
        worst=(float('inf'),None,None,None)
        negative=0
        for t in range(250):
            n=6
            K=random_K(rng,n,complex_)
            V=random_unitary(rng,n,complex_)
            L=(V*np.exp(rng.uniform(-8,8,n)))@V.conj().T
            T,p=operator(K,logdet_table(L))
            low=float(np.linalg.eigvalsh(T)[0])
            records.append({'complex':complex_,'trial':t,'mineig_T':low})
            if low<-1e-8:
                negative+=1
                q,U=rank2_min(T,n,rng,trials=2,complex_=complex_)
                if q<worst[0]:worst=(q,K,L,U)
        print('complex',complex_,'negative',negative,'best decomposable',worst[0],flush=True)
        if worst[1] is not None:np.savez(OUT/f'worst_external_{complex_}.npz',q=worst[0],K=worst[1],L=worst[2],U=worst[3])
    (OUT/'external_search_results.json').write_text(json.dumps(records,indent=2))

if __name__=='__main__':main()
