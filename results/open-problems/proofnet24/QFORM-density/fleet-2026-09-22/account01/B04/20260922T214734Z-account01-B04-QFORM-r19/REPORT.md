SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B04, 2026-09-22T21:47:34Z.
attacking: integrated product-Fourier smoothing for nonzero-diagonal indefinite physical pairs, followed by a contamination-safe four-coordinate Schur splice.

# account01/B04 r19 — integrated Fourier L2 for an indefinite pair and a four-coordinate contamination splice

Status: `ESSENTIAL_STEP_APPLIED / SUPPORTING_THEOREMS_PROVED / FULL_TARGET_OPEN`.
Execution: `WITHOUT_VERIFIED_BRAIN`.

The full target remains open. All random coordinates below are original independent coordinates with probability densities bounded by one. No moment, support, log-concavity, Gaussian, post-rotation independence, or pointwise quadratic-phase decay hypothesis is used. The arbitrary-joint coarea and positive conditional-projection-moment shortcuts are not used.

## 1. Conditional end-to-end route and the first missing interface

A complete proof would follow if the bare spectral hypothesis `s_3(A)>=1` could be routed, with universal currency and without selecting a vanishing local minor, into one of the already-paid square/ridge/diffuse/pair branches. The current B04 obstruction is that the physically useful packets can carry nonzero self-quadratic curvature and cross-contamination. This run pays two analytic interfaces:

1. an **integrated Fourier L2 estimate for every invertible indefinite physical pair**, allowing arbitrary affine translation and nonzero diagonal entries; and
2. a **four-coordinate Schur splice** that tolerates an arbitrary cross block between two physical coordinate pairs, provided the first pair is indefinite/invertible and the two-dimensional Schur remainder is nonzero.

Neither statement asserts that a universally conditioned packet is forced by `s_3(A)>=1`.

## 2. Source-pinned pair envelope

The complete source used here is the interactive pair-log theorem

`yspennstate/math-open-problems@f7f0fedb2d93b46824f96cac1164af6f8a55626f`
`proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/PAIR_LOG_THEOREM.md`.

Its Section 3 proves the following for independent cap-one `U,V`. If

`F=(U,V) B (U,V)^T+2 ell.(U,V)+c`,

where `B` is invertible and indefinite, write

`Delta=|det B|`, `kappa=sigma_min(B)>0`,

and let `t0` be the completed-square critical value. For every cutoff `r>0`, a density version satisfies a.e.

`p_F(t) <= A + G(t)`,

`A=2sqrt(2)/r`,

`G(t)=Delta^(-1/2) log_+( 2r^2/(kappa |t-t0|) )`.        (2.1)

This is a logarithmic envelope, not a pointwise power-decay statement.

## 3. New theorem: integrated Fourier L2 for one indefinite physical pair

### Theorem 3.1 — `QFORM-INDEFINITE-PAIR-FOURIER-L2-v1`

Under the hypotheses of Section 2, put

`K0 = 113sqrt(2)/7 + 49/32 = 24.360697506879966... .`

Then

`||p_F||_2 <= sqrt(K0) Delta^(-1/8) kappa^(-1/4)`,          (3.1)

and therefore, with the Fourier convention `phi_F(t)=E exp(itF)`,

`||phi_F||_2 <= sqrt(2pi K0) Delta^(-1/8) kappa^(-1/4)`,    (3.2)

where `sqrt(2pi K0)=12.371854212197725...`.

The estimate is uniform over all affine coefficients `ell,c`.

#### Proof

For `lambda>A`, (2.1) implies

`{p_F>lambda} subset {G>lambda-A}`.

Writing `b=Delta^(-1/2)` and `C=2r^2/kappa`,

`|{G>x}| <= 2C exp(-x/b)`, `x>0`.                           (3.3)

For every `lambda>0`, probability normalization also gives

`|{p_F>lambda}| <= 1/lambda`.                                (3.4)

Using layer cake,

`||p_F||_2^2 = 2 int_0^infinity lambda |{p_F>lambda}| dlambda`.

Use (3.4) on `[0,A]` and (3.3) on `(A,infinity)`:

`||p_F||_2^2`
` <= 2A + 4C int_A^infinity lambda exp(-(lambda-A)/b) dlambda`
` = 2A + 4C(Ab+b^2)`
` = 4sqrt(2)/r + 16sqrt(2) r/(kappa sqrt(Delta)) + 8r^2/(kappa Delta).`  (3.5)

