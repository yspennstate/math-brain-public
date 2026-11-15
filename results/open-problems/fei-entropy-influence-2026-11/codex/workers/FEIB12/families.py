import json,math,csv,time
from pathlib import Path
from numerics import *

def summarize(F,family,name,meta=None):
    F=np.atleast_2d(F);n=F.shape[-1].bit_length()-1;d=data(F,details=n<=8);rows=[]
    Z,kl,C=coupling(d)
    for j,f in enumerate(F):
        I=float(d['I'][j]);v=float(d['var'][j]);ph=d['phi'][j].tolist();r=dict(family=family,name=name+(f'_{j}' if len(F)>1 else ''),n=n,I=I,var=v,phi=ph,phi_over_I=[x/I if I else None for x in ph],cost_over_I=(ph[2]-ph[-1])/I if I else None,cost_over_excess=(ph[2]-ph[-1])/(I-v) if I-v>1e-12 else None,tt=tt_hex(f))
        r['conditional_entropy_over_I']=float(C[j]/I) if I else None
        if n<=8:r['gamma']=float(d['gamma'][j]);r['gamma_over_I']=r['gamma']/I if I else None
        if meta:r.update(meta)
        rows.append(r)
    return rows

def readonce(n,rng):
    xs=np.arange(1<<n);leaves=[(1-2*((xs>>i)&1),f'x{i}') for i in range(n)]
    leaves=[(v,s) if rng.integers(2) else (-v,'NOT('+s+')') for v,s in leaves]
    while len(leaves)>1:
        ids=sorted(rng.choice(len(leaves),2,replace=False),reverse=True);a,ta=leaves.pop(ids[0]);b,tb=leaves.pop(ids[1]);op=rng.choice(['AND','OR'])
        ab=((a>0)&(b>0)) if op=='AND' else ((a>0)|(b>0))
        leaves.append((2*ab.astype(np.int8)-1,f'{op}({ta},{tb})'))
    return leaves[0]

