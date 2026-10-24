# account02/B07 — mixed-overlap singular split and pivot-ridge payment

Run: `20260922T170237Z-b07-e559ca`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: Coordinate minor selection  
Classification: **ESSENTIAL_STEP_APPLIED + CANDIDATE_REFUTED (intermediate scalar-pivot extraction); FULL QFORM OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`

## 1. Conditional end-to-end argument and first unpaid implication

The exact owner target is unchanged: for arbitrary independent real coordinates with densities at most one and arbitrary real symmetric `A` with at least three eigenvalues of absolute value at least one, prove a universal essential-supremum bound for the density of `X^T A X`, or give a target-valid counterexample.

The completed designated-partner result account03/B07 r12, `QFORM-THIRD-COMPOUND-OVERLAP-REDUCTION-v1`, reduces every target matrix to one of four original-coordinate third-compound overlap packets O0/O1/O2/O3. Its O0 diffuse-ridge branch is already paid. The preceding account02/B07 run further compresses the unpaid O0 branch to at most four determinant-heavy physical rows at calibrated effective dimension three.

This run attacks the first mixed branch O1, rather than repeating O0. The first unpaid implication is now:

**`QFORM-O1-HYPERBOLIC-PACKET-PAYMENT-v1`.** Pay, with a universal density constant and without rotating the product law, a one-shared-coordinate packet whose determinant mass is carried either by the singular/near-zero scalar-pivot term

`sum_i ||u_i||^2 ||v_i||^2 ||P_(u_i perp) B P_(v_i perp)||_F^2`,

or by the finite calibrated two-row/two-column ridge-heavy obstructions left by the nonzero-pivot payment below. A proof of this plus corresponding O2/O3 and prior O0-four-heavy payments would close the partner's exhaustive overlap reduction.

The source-valid family in Section 6 shows why the singular/near-zero part cannot be discarded: O1 determinant mass may stay exactly one while its shared physical scalar pivot tends to zero.

## 2. Source-pinned completed inputs actually used

1. Designated partner account03/B07 r12, `QFORM-THIRD-COMPOUND-OVERLAP-REDUCTION-v1`: `yspennstate/math-open-problems@685929d9daee92a164dbf6ba6f9305d2e6550826`, `proofnet24/QFORM-density/fleet-2026-09-22/account03/B07/20260922T163733Z-account03-B07-qform-r12/REPORT.md`.

   In particular, its O1 alternative supplies an original-coordinate three-color partition `C,L,R` with

   `sum_(i in C) sum_(|S|=|T|=2, S subset L,T subset R) det A[{i} union S,{i} union T]^2 >= 1/972`.

   Its O2 alternative analogously supplies a two-shared-coordinate aggregate at least `1/324`.

2. account03/B09 `QFORM-PIVOT-RIDGE-BILINEAR-v1`: `yspennstate/math-open-problems@62bdcf30669c1037a3c7d87aee1fcb2bdcccd251`, `proofnet24/QFORM-density/fleet-2026-09-22/account03/B09/account03-B09-20260922T155042Z-qform12/REPORT.md`.

   If a physical scalar pivot `a!=0` is completed out, a residual original-coordinate cross block `N` with ridge kernel `K=N N^T(gamma^2 I+N N^T)^(-1)`, `theta=tr K`, and `max diag K<=q/2`, `theta>q`, gives an essentially bounded density for the full form. All other self blocks and outside couplings are retained. I apply its exact `q=1`, `theta=3/2`, `r=5/3` formula below.

3. Prior account02/B07 state: `yspennstate/math-open-problems@059c2aefcc283898976e9e207fcc01049b85fb97`, same worker path for run `20260922T163428Z-account02-B07-QFORM-r12`. It pays the O0 calibrated ridge-diffuse branch or leaves at most four determinant-heavy physical rows. No claim from that run is promoted to O1/O2 without a new derivation here.

Corrections respected: no law-uniform pointwise Fresnel decay, no post-rotation independence, no unrestricted fiber supremum, no single-good-minor inference, no single Schur-rank-two extraction, and no normalized conditional spectral-density cap.

## 3. O1 exact exterior identity, including zero scalar pivots

Fix the partner's O1 partition `C,L,R`. For `i in C`, define

`a_i=A_ii`, `u_i=A[L,i]`, `v_i=A[i,R]^T`, `B=A[L,R]`.

For `S subset L`, `T subset R`, `|S|=|T|=2`, put

`h_i(S,T)=det A[{i} union S,{i} union T]`

and let `H_i` be the matrix with these entries, indexed by coordinate two-subsets.

Let `C_2(B)` be the second compound of `B`. Let `iota_v : wedge^2 R^R -> R^R` be contraction with `v`, with

`iota_v(e_t1 wedge e_t2)=v_t1 e_t2-v_t2 e_t1`,

and let `W_u(z)=u wedge z`. Direct expansion of the `3 x 3` determinant gives the inverse-free operator identity

`boxed( H_i = a_i C_2(B) - W_(u_i) B iota_(v_i). )`            (3.1)

Indeed for `S={s1,s2}`, `T={t1,t2}` the second term is

`v_t1(u_s1 B_s2,t2-u_s2 B_s1,t2)
 -v_t2(u_s1 B_s2,t1-u_s2 B_s1,t1)`,

which is exactly the non-pivot part of the Laplace expansion.

The Hilbert-Schmidt norm of the singular term has the exact invariant form

`boxed(
 ||W_u B iota_v||_HS^2
 = ||u||^2 ||v||^2 ||P_(u perp) B P_(v perp)||_F^2.
)`                                                               (3.2)

Proof: if `u` or `v` vanishes both sides vanish. Otherwise choose orthogonal bases only for this deterministic norm calculation so `u=||u||e_1`, `v=||v||e_1`. Contraction kills `wedge^2(v perp)` and sends `e_1 wedge e_j` to `||v||e_j`; wedging with `u` removes exactly the `u`-parallel component of `B e_j`. Summing the squared norms over `j>1` gives (3.2). No random variable is rotated.

Therefore if

`W_i := ||H_i||_HS^2`, `E_2(B):=||C_2(B)||_HS^2=e_2(BB^T)`,

then

`W_i <= 2 a_i^2 E_2(B)
       +2 ||u_i||^2||v_i||^2||P_(u_i perp) B P_(v_i perp)||_F^2`. (3.3)

Summing (3.3) over the partner's O1 packet `sum_i W_i>=1/972` proves the dimension-free aggregate dichotomy

`boxed(
 E_2(B) sum_i a_i^2 >= 1/3888
)`                                                               (3.4a)

or

`boxed(
 sum_i ||u_i||^2||v_i||^2||P_(u_i perp) B P_(v_i perp)||_F^2
 >=1/3888.
)`                                                               (3.4b)

In particular, if all shared scalar pivots vanish, the entire O1 packet is exactly the hyperbolic resource in (3.4b), not an error term.

## 4. Nonzero O1 pivot: exact Schur packet and calibrated ridge payment

Assume now `a=a_i!=0`. Let

`N_i = B-u_i v_i^T/a`,

the `L x R` cross block of the scalar Schur complement after completing the original physical coordinate `i`. The rank-one determinant lemma on every `2 x 2` subblock gives the exact identity

`boxed( H_i = a C_2(N_i), )`                                    (4.1)

hence

`boxed( W_i = a^2 E_i,  E_i:=e_2(N_i N_i^T). )`                 (4.2)

Suppose `W_i>0`, so `rank N_i>=2`. Calibrate `gamma>0` by

`theta(gamma)=tr[N_i N_i^T(gamma^2 I+N_i N_i^T)^(-1)]=3/2`.      (4.3)

Such a `gamma` exists because the trace decreases continuously from `rank N_i>=2` to zero. Let

`k_j=s_j^2/(gamma^2+s_j^2)`, `y_j=s_j^2/gamma^2=k_j/(1-k_j)`.

For independent Bernoulli variables with means `k_j`,

`e_2(k)=E binom(N,2) >= E(N)-1 =1/2`,                            (4.4)

because `binom(m,2)>=m-1` for every integer `m>=0`. Since `y_j>=k_j`,

`E_i/gamma^4=e_2(y)>=e_2(k)>=1/2`, so `gamma^4<=2E_i`.           (4.5)

Also

`D:=det(I+N_iN_i^T/gamma^2)=prod_j(1+y_j)>=e_2(y)=E_i/gamma^4`. (4.6)

Now assume either the row ridge leverage of `N_i` or the column ridge leverage of `N_i` at this same calibrated `gamma` is at most `1/2` coordinatewise. Swap the two residual banks if needed and apply account03/B09 with `q=1`, `theta=3/2`, `r=5/3`. Its exact formula gives

`||p_Q||_infinity
 <= C_* |a|^(-1/2) gamma^(-1/2) D^(-1/6)`,                     (4.7)

where `C_*=11.882925976348...`. Using (4.5)-(4.6),

`||p_Q||_infinity
 <= C_* 2^(1/24) |a|^(-1/2) E_i^(-1/8)
 < 12.232 |a|^(-1/2) E_i^(-1/8)`

and therefore, by (4.2),

`boxed(
 ||p_Q||_infinity < 12.232 (a_i^2 W_i)^(-1/8).
)`                                                               (4.8)

This is a full-form bound: arbitrary self blocks, the remaining coordinates in `C`, all extra eigenvalues, and all outside couplings remain present through the source theorem.

If (4.8) does not apply because both row and column ridge gates fail, then on each side the set of coordinates with calibrated ridge leverage strictly greater than `1/2` has cardinality at most two, since the total ridge trace is `3/2`. Thus the nonzero-pivot O1 residual is reduced to a **two-heavy-row / two-heavy-column calibrated obstruction**, rather than a request to invert one tiny physical minor.

## 5. O2 exact adjugate identity and singular pair split

For completeness, the adjacent O2 branch also has an inverse-free packet identity. Fix a shared physical pair `I={i1,i2} subset C` and put

`P=A[I,I]`, `U=A[L,I]`, `V=A[I,R]`, `B=A[L,R]`.

Let `G_I` be the `L x R` matrix

`G_I(j,k)=det A[I union {j}, I union {k}]`.

Expanding the bordered determinant gives

`boxed( G_I = det(P) B - U adj(P) V. )`                         (5.1)

This is valid with no invertibility assumption.

* If `det(P)!=0`, then `G_I=det(P)(B-U P^(-1)V)`, exactly the pair-Schur cross numerator.
* If `rank(P)=1`, write `P=lambda w w^T` with `||w||=1` and unit `w_perp`. Then `adj(P)=lambda w_perp w_perp^T`, so

  `G_I=-lambda (U w_perp)(w_perp^T V)` and

  `boxed( ||G_I||_F^2=lambda^2 ||U w_perp||^2 ||V^T w_perp||^2. )` (5.2)

* If `P=0`, then `G_I=0`.

Therefore the partner's O2 aggregate `sum_I ||G_I||_F^2>=1/324` splits exactly into invertible pair-Schur packets and rank-one null-direction hyperbolic products; a singular pair is not handled by an unjustified inverse or limiting convention.

## 6. Source-valid counterexample to scalar-pivot extraction from O1 mass

The O1 aggregate cannot by itself force a quantitatively nonzero shared scalar pivot. For `0<=epsilon<=1`, take the symmetric `5 x 5` matrix

`A_epsilon =`

`[[epsilon,1,0,1,0],`
` [1,      0,0,0,0],`
` [0,      0,0,0,1],`
` [1,      0,0,0,0],`
` [0,      0,1,0,0]].`

Its spectrum is

`{ (epsilon+sqrt(epsilon^2+8))/2,
   (epsilon-sqrt(epsilon^2+8))/2,
   0, 1, -1 }`.

For `0<=epsilon<=1` at least four eigenvalues have absolute value at least one, so this lies inside the full owner target.

Take `C={0}`, `L={1,2}`, `R={3,4}`. The unique O1 determinant is

`det A[{0,1,2},{0,3,4}]
 = det [[epsilon,1,0],[1,0,0],[0,0,1]]=-1`,                    (6.1)

so `W_0=1` for every epsilon. Yet the shared pivot is `a_0=epsilon`. For `epsilon>0`,

`N_0=diag(-1/epsilon,1)`, `E_0=1/epsilon^2`, `W_0=epsilon^2 E_0=1`,

and the scale controlling (4.8) is `a_0^2 W_0=epsilon^2 ->0`. At `epsilon=0` the scalar Schur complement is undefined but the inverse-free identity (3.1) gives the same determinant exactly through the hyperbolic term.

Thus the intermediate implication

`fixed O1 determinant mass => dimension-free nonzero scalar-pivot scale`

is **false inside the target**. This is not a counterexample to QFORM; it identifies the necessary near-zero/hyperbolic payment branch.

## 7. Exact verification

`CHECK.py` and `CHECK_OUTPUT.txt` in this run directory verify with exact rational arithmetic:

* (3.1) on all nine O1 minors of a deterministic integer fixture;
* (3.2) by an inverse-free projection identity;
* (5.1) on all nine O2 minors;
* (5.2) on an exact rank-one pair pivot;
* the calibrated `theta=3/2` elementary-symmetric inequalities;
* the inherited constant `12.231122285324<12.232`;
* the target-valid near-zero family and its exact O1 minor `-1`.

Terminal marker: `STATUS=QFORM_MIXED_OVERLAP_SINGULAR_SPLIT_CHECK_PASS`.

## 8. Status

* `QFORM-O1-COMPOUND-SCHUR-FACTOR-v1`: **PROVED**.
* `QFORM-O1-PIVOT-RIDGE-PAYMENT-v1`: **PROVED conditional full-form payment**, using account03/B09 under its exact calibrated leverage gate.
* `QFORM-O2-ADJUGATE-SINGULAR-SPLIT-v1`: **PROVED structural identity**.
* `QFORM-O1-PIVOT-SCALE-FROM-MASS`: **REFUTED as an intermediate inference** by the target-valid family (6.1).
* O1 singular/near-zero hyperbolic packet, O1 finite ridge-heavy core, O2 aggregate payment, O3 aggregate payment, and prior O0 four-heavy payment: **OPEN**.
* Full QFORM: **OPEN / NOT PROVED / NOT DISPROVED**.

No post-rotation independence, moment/support hypothesis, benchmark answer, scheduler mutation, email, notification, public workflow, paid model/API, cross-account authentication, or permission expansion is used.
