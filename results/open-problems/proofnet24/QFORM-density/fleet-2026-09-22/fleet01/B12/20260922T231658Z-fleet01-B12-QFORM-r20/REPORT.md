SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B12, 2026-09-22T23:16:58Z.
attacking: hybrid spike-plus-tail stability — absorb arbitrarily large signed spectral spikes by rank reserve, while paying an arbitrary-rank small spectral tail only once before the protected two-bank certificate.

# fleet01/B12 r20 — hybrid arbitrary-spike plus small-tail stability

## Status

**PROVED SUPPORTING STABILITY THEOREM. FULL QFORM TARGET REMAINS OPEN.**

Programme: `QFORM-DENSITY-3EIG-20260922`, programme revision `2026-09-22.5`. Owner-control revision read during the run: `2026-09-22.15`. Initial fresh control commit: `yspennstate/math-research-brain@6e7f0085d2613381adfbbb53e54f20eebd5f18df`; first substantive refresh: `@0693556aa32a772fb70ca0eb0e1da6b5acf9fb1a`. Execution state: `WITHOUT_VERIFIED_BRAIN`.

The exact target remains: for independent real original-coordinate inputs with densities bounded by one and a real symmetric matrix with at least three eigenvalues of modulus at least one, prove a universal density cap for `X^T A X`, or give a valid counterexample. No Gaussianity, log-concavity, moment, compact-support, connected-support, pointwise van-der-Corput decay, post-rotation independence, arbitrary-joint coarea, or normalized worst-fiber estimate is used below.

The new result combines the two genuinely different additional-eigenvalue currencies already isolated by the fleet:

1. **arbitrarily large spectral changes** are paid by a finite rank reserve, not by operator norm;
2. **arbitrarily many remaining smaller spectral changes** are paid by one operator-norm tail parameter.

The combination is not a convolution statement: all conditioning remains in original-coordinate product blocks.

## Source-valid designated-partner result actually used

The designated partner `fleet02/B12` proved `QFORM-RANK-RESERVE-PAIR-COMPRESSION-STABILITY-v1` at

