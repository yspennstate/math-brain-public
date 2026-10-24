SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B20, 2026-09-24T10:13:33Z.
attacking: replace the current retained-tail endpoint by an unconditional one-scale spectral-window dichotomy: either the high-spectrum frame is diffuse enough for a full-law ridge payment, or the completed account04/B20 window-leverage lemma forces a literal physical star at a fixed universal scale.

# account03/B20 r51 — 1/25 spectral window: continuous ridge payment or a 1/200 physical star

Programme: `QFORM-DENSITY-3EIG-20260922`.

Status: **ESSENTIAL_STEP_APPLIED / NEW UNCONDITIONAL COMPILER / FULL QFORM OPEN / NOT PROVED / NOT DISPROVED**.

Execution: **WITHOUT_VERIFIED_BRAIN**. Repository retrieval/writeback is not native learned-memory receiver ingestion.

Regularity: the diffuse spectral-window branch below has a continuous `C_0` density. The scalar-pivot exit used on the concentrated branch gives an essentially bounded density in its stated source scope; continuity is not imported there. The surviving physical-star branch is structural only. Full-target continuity remains OPEN.

All coordinate sets are literal ORIGINAL-coordinate sets. Orthogonal operations below are deterministic coefficient-space spectral decompositions only; no rotated random coordinates are declared independent. No Gaussian, log-concave, moment, compact-support, connected-support, iid, arbitrary-joint coarea, conditional projection cap, worst-fibre, law-uniform pointwise oscillatory decay, or coefficient-tail deletion assumption is used.

## 1. Source-pinned frontier and completed inputs

The full target is: for every `n`, independent real `X_i` with probability densities `0<=f_i<=1`, and every real symmetric `A` with at least three eigenvalues of absolute value at least one, prove that `Q=X^T A X` has a density with universal finite `L^infinity` norm, or give a counterexample.

The freshest same-route structural endpoint read before this run is account01/B19 r56,

`yspennstate/math-open-problems@e5211d16c0bc2b4bce3cb6fef161d984b20d3029`,

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B19/20260924T095039Z-account01-B19-QFORM-auto11-r56/REPORT.md`.

It reduces an anchored robust-rank-two branch to a finite rank-12 (rank-11 on determinant collapse) carrier plus a genuine retained operator tail below `0.187623`, without deleting that tail. That is a strong local normal form but is not itself an endpoint theorem.

The analytic payment used here is the completed one-scale ridge theorem

`QFORM-RIDGE-DENSITY-v1`,

source:

`yspennstate/math-open-problems@9c1167db05c7b0f520f060796fde921ed769a4e7`,

`proofnet24/QFORM-density/interactive/20260922T151048Z-ridge-window/REPORT.md`.

For a literal physical cross block `B=A[I,J]`, set

`K_gamma=B B^T (gamma^2 I+B B^T)^(-1)`,

`theta_gamma=tr K_gamma`.

If, for `q=1`,

`max_i (K_gamma)_ii <= 1/2`, `theta_gamma>2`,

then the FULL ambient quadratic form has a continuous `C_0` density and

`||p_Q||_infinity <= sqrt(e)/(sqrt(2) gamma) * theta_gamma/(theta_gamma-2)`.

The same source proves the perturbative ridge-leverage inequality: if `B=B_0+F`, `||F||op<=eta`, and `S=range(B_0)` has physical projection diagonal at most `ell`, then

`(K_gamma)_ii <= (sqrt(ell)+eta/gamma)^2`.

This is a deterministic coefficient perturbation estimate, not deletion of `X^T F X`.

The designated partner input actually applied below is account04/B20 r13,

`yspennstate/math-open-problems@d2560a041fd91c05d7fddf50f5b5414ecd2680a2`,

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B20/20260924T051424Z-account04-B20-QFORM-r13/REPORT.md`,

theorem `QFORM-WINDOW-LEVERAGE-TO-PHYSICAL-STAR-v1`:
for symmetric `C`, spectral projection `P_tau=1_{|lambda(C)|>=tau}`, and an ORIGINAL coordinate `i` with `q_i=(P_tau)_ii`,

`max{|C_ii|, ||C_{-i,i}||_2} >= tau sqrt(q_i/2)`.

The same source invokes the completed all-sign scalar-pivot theorem: under `s_3(A)>=1`, a physical diagonal pivot `|A_ii|>=a` pays the full law by

`||p_Q||_infinity <= C_* / sqrt(a)`,

`C_* = 1 + 44*10^(15/2)`.

Continuity is not claimed from that scalar-pivot input.

## 2. Main theorem

### Theorem — `QFORM-SPECTRAL25-RIDGE-OR-STAR200-v1`

Assume the full target hypotheses and let

`rho:=1/25`,

`P:=1_{|A|>=rho}`

