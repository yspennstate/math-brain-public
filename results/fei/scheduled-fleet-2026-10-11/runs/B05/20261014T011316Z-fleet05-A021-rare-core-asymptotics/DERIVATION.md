# Relative bias pays a point-switch without renewing face reserves

All cubes are uniform, all signs Boolean, and all entropy is in bits.
Write c=1/ln2. For nonnegative row masses a,b, let
Psi(a,b)=(a+b)h2(b/(a+b)), continuously extended at zero. A physical
query is K-good if B_i=H(S_i|S_-i)<=K Inf_i. No terminal is discarded.

## 1. All-dimensional point-switch inequality

Let G,H be ANY signs on the same data cube, gamma=P(G!=H)>0,
eta=P(G=-1), and a=eta/gamma. For j>=1 fresh point controls put
F=G+A_j(H-G), with active selector point zero. At a live selector query
put rho=2^-(j-1) and d=rho gamma. Then

    B_i(F)/d <= max{4,c+log2(8a+4)}+2c/sqrt(e).             (1)

There is no lower bound on gamma, no balance or monotonicity hypothesis,
and the estimate is uniform in j and both data and selector dimensions.
If gamma=0, the selector is irrelevant and B=d=0.

Proof. Set Delta_T=(Hhat(T)-Ghat(T))/2, so sum Delta_T^2=gamma.
For every NONEMPTY remaining-selector Fourier label, the first child
coefficient is zero; the two parent sector masses coincide. Their exact
erasure contribution, summing residual-selector multiplicities, is
2(1-rho)d. In the empty remaining-selector sector, the two parent
coefficients are u_T=Ghat(T)+rho Delta_T, v_T=-rho Delta_T.

Separate T=empty from T!=empty. For T!=empty let
M=sum v_T^2<=rho^2 gamma. The total row mass P obeys

    P=sum[(Ghat+rho Delta)^2+rho^2 Delta^2]
     <=2 Var(G)+4rho^2 gamma
     <=8eta+4rho^2 gamma
      =gamma(8a+4rho^2)=Pstar.

The first inequality uses (x+y)^2<=2x^2+2y^2; Var(G)=4eta(1-eta).
The elementary binary entropy bound Psi(u^2,v^2)
<=v^2 log2(e(u^2+v^2)/v^2), followed by log-sum, gives
sum_(T!=empty) Psi<=M log2(eP/M). Replacing P by Pstar is valid;
x log2(ePstar/x) is increasing on 0<=x<=Pstar, and rho^2 gamma<=Pstar.
Consequently these rows contribute at most

    rho^2 gamma log2(e(8a/rho^2+4)).

For T=empty, |Delta_empty|=|EH-EG|/2<=gamma by coupling on the same
input. Its derivative sector mass M0<=rho^2 gamma^2. The row's total
mass is at most one by parent Parseval. Adding a nondifferentiated mass
1-P0 can only increase Psi, hence its entropy is <=h2(M0), and therefore
<=M0 log2(e/M0)<=rho^2 gamma^2 log2(e/(rho^2 gamma^2)). The last
monotonicity uses rho^2 gamma^2<=1. Dividing by d, this contribution is
at most x log2(e/x^2), x=rho gamma, whose maximum on [0,1] is
2c/sqrt(e), obtained at x=e^-1/2. These estimates also cover zero rows
by continuity; no division by a zero packet is required.

Combining and using 8a/rho^2+4<=(8a+4)/rho^2 gives

    B/d <=2(1-rho)+rho[L+2log2(1/rho)]+2c/sqrt(e),
    L=c+log2(8a+4).

For rho=2^-l, l>=0, the first part is
2+2^-l(L-2+2l). It is <=max(4,L): if L<=4, enlarge to 4 and use
1+l<=2^l; if L>=4, use 2l/(2^l-1)<=2 for l>=1 and handle l=0
directly. This proves (1). It does NOT replace the actual erasure by
the marginal h2(d), which would lose log(1/gamma).

The same bound may be applied after flipping BOTH output signs; thus
eta can be replaced by min(P(G=-1),P(G=1)) if desired. The baseline G
is always the physically inactive branch of the point selector.

## 2. Rigorous constant consequences, even when gamma tends to zero

If eta<=gamma/5, then EVERY point-selector node is strictly 6-good.
If eta<=gamma, then EVERY point-selector node is strictly 7-good.
Here are elementary constant certificates, requiring no numerical log:
ln2>2(1/3+1/81+1/1215)=842/1215>9/13, so c<13/9.
Also e>65/24>(13/8)^2, so 2c/sqrt(e)<16/9.
For a<=1/5, L<=c+log2(28/5)<3/2+5/2=4, since
(28/5)^2<32. Formula (1) is <4+16/9<6.
For a<=1, L<=c+log2(12)<13/9+18/5, since 12^5<2^18.
Thus max(4,L)+2c/sqrt(e)<307/45<7.