Set

`delta=kappa/sqrt(Delta)`.

Because the singular values of `B` are `s_max>=kappa` and `Delta=s_max*kappa`, one has `0<delta<=1`. Write `r=sqrt(Delta) x` and then `x=y sqrt(delta)`. Equation (3.5) becomes

`||p_F||_2^2`
` <= Delta^(-1/2) [ delta^(-1/2)(4sqrt(2)/y+16sqrt(2)y)+8y^2 ]`
` <= Delta^(-1/2) delta^(-1/2) [4sqrt(2)/y+16sqrt(2)y+8y^2].`  (3.6)

Choose the explicit rational `y=7/16`. The bracket is exactly

`113sqrt(2)/7 + 49/32 = K0`.

Since `Delta^(-1/2) delta^(-1/2)=Delta^(-1/4)kappa^(-1/2)`, (3.1) follows. Plancherel gives (3.2). QED.

This is an **integrated** Fourier estimate. It does not imply, and the proof never uses, a law-uniform pointwise decay estimate.

## 4. Product Fourier corollary: two arbitrary indefinite pair blocks

### Corollary 4.1 — `QFORM-TWO-INDEFINITE-PAIR-FOURIER-CONVOLUTION-v1`

Let four selected original coordinates form two disjoint pairs. Conditional on all outside coordinates `W`, suppose the selected quadratic block is block diagonal with invertible indefinite `2x2` blocks `B_1,B_2`; arbitrary linear terms depending on `W` are allowed, and `W` may carry arbitrary quadratic curvature. Put

`Delta_j=|det B_j|`, `kappa_j=sigma_min(B_j)`.

Then the full quadratic form has a continuous density and

`||p_Q||_infinity`
` <= K0 (Delta_1 Delta_2)^(-1/8)(kappa_1 kappa_2)^(-1/4).`   (4.1)

#### Proof

Fix `W=w`. The two pair outputs are independent because they use disjoint original-coordinate inputs. Theorem 3.1 gives the uniform conditional Fourier bounds

`||phi_j||_2 <= sqrt(2pi K0) Delta_j^(-1/8)kappa_j^(-1/4)`.

Hence Cauchy-Schwarz yields

`int_R |phi_1(t)phi_2(t)| dt`
` <= 2pi K0 (Delta_1Delta_2)^(-1/8)(kappa_1kappa_2)^(-1/4).`

Fourier inversion gives (4.1). The conditional density is the convolution of two L2 densities, hence is bounded and continuous. The bound is uniform in `w`; after adding the outside scalar shift and averaging in `W`, dominated convergence gives a continuous density for the full form. QED.

For pure-cross pairs `B_j=[[0,c_j],[c_j,0]]`, (4.1) scales correctly as `(|c_1c_2|)^(-1/2)`. Its constant is not intended to beat the earlier exact-zero-diagonal matching theorem; its gain is robustness to arbitrary nonzero pair diagonals.

## 5. New two-dimensional square-root small-ball lemma

### Lemma 5.1 — `QFORM-2D-QUADRATIC-SQRT-SMALLBALL-v1`

Let `Y,Z` be independent cap-one random variables, let `S` be a nonzero symmetric `2x2` matrix, and put `s=||S||_op`. For arbitrary affine terms and every `rho>0`,

`sup_t P( (Y,Z)S(Y,Z)^T + affine in [t-rho,t+rho] )`
` <= min(1, 13 sqrt(rho/s)).`                                 (5.1)

#### Proof

Write `S=[[a,c],[c,b]]`.

If `max(|a|,|b|)>=s/4`, condition on the other original coordinate. Completing the resulting scalar quadratic and using

`|{x: |x^2-u|<delta}| <= 2sqrt(2delta)`

gives a bound at most `4sqrt(2) sqrt(rho/s)`, which is below (5.1).

Assume now `|a|,|b|<s/4`. Since

`s <= max(|a|+|c|,|b|+|c|)`,

one has `|c|>3s/4`. Therefore `S` is indefinite and

`Delta_S=|det S|=c^2-ab > s^2/2`,

`kappa_S=Delta_S/s > s/2`.                                    (5.2)

