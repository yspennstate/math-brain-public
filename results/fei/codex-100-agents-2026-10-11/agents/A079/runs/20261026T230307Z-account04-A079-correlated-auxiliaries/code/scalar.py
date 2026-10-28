from pathlib import Path
from math import comb
import json, time

ROOT = Path(__file__).resolve().parents[1]

def mul(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): out[i+j]+=x*y
    return out

def power(a,n):
    out=[1]
    for _ in range(n): out=mul(out,a)
    return out

def certificate(a,b):
    # Homogeneous polynomial evaluated at (u,v)=(t,1).
    first=[0]*(a+1); first[0]=1; first[a]=3
    term=[0]*(3*b+1)
    for k in range(4): term[b*k]=comb(3,k)
    term[3*b]+=8
    left=power(first,3*b); right=power(term,a)
    coeff=[(1 << (4*a-6*b))*x-y for x,y in zip(left,right)]
    degree=3*a*b
    # Homogeneity converts the two cones into P(1+w,1) and P(1,1+w).
    cones=[]
    for c in (coeff,list(reversed(coeff))):
        shifted=[sum(c[j]*comb(j,k) for j in range(k,degree+1)) for k in range(degree+1)]
        cones.append(shifted)
    values=[]
    for u,v in [(10,11),(11,10),(100,101),(101,100),(1,0),(0,1),(1,1)]:
        val=sum(c*u**i*v**(degree-i) for i,c in enumerate(coeff))
        values.append({'u':u,'v':v,'sign':(val>0)-(val<0),'value':str(val)})
    return {'a':a,'b':b,'degree':degree,'coefficients':[str(x) for x in coeff],
            'ordered_cone_coefficients':[[str(x) for x in row] for row in cones],
            'positive_cone_certificate':all(x>=0 for row in cones for x in row),
            'negative_counts':[sum(x<0 for x in row) for row in cones], 'exact_values':values}

if __name__=='__main__':
    start=time.perf_counter()
    records=[certificate(a,b) for a,b in [(5,3),(7,4)]]
    result={'records':records,'seconds':time.perf_counter()-start,'arithmetic':'integer coefficients and evaluations'}
    (ROOT/'out').mkdir(exist_ok=True)
    (ROOT/'out/scalar.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps([{'p':f"{r['a']}/{r['b']}",'certificate':r['positive_cone_certificate'],'negative_counts':r['negative_counts'],'signs':[(v['u'],v['v'],v['sign']) for v in r['exact_values']]} for r in records]))
