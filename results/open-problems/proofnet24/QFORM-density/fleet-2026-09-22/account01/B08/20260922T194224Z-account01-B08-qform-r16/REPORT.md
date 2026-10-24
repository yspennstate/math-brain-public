SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B08, 2026-09-22T19:42:24Z.
attacking: basis-invariant diffuse spectral-window closure and the first exhaustive ridge/local alternative.

# account01/B08 — improved basis-invariant diffuse spectral-window theorem

**Run:** `20260922T194224Z-account01-B08-qform-r16`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Diffuse eigenvector case  
**Status:** `ESSENTIAL_STEP_APPLIED / SUPPORTING_THEOREM_PROVED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Target and conditional end-to-end argument

The full target is: for every dimension, every product law with independent real coordinate densities bounded by one, and every real symmetric `A` with at least three eigenvalues of modulus at least one, prove a universal density bound for `Q=X^T A X`; continuity is an additional desired conclusion.

A compact sufficient route is now:

1. If a basis-invariant high-spectral projection of `A` is diffuse, partition its physical frame into two balanced original-coordinate banks by MSS.
2. The high spectral piece then creates three uniformly large cross singular values.
3. The low spectral tail perturbs both the cross singular values and ridge leverage by a controlled amount.
4. Apply the completed one-scale ridge theorem before Fourier inversion.
5. The remaining full-target branch is therefore necessarily leverage-heavy in the **whole high spectral window**, not merely in a chosen triple of eigenvectors; it must be paid by physical pivots/pairs/grouped banks.

This run proves Step 1–4 under a strictly weaker leverage hypothesis than the existing `1/32` theorem at the same spectral threshold `1/64`, and records why delocalization of a chosen eigen-triple is not an invariant structural condition when eigenvalues repeat.

## 2. Dependencies actually used

### 2.1 Ridge-window theorem

Canonical source: `yspennstate/math-open-problems@9c1167db05c7b0f520f060796fde921ed769a4e7`, path `proofnet24/QFORM-density/interactive/20260922T151048Z-ridge-window/REPORT.md`.

For an original-coordinate cross block `B`, `gamma>0`, and

`K_gamma=BB^T(gamma^2 I+BB^T)^(-1)`, `theta_gamma=tr K_gamma`,

if for some `q in [1,2]`

`max_i (K_gamma)_ii <= q/2`, `theta_gamma>2q`,

then the full quadratic form, retaining arbitrary self blocks, outside coordinates and couplings, has a continuous `C_0` density and

`||p_Q||_infinity <= sqrt(e)/(sqrt(2q) gamma) * theta_gamma/(theta_gamma-2q)`.

The same source proves the perturbative ridge-leverage estimate: if `B=B0+F`, `||F||<=eta`, and `S=range(B0)`, then

`(K_gamma)_ii <= [sqrt((P_S)_ii)+eta/gamma]^2`.

### 2.2 MSS two-part frame partition

For a Parseval frame with row norms squared at most `epsilon`, the two-part Marcus–Spielman–Srivastava partition gives a physical cut `I|J` for which both partial Gram matrices are bounded below by

`delta(epsilon)=1/2-epsilon-sqrt(2 epsilon)`.

The exact source and statement are already pinned in the ridge-window proof above.

### 2.3 Assigned partner result actually applied

Assigned partner: account02/B08, theorem `QFORM-SCALAR-ORTHOGONAL-CROSSBLOCK-v1`, canonical source
`yspennstate/math-open-problems@caf8de3c65ae54b8ec8df9bfe977a76bf0a6ab99`, path `proofnet24/QFORM-density/fleet-2026-09-22/account02/B08/B08-20260922T173452Z-r15/REPORT.md`.

If a square physical cross block satisfies `BB^T=sigma^2 I_m`, `m>4`, then

`||p_Q||_infinity <= [e sqrt(2)/(4 sigma)] m/(m-4)`, continuously and with arbitrary self/outside terms retained.

Section 5 below applies this theorem literally to the full-spectrum Sylvester-Hadamard stress family.

## 3. New theorem: `QFORM-SPECTRAL-WINDOW-LEVERAGE-1OVER22-v1`

Let `A` be any real symmetric matrix with at least three eigenvalues of modulus at least one. Let

`P = 1_{|A| >= 1/64}`

be the **entire** spectral projection onto all eigenspaces with `|lambda|>=1/64`. Suppose

`max_i P_ii <= 1/22`.                                             (3.1)

Then for every independent real `X_i` with densities `0<=f_i<=1`, the law of `Q=X^T A X` has a continuous density vanishing at infinity and

`||p_Q||_infinity <= C_22`,                                      (3.2)

where one may take

`C_22 = 15625 sqrt(e) / [117 sqrt(6) (5/11-1/sqrt(11)-1/64)] < 655.`

No moment, support, centering, sign, rank, or post-rotation independence assumption is used. Eigenvalues below `1/64` may be arbitrarily numerous, nonzero, and of either sign.

This strictly enlarges the previously proved spectral-window branch `max_i P_ii<=1/32` at the **same** threshold `1/64` (at the expense of a larger constant).

### Proof

Write

`A=A_H+E`, `A_H=U Lambda_H U^T`,

where the columns of `U` span `P`. Then

`||E||<eta:=1/64`, `||u_i||^2=P_ii<=epsilon:=1/22`,

and `Lambda_H` contains at least three singular values at least one.

Apply the two-part MSS partition to the rows `u_i`. There is a physical cut `I|J` such that

`M_I=U_I^T U_I >= delta I`, `M_J=U_J^T U_J >= delta I`,

with

`delta = 1/2-1/22-sqrt(1/11) = 5/11-1/sqrt(11).`                 (3.3)

The high-piece cross block

`B0=(A_H)[I,J]=U_I Lambda_H U_J^T`

therefore has at least three singular values at least `delta`: its nonzero singular values equal those of

`M_I^(1/2) Lambda_H M_J^(1/2)`,

and both Gram square roots have minimum singular value at least `sqrt(delta)`.

For the true cross block

`B=A[I,J]=B0+F`, `F=E[I,J]`, `||F||<=eta`,

Weyl/min-max gives

`s_3(B) >= sigma := delta-eta.`                                 (3.4)

Because `M_I,M_J` are positive definite and `Lambda_H` is invertible on `P`,

`range(B0)=range(U_I)`.

Hence the diagonal of the projection onto `range(B0)` satisfies

`(P_range(B0))_ii = u_i^T M_I^(-1)u_i <= epsilon/delta.`       (3.5)

Choose

`q=27/25`, `gamma=(3/5)sigma.`                                  (3.6)

The three singular values in (3.4) imply

`theta_gamma >= 3/(1+(3/5)^2)=75/34.`                          (3.7)

Since

`75/34 - 2q = 75/34-54/25 = 39/850 >0`,                        (3.8)

the effective-dimension condition will hold once the ridge-leverage condition is checked.

By the perturbative ridge-leverage theorem,

`max_i(K_gamma)_ii <= [sqrt(epsilon/delta)+eta/gamma]^2.`       (3.9)

We verify this is strictly below `q/2=27/50` without decimals. First

`delta>153/1000`,

because `1/sqrt(11)<3317/11000`; after squaring, this is the exact integer inequality

`11000^2 < 11*3317^2`, whose right minus left side is `27379`.

Therefore

`sqrt(epsilon/delta)<sqrt(500/1683)<5451/10000`,               (3.10)

where the final comparison follows by squaring; the positive integer gap is

`5451^2*1683 - 500*10000^2 = 7653883`.

Also

`sigma>153/1000-1/64=1099/8000`,

so

`gamma>(3/5)(1099/8000)=3297/40000`

and hence

`eta/gamma < 625/3297.`                                        (3.11)

Combining (3.10)-(3.11),

`[sqrt(epsilon/delta)+eta/gamma]^2
 < (5451/10000+625/3297)^2
 = 27/50 - 288569529191/1087020900000000
 < 27/50=q/2.`                                                  (3.12)

Thus all hypotheses of the one-scale ridge theorem hold. It gives a continuous `C_0` density and

`||p_Q||_infinity
 <= sqrt(e)/(sqrt(2q) gamma) * theta_gamma/(theta_gamma-2q)
 <= sqrt(e)/(sqrt(54/25) gamma) * (75/34)/(75/34-54/25).`

The ratio in the last factor is exactly

`(75/34)/(39/850)=625/13`.

Using `gamma=(3/5)sigma` therefore yields

`||p_Q||_infinity
 <= 15625 sqrt(e)/(117 sqrt(6) sigma)
 = C_22 <655.`

This proves (3.2). QED.

## 4. Basis-invariance correction: chosen eigenvector diffuseness alone is insufficient

A statement of the diffuse branch in terms of **existence of three diffuse large eigenvectors** is not structurally meaningful when eigenvalues repeat.

Take `A=I_n`, with `n` admitting three flat orthonormal Walsh/Hadamard vectors. Because the eigenvalue `+1` has multiplicity `n`, those three flat vectors are legitimate eigenvectors and their selected-frame row leverage is exactly `3/n ->0`. Nevertheless every physical cross block of `A` is identically zero and the full high spectral projection is `P=I`, so `P_ii=1`.

Thus:

`QFORM-SELECTED-EIGENVECTOR-DIFFUSENESS-NONINVARIANT-v1`:

> Existence of a delocalized chosen triple of large eigenvectors does **not** imply any nontrivial physical cross block, any global ridge cut, or high-window diffuseness. A valid diffuse reduction must be formulated in a basis-invariant way (for example by the full spectral-window projector), and its complement must retain local/grouped-coordinate mechanisms.

This is an intermediate structural correction, not a counterexample to QFORM. For `A=I_n`, the diagonal theorem already gives the universal `pi` bound.

## 5. Assigned partner applied on the complementary diffuse-looking stress family

The partner account02/B08 report supplies the normalized Sylvester-Hadamard family

`A_k=H^(tensor k)`, `n=2^k>=16`,

whose spectrum lies entirely in `{+1,-1}`. It contains an explicit three-dimensional eigenframe with maximum selected-row leverage tending to zero, but its **full** high spectral projector is again `P=I`, so theorem (3.2) correctly does not classify it as window-diffuse.

Across the first tensor-bit cut, however,

`B=2^(-1/2) A_(k-1)`,

so

`BB^T=(1/2)I_m`, `m=n/2`.

Applying the assigned partner theorem with `sigma=1/sqrt(2)` gives the actual target-level inequality

`||p_{X^T A_k X}||_infinity
 <= e n/[2(n-8)] <= e,   n>=16,`                               (5.1)

and the density is continuous `C_0`.

This comparison is useful: `I_n` and the Hadamard family can both admit arbitrarily diffuse **chosen** three-eigenvector frames, while one has zero cross geometry and the other has an excellent global scalar-orthogonal ridge cut. The full spectral-window projector distinguishes neither (both equal `I`); the correct full-target reduction therefore has to combine invariant window diffuseness with local diagonal/pair/grouped and global ridge mechanisms rather than reason from a selected basis.

## 6. What changed and what remains

### Proved this run

1. `QFORM-SPECTRAL-WINDOW-LEVERAGE-1OVER22-v1`: at spectral threshold `1/64`, high-window leverage `<=1/22` suffices for a continuous universal density bound `<655`, improving the existing `1/32` leverage branch at the same threshold.
2. `QFORM-SELECTED-EIGENVECTOR-DIFFUSENESS-NONINVARIANT-v1`: existence of a diffuse chosen eigen-triple does not imply diffuse physical geometry; `A=I_n` is an exact source-valid counterexample to that intermediate idea.
3. Literal application of the assigned partner account02/B08 scalar-orthogonal-crossblock theorem gives (5.1) on a genuine full-spectrum Hadamard target family.

### First unpaid implication

`QFORM-HIGH-WINDOW-HEAVY-TO-LOCAL-OR-RIDGE-v1`:

Under the bare three-large-eigenvalue hypothesis, if the basis-invariant high-window projection at `|lambda|>=1/64` has a coordinate with leverage `>1/22`, prove that the resulting leverage-heavy physical geometry forces, with universal constants, one of the already paid original-coordinate mechanisms:

- an invertible indefinite pair/full-matrix pair certificate;
- a scalar pivot plus ridge certificate;
- a grouped-coordinate bank/projection-Plancherel certificate; or
- a global ridge cut.

The reduction must survive repeated eigenvalues, the singleton-plus-two-banks family, the no-fixed-good-minor corrections, and arbitrary additional spectrum. This is the true complement of the new diffuse theorem. Full QFORM remains OPEN.

## 7. Corrections and scope

Consumed corrections include the false pointwise van-der-Corput route, the fiber-sup dimension loss, no post-rotation independence, the false arbitrary-joint rank-three coarea lemma, the false positive conditional projection-moment gate, the local-cross-rank-three counterexample, and the fixed-local-principal-only failure. None is used here.

No Gaussianity, log-concavity, compact support, moments, connected support, or diagonal-basis assumption is introduced. Continuity is genuinely proved on theorem (3.2) and the partner application (5.1), but remains open for the unrestricted full target.
