SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 02, slot B19, 2026-09-22T23:10:07Z.
attacking: the high-normalized-leverage near-span interface — replace the small-leverage MSS gate by an exact disjoint-basis volume average, then use the current partner's aggregate rank-one-bank theorems to isolate the remaining heavy physical core.

# fleet02/B19 r21 — disjoint-basis cross-cut and heavy-core reduction

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Universal proof assembly / SYNTHESIS  
**Owner control consumed:** revision `2026-09-22.15`  
**Classification:** `ESSENTIAL_STEP_APPLIED / SUPPORTING TARGET-LEVEL BRANCH PROVED / FULL TARGET OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

The owner target is unchanged: independent original-coordinate real inputs with marginal densities at most one, arbitrary finite dimension, and an arbitrary real symmetric matrix with at least three eigenvalues of modulus at least one. No moment, support, log-concavity, diagonal-basis or post-rotation-independence hypothesis is introduced.

The live correction set was consumed before the derivation: no arbitrary-joint coarea bound, conditional projection-density moment, conditional-cap-as-independence step, law-uniform pointwise Fresnel decay, fixed-good-minor extraction, or small-coefficient perturbative deletion is used.

## 1. Source-valid state and dependencies

The immediate state is fleet02/B19 r20, canonical source

`yspennstate/math-open-problems@4a4682f27ee74da65f62c20fc4520e81b48bece6`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B19/20260922T221019Z-fleet02-B19-qform-r20/REPORT.md`.

In the exact-rank-three heavy-null compression,

`A=R M R^T`, `R^T R=I_3`, `D=|det M|>=1/2`,

there is an original-coordinate row

`u_0=sqrt(c) r`, `r^T M r=0`, `c>=7/9`.

For the `c<=61/64` near-span chamber put

`H=I-u_0u_0^T`, `z_j=H^(-1/2)u_j` for `j!=0`.

Then

`sum_(j!=0) z_jz_j^T=I_3`,

and the normalized complement leverages are

`ell_j=||z_j||^2=u_j^T H^(-1)u_j`.

r20 paid the small-leverage region by MSS. The present run replaces that gate by a stronger elementary volume average.

The **current named partner** is fleet03/B19 r19, canonical source

