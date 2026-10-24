# Two distinct edited vertices with arbitrary unequal overlapping controllers

For paired quadratic bent b on k=2m>=6 bits, distinct vertices v,w,
arbitrary independent-of-data indicators A,B on the SAME uniform controller
cube, signs a=1-2A,c=1-2B, and delta=2^-k, define the actual Boolean sign

    F=b(x)[1-2 1_(x=v) A(z)-2 1_(x=w) B(z)].

The data supports are disjoint, so this is a sign even if A and B overlap.
No independence between A and B is assumed. The scoped result is

    I_ctrl(F)=delta[I(a)+I(c)],
    H(F)<=9 I_data(F)+delta[H(a)+H(c)].                 (T1)

Thus controller bounds C_a,C_c give H(F)<=max(9,C_a,C_c)I(F).
These are inherited controller bills, not a universal terminal certificate.

## Exact signed cross terms and physical adjacent-edge cancellation

    Fhat(S,T)=bhat(S)1_(T=empty)
       -2delta[b(v)chi_S(v)Ahat(T)+b(w)chi_S(w)Bhat(T)]. (T2)

The square contains its full signed interference. For each nonempty T put
u=b(v)Ahat(T), z=b(w)Bhat(T). Distinct vertices split the data labels into
equal cosets of chi_S(v xor w)=+1,-1. Their exact entropy contribution is

    2^(k-1)[phi(4delta^2(u+z)^2)+phi(4delta^2(u-z)^2)]. (T3)

The remaining controller-empty contribution is the sum over S of
phi((bhat(S)-2delta[b(v)chi_S(v)EA+b(w)chi_S(w)EB])^2).
Equations (T2)-(T3) are root identities for any bent reference, while the
good access schedule below is specifically quadratic paired.

For each data direction i, write alpha=EA,beta=EB,zeta=E(AB). Exact edges give

Inf_i(F)=1/2+2delta[alpha b(v)b(v xor e_i)+beta b(w)b(w xor e_i)]
         -4delta b(v)b(w)zeta 1_(w=v xor e_i).         (T4)

The last term is the adjacent double-flip cancellation and must be retained.
Controller influence is the disjoint data-fiber sum in (T1), with no AB term.

## Access and retained fibers

Query first coordinates in all pairs, then STOP. At a node after q<m
queries, remaining perturbation measure is at most
(alpha+beta)2^{-(k-q)}. Relative to the intact-pair derivative1/2,
d>=1/2-2^(1-m)>=1/4. Hence every access node is K4-good.

If v,w have different first-coordinate projections, two exceptional leaves
each use the single-point theorem with their separate controller entropy.
Their complete physical inheritance coefficient is delta, and their actual
terminal data cost is at most7 times their terminal data influence.

If they have the same first-coordinate projection, one leaf of reach
tau=2^-m is chi_L q, with q=1-2 1_(t=v')A-2 1_(t=w')B, v'!=w'.
Each raw partner influence is <=2tau(alpha+beta)<=4tau<=1/2, so the
character shift can only increase its actual data influence. Direct edges
give, if v',w' are adjacent in direction i,

    Inf_i(q)=2tau P(A!=B),
    Inf_j(q)=2tau(alpha+beta) for j!=i;

for nonadjacent vertices every partner direction has influence
2tau(alpha+beta). In all cases

    I_data(q)>=2tau(m-1)(alpha+beta).                 (T5)

This lower bound uses actual post-cancellation influence, not the sum of
the two pre-cancellation point boundaries.

## Complete exceptional-leaf entropy bound

Put s=alpha+beta and u=alpha^2+beta^2. The controller-empty root coefficient
of q is 1-2tau s, with entropy at most4tau s log2(e). Its nonempty-partner
controller-empty total mass is exactly M=4tau u-4tau^2 s^2.
Log-sum bounds that sector by M log2(e*2^m/M). This expression increases
for M<=2^m, so M<=4tau u gives

    sector <=8tau m u+4tau u[log2(e)-2]+4tau u log2(1/u)
           <=8tau m u+4tau u log2(1/u).              (T6)

The second inequality uses log2(e)<2. Zero u is handled by continuity.
For T!=empty, the exact controller marginal is
4tau[Ahat(T)^2+Bhat(T)^2], from orthogonality of the distinct point characters.
Its conditional partner entropy is at most m. Subadditivity
phi(x+y)<=phi(x)+phi(y) therefore bounds the total nonempty-controller
sector by

    tau[H(a)+H(c)]+8tau m[alpha(1-alpha)+beta(1-beta)]. (T7)

The subtracted controller-empty phi terms are nonnegative and can be
discarded in an upper bound. Thus all spectral rows, including the empty
row, are accounted for. Finally,

u log2(1/u)<=alpha^2 log2(1/alpha^2)+beta^2 log2(1/beta^2)
             <=2s log2(e)/e.

Combining (T6)-(T7) gives

H(q)<=tau[H(a)+H(c)]+tau s[8m+4log2(e)+8log2(e)/e]
     <=tau[H(a)+H(c)]
       +[4m+2log2(e)+4log2(e)/e]/(m-1) I_data(q)
     <=tau[H(a)+H(c)]+9 I_data(q).                   (T8)

The coefficient decreases with m and at m=3 is strictly below9 using
log2(e)<3/2 and e>2. It remains valid if the two point boundaries cancel
on their shared edge. Character multiplication preserves H and increases
the data influence used to pay (T8), while leaving controller influence intact.
When alpha+beta=0 all entropy and raw-data terms are zero and (T8) is equality.

## One physical partition and universal gap

The access coefficient4+2/ln2<7<9, terminal data influence is disjoint
from removed access influence, and controllers remain unqueried. Exceptional
leaf reach tau multiplies the inherited tau controller bill, yielding delta
per controller, each once. This proves (T1) by the complete entropy telescope.

No scoped proof line remains unpaid. The first universal gap is paying
arbitrary inherited controller entropy, or extending the signed-collision
data reserve to growing numbers of edited vertices without a growing
coefficient. No zero-cost constant-leaf completion or FEI for arbitrary
controllers follows from (T1).
