from pathlib import Path
from fractions import Fraction as F
import json,time
from arithmetic import fwht,log2,scale,plus,phi_ratio,Q
ROOT=Path(__file__).resolve().parents[1]
H=[-1 if x in {0,1,2,4,8,16,32,6,17,40} else 1 for x in range(64)]
CO=fwht(H)
def signed(iv,r):
    if r>=0:return scale(iv,r)
    lo,hi=scale(iv,-r);return -hi,-lo
def packets(p,j=0):
    m=1-2*p;v=1-m*m;rows=[]
    for T in range(64):
        if T>>j&1:continue
        a=b=F(0)
        for U in range(64):
            if U>>j&1 or U&T!=T:continue
            a+=CO[U]*m**(U^T).bit_count()
            b+=CO[U|1<<j]*m**(U^T).bit_count()
        w=v**T.bit_count();rows.append((T,w*(a+m*b)**2,w*b*b))
    return rows
def direct(p,j=0):
    m=1-2*p;v=1-m*m;rows=[]
    for T in range(64):
        if T>>j&1:continue
        ca=cb=F(0)
        for x in range(64):
            if x>>j&1:continue
            prob=F(1);basis=F(1)
            for k in range(6):
                if k==j:continue
                y=1-2*(x>>k&1);prob*=p if y==-1 else 1-p
                if T>>k&1:basis*=y-m
            a=F(H[x]+H[x|1<<j],2);b=F(H[x]-H[x|1<<j],2)
            ca+=prob*basis*(a+m*b);cb+=prob*basis*b
        rows.append((T,ca*ca/v**T.bit_count(),cb*cb/v**T.bit_count()))
    return rows
def reserve(p,t,rows=None):
    rows=rows or packets(p);q=sum(D for _,U,D in rows);iv=(0,0)
    for _,U,D in rows:iv=plus(iv,phi_ratio(U,t*D,F(1)))
    return plus(iv,signed(phi_ratio((1-2*p)**2,t,F(1)),-q))
def slope(p,rows):
    m=1-2*p;q=sum(D for _,U,D in rows)
    if not m:return {'status':'BALANCED_SAFE'}
    if any(D and not U for _,U,D in rows):return {'status':'NEGATIVE_INFINITY'}
    iv=(0,0)
    for _,U,D in rows:
        if D:iv=plus(iv,scale(log2(U/D),D))
    iv=plus(iv,signed(log2(m*m),-q))
    assert iv[0]>0 or iv[1]<0
    return {'status':'SAFE' if iv[0]>0 else 'UNSAFE_SMALL_SINGLETON','slope_interval':iv}
def main():
    start=time.perf_counter();records=[];checks=0
    for p in [F(M,64) for M in range(1,64)]+[F(1,128),F(127,128)]:
        rows=packets(p);assert rows==direct(p);checks+=32
        q=2*p*(1-p)**3*(2-p)
        for j in range(6):assert sum(D for _,U,D in packets(p,j))==q;checks+=1
        assert sum(U for _,U,D in rows)+(1-(1-2*p)**2)*q==1;checks+=1
        rec={'p':str(p),'q':str(q),'criterion':slope(p,rows),'packets':[[T,str(U),str(D)] for T,U,D in rows]}
        records.append(rec)
        (ROOT/'out'/'BIAS_CERTIFICATES.json').write_text(json.dumps(records,indent=2)+'\n')
        assert time.perf_counter()-start<55
    safe=[i for i in range(1,64) if records[i-1]['criterion']['status'] in ['SAFE','BALANCED_SAFE']]
    # Explicit same-bias small-singleton witnesses, frozen physical dimension 12.
    witnesses=[]
    for M in [16,17,18,19,20]:
        p=F(M,64);t=F(1,1024)**2
        for pp in [p,1-p]:
            iv=reserve(pp,t);witnesses.append({'p':str(pp),'beta':'1/1024','reserve_interval':iv,'strict_sign':'positive' if iv[0]>0 else 'negative' if iv[1]<0 else 'unresolved'})
    result={'version':'geometric-reserve-v1','scale_bits':192,'bias_cases':65,'packet_and_multiplier_assertions':checks,'safe_M':safe,'witness_diagnostics':witnesses,'runtime_seconds':time.perf_counter()-start,'failed':0}
    (ROOT/'out'/'CHECK.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
if __name__=='__main__':main()
