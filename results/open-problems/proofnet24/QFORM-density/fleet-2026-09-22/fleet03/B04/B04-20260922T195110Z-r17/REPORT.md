SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B04, 2026-09-22T19:51:10Z.
attacking: translation-uniform fractional-trace synthesis for a scalar square coupled to two disjoint product banks; remove the independence requirement between the completed-square shift and the rank-two bank residual.

# fleet03/B04 — banked Schur half-Riesz closure

**Run:** `B04-20260922T195110Z-r17`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Product Fourier rearrangement  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Outcome:** `ESSENTIAL_STEP_APPLIED / NEW SUPPORTING THEOREM / FULL_TARGET_OPEN`

## 1. Full target and corrected scope

The full target remains open: for every dimension, independent real physical coordinates with densities bounded by one, and every real symmetric matrix with at least three eigenvalues of modulus at least one, prove a universal density cap for `X^T A X`, or give a valid counterexample. No moment, compact-support, log-concavity, Gaussianity, connected-support, or eigen-coordinate-independence assumption is used below. Continuity is tracked separately.

The live corrections prohibit the false law-uniform pointwise Fresnel-decay shortcut, post-rotation independence, arbitrary-joint coarea, positive conditional-projection density moments, and naive fiber-supremum arguments. None is used here.

The proof-first owner request names **translation-uniform fractional-trace synthesis** as a first unpaid implication. The previous B04 packet theorem bounded a scalar square plus a rank-one hyperbolic bank only when the square translation was independent of those bank variables after conditioning. This run removes that independence requirement when the bank residual is an invertible rank-two quadratic form.

## 2. Completed mathematics actually consumed

### 2.1 Orientation-free rank-two half-Riesz theorem

Completed source:

`yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`

`proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`

It proves that for independent cap-one inputs, every invertible symmetric two-dimensional quadratic form with arbitrary affine term satisfies

`sup_t E |Y^T Lambda Y + b^T Y - t|^(-1/2) <= 128 |det Lambda|^(-1/4)`,

and when the affine term lies in the two-dimensional quadratic range the constant improves to

`16 sqrt(30) |det Lambda|^(-1/4)`.

The present run applies the **sharper in-range constant** after rescaling two independent bank projections to cap-one variables. This is an actual inequality use, not a citation-only dependency. The source is a supplied complete analytic proof; its programme record says independent review is pending.

### 2.2 Disjoint-bank projection cap

Completed same-role source:

`yspennstate/math-open-problems@07305f53ba9b8a1d3e6e79f8c851f415f007d4a7`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B04/B04-20260922T181702Z-dac07509/REPORT.md`

For disjoint original-coordinate banks,

`U=u^T X_I`, `V=v^T X_J`,

with `s=||u||_2`, `t=||v||_2`, it records the product-projection bounds

`||p_U||_infinity <= sqrt(2)/s`, `||p_V||_infinity <= sqrt(2)/t`.

These are applied quantitatively below.

### 2.3 Designated partner status

The designated partner is `fleet04/B04`. A fresh direct repository lookup of

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B04`

returned no directory, and the shared handoff directory for that slot was absent. I therefore do not fabricate a designated-partner result. The completed compatible worker mathematics actually used is source-pinned above.

## 3. Scalar-square kernel with a translation depending on the residual variables

Let `Z` have density at most one, `a != 0`, and let `d` be any deterministic real number. The density `h_d` of `a(Z+d)^2` satisfies, for almost every nonzero `y`,

`h_d(y) <= |a|^(-1/2) |y|^(-1/2)`.                 (3.1)

Indeed, after reflecting the output if necessary, for `a>0` and `y>0`,

`h_d(y) = [f_Z(-d+sqrt(y/a))+f_Z(-d-sqrt(y/a))]/[2 sqrt(a y)]`

and each numerator term is at most one. The bound is uniform in `d`; for the wrong output sign the density is zero.

This elementary pointwise kernel is the reason the next theorem allows the completed-square shift to depend arbitrarily on the two bank variables. No convolution independence between the square and the bank residual is needed.

## 4. Main theorem: banked Schur half-Riesz closure

Let `{0}`, `I`, `J`, and `W` be mutually disjoint sets of original coordinates. Write

`Z=X_0`, `U=u^T X_I`, `V=v^T X_J`,

`s=||u||_2>0`, `t=||v||_2>0`, `sigma=s t`.

Let `B` be an invertible real symmetric `2 x 2` matrix and `a != 0`. Allow arbitrary measurable functions of `W` in the affine coefficients and define

`Q = a ( Z + ell_1(W) U + ell_2(W) V + d(W) )^2`
`    + [U,V] B [U,V]^T + beta_1(W) U + beta_2(W) V + R(W)`.       (4.1)

All displayed functions are deterministic once `W` is conditioned on. This includes the dependence of the square translation on `U,V`, which the preceding B04 convolution theorem did not allow.

### Theorem 4.1 — `QFORM-BANKED-SCHUR-HALFRIESZ-v1`

Under (4.1), `Q` has an essentially bounded density and

`||p_Q||_infinity`
` <= 16 sqrt(60) |a|^(-1/2) sigma^(-1/2) |det B|^(-1/4)`.       (4.2)

Numerically,

`16 sqrt(60) = 123.93546707863734...`.                          (4.3)

No continuity claim is made by this theorem.

### Proof

Condition on `W=w`. Because `{0}`, `I`, `J`, and `W` are disjoint original-coordinate groups, `Z,U,V` remain independent under this conditioning.

Put

`T_w(U,V)=[U,V]B[U,V]^T+beta_1(w)U+beta_2(w)V+R(w)`.

For fixed `(u,v)`, (3.1) applied with the deterministic translation

