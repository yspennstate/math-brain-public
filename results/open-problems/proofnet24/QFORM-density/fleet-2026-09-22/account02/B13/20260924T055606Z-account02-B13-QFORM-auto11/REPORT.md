SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B13, 2026-09-24T05:56:06Z.
attacking: partner r44's near-rank-one exact-rank-two survivor; force a second literal physical square and spend both squares in the rank-two Fresnel integral, then isolate the genuinely rough remainder that still cannot be deleted.

# account02/B13 — two-square Strichartz bootstrap and the rho^(-7/3) second carrier mode

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260924T055606Z-account02-B13-QFORM-auto11`  
Role: extremal product laws / complementary constructions and source-valid counterexamples  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Status: **NEW SUPPORTING THEOREM AND STRICTLY SHARPER NEAR-RANK-ONE OBSTRUCTION / FULL QFORM OPEN / GLOBAL CONTINUITY OPEN**.

No moment, compact-support, log-concavity, connected-support, diagonal-basis, post-rotation-independence, bounded-diameter, fixed-fragment-count, attained-bathtub-optimizer, or coefficient-small random-error deletion is used.

## 1. Fresh source state and first unpaid implication

Fresh brain control was resolved at `math-research-brain@ffaa62dd3b3d172fcc95d5c2d8bdbcf8d4817837` and refreshed again before this report. OWNER CONTROL remains revision `2026-09-22.15`, QFORM-only, with no stop for account02/B13. The full target remains OPEN.

The latest completed compatible designated-partner result at the refresh is account03/B13 r44:

`math-open-problems@57ccfc48fbd392d6b1948c288308c9e3db05e69b`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B13/20260924T053240Z-account03-B13-qform-r44/REPORT.md`.

Its completed theorem `QFORM-R2-ONE-PHYSICAL-SQUARE-STRICHARTZ-v1` says that in

`A=D+U Lambda U^T`, `U^T U=I_2`, `max_i ||u_i||^2<=1/3`,

if `Lambda` is invertible and one original physical diagonal coefficient obeys `|d_k|>=1`, then for arbitrary cap-one product laws and arbitrary deterministic affine terms

`||p_Q||_infty <= C_sq (1+|det Lambda|^(-6/13))`                  (1.1)

for a universal finite `C_sq`. It also imports the completed account04/B13 sparsification

`d_(5) <= C_D rho^(-1)`,   `C_D=2 sqrt(30 pi)=19.416259125557...`. (1.2)

The first unpaid implication after the new work below is

`QFORM-RANK1-2BIGDIAG-DIAGTAIL-SUPERSMALL-MODE-RECEIVER-v1`:
retain, in original product coordinates, a dominant rank-one carrier, two physical diagonal coefficients of size at least `3/4`, the distributed diagonal tail `||D_tail||_op=O(rho^-1)`, and the second carrier mode `O(rho^-7/3)`. A proof must keep the last two terms in the actual phase; otherwise produce a genuine bounded-finite-union product-indicator counterexample in this exact normal form.

## 2. First bootstrap: r44 already forces det Lambda = O(rho^(-13/6))

Let `rho=P(Q in J)/|J|`. From (1.1), if `rho>2 C_sq`,

`rho <= C_sq(1+|det Lambda|^(-6/13))`

implies

`boxed: |det Lambda| <= (2 C_sq/rho)^(13/6).`                    (2.1)

This is a strict self-improvement over the previous `O(rho^-2)` determinant obstruction.

Write the eigenvalues of the symmetric `2 x 2` matrix `Lambda` as `lambda_1,lambda_2`, ordered by

`|lambda_1|>=|lambda_2|`.

There is also a universal lower bound on the dominant mode in every sufficiently high-ratio survivor. Let `S` be the four largest diagonal coordinates from (1.2). If `|lambda_1|<1/8` and `rho>=8 C_D`, then

`||A-D_S||_op <= |lambda_1|+C_D/rho <1/4`.

Since `s_3(A)>=1`, Weyl gives `s_3(D_S)>3/4`. Hence three physical coordinates `T subset S` satisfy `|d_i|>3/4`. On that same physical triple,