These are conditional point-switch bounds, not fixed local prices for
arbitrary rare splits. Inactive-branch minority relative to source change
is the explicit extra hypothesis; the retired local variance refunds
are neither used nor claimed.

## 3. The logarithmic contrast is necessary in order

For even m>=4 let b_m=(-1)^(x1x2+...+x_(m-1)x_m), let b'_m flip b_m
only at zero, and take G=z b_m, H=z b'_m with a fresh balanced sign z.
The one-pair sign (-1)^(xy) has normalized Fourier coefficients
(1,1,1,-1)/2; multiplying independent pairs proves the claimed flat
coefficient magnitude 2^(-m/2) directly.
Then eta=1/2, gamma=delta=2^-m. At one selector (j=1) all nonzero core
Fourier rows have G coefficient sigma sqrt(delta), H coefficient
sigma sqrt(delta)-2delta, sigma in {-1,1}. The parent sectors have
masses (sigma sqrt(delta)-delta)^2 and delta^2. Each row's total mass
is >=delta(1-sqrt(delta))^2>=delta/4. Its entropy is at least
delta^2 log2[(delta/4)/delta^2]=delta^2(m-2), since the other part of
Psi is nonnegative. There are 1/delta such rows. Therefore

    B/d >= m-2 = log2(eta/gamma)-1.                       (2)

This actual Boolean family proves that a universal point-switch price
depending only on eta/gamma must grow at least logarithmically as the
contrast grows. Equation (1) has that order, with explicit absolute
additive constants. Neither (2) nor small selector influence disproves
FEI; the core and its terminal entropy remain real costs. It rules out
a contrast-blind constant price, rather than a policy choosing a different
coordinate or spending a certified terminal reserve.

For an exact optimal-price formulation, let P(theta) be the supremum of
B_i(F)/d over ALL actual Boolean pairs G,H on any uniform data cube,
ALL positive point-control widths j, gamma>0, and eta/gamma<=theta.
For theta>=1, (1) and the rational constants in section 2 give
P(theta)<=(log2(theta)+307/45)<log2(theta)+7: since L>4 at theta>=1,
use 8theta+4<=12theta. For theta>=8 choose the largest even m>=4 with
2^(m-1)<=theta. Then 2^(m-1)>theta/4 and the actual bent-flip example
has B/d>=m-2>log2(theta)-3. Therefore, for EVERY real theta>=8,

    log2(theta)-3 <= P(theta) <= log2(theta)+307/45,
    lim_(theta->infinity) P(theta)/log2(theta)=1.           (2a)

The upper supremum need not attain the strict pointwise bound, so the
non-strict inequality in (2a) is intentional. This identifies the optimal
leading logarithmic cost uniformly in the rarity width. A claimed global
potential that assigns such switches a scalar rate depending only on
contrast must allow this logarithm or supply an explicitly owned rebate.
For a thinned node the underlying gamma, not the smaller physical
d=rho gamma, is the source parameter in (1); redefining gamma at each
history would restore a false rarity logarithm. The same branches and
their real terminal accounts must be carried through the selector block.

## 4. Complete small-disagreement closure for the overlapping point family

Let S,W,U,V be point indicators on mutually disjoint fresh blocks of
positive widths s,L,R,T, and let g be ANY independent Boolean core,
balanced or not. Put B=WUV, C=U OR V, A=B+S(C-B), F=1+A(g-1).
Write alpha=2^-s, p=2^-L, q=2^-R, r=2^-T,
eta0=pqr, beta=q+r-qr, e0=beta-eta0, pi=eta0+alpha e0,
a_g=1-Eg and J(A)=I(1-2A)/2.

Query S first. Its inactive branch G=1+B(g-1), active branch
H=1+C(g-1). They obey P(G=-1)=eta0 a_g/2,
P(G!=H)=e0 a_g/2. If a_g=0 all costs vanish. Otherwise their ratio
is eta0/e0<=1/5: since p,q,r<=1/2,
6pqr<=3qr<=q+r-qr, equivalently 6eta0<=beta.
Thus every S query is 6-good by section 2, uniformly in all four widths,
even when branch disagreement tends to zero. No complete face price
is reserved at ANY separator layer.

