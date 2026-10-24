# Three nonconstant cores: released bank has no fixed local data price

All cubes are uniform, all signs Boolean, entropy in bits. This targets
an explicit proposed local rule, not FEI or the conserved-bank identity.

## Family and physical histories

Let m>=4 be even, delta=2^-m, and
b(y)=(-1)^(y0*y1+y2*y3+...+y_(m-2)*y_(m-1)). Let v=0,w=e0,
so b(v)=b(w)=1. Let z be an independent balancing sign and x an
independent bit. On the SAME data cube define three distinct nonconstant
balanced cores

    g0=z b(y),
    g1=z b(y)[1-2 1_(y=v)1_(x=0)],
    g2=z b(y)[1-2 1_(y=w)1_(x=0)].

Take two fresh fair controller bits A,B, active at zero. The actual output
is F=g0+A[g1+B(g2-g1)-g0]. Original terminal probabilities are
pi=(1/2,1/4,1/4). No data branch is copied; repeated labels, if present,
would retain their physical weights. Query x while both controllers are
unresolved. This is precisely a three-label mixed physical history.

Write C1=A(1-B), C2=AB. Then

    F=z b-2z 1_(x=0)[1_v C1+1_w C2].

At each exceptional vertex the chosen altered core occurs with probability
1/4. Direct physical edges therefore give

    d=Inf_x(F)=delta/2,
    I_controls=delta,
    I_terminal=1+m/2+m delta/2,
    I(F)=1+m/2+(m+2)delta/2.                              (1)

For completeness, the y-direction correction is zero in direction1,
and delta/2 in every other direction. At v all old incident b edges are
nonpivotal; at w exactly direction1 was pivotal. Each point flip is
selected with probability (1/4)(1/2)=1/8. The x contribution is delta/2,
both controller contributions are delta/2, and the z contribution is1.
This also reconstructs the influence and terminal partition in (1).

## Exact conserved bank and release

Use the source's fixed symmetric bank

    R_star=2 sum_(j<k) pi_j pi_k I(gj gk).

The actual product boundaries are
I(g0g1)=I(g0g2)=(m+1)delta, I(g1g2)=2m delta. Thus

    R_root=(3m+2)delta/4,
    R_(x=1)=0, R_(x=0)=(3m-1)delta/2,
    release=R_root-[R_(x=0)+R_(x=1)]/2=3delta/4=3d/2.     (2)

These are the actual conditioned cores and original controller weights.
They independently verify the source's release formula: at v only label1
is x-pivotal, at w only label2 is x-pivotal, giving q=1/4 at each point,
so release=2 E_y q(1-q)=3delta/4. Conservation remains valid.

## Actual Fourier erasure lower bound

The tensor two-bit Walsh transform of (-1)^(y0*y1) is
(1,1,1,-1)/2, so b has all Fourier coefficients t sigma_T,
t=2^(-m/2)=sqrt(delta), sigma_T in {+1,-1}. Every core Fourier label
contains z. Put eta_T=(-1)^(T0); exactly half the y labels have eta=+1.
For the EMPTY controller frequency, the parent x-sector coefficients are

    u_T=t sigma_T-delta(1+eta_T)/4,
    v_T=-delta(1+eta_T)/4.

On eta=+1 these become u=t sigma-delta/2, v=-delta/2.
Each such row has v^2=delta^2/4 and total mass >=delta/4, since
|u|>=t-delta/2>=t/2. Its entropy contribution is therefore at least

    v^2 log2((u^2+v^2)/v^2)>=m delta^2/4.

There are 2^(m-1) such rows, giving at least m delta/8. For NONEMPTY
controller frequencies u=v (up to a common sign), since the baseline
z b has no such coefficient. Their derivative mass is the remaining
d-delta/8=3delta/8, so their binary entropy is exactly3delta/4.
Consequently the true spectral erasure, not the marginal h2(d), obeys

    B_x(F)>=3delta/4+m delta/8,
    B_x(F)/d>=3/2+m/4.                                  (3)