`sigma_min(A[T,T]) >= 3/4-||(U Lambda U^T)[T,T]||_op >5/8`.       (2.2)

Now apply the completed physical-three-coordinate theorem from the owner-pinned `COUNTEREXAMPLE_SEARCH.md`: a physical `3 x 3` block with minimum absolute eigenvalue at least `c` gives density at most `6 sqrt(pi)/c`. Equation (2.2) therefore gives

`||p_Q||_infty <= 48 sqrt(pi)/5 =17.0155569686...`.               (2.3)

Thus an unbounded-ratio sequence necessarily has `|lambda_1|>=1/8`; combining with (2.1),

`|lambda_2| <= 8 (2 C_sq)^(13/6) rho^(-13/6)`.                   (2.4)

This is an equation-level use of a completed theorem from the required pinned source, not a numerical heuristic.

## 3. A second physical square is forced

Once (2.4) is below `1/4`, remove only the second carrier eigenmode and put

`A_0=D+lambda_1 v v^T`,

where `v` is a physical unit vector. Then

`s_3(A_0)>=s_3(A)-|lambda_2| >=3/4`.                              (3.1)

A rank-one perturbation changes singular-value index by at most one, so

`s_3(D+lambda_1 v v^T) <= s_2(D)`.                               (3.2)

Consequently

`boxed: s_2(D)>=3/4.`                                             (3.3)

Since `D` is diagonal, (3.3) means that there are two distinct original physical coordinates `k,l` with

`boxed: |d_k|>=3/4,   |d_l|>=3/4.`                               (3.4)

If `lambda_2=0` exactly, the same argument starts directly from `A=A_0`, and in fact gives `s_2(D)>=1`; thus (3.4) also covers the exact-rank-one endpoint.

The important point is that no support information is used: the second square is forced by spectral rank-one interlacing in coefficient space.

## 4. New analytic theorem: two physical squares improve the determinant exponent to 3/7

### Theorem 4.1 — `QFORM-R2-TWO-PHYSICAL-SQUARES-STRICHARTZ-v1`

Assume

`A=D+U Lambda U^T`, `U^T U=I_2`, `max_i ||u_i||^2<=1/3`,          (4.1)

`Lambda` is invertible, and two distinct original coordinates `k,l` obey

`|d_k|,|d_l|>=3/4`.                                               (4.2)

Then for every independent cap-one product law and every deterministic affine term,

`boxed: ||p_Q||_infty <= C_2 (1+|det Lambda|^(-3/7))`             (4.3)

for one universal finite constant `C_2`. The density is bounded and continuous.

### Proof

Use the same notation and the same two completed analytic lemmas as partner r44. Put

`c_i=||u_i||^2`,

and for fixed Fourier time `t`,

`G_i(t,s)=int f_i(x) exp(i t(d_i x^2+b_i x)) exp(i s x) dx`.       (4.4)

Rank-two Fresnel linearisation gives

`|phi_Q(t)| <= (4 pi |t|)^(-1) |det Lambda|^(-1/2) J(t)`,         (4.5)

with

`J(t)=int_{R^2} prod_i |G_i(t,<u_i,xi>)| dxi`.                    (4.6)

For every row with `c_i>0`, write `u_i=sqrt(c_i) uhat_i`. The geometric Brascamp--Lieb identity

`sum_i c_i uhat_i uhat_i^T=I_2`

applied exactly as in r44 gives, after spending the completed high-power Hausdorff--Young budget on every nonspecial row,

`J(t) <= K_BL F_k(t) F_l(t)`                                     (4.7)

when `c_k,c_l>0`, where

`F_j(t)=||G_j(t,.)||_{L_s^(1/c_j)}`                              (4.8)

and `K_BL` is universal. The factors `c_j^(-c_j/2)` are uniformly bounded on `0<c_j<=1/3`; all nonspecial scale factors cancel against their `L^(1/c_i)` budgets exactly as in the one-square proof.

The partner's one-dimensional parabola mixed-norm lemma gives

