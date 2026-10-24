# An influence-paid raw-indicator to Boolean-sign block transfer

Uniform finite cubes throughout. Let g=1_U, f=1-2g and p=E g. For a
nonempty physical block A, write p_x=E_y g(x,y), and use the inherited
indicator orientation in every child. Let F(g) be raw Fourier entropy
in bits, E_A(g)=sum_s |s_A| ghat(s)^2, I_A(f)=4E_A(g),
Lambda_A(g)=F(g)-E_x F(g_x), and L_A(f)=H(f)-E_x H(f_x).
Put kappa=2/ln2. A need not separate components for the transfer theorem.

## 1. Exact empty-coefficient correction

Nonempty Fourier coefficients of f equal -2 times those of g, while
fhat(empty)=1-2p. Parseval gives sum_(s!=empty) ghat(s)^2=p-p². In
natural entropy units, define the explicit scalar correction

    T(p)=-(1-2p)² ln((1-2p)²)+4p² ln(p²)-8ln2 p(1-p),

with zero-log terms interpreted by continuity. Then exactly

    (ln2)H(f)=4(ln2)F(g)+T(p),
    (ln2)L_A(f)=4(ln2)Lambda_A(g)+T(p)-E_x T(p_x).       (1)

This is a signed physical-child ledger, not component pruning. All child
means are retained, including p_x=0,1 and p_x>1/2. The correction is
defined independently of any desired bound.

## 2. Negative curvature is controlled by the mass-tilt entropy

For 0<p<1, p!=1/2, direct differentiation cancels all polynomial terms:

    T''(p)=16 ln(2p/|1-2p|).                            (2)

It is nonnegative for p>=1/4. For 0<p<1/4, since 1-2p<1,

    p T''(p)>=16p ln(2p)>=-8/e.

The last inequality is the elementary minimum of t ln t at t=1/e.
Consequently T(p)+(8/e)p ln p is convex on [0,1]. At p=1/2 the derivative
of -(1-2p)²ln((1-2p)²) is continuous, its second derivative tends to
positive infinity, and convexity extends across that point. Endpoints
follow by continuity. Jensen applied to the actual uniform physical
child means yields

    T(p)-E_x T(p_x) <= (8/e) Ent_x(p_x),                (3)

where Ent(w)=E[w ln(w/Ew)]. No lower bound on p is present. The sharper
constant 8/e is not claimed optimal. The convenient relaxation 8/e<3
follows from e>1+1+1/2+1/6=8/3.

## 3. The same physical queried energy pays this entropy

Apply cube logarithmic Sobolev to u(x)=sqrt(p_x):

    Ent_x(p_x)<= (1/2)sum_(i in A) E_x(u(x)-u(x^i))².

For fixed x, sqrt(p_x) is the L2 norm of the indicator g_x(y). The
reverse triangle inequality gives

    (sqrt(p_x)-sqrt(p_xi))² <= E_y(g_x(y)-g_xi(y))².

Average x and sum i. In the normalization D_i=(Id-flip_i)/2 this proves

    Ent_x(p_x)<=2E_A(g).                               (4)

For completeness, the logarithmic Sobolev inequality needed here has
an elementary proof. At one bit, for (t,1), twice the Dirichlet-minus-
entropy difference is
G(t)=(t²+1)ln((t²+1)/2)-2t²ln t+(t-1)². G(1)=0 and G'(t)>=0 for t>=1,
because 1-1/t-ln(2t²/(t²+1)) vanishes at one and has derivative
(t-1)²/[t²(t²+1)]. Symmetry G(t)=t²G(1/t) covers t<=1; continuity covers
zero entries. Entropy tensorization follows by conditioning and convexity
of the entropy functional on product coordinates, yielding the displayed
cube inequality. Thus no external analytic theorem is an unpaid premise.

Combining (1)--(4) gives the universal, actual Boolean block transfer

    L_A(f) <= 4Lambda_A(g)+(4/(e ln2)) I_A(f).          (5)

For any finite adaptive physical restriction tree with leaves rho,
multiply (5) by actual node reach weights and telescope both entropy
ledgers and queried influence. The terminal-inclusive result is

    H(f)-E_rho H(f_rho)
       <=4[F(g)-E_rho F(g_rho)]
         +(4/(e ln2))[I(f)-E_rho I(f_rho)].              (5T)

