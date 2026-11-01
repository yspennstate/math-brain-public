#!/usr/bin/env python3
"""Exact symbolic checker for BT4-F3-R3-TRI-ALT5-v1.

The checker encodes only consequences already present in the inherited
oriented exact-seven F3 defect-one pivot orbit.  It intentionally
*over-approximates* one-inport information by forbidding no unknown
in-arcs except those forced by orientation/sink conditions.  Therefore
absence of a surviving five-pivot alternating state is safe for the
stated lemma.

Universe: two triangular light supports A,B plus a three-vertex remainder.
The heavy support H is not expanded vertex-by-vertex; for each vertex when
it becomes a remainder sink we retain h=|N+(v) cap H| in {2,3}.  Since the
pivoted support is light, h=3 means A,B each contribute 2 outneighbors;
h=2 means the nonpivoted light support is heavy and contributes all 3.
Exact outdegree seven then fixes every sink's local outneighbor set.
"""
from itertools import combinations
import json

V = ("a0","a1","a2","b0","b1","b2","r0","r1","r2")
VS = set(V)


def add_req(E,F,u,v):
    if u == v or (u,v) in F or (v,u) in E:
        return False
    E.add((u,v)); F.add((v,u)); return True


def succ2(cyc,p):
    i = cyc.index(p)
    return cyc[(i+1)%3], cyc[(i+2)%3]


def in_from(E,cyc,v):
    return [x for x in cyc if (x,v) in E]


def triangle_sets(E):
    out=[]
    for X in combinations(V,3):
        a,b,c=X
        if ((a,b) in E and (b,c) in E and (c,a) in E) or \
           ((a,c) in E and (c,b) in E and (b,a) in E):
            out.append(frozenset(X))
    return set(out)


def three_triangle_pack(E):
    T=list(triangle_sets(E))
    for i in range(len(T)):
        for j in range(i+1,len(T)):
            if T[i] & T[j]:
                continue
            R=VS-T[i]-T[j]
            if len(R)==3 and frozenset(R) in T:
                return tuple(sorted(tuple(sorted(x)) for x in (T[i],T[j],frozenset(R))))
    return None


class State:
    __slots__=("A","B","R","sink","E","F","seq","L","h")
    def __init__(self,A,B,R,sink,E=None,F=None,seq=None,L=None,h=None):
        self.A=tuple(A); self.B=tuple(B); self.R=frozenset(R); self.sink=sink
        self.E=set() if E is None else set(E)
        self.F=set() if F is None else set(F)
        self.seq=[] if seq is None else list(seq)
        self.L={} if L is None else {k:frozenset(v) for k,v in L.items()}
        self.h={} if h is None else dict(h)
    def key(self):
        return (self.A,self.B,tuple(sorted(self.R)),self.sink,
                tuple(sorted(self.E)),tuple(sorted(self.F)),
                tuple(sorted((k,tuple(sorted(v))) for k,v in self.L.items())),
                tuple(sorted(self.h.items())))


def initial():
    E=set(); F=set()
    A=("a0","a1","a2"); B=("b0","b1","b2")
    for C in (A,B):
        for i in range(3):
            assert add_req(E,F,C[i],C[(i+1)%3])
    # canonical initial remainder sink r0
    F.add(("r0","r1")); F.add(("r0","r2"))
    return State(A,B,{"r0","r1","r2"},"r0",E,F,[],{}, {})


def establish_sink(st,supp,port):
    s=st.sink
    C=st.A if supp=="A" else st.B
    O=st.B if supp=="A" else st.A
    x,y=succ2(C,port)
    required={x,y}
    hvals=[st.h[s]] if s in st.h else [2,3]
    out=[]
    for hv in hvals:
        if hv==3:
            Ls=[frozenset(required|set(q)) for q in combinations(O,2)]
        else:
            Ls=[frozenset(required|set(O))]
        if s in st.L:
            Ls=[st.L[s]] if st.L[s] in Ls else []
        for L in Ls:
            if L & set(st.R):
                continue
            if len(L & set(C)) != 2:
                continue
            if hv==3 and (len(L & set(O)) != 2 or len(L)!=4):
                continue
            if hv==2 and (len(L & set(O)) != 3 or len(L)!=5):
                continue
            E=set(st.E); F=set(st.F); ok=True
            # exact outdegree seven: hv external H-neighbors plus this exact local set.
            for z in VS-{s}:
                if z in L:
                    if (s,z) not in E and not add_req(E,F,s,z):
                        ok=False; break
                else:
                    if (s,z) in E:
                        ok=False; break
                    F.add((s,z))
            if not ok:
                continue
            LL=dict(st.L); LL[s]=L
            hh=dict(st.h); hh[s]=hv
            out.append(State(st.A,st.B,st.R,s,E,F,st.seq,LL,hh))
    return out


