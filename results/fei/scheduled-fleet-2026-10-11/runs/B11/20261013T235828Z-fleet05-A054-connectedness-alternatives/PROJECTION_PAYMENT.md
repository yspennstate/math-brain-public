# Physical projection credits pay component cross terms

Bits throughout. Write F(h)=sum_s hhat(s)^2 log2(1/hhat(s)^2),
M(h)=E h² and E_A(h)=sum_s |s_A|hhat(s)^2. Put kappa=2/ln2.
These are raw quantities for indicators; sign influence is I(1-2g)=4E(g).

## 1. Cross term and terminal correction

For a queried physical block A and C=A^c, set
v_t(x)=E_y h(x,y)chi_t(y), q_t=E_x v_t(x)² and

    B_A(h)=sum_t q_t H((hhat(e,t)²/q_t)_e),
    Jraw_A(h)=sum_t Ent_x(v_t²)/ln2,
    Lambda_A(h)=B_A(h)+Jraw_A(h).

Zero rows vanish. Expansion gives F(h)-average_x F(h_x)=Lambda_A(h),
and the supplied two-point log-Sobolev proof from stage 1 gives
Jraw_A(h)<=kappa E_A(h). For completeness, the analytic bound is
standalone: for a nonnegative two-point function (t,1), twice the
Dirichlet-minus-entropy difference is
G(t)=(t²+1)ln((t²+1)/2)-2t²ln t+(t-1)². G(1)=0, and for t>=1 its
derivative is nonnegative because
1-1/t-ln(2t²/(t²+1)) has derivative (t-1)²/[t²(t²+1)] and vanishes at one.
The symmetry G(t)=t²G(1/t) and continuity cover the other cases. Entropy
tensorization, obtained by conditioning and convexity of the entropy
functional on product coordinates, yields Ent(w²)<=2sum_i||D_i w||²
for real w after applying it to |w| and using the modulus contraction.
Summing over partial Fourier rows and Parseval gives the claimed bound.
Unequal child masses are retained: Jraw/M is
channel mutual information PLUS KL of the physical marginal against uniform.

For actual connected components g=1_U=sum_k g_k define the signed block
cross term X_A=Lambda_A(g)-sum_k Lambda_A(g_k). For every block, even one
that does not separate components, there is the exact terminal-inclusive identity

    F(g)-sum_k F(g_k)
      = X_A+average_x [F(g_x)-sum_k F((g_k)_x)].           (1)

The g_k restrictions in (1) remain labelled pieces; they need not be the
connected components of the children. Do not prune or relabel them for free.
This is an identity of coherent sums of Fourier amplitudes, not a mixture.

Let R_k be the physical projection of U_k on A. If these nonempty sets
are pairwise disjoint, every A-fiber meets at most one component and
the bracketed terminal term in (1) vanishes. Such A is component-isolating.
The cross term is then the entire raw excess, and an independently defined
upper interface is

    Gamma_A=[B_A(g)+kappa E_A(g)-sum_k Lambda_A(g_k)]_+.

It satisfies F(g)<=sum_k F(g_k)+Gamma_A. Its definition uses partial
Fourier rows, conditional entropy and energy, not the unexplained gap.

## 2. Projection uncertainty credit: no product structure

Let R be a nonempty subset of the A-cube of uniform measure mu, and let
w be any real function supported on R. For q=E w²>0,

    |what(e)|² <= mu q                                (Cauchy--Schwarz).

Thus each normalized Fourier probability what(e)²/q is at most mu,
and its Shannon entropy is at least log2(1/mu). Also the density
w²/q is supported on R, so its KL from the uniform A law is at least
log2(1/mu): normalize uniform measure on R and use nonnegative KL.
Consequently

    H((what(e)²/q)_e) >= log2(1/mu),
    Ent(w²)/ln2 >= q log2(1/mu).                        (2)

Every partial-Fourier row of g_k is supported on R_k, whether or not
U_k is a Cartesian product. Let p_k=M(g_k), mu_k=|R_k|/2^r, r=|A|.
Summing (2) gives the useful lower credit

    Lambda_A(g_k) >= 2p_k log2(1/mu_k).                 (3)

