# account01/B06 r50 — scalar-pivot / P2 weighted curved receiver

**Run:** `20260924T073602Z-account01-B06-QFORM-r50`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, programme revision `2026-09-22.5`, OWNER CONTROL `2026-09-22.15`  
**Assignment:** Curved fiber integration  
**Status:** NEW SUPPORTING ANALYTIC THEOREM + EXACT P1/P2 PLUCKER BRIDGE + DESIGNATED PARTNER APPLIED; full unrestricted QFORM remains OPEN; global continuity remains OPEN  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 0. Scope and source discipline

The target remains: for every `n`, independent real `X_i` with densities `0<=f_i<=1`, and every real symmetric `A` with at least three eigenvalues of absolute value at least one, prove that `Q=X^T A X` has an essentially bounded density by one universal finite constant, or give a valid counterexample. No moment, support, compactness, connected-support, Gaussian, log-concavity, iid, or diagonal-basis assumption is introduced. No input rotation is treated as preserving independence.

Fresh `math-research-brain` control was read before the substantive calculation. OWNER CONTROL remains revision `2026-09-22.15`, QFORM-only, and account01/B06 is not paused. The live corrections were refreshed; in particular this run does not use law-uniform pointwise van der Corput, arbitrary-joint coarea, a worst conditional fiber cap, a largest-minor inference, or an unrestricted curved-fiber supremum.

Immediate predecessor: account01/B06 r49, canonical mathematics `yspennstate/math-open-problems@3b734087af35e1fa1c601fc92ddadf73e4d3a206`, path `proofnet24/QFORM-density/fleet-2026-09-22/account01/B06/20260924T063803Z-account01-B06-QFORM-r49/REPORT.md`. It paid the exact rank-one physical-pair endpoint by a parabolic product-fiber theorem but left the invertible-near-singular transition unpaid.

The designated partner result actually applied below is account02/B06 `QFORM-E2-HALFRIESZ-ROW-GATE-FREE-v1`, source `proofnet24/QFORM-density/fleet-2026-09-22/account02/B06/b06-20260923T192839Z-auto11/REPORT.md`. For a literal original-coordinate cross block `N` between two disjoint product banks, with `Z_2=e_2(N^T N)>0`, and arbitrary same-bank quadratic/affine curvature retained, it proves

`H_(1/2)(S):=sup_t E|S-t|^(-1/2) <= 8 e^(1/4) Z_2^(-1/8).`       (0.1)

This is fractional-potential credit, not by itself a density theorem. The new step below supplies the third smoothing resource as a literal original-coordinate scalar square.

For the live three-hub collar, the newest account02/B06 r15 result `QFORM-THREEHUB-S2-PAIR-OR-TRIPLE-COMPILER-v1` also gives an actual target-level exit

`sigma_2(K)>=1/64  =>  ||p_Q||_infinity<3149`                    (0.2)

for the literal physical three-hub block `K`. The r50 theorem is therefore aimed at the complementary near-rank-one hub branch rather than duplicating (0.2).

## 1. Literal scalar pivot and exact Schur geometry

Let `H={i,j,k}` be three literal original-coordinate hubs and `T` the disjoint literal tail bank. Write the corresponding blocks of the ambient symmetric matrix as `K=A[H,H]`, `M=A[H,T]`. Fix a literal hub coordinate `i` with `a:=K_ii !=0`, and put `J=H\{i}`. Reorder only the deterministic matrices so that `i` is first and `J` follows:

`K = [[a, c^T], [c, K_0]]`,
`M = [[m^T], [M_0]]`.

Define the exact scalar-pivot Schur blocks

`B := K_0 - c c^T/a`,                                           (1.1)
`N := M_0 - c m^T/a`.                                           (1.2)

Completing the square in the **literal original coordinate** `X_i` gives

`Q = a (X_i + L(X_J,X_T)/a)^2 + S(X_J,X_T)`,                    (1.3)

where `S` is the exact scalar Schur-complement quadratic polynomial on the still-independent original coordinates `J union T`. Its literal `J x T` cross block is exactly `N`. Every quadratic coefficient inside `J`, every quadratic coefficient inside `T`, and every affine term remains in `S`; nothing is dropped.

## 2. Scalar square peel + designated account02/B06 E2 theorem

### Theorem 2.1 — `QFORM-SCALARPIVOT-E2-WEIGHTED-v1`

Under (1.1)-(1.3), suppose

`Z_i := e_2(N^T N)=det(NN^T)>0`.                                 (2.1)

Then the full ambient quadratic form has an essentially bounded density and

`boxed: ||p_Q||_infinity <= 8 e^(1/4) |a|^(-1/2) Z_i^(-1/8).`    (2.2)

No continuity conclusion is asserted by this argument.

#### Proof

Condition on all original coordinates except `X_i`. For every fixed value of the complement, the translated scalar `X_i+b` still has density cap one. The pushforward under `u -> a u^2` has density bounded by `|a|^(-1/2)|y|^(-1/2)` on the appropriate half-line: the two roots contribute at most `2/[2 sqrt(|a||y|)]`. Therefore, for a.e. output level `q`, after averaging the complement,