`||F_j||_{L_t^(r_j)} <= S_* |d_j|^(-1/r_j)`,

`1/r_j=(1-2c_j)/4`, hence `4<=r_j<=12`.                           (4.9)

Put

`theta=1/r_k+1/r_l=(1-c_k-c_l)/2`.                               (4.10)

Because each `c_j<=1/3`,

`theta>=1/6`.                                                     (4.11)

Let `p` satisfy `1/p+theta=1`. Holder in `t`, (4.5), (4.7), and (4.9) imply, for `T>=1`,

`int_{|t|>T} |phi_Q(t)| dt
 <= K |det Lambda|^(-1/2) T^(-theta)
 <= K |det Lambda|^(-1/2) T^(-1/6)`.                             (4.12)

Here (4.2) absorbs the square coefficients into the universal constant, and `theta>=1/6` keeps the `L^p` norm of `|t|^-1` uniformly away from its logarithmic endpoint.

If one special row has zero leverage, its factor is independent of the Fresnel variable. The r44 square estimate gives its scalar characteristic function an `L_t^3` norm bounded universally under (4.2). The other special factor has exponent `r<=12`, so the available reciprocal time integrability is at least `1/3+1/12=5/12`, stronger than (4.11). If both special leverages vanish, it is `2/3`, stronger again. Thus (4.12) holds uniformly in every zero-leverage endpoint.

On `|t|<=T`, use only `|phi_Q(t)|<=1`. Therefore

`||phi_Q||_1 <= 2T + K |det Lambda|^(-1/2) T^(-1/6)`.             (4.13)

Choose

`T=max{1,(K |det Lambda|^(-1/2))^(6/7)}`.                         (4.14)

Then

`||phi_Q||_1 <= C (1+|det Lambda|^(-3/7))`.                       (4.15)

Fourier inversion proves (4.3) and continuity. QED.

The exponent `3/7` is the worst diffuse-leverage case `c_k=c_l=1/3`; smaller total leverage gives a better exponent.

## 5. Main bootstrap: the second carrier is actually O(rho^(-7/3))

Return to a sufficiently high-ratio diffuse exact-rank-two survivor. Sections 2-3 give the two physical squares (3.4). Apply Theorem 4.1 to the **original full rank-two carrier**, not to a rotated random vector. If `rho>2C_2`, then

`rho <= C_2(1+|det Lambda|^(-3/7))`

forces

`boxed: |det Lambda| <= (2C_2/rho)^(7/3).`                        (5.1)

Together with `|lambda_1|>=1/8`,

`boxed: |lambda_2| <= 8(2C_2)^(7/3) rho^(-7/3).`                  (5.2)

This strictly sharpens both the partner's initial `O(rho^-1)` near-rank-one approximation and the first bootstrap `O(rho^-13/6)`.

Hence every unbounded-ratio sequence in the diffuse exact-rank-two chamber has the exact coefficient normal form

`A = D + lambda_1 v v^T + lambda_2 w w^T`,                        (5.3)

with

- `v,w` physical orthonormal vectors;
- `|lambda_1|>=1/8`;
- two physical diagonal entries `|d_k|,|d_l|>=3/4`;
- after retaining the four largest diagonal entries, `||D_tail||_op<=19.416260 rho^-1`;
- `|lambda_2|=O(rho^-7/3)`.

The first unpaid receiver in Section 1 is therefore materially narrower than the r44 debt.

## 6. Why even rho^(-7/3) cannot be deleted for rough product laws

### Proposition 6.1 — `QFORM-ARBITRARILY-SMALL-RANK1-ROUGH-NONPERTURBATION-v1`

No coefficient rate by itself, even much faster than `rho^-7/3`, makes a rank-one quadratic term a law-uniform small random perturbation on the allowed product class.

Fix `epsilon>0`, let

`w=(e_5+e_6)/sqrt(2)`,   `E=epsilon w w^T`,                       (6.1)

so `||E||_op=epsilon`. Put `R=epsilon^(-1/2)`, and let `X_5,X_6` independently have density one on