Define Q_A=sum_k p_k log2(1/mu_k), p=sum_k p_k, and the explicit
nonnegative projection debt Theta_A=[rp-2Q_A]_+. Then

    X_A <= kappa E_A(g)+rp-2Q_A,
    Gamma_A <= kappa E_A(g)+Theta_A.                    (4)

The payment class consists of component-isolating proper blocks with
Q_A>=rp/2. Individual mu_k<=2^-r/2 suffice, but weighted average
projection information is the actual hypothesis. Equations (3)--(4)
prove Gamma_A<=kappa E_A on this class. The stage-1 subcube-cylinder
class is a special case with mu_k=2^-d_k; Cartesian structure, fixed
selector coordinates and uniform fiber shape are no longer required.

## 3. Indicator edge isoperimetry supplies the energy density

For an indicator u on an r-cube with mean m,

    E(u)>= (m/2) log2(1/m).                             (5)

Here is an elementary induction with the needed normalization. The
two last-coordinate children have means m0,m1; s=m0+m1. The last
coordinate energy is one quarter of their disagreement probability,
at least |m0-m1|/4. The inductive average child energy is at least
[m0 log2(1/m0)+m1 log2(1/m1)]/4. Their sum is at least
(s/4)log2(2/s) because h2(m0/s)>=2 min(m0/s,m1/s), by concavity of
binary entropy between 0 and 1/2. This is (5); s=0 is immediate.

Fix y on C. The support of (g_k)_y on A lies within R_k, and its mean
m_y<=mu_k. By (5), E_A((g_k)_y)>=m_y log2(1/mu_k)/2. Average y to get

    E_A(g_k)>= (p_k/2)log2(1/mu_k),
    E_A(g)>=Q_A/2.                                     (6)

Actual components have no cross boundary edges, so E_A(g)=sum_k E_A(g_k).
In the paid projection class (6) gives E_A(g)>=rp/4, the same density
used in stage 1, now derived without subcubes or tensor formulas.

## 4. Criticality enters only at actual child deficits

For E(g)>0, energy additivity gives the corrected comparison

    Rraw(g)<=max_k Rraw(g_k)+Gamma_A/E(g),

with nonzero-energy components only. If all proper physical restrictions
of g have F(g_x)<=Rraw(g)E(g_x), then

    Rraw(g)E_A(g)<=Lambda_A(g)<=rp+kappa E_A(g).

In the paid projection class, E_A>=rp/4>0 implies Rraw(g)<=4+kappa.
The interface bound holds even without criticality; the ratio exclusion
uses it exactly in the preceding averaged-child comparison.

For the actual sign f=1-2g, physical ratio criticality gives
R(f)I_A<=H(f)-average H(f_x)<=r+kappa I_A. Since I_A=4E_A>=rp,

    p>=p0>0 implies H(f)/I(f)<=kappa+1/p0.               (7)

In particular at 1/4<=p<=1/2 the same 4+kappa bound now covers arbitrary
non-Cartesian component shapes with the weighted projection condition.
For a least-dimensional fixed-K violator, keep its root deficit D_K>0:
KI_A+D_K<=r+kappa I_A. Thus K>=kappa+1/p0 rules out this class.
This does not claim the row phases are physical descendants, nor that
the components or the actual children inherit criticality.

## 5. Surviving universal obligation and counterexample scope

The Brain45 seven-bit and Brain44 nine-bit selector-star examples both
have slightly insufficient Q_A at their natural data separator; their
Theta_A is retained in (4). This is compatible with their positive raw
component excess. The exact partial-Fourier Gamma may be cheaper than
the projection-only upper bound, but neither is set to zero without proof.

The new all-dimensional delta is the support uncertainty credit (3) and
the energy density (6), which replace the cylinder restriction by a
weighted physical projection condition. Exact phi on Brain45 is a
mandatory control, not a universal payment or novelty claim.

First unsupported line: every dimension-minimal high-K violating sign
admits a proper component-isolating block with paid projection debt and
a uniformly positive support mass, or another proper block whose actual
cross term AND terminal deficit are paid. Connected supports have only
one component, and rare support remains allowed; no universal admission
or full FEI conclusion is obtained.
