SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B15, 2026-09-23T17:28:33Z.
attacking: an expected-conditional-height regularity compiler that replaces a fiber supremum by the actual conditioning average, while separating absolute continuity, essential height, and C0 continuity.

# fleet03/B15 auto24 — expected conditional height and C0 mixture compiler

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T172833Z-fleet03-B15-qform-auto24`  
Status: `NEW TARGET-LEVEL REGULARITY COMPILER / PARTNER APPLIED / FULL QFORM OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`.

The full unrestricted universal-height conjecture remains OPEN. This report proves a target-level regularity lemma that is deliberately weaker than a uniform fiber-supremum requirement and therefore fits the live correction that naive fiber suprema can lose dimension.

## 1. Exact implication ledger

There are three logically distinct statements.

1. **Absolute continuity.** For every nonzero real quadratic polynomial `q(x)=x^T A x+b^T x+c` and every absolutely continuous joint input law, `q(X)` is absolutely continuous. No product structure or density cap is needed for this qualitative fact.
2. **Instancewise bounded/continuous density.** The completed fixed-instance B15 source proves that for every fixed symmetric `A` of rank at least three and every independent cap-one product law, `X^T A X` has an instance-dependent bounded density with a representative in `C_0(R)`. Its constants can deteriorate with physical pivots/minors and do not solve the owner’s quantifier reversal.
3. **Universal height.** The still-unpaid statement is one constant `C` valid simultaneously over all dimensions, all admissible product laws and all symmetric `A` with `s_3(A)>=1`.

The live shared claim ledger still marks the full theorem open. Nothing below changes that status.

## 2. Absolute continuity, separately and with no height claim

Let `q(x)=x^T A x+b^T x+c` be nonconstant. Its critical set

    Crit(q)={x: 2Ax+b=0}

is either empty or a proper affine subspace, hence Lebesgue-null. Let `N subset R` be Lebesgue-null and

    E_k={x: |x|<=k, |grad q(x)|>=1/k}.

Coarea gives

    integral_{E_k cap q^{-1}(N)} |grad q(x)| dx
      = integral_N H^{n-1}(E_k cap q^{-1}(t)) dt = 0.

Hence `Leb(E_k cap q^{-1}(N))=0`. The union of the `E_k` covers the complement of the critical set up to a null set, so `q^{-1}(N)` is null. Any absolutely continuous joint law therefore gives `P(q(X) in N)=0`.

This proves a density exists; it gives no finite universal or instancewise `L^infinity` constant.

## 3. Exact heat-height functional

For a probability law `mu` on `R`, let

    gamma_r(x)=(2*pi*r^2)^(-1/2) exp(-x^2/(2r^2))

and define the countably measurable heat height

    H(mu)=sup_{r in Q_{>0}, y in Q} (mu*gamma_r)(y) in [0,infinity].

### Lemma 3.1 — exact height identity

`H(mu)` is exactly the optimal essential density height, in the extended sense:

    H(mu)=inf{ ||p||_infinity : mu=p(x) dx },

with the right side `+infinity` when no bounded density exists.

### Proof

If `mu=p dx` and `||p||_infinity=M`, then convolution with a probability kernel gives `(mu*gamma_r)(y)<=M`, hence `H(mu)<=M`. Conversely, if `H(mu)=M<infinity`, continuity of each Gaussian convolution extends the rational-center bound to every center. For every nonnegative `phi in C_c(R)`,

    integral phi dmu
      = lim_{r downarrow 0, r rational} integral phi(y) (mu*gamma_r)(y) dy
      <= M integral phi(y) dy.

Thus `mu<=M dy`, so `mu` has a density bounded by `M`. Applying the first half to that density gives equality. This also shows that no prior absolute-continuity assumption is needed in the heat formulation.

## 4. New lemma: expected conditional height is enough

### Theorem 4.1 — `QFORM-CONDITIONAL-EXPECTED-HEIGHT-COMPILER-v1`

Let `(Y,W)` be a random pair on standard Borel spaces and let `mu_w=L(Y|W=w)` be a regular conditional law. Then

    boxed( H(L(Y)) <= E[ H(mu_W) ]. )                 (4.1)

The right side may be infinite. In particular, if `E H(mu_W)<=C`, then `Y` has a density satisfying

    boxed( ||p_Y||_infinity <= C. )                  (4.2)

This requires an **average of actual conditional output heights**, not a supremum over conditioning values.

### Proof

For every rational `r>0` and rational `y`, disintegration gives

    (L(Y)*gamma_r)(y)
       = E[(mu_W*gamma_r)(y)]
       <= E H(mu_W).

Take the countable supremum in `(r,y)` and invoke Lemma 3.1. QED.

### Theorem 4.2 — C0 upgrade with an integrable height envelope

Assume in addition that, for almost every `w`, `mu_w` has a density `p_w in C_0(R)`, and there is a measurable `M(w)` with

    ||p_w||_infinity <= M(w),       E M(W)<infinity.

Then the unconditional law has a density

    p(y)=E[p_W(y)]

with

    boxed( p in C_0(R),   ||p||_infinity <= E M(W). )    (4.3)

No common modulus of continuity of the family `{p_w}` is required.

### Measurability and proof

A jointly measurable density version can be obtained canonically from the conditional kernels. Put

    k_m(w,y)=(mu_w*gamma_{1/m})(y).

Each `k_m` is jointly measurable. On every good fiber with `p_w in C_0`, Gaussian approximate identities satisfy `k_m(w,.) -> p_w` uniformly. Hence `p_*(w,y)=limsup_m k_m(w,y)` is jointly measurable and equals `p_w(y)` for almost every `w`. Tonelli shows that `p(y)=E p_*(W,y)` is a density of `Y`.

If `y_n->y`, then `p_*(W,y_n)->p_*(W,y)` almost surely and `|p_*(W,y_n)|<=M(W)` almost surely, so dominated convergence proves continuity. If `|y_n|->infinity`, the fiberwise `C_0` property gives `p_*(W,y_n)->0`, and the same domination proves `p(y_n)->0`. The height inequality follows by averaging.

This is the exact regularity replacement for the stronger but often wasteful gate `sup_w ||p_w||_infinity<infinity`.

## 5. QFORM interpretation: average a conditional output certificate, do not take a fiber supremum

Fix any original-coordinate subset `I` and put `W=X_{I^c}`. Because the original law is a product, conditioning on `W=w` leaves the coordinates `X_I` independent with the same cap-one marginals. The conditional polynomial is an affine quadratic in those original coordinates; outside variables create affine and constant terms but do not rotate the source law.

Therefore a future proof may use the following valid interface:

> If one constructs a measurable conditional certificate `M(W)` for the **actual conditional quadratic-output density** such that `||p_{Q|W}||_infinity<=M(W)` almost surely and `E M(W)<=C`, then the full output satisfies `||p_Q||_infinity<=C`. If those conditional densities lie in `C_0`, then `p_Q in C_0` as well.

This is materially weaker than controlling `sup_w M(w)`. It does not resurrect the refuted projection-density/fiber-supremum mechanism: the quantity being averaged is the genuine conditional **output** height after all product-preserving smoothing on the selected coordinates. A bound on a projected input density or on an arbitrary indefinite surface trace is not a substitute.

## 6. Assigned partner fleet04/B15 applied at an actual inequality

Completed partner source:

`yspennstate/math-open-problems@cff8e1368d32302e6d649f776579a5c1951929b1`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B15/20260923T151702Z-fleet04-B15-pivoted-convolution-r6/REPORT.md`.

