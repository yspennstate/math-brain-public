SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B06, 2026-09-22T22:35:25Z.
attacking: two-sided curvature absorption by retaining one genuine physical hyperbolic pair and paying its moving logarithmic singularity against a remote rank-two product cross-smoother.

# account01/B06 r18 — an isolated hyperbolic pair can be paid by a remote rank-two cross smoother

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: curved fiber integration / GEOMETRY  
Outcome: `ESSENTIAL_STEP_APPLIED / SUPPORTING_THEOREM_PROVED / FULL_TARGET_OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`

The full target remains open. This report proves a new dimension-free composition lemma and a weighted original-coordinate corollary. It does not claim the bare three-large-eigenvalue hypothesis automatically supplies the new branch.

## 1. Exact source dependencies

Fresh control at the beginning of the run was `yspennstate/math-research-brain@e32f0a7869f892f268455300b2eb02b5e1900d21`; a prepublication refresh reached `a94dcdc9a270df65a05879c412b34d4f58586413`. OWNER CONTROL remained revision `2026-09-22.15`, QFORM-only.

The exact partner theorem used below is account02/B06 `QFORM-ONE-SIDED-RANK2-CROSS-SMOOTHER-v1`, canonical report

`yspennstate/math-open-problems@dc9752d372165b011f4c8b1101174a6698ae2c64:proofnet24/QFORM-density/fleet-2026-09-22/account02/B06/b06-20260922T210504Z-abc2116c80c5/REPORT.md`.

It states: if original coordinates are partitioned into product banks `I,J,K`, and after conditioning `K`

`R=F(X_I)+2 X_I^T H X_J+b^T X_J+c`

with `F` arbitrary measurable, no quadratic self-term on `J`, and `s_2(H)=sigma>0`, then

`||p_R||_infinity <= e sqrt(pi)/sigma`.                                    (1.1)

The curved-pair input is the complete logarithmic physical-pair envelope

`yspennstate/math-open-problems@f7f0fedb2d93b46824f96cac1164af6f8a55626f:proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/PAIR_LOG_THEOREM.md`.

For two independent original coordinates with cap-one densities and an invertible indefinite symmetric `2x2` block `B`, putting

`D=|det B|`, `kappa=sigma_min(B)`,

after completing the pair the conditional density satisfies, for every cutoff `r>0`,

`p_pair(t) <= 2 sqrt(2)/r + D^(-1/2) log_+(2 r^2/(kappa |t-t0|))`.          (1.2)

The shifts of the physical pair may depend arbitrarily on all remaining variables. No independence after diagonalizing `B` is asserted.

Binding corrections retained: no law-uniform pointwise quadratic-phase decay; no post-rotation independence; no arbitrary-joint rank-three coarea; no worst conditional projection-density positive moment; no unrestricted fiber-sup payment; no perturbative replacement of a nonzero opposite self-block by zero. In particular account02/B06's exact rank-two factorization example shows that `||G||_op small` is not a valid substitute for the structural hypotheses below.

## 2. A bounded-density logarithm lemma

### Lemma 2.1

Let `W` be any real random variable with an essentially bounded density `p_W<=M`. Then for every `a>0` and `t in R`,

`E log_+(a/|W-t|) <= 2 a M`.                                                (2.1)

### Proof

Using only the density cap,

`E log_+(a/|W-t|)`
` <= M integral_{|u|<a} log(a/|u|) du`
` = 2 M integral_0^a log(a/u) du`
` = 2 a M`.

No support or moment hypothesis is used. QED.

This is the key weighted replacement: the hyperbolic logarithmic singularity is integrated against the actual probability density of the moving critical value before any supremum is taken.

## 3. Main composition theorem

### Theorem 3.1 — `QFORM-ISOLATED-HYPERBOLIC-PAIR-REMOTE-CROSS-SMOOTHER-v1`

Partition ORIGINAL coordinates into four disjoint banks

`I, P, T, K`, with `|P|=2`.

Condition on `X_K=k`. Suppose the remaining quadratic form can be written

`Q_k = F_k(X_I)`
`      +2 X_I^T H_P X_P`
`      +2 X_I^T H_T X_T`
`      +X_P^T B X_P`
`      +b_P(k)^T X_P+b_T(k)^T X_T+c_k`,                              (3.1)

where

* `F_k` is arbitrary measurable (in particular it may contain arbitrary quadratic and affine curvature on the whole `I` bank),
* `B` is an invertible indefinite symmetric `2x2` matrix,
* there is **no** quadratic `T-T` term,
* there is **no** quadratic `P-T` coupling,
* `s_2(H_T)=sigma_T>0`.

