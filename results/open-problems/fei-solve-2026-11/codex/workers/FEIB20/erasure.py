#!/usr/bin/env python3
"""Importance sampling of mate erasure entropy using six tensor-product terms plus the constant."""
import nested as N
import sys, math, json, time
sys.path.insert(0,'~/fei_solve_agent/code')
from tree_dnf import Tree, Phi
import numpy as np

def partial(a,b,k):
    aa=[];bb=[];mult=[];zero=None
    for c0 in range(k+1):
      for c1 in range(k+1-c0):
       for c2 in range(k+1-c0-c1):
        c3=k-c0-c1-c2;counts=[c0,c1,c2,c3]
        aa.append(np.prod([a[j]**counts[j] for j in range(4)]));bb.append(np.prod([b[j]**counts[j] for j in range(4)]))
        mult.append(math.factorial(k)//math.prod(math.factorial(c) for c in counts))
        if c0==k:zero=len(aa)-1
    return np.array(aa),np.array(bb),np.array(mult),zero

def mate_mc(w,D,samples,seed):
    T=Tree(w,D);q=T.q;sg=math.sqrt(q*(1-q));L=w-1
    a=np.array([1-q/2,q/2,-sg/2,sg/2]);b=np.array([(1-q)/2,-(1-q)/2,-sg/2,sg/2])
    ap,bp,mult,pzero=partial(a,b,L-1)
    zp=[np.dot(mult,ap*ap),np.dot(mult,bp*bp)];pp=[mult*ap*ap/zp[0],mult*bp*bp/zp[1]]
    # target Q basis alpha=0,1, for coefficients omitting/including z.
    ag=np.array([a[0],a[2]]);ah=np.array([a[1],a[3]])
    bg=np.array([b[0],b[2]]);bh=np.array([b[1],b[3]])
    vectors=[ag,ag,bg,ah,ah,bh]
    partialkind=[0,0,1,0,0,1];restkind=[0,1,1,0,1,1]
    zrest=[T.Zn,T.Zm];prest=[T.pn,T.pm];rcoef=[T.n,T.m]
    ztarget=[float((v*v).sum()) for v in vectors]
    norm=[2*ztarget[c]*zp[partialkind[c]]*zrest[restkind[c]]**(D-1) for c in range(6)]
    # Fixed mixture; all components retain nonzero probability.
    weights=np.array([.15]*6+[.1]);rng=np.random.default_rng(seed)
    sums=np.zeros(3);squares=np.zeros(3);done=0
    while done<samples:
        B=min(4000,samples-done);comp=rng.choice(7,size=B,p=weights)
        alpha=np.zeros(B,dtype=int);pt=np.full(B,pzero,dtype=int);rest=np.full((B,D-1),T.zero,dtype=int);root=np.zeros(B,dtype=int)
        for c in range(6):
            ix=np.where(comp==c)[0];num=len(ix)
            if num==0:continue
            alpha[ix]=rng.choice(2,size=num,p=vectors[c]**2/ztarget[c]);pt[ix]=rng.choice(len(ap),size=num,p=pp[partialkind[c]])
            rest[ix]=rng.choice(len(T.n),size=(num,D-1),p=prest[restkind[c]]);root[ix]=rng.integers(2,size=num)
        nr=T.n[rest].prod(axis=1);mr=T.m[rest].prod(axis=1)
        pa,pb=ap[pt],bp[pt];sign=1-2*root
        g=ag[alpha]*pa*nr+sign*(ag[alpha]*pa-bg[alpha]*pb)*mr
        h=ah[alpha]*pa*nr+sign*(ah[alpha]*pa-bh[alpha]*pb)*mr
        zero=(root==0)&(alpha==0)&(pt==pzero)&(rest==T.zero).all(axis=1)
        g-=zero
        dens=np.zeros(B)
        for c in range(6):
            rc=nr if restkind[c]==0 else mr;pc=pa if partialkind[c]==0 else pb
            dens+=weights[c]*(vectors[c][alpha]*pc*rc)**2/norm[c]
        dens+=weights[6]*zero/(mult[pzero]*T.mult[T.zero]**(D-1))
        vals=[Phi(g*g,h*h)/dens,h*h/dens,(g*g+h*h)/dens]
        for k,v in enumerate(vals):sums[k]+=v.sum();squares[k]+=(v*v).sum()
        done+=B
    mean=sums/done;se=np.sqrt(np.maximum(0,squares/done-mean*mean)/done)
    return mean,se

def run():
    rows=[]
    for w,D in [(3,2),(4,2),(10,8),(12,16),(14,30),(16,55)]:
        start=time.time();T=N.Model(w,D);delta=N.witness(T,1,T.order('clause'))['inf']
        mean,se=mate_mc(w,D,400000,20261110)
        r={'w':w,'D':D,'coordinate':'mate','samples':400000,'seed':20261110,'inf':delta,'E_ratio':float(mean[0]/delta),'E_se_ratio':float(se[0]/delta),'inf_check_ratio':float(mean[1]/delta),'inf_check_se_ratio':float(se[1]/delta),'mass_check':float(mean[2]),'mass_check_se':float(se[2]),'seconds':time.time()-start}
        if w==3:
            mu=N.spectrum(T);p,q=N.paired(mu,1);exact=N.entropy(p,q)/q.sum();r['exact_E_ratio']=exact;assert abs(r['E_ratio']-exact)<5*r['E_se_ratio']
        assert abs(r['mass_check']-1)<5*r['mass_check_se']
        assert abs(r['inf_check_ratio']-1)<5*r['inf_check_se_ratio']
        rows.append(r);print(json.dumps(r),flush=True)
        if w>=10:
            BT=Tree(w,D);mean,se=BT.mc(400000,20261110)
            rr={'w':w,'D':D,'coordinate':'root','samples':400000,'seed':20261110,'inf':BT.inf,'E_ratio':float(mean[0]/BT.inf),'E_se_ratio':float(se[0]/BT.inf),'inf_check_ratio':float(mean[1]/BT.inf),'inf_check_se_ratio':float(se[1]/BT.inf),'mass_check':float(mean[2]),'mass_check_se':float(se[2])}
            assert abs(rr['mass_check']-1)<5*rr['mass_check_se'];assert abs(rr['inf_check_ratio']-1)<5*rr['inf_check_se_ratio']
            rows.append(rr);print(json.dumps(rr),flush=True)
        with open('erasure.json','w') as f:json.dump(rows,f,indent=2)
if __name__=='__main__':run()