`d = ell_1(w)u+ell_2(w)v+d(w)`

gives a conditional density kernel satisfying

`p_{Q | U=u,V=v,W=w}(x)`
` <= |a|^(-1/2) |x-T_w(u,v)|^(-1/2)`                           (4.4)

for almost every `x`. Averaging over `(U,V)` yields

`p_{Q|W=w}(x)`
` <= |a|^(-1/2) E[ |x-T_w(U,V)|^(-1/2) | W=w ]`.              (4.5)

Now let

`K_U=sqrt(2)/s`, `K_V=sqrt(2)/t`.

By the disjoint-bank projection theorem,

`||p_U||_infinity<=K_U`, `||p_V||_infinity<=K_V`.              (4.6)

Set `U'=K_U U`, `V'=K_V V`. Then `U',V'` are independent and each has density cap at most one. In these variables the quadratic matrix is

`B' = diag(K_U^(-1),K_V^(-1)) B diag(K_U^(-1),K_V^(-1))`,      (4.7)

so

`|det B'| = |det B|/(K_U^2 K_V^2)`.                            (4.8)

The affine term in `(U',V')` lies in the full two-dimensional quadratic range. Applying the completed rank-two affine half-Riesz theorem with its sharper in-range constant therefore gives

`sup_x E |x-T_w(U,V)|^(-1/2)`
` <= 16 sqrt(30) |det B'|^(-1/4)`
` = 16 sqrt(30) |det B|^(-1/4) (K_U K_V)^(1/2).`              (4.9)

Since

`K_U K_V <= 2/(s t)=2/sigma`,                                  (4.10)

(4.9) becomes

`sup_x E |x-T_w(U,V)|^(-1/2)`
` <= 16 sqrt(60) sigma^(-1/2)|det B|^(-1/4)`.                 (4.11)

Combine (4.5) and (4.11). The bound is uniform in `w`; averaging the conditional densities over `W` proves existence of an essentially bounded density and (4.2). QED.

### What was paid

The completed-square shift may now contain `U` and `V` themselves. Thus the square and rank-two bank residual need not be independent after completing the square. The price is a half-Riesz estimate rather than the sharper `L^(3/2)*L^3` convolution constant from the preceding B04 run.

The theorem pays the bank scale `sigma=||u||_2||v||_2`, not one physical coefficient. It therefore remains dimension-free when every individual coefficient in the two banks tends to zero.

## 5. Explicit genuinely rotated indefinite target family

For each integer `m>=2`, take disjoint original-coordinate groups

`Z`, `X_1,...,X_m`, `Y_1,...,Y_m`

with arbitrary independent densities bounded by one. Put

`u=v=m^(-1/2)(1,...,1)`,
`U=u^T X`, `V=v^T Y`.

Consider

`Q_m = 3[(Z+U)^2 + U^2 - V^2]`.                               (5.1)

On the active orthonormal span `(Z,U,V)`, the matrix equals

`3 * [[1,1,0],[1,2,0],[0,0,-1]]`.                              (5.2)

Its three nonzero eigenvalues are exactly

`3(3+sqrt(5))/2`, `3(3-sqrt(5))/2`, `-3`.                     (5.3)

Since

`3(3-sqrt(5))/2 = 1.145898033750315... > 1`,                  (5.4)

this is an exact target instance with three eigenvalues of modulus at least one, indefinite signature, and a genuinely rotated positive two-plane.

In original coordinates, singleton-to-bank coefficients are of order `m^(-1/2)` and in-bank coefficients are of order `m^(-1)`; no fixed physical coefficient survives as `m->infinity`.

Apply Theorem 4.1 with

`a=3`, `B=3 diag(1,-1)`, `sigma=1`, `|det B|=9`.

Then every admissible product input law satisfies

`||p_(Q_m)||_infinity`
` <= 16 sqrt(60) * 3^(-1/2) * 9^(-1/4)`
` = 16 sqrt(60)/3`
` = 41.31182235954578...`.                                    (5.5)

This example is not diagonal in the independent coordinates and explicitly uses the new correlated completed-square translation `Z+U`.

## 6. Relation to the full target and first unpaid implication

This theorem does **not** prove the full conjecture. An arbitrary matrix with three large eigenvalues has not been shown to contain, after product-preserving conditioning/grouping, a packet of the exact form (4.1) with uniformly bounded reciprocal cost

`|a|^(-1/2) sigma^(-1/2)|det B|^(-1/4)`.

The first unpaid implication is therefore the structural routing problem:

> Given arbitrary symmetric `A` with `s_3(A)>=1`, either extract a product-preserving scalar-square plus two-bank rank-two Schur packet whose above reciprocal cost is universally bounded, or route quantitatively to an already paid ridge/full-matrix-pair/diffuse/multi-bank branch, without selecting a vanishing local minor and without discarding quadratic leakage.

The new theorem removes one analytic obstruction from that routing problem: **dependence of the scalar-square translation on the two bank variables is no longer an obstruction** whenever the residual bank quadratic is invertible.

A remaining genuinely hard branch is a zero/near-isotropic scalar pivot together with a rank-deficient or badly routed residual bank block. That is consistent with the fresh proof-first owner priority.

## 7. Status

- Full QFORM: `OPEN`.
- New theorem: supporting analytic theorem proved conditional on the source-pinned rank-two half-Riesz theorem and standard disjoint-bank projection cap.
- Continuity: **not proved** by this theorem; only existence of an essentially bounded density.
- Designated `fleet04/B04` result: none available at fresh lookup; none invented.
- Pointwise Fresnel decay: not used.
- Post-rotation independence: not used.
- Repository access is not native brain ingestion: status remains `WITHOUT_VERIFIED_BRAIN`.
