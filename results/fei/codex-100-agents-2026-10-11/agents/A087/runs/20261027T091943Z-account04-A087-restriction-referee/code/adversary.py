from audit import *

def main():
    t0=time.monotonic();checks=0
    def ck(x):
        nonlocal checks
        assert x;checks+=1
    # Frozen before execution in ADVERSARY_SPEC.json: actual point4 x point3,
    # common reset boundary r=3, install the smaller factor first, then both A children.
    fa,fb=point(4),point(3);pa,pb=spectrum(fa),spectrum(fb);qb=margprod(pb)
    tensor=lambda p,q:[x*y for y in q for x in p]
    f=[a*b for b in fb for a in fa];p=spectrum(f);q=tensor(pa,qb)
    ck(p==tensor(pa,pb));ck(sum(q)==1)
    root=entropy(p);mid=cross(p,q);complete=scale(M(3),F(3,2))
    ck(mid[0]>root[1]);ck(mid[0]>complete[1])
    gap=add(mid,scale(maxiv(root,complete),-1))
    ck(gap[0]>F(1,5))
    children=[]
    for b in (0,1):
        fc=child(f,0,b);pc=spectrum(fc);qa=spectrum(child(fa,0,b));qc=tensor(qa,qb)
        ck(pc==tensor(qa,pb));ck(sum(qc)==1)
        ce=cross(pc,qc);h=entropy(pc);kl=add(ce,scale(h,-1))
        ck(ge(kl,(F(0),F(0))))
        ck(overlap(ce,add(entropy(qa),M(3))))
        children.append(ce)
    ck(ge(add(H(4),M(3)),scale(add(*children),F(1,2))))
    save('out/ADVERSARY.json',{'status':'PASS','assertions':checks,'elapsed_seconds':time.monotonic()-t0,'actual_n':7,'r':3,'root_entropy':[str(x) for x in root],'mixed_terminal_full_CE':[str(x) for x in mid],'completed_expected_full_CE':[str(x) for x in complete],'intermediate_over_endpoint_max_gap':[str(x) for x in gap],'interpretation':'Guard against heterogeneous endpoint-max extrapolation; A061 identical-block theorem is unchanged. Both actual children retain frozen product Q and complete H+KL.'})
    print(json.dumps({'status':'PASS','assertions':checks,'strict_gap_lower':'1/5','elapsed_seconds':time.monotonic()-t0}))

if __name__=='__main__':main()