be the spectral projection of `A` onto all eigenspaces whose eigenvalues have absolute value at least `rho`.

Then one of the following holds.

1. **Diffuse-window continuous payment.** If

   `max_i P_ii <=1/32`,

   then the FULL ambient law has a continuous density vanishing at infinity and

   `boxed: ||p_Q||_infinity <1398.`

2. **Concentrated-window physical packet.** If

   `max_i P_ii >1/32`,

   then there is an ORIGINAL coordinate `i` satisfying

   `boxed: max{|A_ii|, ||A_{-i,i}||_2} >1/200.`

   If the diagonal alternative occurs, the completed scalar-pivot theorem pays the full law by

   `boxed: ||p_Q||_infinity < 1.968*10^10.`

Consequently every target state surviving both completed payments satisfies simultaneously

`boxed: |A_jj| <=1/200 for every original coordinate j,`

and, for at least one original coordinate `i`,

`boxed: ||A_{-i,i}||_2 >1/200.`

No assertion is made that this single physical star alone pays the full target.

## 3. Proof of the diffuse-window payment

Write the exact spectral decomposition

`A=A_H+E`,

where

`A_H=U Lambda_H U^T`

contains precisely the spectral subspace `P=UU^T` for `|lambda|>=rho`. Thus

`U^T U=I`, `||E||op<rho=1/25`,

and, in the diffuse branch,

`||u_i||_2^2=P_ii<=1/32`

for every physical row `u_i` of `U`.

Because the target has at least three eigenvalues of magnitude at least one, the invertible diagonal matrix `Lambda_H` has at least three singular values at least one.

### 3.1 MSS physical partition

Apply the two-part Marcus-Spielman-Srivastava frame partition to the rows of `U`. There is a literal ORIGINAL-coordinate partition

`[n]=I disjoint_union J`

such that both partial Gram matrices obey

`delta I <= U_I^T U_I, U_J^T U_J <= (25/32) I`,

where

`delta=7/32`.

No random variable has been rotated; only physical coordinates have been partitioned.

Let

`B_0=(A_H)[I,J]=U_I Lambda_H U_J^T`.

Since both restricted frames have minimum nonzero singular value at least `sqrt(delta)`, the approximation-number inequality gives

`s_3(B_0)>=delta*s_3(Lambda_H)>=delta=7/32`.

The actual cross block is

`B=A[I,J]=B_0+E[I,J]`.

Restriction does not increase operator norm, hence

`||E[I,J]||op<rho`.

Weyl therefore yields the strict lower bound

`s_3(B)>sigma:=delta-rho=7/32-1/25=143/800.`

### 3.2 Physical range leverage of the truncated block

Because `U_J^T U_J` is positive definite and `Lambda_H` is invertible on the selected spectral subspace,

`range(B_0)=range(U_I)`.

The orthogonal projection onto that range is

`Pi_0=U_I (U_I^T U_I)^(-1) U_I^T`.

Thus for every `i in I`,

`(Pi_0)_ii <= ||u_i||^2/delta <= (1/32)/(7/32)=1/7`.

So the unperturbed physical range has leverage at most `ell=1/7`.

### 3.3 Choose a ridge scale that tolerates the full 1/25 tail

Set

`gamma:=(7/10)sigma=1001/8000`.

Then

`rho/gamma = (1/25)/(1001/8000)=320/1001`.

The ridge-stability theorem gives

`max_i (K_gamma)_ii <= (1/sqrt(7)+320/1001)^2`.

This number is strictly below `1/2`. For an exact rational certificate, put

`a=320/1001`,

`y=5/14-a^2=510915/2004002>0`.

The desired inequality is equivalent to `2a/sqrt(7)<y`. Squaring is legitimate because both sides are positive, and

`y^2-(4/7)a^2
 =26508646025/4016024016004
 >0`.

Hence

`boxed: max_i (K_gamma)_ii<1/2.`

### 3.4 Effective ridge dimension is already above two

At least three singular values of the ACTUAL physical cross block `B` are strictly larger than `sigma`. Therefore

`theta_gamma
 =sum_k s_k(B)^2/(gamma^2+s_k(B)^2)
 >3 sigma^2/(gamma^2+sigma^2)`

`=3/(1+(7/10)^2)`

`=300/149`

`>2`.

Thus the ridge criterion applies with `q=1`.

The function `theta/(theta-2)` is decreasing for `theta>2`; using `theta>300/149` gives

`theta/(theta-2)<150`.

Consequently

`||p_Q||_infinity
 < sqrt(e)/(sqrt(2) gamma) *150`

`= sqrt(e)/sqrt(2) * (8000/1001)*150`

`=1397.588800158...`

`<1398`.

The ridge theorem simultaneously yields a continuous density vanishing at infinity. This proves branch 1.

