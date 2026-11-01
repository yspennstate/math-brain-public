from pathlib import Path
helper=Path(__file__).resolve().parents[2]/'20261014T054454Z-fleet05-A014-overlap-beyond-worst-case-read/code/check.py'
source=helper.read_text(encoding='utf-8')
exec(compile(source.split("rows=[];candidates=0;sets=0;wins=")[0],str(helper),'exec'))
from profile import reference,core_characters,core_boundary
from rigorous_log import lg
def binary_bounds(interval):
    scale=1<<40
    return F(math.floor(interval[0]*scale),scale),F(math.ceil(interval[1]*scale),scale)
refs=[];pairs=0;profiles=0;max_ratio=F(0);max_tail=F(0);worst=None
for a in ([1,2] if args.pilot else [1,2,3]):
    universe=list(itertools.combinations(range(a),2))
    for b in ([3*a] if args.pilot else [3*a,3*a+1]):
        n=a+b;rho=2**a*F(3,4)**b
        ck(rho<=F(19,20)**b)
        for mask in range(1<<len(universe)):
            edges=tuple(e for j,e in enumerate(universe) if mask>>j&1)
            masses,Z,q=reference(a,b,edges);profiles+=len(q)
            ck(all(z>0 for z in masses.values()));ck(sum(math.comb(b,l)*x for (S,l),x in q.items())==1);ck(Z**4<=2**n)
            logs={key:binary_bounds(lg(1/x)) for key,x in q.items()};ln=binary_bounds(lg(n))
            for (S,l),bounds in logs.items():
                ck(bounds[1]<=F(39*n,4)+a*ln[0]*(l<a))
            local_max=F(0);local_tail=F(0)
            for truth in range(1<<(1<<a)):
                g=[(truth>>x)&1 for x in range(1<<a)];N=sum(g);c=g[0];e=core_boundary(g,a);t=core_characters(g)
                s=F(N+b,1<<n);v=4*s*(1-s);I=F(2*(e+b*(N+n-2*c)),1<<n)
                p={key:4*F(t[S]+b-2*l,1<<n)**2 for key in q for S,l in [key]}
                ck(sum(math.comb(b,l)*x for (S,l),x in p.items())==v)
                ck(sum((S.bit_count()+l)*math.comb(b,l)*x for (S,l),x in p.items())==I)
                ck(I>=n*s);ck(v/I<=F(4,n));ck(s<=F(1,2));ck(v>=F(1,2**(n-1)))
                tau=sum((math.comb(b,l)*x for (S,l),x in p.items() if l<a),F(0))
                ck(tau<=F(8,9)*s*(b+8)*rho)
                tail=(a*ln[0]*tau/I,a*ln[1]*tau/I);ck(tail[1]<=F(166,3))
                hb=binary_bounds(CE([v,1-v],[v,1-v]));lo,hi=hb
                for key,x in p.items():
                    S,l=key;weight=math.comb(b,l)*x;low,high=logs[key];lo+=weight*low;hi+=weight*high
                ck(hi<=F(298,3)*I);ck(hi<100*I);ck(hi<=(44+tail[0])*I)
                if hi/I>max_ratio:max_ratio=hi/I;worst={'a':a,'b':b,'H_edge_mask':mask,'core_truth_table':truth}
                max_tail=max(max_tail,tail[1]);local_max=max(local_max,hi/I);local_tail=max(local_tail,tail[1]);pairs+=1
            refs.append({'a':a,'b':b,'H_edge_mask':mask,'edges':edges,'Z_F':str(Z),'complete_profile_masses':{f'{S},{l}':str(x) for (S,l),x in masses.items()},'all_core_CE_over_I_upper':outward((local_max,local_max)),'all_core_tail_congestion_upper':outward((local_tail,local_tail))})
        (R/'out/checkpoint.json').write_text(json.dumps({'a':a,'b':b,'pairs':pairs,'assertions':assertions,'elapsed_seconds':time.monotonic()-start})+'\n',encoding='utf-8',newline='\n')
out={'helper_version':'A014-dominating-clique-profile-v3','mode':'pilot' if args.pilot else 'full','function_reference_pairs':pairs,'reference_graphs':len(refs),'nonempty_profiles':profiles,'assertions':assertions,'elapsed_seconds':time.monotonic()-start,'max_CE_over_I_upper':outward((max_ratio,max_ratio)),'max_tail_congestion_upper':outward((max_tail,max_tail)),'worst':worst,'references':refs}
(R/('out/pilot.json' if args.pilot else 'out/check.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps({k:v for k,v in out.items() if k!='references'}))
