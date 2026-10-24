import argparse,json,time,hashlib
from pathlib import Path
from fractions import Fraction as Q
import numpy as np
ROOT=Path(__file__).resolve().parents[1];SCALE=1<<40
LOW=np.array([0x55555555,0x33333333,0x0f0f0f0f,0x00ff00ff,0x0000ffff],dtype=np.uint32)
def floor(x):return x.numerator//x.denominator
def ceil(x):return -floor(-x)
def series(z):
    p=sum((2*z**(2*j+1)/Q(2*j+1) for j in range(40)),Q(0))
    return p,p+2*z**81/(81*(1-z*z))
LN2=series(Q(1,3));L2=(floor(LN2[0]*SCALE),ceil(LN2[1]*SCALE))
def ln(k):
    e=k.bit_length()-1;r=Q(k,1<<e);z=(r-1)/(r+1);l,h=series(z)
    return l+e*LN2[0],h+e*LN2[1]
LOG={k:ln(k) for k in range(1,769)}
def entropy_num(w,den=256):
    if not w:return 0,0
    l,h=LOG[den];u,v=LOG[w]
    return floor(w*(l-v)*SCALE),ceil(w*(h-u)*SCALE)
GLO=np.array([entropy_num(k*k)[0] for k in range(17)],np.int64)
GHI=np.array([entropy_num(k*k)[1] for k in range(17)],np.int64)
def fwht(v):
    w=v.copy()
    for h in (1,2,4,8,16):
        if h>=w.shape[1]:break
        blocks=w.reshape(-1,w.shape[1]//(2*h),2,h)
        a=blocks[:,:,0,:].copy();b=blocks[:,:,1,:].copy()
        blocks[:,:,0,:]=a+b;blocks[:,:,1,:]=a-b
    return w
BRLO=[];BRHI=[]
for mask in range(16):
    w=fwht(np.array([[1-2*((mask>>j)&1) for j in range(4)]],np.int32))[0]
    lo=hi=Q(0)
    for t in w:
        t=int(t)
        if t:
            p=Q(t*t,16);u,v=LOG[16];l,h=LOG[t*t];lo+=p*(u-h);hi+=p*(v-l)
    BRLO.append(floor(lo*256*SCALE));BRHI.append(ceil(hi*256*SCALE))
BRLO=np.array(BRLO,np.int64);BRHI=np.array(BRHI,np.int64)
BOUNDLO=[];BOUNDHI=[]
for k in range(769):
    # 256*SCALE times ln2 times selector bound at s=k/256, a=3.
    lo=hi=Q(0)
    for t in [k,768-k]:
        if t:
            u,v=LOG[768];l,h=LOG[t];lo+=t*(u-h);hi+=t*(v-l)
    lo+=min(768*LN2[0],2*k);hi+=min(768*LN2[1],2*k)
    BOUNDLO.append(floor(lo*SCALE));BOUNDHI.append(ceil(hi*SCALE))
BOUNDLO=np.array(BOUNDLO,np.int64);BOUNDHI=np.array(BOUNDHI,np.int64)
def translate(m,a):
    for i in range(5):
        if a>>i&1:
            d=1<<i;low=LOW[i];m=((m>>d)&low)|((m&low)<<d)
    return m
def interval_record(mask,coordinate,lo,hi,blo,bhi,**kwargs):
    return dict(mask=int(mask),coordinate=coordinate,delta_num_interval=[int(lo),int(hi)],bound_num_interval=[int(blo),int(bhi)],ratio_interval=[str(Q(int(lo),int(bhi))),str(Q(int(hi),int(blo)))],**kwargs)
def run(pilot):
    start=time.perf_counter();stop=1<<20 if pilot else 1<<32;cap=60 if pilot else 1200;chunk=32768
    counts=dict(raw=0,minority_le_16=0,group_sorted=0,translation_minimal=0,zero_selector=0,singleton_tested=0,boundary_81_failures=0,boundary_81_unresolved=0,selector_90_failures=0,boundary_90_failures=0)
    bestsel=None;bestnode=None;bestselval=-1;bestnodeval=-1;failures=[];digest=hashlib.sha256();lastsave=0
    idx=np.arange(32,dtype=np.uint32);card=np.array([j.bit_count() for j in range(32)],np.int64);selcard=np.array([(j&7).bit_count() for j in range(32)],np.int64)
    for first in range(1,stop,2*chunk):
        if time.perf_counter()-start>cap:raise RuntimeError('Frozen deadline; checkpoint retained')
        masks=np.arange(first,min(first+2*chunk,stop),2,dtype=np.uint64).astype(np.uint32);counts['raw']+=len(masks)
        masks=masks[np.bitwise_count(masks)<=16];counts['minority_le_16']+=len(masks)
        for group in [(0,1,2),(3,4)]:
            prev=np.bitwise_count((masks^(masks>>(1<<group[0])))&LOW[group[0]])
            for i in group[1:]:
                cur=np.bitwise_count((masks^(masks>>(1<<i)))&LOW[i]);keep=prev<=cur;masks=masks[keep];prev=cur[keep]
        counts['group_sorted']+=len(masks)
        for a in range(1,32):
            if not len(masks):break
            t=translate(masks,a);masks=masks[((t&1)==0)|(masks<=t)]
        counts['translation_minimal']+=len(masks)
        if len(masks):
            digest.update(masks.tobytes())
            w=fwht((1-2*((masks[:,None]>>idx)&1).astype(np.int32)));assert np.all((w&1)==0)
            c=w//2;ac=np.abs(c);sq=c.astype(np.int64)**2;assert np.all(sq.sum(axis=1)==256)
            hlo=GLO[ac].sum(axis=1);hhi=GHI[ac].sum(axis=1)
            childlo=np.zeros(len(masks),np.int64);childhi=childlo.copy()
            for x in range(8):
                bm=np.zeros(len(masks),np.uint32)
                for y in range(4):bm|=((masks>>(x+8*y))&1)<<y
                childlo+=BRLO[bm];childhi+=BRHI[bm]
            dl=8*hlo-childhi;dh=8*hhi-childlo;snum=sq@selcard
            blo=8*BOUNDLO[snum];bhi=8*BOUNDHI[snum]
            positive=snum>0;counts['zero_selector']+=int((~positive).sum())
            assert np.all(dh[positive]<blo[positive]),'Lead selector inequality violated'
            assert np.all((dl[~positive]<=0)&(dh[~positive]>=0))
            counts['selector_90_failures']+=int((10*dh[positive]>=9*blo[positive]).sum())
            ratios=np.where(positive,dh/np.maximum(blo,1),-1);j=int(np.argmax(ratios))
            if ratios[j]>bestselval:
                bestselval=float(ratios[j]);bestsel=interval_record(masks[j],None,dl[j],dh[j],blo[j],bhi[j],selector_num=int(snum[j]),denominator=2048*SCALE)
            for i in range(5):
                left=np.array([t for t in range(32) if not(t>>i&1)]);right=left|(1<<i)
                aa=c[:,left];bb=c[:,right];p=np.abs(aa+bb);q=np.abs(aa-bb)
                dl=2*hlo-(GHI[p].sum(axis=1)+GHI[q].sum(axis=1));dh=2*hhi-(GLO[p].sum(axis=1)+GLO[q].sum(axis=1))
                dn=sq[:,right].sum(axis=1);en=sq[:,right]@(card[right]-1)
                physical=np.bitwise_count((masks^(masks>>(1<<i)))&LOW[i]).astype(np.int64);assert np.all(dn==16*physical)
                active=dn>=32;counts['singleton_tested']+=int(active.sum())
                blo=6*dn*SCALE+4*en*L2[0];bhi=6*dn*SCALE+4*en*L2[1]
                assert np.all(dh[active]<blo[active]),'Lead boundary bound violated'
                counts['boundary_90_failures']+=int((10*dh[active]>=9*blo[active]).sum())
                bad=active&(100*dl>81*bhi);unresolved=active&(~bad)&(100*dh>=81*blo)
                counts['boundary_81_failures']+=int(bad.sum());counts['boundary_81_unresolved']+=int(unresolved.sum())
                for j in np.flatnonzero(bad):
                    if len(failures)<256:failures.append(interval_record(masks[j],i,dl[j],dh[j],blo[j],bhi[j],influence_num=int(dn[j]),derivative_num=int(en[j]),denominator=512*SCALE))
                ratios=np.where(active,dh/np.maximum(blo,1),-1);j=int(np.argmax(ratios))
                if ratios[j]>bestnodeval:
                    bestnodeval=float(ratios[j]);bestnode=interval_record(masks[j],i,dl[j],dh[j],blo[j],bhi[j],influence_num=int(dn[j]),derivative_num=int(en[j]),denominator=512*SCALE)
            if failures and not (ROOT/'out'/'first_falsifiers.json').exists():(ROOT/'out'/'first_falsifiers.json').write_text(json.dumps(failures,indent=2))
        if time.perf_counter()-lastsave>=15:
            result=dict(counts=counts,best_selector=bestsel,best_boundary=bestnode,failures=failures,runtime_seconds=time.perf_counter()-start,last_mask=first,complete=False,enumeration_sha256=digest.hexdigest())
            (ROOT/'out'/'checkpoint.json').write_text(json.dumps(result,indent=2));print(json.dumps(dict(raw=counts['raw'],representatives=counts['translation_minimal'],seconds=result['runtime_seconds'],fail81=counts['boundary_81_failures'])),flush=True);lastsave=time.perf_counter()
    assert counts['raw']==stop//2
    if not pilot:assert counts['minority_le_16']==1<<30
    result=dict(mode='pilot' if pilot else 'full',counts=counts,best_selector=bestsel,best_boundary=bestnode,failures=failures,runtime_seconds=time.perf_counter()-start,complete=True,enumeration_sha256=digest.hexdigest(),scale=SCALE,all_lead_bounds_certified=True,certified_selector_cap_90=counts['selector_90_failures']==0,certified_boundary_cap_90=counts['boundary_90_failures']==0)
    (ROOT/'out'/('pilot.json' if pilot else 'census.json')).write_text(json.dumps(result,indent=2));print(json.dumps({k:v for k,v in result.items() if k!='failures'},indent=2))
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--pilot',action='store_true');run(ap.parse_args().pilot)
