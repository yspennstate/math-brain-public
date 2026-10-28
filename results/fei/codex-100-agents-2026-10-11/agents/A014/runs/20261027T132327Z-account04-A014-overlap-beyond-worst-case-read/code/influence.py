from pathlib import Path
source=Path(__file__).with_name('check.py').read_text(encoding='utf-8')
exec(compile(source.split('graphfixtures=0;graphatoms=0')[0],str(Path(__file__).with_name('check.py')),'exec'))

cases=0;physicalinputs=0
for n in ([2,3] if PILOT else [2,3,4]):
    universe=list(combinations(range(n),2))
    for mask in range(1,1<<len(universe)):
        edges=[e for j,e in enumerate(universe) if mask>>j&1]
        sets=[x for x in range(1<<n) if not any((x>>u&1) and (x>>v&1) for u,v in edges)]
        p=[F(sum(x>>j&1 for x in sets),len(sets)) for j in range(n)]
        t=[1-2*x for x in p];s=F(len(sets),1<<n);v=4*s*(1-s)
        C=[int(x in sets) for x in range(1<<n)]
        I=F(sum(C[x]!=C[x^(1<<j)] for x in range(1<<n) for j in range(n)),1<<n)
        ck(all(z>=0 for z in t));ck(I==2*s*sum(t));physicalinputs+=1<<n
        for u,w in edges:ck(p[u]+p[w]<=F(2,3))
        for weights in weightings(n,edges):
            W=sum(weights.values());loads=[sum((w for e,w in weights.items() if j in e),F(0)) for j in range(n)]
            paid=sum(z*w for z,w in zip(t,loads))
            ck(F(2,3)*W<=paid<=sum(t));ck(I>=F(4,3)*s*W);ck(v*W<=3*I)
            total=sum((raw({j for j in range(n) if a>>j&1},n,weights) for a in range(1<<n)),F(0))
            ck(v*lg(total)[1]<F(9,16)*I);cases+=1

for m in range(1,129):
    a=F(3,4)**m;v=4*a*(1-a);I=F(4*m,3)*a
    ck(v*m/I==3*(1-a));ck(v*m<3*I)
ck(F(275,784)<F(3,8));ck(F(275,784)*F(3,2)<F(9,16))
out={'helper_version':'A014-fractional-normalizer-influence-v1','mode':'pilot' if PILOT else 'main','graph_activity_fixtures':cases,'actual_truth_inputs':physicalinputs,'matching_sharpness_controls':128,'assertions':CHECKS,'elapsed_seconds':time.monotonic()-START}
(RUN/'out'/('influence_pilot.json' if PILOT else 'influence.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps(out))
