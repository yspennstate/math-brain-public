# Full FEI reduces without loss of constant to Boolean block-prime functions

Entropy is in bits. Call g block-prime if no coordinate block B with
2<=|B|<=N-1 can be replaced by a single Boolean summary even when all
outside coordinates remain individually available. This is the definition
used here, without a claim about other notions of prime function.

## 1. Actual Boolean construction

For ANY f:{0,1}^n->{-1,+1}, including constants and dummies, and m>=3,
put N=n+m and G_m(x,z)=f(x)b_N(x,z), where b_N(u) is -1 exactly when
|u|<=1 and +1 otherwise. Every G_m is block-prime, and with f,n fixed
and m tending to infinity,

    H(G_m)->H(f), I(G_m)->I(f).

For nonconstant f the entropy/influence ratio also converges. Therefore
FEI(C) on all block-prime functions in all dimensions is equivalent to
full FEI(C), with the SAME finite C>=0. This is a reduction, not a solution.

## 2. Three residual rows for every proper block

The truth matrix with B assignments as rows and outside assignments as
columns admits a Boolean summary exactly when there are at most two
distinct rows. Necessity is pigeonhole; sufficiency labels the two row
types by the two signs. We exhibit three distinct rows for every proper
B of size at least two. All unmentioned coordinates are zero.

A. B contains at least two padding bits p,q. Use inside assignments
0,e_p,e_p+e_q and outside columns 0,e_j, with any j outside B. The
original inside x is unchanged, so let a,b be the respective f signs
on these two columns. The row patterns are

    (-a,-b), (-a,b), (a,b).

They are pairwise distinct for every a,b in {-1,+1}. The outside bit
exists since B is proper, and may be either an original or padding bit.

B. B contains exactly one padding bit p, and thus an original bit i.
At least two padding bits q,r lie outside B because m>=3. Use inside
assignments 0,e_p,e_i+e_p and outside columns 0,e_q,e_q+e_r. Let a be
f(0), and b be f(e_i). The row patterns are

    (-a,-a,a), (-a,a,a), (b,b,b).

The first two differ and are nonconstant; the last is constant. Thus
they are distinct for both choices of the original signs.

C. B contains no padding bits, so choose two original bits i,j in B
and two padding bits q,r outside. Inside assignments 0,e_i,e_i+e_j,
outside columns 0,e_q,e_q+e_r, give

    (-a,-a,a), (-b,b,b), (c,c,c).

The first has equal first two entries and unequal last two; the second
has unequal first two and equal last two; the third is constant. These
patterns are pairwise distinct for arbitrary f signs a,b,c.

The cases exhaust all B and use no property of f. Every G_m has every
coordinate relevant: a dummy bit would make its complement block have
at most two rows, contradicting the result since N>=3. Fixing any two
padding bits to one recovers the complete original f, with other padding
bits becoming dummy. This restriction alone gives no ratio comparison.

## 3. Influence approximation

Let f^pad(x,z)=f(x), delta_N=(N+1)/2^N. The disagreement set of G_m and
f^pad is EXACTLY the N+1 vertices of the ball. For each coordinate the
pivotal-edge indicator can change only if an endpoint is in this set,
an event of probability at most 2 delta_N. Hence

    |I(G_m)-I(f)|<=2N delta_N ->0.

This holds at every N>=3, including constant f. No rare-restriction
influence assumption is used.

## 4. Entropy approximation on a growing spectral alphabet

Let v,w be the real normalized Fourier coefficient vectors of G_m and
f^pad on the same N-cube. Parseval gives ||v||=||w||=1 and
||v-w||^2=4 delta_N. For their squared spectral laws P,Q,

    epsilon=TV(P,Q)=(1/2)sum |v_S-w_S||v_S+w_S|
           <=(1/2)||v-w|| ||v+w||<=2 sqrt(delta_N).

For completeness, entropy continuity follows by matching common mass
min(P_S,Q_S) diagonally and coupling the residual mass off the diagonal
(the residual supports are disjoint). The mismatch event E has
probability epsilon. On M=2^N possible values, conditioning on E and
the second variable gives

    H(P)-H(Q)<=H(X|Y)<=h_2(epsilon)+epsilon log2(M-1).

When E=0 the first variable is known; when E=1 it has at most M-1
possibilities. Reverse X,Y for the opposite difference. The epsilon=0
case is direct and needs no division. For sufficiently large N,
epsilon_bar=2 sqrt(delta_N)<=1/2. Since h_2 is increasing on [0,1/2],

    |H(G_m)-H(f)|<=h_2(epsilon_bar)+N epsilon_bar ->0.

Padding preserves H(f) exactly. The error tends to zero because
N sqrt((N+1)/2^N)->0, not merely because disagreement tends to zero.
Thus the growing alphabet is paid. No dimension-dependent entropy sum
is interchanged with a limit without this bound.

For nonconstant f, I(f)>0: the connected cube has a pivotal edge. Thus
division in H(G_m)/I(G_m)->H(f)/I(f) is justified for large m. Constant
f has H(f)=I(f)=0 and requires no ratio division.

## 5. Universal consequence and initial bank

If H(g)<=C I(g) for all block-prime g with one fixed finite C, apply it
to G_m and pass to the limits. This proves H(f)<=C I(f) for arbitrary
f. The reverse implication is immediate. Any strict FEI(C) violation
would therefore have a finite block-prime violation; no violation is
constructed without an original violating function.

Every proper disjoint Boolean decomposition of G_m consists only of
singleton blocks. Their nonconstant cores are bits or complements,
have zero entropy and zero stopping deficit hull rho_K for K>=0. Hence
the previous A075 supplied coherent bank has initial value exactly

    U_K(G_m)=H(G_m)+kappa I(G_m)

on EVERY proper Boolean partition. For nonconstant f its normalized
price tends to H(f)/I(f)+kappa. Optimizing these partitions cannot reduce
the price. A whole-domain core retains the original problem. This
upgrades A071's ball obstruction to arbitrary starting Boolean ratios
with an explicit construction and a justified approximation bridge.
It does not refute an O(I) bank price; that price remains equivalent
to full FEI. Multiple-output summaries, overlaps and paid restriction
histories lie outside the present obstruction.

The first unsupported line remains an O(I) initial source on arbitrary
block-prime cores, or another invariant paying entropy from the same
unused original influence. No such bound is proved. Full FEI remains
OPEN. The rung is analytic proof with exact finite validation, subject
to independent review; any formal-check receipt is separate.