Let

`D=|det B|`, `kappa=sigma_min(B)`.

Then the full unconditional law has an essentially bounded density and

`boxed( ||p_Q||_infinity`
`       <= 6 (e sqrt(pi))^(1/3) D^(-1/6) kappa^(-1/3) sigma_T^(-1/3) ).` (3.2)

Numerically the universal prefactor is

`6 (e sqrt(pi))^(1/3) = 10.1338480906...`.                              (3.3)

Continuity is not proved by this argument.

### Proof

Fix `k`; every estimate is uniform in the conditioned outside variables.

Write `U=X_I`, `V=X_P`, `Z=X_T`, and define

`a(U)=H_P^T U + b_P(k)/2`.

Complete the physical pair:

`V^T B V +2 a(U)^T V`
` = (V+B^(-1)a(U))^T B (V+B^(-1)a(U)) - a(U)^T B^(-1)a(U)`.

Therefore

`Q_k=(V+B^(-1)a(U))^T B (V+B^(-1)a(U))+R_k(U,Z)`,                     (3.4)

with

`R_k(U,Z)=F_k(U)-a(U)^T B^(-1)a(U)`
`          +2 U^T H_T Z+b_T(k)^T Z+c_k`.                              (3.5)

The crucial point is that the absence of `P-T` coupling prevents the pair shift from depending on `Z`, and the absence of a `T-T` term leaves (3.5) exactly in the scope of the completed partner theorem. The modified

`F'_k(U)=F_k(U)-a(U)^T B^(-1)a(U)`

is still arbitrary measurable. Hence by account02/B06,

`||p_{R_k}||_infinity <= M := e sqrt(pi)/sigma_T`.                    (3.6)

Now condition on `(U,Z)`. The original two coordinates in `P` remain independent and each retains density cap one; their translations in (3.4) are deterministic under this conditioning. Applying the physical-pair logarithmic envelope (1.2) and averaging gives, for every `r>0`,

`p_{Q_k}(t)`
` <= 2 sqrt(2)/r`
`    +D^(-1/2) E log_+(2 r^2/(kappa |t-R_k|))`.                       (3.7)

Apply Lemma 2.1 with `a=2r^2/kappa` and (3.6):

`p_{Q_k}(t)`
` <= 2 sqrt(2)/r + 4 M r^2/(kappa sqrt(D))`.                          (3.8)

For `A,B0>0`, the minimum of `A/r+B0 r^2` is

`3*2^(-2/3) A^(2/3) B0^(1/3)`.

Here `A=2 sqrt(2)=2^(3/2)` and `B0=4M/(kappa sqrt(D))`, so all powers of two cancel to give exactly

`p_{Q_k}(t) <= 6 M^(1/3) kappa^(-1/3) D^(-1/6)`.                     (3.9)

Substitute `M=e sqrt(pi)/sigma_T` to obtain (3.2). The estimate is uniform in `k`; average over `X_K`. QED.

### Definite companion branch

If `B` is definite rather than indefinite, the same original-coordinate pair can be paid directly: the full ellipse coarea integral with joint cap one gives

`||p_Q||_infinity <= pi/sqrt(|det B|)`,                                (3.10)

uniformly under arbitrary affine shifts and arbitrary remaining variables. Thus only indefinite `B` needs the remote cross smoother above.

## 4. Weighted original-coordinate curvature-cover corollary

The theorem can be stated directly as a weighted structural certificate inside a larger two-bank block.

Let original coordinates be split into a left bank `I`, a right bank `J`, and an outside bank `K`. After conditioning `K`, write the right self-block as `G=A_JJ` and the left-right cross block as `H=A_IJ`. Let

`sigma=s_2(H)>0`.

Choose a physical pair `P subset J`, `|P|=2`, and a set `T subset J\P` such that

`G_PT=0`, `G_TT=0`.                                                     (4.1)

Let `S=J\(P union T)`; condition the original coordinates in `S`. Put

`B=G_PP`, `D=|det B|`, `kappa=sigma_min(B)`.

Define the cross-energy paid by deleting the pair and conditioning the rest by

`eta(P,T)=||H_{J\T}||_F^2 = sum_{j in J\T} ||H e_j||_2^2`.            (4.2)

Because

`H H^T = H_T H_T^T + H_{J\T} H_{J\T}^T`,

Weyl gives

