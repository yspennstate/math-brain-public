"""Exact forest edge-Rayleigh polynomial by frontier connectivity DP.

Retains marked endpoints, forgets other vertices after their last edge, and
rejects every edge insertion that would close a cycle. No determinants used.
"""
from fractions import Fraction as F
from general_H2_mirror_stress_heat import mul


def canonical(state):
    names={};out=[]
    for x in state:
        if x not in names:names[x]=len(names)
        out.append(names[x])
    return tuple(out)


def accumulate(dst,state,poly,shift=0,weight=1):
    out=dst.setdefault(state,{})
    for k,v in poly.items():out[k+shift]=out.get(k+shift,0)+v*weight


def forest_R_dp(n,edges,e,f):
    fixed=list(dict.fromkeys(e+f));active=list(fixed)
    states={tuple(range(len(active))):{0:1}}
    for step,(x,y,w)in enumerate(edges):
        w=int(w)if F(w).denominator==1 else F(w)
        new=[z for z in [x,y]if z not in active]
        if new:
            expanded={}
            for state,poly in states.items():
                st=list(state);next_label=max(st,default=-1)+1
                st.extend(range(next_label,next_label+len(new)))
                expanded[tuple(st)]=poly
            states=expanded;active+=new
        ix=active.index(x);iy=active.index(y);branches={}
        for state,poly in states.items():
            accumulate(branches,state,poly)
            if state[ix]!=state[iy]:
                sx,sy=state[ix],state[iy]
                joined=canonical([sx if z==sy else z for z in state])
                accumulate(branches,joined,poly,1,w)
        future={z for xx,yy,ww in edges[step+1:]for z in [xx,yy]}
        keep=[i for i,z in enumerate(active)if z in fixed or z in future]
        if len(keep)<len(active):
            states={}
            for state,poly in branches.items():accumulate(states,canonical([state[i]for i in keep]),poly)
            active=[active[i]for i in keep]
        else:states=branches
    polys=[{}for _ in range(4)]
    for state,poly in states.items():
        a,b,c,d=[state[active.index(z)]for z in e+f]
        ee=a!=b;ff=c!=d
        for P,ok in zip(polys,[True,ee,ff,ee and ff and {a,b}!={c,d}]):
            if ok:
                for k,v in poly.items():P[k]=P.get(k,0)+v
    A,B,C,D=polys;R=mul(B,C)
    for k,v in mul(A,D).items():R[k]=R.get(k,0)-v
    return {k:F(v)for k,v in sorted(R.items())if v}
