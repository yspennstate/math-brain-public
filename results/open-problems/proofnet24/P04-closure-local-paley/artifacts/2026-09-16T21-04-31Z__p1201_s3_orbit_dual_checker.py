from fractions import Fraction

P = 1201
DEN = 2
T = 21
CERT_CODE = "88995779a96a75aa59888676878755866868666978888666999977976a597a8678986679577778846746856a99686787644657677878a584b686877b758a97847759776777c767889876258368887a477576747743587a86b9964b887887958677849758a999877875883a78767766a8887a968597998a7658a6b974766976787567767779886959566955567a4a77876866796777967767888878667a679a98877486694988a6865699a69886997886575a4548679557268776688969a94656a9a795578d5997498774a9666989486686875756a7879a658696786876777967866996787a88767788677557877767b76876798888787a79857587b788567677676569749696a69a78777a7546968979596879957878a6599a47587568777b87a86a97b89986876698698a6865496688667777975776469579759769568a77666878566885ba698888866c6466878949868664596875a587a779758b86568a746667886c5784a867774879688986a75879595579b68666885779977646ba669787a7887849a75838788987987895757797997846687b8766a87857a8877789a79879866a54668896857a67786677694694786576795386878677878577a868a8856897aa767567a86a67778787876659a7aa878459966768897786799a5766839946767b97478a68987885679776877698456b465a8a87567a92a89779386a767768a67779588759566659675ac56897788748566987899889364b485855989867787669a586b886697868985884aa96978687748968878786978a598a7388789767676978686778678b6557a867b85877946686b56837883968959769766776a958896a76758a5587b696775766875987896888b4887888665a74867697666658958997873859976986676a6777647486b586578688986b5a5886645778a78a5686898a98a978687676788a59656879667796a89467597a9698a498a775655877767a67777986675988a692768678a77879776763876a6677988a4a6898367767776c77675b4998b58684697b6956775676887a8679657968768667884a889857787a76876657968875a9768586779897675979897998767aa594884798a7a877678975998676668537978698764797a7467a6887868998567998a5879a879689778877589877897468894687847686667a76968557c875768476576697858587799686667765a97977695876749578a557a699789a89587799877a778565667766775ba686896775868a787858776878886d788666a7a9889a9553796a867656588789a677898996878769888627987894947b7b4857955a36797886a676699976798897787777948796655978796974696647865663877698748a47687766877874867777a79787a86689777799776579688866785859857577788756888477968a89897899795565a74b99778686877aa97789888587968667989788b66886557889779778bb775675a8977a6755887768536779886868456786566567985739a7777597886689a777748798765787796497599369a96479678886757566799376c89768988978a7769676aa9564598968878b796549b557676b674897b584876aa8875478677758a76aa967a77769687a8978877995b78a668a75ba9376876baa6977858589876a8a99877975875a8997658656869b67a78596698774a9a6b9976869a569a877858898888776777976759586678668667a7786864859676589a9668767668987889786766887876495957778a787a57779758886688966a87486876a588986b78886898667a8767a776a65995698966679877a97865b667787597769597977699864779486774a796a6755768467869794989c8987567796786773757b768a9859666575759798759a8889a8a67567a897766996747676777697b8678775598a957958799686786978786778776557c6796989586879a969887869577a7595669699586887889575787876587797597779879586688688a868477668a7868788779766696958a658a8888956585a8a88878a66568a6a7878777585698488969787a8988666b5a7487566986768767956896787979b57a584856977569776a7778a6667797869796a669a86b89669a788979769847776797786a7a689a5884779987889a5869758697a69745a76695977888878662956b076698595b8698687876a657a7869986879777959b74578877793887669669779778668669877977797a7969768879547878876975aa55a856569879786564786987a8677867749a68b677877b843887697766686957757b676a6859653a99777a8888666687646b5a69869aa6887477b579596689b5579287746889968665a955785a877589996559758968a86898889658758a74b69a664869989396858547686979958865666685a63576666689895669899896b69879968594574748a79687467984a7474887476676778976a9a9984956678599579a787895965885a5667aa6756787aa567b6aab786a59749975768897866768768697768878688869889778858888a688998b96877759469687877667487678796aa4676776868b77656b7647688a887b995667799766968877696836a888699a8277879a58776"
CERT = [int(ch,16)-9 for ch in CERT_CODE]
assert len(CERT)==3770

