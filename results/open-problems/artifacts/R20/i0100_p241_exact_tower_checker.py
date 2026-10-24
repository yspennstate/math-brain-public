#!/usr/bin/env python3
"""
R20 / I0100 p=241 exact primal/dual certificate checker.
Afonso S. Bandeira, Randomstrasse 101 (2025), Conjecture 26.

Target: T_p = theta(complement G_{p,1}), standard Lovasz theta, where
G_{p,1} is the graph induced by the Paley graph on the neighbors of 0.

The certificate is generated and checked with exact arithmetic in
 K0 = Q(gamma), gamma=2*cos(pi/30), deg 8,
using K=K0(alpha), alpha^2=gamma+2, alpha=2*cos(pi/60).
Every variable is u+alpha*v.  The 31x31 degree-16 system thereby becomes an
exact 62x62 degree-8 system.  Signs are certified by rational interval
arithmetic: gamma is isolated as the largest real root of its exact degree-8
minimal polynomial, and alpha=sqrt(gamma+2) is enclosed between explicitly
checked rational square bounds.

Run:
  python checker.py primal
  python checker.py dual
Each mode verifies its objective against the same exact coefficient pair.
"""
import sys, sympy as sp

P=241; N=120
NONEDGE=[5,6,11,12,13,14,16,19,23,27,28,30,32,33,34,36,37,39,40,41,42,43,45,47,48,49,52,53,55,57]
SUPPORT=[0,1,2,4,5,6,10,11,12,13,14,15,16,19,24,28,29,31,33,34,35,38,39,41,45,47,49,50,54,58,60]
EU=[
'19020133972918522252893028187000382061422509411606853691817809991669536074293524557993872799/128332665673447785628777308363792433173957306174371515423393082395084811925736203800539711180',
'935140504562567652944045410339432959005154436026087637655336416632710390600785247945728358/32083166418361946407194327090948108293489326543592878855848270598771202981434050950134927795',
'-24422946095345765260275497585726922516464610805446940857857529000956127799979773927767168295/25666533134689557125755461672758486634791461234874303084678616479016962385147240760107942236',
'-56825121464026271271963355822281055146879328320583360465298791003463536415570259738568771333/384997997020343356886331925091377299521871918523114546270179247185254435777208611401619133540',
'104898129883016849430955145156811289008822116284524964168922553576056054764480867645425038911/64166332836723892814388654181896216586978653087185757711696541197542405962868101900269855590',
'91310656392170122214803453093395782148109335111544123206260817381063261448389656324411930261/384997997020343356886331925091377299521871918523114546270179247185254435777208611401619133540',
'-40083261089896449776317333902478365820274937655713370668929537925337364930339530876040536447/64166332836723892814388654181896216586978653087185757711696541197542405962868101900269855590',
'-31897173537428165196683943274129142564528903594065482198166362003798936925192818570886527863/384997997020343356886331925091377299521871918523114546270179247185254435777208611401619133540']
EV=[
'-1864277140112408220323654469984793348419521731002866836653067796816655205075296551682102833/25666533134689557125755461672758486634791461234874303084678616479016962385147240760107942236',
'-7372645253675907746192161112672767882536607152558085890523942649765763479470146239495730127/384997997020343356886331925091377299521871918523114546270179247185254435777208611401619133540',
'99153608506054912334172225622161898137904833167146567411167432471034044941144484984629634391/192498998510171678443165962545688649760935959261557273135089623592627217888604305700809566770',
'1290093715094150283318777312208181827731905353489481126020598614840141473190095040149412489/25666533134689557125755461672758486634791461234874303084678616479016962385147240760107942236',
'-90703706244464613422626843963422766317061984134832619314915114267360524632063053998134854378/96249499255085839221582981272844324880467979630778636567544811796313608944302152850404783385',
'-8578382679744475154010024835456065390451358495865170792547525679455616288425719722908455164/96249499255085839221582981272844324880467979630778636567544811796313608944302152850404783385',
'65584924207569057697384396239295701207431492378647967757551508888892062541789224353682377909/192498998510171678443165962545688649760935959261557273135089623592627217888604305700809566770',
'54893229395229718642479261657766493745623637330209917695564465106864319394860768415583246847/384997997020343356886331925091377299521871918523114546270179247185254435777208611401619133540']
K=sp.QQ.algebraic_field(2*sp.cos(sp.pi/30)); g=K.unit
assert K.ext.minpoly.degree()==8

def same(x,L): return [sp.Rational(c) for c in x.to_list()]==[sp.Rational(s) for s in L]