def pivot(st,supp,port):
    out=[]
    for st0 in establish_sink(st,supp,port):
        C=st0.A if supp=="A" else st0.B
        s=st0.sink
        E=set(st0.E); F=set(st0.F)
        # inherited one-inport consequence: any already-forced second inport kills the branch.
        if any(x != port for x in in_from(E,C,s)):
            continue
        x,y=succ2(C,port)
        ok=True
        for u,v in ((port,s),(s,x),(s,y)):
            if (u,v) not in E and not add_req(E,F,u,v):
                ok=False; break
        if not ok:
            continue
        C2=(port,s,y)
        free=x
        R=set(st0.R); R.remove(s); R.add(free)
        A2=C2 if supp=="A" else st0.A
        B2=C2 if supp=="B" else st0.B
        for ns in sorted(R):
            F2=set(F); ok=True
            for z in R:
                if z==ns:
                    continue
                if (ns,z) in E:
                    ok=False; break
                F2.add((ns,z))
            if not ok:
                continue
            if len(in_from(E,A2,ns))>1 or len(in_from(E,B2,ns))>1:
                continue
            if ns in st0.L and (set(st0.L[ns]) & R):
                continue
            out.append(State(A2,B2,R,ns,E,F2,
                             st0.seq+[(supp,port,s,free)],st0.L,st0.h))
    return out


def fan_profile(st):
    s=st.sink
    if s not in st.L or s not in st.h:
        return None
    L=set(st.L[s])
    prof=(st.h[s],len(L&set(st.A)),len(L&set(st.B)))
    return prof, sorted(prof)==[2,2,3]


def run(next_sink):
    # First pivot A at a0 is WLOG by rotating the A triangle.  The two old
    # non-sink remainder vertices are symmetric, so both r1/r2 are checked.
    S=[x for x in pivot(initial(),"A","a0") if x.sink==next_sink]
    hist=[{"step":1,"support":"A","candidates":len(S),"three_pack":0,"survivors":len(S)}]
    for step,supp in ((2,"B"),(3,"A"),(4,"B"),(5,"A")):
        N=[]
        for st in S:
            C=st.A if supp=="A" else st.B
            for p in C:
                N.extend(pivot(st,supp,p))
        D={x.key():x for x in N}
        cand=list(D.values())
        packed=[x for x in cand if three_triangle_pack(x.E) is not None]
        S=[x for x in cand if three_triangle_pack(x.E) is None]
        hist.append({"step":step,"support":supp,"candidates":len(cand),
                     "three_pack":len(packed),"survivors":len(S)})
    exceptions=[]
    for st in S:
        fp=fan_profile(st)
        exceptions.append({
            "A":list(st.A),"B":list(st.B),"R":sorted(st.R),"sink":st.sink,
            "fan_profile":list(fp[0]) if fp else None,
            "fan_profile_is_322":bool(fp and fp[1]),
            "h":dict(sorted(st.h.items())),
            "sink_local_targets":sorted(st.L.get(st.sink,()))
        })
    return hist,exceptions


def main():
    h1,e1=run("r1")
    h2,e2=run("r2")
    assert h1==h2
    assert h1==[
        {"step":1,"support":"A","candidates":4,"three_pack":0,"survivors":4},
        {"step":2,"support":"B","candidates":48,"three_pack":0,"survivors":48},
        {"step":3,"support":"A","candidates":384,"three_pack":0,"survivors":384},
        {"step":4,"support":"B","candidates":768,"three_pack":576,"survivors":192},
        {"step":5,"support":"A","candidates":216,"three_pack":213,"survivors":3},
    ]
    assert len(e1)==len(e2)==3
    assert all(x["fan_profile"]==[3,1,3] and not x["fan_profile_is_322"] for x in e1+e2)
    payload={
        "candidate":"BT4-F3-R3-TRI-ALT5-v1",
        "mirror_remainder_choice_agrees":True,
        "history":h1,
        "fifth_step_nonpack_exceptions":e1,
        "valid_surviving_five_alternation_states":0,
        "interpretation":"213/216 fifth-step candidates already force three disjoint local directed triangles; the remaining three have next-sink fan profile (H,A,B)=(3,1,3), not a permutation of (3,2,2)."
    }
    print(json.dumps(payload,sort_keys=True,indent=2))


if __name__ == "__main__":
    main()