When S fails, resolve the conjunction B by a point block. Its inactive
branch is constant 1, hence eta=0 and all its queries are 6-good.
When S succeeds, resolve U OR V by querying the U block first. Its
inactive branch is G'=1+V(g-1), active branch H'=g, so
P(G'=-1)/P(G'!=H')=r/(1-r)<=1 when a_g>0.
All U queries are 7-good. On U failure resolve V, again with constant
inactive branch, so these nodes are 6-good. Stop at constants or g.

This actual control-only stopping tree has Q_bad,7=0 for every choice
of widths and EVERY Boolean g. The terminal core is reached with physical
probability pi, retaining pi H(g) and pi I(g). The exact exclusive accounts
are

    J_B=(L+R+T)eta0,
    J_C=R q(1-r)+T r(1-q),
    J(A)=s alpha e0+(1-alpha)J_B+alpha J_C,
    I_ctrl=a_g J(A), I(F)=a_g J(A)+pi I(g).              (3)

The physical entropy decrement is B+JS with JS<=2c d; the physical
influence telescope has queried cost I_ctrl. Hence

    H(F) <= (7+2c)a_g J(A)+pi H(g).                     (4)

More sharply 7 can be replaced by 307/45; thus the new prefix constant
is <10 because 307/45+26/9=437/45<10. If H(g)<=C0 I(g), the completed
bound is H(F)<=max(10,C0) I(F), with strict slack on nonzero controls.
For balanced g, the old terminal formulas are recovered by a_g=1.

The same argument gives the arbitrary-core two-event union control
ledger, without the old lower bound on a_g. No arbitrary-core FEI is
claimed: (4) retains pi H(g) and inherits any unpaid terminal ratio.
The case s=L=R=T=1 does not contradict the earlier five-bit witness:
that witness queried a different, privately occurring control first.

## 5. Independent reconstruction of the A023 one-use reserve

Review target is ONLY the single-separator addition to
A023-OVERLAP-EXPOSURE-GOOD-CONTROL-LEDGER v2, not its whole bundled claim.
For a fair separator X, children controllers are B=WUV and C=U OR V.
The difference D=C-B has directional edge cuts disjoint between B and C:
U/V edges of C require the other block inactive, whereas those of B
require it active; W edges occur only in B. Thus J(D)=J_B+J_C.
With balanced g, the actual root query has d_X=e0/2 and

    c_X=I(1+D(g-1))/2=e0 I(g)/2+(J_B+J_C)/2.

Physical influence after the root is Jrem+pi I(g), with
Jrem=(J_B+J_C)/2 and pi=(beta+eta0)/2. Since e0/2<=pi,
c_X<=Jrem+pi I(g)=I(F)-d_X. This proves the root reservation can be
spent once. The stated descendant rule can also be reconstructed here:
before separating the constant core row in section 1, all empty-selector
rows have derivative mass rho^2 gamma and total mass <=1. Log-sum gives
B/d<=2(1-rho)+rho log2(e/(rho^2 gamma)). In the active two-event branch,
the source disagreement while resolving U is (1-r)/2>=1/4, because g is
balanced. In either surviving single-point branch it is 1/2. Therefore,
with rho=2^-l, B/d<=2+2^-l(c+2l)<4, since c<2 and 1+l<=2^l.
Every descendant is strictly 4-good, including arbitrary positive widths.
Thus the entropy bound K=5+2c and terminal coefficient C0+1 follow by adding
the root B<=4d_X+c_X, JS<=2c d_X, descendant (4+2c)Jrem and terminal
pi H(g). This independently reconstructs that specified algebra and
boundary ownership and the full single-separator entropy/face theorem.
The source bent-selector class conclusion also follows independently:
the balanced seed has Fourier support at most 2^(m+1), H<=m+1, while
I=1+m/2+(m+1)2^-m, so H/I<2<3. This review does NOT accept the earlier
bundled unbalanced-core two-event scope, source full retained-KL
computation, or unrestricted nested reservations. The new proof above
does not assume them.

## Exact first unsupported universal line

For the biased-core finite certificates, the compressed controller split
identity is also exact: if a_U=hat(A_+)(U), b_U=hat(A_-)(U), then
B_control=Var(g) sum_U K(a_U,b_U)
+sum_U K(1_{U=empty}-a_g a_U,1_{U=empty}-a_g b_U), where
K(x,y)=((x^2+y^2)/2)h2((x+y)^2/[2(x^2+y^2)]).
Nonempty core labels scale K by ghat(T)^2 and sum to Var(g); empty-core
labels give the shifted second term. Thus an actual 32-bit point-defect
core can be certified through its exact bias, without enumerating its
truth table or claiming its empty row is balanced.

There is no proof that every Boolean function admits an actual physical
policy with only bounded-contrast point-switch nodes, nor a nonreusing
payment for the large-contrast nodes and every terminal core. Tribes and
balanced cores already show that bounded contrast is not a universal
description. Equation (2) rules out simply removing that contrast from
this interface. Threshold-4 payment for arbitrary-width small-gamma
overlap is also still open; the closure above uses threshold 7, which is
permitted in the existential C019 bridge but must not be relabeled K=4.
