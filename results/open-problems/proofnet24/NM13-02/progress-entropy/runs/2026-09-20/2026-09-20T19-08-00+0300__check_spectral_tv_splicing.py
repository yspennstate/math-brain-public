import math, json, random
from collections import Counter

TOL=3e-12

def fwht_int(a):
    a=list(map(int,a)); n=len(a); h=1
    while h<n:
        for i in range(0,n,2*h):
            for j in range(i,i+h):
                x=a[j]; y=a[j+h]
                a[j]=x+y; a[j+h]=x-y
        h*=2
    return a

def entropy_from_w(W):
    N=len(W); s=0.0
    for w in W:
        if w:
            p=(w/N)**2
            s -= p*math.log2(p)
    return s

def influence_total(vals, n):
    N=len(vals); total=0.0; coords=[]
    for i in range(n):
        cnt=sum(1 for x in range(N) if vals[x] != vals[x^(1<<i)])
        inf=cnt/N; coords.append(inf); total += inf
    return total,coords

def metrics(Wg,Wh,g=None,h=None):
    N=len(Wg); B=0.0; overlap=0.0; tv=0.0
    for ug,vh in zip(Wg,Wh):
        u=ug/N; v=vh/N; x=abs(u); y=abs(v)
        den=x*x+y*y
        if den:
            p=((x-y)*(x-y))/(2*den)
            hb=0.0 if p<=0 or p>=1 else -p*math.log2(p)-(1-p)*math.log2(1-p)
            B += 0.5*den*hb
        overlap += x*y
        tv += 0.5*abs(x*x-y*y)
    M=0.5*(1-overlap)
    out={"B":B,"M":M,"TV":tv}
    if g is not None:
        inf=sum(1 for a,b in zip(g,h) if a!=b)/len(g)
        out["inf"]=inf; out["j"]=min(inf,1-inf)
    return out

def compatible_at(Wg,Wh,t):
    x=abs(Wg[t]); y=abs(Wh[t])
    return x==0 or y==0 or x==y

def exhaustive_small(max_n=3):
    result={"all_pair_count":0,"toggle_pair_count":0,"one_exception_cert_count":0,
            "max_B_minus_TV":-1e9,"max_toggle_abs_B_minus_2M":0.0,
            "max_toggle_2M_minus_2j":-1e9,"max_one_exception_TV_minus_4M":-1e9,
            "max_B_over_TV":0.0,"max_toggle_B_over_j":0.0}
    function_count=0
    for n in range(1,max_n+1):
        N=1<<n; funcs=[]
        for mask in range(1<<(N-1)):
            vals=[1]+[1 if ((mask>>(x-1))&1)==0 else -1 for x in range(1,N)]
            funcs.append((vals,fwht_int(vals)))
        function_count += len(funcs)
        for g,Wg in funcs:
            for h,Wh in funcs:
                z=metrics(Wg,Wh,g,h); B=z["B"]; M=z["M"]; tv=z["TV"]; j=z["j"]
                if B>tv+TOL or M>j+TOL:
                    raise AssertionError(("universal",n,B,tv,M,j))
                result["all_pair_count"]+=1
                result["max_B_minus_TV"]=max(result["max_B_minus_TV"],B-tv)
                if tv>1e-15: result["max_B_over_TV"]=max(result["max_B_over_TV"],B/tv)
                bad=[t for t in range(N) if not compatible_at(Wg,Wh,t)]
                if not bad:
                    if abs(B-tv)>TOL or abs(B-2*M)>TOL or 2*M>2*j+TOL:
                        raise AssertionError(("toggle",n,B,tv,M,j))
                    result["toggle_pair_count"]+=1
                    result["max_toggle_abs_B_minus_2M"]=max(result["max_toggle_abs_B_minus_2M"],abs(B-2*M))
                    result["max_toggle_2M_minus_2j"]=max(result["max_toggle_2M_minus_2j"],2*M-2*j)
                    if j>1e-15: result["max_toggle_B_over_j"]=max(result["max_toggle_B_over_j"],B/j)
                if len(bad)<=1:
                    certs = N if len(bad)==0 else 1
                    if tv>4*M+TOL:
                        raise AssertionError(("one-exception",n,bad,tv,M))
                    result["one_exception_cert_count"] += certs
                    result["max_one_exception_TV_minus_4M"]=max(result["max_one_exception_TV_minus_4M"],tv-4*M)
    result["functions_mod_sign_total"]=function_count
    return result

def random_n4(samples=2500,seed=20260920):
    rng=random.Random(seed); n=4; N=16
    maxv=-1e9; toggle=0; one=0
    for _ in range(samples):
        g=[1]+[rng.choice((-1,1)) for _ in range(N-1)]
        h=[1]+[rng.choice((-1,1)) for _ in range(N-1)]
        Wg=fwht_int(g); Wh=fwht_int(h); z=metrics(Wg,Wh,g,h)
        if z["B"]>z["TV"]+TOL or z["M"]>z["j"]+TOL:
            raise AssertionError(("random4",z))
        maxv=max(maxv,z["B"]-z["TV"])
        bad=[t for t in range(N) if not compatible_at(Wg,Wh,t)]
        if not bad:
            toggle+=1
            if abs(z["B"]-2*z["M"])>TOL: raise AssertionError(("random-toggle",z))
        if len(bad)<=1:
            one+=1
            if z["TV"]>4*z["M"]+TOL: raise AssertionError(("random-one",z,bad))
    return {"samples":samples,"max_B_minus_TV":maxv,"toggle_pairs":toggle,"one_exception_pairs":one}

