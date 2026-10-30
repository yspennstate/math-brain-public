SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B05, 2026-09-22T22:52:32Z.
attacking: reverse the coarea conditioning order so arbitrary quadratic leakage on two diffuse banks is frozen before the reciprocal Jacobian is paid, and isolate the genuinely remaining third-curvature location problem.

# fleet02/B05 — reverse-conditioned bank leakage and random-slope square smoothing

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Quadratic coarea bound / complementary constructions and source-valid counterexamples  
**Run:** `20260922T225232Z-fleet02-B05-QFORM-37473ccc`  
**Status:** `ESSENTIAL_STEP_APPLIED`; one stronger intermediate statement is `CANDIDATE_REFUTED`; the full QFORM conjecture remains **OPEN**.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact target and binding sources

The target is the full arbitrary-product-law statement: for independent real original-coordinate inputs with probability densities bounded by one, and any real symmetric matrix having at least three eigenvalues of absolute value at least one, prove a dimension-free essential density bound for `X^T A X`, or give a genuine counterexample. No moments, support assumptions, diagonal-basis independence, post-rotation independence, Gaussianity, or log-concavity are used below.

Fresh owner control remained revision `2026-09-22.15`, QFORM-only. Binding corrections retained include failure of law-uniform pointwise quadratic-phase decay, dimension loss from unrestricted fiber suprema, failure of arbitrary-joint rank-three coarea, and failure of positive conditional projection-density moments. The argument below conditions only on disjoint **original-coordinate product banks** and never replaces them by an arbitrary joint density.

The named partner result actually used is fleet03/B05 run `20260922T214348Z-fleet03-B05-QFORM-r18`, canonical mathematics

`yspennstate/math-open-problems@1b86f205262fdfdba6fd1f1166fcc9f7ea75828c:proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B05/20260922T214348Z-fleet03-B05-QFORM-r18/REPORT.md`.

Its two-arm theorem proves a density cap `2/sqrt(|beta gamma|)` for two independent physical pivots driving two independent arm variables, and its bank corollary uses the product-marginal estimate

`||p_(b dot V)||_infinity <= sqrt(2)/||b||_2`.                         (1.1)

Its first unpaid factor was arbitrary quadratic leakage on the **same two arm banks**: terms such as `U^T D V` or within-bank quadratic phases invalidate the partner's forward conditioning because, after conditioning the pivots, they are not mere translations of the arm aggregates. The partner also supplied the incident-minor tube dichotomy: in its small-central-entry branch `||b||_2 ||c||_2 > c0`, where

`c0 = sqrt(9092287/17072000)-1/4 = 0.479784049338683...`.               (1.2)

The present run attacks exactly that unpaid factor by reversing which variables are conditioned first.

## 2. Reverse-conditioned two-bank coarea

### Theorem 2.1 — `QFORM-REVERSE-CONDITIONED-BANK-LEAKAGE-v1`

Let `X,Y` be independent real random variables with densities bounded by one. Let `U,V` be two disjoint original-coordinate product banks, mutually independent and independent of `X,Y`. Let `L=L(U)` and `M=M(V)` be scalar random variables having densities bounded by `L0,M0`, respectively. Let `H(U,V)` be an arbitrary measurable real function. Define

`R = H(U,V) + 2 X M(V) + 2 Y L(U).`                                    (2.1)

Then `R` is absolutely continuous and

`boxed( ||p_R||_infinity <= 2 sqrt(L0 M0). )`                           (2.2)

In particular, `H` may contain an arbitrary cross-bank quadratic form `U^T D V`, arbitrary within-bank quadratic forms, arbitrary bank-linear terms, and arbitrary measurable interactions between the two banks. No regularity or size bound on `H` is needed.

### Proof

Condition first on `(U,V)=(u,v)`, not on the pivots. Put `l=L(u)`, `m=M(v)`. The term `H(u,v)` is now a fixed translation. The two remaining random summands `2mX` and `2lY` are independent. Their conditional density caps are

`1/(2|m|)` and `1/(2|l|)`                                               (2.3)

at nonzero slopes. Therefore convolution gives

`||p_(R | U=u,V=v)||_infinity <= 1/[2 max(|m|,|l|)].`                  (2.4)

Since `L` and `M` are independent and have density caps `L0,M0`, for every `r>0`,

`P(max(|L|,|M|)<r)
 <= min(1,2L0 r) min(1,2M0 r)
 <= min(1,4L0 M0 r^2).`                                                (2.5)

The two scalar laws are absolutely continuous, so the simultaneous zero-slope event has probability zero. Layer cake, split at `t0=2 sqrt(L0 M0)`, yields

`E 1/max(|L|,|M|)
 = integral_0^infinity P(max(|L|,|M|)<1/t) dt
 <= t0 + integral_(t0)^infinity 4L0M0/t^2 dt
 = 4 sqrt(L0M0).`                                                      (2.6)

Averaging (2.4) proves (2.2). Tonelli supplies an integrable density representative. QED.

### Bank normalization

For linear aggregates `L=c dot U`, `M=b dot V`, put `s=||c||_2`, `r=||b||_2`. Applying the partner's source-pinned product-marginal bound (1.1),

