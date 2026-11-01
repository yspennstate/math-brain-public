# Exact sector eligibility after ordinary prefixes

All logarithms are base 2. Cubes are finite, physical outcomes are fair, and
Fourier probabilities are squared normalized real Fourier coefficients. Every
reference is a normalized probability law; every kernel uses the fair extension
on every source-zero erased row. No reference-only mass is discarded.

## 1. State and initial conditions

Let g,h be arbitrary Boolean functions on the same n-bit cube, n>=0, and set
F(u,v,y)=g(y) for v=0 and F(u,v,y)=(-1)^u h(y) for v=1. Write p_0=p_g,
p_1=p_h. The source spectrum is P(b,c,T)=p_b(T)/4, b=s_u,c=s_v.
Start with ANY reference of the form

    Q(b,c,T)=w_b R_b(T)/2,  w_b>0, w_0+w_1=1,

where each R_b is normalized and supports p_b. This hypothesis is on the FULL
reference, including source-zero atoms. It holds at the genuine marginal
product root, where w_b=1/2 and R_0=R_1=product Ber((Inf_j g+Inf_j h)/2).
The initial KL K is supplied and already booked; no influence bound on it is
assumed. Independent old consumption omega is never refunded.

Take any adaptive ordinary history querying only y coordinates, before v or u.
At every resulting node the same representation holds with the actual Boolean
restrictions g_rho,h_rho, actual normalized conditional references R_b,rho and
updated weights w_b,rho. Indeed the ordinary coherent kernel is independent
of c within each b sector, including its fair zero-row extension. If t_b(e)
is the prediction in sector b, then the full prediction is t(e)=sum_b w_b t_b(e),
w'_b=w_b t_b(e)/t(e), and R'_b is the actual normalized sector transport.
Every t_b(e) is positive because R_b supports a Boolean source with both
physical outcomes of probability 1/2. No independence of the core coordinates
or product structure of R'_b is asserted.

## 2. Exact protected-pivot reset bill

At any such node put a_b=R_b(supp p_b), D_b=KL(p_b||R_b),
T_b=TC(p_b), L_b=D_b-T_b, and

    r_0=1/2+(w_0 a_0-w_1 a_1)/2, r_1=1-r_0,
    c_b=log(w_b/r_b), J_b=c_b-L_b.

Query v. Its actual outcome law is fair, its prediction is r, and its erasure
KL credit E_v is exactly zero. The inherited child KL is

    K_b=D_b+log(r_b/w_b),

so replacing that FULL inherited reference by the child's actual marginal
product has signed debit T_b-K_b=J_b. The surviving u indicator is deterministic
in each child, so it contributes zero marginal entropy. This formula retains
all reference-only child mass. On positive source atoms its inherited mass is
w_b R_b(T)/r_b; no formula for a reference-only atom is silently substituted.

If each child may independently retain its inherited reference or install its
actual product, the EXACT least extra reserve at this node is

    B=( [c_0-L_0]_+ + [c_1-L_1]_+ )/2.                 (1)

Necessity follows by resetting precisely the positive-debit children and
stopping there. Sufficiency follows by assigning child potential
K_b+[J_b]_+=max(K_b,T_b) before the choice and its chosen actual KL afterward.
Any subsequent finite physical query tree using inherited references is paid
by current KL. No second reset is included.

Here a_b>0 implies r_b>w_b/2. Moreover (w_0-r_0)+(w_1-r_1)=0,
so at most one c_b is positive and each c_b<1. Therefore

    B <= ([-L_0]_+ + [-L_1]_+)/2
         + ([c_0]_+ + [c_1]_+)/2
      <= ([-L_0]_+ + [-L_1]_+)/2 + 1/2.              (2)