IRRED={1:0b11,2:0b111,3:0b1011,4:0b10011}
def gf_mul(a,b,m):
    poly=IRRED[m]; res=0; aa=a; bb=b
    while bb:
        if bb&1: res ^= aa
        bb >>=1; aa <<=1
        if aa & (1<<m): aa ^= poly
    return res & ((1<<m)-1)

def graph_children(m):
    q=1<<m; N=q**3; gy=[0]*N; gx=[0]*N
    for y in range(q):
        for z in range(q):
            for x in range(q):
                idx=x | (z<<m) | (y<<(2*m))
                gy[idx]=-1 if y==gf_mul(x,z,m) else 1
                gx[idx]=-1 if x==gf_mul(y,z,m) else 1
    return gy,gx

def finite_field_family():
    rows=[]
    for m in range(1,5):
        q=1<<m; gy,gx=graph_children(m); N=len(gy); Wy=fwht_int(gy); Wx=fwht_int(gx)
        c=1-2/q; a=2/(q*q); tail_num=round(N*a); head_num=round(N*abs(c))
        expected_tail=q*q*(q-1)
        expected=Counter({tail_num:expected_tail}) if q==2 else Counter({head_num:1,tail_num:expected_tail})
        if Counter(abs(w) for w in Wy if w)!=expected or Counter(abs(w) for w in Wx if w)!=expected:
            raise AssertionError(("child spectrum",m))
        sy={i for i,w in enumerate(Wy) if w and i!=0}; sx={i for i,w in enumerate(Wx) if w and i!=0}
        exp_sy={i for i in range(N) if (i>>(2*m)) & (q-1)}; exp_sx={i for i in range(N) if i & (q-1)}
        if sy!=exp_sy or sx!=exp_sx: raise AssertionError(("support geometry",m))
        r=len(sy^sx); inter=len(sy&sx)
        z=metrics(Wy,Wx,gy,gx)
        if any(not compatible_at(Wy,Wx,t) for t in range(N)): raise AssertionError(("not toggle",m))
        if abs(z["B"]-2*z["M"])>TOL or abs(z["B"]-z["TV"])>TOL: raise AssertionError(("toggle identity",m,z))
        B_formula=4*(q-1)/(q**3); delta_formula=2*(q-1)**2/(q**3)
        if abs(z["B"]-B_formula)>TOL or abs(z["inf"]-delta_formula)>TOL: raise AssertionError(("root formula",m,z))
        H=entropy_from_w(Wy); I,_=influence_total(gy,3*m)
        p0=c*c; s=4*(q-1)/(q*q)
        H_formula=(0 if p0==0 else -p0*math.log2(p0))+s*(4*m-2)
        I_formula=6*m/q-4*m/(q*q)
        if abs(H-H_formula)>5e-11 or abs(I-I_formula)>TOL: raise AssertionError(("child formula",m,H,H_formula,I,I_formula))
        if H>(8/3)*I+TOL: raise AssertionError(("8/3 child",m,H,I))
        parent=gy+gx; Wp=fwht_int(parent); NP=2*N
        cnt=Counter(abs(w) for w in Wp if w); expected_cnt=Counter()
        if c!=0: expected_cnt[round(NP*abs(c))]=1
        expected_cnt[round(NP*a)]+=q*(q-1)**2
        expected_cnt[round(NP*a/2)]+=4*q*(q-1)
        if cnt!=expected_cnt: raise AssertionError(("parent spectrum",m,cnt,expected_cnt))
        Iparent,_=influence_total(parent,3*m+1)
        graft=z["B"]+H
        if graft>(8/3)*Iparent+TOL: raise AssertionError(("graft 8/3",m,graft,Iparent))
        Rlarge=(q*(q-1)**2+1) if q>=4 else q*(q-1)**2
        rows.append({"m":m,"q":q,"tail_symdiff_r":r,"tail_intersection":inter,
          "B_root":z["B"],"M_root":z["M"],"TV_root":z["TV"],"selector_influence":z["inf"],
          "B_over_selector_influence":z["B"]/z["inf"],"child_H":H,"child_I":I,"child_H_over_I":H/I,
          "parent_I":Iparent,"graft_B_plus_H":graft,"graft_over_parent_I":graft/Iparent,
          "parent_medium_count":q*(q-1)**2,"parent_small_count":4*q*(q-1),
          "few_exception_R_at_smallest_unit":Rlarge,"few_exception_bound_6_plus_log2_R1":6+math.log2(Rlarge+1)})
    return rows

def scalar_grid(N=200000):
    max_ratio=0.0; min_slack=1.0
    for k in range(N+1):
        p=0.5*k/N
        h=0 if p==0 else -p*math.log2(p)-(1-p)*math.log2(1-p)
        rhs=2*math.sqrt(p*(1-p))
        if h>rhs+1e-14: raise AssertionError((p,h,rhs))
        if rhs>0: max_ratio=max(max_ratio,h/rhs)
        min_slack=min(min_slack,rhs-h)
    return {"grid_points":N+1,"max_h_over_2sqrt":max_ratio,"min_slack":min_slack}

if __name__=='__main__':
    out={"status":"PASS","scalar":scalar_grid(),"exhaustive_small":exhaustive_small(),
         "random_n4":random_n4(),"finite_field_family":finite_field_family()}
    print(json.dumps(out,indent=2,sort_keys=True))