It proves for independent cap-one `X,Y`

    T=a X^2 + 2b X Y + 2u X + 2v Y + c,
    ||p_T||_p <= p |b|^{-1+1/p},                       (6.1)

uniformly in `a,u,v,c`, and for an independent square receiver

    S=gamma Z^2+2wZ,
    ||p_S||_{3/2} <= 2 |gamma|^{-1/3}.                 (6.2)

With `p=3`, convolution gives the conditional `C_0` bound

    ||p_{T+S}||_infinity
       <= 6 |b|^{-2/3} |gamma|^{-1/3}.                 (6.3)

Now take an ambient QFORM whose physical principal block on three original coordinates is

        [ a  b  0 ]
        [ b  0  0 ]
        [ 0  0  gamma ],

with arbitrary outside block and arbitrary outside couplings. Condition on all outside original coordinates `W`. They generate only affine terms in the selected three coordinates, so the partner theorem gives for almost every `w`

    p_{Q|W=w} in C_0,
    H(L(Q|W=w)) <= 6 |b|^{-2/3}|gamma|^{-1/3}.          (6.4)

Applying Theorems 4.1-4.2 gives the actual unconditional inequality

    boxed(
      p_Q in C_0(R),
      ||p_Q||_infinity <= 6 |b|^{-2/3}|gamma|^{-1/3}.
    )                                                   (6.5)

