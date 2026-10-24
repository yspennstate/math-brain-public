"""Exact finite cores for the mixed-spectrum continuation (standard library).

Not a proof-assistant verification of the analytic inequalities.  No floating
point is used to decide any assertion.  Outputs are regenerated, not trusted.
"""
from collections import Counter, defaultdict
from fractions import Fraction as Q
from itertools import product
from math import comb
from pathlib import Path
import hashlib
import json

ROOT=Path(__file__).resolve().parent
EDGES=[(i,(i+1)%10) for i in range(10)]+[(i,i+5) for i in range(5)]


def selected_edges(mask, edges=EDGES):
    return [e for j,e in enumerate(edges) if mask>>j&1]


def adjacency(edges):
    adj=defaultdict(list)
    for x,y in edges:
        adj[x].append(y);adj[y].append(x)
    return dict(adj)


def components(adj):
    seen=set();out=[]
    for x in adj:
        if x in seen:continue
        stack=[x];seen.add(x);part=[]
        while stack:
            v=stack.pop();part.append(v)
            for w in adj[v]:
                if w not in seen:seen.add(w);stack.append(w)
        out.append(part)
    return out


def theta_description(adj, part):
    """Return the sorted three branch-to-branch path lengths, or None."""
    branch=[x for x in part if len(adj[x])==3]
    if len(branch)!=2:return None
    a,b=branch;lengths=[]
    for start in adj[a]:
        prev,cur=a,start;length=1
        while cur not in branch:
            nxt=next(x for x in adj[cur] if x!=prev)
            prev,cur=cur,nxt;length+=1
        if cur!=b:return None  # A barbell has a returning cycle.
        lengths.append(length)
    return tuple(sorted(lengths))


def barbell_description(adj, part):
    branch=[x for x in part if len(adj[x])==3]
    if len(branch)!=2:return None
    a,b=branch;bridges=[];loops=[]
    for endpoint,other in [(a,b),(b,a)]:
        local_loops=[]
        for start in adj[endpoint]:
            prev,cur=endpoint,start;length=1
            while cur not in branch:
                nxt=next(x for x in adj[cur] if x!=prev)
                prev,cur=cur,nxt;length+=1
            if cur==other:
                if endpoint==a:bridges.append(length)
            else:local_loops.append(length)
        if local_loops:
            assert len(local_loops)==2 and local_loops[0]==local_loops[1]
            loops.append(local_loops[0])
    if len(bridges)==1 and len(loops)==2:
        return tuple(sorted(loops))+(bridges[0],)
    return None


def category(edges):
    adj=adjacency(edges)
    if not adj:return 'empty'
    if any(len(v)==1 for v in adj.values()):return 'vanish'
    parts=components(adj)
    if all(len(adj[x])==2 for x in adj):
        return 'cycles:'+','.join(map(str, sorted(map(len,parts))))
    if len(parts)==1:
        desc=theta_description(adj,parts[0])
        if desc is not None:return 'theta:'+','.join(map(str,desc))
        desc=barbell_description(adj,parts[0])
        if desc is not None:return 'barbell:'+','.join(map(str,desc))
    if len(parts)==2:
        cyc=[p for p in parts if all(len(adj[x])==2 for x in p)]
        other=[p for p in parts if not all(len(adj[x])==2 for x in p)]
        if len(cyc)==1 and len(cyc[0])==4 and len(other)==1:
            if theta_description(adj,other[0])==(1,3,3):
                return 'cycle4+theta133'
    return 'remainder'


