SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B08, 2026-09-22T21:52:31Z.
attacking: fractional-ridge L3 smoothing for arbitrary higher-rank cross tails, plus a no-moment falsifier for small-tail characteristic-function perturbation.

# account01/B08 QFORM r18 — fractional-ridge L3 smoothing and a sharp tail-perturbation obstruction

**Outcome:** `ESSENTIAL_STEP_APPLIED / PROVED_SUPPORTING_THEOREM / REFUTED_INTERMEDIATE_MECHANISM / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Fresh coherent control source:** `yspennstate/math-research-brain@ea264205433b3ad2eb15f41dc200155e2e2574d3`, OWNER CONTROL revision `2026-09-22.15`.

The full owner target remains open: for every finite n, independent real coordinates with one-dimensional densities at most one, and every real symmetric A with at least three eigenvalues of modulus at least one, prove a universal bound on the density of X^TAX, or give a target-valid counterexample. The new positive result below proves essential boundedness only on a quantified diffuse physical-cross-range branch. It does not prove continuity. The negative result below refutes only a perturbative proof mechanism, not QFORM.

## 1. Live source corrections respected

This report does not use any of the following refuted interfaces: law-uniform pointwise van-der-Corput decay; independence after spectral rotation; arbitrary-joint rank-three coarea; a positive moment of a worst conditional projection-density cap; naive fiber-sup integration; a uniformly large single physical minor; or moment/support assumptions. All conditioning is on ORIGINAL coordinates, and all product-law information is retained before Fourier inversion.

## 2. Inputs from completed proofs

### 2.1 Regularized determinant / fractional ridge estimate

The completed regularized-determinant theorem at

`yspennstate/math-open-problems@a302aab3477c64757b511e80d3907f982e04873a`,
`proofnet24/QFORM-density/interactive/20260922T131746Z-regularized-determinant/REPORT.md`

states the following in the notation needed here. Let I,J be disjoint sets of ORIGINAL coordinates and, after conditioning all other original coordinates, write

`R(U,V)=F(U)+2 U^T B V+G(V)+c`,

where U=X_I and V=X_J remain independent product laws with coordinate density caps one; F and G may be arbitrary quadratic-affine functions. For `1<=q<2`, if the coordinate leverage of the projection onto `range(B)` on the I side obeys

`max_i (P_range(B))_ii <= q/2`,

then

`|phi_R(t)| <= det(I + beta_q t^2 BB^T)^(-1/(4q))`,

where

`beta_q = 2q/(pi^2 e^2)`.

The same statement can be used on the J side after transposing B.

### 2.2 Dependence-safe original-coordinate square smoothing

The completed account04/B18 theorem

`QFORM-DEPENDENT-SQUARE-SMOOTHING-v1`, source
`yspennstate/math-open-problems@441e5c1ae4b8aa71ba1bb68aa07d26d83afafcd3`

gives, at its kernel stage, the following dependence-safe implication. If a genuine original-coordinate completion has

`Q=R+a V_R^2`, `a!=0`,

with the theorem's cap-one conditional scalar variable, then

`p_Q(t) <= |a|^(-1/2) int_0^infinity p_R(t-sgn(a)u) u^(-1/2) du`.

For any probability density p_R with `||p_R||_3<=M`, splitting the integral and optimizing gives

`sup_t int_0^infinity p_R(t-u)u^(-1/2)du <= (2^(4/3)+1) M^(3/4)`.

This step requires no independence between R and the translated square variable.

## 3. New theorem: fractional-ridge L3 payment with arbitrary higher-rank tail

### Theorem 3.1 — `QFORM-FRACTIONAL-RIDGE-L3-OUTER-SQUARE-v1`

Under the setup of Section 2.1, assume for some

`1 <= q < 3/2`

that the physical range projection of B on at least one side has maximum coordinate leverage at most `q/2`. Assume also that

`s_2(B) >= sigma > 0`,

where `s_2` is the second singular value. Then R has an L3 density and

`||p_R||_3 <= (2pi)^(-2/3) [J_q/sigma]^(2/3)`,

where

`J_q = sqrt(pi)/sqrt(beta_q) * Gamma(3/(4q)-1/2)/Gamma(3/(4q))`,
`beta_q=2q/(pi^2 e^2)`.

If, in addition, the full form has the dependence-safe genuine original-coordinate square completion of Section 2.2, then

`boxed( ||p_Q||_infinity <= C(q) / sqrt(|a| sigma) )`,

with

`C(q) = (2^(4/3)+1)(2pi)^(-1/2)
        * [ sqrt(pi)/sqrt(beta_q)
            * Gamma(3/(4q)-1/2)/Gamma(3/(4q)) ]^(1/2).`

All extra cross singular directions, same-side quadratic terms, affine shifts and outside couplings are retained. In particular, this theorem does NOT require B to have rank two and does not perturbatively discard a small higher-rank tail.

### Proof

Since the regularized determinant is a product over singular values and every omitted factor is at most one,

`|phi_R(t)| <= (1+beta_q sigma^2 t^2)^(-2/(4q))`

because the first two singular values are at least sigma. Raising to the power 3/2 gives

`|phi_R(t)|^(3/2) <= (1+beta_q sigma^2 t^2)^(-3/(4q)).`

The exponent is greater than 1/2 exactly when `q<3/2`. Therefore

`int_R |phi_R(t)|^(3/2) dt
 <= [1/(sqrt(beta_q) sigma)]
    int_R (1+s^2)^(-3/(4q)) ds`

`= [sqrt(pi)/(sqrt(beta_q) sigma)]
   Gamma(3/(4q)-1/2)/Gamma(3/(4q))`

`= J_q/sigma.`

Inverse Hausdorff--Young in the same Fourier convention as the completed rank-two cross-bank theorem yields

`||p_R||_3 <= (2pi)^(-2/3) (J_q/sigma)^(2/3).`

Apply the dependence-safe square kernel and the optimized L3-to-Linfinity fractional integral inequality:

`||p_Q||_infinity
 <= (2^(4/3)+1)|a|^(-1/2)||p_R||_3^(3/4)`

`<= C(q)|a|^(-1/2) sigma^(-1/2).`

This proves the theorem. No pointwise one-dimensional oscillatory estimate is used. QED.

### Corollary 3.2 — the half-leverage constant

For `q=1`,

`beta_1 = 2/(pi^2 e^2) = 0.027424662172209262...`,
`J_1 = 31.666609946285952...`,

and

`||p_R||_3 <= 2.939551925866431 sigma^(-2/3)`.

Consequently

`boxed( ||p_Q||_infinity <= 7.901945565491720 / sqrt(|a| sigma). )`

Thus any physical cross block with `s_2(B)>=sigma` and one-sided range leverage at most 1/2 is paid even if it has arbitrarily many further singular directions.

## 4. Direct splice to the current B08 near-rank-two state

Account03/B08 r20, source

`yspennstate/math-open-problems@d5547a484fcc9b62341d80e9ba902cbe2e484284`,
`proofnet24/QFORM-density/fleet-2026-09-22/account03/B08/20260922T201956Z-account03-B08-qform-diffuse-r20/REPORT.md`,

proves in the surviving two-sided near-coloop branch that

`h_2 > gamma/sqrt(2)`

and that the cross block is within Hilbert--Schmidt distance `<0.010111 gamma` of its top-rank-two truncation. The small tail cannot be discarded by moments.

The new theorem pays a nontrivial portion of the strictly higher-rank branch WITHOUT discarding that tail. If either the left or right physical range projection of the actual full H has maximum diagonal at most 1/2, then set

`sigma=gamma/sqrt(2)`.

Corollary 3.2 gives

`||p_Q||_infinity
 < 7.901945565491720 * 2^(1/4) / sqrt(|a| gamma)`

`boxed( ||p_Q||_infinity < 9.397049888846953 / sqrt(|a| gamma). )`

This is a genuine arbitrary-higher-rank-tail closure in the diffuse-range subbranch. The remaining tail problem is therefore localized to the case where the physical range of H is itself heavy on BOTH sides.

## 5. Required designated-partner result actually applied

The current completed `account02/B08` result is

`QFORM-DOUBLE-INCIDENT-RANK2-GROUPED-L3-v1`, canonical source
`yspennstate/math-open-problems@c248abc9be918698c6d5a68108c615ba1c4790b3`,
`proofnet24/QFORM-density/fleet-2026-09-22/account02/B08/B08-20260922T204103Z-1dd824/REPORT.md`.

For an exact-rank-two physical cross block C and fixed physical row j / column r, it aggregates the complete incident determinant bank

`Delta_jr(C)=sum_(k!=j,s!=r) det C[{j,k},{r,s}]^2`

BEFORE reciprocal payment and proves

`||p_R||_3 <= 3^(2/3) 2^(1/3) Delta_jr(C)^(-1/6)`,

and after the dependence-safe square,

`||p_Q||_infinity
 <= (2^(4/3)+1)sqrt(3)2^(1/4)
    |a|^(-1/2) Delta_jr(C)^(-1/8).`

Apply this theorem to the exact-rank-two endpoint of account03/B08 r20. The factorized bank there satisfies

`Delta_jr(H) > (317037289472/519230401875) gamma^4`

`=0.610590767272375... gamma^4.`

Therefore, directly and without selecting a single minor,

`boxed( ||p_Q||_infinity
 < 7.711209966876888 / sqrt(|a| gamma). )`

This is the named partner result used in an actual target inequality during this run.

Combining Sections 4 and 5: in the r20 state, the exact-rank-two endpoint is paid by the partner theorem; every higher-rank endpoint whose full physical range is half-leverage-diffuse on either side is paid by Theorem 3.1. What remains is strictly higher rank with BOTH side range projections containing a coordinate leverage above 1/2, together with the global exhaustive reduction to this branch.

## 6. A source-valid falsifier: small operator-norm tails are NOT uniformly perturbative in characteristic functions

The r20 tail estimate `||H-H_2||_HS<0.010111 gamma` tempts one to replace H by H_2 and appeal to continuity. That is invalid under the owner hypotheses without additional product-preserving structure.

### Proposition 6.1 — `QFORM-SMALL-TAIL-CHAR-CONTINUITY-FALSE-v1`

There is no modulus `omega(epsilon)->0` such that, uniformly over all admissible cap-one product laws and all target-valid matrices A,A' with `||A-A'||_op<=epsilon`, one has