`p_Q(q) <= |a|^(-1/2) E |q-S|^(-1/2) <= |a|^(-1/2) H_(1/2)(S).` (2.3)

Now apply the designated account02/B06 theorem (0.1) to the **actual literal cross block `N`** of `S`, using the disjoint original-coordinate banks `J` and `T`. It gives

`H_(1/2)(S) <= 8 e^(1/4) e_2(N^T N)^(-1/8).`                    (2.4)

Combining (2.3)-(2.4) proves (2.2). QED.

The scalar-square singularity `|q-S|^(-1/2)` is not replaced by its infinite fiber supremum. It is averaged against the complete product-derived half-Riesz control of the remaining two-bank curved geometry. The `E_2` packet is aggregated before any physical minor is inverted.

## 3. Exact P2 mixed-minor identity

For tail indices `p<q`, define the oriented three-by-three mixed minor

`S_i(p,q):=det A[H,{i,p,q}]`.                                    (3.1)

### Lemma 3.1 — `QFORM-SCALARPIVOT-P2-IDENTITY-v1`

For every `p<q`,

`boxed: S_i(p,q) = +/- a det N[:,{p,q}].`                        (3.2)

Consequently the complete fixed-pivot P2 energy

`Sigma_i := sum_(p<q) S_i(p,q)^2`                                (3.3)

satisfies

`boxed: Sigma_i = a^2 Z_i.`                                      (3.4)

#### Proof

The relevant mixed block, with the pivot column first, is

`[[ a,   m_p,     m_q   ], [ c, M_0[:,p], M_0[:,q] ]]`.

Subtract `(c/a)` times the first row from the two lower rows. The determinant is unchanged and the lower two entries in the two tail columns become precisely `N[:,p]` and `N[:,q]`. Expansion along the first column gives (3.2). Squaring and summing uses the two-row Cauchy-Binet identity `sum_(p<q) det N[:,{p,q}]^2 = det(NN^T)`. QED.

Combining Theorem 2.1 with (3.4) gives:

### Corollary 3.2 — `QFORM-SCALARPIVOT-P2-DENSITY-v1`

If `a!=0` and `Sigma_i>0`, then

`boxed: ||p_Q||_infinity <= 8 e^(1/4) |a|^(-1/4) Sigma_i^(-1/8) = 8 e^(1/4) (a^2 Sigma_i)^(-1/8).` (3.5)

Thus the homogeneous degree-eight currency `Gamma_i:=a^2 Sigma_i` is a direct product-preserving density certificate:

`Gamma_i>=gamma>0  =>  ||p_Q||_infinity <=8e^(1/4) gamma^(-1/8).` (3.6)

No individual mixed minor is required to be large.

## 4. Exact bridge to the P1 mixed-minor rows

Let `R:=adj(K) M`, so, up to the fixed orientation convention, row `h` of `R` is exactly the complete account02/B06 r13 one-tail/two-hub mixed-minor row `R_h`.

### Lemma 4.1 — `QFORM-P1-P2-PLUCKER-BRIDGE-v1`

With `J=H\{i}`,

`boxed: R_J = a adj(B) N,`                                       (4.1)
`boxed: R_i = det(B) m^T - c^T adj(B) N.`                        (4.2)

Moreover, for every `p<q`,

`boxed: R_j(p)R_k(q)-R_j(q)R_k(p) = +/- det(K) S_i(p,q).`        (4.3)

Hence, if

`W_i := sum_(p<q) [R_j(p)R_k(q)-R_j(q)R_k(p)]^2`,                (4.4)

then

`boxed: W_i = a^4 det(B)^2 Z_i = det(K)^2 Sigma_i.`              (4.5)

#### Proof

When `B` is invertible, the block inverse of `K` gives the lower two rows of `K^{-1}` as `[-B^{-1}c/a, B^{-1}]`. Using `det K=a det B`,

`(adj K M)_J = det(K) B^{-1}(M_0-cm^T/a) = a det(B)B^{-1}N = a adj(B)N`,

which is (4.1). The top row of the same block inverse gives (4.2). The identities extend to singular `B` as algebraic identities after clearing the fixed nonzero scalar denominator `a`.

Taking the determinant of columns `p,q` in (4.1),

`det R_J[:,{p,q}] = a^2 det(adj B) det N[:,{p,q}] = a^2 det(B) det N[:,{p,q}]`.

By (3.2) and `det K=a det B`, this is exactly `det(K) S_i(p,q)` up to orientation sign. Squaring and summing gives (4.5). QED.

### Corollary 4.2 — determinant-loss cancellation in the near-singular pair transition

Whenever `W_i>0`, Corollary 3.2 and (4.5) give

`boxed: ||p_Q||_infinity <= 8 e^(1/4) |det B|^(1/4) W_i^(-1/8).` (4.6)

