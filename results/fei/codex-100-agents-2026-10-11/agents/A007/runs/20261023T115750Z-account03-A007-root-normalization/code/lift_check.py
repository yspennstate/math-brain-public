from fractions import Fraction as R
from pathlib import Path
import argparse, json, time
ROOT=Path(__file__).resolve().parents[1]
START=time.perf_counter();checks=0
def ck(x):
    global checks
    checks+=1; assert x,checks
    if checks%1000==0:assert time.perf_counter()-START<55
def transform(t):
    a=list(t);h=1
    while h<len(a):
        for i in range(0,len(a),2*h):
            for j in range(i,i+h):a[j],a[j+h]=a[j]+a[j+h],a[j]-a[j+h]
        h*=2
    return [R(v,len(a)) for v in a]
def influence(t):
    n=(len(t)-1).bit_length()
    return sum(R(sum(t[x]!=t[x^(1<<j)] for x in range(len(t))),len(t)) for j in range(n))
def main():
    p=argparse.ArgumentParser();p.add_argument('--pilot',action='store_true');args=p.parse_args()
    cases=0;truth_points=0
    for n in range(1,3 if args.pilot else 4):
        for word in range(1,(1<<(1<<n))-1):
            f=[1 if (word>>x)&1 else -1 for x in range(1<<n)];fh=transform(f);oldI=influence(f)
            q=[R(0)]+[R(s+1,sum(range(2,(1<<n)+1))) for s in range(1,1<<n)]
            for k,labels in [(1,[1]*n),(1,[j%2 for j in range(n)]),(2,[1+j%3 for j in range(n)])]:
                g=[]
                for xz in range(1<<(n+k)):
                    x=xz&((1<<n)-1);z=xz>>n;y=0
                    for j in range(n):y|=(((x>>j)&1)^((z&labels[j]).bit_count()%2))<<j
                    g.append(f[y])
                gh=transform(g);pred=[R(0)]*len(g);ref=[R(0)]*len(g);extra=R(0)
                for s,c in enumerate(fh):
                    mask=0
                    for j in range(n):
                        if (s>>j)&1:mask^=labels[j]
                    target=s|(mask<<n);pred[target]=c;ref[target]=q[s]
                    extra+=c*c*mask.bit_count()
                ck(gh==pred);ck(sum(ref)==1);ck(sorted(c*c for c in gh if c)==sorted(c*c for c in fh if c))
                newI=influence(g);ck(newI==oldI+extra);ck(newI>=oldI)
                ck(sum(s.bit_count()*c*c for s,c in enumerate(gh))==newI)
                cases+=1;truth_points+=len(g)
    ck(cases==(48 if args.pilot else 810));ck(time.perf_counter()-START<55)
    result={'PASS':True,'cases':cases,'assertions':checks,'physical_truth_points':truth_points,'elapsed_seconds':time.perf_counter()-START,'pilot':args.pilot}
    (ROOT/'out'/('lift_pilot.json' if args.pilot else 'lift_full.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result))
if __name__=='__main__':main()