The actual entropy decrement D_x=H(F)-[H(F|x=0)+H(F|x=1)]/2 equals
B_x+JS_x>=B_x. Combining (2),(3) proves for EVERY fixed finite K,lambda>=0

    [D_x-lambda release]/d>=m/4+(3/2)(1-lambda).           (4)

Choosing an even m>4K+6(lambda-1) refutes the explicit local rule
D_x<=K d+lambda release. In particular m=18 already has
B_x>4d+release by the rational lower bound. The family has three distinct
nonconstant shared-data cores and two actual nested point selectors;
it is not the source's constant-core AND2 guard or a formal spectral law.

## Vanishing-influence rare family and retained terminals

Let V be a fresh compatible point indicator of width t, and define each
terminal core Gj=1+V(gj-1). The SAME three controller labels select
F_t=1+V(F-1); all Gj remain distinct and nonconstant. The bank and x
query have

    d_t=2^-t d, release_t=2^-t release,
    B_x(F_t)=2^-t B_x(F), D_x(F_t)=2^-t D_x(F).           (5)

The influence scaling follows directly from point activation. For the
bank release, each data x-edge is pivotal only when V is active. For
erasure, each original data Fourier row contains z and hence is nonempty:
all V-frequency lifts multiply its two sector masses by 2^(-2t), and
there are 2^t such labels. The exceptional all-empty data row has zero
x-derivative because both x-children are balanced. Thus it contributes no
erasure. For entropy decrement, the activation formula is
H(1+V(h-1))=2^-t H(h)+A(t) for every balanced h, where A(t) is independent
of h. Both actual x children are balanced, giving the final equality.
This proves (5) without confusing physical weights and spectral labels.

Take t=m. Then dimension is2m+4, P(F_m=-1)=2^(-m-1), and
I(F_m)=2^-m[I(F)+m] tends to zero. The unbounded ratio (4) persists.
Complete activated terminal entropy remains sum_j pi_j H(Gj), never zero
by fiat. The terminal bank is conditioned from the same three Gj.

## Scope and full FEI remain open

F has support on at most2^(m+3) spectral labels (the balancing z merely
shifts labels), so H(F)<=m+3. Equation(1) gives I(F)>=1+m/2, hence
H(F)<3I(F) for m>=4. The fresh activation has constant-child controls;
their exact entropy formula gives B/d<3, and JS<=2d/ln2<3d. Retaining
2^-t H(F) proves H(F_t)<6I(F_t). These are paid actual Boolean families.

To reconstruct these elementary activation constants, the constant-child
parent pair has exact erasure
B/d=2(1-d)+Psi(d^2,(1-d)^2)/d. The entropy remainder gives the upper
bound 2+d[log2(e)-2+2log2(1/d)]; maximizing the variable term over d>0
gives log2(e)/sqrt(e)<1. For JS, its scalar natural-log Jensen gap on
masses p,q is at most (sqrt(p)-sqrt(q))^2/2. With
x=(p-q)/(p+q), this follows by differentiating
artanh(x)<=x/sqrt(1-x^2) on [0,1) and symmetry. For signed Fourier child
amplitudes, (|a|-|b|)^2<=(a-b)^2 and their squared difference sums to4d,
so JS<=2d/ln2<3d. The influence telescope removes exactly
t*2^-t from a balanced activation and retains2^-t I(F). Combined with
H(F)<3I(F), this proves the stated complete rare-family certificate.

Therefore this result refutes ONLY the proposed fixed-rate local mixed-
data-query payment using queried influence and released fixed bank alone.
It does not refute R_star conservation, the source's control-only entropy
theorem, a different selected query, use of genuinely unused child slack,
or a universal stopping route. The remaining root bank after this query
is positive and of order m delta; it cannot be silently counted as released.
A021's logarithmic contrast warning is consistent with this calculation;
the new conclusion is its exact conversion to a three-label conserved
release-price obstruction under the original physical terminal weights.

First unsupported universal line: pay the dimension-growing x-query
residual from one genuinely unused inherited certified child/terminal
surplus, retaining the fixed remaining bank and both actual child bills,
or select a paid controller/core query avoiding that residual. The family
does not deny either possibility.