This is the key transition formula. The older invertible-pair receivers deteriorate as a physical pair becomes singular because they pay a reciprocal `sigma_min(B)`. Formula (4.6) goes in the opposite direction: **provided the two P1 mixed-minor rows keep genuine area `W_i`, collapse of `det B` helps rather than hurts.**

Therefore the near-singular transition is not itself the obstruction. The true residual obstruction is geometric: the two relevant P1 rows must become nearly collinear (`W_i` small) at the same time that the hub block becomes near rank one.

## 5. Splice with the newest account02/B06 three-hub theorem

Let the literal three-hub block `K` have singular values `s_1>=s_2>=s_3`. The newest designated-partner r15 theorem pays the branch

`s_2>=1/64`                                                      (5.1)

by the target-level bound `||p_Q||_infinity<3149`. Hence r50 only needs the complementary branch `s_2<1/64`.

Let `lambda_1` be an eigenvalue with `|lambda_1|=s_1` and `r` a corresponding unit eigenvector. Some literal coordinate `i` has `r_i^2>=1/3`. Since the other eigenvalues have absolute value at most `s_2`,

`|K_ii| >= s_1 r_i^2 - s_2(1-r_i^2) >= s_1/3 - 2s_2/3.`         (5.2)

Thus either:

- `s_1<4s_2`, in which case `||K||_op=s_1<1/16`, so the entire physical three-hub block is small and a different cross/tail resource must carry the target spectrum; or
- `s_1>=4s_2`, in which case there is a literal coordinate `i` with

`boxed: |a|=|K_ii|>=s_1/6.`                                      (5.3)

For that strong physical pivot, r50 gives

`boxed: ||p_Q||_infinity <=8e^(1/4)(6/s_1)^(1/4) Sigma_i^(-1/8).` (5.4)

Equivalently, if the homogeneous packet `Gamma_i=a_i^2 Sigma_i` is quantitatively nonzero, (3.6) is already a universal target-level exit.

Combining (5.1)-(5.4), the former vague “near-singular physical pair” debt has been sharpened to `QFORM-RANKONE-HUB-LOW-P2-ROWCOLLINEAR-v1`: `sigma_2(K)<1/64`, and either the whole hub block is small, or a strong literal scalar pivot exists but its complete fixed-pivot P2 packet is small; equivalently, when `det K!=0`, the corresponding two P1 mixed-minor rows have small Pluecker area by (4.5). No small rank-two hub remainder was deleted.

## 6. Model family showing why aggregate P2 is the right currency

Take `m>=2`, orthonormal `u,v in R^m`, and `0<epsilon<=1/2`. Define

`K=diag(1,epsilon,epsilon)`,
`M=[0; epsilon^(-1)u^T; epsilon^(-1)v^T]`,

with zero tail self-block for simplicity. Pivot on the first hub. Then

`a=1`, `B=epsilon I_2`, `N=epsilon^(-1)[u^T;v^T]`,
`Z_i=epsilon^(-4)`, `Sigma_i=epsilon^(-4)`, `W_i=1`.

Corollary 3.2 gives

`boxed: ||p_Q||_infinity <= 8e^(1/4) epsilon^(1/2).`              (6.1)

By contrast, a naive conditional definite-pair bound on `B=epsilon I_2` is `pi/epsilon` and diverges. The ambient deterministic spectrum contains the scalar eigenvalue `1` and, on each of the two orthogonal hub-tail planes, the two eigenvalues of `[[epsilon,epsilon^(-1)],[epsilon^(-1),0]]`; for `epsilon<=1/2` this is inside the owner target. If `u,v` are diffuse, every individual physical cross coefficient can be small while the complete `Sigma_i` remains `epsilon^(-4)`. Thus (6.1) is genuinely aggregate, not a hidden largest-minor argument.

## 7. Remaining debt

This run does **not** prove the full QFORM conjecture and does **not** prove global continuity.

The new theorem pays any literal scalar pivot carrying a quantitative complete P2 mixed-minor bank, including a large part of the near-singular two-hub transition that caused reciprocal loss in earlier pair receivers. The first remaining local implication is now `QFORM-RANKONE-HUB-LOW-P2-ROWCOLLINEAR-v1`.

A correct next step should exploit simultaneously: three large eigenvalues globally; a near-rank-one (or entirely small) literal three-hub block; small fixed-pivot P2 energy at every strong hub pivot; and near-collinearity of the surviving P1 mixed-minor rows. It should route that structure to a grouped rank-two/rank-three original-product receiver or a finite heavy-tail-hub endpoint, while retaining the small nonzero hub remainder and arbitrary same-bank tail curvature.

**Full arbitrary-dimensional QFORM:** OPEN / NOT PROVED / NOT DISPROVED.  
**Global continuous density:** OPEN.  
**r50 conclusion:** essential boundedness in the stated scalar-pivot/P2 branches, with a dimension-free weighted product estimate and exact P1/P2 Pluecker identities.