Here g_rho=(1-f_rho)/2 uses the same inherited orientation and the same
leaf partition. The correction consumes each erased influence once;
leaf entropy is never set to zero unless the leaves are actually constant.
A raw tree decrement paid at K times erased indicator energy thus
transfers to a sign decrement paid at K+4/(e ln2) times erased sign
influence, without an added support-density assumption or repeated root
charge. The two-point scalar correction itself also telescopes exactly
to T(p_root)-E_rho T(p_rho).

An exact-arithmetic-friendly weaker version has additive charge
(3/(2ln2)) I_A(f). If I_A=0, the physical g is constant across the block,
p_x is constant, and all decrements and corrections in (1) vanish.

## 4. Density-free projection payment on physical critical sources

Let U_k be the actual connected components of U, g_k=1_Uk, p_k=E g_k,
and let R_k be their projections on a proper block A of r coordinates.
Assume the projections are pairwise disjoint. Put mu_k=|R_k|/2^r,
Q_A=sum_k p_k log2(1/mu_k), p=sum_k p_k.

Each component partial-Fourier row is supported on R_k. Cauchy--Schwarz
bounds each normalized Fourier atom by mu_k; its entropy is at least
log2(1/mu_k). Its physical squared-row density has KL to the uniform
block law at least the same number, by restricting the reference to
R_k and using nonnegative KL. Therefore

    Lambda_A(g_k)>=2p_k log2(1/mu_k).

Fiberwise indicator edge isoperimetry gives
E_A(g_k)>=p_k log2(1/mu_k)/2. Here a self-contained induction is enough:
for child means m0,m1, last-coordinate energy is at least |m0-m1|/4,
and child energies average to at least
[m0 log2(1/m0)+m1 log2(1/m1)]/4. Concavity h2(t)>=2min(t,1-t) proves
their sum is at least (m/2)log2(1/m), m=(m0+m1)/2. Each data-fiber mean
is at most mu_k; average the resulting bound in the retained data bits.

Actual components have no cross boundary edges, hence E_A(g)=sum_k E_A(g_k).
The previous explicit component interface

    Gamma_A=[B_A(g)+kappa E_A(g)-sum_k Lambda_A(g_k)]_+

satisfies F(g)<=sum_k F(g_k)+Gamma_A. If Q_A>=rp/2, then
Gamma_A<=kappa E_A(g), E_A(g)>=rp/4, and

    Lambda_A(g)<=rp+kappa E_A(g)<=(4+kappa)E_A(g).      (6)

The last upper bound itself does not require disjointness; the disjoint
projection hypothesis is kept to remain in the proved component-payment
class. It uses B_A(g)<=rp and the raw squared-row logarithmic Sobolev
bound Jraw_A(g)<=kappa E_A(g), in the same normalization as (4).

From (5)--(6), for every sign whose indicator support meets this projection
condition, irrespective of rarity, there is a paid actual proper block:

    L_A(f)<=C_proj I_A(f),
    C_proj=4+2/ln2+4/(e ln2)<10.                        (7)

The strict numerical relaxation follows from ln2>2/3 and e>8/3,
which give C_proj<4+3+9/4=37/4<10. These are elementary analytic bounds,
not decimal rounding assertions.

If f is physical-descendant ratio critical, its actual child comparison
gives L_A(f)>=R(f)I_A(f). Since (6) ensures I_A>0 for p>0,r>0, (7)
implies H(f)/I(f)<=C_proj. Thus the prior positive-density hypothesis
p>=p0 is completely removed. Arbitrarily rare, non-Cartesian support is
admitted to this stated critical class. The former sharper moderately
balanced bound remains valid at its previous scope.

For a least-essential-dimension K-violator, let
S_A=-E_x[H(f_x)-K I(f_x)]>=0. The exact deficit line is

    D_K(f)+S_A=L_A(f)-K I_A(f)
                   <=(C_proj-K)I_A(f).                (8)

Thus K>=C_proj excludes the projection class with every actual child
reserve retained. Components are not physical descendants; no child is
assumed to inherit criticality. The transfer pays one queried physical
influence account, not a reused parent-plus-child budget.

## 5. Honest universal gap

The universal new statement is the raw-to-sign correction payment (5).
The new critical consequence (7)--(8) is restricted to an affordable
proper projection block; it does not assert such a block exists for
every source. Support rarity is no longer a blocker for this class.
Connected supports and component projections overlapping on every proper
block can still defeat the geometric selection hypothesis. The first
unsupported line is a universal paid proper-block choice or a terminal-
inclusive correction for those overlaps. Full FEI remains open.