`yspennstate/math-open-problems@39b2d7a6fc503f2abbeee3b50c30ed64886de365`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B19/20260922T223200Z-fleet03-B19-QFORM-r19/REPORT.md`.

I use two proved partner theorems exactly as stated there:

1. `QFORM-RANKONE-BANK-SCHUR-PIVOT-v1`: a rank-one original-coordinate bank with total row weight `lambda`, scalar coefficient `a!=0`, and exact-rank-three spectral determinant `D` obeys

`||p_Q||_inf <=16 sqrt(60) [lambda |a| D]^(-1/4)`.

2. `QFORM-TWO-RANKONE-BANK-PAIRLOG-v1`: for two disjoint rank-one banks with complete principal-triple determinant mass `mu`, and indefinite compressed pair block having `kappa=sigma_min(B)>0`,

`||p_Q||_inf <=C_pair (mu kappa)^(-1/4)`,

`C_pair=4 sqrt(20) 8^(1/4)<30.085`.

I also use the completed exact-cross-rank theorem pinned in r20: if a physical original-coordinate cross block `C` has exact rank three then

`||p_Q||_inf <=3e Pi_3(C)^(-1/3)`,

with arbitrary self terms and outside coordinates retained.

Finally I consume the newer compatible fleet01/B19 result

`yspennstate/math-open-problems@09bb706f11ea00995a61f0c7323bf67997c65932`,

`QFORM-INDEPENDENT-LINEAR-SQUARE-SMOOTHING-v1`, which pays the exact null-coloop endpoint `c=1` by

`||p_Q||_inf <=6e^(2/3)|det M|^(-1/3)<11.687`

in the source target chamber. Thus the previous near-unit alternative is punctured: `61/64<c<1` is still open, but the endpoint `c=1` is not.

## 2. New theorem: Parseval disjoint-basis volume cut

### Theorem 2.1 — `QFORM-PARSEVAL-DISJOINT-BASIS-CROSSCUT-v1`

Let `z_1,...,z_N in R^3` be a Parseval frame,

`sum_i z_i z_i^T=I_3`,

and let

`alpha=max_i ||z_i||^2`.

If `alpha<1/3`, then there is a bipartition of the original indices into `P,Q` such that, writing

`G_P=sum_(i in P)z_i z_i^T`, `G_Q=I-G_P`,

one has

`boxed: det(G_P) det(G_Q) >= (1-3alpha)/64.`                    (2.1)

This is an existence statement about a partition of original coordinate indices; no random variables are rotated.

### Proof

For each three-element index set `I`, put

`d_I=det(Z_I)^2>=0`,

where `Z_I` is the `3x3` matrix with rows `z_i`, `i in I`. Cauchy--Binet gives

`sum_I d_I=det(sum_i z_i z_i^T)=1`.                              (2.2)

Choose a Bernoulli `1/2` random bipartition `P,Q`. Again by Cauchy--Binet,

`det(G_P)=sum_(I subset P) d_I`,
`det(G_Q)=sum_(J subset Q) d_J`.

Therefore

`E[det(G_P)det(G_Q)]`
` = 2^(-6) sum_(I cap J=empty) d_I d_J`.                         (2.3)

It remains to lower-bound the disjoint-pair mass. For every coordinate `i`, the exact marginal identity is

`sum_(I contains i) d_I=||z_i||^2=:ell_i`.                      (2.4)

One quick proof of (2.4) is to differentiate at all weights equal to one the Cauchy--Binet identity

`det(sum_j t_j z_jz_j^T)=sum_I d_I product_(j in I)t_j`:

the left derivative is `z_i^T I_3^(-1)z_i=ell_i`, and the right derivative is the displayed sum.

By the union bound on the event that two volume-sampled triples intersect,

`sum_(I cap J != empty) d_I d_J`
` <=sum_i (sum_(I contains i)d_I)^2`
` =sum_i ell_i^2`
` <=alpha sum_i ell_i`
` =3alpha`,                                                      (2.5)

since `sum_i ell_i=trace I_3=3`. Combining (2.2)--(2.5),

`sum_(I cap J=empty)d_Id_J >=1-3alpha`.

Thus the expectation in (2.3) is at least `(1-3alpha)/64`; some deterministic partition attains at least its expectation. QED.

The proof is elementary Cauchy--Binet plus averaging. It does not require the MSS theorem and works up to normalized leverage strictly below `1/3`.

## 3. Target-level application to the heavy-null near-span chamber

Apply Theorem 2.1 to the normalized complement frame from Section 1. For the resulting original-coordinate partition `P,Q`, let `U_P,U_Q` have physical spectral rows `u_j`. Because

`U_P^T U_P=H^(1/2)G_P H^(1/2)`,

and `det H=1-c`,

`det(U_P^TU_P)det(U_Q^TU_Q)`
` =(1-c)^2 det(G_P)det(G_Q)`.                                  (3.1)

The physical cross block is

`C=A[P,Q]=U_P M U_Q^T`.

Whenever `alpha<1/3`, (2.1) is positive, so both sides have column rank three and `C` has exact rank three. Its singular-value product is

`Pi_3(C)=D sqrt(det(U_P^TU_P)det(U_Q^TU_Q))`
` >= [D(1-c)/8] sqrt(1-3alpha)`.                               (3.2)

The exact-cross-rank theorem therefore gives

`boxed: ||p_Q||_inf`
` <=3e [ D(1-c) sqrt(1-3alpha)/8 ]^(-1/3).`                    (3.3)

This is a continuous-density bound in this branch.

A convenient fixed threshold is `alpha<=1/4`. Then

`sqrt(1-3alpha)>=1/2`.

Using `D>=1/2` and `1-c>=3/64`,

`Pi_3(C)>=3/2048`,

and hence

`boxed: alpha<=1/4, c<=61/64 => ||p_Q||_inf<71.805.`            (3.4)

This strictly enlarges r20's normalized-diffuse chamber: the previous elementary numerical application used `alpha<=1/16`, while the new theorem gives a fixed target-level payment through `alpha<=1/4`, and in fact gives a quantitative bound for every `alpha<1/3`.

## 4. Apply the current partner to the first surviving high-leverage row

Suppose now `c<=61/64` and the new cross-cut payment fails at the fixed threshold, so some row `j!=0` has

`ell_j>1/4`.                                                     (4.1)

Write orthogonally

`u_j=a r+z`, `z perpendicular r`.

Because

`H^(-1)=(1-c)^(-1)rr^T+P_(r perp)`,

`ell_j=a^2/(1-c)+||z||^2`.                                      (4.2)

There are two exact alternatives.

### 4.1 Transverse-heavy row

Assume

`||z||^2>1/8`.                                                   (4.3)

Define the complete physical principal-triple determinant mass through the two singleton banks `{0}` and `{j}`:

`mu_(0j)=sum_(k notin {0,j}) |det A[{0,j,k},{0,j,k}]|`.         (4.4)

Because `A=RMR^T`, every principal triple satisfies

`|det A_I|=D det(R_I)^2`.

Let `n=u_0 cross u_j`. Then `n` is orthogonal to `u_0,u_j`, and Parseval gives

`sum_(k notin {0,j}) det(u_0,u_j,u_k)^2`
` = n^T (I-u_0u_0^T-u_ju_j^T)n`
` =||n||^2`
` =c||z||^2`.                                                    (4.5)

Therefore the exact aggregate identity is

`boxed: mu_(0j)=D c ||z||^2.`                                   (4.6)

Using `D>=1/2`, `c>=7/9` and (4.3),

`boxed: mu_(0j)>7/144.`                                         (4.7)

This spends no reciprocal local minor: the entire completion bank is retained.

Let

`B=A[{0,j},{0,j}]=[[0,b],[b,q]]`,

where `b=A_(0j)`, `q=A_(jj)`, and put `kappa=sigma_min(B)`.

If

`kappa>=1/64`,                                                   (4.8)

then `B` is automatically invertible indefinite (its upper-left entry is exactly zero), so the named partner's two-rank-one-bank pair-log theorem applies with (4.7):

`||p_Q||_inf`
` <=C_pair ((7/144)(1/64))^(-1/4)`
` <181.222.`                                                     (4.9)

Independently, apply the partner's rank-one-bank Schur-pivot theorem to the singleton bank `{j}`. Its row weight is `lambda=||u_j||^2`, its scalar coefficient is exactly `q=A_jj`, and define

`theta_j=||u_j||^2 |q| D`.                                      (4.10)

If

`theta_j>=1/4096`,                                               (4.11)

then

`||p_Q||_inf <=128 sqrt(60)<992`.                               (4.12)

Consequently every still-unpaid transverse-heavy state satisfies both

`kappa<1/64`, `theta_j<1/4096`.                                 (4.13)

Since `||u_j||^2>=||z||^2>1/8` and `D>=1/2`, (4.13) implies

`boxed: |A_jj|<1/256.`                                          (4.14)

For `B=[[0,b],[b,q]]`, its smaller singular value is

`kappa=(sqrt(q^2+4b^2)-|q|)/2`,

so exactly

`b^2=kappa(kappa+|q|)`.

Combining (4.13)--(4.14) gives

`boxed: |A_0j|<sqrt(5)/128=0.0174693... .`                      (4.15)

Thus the entire unpaid transverse-heavy chamber is compressed to a **double-near-null physical pair carrying a large aggregate O3 completion bank**:

`mu_(0j)>7/144`, `|A_jj|<1/256`, `|A_0j|<sqrt(5)/128`.          (4.16)

### 4.2 Longitudinal-heavy row

If (4.3) fails, then (4.1)--(4.2) force

`a^2/(1-c)>1/8`.                                                (4.17)

Across all complementary rows,

`sum_(j!=0) a_j^2=1-c`.

Hence there can be **at most seven** original-coordinate rows satisfying (4.17). This makes the other surviving high-leverage mechanism a finite longitudinal-heavy physical core, rather than an unrestricted diffuse-frame problem.

The partner scalar-bank theorem may of course remove any of these rows whenever its `theta_j` exceeds `1/4096`; the statement above records only the source-independent finite-cardinality consequence needed for the next synthesis step.

## 5. Updated conditional proof and first unpaid implication

A correction-safe end-to-end route is now:

1. retain the completed ridge/window, low-offdiagonal, physical-pivot, grouped-square and exact-cross-rank payments at their stated scopes;
2. use fleet03/B19's sequential and rank-one-bank payments before entering the exact heavy-null near-span chamber;
3. use B19 r19 and fleet03/B10's aggregate O3 result to remove the leakage-residual discontinuity;
4. in `c<=61/64`, use Theorem 2.1 here to pay every normalized complement with `max ell_j<=1/4` (indeed every `max ell_j<1/3` quantitatively);
5. in the remaining high-leverage state, use Section 4 plus the **current named partner fleet03/B19 r19**: every transverse-heavy row is either paid or becomes the explicit double-near-null/O3 packet (4.16), while the longitudinal-heavy rows form a set of cardinality at most seven;
6. use fleet01/B19's newer direct linear-square theorem to remove the exact near-unit endpoint `c=1`.

Therefore the first unpaid exact-rank-three implication is now:

### `QFORM-NEARSPAN-HEAVYCORE-OR-PUNCTURED-NEARUNIT-v1` — OPEN

In the source-valid small-leakage heavy-null state, prove a universal density bound, unless an already-paid packet occurs, in the union of:

**(A)** `c<=61/64`, `max ell_j>1/4`, after the partner payments, where every surviving high row belongs to one of the two explicitly quantified classes:

- a longitudinal-heavy core of at most seven original coordinates satisfying `a_j^2/(1-c)>1/8`; or
- a transverse row satisfying the double-near-null/O3 certificate (4.16);

and

**(B)** the genuinely punctured near-unit chamber

`61/64<c<1`.

A valid closure must keep original-product provenance. In particular, (4.15) is **not** permission to delete the small pair coefficient, and the punctured near-unit complement cannot be replaced by a merely conditionally bounded effective scalar. Those shortcuts are already refuted by the live corrections and the fleet01/B19 counterexample.

This is a strict reduction of r20's first missing implication: the normalized-diffuse threshold has moved from the MSS scale to `1/4` (quantitatively to every `alpha<1/3`), and the high-leverage survivor is now a finite/heavy physical core plus a specific aggregate O3 double-near-null packet.

The full arbitrary-matrix target remains open because the source-valid reduction from arbitrary additional spectrum into these exact-rank-three chambers is still incomplete. No full-proof claim is made, and two independent end-to-end reviews do not exist.

## 6. Verification status

`CHECK.py` and `CHECK.txt` in this run directory verify an exact repeated-axis Parseval test of the disjoint-basis averaging identity and the numerical constants `71.805`, `181.222`, `1/256`, and `sqrt(5)/128`. The checker is regression evidence only; the proof is the exact Cauchy--Binet/partner argument above.
