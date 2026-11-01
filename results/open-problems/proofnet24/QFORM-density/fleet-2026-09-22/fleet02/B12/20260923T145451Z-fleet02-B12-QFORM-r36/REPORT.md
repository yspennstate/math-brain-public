SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B12, 2026-09-23T14:54:51Z.
attacking: a six-mode spectral-square carrier theorem that closes the rank-two self-block regime by an ORIGINAL-coordinate physical pair, while retaining arbitrary extra spectrum and paying a dense tail only through final-matrix inequalities.

# fleet02/B12 r36 — six-mode carrier closure and dense-tail stability

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Additional eigenvalue control  
Status: **PROVED SUPPORTING THEOREM / FULL QFORM OPEN**  
Continuity: **not claimed for the theorem as a whole**; the D5 exit is continuous, while the physical-core/pair exits used here establish essential boundedness.

## 1. First unpaid implication and what changes

The newest designated partner, fleet03/B12 r35,

`yspennstate/math-open-problems@03e610ce80aca57585c3b997f5d194b94443df1b`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B12/20260923T144737Z-qform-eigenvalue-r35/REPORT.md`

proved the spectral-square spill inequality. For an ORIGINAL-coordinate set `H`, with

`C=A[H,H]`, `B=A[H,H^c]`, `0<=G<=A^2`, `lambda_k(G[H,H])>=g^2`,

if `c=s_{r+1}(C)<g`, then

` s_{k-r}(B) >= sqrt(g^2-c^2). `                                  (1.1)

Its leverage-free closure spends two self-block directions (`r=2`) and therefore asks for `k>=7` so that five cross singular directions survive for D5. The first unpaid implication attacked here is whether one can recover the missing sixth carrier mode without assuming cross leverage.

**Answer: yes.** If the self block is neither genuinely rank-three nor sufficiently close to rank one, then its approximate rank-two part forces a quantitatively invertible ORIGINAL-coordinate physical pair. That pair is already a paid receiver. This gives a six-mode carrier theorem.

The remaining full-target gap is still structural: the owner hypothesis gives only three global eigenvalues of modulus at least one, not six spectral-square carrier modes on a bounded physical set. No claim below closes that gap.

## 2. Approximate rank-two self blocks force a physical pair

Let `C=C^T` be an `m x m` matrix, `m>=2`, and let

`s1(C)>=s2(C)>=s3(C)>=...`

be its singular values. Put

`N = binom(m,2)`.

### Lemma 2.1 — rank-two Pluecker extraction with operator-norm tail

Assume

`s2(C)>=b`, `s3(C)<a`,                                          (2.1)

where `b>0`. Then some ORIGINAL-coordinate pair `I={i,j}` obeys

`sigma_min(C[I,I]) >= b/N-a`.                                  (2.2)

In particular, if `a<b/N`, this pair is invertible.

### Proof

Let `lambda_1,lambda_2` be the two eigenvalues of `C` of largest absolute value and `u,v` corresponding orthonormal eigenvectors. Write

`C_2=lambda_1 uu^T+lambda_2 vv^T`, `E=C-C_2`.

Then

`||E||op=s3(C)<a`.                                             (2.3)

The Pluecker identity for two orthonormal vectors is

`sum_{i<j}(u_i v_j-u_j v_i)^2=1`.                             (2.4)

Hence for some pair `I={i,j}`,

`w_I^2:=(u_i v_j-u_j v_i)^2 >= 1/N`.                          (2.5)

For the `2 x 2` principal compression `K=C_2[I,I]`, direct expansion gives

`det K=lambda_1 lambda_2 w_I^2`.                               (2.6)

Also `||K||op<=||C_2||op=s1(C)`. Therefore

`sigma_min(K)=|det K|/sigma_max(K)`
`            >= s1(C)s2(C)/(N s1(C))`
`            >= b/N`.                                         (2.7)

The principal compression of `E` has operator norm at most `||E||op<a`. Weyl now gives

`sigma_min(C[I,I])>=sigma_min(K)-||E[I,I]||op>b/N-a`.          (2.8)

This proves the lemma. QED.

This argument is sign-free: the extracted pair can be definite or indefinite. No rotated random variables are introduced.

## 3. Both signatures of the extracted pair are paid

Put

`kappa=b/N-a>0`.                                               (3.1)

For the pair found in Lemma 2.1, all singular values have size at least `kappa`, hence

`D:=|det C[I,I]|>=kappa^2`.                                   (3.2)

### Definite pair

Condition on every ORIGINAL coordinate outside `I`. The remaining two variables are still independent with densities at most one, and all exterior couplings become affine terms. Completing the square gives a translated definite quadratic form `y^TBy` with `B=C[I,I]`. Under `z=|B|^{1/2}y`, the two-dimensional density is at most `D^{-1/2}`. Polar coarea for `|z|^2` gives

`||p_Q||inf <= pi/sqrt(D) <= pi/kappa`.                        (3.3)

No support or moment assumption is used.

### Indefinite pair

Use the completed arbitrary-rank physical-pair theorem

`yspennstate/math-open-problems@742ac943440e41925fe09db9a8c02a96cbd83dbc`

`proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/FULL_MATRIX_PAIR_EXTENSION.md`.

If the full final matrix satisfies `s3(A)>=s>0`, that theorem gives

`||p_Q||inf <= 3*400^(1/3)*(D^2*kappa*s)^(-1/6)`.              (3.4)

Using (3.2),

`||p_Q||inf <= 3*400^(1/3)*kappa^(-5/6)*s^(-1/6)`.            (3.5)

All remaining eigenvalues and couplings are arbitrary in this receiver.

## 4. Six-mode spectral-square carrier theorem

Let `A=A^T` satisfy `s3(A)>=s>0`. Let `H` be an ORIGINAL-coordinate set of size `m>=6`, put

`C=A[H,H]`, `B=A[H,H^c]`, `N=binom(m,2)`,

and suppose there is a positive semidefinite certificate

`0<=G<=A^2`, `lambda_6(G[H,H])>=g^2`                         (4.1)

for some `g>0`.

Fix parameters

`0<a<b/N`, `0<b<g`, and put `kappa=b/N-a`.                    (4.2)

Let

`A_m=2sqrt(6 pi m)`, `C_5=5sqrt(2e)`, `C_pair=3*400^(1/3)`.   (4.3)

### Theorem 4.1 — `QFORM-SIX-MODE-SPECTRAL-SQUARE-CARRIER-v1`

Under (4.1)-(4.2), for every independent cap-one product source and arbitrary affine terms,

`||p_Q||inf <= max {`
`    A_m/a,`
`    pi/kappa,`
`    C_pair*kappa^(-5/6)*s^(-1/6),`
`    C_5/sqrt(g^2-b^2)`
`}.`                                                           (4.4)

Every additional eigenvalue of `A`, of either sign and any magnitude, is retained in the ACTUAL final matrix.

### Proof

There are three exhaustive regimes.

**(i) Physical rank-three self block.** If `s3(C)>=a`, the completed finite-dimensional physical receiver used in fleet03/B12 r35 gives

`||p_Q||inf <= A_m/a`.                                        (4.5)

It is applied after conditioning only outside the original set `H`.

**(ii) Nearly rank-one self block.** Suppose `s3(C)<a` and `s2(C)<b`. Apply the partner spill theorem (1.1) with `k=6,r=1`:

`s5(B) >= sqrt(g^2-s2(C)^2) > sqrt(g^2-b^2)`.                 (4.6)

Now consume the required pinned newest-Claude result at

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/FOURIER_ROUTE_REPORT.md`.

