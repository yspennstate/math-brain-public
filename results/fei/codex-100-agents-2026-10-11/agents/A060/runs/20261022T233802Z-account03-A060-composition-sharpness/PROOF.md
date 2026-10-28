# The exterior density logarithm has sharp leading coefficient one

Rung: analytic proof with exact Boolean and rational certificates; independent review pending. Full FEI remains OPEN.
All entropies are in bits; ln denotes natural logarithm. The claim concerns the
ORIGINAL fine selector reserve at an actual physical query, including both full
physical child entropies. It does not pay arbitrary inherited or terminal entropy.

## 1. Geometry and exact quantities

Let C be an indicator on an exterior uniform cube, c=E C, 0<c<=1. Let K0 vanish
on C=1 and take values in {-1,1} on C=0. No independence of K0 and C is assumed.
An internal private priority list g, on blocks disjoint from the exterior cube,
selects independent Boolean cores using point tests and ends at a constant default.
Actual compatible physical restrictions of the list and its cores are allowed.
Write F=K0+Cg and query one coordinate of an unfinished internal point test.
Let d be its actual influence, D=H(F)-E_child H(F_child), and kappa the drop of
the same merged fine reserve R=sum eta(label mass) Var(core).

At the queried test, q=2^-r with r>=1, current core u of mean m, SAME later
fallback v of mean n, delta=m-n, V=1-n^2, M=n+q delta, x=q|delta|<=1.
For earlier unfinished tests A_j, let E=product(1-A_j), e=E E>0, and
K=sum m_j A_j product_(h<j)(1-A_h). Let Z_v be the fine variance average of v.
Then, with Phi(a,b)=eta(a)+eta(b)-eta(a+b),

    d=c e q(1-m n),
    kappa=c e [q(1-m^2)+k(q) Z_v],
    k(q)=eta(1-q)-eta(1-2q)/2 >= 0,
    B-kappa=c e(q-2q^2)(V+delta^2)
             +c e V Phi((1-q)^2,q^2)-c e k(q) Z_v+S,
    S=sum_(s,T) Phi((K0hat(s)1_(T=empty)
                     +Chat(s)(Khat(T)+M Ehat(T)))^2,
                    x^2 Chat(s)^2 Ehat(T)^2).

These are A059 stage17 equations (1), re-derived in REVIEW_A059.md. Every earlier
nonempty data row has no queried amplitude; every current/fallback nonempty data
row misses K0. Thus the coherent term displayed here is the entire remaining
interaction. The constant scale c in each fine-label mass cancels in the reserve
drift, since eta(c a)=c eta(a)+a eta(c) and label probabilities are harmonic.
No fresh reserve is introduced.

## 2. All-density upper bound

On positive Chat rows set mu(s)=Chat(s)^2/c and U_s=K0hat(s)/Chat(s).
Parseval and the disjoint physical support of K0,C give

    E_mu U_s^2 <= (1-c)/c = rho.

Rows with Chat=0 have zero queried amplitude, so are omitted without division.
Under nu(T)=Ehat(T)^2/e, the private earlier blocks are independent, the empty
frequency has mass e, and the last-nonempty-block argument gives

    |Khat/Ehat+M| <= 3/t_J,       E_nu ln(1/t_J)<=1-e<=1.

These require independent earlier control blocks, but no lower bound on c.
For x>0, the elementary sum/product log bounds and Jensen only in mu give

    E_(mu nu) ln(1+(Khat/Ehat+M+1_empty U_s/e)^2/x^2)
       <= ln(1+18/x^2)+2+e ln(1+2 rho/(x^2 e^2))
       <= ln(1+18/x^2)+ln(1+2 rho/x^2)+2+2/exp(1).

In the second line, 1+a/e^2<=(1+a)/e^2, e<=1 and
e ln(1/e)<=1/exp(1) are used. Unlike A059's frequent-density specialization,
rho is retained explicitly. The scalar packet inequality
Phi(a,b)<=b[1+ln(1+a/b)]/ln 2 now gives

    S <= c e x^2 [A(c)+4 ln(1/x)]/ln 2,
    A(c)=3+2/exp(1)+ln 19+ln(1+2 rho).