The weak half-bit constant is the sharp uniform supremum: for even n>=4 take
g=(-1)^(y_0(y_1+...+y_(n-1))) and h=(-1)^(y_0 y_1+y_2 y_3+...).
Both have every influence 1/2. The rank-two star quadratic has four uniform
spectral atoms, while the tensor of bent pairs has a uniform full spectrum.
With the genuine product root R_b=uniform and w_b=1/2, L_b=0,
a_0=2^(2-n), a_1=1 and B=(1-log(1+2^(2-n)))/2 tends to 1/2.
If each R_b is a
product law, L_b=sum_j KL(Ber(Inf_j g_b)||Ber(R_b marginal_j))>=0, so B<=1/2
even when the two products differ and w is not fair. At the genuine product
root this recovers the earlier theorem. After ordinary prefixes, the signed
L_b must be measured again; root product eligibility is not hereditary.

The coefficient of the average negative eligibility loss in (2) cannot be
reduced: if g=h, w=(1/2,1/2), R_0=R_1=R, then r=(1/2,1/2), c=0 and
B=[TC(g)-KL(p_g||R)]_+ exactly. A061's genuine-product-root prefix family
realizes arbitrarily large positive values of this last quantity.

For clarity, branch selection costs more than an endpoint average:

    mean J_b = O_v-KL(fair||w)-mean L_b,
    B=mean J_b+mean[-J_b]_+,

where O_v=KL(fair||r). Neither mean J nor O_v alone is the pending reserve.

## 3. Global potential, all cuts, and boundary terms

Fix any FINITE declared ordinary prefix tree, with a subset of its nodes at
which pivot-now is admitted. Keeping the current reference and stopping is
always admitted. At leaves pivot-now is admitted or only retention is admitted.
At a node with no ordinary continuation set G=max(0,B) if pivot is allowed,
and G=0 otherwise. Backward recursively set

    G_rho=max(0, B_rho if admitted,
                 mean_e G_rho,e - E_rho,i if continuation i admitted).

For multiple declared continuation directions take their maximum. E_rho,i is
the FULL actual common-kernel KL erasure credit, which is nonnegative; it is
not replaced by an entropy erasure or clipped signed reset price. This is a
finite backward definition, with no convergence or optional-stopping limit.

The potential is current K+G before the pivot, K_b+[J_b]_+ after the pivot
and before the reset choice, and current K after that choice. At every ordinary
node K=E+O+mean K_child, so its expected drop is at least O. At the pivot,
K=O_v+mean K_b because E_v=0, and (1) supplies exactly the branch-choice bill.
Thus at EVERY stopping cut tau of EVERY admitted policy, including cuts before
the pivot, between pivot and reset, immediately after reset, or later,

    E K_tau + E sum_{queries before tau} O <= K_root+G_root.       (3)

Adding E H(F_tau) to BOTH sides gives the full terminal cross-entropy statement;
H is not an entropy-free boundary. Any omitted nonnegative erasure credits
only strengthen (3). G is the least nonnegative extra reserve for these declared
actions and immediate stopping cuts: each maximum is forced by an available
action, and finite backward induction constructs an attaining policy.

If one original owner S is supplied, sufficient initial funding is
S-omega-K_root>=G_root. If theta was already reserved for a nested subclass
with the SAME root reference, G_root>=theta and only G_root-theta is topped up.
Already consumed debits remain in omega. No new owner is created at a child.
This theorem supplies an exact global debt potential, NOT a cheap universal
initial condition. Its new mathematical input is (1), the persistent conditional
sector representation, and the sharp eligibility bound (2); the KL-chain
backward induction itself is standard and is not claimed as a new telescope.

## 4. A genuinely rare branch with increasing debt potential

Use A061's l=2 source with K_0=5/2, selector prediction (1/8,7/8),
O=(1-log(7/8))/2, and B=3-log(7)/2=1+O. Add k>=1 physical dummy bits
z_1,...,z_k. Its actual product reference has the original reference on the
11-bit source and a deterministic empty Fourier set on these dummy bits.
Query the dummy bits in order; stop retaining the reference at the first 1.
Only on the all-zero history, of physical probability epsilon=2^(-k), execute
the expensive ordinary selector, protected pivot and actual product resets.