def polynomial(edges):
    out=Counter()
    for mask in range(1<<len(edges)):
        es=selected_edges(mask,edges);adj=adjacency(es)
        if any(len(v)==1 for v in adj.values()):continue
        n3=sum(len(v)==3 for v in adj.values())
        assert n3%2==0
        out[len(es),n3//2]+=1
    return dict(out)


def bernstein(poly,n,m):
    return {(i,j):sum(c*Q(comb(i,a),comb(n,a))*Q(comb(j,b),comb(m,b))
                     for (a,b),c in poly.items() if a<=i and b<=j)
            for i in range(n+1) for j in range(m+1)}


def reconstruct(coeff,n,m):
    out=defaultdict(Q)
    for (i,j),v in coeff.items():
        for a in range(n-i+1):
            for b in range(m-j+1):
                out[i+a,j+b]+=v*comb(n,i)*comb(n-i,a)*comb(m,j)*comb(m-j,b)*(-1)**(a+b)
    return {k:v for k,v in out.items() if v}


def negative_ray(c):
    # lambda=-a*y, z=(1-a)^2/a, divide by a^4*y^4.
    out=defaultdict(Q)
    for (e,k),v in c.items():
        if e==0:continue
        for j in range(2*k+1):
            a,b=e-k+j-4,e-4
            assert a>=0 and b>=0
            out[a,b]+=v*(-1)**(e+j)*comb(2*k,j)
    return {k:v for k,v in out.items() if v}


def weighted_density(w,p):
    """Exact 5-variable contraction; H's complement is a 10-cycle."""
    n=len(w)
    c=[[[sum(p[u]*w[u][i]*w[u][j]*w[u][k] for u in range(n))
          for k in range(n)] for j in range(n)] for i in range(n)]
    total=Q(0)
    for z in product(range(n),repeat=5):
        term=Q(1)
        for i in range(5):term*=p[z[i]]*c[z[i]][z[(i+1)%5]][z[(i+2)%5]]
        total+=term
    return total


def matmul(a,b,p):
    return [[sum(a[i][k]*p[k]*b[k][j] for k in range(len(p)))
             for j in range(len(p))] for i in range(len(p))]


def moment(a,b,p):
    return sum(p[i]*p[j]*a[i][j]*b[i][j] for i in range(len(p)) for j in range(len(p)))


def regular(w,p):
    assert sum(p)==1 and all(x>0 for x in p)
    assert all(w[i][j]==w[j][i] and w[i][j]>=0 for i in range(len(p)) for j in range(len(p)))
    assert all(sum(p[j]*w[i][j] for j in range(len(p)))==1 for i in range(len(p)))


def eigenvalue(w,p,f):
    norm=sum(p[i]*f[i]**2 for i in range(len(p)))
    assert norm>0 and sum(p[i]*f[i] for i in range(len(p)))==0
    image=[sum(p[j]*w[i][j]*f[j] for j in range(len(p))) for i in range(len(p))]
    lam=next(image[i]/f[i] for i in range(len(p)) if f[i])
    assert all(image[i]==lam*f[i] for i in range(len(p)))
    return lam


def main():
    assert len(set(frozenset(e) for e in EDGES))==15
    assert all((x-y)%2 for x,y in EDGES)
    complement=[(i,j) for i in range(0,10,2) for j in range(1,10,2) if frozenset((i,j)) not in {frozenset(e) for e in EDGES}]
    ca=adjacency(complement)
    assert len(complement)==10 and len(components(ca))==1 and all(len(v)==2 for v in ca.values())
    counts=Counter();residual=Counter();degree=Counter();cycle_terms=Counter()
    paid={'empty','cycles:4','cycles:6','cycles:8','cycles:10','cycles:4,4','cycles:4,6',
          'theta:1,3,3','theta:2,2,4','theta:3,3,3','theta:2,4,4','theta:2,2,6','barbell:4,4,2','cycle4+theta133'}
    for mask in range(1<<15):
        es=selected_edges(mask);tag=category(es);counts[tag]+=1
        if tag=='vanish':continue
        degree[len(es)]+=1
        if tag.startswith('cycles:'):cycle_terms[tag]+=1
        if tag not in paid:residual[len(es)]+=1
    assert sum(degree.values())==625
    expected={'empty':1,'cycles:4':5,'cycles:6':15,'cycles:8':25,'cycles:10':8,
              'cycles:4,4':5,'cycles:4,6':5,'theta:1,3,3':5,'theta:2,2,4':10,
              'theta:3,3,3':10,'theta:2,4,4':30,'theta:2,2,6':30,'barbell:4,4,2':10,'cycle4+theta133':5}
    for k,v in expected.items():assert counts[k]==v,(k,counts[k],v)
    assert dict(residual)=={9:50,10:15,11:150,12:155,13:75,14:15,15:1},residual
    error=sum(v*Q(1,2)**(e-4) for e,v in residual.items())
    assert error==Q(7651,2048) and 5-error==Q(2589,2048)
    # Check all induced graphs, not just chosen representatives.
    sigs={};multiplicities=Counter()
    for mask in range(1<<10):
        es=[e for e in EDGES if all(mask>>x&1 for x in e)]
        c=polynomial(es);sig=tuple(sorted(c.items()));multiplicities[sig]+=1
        if sig not in sigs:sigs[sig]=(mask,c)
    assert len(sigs)==10 and sum(multiplicities.values())==1024
    certificates=[]
    for sig,(mask,c) in sigs.items():
        ray=negative_ray(c)
        record={'representative_vertex_mask':mask,'number_of_vertex_subsets':multiplicities[sig],
                'rank_two_coefficients':[[e,k,v] for (e,k),v in sorted(c.items())]}
        if not ray:
            record.update(kind='constant_polynomial',value=1)
        else:
            n=max(a for a,b in ray);m=max(b for a,b in ray)
            bc=bernstein(ray,n,m)
            assert min(bc.values())>=0
            assert reconstruct(bc,n,m)==ray
            record.update(kind='negative_ray_bernstein',degrees=[n,m],minimum=str(min(bc.values())),
                          coefficients=[[i,j,str(v)] for (i,j),v in bc.items()])
        certificates.append(record)
    # A rank-four hierarchical example with genuinely nonzero cubic moments.
    p=[Q(1,10),Q(1,5),Q(3,10),Q(2,5)]
    f0=list(map(Q,[7,7,-3,-3]));f1=list(map(Q,[2,-1,0,0]));f2=list(map(Q,[0,0,4,-3]))
    lam=[-Q(1,10),-Q(23,500),-Q(67,400)]
    fs=[f0,f1,f2]; norms=[sum(p[i]*f[i]**2 for i in range(4)) for f in fs]
    w=[[Q(1)+sum(l*f[i]*f[j]/norm for l,f,norm in zip(lam,fs,norms)) for j in range(4)] for i in range(4)]
    regular(w,p)
    assert [eigenvalue(w,p,f) for f in fs]==lam
    mixed=sum(p[i]*f0[i]*f1[i]**2 for i in range(4));skew=sum(p[i]*f1[i]**3 for i in range(4))
    assert mixed==Q(21,5) and skew==Q(3,5)
    t=weighted_density(w,p);assert t>1
    # The universal theta payment, in exact arithmetic on this rank-four example.
    u=[[x-1 for x in row] for row in w];u2=matmul(u,u,p);u3=matmul(u2,u,p)
    s6=moment(u3,u3,p)
    theta=moment(u,[[x*x for x in row] for row in u3],p)
    A=moment(w,[[x*x for x in row] for row in u3],p)
    assert 15*s6+5*theta==10*s6+5*A and A>=0
    # A separate sign-extension example (rank four; overlapping amplitudes).
    pz=[Q(1,3),Q(2,3)];base=[[Q(3,5),Q(6,5)],[Q(6,5),Q(9,10)]]
    states=list(product(range(2),(-1,1),(-1,1)))
    weights=[pz[z]/4 for z,e,h in states]
    a1=[Q(1),Q(2)];a2=[Q(2),Q(1)];l1=-Q(1,100);l2=Q(1,80)
    lift=[[base[z][zz]+l1*a1[z]*a1[zz]*e*ee+l2*a2[z]*a2[zz]*h*hh
           for zz,ee,hh in states] for z,e,h in states]
    regular(lift,weights)
    tb=weighted_density(base,pz);tl=weighted_density(lift,weights)
    tau=[l1*sum(pz[z]*a1[z]**2 for z in range(2)),l2*sum(pz[z]*a2[z]**2 for z in range(2))]
    spec={j:sum(x**j for x in tau) for j in (4,6,8,10)};b=Q(3,5)
    lower=(5*b**11*spec[4]+15*b**9*spec[6]+25*b**7*spec[8]+8*b**5*spec[10]
           +5*b**7*spec[4]**2+5*b**5*spec[4]*spec[6])
    assert tl-tb>=lower>0
    # Continuity of the new local bound: rational test kernels in its range.
    local=[]
    for scale in (Q(1,4),Q(1,2),Q(3,4)):
        wl=[[1+scale*(x-1) for x in row] for row in w]
        delta=max(abs(x-1) for row in wl for x in row)
        if delta>Q(1,2):continue
        tlc=weighted_density(wl,p);s4=sum((scale*x)**4 for x in lam);s6c=sum((scale*x)**6 for x in lam)
        low=1+Q(2589,2048)*s4+10*s6c
        assert tlc>=low
        local.append({'scale':str(scale),'delta':str(delta),'density':str(tlc),'bound':str(low)})
    # Symmetrization is not a reduction in the needed direction.
    fullpoly=polynomial(EDGES)
    def eval_rank2(lam,z):
        return sum(v*lam**e*z**k for (e,k),v in fullpoly.items())
    original=eval_rank2(-Q(1,2),Q(1,2))
    symmetrized=eval_rank2(-Q(1,2),Q(0))
    assert symmetrized>original>1
    output={'status':'ALL_EXACT_CHECKS_PASS','analytic_proof_assistant_checked':False,
            'edge_subsets_checked':1<<15,'surviving_edge_subsets':625,
            'classification_counts':dict(sorted(counts.items())),
            'surviving_counts_by_edges':dict(sorted(degree.items())),
            'unpaid_remainder_counts':dict(sorted(residual.items())),
            'half_radius_error':str(error),'half_radius_fourth_coefficient':str(5-error),
            'induced_vertex_subsets_checked':1024,'distinct_induced_polynomials':len(sigs),
            'induced_certificates':certificates,
            'hierarchical_example':{'weights':list(map(str,p)),'kernel':[[str(x) for x in row] for row in w],
              'nonconstant_eigenvalues':list(map(str,lam)),'mixed_moment_unscaled':str(mixed),'skew_unscaled':str(skew),'density':str(t)},
            'sign_extension_example':{'base_density':str(tb),'lift_density':str(tl),'guaranteed_increment':str(lower),'increment':str(tl-tb),'new_eigenvalues':list(map(str,tau))},
            'local_exact_checks':local,
            'symmetrization_obstruction':{'r':'1/2','original_density':str(original),'symmetrized_density':str(symmetrized),'increase':str(symmetrized-original)},
            'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    (ROOT/'checks.json').write_text(json.dumps(output,indent=2)+'\n')
    print('ALL_EXACT_CHECKS_PASS')
    print('32768 edge subsets; 625 surviving subsets; 1024 induced vertex subsets; 10 induced polynomials.')
    print('Residual counts:',dict(sorted(residual.items())))
    print('Half-radius coefficient:',5-error)
    print('Rank-four examples, mixed moments, theta payment, sign-extension bound: PASS')

if __name__=='__main__':main()