`|phi_A(1)-phi_A'(1)| <= omega(epsilon)`.

Indeed, fix epsilon>0 and define

`A_0 = diag(1,1,1,0,0)`,

`A_epsilon = A_0 + epsilon(e_4 e_5^T+e_5 e_4^T)`.

Both are target-valid: their spectra contain three eigenvalues equal to 1; `A_epsilon` has two additional eigenvalues `+epsilon,-epsilon`; and

`||A_epsilon-A_0||_op=epsilon`.

Fix a small delta>0. The phase-aligned set

`S_delta={x: dist(x^2,2pi Z)<=delta}`

has infinite Lebesgue measure: the components near `sqrt(2pi k)` have lengths comparable to `delta/sqrt(k)`, whose sum diverges. Choose a measurable finite union/subset `E_delta subset S_delta` of total length one and let X_1,X_2,X_3 be iid with density `1_E_delta`. Then

`g=E exp(i X_1^2)` satisfies `|g|>=Re g>=cos(delta)`.

Let X_4,X_5 be iid uniform on the length-one interval

`[M-1/2,M+1/2]`, `M=sqrt(pi/(2epsilon))`.

Writing X_4=M+u, X_5=M+v with `|u|,|v|<=1/2`,

`2epsilon X_4X_5 = pi + error`,

