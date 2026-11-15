import json,math,time,os,resource,itertools
import numpy as np
import mpmath as mp
from experiment import phi,wht,bits,masses,best_order,analyse,adaptive_energy
from large import P
mp.mp.dps=90

def census():
    n=4;N=16;idx=np.arange(N);pc=np.array([int(j).bit_count() for j in idx]);total=65536;errs=dict(entropy_lower=0.,entropy_upper=0.,degree_influence=0.,sensitivity_influence=0.);maxF=0.;maxgap=0.;arg=None
    for start in range(0,total,256):
        tt=np.arange(start,start+256,dtype=np.uint64);f=1.-2.*((tt[:,None]>>idx.astype(np.uint64))&1).astype(float);fh=wht(f);mu=fh**2
        deg=np.max(np.where(mu>0,pc[None,:],0),axis=1);sen=np.zeros_like(f)
        for j in range(n):sen+=(f!=f[:,idx^(1<<j)])
        s=sen.max(axis=1);minF=np.full(256,np.inf);minE=np.full(256,np.inf)
        for i in range(n):
            lo=idx[((idx>>i)&1)==0];p,q=mu[:,lo],mu[:,lo+(1<<i)];delta=q.sum(axis=1);live=delta>0;a=p.copy();b=q.copy()
            for j in range(3):
                aa=a.reshape(256,-1,2,1<<j);bb=b.reshape(256,-1,2,1<<j);aa[:,:,1,:]+=aa[:,:,0,:];bb[:,:,1,:]+=bb[:,:,0,:]
            d=np.full((256,8),np.inf);d[:,0]=phi(a[:,0],b[:,0])
            for R in range(1,8):
                for j in range(3):
                    if R>>j&1:
                        Q=R^(1<<j);d[:,R]=np.minimum(d[:,R],d[:,Q]+phi(a[:,R]-a[:,Q],b[:,R]-b[:,Q]))
            E=phi(p,q).sum(axis=1);L=d[:,-1];errs['entropy_lower']=max(errs['entropy_lower'],float(np.max(E-L)));errs['entropy_upper']=max(errs['entropy_upper'],float(np.max(L-phi(1-delta,delta))))
            errs['degree_influence']=max(errs['degree_influence'],float(np.max(np.where(live,np.exp2(1-deg)-delta,0))))
            errs['sensitivity_influence']=max(errs['sensitivity_influence'],float(np.max(np.where(live,np.exp2(2-2*s)-delta,0))))
            minF=np.minimum(minF,np.where(live,L/np.maximum(delta,1e-300),np.inf));minE=np.minimum(minE,np.where(live,E/np.maximum(delta,1e-300),np.inf))
        valid=np.isfinite(minF);gaps=np.zeros(256);gaps[valid]=minF[valid]-minE[valid]
        if np.any(valid) and max(minF[valid])>maxF:
            k=int(np.argmax(np.where(valid,minF,-1)));maxF=float(minF[k]);arg=format(start+k,'x')
        maxgap=max(maxgap,float(max(gaps)))
    return dict(functions=total,errors=errs,max_F=maxF,max_F_truth=arg,max_gap=maxgap)

def fano_precision(depthmax=40):
    rec=next(r for r in json.load(open('structured.json'))['data'] if r['name']=='Fano_STS7_DNF');x=bits(7);f=np.where(np.any([x[:,L].all(axis=1) for L in rec['terms']],axis=0),-1.,1.);fh=wht(f);p,q=masses(fh**2,0)
    # Base masses are exact dyadics, represented by integers before arbitrary-precision arithmetic.
    scale=2**14;aa=[mp.mpf(int(round(z*scale))) for z in p];bb=[mp.mpf(int(round(z*scale))) for z in q]
    pivotal_count=int(sum(f[j]!=f[j^1] for j in range(128)))
    assert pivotal_count==36 and sum(bb)==mp.mpf(9)/32*scale
    for j in range(6):
        for R in range(64):
            if R>>j&1:aa[R]+=aa[R^(1<<j)];bb[R]+=bb[R^(1<<j)]
    alpha=mp.mpf(9)/32;c=mp.mpf(1);value=mp.mpf(0);rows=[]
    for depth in range(1,depthmax+1):
        d=[mp.inf]*64;d[0]=P(aa[0],c*c*bb[0])
        for R in range(1,64):
            d[R]=min(d[R^(1<<j)]+P(aa[R]-aa[R^(1<<j)],c*c*(bb[R]-bb[R^(1<<j)])) for j in range(6) if R>>j&1)
        inc=d[-1]/(scale*alpha*c);value+=inc;c*=alpha
        if depth in [1,2,4,8,20,40]:rows.append(dict(depth=depth,F=str(value),increment=str(inc)))
    C=mp.log(1/alpha,2)+1/mp.log(2);q=depthmax
    tail=alpha**q*(2*mp.log(1/alpha,2)*(q/(1-alpha)+alpha/(1-alpha)**2)+C/(1-alpha))
    return dict(precision=90,coordinate0_pivotal_inputs=pivotal_count,total_inputs=128,rows=rows,E='0 exactly by oddness',F_finite=str(value),tail=str(tail),upper=str(value+tail),note='Arbitrary precision, not directed interval rounding')