def majority_large(n):
    m=(n-1)//2;c=math.comb(2*m,m)/2.**(2*m);hat=[0.]*(n+1)
    for r in range(m+1):hat[2*r+1]=(-1)**r*c*(math.comb(m,r)/math.comb(2*m,2*r))
    mu=np.array(hat)**2;W=np.array([math.comb(n,k)*mu[k] for k in range(n+1)])
    I=sum(k*W[k] for k in range(n+1));phi=[];F=[]
    for u in US:
        Fu=np.array([sum(math.comb(n-k,j-k)*mu[j]*u**(j-k) for j in range(k,n+1)) for k in range(n+1)])
        phi.append(float(-sum(W[k]*math.log2(Fu[k]) for k in range(n+1) if W[k])));F.append(Fu)
    mean=0.;atom=0.;quant=0.;med=0.
    for k in range(n+1):
        if not W[k]:continue
        q=np.array([math.comb(n-k,j-k)*mu[j]/F[-1][k] for j in range(k,n+1)])
        M=sum(q*np.arange(len(q)));w=q[0];mean+=W[k]*M
        cm=M/(1-w) if w<1 else 0
        atom-=W[k]*math.log2(w+(1-w)*2.**(-cm))
        cdf=np.cumsum(q);choices=[-math.log2(v)+j for j,v in enumerate(cdf) if v>0];quant+=W[k]*min(choices)
        med+=W[k]*int(np.argmax(cdf>=.5))
    Z=np.array([sum(math.comb(j,k)*mu[k]/F[-1][k] for k in range(j+1) if mu[k]) for j in range(n+1)])
    KL=float(sum(W[j]*Z[j]*math.log2(Z[j]) for j in range(n+1) if Z[j]>0 and W[j]>0))
    cond=(phi[0]-phi[-1]+KL)/I
    return dict(conditional_entropy_over_I=cond,kraft_error=float(abs(sum(W*Z)-1)),family='majority',name=f'majority_{n}',n=n,I=I,var=1.,phi=phi,phi_over_I=[x/I for x in phi],cost_over_I=(phi[2]-phi[-1])/I,cost_over_excess=(phi[2]-phi[-1])/(I-1) if I>1 else None,tt=None,symmetric_signs='+'*((n+1)//2)+'-'*((n+1)//2),mean_Jensen_over_I=mean/I,atom_bound_over_I=atom/I,quantile_bound_over_I=quant/I,median_level_over_I=med/I,parseval_error=float(abs(W.sum()-1)))

def and_large(n):
    a=2.**(1-n);M=(1-a)**2;phi=[]
    for u in US:
        delta=-2*a+a*a*(1+u)**n
        empty=-M*math.log1p(delta)/math.log(2)
        non=a*a*((2.**n-1)*2*(n-1)-(n*2.**(n-1)-n)*math.log2(1+u))
        phi.append(empty+non)
    I=n*a;v=2*a-a*a
    return dict(family='AND',name=f'AND_{n}',n=n,I=I,var=v,phi=phi,phi_over_I=[x/I for x in phi],cost_over_I=(phi[2]-phi[-1])/I,cost_over_excess=(phi[2]-phi[-1])/(I-v) if I>v else None,tt='0x1',method='closed form with log1p')

def main():
    rows=[];rng=np.random.default_rng(12102026)
    for n in range(1,17):
        xs=np.arange(1<<n);F=np.ones(1<<n,dtype=np.int8);F[0]=-1;rows+=summarize(F,'AND',f'AND_{n}')
        if n%2:rows+=summarize(1-2*(pc(n)>n//2),'majority',f'majority_{n}')
        if n in [4,6,8,12,16]:
            for r in range(6):
                f,tree=readonce(n,rng);rows+=summarize(f,'read_once',f'formula_{n}_{r}',{'tree':tree})
    for w,t in [(1,2),(2,2),(2,3),(2,4),(3,3),(3,4),(3,5),(4,4)]:
        n=w*t;xs=np.arange(1<<n);hit=np.zeros(1<<n,dtype=bool)
        for j in range(t):hit|=((xs>>(w*j))&((1<<w)-1))==0
        rows+=summarize(1-2*hit,'tribes',f'tribes_w{w}_t{t}')
    import itertools
    xs=np.arange(512);hit=np.zeros(512,dtype=bool)
    for p in itertools.permutations(range(3)):
        mask=sum(1<<(3*i+p[i]) for i in range(3));hit|=(xs&mask)==mask
    rows+=summarize(1-2*hit,'PM_K33','perfect_matching_K33')
    for k in [1,2,3]:
        n=k+(1<<k);xs=np.arange(1<<n);addr=xs&((1<<k)-1);out=(xs>>(k+addr))&1
        rows+=summarize(1-2*out,'address',f'address_{k}')
    for n in [6,8,12,16]:
        rows+=summarize(sample(n,24,12345+n),'random',f'random_{n}')
        xs=np.arange(1<<n);signs=1-2*((xs[:,None]>>np.arange(n))&1)
        for j in range(8):
            weights=rng.integers(1,20,n);score=signs@weights;thr=float(np.quantile(score,[.2,.5,.8][j%3]))+.25
            rows+=summarize(2*(score>=thr).astype(np.int8)-1,'LTF',f'LTF_{n}_{j}',{'weights':weights.tolist(),'threshold':thr})
    for n in [17,33,65,129,257,513]:rows.append(majority_large(n))
    for n in [24,32,64,128,256]:rows.append(and_large(n))
    Path('families.json').write_text(json.dumps(rows,indent=2,allow_nan=False))
    with open('families.csv','w') as f:
        w=csv.writer(f);w.writerow(['family','name','n','I','var',*[f'Phi({u})/I' for u in US],'cost/I','cost/(I-var)'])
        for r in rows:w.writerow([r['family'],r['name'],r['n'],r['I'],r['var'],*r['phi_over_I'],r['cost_over_I'],r['cost_over_excess']])
    print('rows',len(rows),'families',sorted(set(r['family'] for r in rows)),flush=True)
    for fam in sorted(set(r['family'] for r in rows)):
        rs=[r for r in rows if r['family']==fam and r['I']>0];print(fam,'Phi/I maxima',[max(r['phi_over_I'][j] for r in rs) for j in range(6)],'cost/I max',max(r['cost_over_I'] for r in rs),flush=True)
if __name__=='__main__':main()