Apply the source-pinned pair envelope (2.1) with cutoff

`r=sqrt(kappa_S rho)`.

The constant part contributes at most

`2rho * 2sqrt(2)/r <= 8 sqrt(rho/s)`.                         (5.3)

For the logarithmic part, the radially decreasing kernel is maximized on an interval of length `2rho` centered at its singularity, and

`int_{-rho}^{rho} log(2rho/|u|) du = 2rho(1+log 2).`

Together with `Delta_S^(-1/2)<=sqrt(2)/s`, this is at most

`2sqrt(2)(1+log2) (rho/s).`                                    (5.4)

If `rho<=s`, (5.4) is at most `2sqrt(2)(1+log2)sqrt(rho/s)`. Adding (5.3) gives a coefficient below `12.79<13`. If `rho>s`, the trivial probability bound one is stronger than (5.1). QED.

## 6. Main contamination-safe four-coordinate splice

### Theorem 6.1 — `QFORM-4D-INDEFINITE-PAIR-SCHUR-SPLICE-v1`

Choose four original coordinates and partition their physical `4x4` principal block as

`M=[[B,C],[C^T,D]]`,

where `B` is an invertible indefinite `2x2` matrix. Put

`Delta=|det B|`, `kappa=sigma_min(B)`,

`S=D-C^T B^(-1) C`, `s=||S||_op`.

Assume only `S!=0`. All coordinates outside these four may have arbitrary quadratic coefficients and arbitrary couplings to the four selected coordinates. Then the full quadratic form has an essentially bounded density and

`||p_Q||_infinity <= 4sqrt(26) (Delta kappa s)^(-1/4).`      (6.1)

No claim of continuity is made for this general contaminated branch.

#### Proof

Condition on all outside original coordinates. They contribute deterministic affine coefficients to the selected four-variable polynomial. Write the first pair as `u`, the second pair as `v`. Completing the first pair gives exactly

`u^TBu+2u^TCv+linear_u + v^TDv+linear_v+const`
` = (u+B^(-1)(Cv+linear_u/2))^T B (u+B^(-1)(Cv+linear_u/2))`
`   + v^T S v + affine_v + const'.`                           (6.2)

The first pair remains independent of the second pair and its shift in (6.2) may depend arbitrarily on `v`. Lemma 5.1 says the remainder in `v` obeys

`sup_t P(|R-t|<rho) <= (13/sqrt(s)) sqrt(rho).`               (6.3)

Now use Section 4 of the source-pinned pair-log theorem: an indefinite pair with parameters `(Delta,kappa)` whose completed remainder has `H sqrt(rho)` small-ball bound has density cap

`4sqrt(2H)(Delta kappa)^(-1/4)`.

Substituting `H=13/sqrt(s)` gives exactly (6.1). The estimate is uniform in every outside conditioning value, so mixing proves the full ambient assertion. QED.

If the whole physical `4x4` block is invertible, `det M=det B det S` and `s>=sqrt(|det S|)`, hence the weaker determinant-only corollary

`||p_Q||_infinity <=4sqrt(26) Delta^(-1/8)kappa^(-1/4)|det M|^(-1/8)`  (6.4)

is automatic.

The point of (6.1) is that **arbitrary pair-to-pair quadratic contamination `C` is retained**; it is absorbed before any reciprocal local coefficient is paid.

## 7. Designated account02/B04 result applied to an actual inequality

I consumed the latest completed partner report

`yspennstate/math-open-problems@7fd3ff5ed6af96a18f1d9a6c2c71f7ac5143eee1`
`proofnet24/QFORM-density/fleet-2026-09-22/account02/B04/B04-20260922T212021Z/REPORT.md`.

Its theorem `QFORM-ORTHOGONAL-LEAKAGE-SEPARATION-v1` proves that an orthogonal scalar leakage `eta` over a transverse two-frame `v_i` admits a disjoint original-coordinate partition `L,T` with

`(sum_{i in L} eta_i^2) det(sum_{j in T}v_jv_j^T) >= ||eta||^2 det(S_v)/24`.  (7.1)

Thus the current heavy-null bank obstruction is not lack of disjoint independent packets; it is quadratic contamination between those packets. Theorem 6.1 pays that contamination whenever the resulting four-coordinate packet contains an invertible indefinite first pair and a nonzero two-dimensional Schur remainder. This does not yet convert the aggregate currencies in (7.1) into one uniformly conditioned physical four-coordinate packet, so no full routing claim is made.