Its completed D5 theorem has no row-marginal gate and states for the ACTUAL original-coordinate cross block `B`

`||p_Q||inf <= 5sqrt(2e) e5(B^TB)^(-1/10)`.                  (4.7)

Since `e5(B^TB)>=prod_{j=1}^5 s_j(B)^2>=s5(B)^10`, (4.6)-(4.7) give the real inequality

`||p_Q||inf <= 5sqrt(2e)/sqrt(g^2-b^2)`.                     (4.8)

This is an actual use of the required e5f71d79... result, not a citation-only dependency.

**(iii) Approximate rank-two self block.** The only remaining case has `s3(C)<a` and `s2(C)>=b`. Lemma 2.1 yields an original-coordinate pair with `sigma_min>=kappa`. If it is definite, use (3.3); if indefinite, use (3.5). This gives the middle two terms in (4.4).

The cases are exhaustive, proving (4.4). QED.

### Canonical one-parameter specialization

Take

`b=g/2`, `a=g/(4N)`, so `kappa=g/(4N)`.                       (4.9)

Then

`||p_Q||inf <= max {`
`  8N sqrt(6 pi m)/g,`
`  4 pi N/g,`
`  3*400^(1/3)*(4N/g)^(5/6)*s^(-1/6),`
`  10sqrt(2e)/(sqrt(3) g)`
`}.`                                                           (4.10)

This is not optimized; its point is the finite six-mode closure with no cross-range leverage condition. Fleet03/B12 r35 required seven modes for its leverage-free `r=2 -> D5` split.

## 5. Arbitrary dense tails are paid only at matrix level

Theorem 4.1 is already a theorem about the ACTUAL final matrix. It never writes a small matrix tail `T` as a small random variable `X^T T X`.

For explicit perturbative use, let

`A=A_*+T`, `T=T^T`, `||T||op<=delta`.                          (5.1)

Every fixed original-coordinate principal or cross block changes by operator norm at most `delta`, so each receiver certificate has the safe matrix-level erosion

`s_j(A[H,H]) >= s_j(A_*[H,H])-delta`,
`s_j(A[H,H^c]) >= s_j(A_*[H,H^c])-delta`,                     (5.2)

