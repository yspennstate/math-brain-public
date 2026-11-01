from exterior_search import *

def mobius(f):
    c=np.array(f,dtype=float,copy=True)
    n=(len(c)-1).bit_length()
    for i in range(n):
        for m in range(1<<n):
            if m>>i&1:c[m]-=c[m^(1<<i)]
    return c

def projection_operator(W,f):
    n,r=W.shape
    pairs=list(it.combinations(range(n),2));pi={p:j for j,p in enumerate(pairs)}
    T=np.zeros((len(pairs),len(pairs)),dtype=complex)
    c=mobius(f)
    for k in range(2,min(n,r+2)+1):
        for S in it.combinations(range(n),k):
            a=c[sum(1<<i for i in S)]
            if abs(a)<1e-16:continue
            for J in it.combinations(range(r),k-2):
                z=np.zeros(len(pairs),dtype=complex)
                for i,j in it.combinations(range(k),2):
                    rest=[S[l] for l in range(k) if l not in [i,j]]
                    z[pi[(S[i],S[j])]]=(-1)**(i+j)*(1 if k==2 else np.linalg.det(W[np.ix_(rest,J)]))
                T+=a*np.outer(z.conj(),z)
    return (T+T.conj().T)/2

def main():
    rng=np.random.default_rng(500005)
    records=[]
    worst=(1e100,None,None,None)
    for kind in ['logdet','nullity']:
        for complex_ in [False,True]:
            neg=0;low=1e100
            retained=None
            for t in range(300):
                n=6;r=2
                W=random_unitary(rng,n,complex_)[:,:r]
                if kind=='logdet':
                    V=random_unitary(rng,n,complex_)
                    L=(V*np.exp(rng.uniform(-12,12,n)))@V.conj().T
                    f=logdet_table(L)
                else:
                    B=rng.integers(-1,2,size=(n,3))*rng.integers(0,2,size=(n,3))
                    f=np.array([len(S)-np.linalg.matrix_rank(B[S]) if len(S) else 0 for S in subsets(n)],dtype=float)
                    L=B
                T=projection_operator(W,f)
                e=float(np.linalg.eigvalsh(T)[0]);low=min(low,e)
                records.append({'kind':kind,'complex':complex_,'trial':t,'mineig_T':e})
                if e<-1e-8:
                    neg+=1
                    q,U=rank2_min(T,n,rng,trials=2,complex_=complex_)
                    if q<worst[0]:worst=(q,W,L,U)
                    if retained is None or e<retained[0]:
                        retained=(e,dict(T=T,W=W,L=L,f=f,q=q,U=U))
            if retained is not None:
                np.savez(OUT/f'negative_projection_{kind}_{complex_}_retained.npz',**retained[1])
            print(kind,complex_,'min eig',low,'neg',neg,flush=True)
    (OUT/'projection_search_results.json').write_text(json.dumps(records,indent=2))
    print('min decomposable',worst[0],flush=True)

if __name__=='__main__':main()