def structural_checks():
    rows=[]
    for n in range(3,16,2):
        x=bits(n);s=x.sum(axis=1);f=1.-2.*((s*(s-1)//2)%2);r=analyse(f,n,[0]);expected=2-2**(3-n)
        rows.append(dict(name=f'complete_quadratic_{n}',F=r['F'],E=r['E'],formula=expected,error=r['F']-expected))
    # General gate count beyond the three-block checks, still compared with full tables.
    from composition import state,compose
    rng=np.random.default_rng(191915);err=0.;count=0
    for w in [4,5]:
        sizes=[2,2,2,2] if w==4 else [2,2,2,1,1]
        for t in range(12):
            gs=[];children=[]
            for r in sizes:
                g=rng.choice([-1.,1.],1<<r)
                while np.all(g==g[0]):g=rng.choice([-1.,1.],1<<r)
                gs.append(g);children.append(state(g,r))
            F=rng.choice([-1.,1.],1<<w);ss=compose(F,children)
            if not ss['rows']:continue
            from experiment import compose_table
            full=analyse(compose_table(F,gs),sum(sizes));actual={r['i']:r for r in full['rows']};offset=np.cumsum([0]+sizes)
            for r in ss['rows']:
                i=int(offset[r['path'][0]]+r['path'][1]);z=actual[i];err=max(err,abs(r['L']-z['F']*z['inf']));count+=1
    return dict(quadratics=rows,composition_live_coordinates=count,composition_L_error=err)

def thresholds():
    rng=np.random.default_rng(191914);maxprod=0.;maxratio=0.;cases=0
    for n in range(4,13):
        xx=bits(n)
        for t in range(20):
            w=rng.integers(1,10,n);i=int(np.argmax(w));theta=float(rng.integers(-sum(w),sum(w)))+.5
            f=np.where((1-2*xx)@w>theta,1.,-1.);idx=np.arange(1<<n);lo=idx[((idx>>i)&1)==0];g=(f[lo]+f[lo+(1<<i)])/2;h=(f[lo]-f[lo+(1<<i)])/2;delta=float(np.mean(h*h))
            if not delta:continue
            mu=wht(f)**2;p,q=masses(mu,i);order=rng.permutation(n-1).tolist();A=np.arange(len(g));R=0
            from experiment import order_cost
            maxratio=max(maxratio,order_cost(p,q,order)[0]/delta)
            for j in order:
                key=A&R;cross=0.
                for v in np.unique(key):
                    gg=g[key==v];cross+=len(gg)/len(g)*2*np.mean(gg==1)*np.mean(gg==-1)
                R|=1<<j;key=A&R;su=np.bincount(key,weights=h,minlength=len(h));co=np.bincount(key,minlength=len(h));H=su[key]/co[key];stay=float(np.mean(H*H));maxprod=max(maxprod,cross*stay/delta**2)
            cases+=1
    return dict(functions=cases,max_cross_old_stay_new_over_delta_squared=maxprod,max_order_ratio=maxratio)

def main():
    start=time.time();d=dict(census4=census(),fano=fano_precision(),thresholds=thresholds(),structural=structural_checks());M=323/3;C=1/math.log(2)+4+2*math.log2(1+2*M)
    d['constants']=dict(LTF=C,LTF_FEI=C+2/math.log(2),M=M,CrossStay=160/3,degree_additive=1/math.log(2),readonce=10)
    d.update(seconds=time.time()-start,nice=os.getpriority(os.PRIO_PROCESS,0),maxrss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    json.dump(d,open('final_checks.json','w'),indent=2);json.dump(d['constants'],open('constants.json','w'),indent=2);print(json.dumps(d,indent=2))
if __name__=='__main__':main()
