"""Exact checks of the all-port rank-one attachment adjacent theorem.

Component identities, actual apex graph derivatives, direct core/spoke cycle
tests, whole uncontracted small graphs, and all backbone conditionings.
"""
from collections import defaultdict
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json
from forest_matching_negative_association_exact import canonical, terminal


def forest_records(n, edges, profile):
    records = []
    for mask in range(1 << len(edges)):
        parent = list(range(n)); weight = F(1)
        def root(u):
            while parent[u] != u: u = parent[u]
            return u
        for i, (u,v,w) in enumerate(edges):
            if mask >> i & 1:
                u,v = root(u),root(v)
                if u == v: break
                parent[u] = v; weight *= w
        else:
            sums = defaultdict(F)
            for i,x in enumerate(profile): sums[root(i)] += x
            records.append((mask,weight,list(sums.values())))
    return records


def conditioned(records, status):
    return [record for record in records
            if all(v == -1 or (record[0] >> i & 1) == v for i,v in enumerate(status))]


def mixture_parameters(records, s):
    D=Dp=Dpp=EU=EG=EU2=F(0)
    for mask,weight,rows in records:
        ds = [1+s*x for x in rows]; value = weight
        for d in ds: value *= d
        W = sum((x/(1+s*x) for x in rows),F(0))
        Wp = -sum((x*x/(1+s*x)**2 for x in rows),F(0))
        U = sum((x*x/(1+s*x) for x in rows),F(0))
        G = sum((x**3/(1+s*x)**2 for x in rows),F(0))
        D += value; Dp += value*W; Dpp += value*(W*W+Wp)
        EU += value*U; EG += value*G; EU2 += value*U*U
    U = EU/D; Gamma = EG/D+s*(EU2/D-U*U)
    log_second = Dpp/D-(Dp/D)**2
    if s:
        assert U/s-Gamma == -log_second/s >= 0
    assert U>=0 and Gamma>=0
    return D,Dp,Dpp,U,Gamma,log_second


def apex_derivatives(n, edges, profile, s):
    all_edges = edges+[(n,j,s*x) for j,x in enumerate(profile) if x]
    D=Dp=Dpp=F(0)
    for mask in range(1 << len(all_edges)):
        parent=list(range(n+1));mass=F(1);star=0
        def root(u):
            while parent[u]!=u:u=parent[u]
            return u
        for i,(u,v,w) in enumerate(all_edges):
            if mask >> i & 1:
                u,v=root(u),root(v)
                if u==v:break
                parent[u]=v;mass*=w
                star += i>=len(edges)
        else:
            D+=mass
            if s:
                Dp+=mass*star/s;Dpp+=mass*star*(star-1)/(s*s)
    return D,Dp,Dpp


def core_states(marked,rho):
    out=defaultdict(F)
    for outer in (0,1):
        if outer and not rho:continue
        parent=[0,1,2];mass=rho if outer else F(1)
        def root(u):
            while parent[u]!=u:u=parent[u]
            return u
        selected=[(0,1)] if marked&1 else []
        if marked&2:selected.append((1,2))
        if outer:selected.append((0,2))
        for u,v in selected:
            u,v=root(u),root(v)
            if u==v:break
            parent[u]=v
        else:out[canonical(tuple(root(i)for i in range(3)))]+=mass
    return dict(out)


def direct_coefficients(records, columns, rho):
    values=[F(0)]*4
    for _,weight,rows in records:
        for marked in range(4):
            frontier=core_states(marked,rho)
            for row in rows:frontier=terminal(frontier,row,columns)
            values[marked]+=weight*sum(frontier.values(),F(0))
    return values


def scalar_coefficients(parameters,columns,rho):
    D,_,_,U,Gamma,_=parameters;a,b,c=columns;s=a+b+c;l=a*b+a*c+b*c;j=a*b*c
    A=D*(1+rho+(l+rho*b*(a+c))*U+j*Gamma+s*j*U*U)
    E=D*(1+rho+c*(a+b)*U);Ff=D*(1+rho+a*(b+c)*U);C=D
    return [A,E,Ff,C]


def literal_original_graph(n,edges,profile,columns,rho):
    """Enumerates original graph including g and each marked subset."""
    unmarked=edges+[(n+i,j,a*x)for i,a in enumerate(columns)for j,x in enumerate(profile)if a*x]
    if rho:unmarked.append((n,n+2,rho))
    coeffs=[F(0)]*4;counts=[0]*4
    def root(parent,u):
        while parent[u]!=u:u=parent[u]
        return u
    def visit(index,parent,mass):
        if index<len(unmarked):
            visit(index+1,parent,mass)
            u,v,w=unmarked[index];u,v=root(parent,u),root(parent,v)
            if u!=v:
                copy=parent.copy();copy[u]=v;visit(index+1,copy,mass*w)
            return
        for marked in range(4):
            copy=parent.copy()
            for i,(u,v)in enumerate(((n,n+1),(n+1,n+2))):
                if marked>>i&1:
                    u,v=root(copy,u),root(copy,v)
                    if u==v:break
                    copy[u]=v
            else:coeffs[marked]+=mass;counts[marked]+=1
    visit(0,list(range(n+3)),F(1))
    return coeffs,counts