For the required equation-level partner application, I also use account02/B04's completed `QFORM-HYPERBOLIC-PAIR-DENSITY-TRANSFER-v1`, canonical source

`yspennstate/math-open-problems@f446c546c01b66f22c30828b845b1651d7a8a082`
`proofnet24/QFORM-density/fleet-2026-09-22/account02/B04/B04-20260922T174702Z-r15/REPORT.md`.

That theorem states that an outer original-coordinate hyperbolic pair of coefficient `c0!=0` over an **effective completed residual** `H` of density cap `B` gives

`||p_Q||_infinity <= |c0|^(-1)+4B.`                         (7.2)

If `H` has the two-indefinite-pair block structure of Corollary 4.1, substituting (4.1) into (7.2) gives the explicit new inequality

`||p_Q||_infinity`
` <= |c0|^(-1) + 4K0 (Delta_1Delta_2)^(-1/8)(kappa_1kappa_2)^(-1/4),`  (7.3)

with `4K0=97.44279002751986...`. The hypothesis is on the partner theorem's completed residual `H`; no claim is made that the raw residual automatically preserves block diagonality after the outer completion.

## 8. Genuinely rotated indefinite target example

Let

`B=[[1,2],[2,-1]]`, `C=(1/2)I_2`,

and use the selected four-coordinate block

`M=[[B,C],[C,B]]`.

Add a fifth original coordinate with diagonal coefficient `2` and physical couplings `0.05` to each of the four selected coordinates. This gives

`A =`
`[[1,2,1/2,0,1/20],`
` [2,-1,0,1/2,1/20],`
` [1/2,0,1,2,1/20],`
` [0,1/2,2,-1,1/20],`
` [1/20,1/20,1/20,1/20,2]].`

The unperturbed `M direct_sum [2]` has eigenvalues

`-sqrt(5)-1/2, -sqrt(5)+1/2, 2, sqrt(5)-1/2, sqrt(5)+1/2`,

so every eigenvalue has modulus at least `sqrt(5)-1/2>1.73`. The fifth-coordinate coupling perturbation has operator norm exactly `0.1`; Weyl therefore gives every eigenvalue of `A` modulus greater than `sqrt(5)-0.6>1.63`. In particular the target hypothesis is satisfied, and the form is non-diagonal and indefinite.

Here

`Delta=5`, `kappa=sqrt(5)`,

`B^(-1)=B/5`, and

`S=B-(1/4)B^(-1)=(19/20)B`,

so `s=(19/20)sqrt(5)` and

`Delta*kappa*s=95/4`.

Theorem 6.1 therefore gives for **every** admissible product input law

`||p_(X^TAX)||_infinity`
` <=4sqrt(26)(95/4)^(-1/4)`
` =9.239123275153592... .`                                      (8.1)

Only essential boundedness is asserted by this general contaminated-branch proof.

For comparison, if the cross-contamination `C` is set to zero while keeping the arbitrary fifth-coordinate affine coupling, Corollary 4.1 gives the continuous-density bound

`||p_Q||_infinity <= K0/sqrt(5)=10.89443512093865... .`       (8.2)

## 9. Honest remaining implication

The full conjecture is not proved. The new first unpaid implication is

`QFORM-AGGREGATE-TO-4D-SCHUR-CURRENCY-v1`:

> Starting only from `s_3(A)>=1`, convert the aggregate original-coordinate currencies now available (ridge determinant, two-bank transverse determinant, orthogonal leakage separation, weighted matching) into either a physical four-coordinate packet with `Delta*kappa*s` bounded below universally, or route its quantitative failure into an already completed diffuse/ridge/square/hyperbolic branch.

The latest account02/B04 counterexample shows that merely having nonzero leakage in two well-conditioned banks does not force a uniform rank-three cross singular value; that shortcut remains invalid. Theorem 6.1 removes **analytic contamination** once a quantitative four-coordinate Schur packet is present, but the global aggregate-to-packet extraction remains structural debt.

Full-target essential boundedness: **OPEN**. Full-target continuity: **OPEN**. New block-diagonal two-pair branch continuity: **PROVED**. New general four-coordinate contaminated branch continuity: **NOT CLAIMED**.