## 4. Designated account04/B20 result applied at the actual complementary inequality

Assume now the diffuse gate fails. Then for some literal original coordinate `i`,

`q_i=P_ii>1/32`.

Apply account04/B20 r13 `QFORM-WINDOW-LEVERAGE-TO-PHYSICAL-STAR-v1` directly to

`C=A`, `tau=rho=1/25`, `q=q_i`.

It gives

`max{|A_ii|, ||A_{-i,i}||_2}
 >=rho sqrt(q_i/2)`

`> (1/25) sqrt((1/32)/2)`

`=1/200`.

This is the promised literal physical packet. It is an application at the ACTUAL target matrix, not a relabeling of a projected or rotated law.

If `|A_ii|>1/200`, invoke the completed all-sign scalar-pivot theorem at `a=1/200`:

`||p_Q||_infinity
 < C_* sqrt(200)`

`=(1+44*10^(15/2))*sqrt(200)`

`=19677398216.14...`

`<1.968*10^10`.

If that exit does not occur, then the same `i` obeys

`||A_{-i,i}||_2>1/200`.

Moreover, if ANY other physical diagonal exceeded `1/200`, the scalar-pivot theorem would pay there instead. Thus every survivor has all physical diagonals at most `1/200` in magnitude and at least one off-diagonal physical row star larger than `1/200`.

This proves branch 2 and the stated survivor normal form.

## 5. Relation to the freshest retained-tail frontier

The theorem above is unconditional under the bare target hypothesis; therefore it may be inserted BEFORE or AFTER the r49-r56 anchored robust-rank-two compiler without changing its logical validity.

In particular, on the fresh account01/B19 r56 survivor

`A_light=diag(q)+K_12+F`, `rank K_12<=12`, `||F||op<0.1875152587890625`

(or rank at most eleven with collapse-tail `<0.1876220703125`), every still-unpaid target state is now additionally constrained by the physical conclusion

`|A_jj|<=1/200 for all j`,

`max_i ||A_{-i,i}||_2>1/200`.

The retained nonseparable tail is NOT removed by this statement. The next proof must use the star together with the retained third spectral resource / latent carrier, or force one of the already-completed grouped-star, hub+square, physical-pair, physical-E3, D5, ridge/window, incident-volume or finite-core receivers.

## 6. Why this is stronger than the previous 1/64 spectral-window control

The earlier spectral-window corollary used cutoff `rho=1/64`, a fixed choice `gamma=sigma/sqrt(6)`, and gave a continuous diffuse payment below 64 under the same `P_ii<=1/32` leverage gate. Its concentrated complement only forces a physical coefficient packet at scale `1/512` through the partner window lemma.

The present calculation deliberately sacrifices the diffuse constant, raising the cutoff to `rho=1/25` and choosing `gamma=(7/10)(7/32-rho)`. The exact ridge-leverage certificate still remains below one half, while the complementary window-leverage packet improves to the simple universal scale `1/200`. This is useful because the current debt is structural rather than constant optimization: a stronger literal physical star is more valuable than a smaller already-finite density constant.

Nothing in this optimization changes the law class or treats low-spectrum coefficients as random noise: the entire `|lambda|<1/25` part remains inside the actual physical cross block and is handled only through the deterministic ridge-stability inequality.

## 7. First remaining implication

The first live closure edge after this run is

`QFORM-STAR200-WITH-SUBTARGET-TAIL/THIRDRESOURCE-ENDPOINT-v1`:

starting from a still-unpaid target state with

`max_j |A_jj|<=1/200`,

and a literal original-coordinate hub `i` with

`||A_{-i,i}||_2>1/200`,

combine that star with the freshest r56 retained rank-12/rank-11 carrier and tail `<0.187623`, or with the corresponding diffuse third spectral source in the nonanchored branch, to force a completed full-law receiver. The proof must retain all same-bank curvature, all outside couplings, all signs, the genuine nonzero tail, arbitrary fragmented/unbounded cap-one input laws, and every extra spectral mode.

A single star alone is NOT claimed to solve the target.

## 8. Status and corrections

The unrestricted QFORM conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**. Two independent end-to-end reviews would still be required for any eventual full candidate.

Consumed correction boundaries remain in force:

- no law-uniform pointwise quadratic-phase decay for arbitrary cap-one fragmented densities;
- no arbitrary-joint coarea shortcut;
- no positive conditional projection-density moment gate;
- no worst-fibre projected-density cap;
- no post-rotation independence;
- no one-good-minor extraction from aggregate volume;
- no generic fractional-small-ball-to-density upgrade;
- no deletion of a nonzero coefficient tail.

The only continuity statement newly proved here is on the diffuse ridge branch. The scalar-pivot branch supplies essential boundedness only in the cited source scope; the structural star survivor has no density conclusion by itself.