`L0 <= sqrt(2)/s`, `M0 <= sqrt(2)/r`.

Hence Theorem 2.1 gives

`boxed( ||p_R||_infinity <= 2 sqrt(2)/sqrt(r s). )`                    (2.7)

This is the same aggregate scaling (and the same `2 sqrt(2)` constant before bank normalization) as the partner's leakage-free two-arm architecture, but now **all same-bank quadratic leakage is allowed** inside `H`.

At the exact zero-central-entry endpoint of the partner's incident-minor tube, (1.2) gives

`||p_R||_infinity < 2 sqrt(2)/sqrt(c0) < 4.084`,                       (2.8)

again with arbitrary bank leakage. Thus `QFORM-DOUBLE-STAR-DEPENDENT-BANK-LEAKAGE-v1` is completely paid at the zero pivot-core endpoint.

The mechanism is genuinely product-preserving: the reciprocal Jacobian is averaged over the two *independent aggregate slopes*. No unrestricted curved-fiber supremum appears.

## 3. A one-arm fractional coarea estimate that tolerates central coupling

The zero-core assumption in Theorem 2.1 is necessary for a bounded **base density**; Section 5 gives a sharp obstruction when a central `XY` coupling is present. What survives uniformly is the half-Riesz quantity needed for a third square.

### Lemma 3.1 — `QFORM-RANDOM-SLOPE-HALF-RIESZ-v1`

Let `X` be independent of an arbitrary random environment `E`, with `||p_X||_infinity<=L_X`. Let `T=T(E)` have density cap `L_T`, and let `K=K(E)` be arbitrary. Define

`R=K(E)+2X T(E).`                                                      (3.1)

Then

`boxed( sup_q E |q-R|^(-1/2) <= 4 sqrt(2 L_X L_T). )`                 (3.2)

### Proof

For any probability density `g<=L`, the symmetric bathtub bound gives

`sup_a integral |z-a|^(-1/2) g(z) dz
 <= L integral_(-1/(2L))^(1/(2L)) |z|^(-1/2) dz
 = 2 sqrt(2L).`                                                        (3.3)

Conditioning on `E=e`, the variable `2T(e)X` has density cap `L_X/(2|T(e)|)`, so (3.3) gives conditional half-Riesz potential at most

`2 sqrt(L_X/|T(e)|).`                                                  (3.4)

Applying (3.3) once more to the scalar law of `T`, centered at zero,

`E |T|^(-1/2) <= 2 sqrt(2L_T).`                                       (3.5)

Average (3.4) to obtain (3.2). QED.

### Corollary 3.2 — independent-square lift

Let `S` be a further independent real variable with density cap one, `a!=0`, and let `psi=psi(X,E)` be arbitrary. Then

`Q=R+a[S+psi(X,E)]^2`                                                  (3.6)

has

`boxed( ||p_Q||_infinity <= 4 sqrt(2 L_X L_T) |a|^(-1/2). )`          (3.7)

Indeed, conditional on `(X,E)`, the translated square has density kernel at most `|a|^(-1/2)|q-R|^(-1/2)`; averaging and (3.2) give (3.7).

This is a direct square-kernel/coarea estimate, not an independence-after-rotation argument.

## 4. Central cross coupling plus arbitrary bank leakage

Let the two banks and aggregates be as in Theorem 2.1, but now allow a central cross coefficient `alpha`:

`R=H(U,V,Y)+2 alpha X Y+2X M(V)+2Y L(U),`                              (4.1)

where `H` may be arbitrary and may include arbitrary quadratic phases in `U,V,Y` that do not involve `X` quadratically. Take environment `E=(Y,U,V)` and slope

`T=M(V)+alpha Y`.                                                      (4.2)

Because `M(V)` and `Y` are independent, convolution cannot increase density suprema, so

`||p_T||_infinity <= ||p_M||_infinity <= M0`.                          (4.3)

Thus Lemma 3.1 applies even though `H` may contain the entire leaking bank quadratic form. If a genuine independent square `a[S+psi]^2` is available, Corollary 3.2 gives

`||p_Q||_infinity <= 4 sqrt(2M0) |a|^(-1/2).`                          (4.4)

By symmetry one may use `L0` instead, hence the better of the two arm caps. For linear bank aggregates with norms `r,s`,

`boxed(
 ||p_Q||_infinity
 <= 2^(11/4) |a|^(-1/2) [max(r,s)]^(-1/2).
)`                                                                     (4.5)

If the partner's strong-arm product `rs>c0` holds, then `max(r,s)>=sqrt(c0)` and

`||p_Q||_infinity < 2^(11/4)c0^(-1/4)|a|^(-1/2)
                  < 8.083 |a|^(-1/2).`                                (4.6)

Therefore, **at any structural state where the third curvature is a genuine independent original-coordinate square**, neither a nonzero central `XY` coupling nor arbitrary quadratic leakage on the two arm banks is itself an obstruction. The remaining caveat is explicit: (4.1) does not allow an additional `X^2` term on the chosen linear pivot unless that term is handled separately. This report does not infer that every matrix under the bare spectral hypothesis has already been reduced to (4.1)+(3.6).

