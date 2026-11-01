import math, random, json

EPS=2**-12
ETA=1/4
B=math.sqrt((ETA-EPS)/2)
A0=2*math.sqrt(EPS)
THETA=A0/B
Q=4*THETA**2.5

def coeff(p):
    return 136*p*(2**(p/2))*B**(-p)

grid=[2.5+0.5*i/100000 for i in range(100001)]
mx=max(coeff(p) for p in grid)
C0=26151
assert mx<C0

# Physical scaling matters: on Q_h the stopped hitting estimate carries
# the dyadic base frequency 2^h.  Weight a center j by w_j=2^{-j}.
# Candidate new blocks have h-j in {-3,-2,2,3}, so 2^{h-j}<=8.
DEN=1-4*Q
QW=Q/DEN
CW=8*C0/DEN
CWCRIT=CW*math.e**2/9
CWSMALL=CW*(0.25**-1.5)*math.e**2

# Three-block packet duration.  P_j has lower spectral scale >=2^{j-1}
# and condition ratio <=8, hence the passive seed clock is O(2^{-j}).
C=math.sqrt(1-ETA)
DSEED=8*math.log(2/C)
DINPUT=16*(8**1.5)*C**(-3)
MDUR=DSEED*(1+4*QW)
JDUR=DSEED*4*CWCRIT+DINPUT

def packet(j): return {j-1,j,j+1}
def mass(th,inds): return sum(th[i] for i in inds)

random.seed(20260920)
fails=[]
for _ in range(20000):
    j=random.randint(3,17)
    d=random.choice([-2,-1,1,2]); k=j+d
    Pj,Pk=packet(j),packet(k)
    inter=sorted(Pj&Pk); new=sorted(Pk-Pj); old=sorted(Pj-Pk)
    rest=[i for i in range(21) if i not in Pj|Pk]
    lo=1-ETA-EPS
    hi=min(1-ETA,1-EPS)
    x=lo+(hi-lo)*random.random()
    oldm=1-ETA-x
    newm=1-EPS-x
    rem=1-(x+oldm+newm)
    th=[0.0]*21
    for inds,total in [(inter,x),(old,oldm),(new,newm),(rest,max(rem,0.0))]:
        if inds:
            ws=[random.random()+1e-9 for _ in inds]; s=sum(ws)
            for idx,w in zip(inds,ws): th[idx]+=total*w/s
    if mass(th,Pk-Pj)+1e-10<ETA-EPS:
        fails.append((j,k,mass(th,Pj),mass(th,Pk),mass(th,Pk-Pj))); break

weight_ratio=0
cand_scale_ratio=0
for j in range(3,30):
    for d in [-2,-1,1,2]:
        k=j+d
        weight_ratio=max(weight_ratio,2**(-k)/2**(-j))
        for h in {j-3,j-2,j+2,j+3}:
            if h>=0:
                cand_scale_ratio=max(cand_scale_ratio,2**h/2**j)

errs=[]
for _ in range(5000):
    T=10**random.uniform(-3,3); R=10**random.uniform(-3,3); J=10**random.uniform(-3,3)
    p=random.uniform(2.5,2.999)
    rho=T*R**3/J
    lhs=R**(-p)*T**(1-p/3)*J**(p/3)
    rhs=(J/R**3)*rho**(1-p/3)
    errs.append(abs(lhs-rhs)/max(1,abs(lhs),abs(rhs)))

out={
"eps":EPS,"eta":ETA,"b":B,"a":A0,"theta":THETA,"q":Q,
"uniform_unweighted_block_coeff_max":mx,
"den_1_minus_4q":DEN,
"weighted_passive_ratio_q_over_den":QW,
"weighted_active_prefactor":CW,
"weighted_active_critical_constant":CWCRIT,
"weighted_active_smallrho_constant":CWSMALL,
"packet_seed_duration_constant":DSEED,
"packet_cubic_input_duration_constant":DINPUT,
"duration_initial_weight_constant":MDUR,
"duration_critical_input_constant":JDUR,
"max_next_center_weight_ratio":weight_ratio,
"max_candidate_scale_ratio":cand_scale_ratio,
"geometry_fail":fails,
"max_scaling_rel_error":max(errs)
}
print(json.dumps(out,indent=2))
assert Q<0.00931
assert DEN>0.96
assert QW<0.009662
assert CW<217294
assert CWCRIT<178399
assert CWSMALL<12844726
assert DSEED<6.696
assert DINPUT<557.3951
assert MDUR<6.955
assert JDUR<4778729
assert weight_ratio==4
assert cand_scale_ratio==8
assert not fails
assert max(errs)<1e-12
print("CHECK_PASS")
