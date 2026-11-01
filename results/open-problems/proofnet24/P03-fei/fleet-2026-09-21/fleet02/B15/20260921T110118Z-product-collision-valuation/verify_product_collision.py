from fractions import Fraction
import json, math

F = [-1,1,-1,-1,1,-1,-1,1]
G = [-1,-1,1,1,-1,1,1,1,1,-1,1,1,-1,1,1,1]

def fwht(v):
    a=list(map(int,v)); h=1
    while h<len(a):
        for i in range(0,len(a),2*h):
            for j in range(i,i+h):
                x,y=a[j],a[j+h]
                a[j],a[j+h]=x+y,x-y
        h*=2
    return a

def v2(z):
    z=abs(z)
    assert z
    return (z & -z).bit_length()-1

def packets(vals):
    N=len(vals)
    W=fwht(vals)
    groups={}
    for S,w in enumerate(W):
        if w:
            groups.setdefault(abs(w),[]).append((S,1 if w>0 else -1))
    out={}
    for k,items in groups.items():
        mask=[0]*N
        for S,sgn in items: mask[S]=sgn
        V=fwht(mask)
        r=min(v2(x) for x in V if x)
        L=len(items)
        out[k]={"L":L,"r":r,"p":Fraction(L*k*k,N*N),"V":V}
    return W,out

def product(f,g):
    return [f[x]*g[y] for y in range(len(g)) for x in range(len(f))]

Wf,Pf=packets(F)
Wg,Pg=packets(G)
Wh,Ph=packets(product(F,G))

assert Wf == [-2,-2,2,2,-2,-2,2,-6]
assert Wg == [6,-2,-10,-2,-2,6,-2,6,-2,-2,-2,-2,-2,-2,-2,-2]
assert [(k,Pf[k]["L"],Pf[k]["r"],Pf[k]["p"]) for k in sorted(Pf)] == [
    (2,7,0,Fraction(7,16)), (6,1,0,Fraction(9,16))]
assert [(k,Pg[k]["L"],Pg[k]["r"],Pg[k]["p"]) for k in sorted(Pg)] == [
    (2,12,2,Fraction(3,16)), (6,3,0,Fraction(27,64)), (10,1,0,Fraction(25,64))]
assert Ph[12]["L"] == 33
assert Ph[12]["r"] == 0
assert Ph[12]["p"] == Fraction(297,1024)

delta=Fraction(0,1)
terms=[]
for kf,A in Pf.items():
    for kg,B in Pg.items():
        kout=kf*kg
        w=A["p"]*B["p"]
        term=w*(A["r"]+B["r"]-Ph[kout]["r"])
        delta += term
        if term:
            terms.append({"kf":kf,"kg":kg,"kout":kout,"weight":str(w),
                          "r_in":A["r"]+B["r"],"r_out":Ph[kout]["r"],
                          "term":str(term)})
assert delta == Fraction(27,128)
assert terms == [{"kf":6,"kg":2,"kout":12,"weight":"27/256",
                  "r_in":2,"r_out":0,"term":"27/128"}]

def D(P,N):
    ans=0.0
    for k,A in P.items():
        b=Fraction(k*(1<<A["r"]),N)
        ans += float(A["p"])*math.log2(1/float(b))
    return ans

out={"status":"PASS","exact_delta_D":"27/128",
     "nonzero_collision_terms":terms,
     "D_f":D(Pf,len(F)),"D_g":D(Pg,len(G)),
     "D_product":D(Ph,len(F)*len(G))}
out["numeric_delta"]=out["D_product"]-out["D_f"]-out["D_g"]
print(json.dumps(out,indent=2,sort_keys=True))