## 5. Source-valid falsifier: two arms plus arbitrary leakage do not bound the base density when the central core is nonzero

A tempting strengthening of Theorem 2.1 is false.

### Proposition 5.1 — `QFORM-TWO-ARMS-ARBITRARY-LEAKAGE-BASE-DENSITY-FALSE-v1`

Let `X,U,Y,V` be independent `Uniform[-1/2,1/2]`, all with density cap one. Then

`R=2XY+2XV+2UY+2UV=2(X+U)(Y+V)`                                      (5.1)

has an unbounded density at zero, despite two unit-strength arms and a completely legitimate same-bank leakage term `2UV`.

### Proof

Set `A=X+U`, `B=Y+V`. The two variables are independent with triangular density

`g(t)=1-|t|`, `|t|<=1`.                                                (5.2)

For `0<|z|<1/4`, the product density satisfies

`p_(AB)(z)=integral g(u)g(z/u) du/|u|`.

On `2|z|<=u<=1/2`, both `g(u)>=1/2` and `g(z/u)>=1/2`. Therefore

`p_(AB)(z) >= (1/4) integral_(2|z|)^(1/2) du/u
             = (1/4) log(1/(4|z|)) -> infinity.`                      (5.3)

Scaling by two preserves logarithmic divergence. QED.

This refutes the stronger **base-density mechanism**, not the QFORM conjecture: the four-variable matrix in (5.1) has only two nonzero eigenvalues, `+2` and `-2`.

Add an independent cap-one `S` and the third square:

`Q=2(X+U)(Y+V)+S^2.`                                                   (5.4)

The exact symmetric matrix has spectrum `{2,-2,1,0,0}`, so (5.4) is an exact target instance. Here `T=Y+V` has density cap one, and Corollary 3.2 immediately gives

`||p_Q||_infinity <= 4 sqrt(2) <5.657.`                                (5.5)

Thus this construction cleanly exhibits the role of the third curvature: the rank-two logarithm is real, while an independent third square is enough to integrate it without any moment or support assumption.

A symbolic regression file saved with this report verifies the factorization and characteristic polynomials

`chi_A4(lambda)=lambda^2(lambda-2)(lambda+2)`,
`chi_A5(lambda)=lambda^2(lambda-2)(lambda-1)(lambda+2)`,

and terminates `QFORM_B05_REVERSE_COAREA_CHECK_PASS`.

## 6. Conditional end-to-end argument and first unpaid implication

A compact proof architecture is now:

1. Existing physical-pair, ridge-window, diffuse/grouped-coordinate, and separable-perturbation branches remain available only at their proved scopes.
2. If a product-preserving reduction produces two disjoint arm banks with **zero pivot core**, Theorem 2.1 pays arbitrary same-bank quadratic leakage with the aggregate arm norms, so no local-leaf or fiber-supremum loss remains.
3. If the same architecture has a nonzero central cross coupling but also exposes a **genuine independent third square**, Lemma 3.1 + Corollary 3.2 pay arbitrary bank leakage and the central coupling through a single random aggregate slope.
4. Proposition 5.1 proves that, without the third curvature, one cannot hope to upgrade the nonzero-central branch to a uniformly bounded base density: the logarithm is genuine.

Hence the first unpaid implication is now

**`QFORM-EMBEDDED-THIRD-CURVATURE-EXTRACTION-v1`**:

> From the bare hypothesis `s_3(A)>=1` in every configuration not already covered by the completed physical-pair/ridge/diffuse/grouped-coordinate branches, either expose a product-preserving third square independent of the two strong leaking arm banks, or prove a joint coarea estimate that spends the third curvature when it is embedded inside those same banks. The reduction must tolerate arbitrary small dense self-couplings and cannot use moments, unrestricted fiber suprema, or post-rotation independence.

This is strictly sharper than the previous `DOUBLE-STAR-DEPENDENT-BANK-LEAKAGE` debt. The arbitrary bank leakage itself is no longer the missing analytic factor at zero core, and it is no longer the missing factor in the presence of an independent third square. What remains is **where the third curvature lives and how to spend it product-preservingly**.

The partner's large-central-entry branch, where the normalized cross block lies in a small Frobenius tube around rank at most two, remains a separate structural/extraction debt. No full-QFORM conclusion is claimed.

## 7. Honest status

- `ESSENTIAL_STEP_APPLIED`: reverse conditioning removes arbitrary quadratic bank leakage from the zero-core two-arm coarea state and yields a random-slope half-Riesz interface for the square-lifted nonzero-core state.
- `CANDIDATE_REFUTED`: two strong arms plus arbitrary bank leakage do **not** imply bounded base density when a nonzero central cross coupling is present; (5.1) is a source-valid product-law logarithmic witness.
- Full QFORM: **OPEN**.
- Continuity of the full target density: **not proved** here.
- Native learned-memory status: `WITHOUT_VERIFIED_BRAIN`; repository retrieval/transport is not native memory ingestion.
