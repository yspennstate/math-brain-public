#!/usr/bin/env python3
import csv, math, sys
import numpy as np
from scipy.optimize import linear_sum_assignment

SQRT2=math.sqrt(2.0)
EL=SQRT2/3.0
EH=(4.0-SQRT2)/3.0
EF=2.0/3.0

def sign_y_plus_x_sqrt2(X,Y):
    if X==0: return (Y>0)-(Y<0)
    if Y==0: return (X>0)-(X<0)
    if X>0 and Y>0: return 1
    if X<0 and Y<0: return -1
    if X>0 and Y<0: return (2*X*X>Y*Y)-(2*X*X<Y*Y)
    return (Y*Y>2*X*X)-(Y*Y<2*X*X)

def factorization10(vertices):
    v=list(vertices); out=[]
    for r in range(9):
        pairs=[(v[9],v[r])]
        for i in range(1,5): pairs.append((v[(r+i)%9],v[(r-i)%9]))
        out.append(pairs)
    return out

def five_tilings():
    v=0
    rem=[q for q in range(11) if q!=v]
    fac=factorization10(rem)
    out=[]
    for rh in [0,1,2,3,5]:
        slots=[]
        for a,b in fac[0]: slots.append(('L',a+b-10))
        for a,b in fac[rh]: slots.append(('H',a+b-10))
        slots.append(('V',2*v-10))
        out.append((rh,slots))
    return out
TILINGS=five_tilings()

def exact_xy(tup):
    CSL,CSH,sV,ZL,ZH,ZV=tup
    A=11*CSL+ZL; B=11*CSH+ZH; C=11*sV+ZV
    return A-B, 4*B+2*C-2640

def cert_for_perm(p):
    s=np.array([j+p[j] for j in range(11)],dtype=np.float64)
    d=np.array([j-p[j] for j in range(11)],dtype=np.float64)
    for tid,(rh,slots) in enumerate(TILINGS):
        W=np.empty((11,11),dtype=np.float64)
        for c,(typ,znum) in enumerate(slots):
            z=znum/11.0
            if typ=='L': W[:,c]=(s+d*z)*EL
            elif typ=='H': W[:,c]=((s-2)+d*z)*EH
            else: W[:,c]=(s+d*z)*EF
        rr,cc=linear_sum_assignment(-W)
        CSL=CSH=sV=ZL=ZH=ZV=0
        for j,c in zip(rr,cc):
            typ,znum=slots[int(c)]
            sj=int(s[int(j)]); dj=int(d[int(j)])
            if typ=='L': CSL+=sj; ZL+=dj*znum
            elif typ=='H': CSH+=sj-2; ZH+=dj*znum
            else: sV=sj; ZV=dj*znum
        tup=(CSL,CSH,sV,ZL,ZH,ZV)
        X,Y=exact_xy(tup)
        if sign_y_plus_x_sqrt2(X,Y)>0:
            return tid,rh,tup,X,Y
    return None

def main(path):
    n=0; used={}; tuples=set(); minrec=None
    with open(path,newline='') as f:
        for row in csv.reader(f):
            if not row: continue
            p=tuple(map(int,row)); assert len(p)==11
            rec=cert_for_perm(p)
            if rec is None:
                raise AssertionError(f'no exact certificate for {p}')
            tid,rh,tup,X,Y=rec
            n+=1; used[tid]=used.get(tid,0)+1; tuples.add(tup)
            val=Y+X*SQRT2
            if minrec is None or val<minrec[0]: minrec=(val,X,Y,tup,p,tid,rh)
    assert n==20885, n
    assert len(tuples)==1044, len(tuples)
    val,X,Y,tup,p,tid,rh=minrec
    assert (X,Y)==(-502,710), minrec
    assert 710*710-2*502*502==92>0
    print('residuals=',n)
    print('tiling_use=',used)
    print('distinct_exact_tuples=',len(tuples))
    print('minimum_exact_margin=710-502*sqrt(2); square_gap=92; approx=',val)
    print('minimum_tuple=',tup)
    print('minimum_perm=',p)
    print('EXACT S11 ENDPOINT PHASE2 PASSED')

if __name__=='__main__':
    if len(sys.argv)!=2:
        print('usage: phase2.py residual.csv',file=sys.stderr); sys.exit(2)
    main(sys.argv[1])