def legendre(a, p):
    a %= p
    if a == 0:
        return 0
    return 1 if pow(a, (p-1)//2, p) == 1 else -1

def is_prime(n):
    if n < 2:
        return False
    d = 2
    while d*d <= n:
        if n % d == 0:
            return False
        d += 1 if d == 2 else 2
    return True

assert is_prime(P)
assert P % 4 == 1

V=[x for x in range(P)
   if x not in (0,1) and legendre(x,P)==1 and legendre(x-1,P)==1]
idx={x:i for i,x in enumerate(V)}
n=len(V)
assert n==(P-5)//4==299

A=[[0]*n for _ in range(n)]
for i,x in enumerate(V):
    for j in range(i+1,n):
        if legendre(x-V[j],P)==1:
            A[i][j]=A[j][i]=1

r=tuple(idx[(1-x)%P] for x in V)
s=tuple(idx[pow(x,-1,P)] for x in V)
ident=tuple(range(n))

def compose(g,h):
    return tuple(g[h[i]] for i in range(n))

G={ident}
changed=True
while changed:
    changed=False
    for g in list(G):
        for h in (r,s):
            for q in (compose(g,h),compose(h,g)):
                if q not in G:
                    G.add(q); changed=True
G=sorted(G)
assert len(G)==6

def perm_order(g):
    h=ident
    for k in range(1,7):
        h=compose(g,h)
        if h==ident:
            return k
    raise AssertionError("bad group element")
orders={g:perm_order(g) for g in G}
assert sorted(orders.values())==[1,2,2,2,3,3]
sgn={g:(1 if orders[g] in (1,3) else -1) for g in G}

for g in G:
    for i in range(n):
        for j in range(i+1,n):
            assert A[g[i]][g[j]]==A[i][j]

unseen={(i,j) for i in range(n) for j in range(i+1,n) if not A[i][j]}
pair_orbits=[]
while unseen:
    seed=min(unseen)
    orb=set()
    for g in G:
        a,b=g[seed[0]],g[seed[1]]
        if a>b: a,b=b,a
        orb.add((a,b))
    for i,j in orb:
        assert i<j and A[i][j]==0
        unseen.discard((i,j))
    pair_orbits.append(tuple(sorted(orb)))
pair_orbits.sort(key=lambda o:o[0])
assert not unseen
assert len(pair_orbits)==3770
assert len(CERT)==3770
assert sorted({len(o) for o in pair_orbits})==[3,6]

# Integer form M=DEN*(T I-B), where B is edge-fixed and
# B_ij=CERT[k]/DEN on the k-th canonical nonedge S3 orbit.
M=[[0]*n for _ in range(n)]
for i in range(n):
    M[i][i]=DEN*(T-1)
for i in range(n):
    for j in range(i+1,n):
        if A[i][j]:
            M[i][j]=M[j][i]=-DEN
for num,orb in zip(CERT,pair_orbits):
    for i,j in orb:
        M[i][j]=M[j][i]=-num

for g in G:
    for i in range(n):
        for j in range(n):
            assert M[g[i]][g[j]]==M[i][j]

unseen_v=set(range(n))
vertex_orbits=[]
while unseen_v:
    seed=min(unseen_v)
    orb={g[seed] for g in G}
    unseen_v-=orb
    vertex_orbits.append(tuple(sorted(orb)))
vertex_orbits.sort(key=lambda o:o[0])
sizes=sorted(len(o) for o in vertex_orbits)
assert sizes==[2,3]+[6]*49

triv=[]
sign=[]
std=[]
for orb in vertex_orbits:
    base=min(orb)
    triv.append({i:1 for i in orb})
    if len(orb)==6:
        point_to_sign={}
        for g in G:
            y=g[base]
            assert y not in point_to_sign
            point_to_sign[y]=sgn[g]
        sign.append(point_to_sign.copy())
        even=sorted(i for i in orb if point_to_sign[i]==1)
        odd=sorted(i for i in orb if point_to_sign[i]==-1)
        assert len(even)==len(odd)==3
        std.extend([
            {even[0]:1,even[2]:-1},
            {even[1]:1,even[2]:-1},
            {odd[0]:1,odd[2]:-1},
            {odd[1]:1,odd[2]:-1},
        ])
    elif len(orb)==3:
        a,b,c=orb
        std.extend([{a:1,c:-1},{b:1,c:-1}])
    elif len(orb)==2:
        a,b=orb
        sign.append({a:1,b:-1})
    else:
        raise AssertionError("unexpected vertex orbit")

assert len(triv)==51
assert len(sign)==50
assert len(std)==198
assert len(triv)+len(sign)+len(std)==n

def dot_sparse(u,v):
    return sum(c*v.get(i,0) for i,c in u.items())

for fam1,fam2 in ((triv,sign),(triv,std),(sign,std)):
    for u in fam1:
        for v in fam2:
            assert dot_sparse(u,v)==0

def bilinear(u,v):
    return sum(ci*M[i][j]*cj for i,ci in u.items() for j,cj in v.items())

for fam1,fam2 in ((triv,sign),(triv,std),(sign,std)):
    for u in fam1:
        for v in fam2:
            assert bilinear(u,v)==0

def gram(fam):
    q=len(fam)
    Gm=[[0]*q for _ in range(q)]
    for i in range(q):
        for j in range(i,q):
            z=bilinear(fam[i],fam[j])
            Gm[i][j]=Gm[j][i]=z
    return Gm

def bareiss_positive(A):
    A=[row[:] for row in A]
    N=len(A)
    prev=1
    pivots=[]
    max_digits=1
    for k in range(N-1):
        piv=A[k][k]
        assert piv>0,(k,piv)
        pivots.append(piv)
        max_digits=max(max_digits,len(str(abs(piv))))
        for i in range(k+1,N):
            aik=A[i][k]
            for j in range(k+1,N):
                num=A[i][j]*piv-aik*A[k][j]
                assert num % prev == 0
                A[i][j]=num//prev
            A[i][k]=0
        prev=piv
    last=A[N-1][N-1]
    assert last>0
    pivots.append(last)
    max_digits=max(max_digits,len(str(abs(last))))
    return min(pivots),max_digits,len(pivots)

triv_info=bareiss_positive(gram(triv))
sign_info=bareiss_positive(gram(sign))
std_info=bareiss_positive(gram(std))

margin=Fraction(4*P,9)-T*T
assert margin==Fraction(835,9)
assert margin>0

edge_count=sum(sum(row) for row in A)//2
assert edge_count==22165

print("P04-I0101-P1201-S3-ORBIT-DUAL=PASS")
print(f"p={P}")
print(f"|V2|={n}")
print(f"edges={edge_count}")
print(f"nonedge_S3_orbits={len(pair_orbits)}")
print(f"pair_orbit_size_counts=3:{sum(len(o)==3 for o in pair_orbits)},6:{sum(len(o)==6 for o in pair_orbits)}")
print(f"vertex_orbit_sizes={sizes}")
print(f"certificate_denominator={DEN}")
print(f"certificate_numerator_range={min(CERT)}..{max(CERT)}")
print(f"t={T}")
print(f"block_dimensions={len(triv)},{len(sign)},{len(std)}")
print(f"trivial_bareiss_minpivot={triv_info[0]} maxdigits={triv_info[1]} pivots={triv_info[2]}")
print(f"sign_bareiss_minpivot={sign_info[0]} maxdigits={sign_info[1]} pivots={sign_info[2]}")
print(f"standard_bareiss_minpivot={std_info[0]} maxdigits={std_info[1]} pivots={std_info[2]}")
print(f"threshold_margin_4p_over_9_minus_t2={margin}")
print("S3_INVARIANCE_AND_CROSS_BLOCKS=PASS")
print("EXACT_CERTIFICATE=PASS")