`[R-1/4,R+1/4] union [-R-1/4,-R+1/4]`.                            (6.2)

These are bounded two-fragment unit-measure indicator laws. Write

`X_i=S_i R+U_i`,

with independent fair `S_i in {+1,-1}` and `|U_i|<=1/4`. Then

`X^T E X = epsilon/2 (R(S_5+S_6)+U_5+U_6)^2`,                    (6.3)

and, deterministically,

`boxed:
 |X^T E X - (S_5+S_6)^2/2| <= sqrt(epsilon)+epsilon/8.`           (6.4)

Thus as `epsilon->0`, the allegedly negligible quadratic term converges uniformly under this coupling to a nontrivial two-point random shift: `0` when the signs disagree and `2` when they agree. Taking `epsilon` equal to a constant times `rho^-7/3` merely moves the fragment centres out to order `rho^(7/6)`.

This is not a counterexample to QFORM. It is a source-valid obstruction to every proof step of the form “the coefficient tail is `o(1)`, therefore its random quadratic contribution is `o(1)`.” It also explains why bounded-diameter localization would be an illicit shortcut.

## 7. Required pinned Fourier obstruction

The required source

`math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

was reread at `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`. Besides the physical-triple Theorem A used in (2.3), its completed unconditional `D_5` theorem gives, for every disjoint physical cross block `M=A[I,J]`,

`||p_Q||_infty <= 5 sqrt(2e) e_5(M^T M)^(-1/10)`.                (7.1)

Therefore every slab witness obeys the real obstruction

`boxed:
 e_5(M^T M) <= (5 sqrt(2e)/rho)^10,`                              (7.2)

and hence

`boxed:
 s_5(M) <= 5 sqrt(2e)/rho =11.6582199079.../rho.`                 (7.3)

In the exact diagonal-plus-rank-two chamber of Sections 2-5 every off-diagonal physical cross block has rank at most two, so `e_5=0`: `D_5` is structurally blind exactly at this endpoint. The new two-square argument therefore supplies information in a chamber not payable by the fifth-volume theorem, while (7.2) remains the mandatory obstruction on every general pre-reduction survivor.

The pinned numerical counterexample search still reports no valid counterexample; none of its numerical evidence is used as proof.

## 8. Extremal-product scope

The optimizer-free extremal reduction remains the only admissible transfer. Strict cap-one slab violations can be approximated, with arbitrarily small ratio loss, by finite convex mixtures of products of indicators of bounded finite unions of total measure one. No conclusion is drawn that a maximizing law is a single interval, centered, bounded in a uniform diameter, or has uniformly bounded fragment count.

Proposition 6.1 deliberately uses only two-fragment unit-measure indicators, so the rough nonperturbation survives even inside this purified finite-union class.

## 9. Status and next implication

The full arbitrary-density three-large-eigenvalue conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**. Global continuity remains separate.

New results in this run:

1. `QFORM-R2-TWO-PHYSICAL-SQUARES-STRICHARTZ-v1` — two literal physical squares improve the diffuse rank-two determinant exponent from `6/13` to `3/7`.
2. `QFORM-R2-SECOND-MODE-SEVENTHIRDS-v1` — every sufficiently high-ratio diffuse exact-rank-two survivor has `|lambda_2|=O(rho^-7/3)` and two physical diagonal coefficients at least `3/4`.
3. `QFORM-ARBITRARILY-SMALL-RANK1-ROUGH-NONPERTURBATION-v1` — no coefficient decay rate alone permits deletion of the second rank-one mode on fragmented rough inputs.

First unpaid implication:

`QFORM-RANK1-2BIGDIAG-DIAGTAIL-SUPERSMALL-MODE-RECEIVER-v1`.

A valid next proof must use the two large physical squares plus the dominant rank-one carrier to absorb the distributed `O(rho^-1)` diagonal phase and the `O(rho^-7/3)` second carrier **inside** the product-preserving estimate. A valid negative result must be an actual bounded-finite-union product-indicator counterexample in that normal form, not merely another perturbative obstruction.