Thus the partner branch is recovered through the more general expected-height compiler. When `b^2>=|a|+1` and `|gamma|>=1`, the three block eigenvalues have modulus at least one and (6.5) gives `||p_Q||_infinity<=6`.

## 7. Precise status of continuity versus universal height

A completed source theorem at

`yspennstate/math-open-problems@9b8bb7e84811978a2c46c7bb5ec50f2570dbc056`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B15/20260922T200544Z-fleet02-B15-qform-r11/REPORT.md`

proves, with instance-dependent constants,

    rank(A)>=3  =>  p_{X^TAX} in C_0(R) cap L^infinity(R)

for every cap-one product law. I reread the proof structure relevant to the present compiler: absolute continuity by coarea, smooth compact-input `C_0` regularity, rough zero-diagonal stability, and the complementary nonzero-physical-diagonal theorem. I do not relabel the shared claim ledger here; promotion/consolidation is reserved to the authorized updater and any requested independent review.

Assuming that completed fixed-instance theorem, the owner’s continuous-density request and the central height conjecture have the **same optimal universal constant**. Indeed, for each target instance the `C_0` representative is unique as a density up to null sets, and for a continuous function

    sup_y p(y) = ess sup_y p(y).

If a continuous density exceeded its essential supremum at one point, continuity would force a positive-measure neighborhood of exceedance. Therefore

    sup_target esssup p_Q
      = sup_target max_y p_Q(y),                        (7.1)

with either side allowed to be `+infinity`. Thus no class-wide continuity modulus is required to finish the owner’s stronger statement once the universal height is obtained.

This is consistent with the newest fleet02/B15 obstruction: even on the exact countable core there is no common translation modulus or pointwise continuity modulus. The correct target is existence of a continuous representative instance by instance plus a separate universal height estimate, not uniform equicontinuity.

## 8. What this does and does not solve

The new compiler removes one avoidable source of loss: a proof does **not** need a worst-case conditional-fiber height if it can control the expected actual conditional output height. This is potentially useful precisely where rare bad fibers make a supremum diverge.

It does not itself produce a universal `E M(W)` bound from the three-large-eigenvalue hypothesis. The first unpaid implication remains:

    find one product-preserving decomposition or direct argument with
    E H(L(Q|W)) <= C

uniformly over every target instance, or prove the equivalent unconditional height bound directly. Current local principal-block constants can degenerate along valid diffuse/bank families, and the live correction inbox forbids replacing the missing averaged output estimate by a generic projection cap, arbitrary-joint coarea bound, post-rotation independence, or pointwise quadratic-phase decay.

The natural next B15 use is to take a current hub/grouped-bank decomposition whose local certificate depends on the conditioned environment and test its **expectation** rather than its essential supremum. A finite expected certificate would close both bounded density and continuity through Theorem 4.2.

## 9. Source/correction integrity


Consumed corrections include the false uniform pointwise phase decay, no post-rotation independence, dimension-loss from naive fiber suprema, false arbitrary-joint coarea height, false conditional projection-moment gates, no uniformly good single minor/cross cut, and no uniform fragment-count reduction. None is used positively.

The current Claude continuation at `proofnet24/QFORM-density/interactive/20260922T231000Z-semidefinite-and-hub-reduction/README.md` was read from current `math-open-problems` master. Its full conjecture status remains open; its hub and projected-crossing results are supporting inputs, not a completed rough-law universal theorem.

No Gaussian, log-concavity, moment, compact-support, connected-support, diagonal-basis, or centered-input hypothesis has been inserted. No schedule/task/notification/email/permission/model/API setting is changed by this mathematical report.