`yspennstate/math-open-problems@b873b2b52f4c75c331153c9227d0a7fae0f02979`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B12/20260922T225440Z-fleet02-B12-QFORM-r19/REPORT.md`.

In its original-coordinate two-bank factorization, let a base reduced core `H_base` have a protected leading `2 x 2` bank pair `B_base`, with

`beta_base = sigma_min(B_base)>0`

and

`s_(3+r)(H_base) >= s_base >0`.

If a symmetric perturbation `R` has `rank(R)<=r` and its protected pair compression satisfies

`delta = ||R_[12,12]||_op < beta_base`,

then the final core retains `s_3>=s_base`. If `B_base` is indefinite, the full ambient quadratic form, with arbitrary outside quadratic block and arbitrary cross couplings, has density cap

`6*400^(1/3) [ (beta_base-delta)^5 s_base ]^(-1/6)`.          (P-ind)

If `B_base` is definite, the cap is

`2*pi/(beta_base-delta)`.                                      (P-def)

This theorem itself already uses only original-coordinate product structure and a dependence-safe arbitrary-completion compiler.

## 1. Hybrid theorem: arbitrary large rank-r spike + arbitrary-rank small tail

### Theorem `QFORM-HYBRID-SPIKE-TAIL-PAIR-STABILITY-v1`

Work in the same two-bank reduced-core setup as the designated partner. Let the protected base core `H_0` satisfy

`s_(3+r)(H_0) >= s_0 >0`,                                      (1.1)

and let its protected pair be `B_0`, with

`beta_0 = sigma_min(B_0)>0`.                                   (1.2)

Add an arbitrary symmetric reduced-core perturbation

`E = R + S`,                                                    (1.3)

where

`rank(R) <= r`,                                                 (1.4)

`epsilon = ||S||_op`,                                           (1.5)

and

`delta = ||R_[12,12]||_op`.                                    (1.6)

No sign or size restriction is imposed on the nonzero eigenvalues of `R`; `S` may have completely arbitrary rank and sign pattern. Assume only

`epsilon < s_0`,                                                (1.7)

`epsilon + delta < beta_0`.                                    (1.8)

Then the final full ambient quadratic form has an essentially bounded density. More precisely:

### Indefinite protected pair

If `B_0` is invertible indefinite,

`boxed(||p_Q||_infinity
 <= 6*400^(1/3)
    [ (beta_0-epsilon-delta)^5 (s_0-epsilon) ]^(-1/6)).`        (1.9)

### Definite protected pair

If `B_0` is positive or negative definite,

`boxed(||p_Q||_infinity
 <= 2*pi/(beta_0-epsilon-delta).)`                              (1.10)

Every outside quadratic coefficient, outside eigenvalue, and reduced-core/outside cross coupling is arbitrary.

### Proof

Set

`H_tilde = H_0 + S`.                                           (1.11)

By the 1-Lipschitz Weyl inequality for singular values,

`s_(3+r)(H_tilde)
 >= s_(3+r)(H_0) - ||S||_op
 >= s_0 - epsilon`.                                             (1.12)

Let

`B_tilde = B_0 + S_[12,12]`.                                   (1.13)

Because a principal compression cannot increase operator norm,

`||S_[12,12]||_op <= epsilon`.                                 (1.14)

Hence

`sigma_min(B_tilde) >= beta_0-epsilon`.                         (1.15)

Moreover `epsilon<beta_0` by (1.8), so for every `0<=t<=1`,

`sigma_min(B_0+tS_[12,12]) >= beta_0-t epsilon>0`.              (1.16)

Therefore `B_tilde` has the same inertia as `B_0`.

Now regard `H_tilde` as the **base** in the completed fleet02/B12 partner theorem and `R` as its rank-`r` perturbation. Its pair price is exactly `delta`, and (1.8) gives

`delta < beta_0-epsilon <= sigma_min(B_tilde)`.                 (1.17)

The partner theorem therefore applies with

`s_base = s_0-epsilon`,
`beta_base = sigma_min(B_tilde) >= beta_0-epsilon`.             (1.18)

If `B_0` is indefinite, so is `B_tilde`, and (P-ind) gives

`||p_Q||_infinity
 <= 6*400^(1/3)
    [ (sigma_min(B_tilde)-delta)^5 (s_0-epsilon) ]^(-1/6)`
` <= 6*400^(1/3)
    [ (beta_0-epsilon-delta)^5 (s_0-epsilon) ]^(-1/6)`,         (1.19)

which is (1.9).

If `B_0` is definite, so is `B_tilde`, and (P-def) gives

`||p_Q||_infinity
 <= 2*pi/(sigma_min(B_tilde)-delta)
 <= 2*pi/(beta_0-epsilon-delta)`,                              (1.20)

which is (1.10). QED.

### What is genuinely new in (1.9)

The partner r19 theorem permits a perturbation of arbitrary magnitude but only finite rank. The fleet03/B12 finite-tail theorem permits arbitrary-rank perturbations but requires small operator norm inside its protected finite packet. The present theorem permits both simultaneously:

- `R` may contain `r` spectral spikes of **arbitrary size and either sign**;
- `S` may contain **arbitrarily many** further eigenvalues of either sign, with only `||S||_op` charged;
- the only interaction between the two payments is the additive pair-gap loss `epsilon+delta` and the one-time third-source loss `epsilon`.

There is no factor exponential in `r`, no dependence on the number of tail eigenvalues, and no convolution with a dependent spectral remainder.

## 2. Ambient spectral-cloud corollary

The theorem is useful for a genuine full-matrix spectral addition, not merely an abstract reduced-core perturbation.

Let the added ambient symmetric matrix have spectral decomposition

`E_amb = sum_(j=1)^N theta_j v_j v_j^T`,                        (2.1)

where the `v_j` are orthonormal and the real `theta_j` may have either sign. Let `P_c` denote projection onto the partner's reduced core and `P_b` projection onto the two protected bank coordinates inside that core.

Choose any index set `J` with `|J|<=r`, and split

`E_amb = R_amb + S_amb`,                                       (2.2)

`R_amb = sum_(j in J) theta_j v_jv_j^T`,
`S_amb = sum_(j notin J) theta_j v_jv_j^T`.                    (2.3)

The reduced-core spike

`R=P_c R_amb P_c`

has rank at most `r`, regardless of how large the selected `theta_j` are. The reduced-core tail obeys

`||P_c S_amb P_c||_op <= ||S_amb||_op
 = epsilon_J := max_(j notin J) |theta_j|`.                    (2.4)

For the protected pair,

`delta_J := ||P_b R_amb P_b||_op`
` <= sum_(j in J) |theta_j| ||P_b v_j||_2^2`.                  (2.5)

Thus a completely explicit sufficient condition is

`epsilon_J < s_0`,                                             (2.6)

`epsilon_J + sum_(j in J)|theta_j| ||P_b v_j||_2^2 < beta_0`.  (2.7)

Under (2.6)-(2.7), (1.9) or (1.10) applies with

`epsilon=epsilon_J`,
`delta <= sum_(j in J)|theta_j| ||P_b v_j||_2^2`.              (2.8)

All cross terms generated by the ambient spectral vectors between the reduced core and outside coordinates, and all outside quadratic terms, simply alter the already-arbitrary completion in the partner theorem. They are not treated as independent.

### Interpretation

A selected eigenvalue `theta_j` may be arbitrarily large if its leverage on the protected bank pair is correspondingly small. In particular, if

`P_b v_j=0` for all `j in J`,                                   (2.9)

then the selected `r` eigenvalues cost **zero pair gap regardless of magnitude or sign**. Every unselected eigenvalue is allowed provided its modulus is at most the single tail scale `epsilon_J`.

This is a literal large-plus-small eigenvalue stability statement: finitely many enormous arbitrary-sign spikes and arbitrarily many smaller arbitrary-sign eigenvalues can coexist with one dimension-free density certificate.

## 3. Concrete uniform family with arbitrarily many large and small added eigenvalues

Fix arbitrary integers `r,q>=0` and consider the protected reduced-core base

`H_0 = diag(1,-1,1, I_r, 0_q)`.                                (3.1)

Take the first two coordinates as the protected bank pair. Then

`B_0=diag(1,-1)`,
`beta_0=1`,
`s_(3+r)(H_0)=1`.                                               (3.2)

Now replace the `r` reserve eigenvalues by arbitrary real numbers `mu_1,...,mu_r`, with no magnitude or sign restriction, and add `q` arbitrary small eigenvalues `nu_1,...,nu_q` satisfying

`|nu_k|<=epsilon<1`.                                            (3.3)

Equivalently the final core is

`H = diag(1,-1,1, mu_1,...,mu_r, nu_1,...,nu_q)`.              (3.4)

Use

`R=diag(0,0,0, mu_1-1,...,mu_r-1, 0_q)`,
`S=diag(0,0,0, 0_r, nu_1,...,nu_q)`.                           (3.5)

Then

`rank(R)<=r`,
`delta=0`,
`||S||_op<=epsilon`.                                            (3.6)

The indefinite theorem gives

`boxed(||p_Q||_infinity
 <= 6*400^(1/3)/(1-epsilon).)`                                 (3.7)

The bound is independent of `r`, `q`, every `mu_j`, and every `nu_k` subject only to (3.3). Numerically,

`6*400^(1/3)=44.2083779836846...`.                              (3.8)

For `epsilon<=1/4`,

`boxed(||p_Q||_infinity <= 58.9445039782462...).`               (3.9)

The partner theorem still allows an arbitrary outside quadratic remainder and arbitrary outside/core cross coupling compatible with its original-coordinate factorization.

This family is deliberately stronger than either one-sided limit separately: the `mu_j` can be `10^100`, `-10^100`, zero, or mixed, while `q` can be arbitrarily large.

## 4. Pair-aware approximation formulation

For a general reduced-core perturbation `E`, define its rank-`r` pair-aware feasible set by all decompositions

`E=R+S`, `rank(R)<=r`.                                         (4.1)

Every such decomposition provides two costs

`epsilon(R)=||S||_op`,
`delta(R)=||R_[12,12]||_op`.                                   (4.2)

The theorem says that **any** decomposition satisfying

`epsilon(R)<s_0`,
`epsilon(R)+delta(R)<beta_0`                                   (4.3)

is a valid certificate. Therefore one is free to choose the rank-`r` part to optimize pair protection rather than merely taking the `r` largest eigenvalues. This matters for perturbations having one huge eigenvalue with substantial pair leverage and another slightly smaller eigenvalue almost invisible on the pair: the better certificate may spend reserve on the pair-dangerous direction rather than on strict spectral magnitude order.

This pair-aware decomposition is an exact deterministic optimization problem. No probabilistic or numerical extremality claim is required.

## 5. Relation to the full target and the first unpaid implication

This result advances the assigned additional-eigenvalue problem but does not derive its hypotheses from the bare target assumption `s_3(A)>=1`.

The precise unpaid structural implication is now:

> From an arbitrary target matrix with only `s_3(A)>=1`, either extract a protected original-coordinate two-bank packet with enough reserve to admit a decomposition satisfying (4.3), or switch before reciprocal pair payment to one of the already-proved ridge, grouped-bank, physical-triple, hub, or cross-volume branches.

The theorem shows that once such a packet exists, **mixed spectral scales are no longer an obstruction**: finitely many arbitrarily large signed additions and an arbitrarily high-rank smaller tail can be handled simultaneously.

It does not claim that every target matrix admits the protected pair, nor that the constant is sharp. The known singleton-plus-two-banks, Hadamard, and high-anchor stress families still forbid replacing the missing structural step by a one-good-minor assertion.

## 6. Regularity and integrity

The theorem proves existence of an essentially bounded density in its stated scope. **Continuity is not proved here.**

All independence statements refer only to the original coordinate blocks in the source partner theorem. A general spectral rotation is never declared to preserve independence. The arbitrary outside quadratic remainder is handled through the partner's completed dependence-safe arbitrary-completion mechanism.

No numerical experiment is used as proof. A private fixed-seed sanity check of the two elementary matrix inequalities (singular-value Weyl and pair-gap Weyl) found zero violations in 2,000 random trials; this is corroboration only.

Claim ID: `QFORM-HYBRID-SPIKE-TAIL-PAIR-STABILITY-v1`.