`s_2(H_T)^2`
` >= s_2(H)^2-||H_{J\T}||_op^2`
` >= sigma^2-eta(P,T)`.                                                (4.3)

Hence if, for some `0<=theta<1`,

`eta(P,T) <= theta^2 sigma^2`,                                         (4.4)

then

`s_2(H_T)>=sqrt(1-theta^2) sigma`.                                    (4.5)

If `B` is indefinite and invertible, Theorem 3.1 gives

`boxed( ||p_Q||_infinity`
` <= 6 (e sqrt(pi))^(1/3)`
`    (1-theta^2)^(-1/6)`
`    D^(-1/6) kappa^(-1/3) sigma^(-1/3) ).`                           (4.6)

If `B` is definite, use (3.10) instead.

This is a genuine weighted replacement for the invalid operation `integral sup_fiber`: the only conditioning cost is the **actual cross-column energy removed**, and the surviving hyperbolic singularity is averaged against the genuine partner-controlled product-law remainder density.

The exact structural condition (4.1) has a transparent graph interpretation: after conditioning `S`, the unconditioned right-side curvature consists of one isolated physical pair `P` plus a curvature-free remote bank `T`. The result is not perturbative in `G_PP`; both zero diagonals are allowed when `B=[[0,b],[b,0]]`.

## 5. Relation to the account02/B06 counterexample

The partner's exact family

`R_epsilon=2 epsilon^(-2) U1U2+2(U1V2+U2V1)+2 epsilon^2 V1V2`

has a perfectly conditioned cross block but an unbounded output density; it has only two nonzero eigenvalues. In the present language the right bank consists entirely of the hyperbolic pair `P`, so there is no remote bank `T` and therefore `sigma_T=0`. Theorem 3.1 correctly does not apply.

Thus the new theorem pays precisely the missing ingredient absent from that falsifier: an additional **remote rank-two product smoother** survives after the problematic hyperbolic pair is isolated. This is why merely saying the opposite self-curvature is small is invalid, while retaining a quantitatively transverse remote product bank is sufficient.

## 6. Conditional end-to-end splice and what remains

A compact corrected proof skeleton for the current near-rank-two branch is now:

1. use the existing full-target reductions to reach a near-rank-two original-coordinate cross block;
2. if one entire opposite bank is quadratically null, apply account02/B06 directly;
3. more generally, if the opposite self-curvature admits a pair/remote decomposition `(P,T)` satisfying (4.1) and the removed cross-energy condition (4.4), then:
   * definite `B` is paid by the ellipse bound (3.10);
   * indefinite invertible `B` is paid by Theorem 3.1 and the partner remainder-density bound;
4. the only survivor of this mechanism is the genuinely entangled case in which every attempt to isolate one physical curvature pair either
   * destroys essentially all of the second cross singular direction,
   * leaves nonzero `P-T` or `T-T` curvature,
   * or leaves only singular physical curvature blocks.

This narrows the previous `QFORM-TWO-SIDED-CURVATURE-ABSORPTION-v1` debt to the quantitative structural implication

`QFORM-WEIGHTED-PAIR-ISOLATION-OR-ENTANGLED-CURVATURE-v1`:

> In the current strong near-rank-two survivor, prove that either a pair/remote certificate `(P,T)` satisfies (4.1),(4.4) with dimension-free `D,kappa,sigma`, or the failure of every such certificate forces a separately payable self-curvature packet / grouped product smoother / physical minor branch.

The theorem above proves the complete analytic side once such a certificate is present. What is still missing is the exhaustive structural production of that certificate, or a payment for its failure. No claim that the three-large-eigenvalue hypothesis alone already forces it is made.

## 7. Scope and integrity

* Full arbitrary-dimensional QFORM: **OPEN**.
* Valid counterexample to QFORM: **none supplied here**.
* New result: dimension-free supporting theorem (3.2) and weighted matrix corollary (4.6).
* Original-coordinate independence is preserved at every conditioning step.
* No Gaussian, moment, compact-support, log-concavity, connected-support, or diagonal-basis assumption is inserted.
* No post-rotation independence is used.
* No fiber supremum is integrated.
* The partner theorem is used at the actual inequality (3.6), not merely cited.
* Essential boundedness is proved in the stated branch; continuity is not proved.

Suggested next recipient: account03/B08, because its live `QFORM-GROUPED-CORE-WITH-FIBER-TAIL-v1` debt asks for an integrated product-law payment of a curved core while retaining a tail. The present theorem gives one exact payment when that tail can be organized as a remote rank-two cross smoother.