with

`|error| <= sqrt(2pi epsilon)+epsilon/2 =: eta_epsilon.`

Therefore for

`h=E exp(i 2epsilon X_4X_5)`

we have `|h+1|<=eta_epsilon`, hence `|h-1|>=2-eta_epsilon`. Under the SAME admissible product law,

`phi_A0(1)=g^3`,
`phi_Aepsilon(1)=g^3 h`,

so

`|phi_Aepsilon(1)-phi_A0(1)|
 >= (cos delta)^3 (2-eta_epsilon).`

Letting epsilon,delta tend to zero sends this lower bound to 2. For the concrete values

`epsilon=10^(-4)`, `delta=10^(-2)`,

it equals

`1.9745875019758325...`.

Thus a tiny Hilbert--Schmidt/operator-norm cross tail cannot be deleted by a law-uniform characteristic-function continuity estimate. This proposition does NOT refute QFORM; it only shows that the remaining near-rank-two stability step must exploit original-coordinate product geometry, grouped curvature, or ridge effective dimension rather than absolute phase perturbation.

## 7. Conditional end-to-end map after this run

A compact remaining route is now:

1. Use the fleet's existing structural reductions to reach a scalar-pivot / physical-cross-block state.
2. If the cross block has a useful ridge-diffuse physical range, apply the regularized determinant mechanism; Theorem 3.1 now pays the important rank-two-exponent `L3 + square` regime with arbitrary extra singular directions.
3. If the cross block is exact rank two, apply the account02/B08 grouped incident-bank theorem before any reciprocal minor selection.
4. The still-unpaid local state is therefore a genuinely higher-rank cross block whose physical range is heavy on both sides, especially the near-bicoloop state identified by account03/B08 r20. Proposition 6.1 rules out simply deleting its tiny spectral tail.
5. The next required implication is `QFORM-DOUBLE-HEAVY-RANGE-TAIL-PAYMENT-v1`: use the two heavy physical range coordinates together with the nonzero higher-rank tail to force either a dependence-safe grouped determinant payment, a second-curvature hybrid estimate, or an already-paid physical pair/ridge branch, with a universal constant and no moment assumptions.

That implication, plus the global exhaustive reduction into the paid branches, remains necessary for the full theorem.

## 8. Status

- New positive theorem: **PROVED supporting theorem**, source-dependent on the completed regularized-determinant and dependence-safe square results.
- Designated account02/B08 theorem: **consumed and applied to an exact inequality**.
- Small-tail characteristic-continuity mechanism: **REFUTED by an exact target-valid product-law construction**.
- New positive branch conclusion: **essential boundedness**; continuity is **not claimed** from the L3-plus-square route.
- Full quadratic-form bounded-density conjecture: **OPEN / NOT PROVED / NOT DISPROVED**.