def main():
    cases=[
        {'name':'four_common_ports_cycle_backbone_outer_edge','n':4,
         'edges':[(0,1,F(2)),(1,2,F(3)),(2,3,F(5)),(0,3,F(7))],
         'profile':[F(1),F(2),F(3),F(4)],'columns':[F(1),F(2),F(3)],'rho':F(2),'literal':True},
        {'name':'five_common_ports_nonuniform_backbone','n':6,
         'edges':[(0,5,F(2,3)),(1,5,F(3,4)),(2,5,F(5,7)),(3,5,F(7,11)),(4,5,F(11,13)),(0,2,F(13,17)),(1,3,F(17,19))],
         'profile':[F(1,2),F(2,3),F(3,4),F(4,5),F(5,6),F(0)],
         'columns':[F(1,3),F(2,5),F(3,7)],'rho':F(0)},
        {'name':'six_common_ports_zero_middle','n':6,
         'edges':[(i,i+1,F(i+2,i+3))for i in range(5)],
         'profile':[F(i+1,i+2)for i in range(6)],'columns':[F(2),F(0),F(3)],'rho':F(0)},
        {'name':'zero_outer_triangle_strict','n':4,
         'edges':[(0,1,F(2)),(1,2,F(3)),(2,3,F(5))],
         'profile':[F(1),F(2),F(3),F(4)],'columns':[F(0),F(2),F(3)],'rho':F(7),'literal':True},
        {'name':'zero_outer_bridge_equality','n':4,
         'edges':[(0,1,F(2)),(1,2,F(3)),(2,3,F(5))],
         'profile':[F(1),F(2),F(3),F(4)],'columns':[F(0),F(2),F(3)],'rho':F(0)},
        {'name':'zero_profile_triangle','n':3,
         'edges':[(0,1,F(2)),(1,2,F(3)),(0,2,F(5))],
         'profile':[F(0)]*3,'columns':[F(1),F(2),F(3)],'rho':F(7)},
        {'name':'zero_columns_triangle','n':3,
         'edges':[(0,1,F(2)),(1,2,F(3))],
         'profile':[F(1),F(2),F(3)],'columns':[F(0)]*3,'rho':F(7),'literal':True},
    ]
    report={'arithmetic':'exact Fraction and literal union-find cycles','cases':[]}
    for case in cases:
        n,edges,profile,columns,rho=[case[key]for key in('n','edges','profile','columns','rho')]
        records=forest_records(n,edges,profile);s=sum(columns,F(0));params=mixture_parameters(records,s)
        direct=direct_coefficients(records,columns,rho);scalar=scalar_coefficients(params,columns,rho)
        assert direct==scalar
        if s:assert params[:3]==apex_derivatives(n,edges,profile,s)
        counts=None
        if case.get('literal'):
            literal,counts=literal_original_graph(n,edges,profile,columns,rho)
            assert literal==direct
        conditionings=0;smallest=None
        for status in product((-1,0,1),repeat=len(edges)):
            allowed=conditioned(records,status)
            if not sum((record[1] for record in allowed),F(0)):continue
            p=mixture_parameters(allowed,s);coeffs=direct_coefficients(allowed,columns,rho)
            assert coeffs==scalar_coefficients(p,columns,rho)
            A,E,Ff,C=coeffs;R=E*Ff-A*C;D,_,_,U,Gamma,_=p;a,b,c=columns
            assert R==D*D*(rho*(1+rho)+a*c*((1+2*rho)*U+a*c*U*U-b*Gamma))
            lower=D*D*(rho*(1+rho)+a*c*((((a+c)/s)if s else 0)+2*rho)*U+a*a*c*c*U*U)
            assert R>=lower>=0
            strict=bool(rho or (a*c and sum(profile)))
            assert (R>0)==strict
            conditionings+=1;smallest=R if smallest is None else min(smallest,R)
        report['cases'].append({'name':case['name'],'backbone_vertices':n,'backbone_edges':len(edges),
            'nonzero_common_neighbor_profiles':sum(bool(x)for x in profile),
            'positive_backbone_partial_conditionings':conditionings,
            'unconditional_D_Dprime_Dsecond_U_Gamma_logsecond':list(map(str,params)),
            'unconditional_four_marked_coefficients':list(map(str,direct)),
            'smallest_exact_Rayleigh_over_recorded_conditionings':str(smallest),
            'literal_original_graph_match':counts is not None,'literal_forest_counts_by_marked_subset':counts,
            'actual_apex_derivative_identity':bool(s),'all_scalar_difference_and_strictness_checks':True})
        print(case['name'],'PASS;',conditionings,'backbone conditionings.',flush=True)
    Path(__file__).with_name('forest_adjacent_rank_one_attachment_all_ports_exact_results.json').write_text(json.dumps(report,indent=2)+'\n')
    print('All all-port adjacent attachment checks PASS.',flush=True)


if __name__=='__main__':main()