Since A(c)>4, differentiation gives
x[A(c)+4 ln(1/x)]<=A(c) on 0<x<=1. Also
|m-n|<=1-mn, because (1-mn)^2-(m-n)^2=(1-m^2)(1-n^2)>=0.
Consequently S<=d A(c)/ln2. The other positive sectors cost at most 6d,
using V+delta^2<=2(1-mn), V<=2(1-mn) and
Phi((1-q)^2,q^2)<=2q(1-q). The negative reserve sector has the correct sign.
The full physical child-channel term is at most 2d/ln2. Therefore

    D-kappa <= K(c) d,
    K(c)=6+[5+2/exp(1)+ln 19+ln(2/c-1)]/ln2
         <= log2(1/c)+C0,
    C0=6+[5+2/exp(1)+ln 38]/ln2 <20.                 (U)

For the last inequality, use 2/exp(1)<3/4, ln38<11/3, ln2>56/81.
The numerator is <113/12, hence C0<6+(113/12)(81/56)<20.
The exponential comparisons are certified by finite positive Taylor sums.
No small influence is divided out. If x=0 the coherent S is zero directly.
If d=0 at a positive guard, the current/fallback means are the same constant
and all positive sectors vanish. A zero guard or c=0 makes the actual query
irrelevant; set its tax bill to zero rather than writing log(1/0).

At c>=1/2 this recovers the source's upper rate below21. At c=1 the previous
private-list upper rate below17 remains stronger. Neither additive constant
is claimed optimal.

## 3. Actual Boolean witnesses force coefficient one

For every even m>=4, let b be the paired quadratic bent sign on m bits,
b(x)=(-1)^(x1*x2+...+x_(m-1)*x_m), and C=1_(x=0). Thus c=2^-m,
b(0)=1 and every coefficient bhat has magnitude sqrt(c). Put

    K0=b-C,        g=Z,        F=b-C+C Z,

where Z is a fresh fair sign. The internal list has one fair point test returning
constants +1 and -1. Every exterior cell also returns a constant. Thus the
ORIGINAL fine U=R=0 at the root and both actual children. Those children are
exactly b and b-2C. Query influence is d=c, and c can be arbitrarily small.
There is no independent-copy or coarse-reserve interpretation in this claim.

The Fourier coefficient pair at each exterior frequency T is

    a_T=bhat(T)-c,        b_T=c.

Since |a_T|>=sqrt(c)-c=sqrt(c)(1-sqrt(c)), and
Phi(A,B)>=B log2(A/B) for A>0,B>0, the complete erasure obeys

    B/d >= m+2 log2(1-sqrt(c)) >= m-1.             (L)

Indeed there are 1/c rows, each contributes at least
c^2[m+2log2(1-sqrt(c))], and sqrt(c)<=1/4 ensures
(1-sqrt(c))^2>=9/16>1/2. The physical child-channel term is nonnegative by
entropy concavity, so the ACTUAL full decrement D is at least B.

Combining (L) and (U),

    m-1 <= D/d <= m+20,           D/[d log2(1/c)] -> 1.

For every coefficient a<1 and every finite additive rate L0, choosing even
m>(L0+1)/(1-a) contradicts D-kappa <=[a log2(1/c)+L0]d.
Thus the exterior logarithm has exact leading coefficient one, and a fixed
density-free controller coefficient is impossible. This is precisely the
necessity question left open in A059 stage17, not a new discovery of the
previously known bent-splice local obstruction.

The earlier A060 bent-data calculation supplies the finer optional asymptotic
D/d=m+3/ln2+O(c), verified again in the finite certificates. It is not needed
for the leading-coefficient proof. In that DATA representation, the release
was c*m because Z was one variance-one core with mass c. In the present
CONTROLLER representation Z selects two constant fine cores, so kappa=0.
The same actual D has not changed; its reserve debit has. This is why the
previous bounded signed data remainder does not contradict (L).

## 4. Stopping, tensorization and the remaining universal bill

On any compatible finite physical stopping tree consisting of these internal
queries and already-paid data queries, the original profile and both actual
terminals telescope. The new controller bill is

    20 Pi_ctrl + sum_v w_v d_v log2(1/c_v).

Here c_v is the ACTUAL exterior density at that node, not the root density;
earlier paid debits and remaining bank are retained. This is a paid local
interface, not payment of the displayed aggregate density bill. The once-only
root reserve is not restarted when c changes.

