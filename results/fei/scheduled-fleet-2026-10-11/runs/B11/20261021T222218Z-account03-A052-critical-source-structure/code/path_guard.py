from pathlib import Path
from fractions import Fraction as F
import json,time
from check_pair import analyze,walsh
ROOT=Path(__file__).resolve().parents[1]
def rank(vs):
    basis={}
    for v in vs:
        while v:
            k=v.bit_length()-1
            if k in basis: v^=basis[k]
            else: basis[k]=v; break
    return len(basis)
def code(m):
    r=(1<<m)-2
    return [0,1]+[(1<<(v-1))|(1<<v) for v in range(1,r)]+[1<<(r-1)]
def main():
    start=time.perf_counter(); checks=0; profiles=[]
    for m in [3,4,5,6]:
        C=code(m); M=1<<m; r=M-2
        assert len(C)==M and len(set(C))==M; checks+=2
        assert rank(C)==r; checks+=1
        # Every coordinate occurs twice. Every nonempty edge set in a tree
        # has nonempty even boundary, never all M rows (the zero row stays zero).
        assert all(sum(c>>i&1 for c in C)==2 for i in range(r)); checks+=r
        assert not any(c^(1<<i) in C for c in C for i in [2,3]); checks+=2*M
        assert sum((c^12) in C for c in C)==2; checks+=1
        profiles.append({'m':m,'data_bits':r,'address_bits':m,'H':2*m,'I':str(F(2*r,M)+F(m,2)),'p_internal':str(F(2,M)),'C2':0,'C3':0,'C23':str(F(2,M))})
    m=3; C=code(m); r=6; n=9; N=1<<n
    f=[(-1)**(((z&63)&C[z>>6]).bit_count()%2) for z in range(N)]
    table=sum((v<0)<<x for x,v in enumerate(f)); a=walsh(f)
    direct=[sum(f[x]*(-1)**((x&s).bit_count()%2) for x in range(N)) for s in range(N)]
    assert a==direct; checks+=N
    for s in range(N):
        c=s&63; v=s>>6
        expected=N//8*(-1)**((v&C.index(c)).bit_count()%2) if c in C else 0
        assert a[s]==expected; checks+=1
    for u in range(N):
        assert sum(a[s]*a[s^u] for s in range(N))==(N*N if u==0 else 0); checks+=1
    p=[F(sum(a[s]**2 for s in range(N) if s>>i&1),N*N) for i in range(n)]
    assert p==[F(1,4)]*6+[F(1,2)]*3; checks+=n
    for v in range(1,N):
        w=F(sum(a[s]**2 for s in range(N) if (s&v).bit_count()%2),N*N)
        assert min(w,1-w)>=max(p[i] for i in range(n) if v>>i&1); checks+=1
    assert rank([s for s in range(N) if a[s]])==n; checks+=1
    data=analyze(n,table); assert data is not None; checks+=1
    pair=next(p for p in data['pairs'] if p['pair']==[2,3])
    assert F(pair['Csum'])==0 and F(pair['Q'])==F(1,4); checks+=2
    children=[]
    for bit in [2,3]:
        for value in [0,1]:
            inds=[x for x in range(N) if x>>bit&1==value]
            g=[f[x] for x in inds]; b=walsh(g); M=N//2
            assert sum(t!=0 for t in b)==64 and all(t*t in [0,1024] for t in b); checks+=2
            inf=F(sum(s.bit_count()*t*t for s,t in enumerate(b)),M*M)
            assert inf==F(11,4); checks+=1
            physical=sum(g[x]!=g[x^(1<<i)] for x in range(M) for i in range(8))
            assert F(physical,M)==inf; checks+=1
            children.append({'bit':bit,'value':value,'H':6,'I':str(inf),'H_over_I':'24/11'})
    # Independently evaluate partial Fourier rows by four direct physical samples.
    Q=F(0)
    for t in range(N):
        if t&12: continue
        row=[a[t^u] for u in [0,4,8,12]]; q=sum(v*v for v in row)
        if not q: continue
        vals=[sum(row[k]*(-1)**((k&x).bit_count()%2) for k in range(4)) for x in range(4)]
        Q+=sum(F((v*v-q)**2,4*q*N*N) for v in vals)
    assert Q==F(1,4); checks+=1
    out={'checks':checks,'profiles':profiles,'C':C,'table':str(table),'pair':pair,'children':children,'direct_pair_collision':str(Q),'seconds':time.perf_counter()-start,'status':'PASS'}
    (ROOT/'out/PATH_GUARD.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(out))
if __name__=='__main__': main()