# exact cos pair
E=[K.zero]*61; O=[K.zero]*60
E[0]=2*K.one; E[1]=g
for r in range(1,60): E[r+1]=g*E[r]-E[r-1]
O[0]=K.one; O[1]=g-K.one
for r in range(1,59): O[r+1]=g*O[r]-O[r-1]
def cp(k):
    k%=N
    if k>N//2: k=N-k
    return (E[k//2]/2,K.zero) if k%2==0 else (K.zero,O[(k-1)//2]/2)

def gauss(A,b):
    n=len(A); M=[A[i][:]+[b[i]] for i in range(n)]
    for j in range(n):
        q=next(i for i in range(j,n) if M[i][j]!=K.zero)
        M[j],M[q]=M[q],M[j]
        inv=K.one/M[j][j]; M[j]=[x*inv for x in M[j]]
        for i in range(n):
            if i==j: continue
            f=M[i][j]
            if f!=K.zero: M[i]=[M[i][k]-f*M[j][k] for k in range(n+1)]
    return [M[i][-1] for i in range(n)]

def solve(C,B):
    m=len(C); A=[]; b=[]
    for i in range(m):
        row=[K.zero]*(2*m)
        for j,(cu,cv) in enumerate(C[i]):
            row[j]=cu; row[m+j]=(g+2*K.one)*cv
        A.append(row); b.append(B[i][0])
    for i in range(m):
        row=[K.zero]*(2*m)
        for j,(cu,cv) in enumerate(C[i]):
            row[j]=cv; row[m+j]=cu
        A.append(row); b.append(B[i][1])
    x=gauss(A,b); return x[:m],x[m:]

# exact target-embedding interval for gamma
def qr(q): return sp.Rational(int(q.numerator),int(q.denominator))
X=sp.Symbol('x')
MP=sp.Poly.from_list([qr(q) for q in K.mod.to_list()],gens=X)
GI=max((I for I,m in MP.intervals(eps=sp.Rational(1,10**60))),key=lambda I:I[0])
# rational enclosure alpha in (1.9972590695,1.9972590696); certify via gamma interval.
AL=sp.Rational(19972590695,10**10); AU=sp.Rational(19972590696,10**10)
assert AL>0 and AL*AL < GI[0]+2 and AU*AU > GI[1]+2

def mul(I,J):
    a,b=I; c,d=J; z=(a*c,a*d,b*c,b*d); return min(z),max(z)
def evalk(z):
    I=(sp.Rational(0),sp.Rational(0))
    for c in z.to_list():
        I=mul(I,GI); q=qr(c); I=(I[0]+q,I[1]+q)
    return I
def signpair(u,v):
    if u==K.zero and v==K.zero: return 0
    U=evalk(u); V=evalk(v)
    A=mul((AL,AU),V); T=(U[0]+A[0],U[1]+A[1])
    if T[0]>0: return 1
    if T[1]<0: return -1
    raise AssertionError(("interval too wide",T))

def addprod(acc, c, x):
    au,av=acc; cu,cv=c; u,v=x
    return (au+cu*u+(g+2*K.one)*cv*v, av+cv*u+cu*v)

def numpair(u,v):
    gg=float(sp.N(K.to_sympy(g),30)); aa=(gg+2)**0.5
    return float(sp.N(K.to_sympy(u),30))+aa*float(sp.N(K.to_sympy(v),30))

def check_source():
    assert sp.isprime(P) and P%4==1
    # derive the local circulant nonedge representatives from finite-field definition
    fs=[]; x=P-1; d=2
    while d*d<=x:
        if x%d==0:
            fs.append(d)
            while x%d==0: x//=d
        d+=1
    if x>1: fs.append(x)
    root=next(a for a in range(2,P) if all(pow(a,(P-1)//q,P)!=1 for q in fs))
    a=pow(root,2,P); Q={x*x%P for x in range(1,P)}
    vals=[pow(a,j,P) for j in range(N)]
    S={d for d in range(1,N) if (vals[d]-1)%P in Q}
    got=[d for d in range(1,N//2+1) if d not in S]
    assert got==NONEDGE

def primal():
    C=[[(K.one,K.zero) for _ in SUPPORT]]
    B=[(K.one,K.zero)]
    for d in NONEDGE:
        C.append([cp(m*d) for m in SUPPORT]); B.append((K.zero,K.zero))
    U,V=solve(C,B); assert same(U[0],EU) and same(V[0],EV)
    assert all(signpair(u,v)>0 for u,v in zip(U,V))
    # independent residual check
    for row,b in zip(C,B):
        s=(K.zero,K.zero)
        for c,x in zip(row,zip(U,V)): s=addprod(s,c,x)
        assert s==b
    print("PRIMAL exact PASS; positive_weights=31")
    print("objective_numeric=",N*numpair(U[0],V[0]))

def dual():
    C=[]; B=[]
    for m in SUPPORT:
        C.append([(K.one,K.zero)]+[cp(m*d) for d in NONEDGE])
        B.append((K.one if m==0 else K.zero,K.zero))
    U,V=solve(C,B); assert same(U[0],EU) and same(V[0],EV)
    sl=[]
    for m in range(N):
        s=(U[0],V[0])
        for d,u,v in zip(NONEDGE,U[1:],V[1:]): s=addprod(s,cp(m*d),(u,v))
        if m==0: s=(s[0]-K.one,s[1])
        assert signpair(*s)>=0; sl.append(s)
    assert all(sl[m]==(K.zero,K.zero) for m in SUPPORT)
    print("DUAL exact PASS; nonnegative_slacks=120 zero_slacks=",sum(s==(K.zero,K.zero) for s in sl))
    print("objective_numeric=",N*numpair(U[0],V[0]))
    print("covered_before=[5,13,17,29,41,181]")
    print("covered_after=[5,13,17,29,41,181,241]")
    print("largest_exact_prime=241")

if __name__=="__main__":
    check_source()
    if len(sys.argv)!=2 or sys.argv[1] not in {'primal','dual'}: raise SystemExit("primal|dual")
    primal() if sys.argv[1]=='primal' else dual()