For a tensor-closed rule with additive per-factor ledgers, N disjoint copies
of any witness have N times the full decrement, spent query influence and
density-weighted bill, with original factor reserves still zero. A fixed
absolute additive allowance divided by N vanishes. This conclusion does not
assume this particular wrapper family is itself closed under a new canonical
single-wrapper representation, and does not remove overhead charged per factor.

Every witness has the full exterior bent entropy and both complete terminal
entropies retained; total exterior influence grows with m. The local obstruction
is not an FEI counterfamily. The first unsupported universal line is paying the
aggregate density bill after a source-dependent exterior exposure that lowers
c, from ONE unused original bank while preserving old debits and both terminals.
Arbitrary overlapping internal guards and shared physical core data also remain
outside (U). Full FEI is OPEN.

## 5. One actual density-lowering exposure paid from its diminished source bank

The sharpness witness can be reached from a frequent exterior node, without
renewing its original bank. Introduce a fresh fair exterior bit X and define

    W(X,x,Z) = Z                         if X=0,
             = b(x)-C(x)+C(x)Z           if X=1.

Initially its exterior fallback indicator is C_root=(1-X)+X C, with density
(1+c)/2>=1/2 and K0_root=X(b-C). Query X first. The X=1 child is exactly the
rare-density witness above, while X=0 is the same physical Z. Every fine core
remains constant, so the ORIGINAL fine R is zero throughout this history.
Both X children and all four subsequent X,Z terminals remain actual functions.

The source query influence is d_X=(1-c)/2: outside C, comparing the independent
fair Z with the fixed sign b disagrees with probability1/2; on C the children
coincide. The complete source decrement satisfies 0<=D_X<=2. Indeed its erasure
is at most one bit, and its physical two-child Jensen-Shannon term is at most
one bit. This proves the bound without a dimension-dependent estimate or omission
of either terminal.

Freeze ONE source bank B0=6 d_X at the root. First book the ACTUAL D_X, leaving
B1=6d_X-D_X. The only nonzero descendant density tax at a Z query is in the
X=1 child, with original reach1/2:

    T=(c/2)log2(1/c) <= d_X/ln2.

This follows from c ln(1/c)<=1-c. Since c<=1/16 and ln2>2/3,

    D_X+T <=(64/15+1/ln2)d_X <(173/30)d_X,
    B1-T > (7/30)d_X >0.                            (P)

Thus one actual exposure lowers the exterior density below1/2 by an arbitrarily
large factor, and the forced logarithmic tax is paid from the SAME already-debited
source bank. There is no reset and no subsidy from either unresolved terminal.
The ordinary 20d base price of the later rare Z query is separate; its weighted
charge is10c. In the X=0 branch Z is a literal and its entropy decrement is zero.
The exact two-query telescope therefore gives

    H(W)-[H(b)+H(b-2C)]/4 <= 6 d_X+10c,

with the full remaining exterior entropy retained. This is a local history
payment, not a universal bound on H(W). It closes this explicit density-lowering
test of A059's NEXT, at fixed source rate6 and residual bank>7d_X/30.

The unsupported general step is replacing the fair internal Z and this prescribed
exterior switch by an arbitrary inherited nonflat fallback/source query. The
actual disagreement d_X can then shrink relative to the new density bill; the
present bank proof has used the fair-Z mismatch identity explicitly. NEXT should
test that source-dependent history using the measured signed unused ancestor
bank, rather than demanding a density-free local price already refuted above.

## Scalar physical-channel check

For each queried Walsh pair a,b, put v=a^2+b^2 and t=2ab/v on v>0.
The full physical child-channel gap in natural units is
v[(1+t)ln(1+t)+(1-t)ln(1-t)]/2. Its scalar bracket is at most
1-sqrt(1-t^2): on0<=t<1, the derivative difference is
t/sqrt(1-t^2)-atanh(t)>=0, since its derivative is
(1-t^2)^(-3/2)-(1-t^2)^(-1)>=0 and it starts at0.
Evenness and continuity handle negative t and both endpoints. Thus the row
is at most v-|a^2-b^2|=2min(a^2,b^2)<=2b^2. Summing all actual
physical rows yields J<=2d/ln2, with no branch-independence hypothesis.
Nonnegativity of J follows from concavity of entropy of the two actual
child spectral probability laws. These are the channel facts used in(U),(L).
