#!/usr/bin/env python3
"""Exact renewal coefficients and numerical roots for K_m * K_2."""
import csv, decimal, json, math, pathlib
ROOT=pathlib.Path(__file__).resolve().parents[1]
def coefficients(m,depth):
    a=[0]*m; value=1
    for k in range(1,m): value*=m-k; a[k]=value
    numerator=[0]*(depth+1); numerator[0]=1
    if depth: numerator[1]=1
    for k in range(1,min(m,depth+1)):
        numerator[k]+=a[k]
        if k+1<=depth:numerator[k+1]+=a[k]
    c=[]
    for n in range(depth+1):
        c.append(numerator[n]+sum(a[j-1]*c[n-j] for j in range(2,min(m,n)+1)))
    return c

def above(m,x):
    """Numerical sign of sum_k (m-1)_k x^-k - x; monotone in x."""
    total=0.; term=1.
    for k in range(1,m):
        term*=(m-k)/x; total+=term
        if total>x:return True
        ratio=(m-k-1)/x
        if ratio<1 and total+term*ratio/(1-ratio)<x:return False
    return total>x

def root(m):
    lo=1.;hi=float(m-1)
    for _ in range(65):
        mid=(lo+hi)/2
        if above(m,mid):lo=mid
        else:hi=mid
    return (lo+hi)/2

def decimal_root(m):
    with decimal.localcontext() as context:
        context.prec=65
        lo=decimal.Decimal(1);hi=decimal.Decimal(m-1)
        for _ in range(230):
            x=(lo+hi)/2;term=decimal.Decimal(1);s=decimal.Decimal(0)
            for k in range(1,m):term*=decimal.Decimal(m-k)/x;s+=term
            if s>x:lo=x
            else:hi=x
        return str((lo+hi)/2)

def main():
    rows=[]
    for m in (3,4,5,6,8,10,20,50,100,1000,10000,100000,1000000):
        u=root(m)
        row={'degree':m,'mu_numeric':u,'deficit':m-u,'deficit_over_sqrt_m_log_m':(m-u)/math.sqrt(m*math.log(m))}
        if m<=100:
            d=decimal_root(m); assert abs(float(d)-u)<1e-11
            row['decimal65']=d
        rows.append(row)
    (ROOT/'data'/'clique_family.json').write_text(json.dumps(rows,indent=2)+'\n')
    with (ROOT/'data'/'clique_family.csv').open('w') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
    print(json.dumps(rows,indent=2))
if __name__=='__main__':main()