Every dummy query has fair prediction, E=O=0 and leaves the ENTIRE normalized
reference unchanged on the source coordinates. This includes source-zero
rows, whose extension is fair. This argument uses deterministic empty dummy
Fourier coordinates; it is not a tensorization claim for nontrivial factors.
The exact root reserve is epsilon B. Along the continuing zero history after
j queries the potential is K_0+2^(-(k-j))B, so it strictly increases, reaches
K_0+B, and can reach 6 after the G selector branch. The latter event has
probability 2^(-k-1). Other histories stop with the full inherited K_0.

At the declared terminal cut the exact all-k identities are

    E K_terminal = 5/2+epsilon,
    E sum O = epsilon O,
    E H_terminal = 17/2-4 epsilon,
    E K_terminal+E sum O = K_0+epsilon B.

Thus this potential really can grow on arbitrarily rare branches, with its
expected full terminal KL plus outcome cost controlled exactly by its stated
initial value. Both terminal H and KL are retained. For a SAME supplied owner
S=27/2, booked K_0 and old omega<=S/4, this uses epsilon B once and leaves
S-omega-K_0-epsilon B>S/8. The dummy bits have zero influence and do not
magically price K_0 or create an influence bound. The rare schedule is an
explicit model of permissible temporary debt growth, not a new FEI class.

## 5. Consumed obstruction and universal initial-capital obstruction

A061-FIXED-PRODUCT-ONE-PREFIX-HALFBIT-OBSTRUCTION@1 starts at a genuine product
root, takes one ordinary selector query, and then the protected pivot with
g=h in the outer construction. Its source-zero reference rows are retained.
For l>=2, r=1-2^(-l-1), the two prefix children have positive reset liabilities
l+1 and -log r, and E_selector=0. Hence G_root=(l+1-log r)/2, not 1/2.
The family has a conditional payment from its SAME supplied original owner;
it is not an FEI counterexample and says nothing against a good existential
query order. An independent direct finite check and symbolic reconstruction
are recorded in AUDIT.md and the exact output files.

Even choosing the initial reference freely cannot give K_root+G_root=O(I)
for the policy class that admits an immediate pivot and ALL actual product
stops. Indeed set g=h=f. Both pivot children have full product KL TC(f).
For ANY supporting reference, let A denote the total initial capital of an
account paying expected terminal KL plus all outcome KL at every admitted
cut. Choose the admitted cut that queries v, resets BOTH children and stops.
Its terminal bill is TC(f)+O_v, so A>=TC(f)+O_v>=TC(f). This direct terminal
necessity does not assume E_v=0 outside the sector-reference hypothesis.
In particular any valid account A=K_root+G_root must satisfy this lower bound;
no extra-reserve formula from section2 is applied to a general reference.
For an explicit unbounded-ratio family let point_m=1-2*1[x=0] and d=2^(1-m).
Its influences are all d, its spectrum is (1-d)^2 at empty and d^2 at all
nonempty atoms. Thus M>=md(m-1) and H<=2d(2m+1), using
-log(1-d)<=d/((1-d)ln 2). Tensor N=1/d independent copies to form f_m.
Exact source tensor additivity yields I(f_m)=m and
TC(f_m)>=m^2-5m-2. The fresh bent extension has I(F_m)=m+1, so

    (K_root+G_root)/I(F_m) >= (m^2-5m-2)/(m+1) -> infinity.

This is an obstruction to universally cheap INITIAL funding of the full
product-stop class, for every starting reference, not merely failure of an
extra reserve when a reference is given. It is not an FEI counterexample:
in fact H(F_m)<=4m+4=4I(F_m) by the same entropy bound.

The first unsupported line for full FEI must therefore concern a narrower,
explicitly selected set of eligible reference changes and a payment of full
terminal entropy from a SAME influence-priced original account. It cannot
assert a cheap account for every product stopping cut of an arbitrary core.
The exact sector formula and signed recursion quantify the admissibility
test, but do not supply this selected universal entropy/reference policy.
