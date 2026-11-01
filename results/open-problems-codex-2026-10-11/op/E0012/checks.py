import itertools, json, pathlib
from fractions import Fraction as F
rank = {2: 0, 0: 1, 1: 2}
def update(kind, source, target):
    if kind == 'birth1' and source == 1 and target == 0: return 1
    if kind == 'birth2' and source == 2 and target == 0: return 2
    if kind == 'toxin' and source == 1 and target == 2: return 0
    if kind == 'death': return 0
    return target
count = 0
for kind in ('birth1', 'birth2', 'toxin', 'death'):
    for s,t,S,T in itertools.product((2,0,1), repeat=4):
        if rank[s] <= rank[S] and rank[t] <= rank[T]:
            assert rank[update(kind,s,t)] <= rank[update(kind,S,T)]
            count += 1
N=4
configs = list(itertools.product((0,1),repeat=N))
def generator(config, obs, a):
    ans=F(0)
    for i in range(N):
        c=list(config)
        if c[i]:
            c[i]=0; rate=F(1)
        else:
            c[i]=1; rate=a*F(config[(i-1)%N]+config[(i+1)%N],2)
        ans += rate*(obs(c)-obs(config))
    return ans
for a in (F(1,2),F(2),F(3)):
    for c in configs:
        pair=lambda v:v[0]*v[1]
        expected=-2*c[0]*c[1]+a/F(2)*((1-c[0])*c[1]*(c[1]+c[3])+(1-c[1])*c[0]*(c[0]+c[2]))
        assert generator(c,pair,a)==expected
for D in (2,4,6,8):
    for a in (F(0),F(1,2),F(1),F(D,D-1)):
        c=a*D/(2*(D+a))
        k=(D-(D-1)*a)/(D+a)
        assert F(0)<=c<=F(1,2)
        assert -a+2*c*(1+a/D)==0
        assert a-1-2*c*a/D==-k
table=[[F(31,96),F(1,12),F(3,32)],[F(1,12),F(7,60),F(1,20)],[F(3,32),F(1,20),F(17,160)]]
assert list(map(sum,table))==[F(1,2),F(1,4),F(1,4)]
assert all(table[i][j]==table[j][i] and table[i][j]>0 for i in range(3) for j in range(3))
assert table[1][1]+table[1][2]==(1-F(1,3))*F(1,4)
assert table[2][2]+(1+F(5,8))*table[1][2]==(1-F(1,4))*F(1,4)
result={'monotone_comparisons_checked':count,'pair_generator_configurations_checked':len(configs)*3,'exponential_certificate_parameters_checked':16,'positive_pair_table_balance_checked':True,'arithmetic':'exact rational','scope':'finite checks of local maps, generator identity, exponential certificate and moment feasibility; not an infinite-volume proof'}
pathlib.Path('checks_result.json').write_text(json.dumps(result,indent=2),encoding='utf8')
print(json.dumps(result))