and similarly for a physical pair. If `s3(A_*)>=s+delta`, then `s3(A)>=s`.

No statement stronger than (5.2) is needed or used. In particular, no bound of the form `|X^T T X|<=o(1)` is asserted; such a law-uniform bound is false for unbounded cap-one sources.

There is also a useful carrier stability identity that does not depend on `||A_*||`. If for every `x` supported on `H`

`||A_*x|| >= g_*||x||`,                                       (5.3)

then from the triangle inequality

`||Ax|| >= (g_*-delta)||x||`.                                 (5.4)

Equivalently,

`(A^2)[H,H] >= (g_*-delta)^2 I_H`.                            (5.5)

Thus with `G=A^2`, condition (4.1) holds with `g=g_*-delta` whenever `|H|=6` and `delta<g_*`. This is a genuinely dense full-rank tail statement and remains valid even if `A_*` has arbitrarily large norm elsewhere.

## 6. Exact stress family: rank-two self + rank-four cross + arbitrary spectrum + dense tail

This family shows why six rather than seven modes is a real improvement.

Take six original coordinates `H`, four coordinates `J`, and any number of spectator coordinates `K`. Set

`C_0=diag(2,-2,0,0,0,0)`,                                    (6.1)

and let the `6 x 4` cross block be

`B_0 = 2 [ 0_{2 x 4} ; I_4 ]`.                               (6.2)

On `H union J`, define

`A_core=[[C_0,B_0],[B_0^T,0_4]]`.                             (6.3)

On the spectators put an **arbitrary real symmetric matrix** `Theta`, with arbitrary dimension, signs, multiplicities and eigenvalue magnitudes, and set

`A_*(Theta)=A_core direct_sum Theta`.                          (6.4)

Finally add **any** symmetric globally dense tail

`A=A_*(Theta)+T`, `||T||op<=1/64`.                            (6.5)

The ten core eigenvalues before `T` are all of modulus `2`: the first two are `2,-2`, and the remaining eight come from four `[[0,2],[2,0]]` blocks. Therefore, independently of `Theta`,

`s3(A)>=2-1/64=127/64>1`.                                    (6.6)

So every final matrix is in the exact owner target class.

For every vector `x` supported on `H`,

`||A_*(Theta)x||^2 = ||C_0x||^2+||B_0^T x||^2=4||x||^2`.      (6.7)

Hence (5.5) gives

`(A^2)[H,H] >= (127/64)^2 I_6`.                               (6.8)

Thus Theorem 4.1 has a six-mode carrier with `G=A^2`, `g=127/64`. This carrier uses **exactly** two self-block modes and four cross modes before the dense tail. The baseline cross block has rank four, so the no-marginal D5 route does not have five baseline cross directions; the partner's previous seven-mode `r=2 -> five cross directions` closure is unavailable on this six-coordinate carrier.

At the same time the explicit physical pair `{1,2}` is especially well conditioned. Its baseline block is `diag(2,-2)`. Under (6.5), Weyl gives

`kappa>=127/64`, and its signature stays indefinite.           (6.9)

Together with (6.6), the full-matrix physical-pair theorem gives

`||p_Q||inf <= 3*400^(1/3)/(127/64)`
`             = 11.1391188620...`.                            (6.10)

This bound is uniform over the entire arbitrary spectator matrix `Theta` and every dense `T` of norm at most `1/64`. The spectator spectrum can contain arbitrarily many eigenvalues tending independently to either sign infinity. The dense tail can couple all coordinates; it is never treated as an independent convolution term.

The family also explains the role of the new middle branch: a rank-four cross block plus a robust rank-two physical self block is a natural six-mode carrier that does not need a fifth cross direction.

## 7. Scope, corrections, and remaining implication

This report uses only ORIGINAL-coordinate conditioning. It does not assume independence after diagonalizing `A`. It assumes no moments, bounded support, log-concavity, centering or identical laws. Small matrix norm is used only through singular-value/operator inequalities such as (5.2), (5.4), and (5.5).

Consumed live corrections include the refutations of law-uniform pointwise quadratic-phase decay, arbitrary-joint coarea, worst conditional-density moments, universal good-minor/cross-rank reductions, and post-rotation independence. None is used as a premise here.

The full conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**. The exact next bridge is now narrower:

> from only three global eigenvalues of modulus at least one, force either a bounded six-mode spectral-square carrier, or route the failure of such a carrier into an already-paid diffuse-volume, grouped-bank, hub/ridge, physical-pair, rank-two-half-Riesz, or scalar-Schur exit.

The theorem above reduces the leverage-free carrier threshold from seven modes to six, but it does not manufacture those six modes from the bare target hypothesis.

Independent end-to-end review: not supplied by this run.
Execution-memory status: `WITHOUT_VERIFIED_BRAIN`.
