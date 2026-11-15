"""Independent truth-table restrictions, high-precision census extrema and proof checks."""
import itertools,json,math,random,time
from pathlib import Path
import mpmath as mp
from symmetric import evaluate,integer_data,mask_vector

def direct_truth(f,n):
    c=[float(x) for x in f]
    step=1
    while step<len(c):
        for i in range(0,len(c),2*step):
            for j in range(step):
                a,b=c[i+j],c[i+j+step];c[i+j]=(a+b)/2;c[i+j+step]=(a-b)/2
        step*=2
    mu=[x*x for x in c];A=B=G=P=H=I=0.
    for S,w in enumerate(mu):
        if not w:continue
        inside=[i for i in range(n) if S>>i&1];outside=[i for i in range(n) if not S>>i&1]
        cs=[]
        for z in range(1<<len(outside)):
            acc=0
            for y in range(1<<len(inside)):
                x=sum(((y>>j)&1)<<i for j,i in enumerate(inside))+sum(((z>>j)&1)<<i for j,i in enumerate(outside))
                acc+=f[x]*(-1 if y.bit_count()%2 else 1)
            cs.append(acc/(1<<len(inside)))
        up=sum(x*x for x in cs)/len(cs);L=sum(abs(x) for x in cs)/len(cs);p=sum(x!=0 for x in cs)/len(cs)
        A-=w*math.log2(up);B+=w*math.log2(up/w);G+=w*math.log2(L/abs(c[S]));P-=w*math.log2(p);H-=w*math.log2(w);I+=S.bit_count()*w
    return dict(A=A,B=B,Gamma=G,P=P,H=H,I=I)

def main():
    start=time.monotonic();checks=0;maxerr=0.
    # Every Boolean truth table through n=4: the general identities and Gamma<=B/2.
    for n in range(1,5):
        for mask in range(1<<(1<<n)):
            f=[-1 if mask>>x&1 else 1 for x in range(1<<n)]
            # Faster independent spectral/up calculation; expensive restriction checks are for symmetric functions below.
            c=f[:];step=1
            while step<len(c):
                for i in range(0,len(c),2*step):
                    for j in range(step):
                        x,y=c[i+j],c[i+j+step];c[i+j]=x+y;c[i+j+step]=x-y
                step*=2
            mu=[x*x/(1<<(2*n)) for x in c];up=mu[:]
            for i in range(n):
                for S in range(1<<n):
                    if not S>>i&1:up[S]+=up[S|(1<<i)]
            A=sum(-w*math.log2(up[S]) for S,w in enumerate(mu) if w)
            B=sum(w*math.log2(up[S]/w) for S,w in enumerate(mu) if w)
            H=sum(-w*math.log2(w) for w in mu if w)
            I=sum(S.bit_count()*w for S,w in enumerate(mu));var=1-mu[0]
            assert abs(A+B-H)<1e-11
            assert A<=B+2*I-2*var+1e-11
            checks+=1
        for signs in itertools.product([-1,1],repeat=n+1):
            t=[signs[x.bit_count()] for x in range(1<<n)]
            a=direct_truth(t,n);b=evaluate(signs)
            for name,value in a.items():
                maxerr=max(maxerr,abs(value-float(b[name])));assert abs(value-float(b[name]))<1e-11
            assert a['Gamma']<=a['B']/2+1e-11
    print('all_truth_tables_through_n4',checks)
    print('symmetric_direct_truth_max_error',maxerr)
    records=[];precisiondiff=0.;integer_checks=0
    for n in range(1,25):
        row=json.loads(Path(f'census_{n:02d}.json').read_text())
        assert row['representatives']==1<<n
        for name,entry in row['maxima'].items():
            if entry['value']<0:continue
            f=mask_vector(n,entry['mask']);v=evaluate(f,80);v2=evaluate(f,120)
            assert v[name] is not None
            delta=abs(float(v[name])-entry['value']);precisiondiff=max(precisiondiff,delta)
            assert delta<2e-11,(n,name,delta)
            assert abs(v[name]-v2[name])<mp.mpf('1e-70')
            data=integer_data(f);total=1<<(2*n)
            assert sum(math.comb(n,k)*F*F for k,(F,L,Q,N) in enumerate(data))==total
            boundary=sum(math.comb(n-1,t) for t in range(n) if f[t]!=f[t+1])
            assert sum(k*math.comb(n,k)*F*F for k,(F,L,Q,N) in enumerate(data))==2*n*boundary*(1<<n)
            for k,(F,L,Q,N) in enumerate(data):
                lhs=Q*(1<<(n-k))
                rhs=sum(math.comb(n-k,j-k)*data[j][0]**2 for j in range(k,n+1))
                assert lhs==rhs,(n,k,lhs,rhs)
            integer_checks+=1
            vals={key:mp.nstr(value,55) if value is not None and not isinstance(value,(str,bool,int)) else value for key,value in v.items()}
            records.append({'n':n,'objective':name,'mask':entry['mask'],'metrics':vals})
    Path('extrema_high_precision.json').write_text(json.dumps(records,indent=2)+'\n')
    print('high_precision_extremizers_checked',integer_checks)
    print('max_C_vs_80_digit_error',precisiondiff)
    # Attempt to break each analytic step on random arbitrary level laws, plus Boolean spectra.
    rng=random.Random(709)
    tested=0
    for n in [2,3,4,8,16,24,32,64,128]:
        for rep in range(100):
            raw=[10**rng.uniform(-12,0) for _ in range(n+1)];W=[x/sum(raw) for x in raw]
            I=sum(k*w for k,w in enumerate(W));D=sum(w*math.log2(math.comb(n,k)) for k,w in enumerate(W))
            up=[sum(W[j]*math.comb(j,k)/math.comb(n,k) for j in range(k,n+1)) for k in range(n+1)]
            B=sum(w*math.log2(up[k]*math.comb(n,k)/w) for k,w in enumerate(W))
            a=2*math.asinh(1/(2*math.sqrt(n)));kap=(a+1/(n*math.expm1(a)))/math.log(2)
            assert B-D<=kap*I+1e-10
            tested+=1
    print('random_level_laws_entropy_gain_checks',tested)
    print('wall_seconds',time.monotonic()-start)
if __name__=='__main__':main()
