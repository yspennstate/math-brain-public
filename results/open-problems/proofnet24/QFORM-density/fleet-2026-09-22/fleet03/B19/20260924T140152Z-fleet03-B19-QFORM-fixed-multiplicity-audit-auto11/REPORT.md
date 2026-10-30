SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B19, 2026-09-24T14:01:52Z.
attacking: independent end-to-end audit and universal-proof assembly of the later-owner fixed-multiplicity line; verify the new nine-eigenvalue replacement, sharpen its constant by applying completed peer work, and isolate the first eight-eigenvalue obstruction without weakening any target quantifier.

# fleet03/B19 fixed-multiplicity audit and nine-direction proof assembly

Run: `20260924T140152Z-fleet03-B19-QFORM-fixed-multiplicity-audit-auto11`  
Later owner objective obeyed: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Execution status: `WITHOUT_VERIFIED_BRAIN`.

## Source pins

Fresh owner-control repository at invocation:

- `yspennstate/math-research-brain@04766c985e54f75e3e0bbac8b14256cd804e6394`.
- `AGENTS.md` / `CURRENT_OBJECTIVE.md` make the fixed-multiplicity audit/reduction objective later than, and therefore controlling over, the older unstructured three-eigenvalue slot prompt.

Pinned baseline manuscript:

- repository `yspennstate/math-open-problems`;
- baseline source commit `7c0d6e60946b19423e6400a12d34b473cf0591e2`;
- path `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/manuscript.tex`;
- git blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`;
- SHA-256 `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`;
- source length 790 lines.

Fresh `master` immediately before this report write had advanced through concurrent immutable worker additions to `b4dad2b0db2d305ccdda8b4a6a40f4220f86132f`; the pinned manuscript blob remained unchanged.

New theorem sources actually used:

1. Complete nine-direction replacement/reconstruction:
   `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/improvements/fleet01/B11/20260924T131124Z-fleet01-B11-fixedmult-r12/IMPROVEMENT.md`, blob `b25ece64d7409b420d826c87449b32f51f444f38` as read on master `90b1bcb91cb5076cc2dba6724ae5bb699a511008`.
2. Separate complete nine-direction review:
   `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/improvements/fleet01/B16/20260924T124038Z-r11/REPORT.md`, blob `76bb639e30738749993c49de0048e66f5cfc917d`.
3. Designated partner `fleet04/B19` audit/constant ledger:
   `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/audits/fleet04/B19/20260924T132050Z-fleet04-B19-fixedmult-audit-r1/REPORT.md`, blob `0fe4b467a1465ac9ab977bc396f4936c0c0ab338`, first observed at immutable repository ref `1b5f19105fa1c69fe37f97a4ecf7b588a24c931d`.
4. Sharper graph/quarter-power source transfer from `fleet03/B18`:
   `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/audits/fleet03/B18/20260924T131003Z-fleet03-B18-fixedmult-audit-r11b/REPORT.md`, blob `20dd27763df9f9ecae65645b42ba9b2aa90e72fa`.
5. Eight-direction terminal collar:
   `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/improvements/fleet03/B04/20260924T124904Z-fleet03-B04-fixedmult-audit-r2/REPORT.md`, blob `851e0ae9c78a4d9a49f60a1cc5f0026b734579e6`.

## Verdict

### Baseline theorem

**PASS** on the complete pinned 17-eigenvalue manuscript. I reread the complete 790-line source in this invocation and rederived every specialized step used by the theorem. No fatal mathematical defect was found.

The baseline theorem is valid with all stated quantifiers:

\[
s_{17}(A)\ge s>0
\quad\Longrightarrow\quad
\|p_{X^TAX+b^TX+c}\|_{\infty,\mathrm{ess}}
\le 10^4 K^2/s,
\]

for arbitrary dimension, arbitrary real symmetric `A`, arbitrary signature and remaining spectrum, arbitrary affine terms, and independent real coordinates with densities only assumed bounded by `K`.

The known local wording repair remains nonfatal: in the product-projection proof, after rows with `b_i=0` are dropped, the entropy sum should be written

\[
\sum_{b_i>0}(1-b_i)\le d,
\]

rather than equality if the displayed sum is read only over retained rows. The proof uses only the upper bound, so no theorem or constant changes.

### Lowered threshold

**PASS in this B19 independent reconstruction of the complete nine-eigenvalue theorem.** Combining the grouped product-Fourier compiler with the baseline spectral-to-volume/pivot framework yields a complete theorem at multiplicity nine. With the sharper peer constants assembled below, this run proves the same theorem with the improved bound

\[
\boxed{
 s_9(A)\ge s>0
 \quad\Longrightarrow\quad
 \|p_{X^TAX+b^TX+c}\|_{\infty,\mathrm{ess}}
 <3810\,\frac{K^2}{s}.
}
\tag{A}
\]

No Gaussianity, moments, iid law, compact or connected support, log-concavity, exact-rank assumption, leverage assumption, diagonal basis assumption, or independence after rotation is introduced.

The unrestricted three-large-eigenvalue conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**. Multiplicity eight also remains **OPEN**. Global continuity is **not** proved by (A); continuity is available on the integrable-Fourier no-pivot branch only.

## Complete baseline audit ledger

I independently checked the following source ranges and their downstream uses:

- lines 1--90: statement, scaling architecture, exact scope and 9/17 threshold bookkeeping — PASS;
- 91--160: Gaussian regularization, Plancherel/inversion, power envelope and Riesz half-potential — PASS;
- 161--220: nonsymmetric singular-value perturbation, principal Schur spectral count and strict diagonal dominance — PASS;
- 221--282: geometric rank-one Brascamp--Lieb heat flow and product projection density — PASS, with the nonfatal `<=d` wording repair above;
- 283--373: scalar Fourier powers, original-coordinate decoupling, graph/determinant crossing bound — PASS;
- 374--403: Cauchy--Binet crossing volumes, order-five density and order-three half-potential endpoints — PASS;
- 404--482: scalar square profile, definite pair and hyperbolic pair estimates — PASS;
- 483--525: quarter-power concentration/logarithmic potential — PASS;
- 526--630: disjoint-minor sampling, nonsymmetric interpolation completion, global rank `<=3r`, restricted rank `<=r`, spectral-to-volume contradiction and random coordinate cut — PASS;
- 631--725: no-pivot consequences, singular kernel integrals, pivot truncated half-potential and nine-direction half-potential — PASS;
- 726--790: final 17-direction case split, rescaling and limitations — PASS.

The repository's newly landed reproducibility package was also read. `SOURCE_MANIFEST.json` matches the pinned blob/hash. `checks.json` reports PASS for 534 exact interpolation seeds, 18 exact volume comparisons, exact diagonal-dominance slack `297/2800`, 240 floating Schur-threshold diagnostics and 30 graph-weight diagnostics. These are diagnostics, not proof certificates.

## Independent reconstruction of the nine-direction analytic engine

The new ingredient is a grouped product-Fourier compiler. Let `H,I,J` be disjoint original-coordinate banks; let `W` be a `k`-dimensional orthogonal projection of `X_H` whose density is bounded by `M_H`; and write

\[
Q=F(X_H)+2\langle W,MX'+\beta\rangle+R(X'),
\qquad X'=(X_I,X_J).
\]

Assume `M_J` has row rank `k`; let `S` be the product of its nonzero singular values. Orthogonally remove the row space already represented by `M_J` from the remaining physical crossing rows and call the residual row matrix `C`. For order `ell`, let

\[
Z_\ell=\sum_{|T|=\ell}\det(C_TC_T^T),
\qquad
w_T=\frac{\det(C_TC_T^T)}{Z_\ell},
\qquad
\alpha_i=\sum_{T\ni i}w_T.
\]

If all `alpha_i<=1/2` and `d=k+ell`, then

\[
|\phi_Q(t)|
\le
\min\{1,K_{k,\ell}|t|^{-d/2}\},
\tag{1}
\]

where

\[
K_{k,\ell}=
M_H^{1/2}\pi^{d/2}2^{\ell/4}e^{(k+2\ell)/4}
\left(\frac{\ell^\ell}{\ell!}\right)^{1/4}
S^{-1/2}Z_\ell^{-1/4}.
\tag{2}
\]

I checked the dependence-sensitive steps rather than importing the peer verdict:

1. Push `e^{itF}dP_H` to `W`. Its complex density `a_t` has `|a_t|<=p_W`, hence `||a_t||_2^2<=M_H`. Plancherel after `xi=2t(l+beta)` gives exactly `M_H(pi/|t|)^k`.
2. For the light-bank complex pushforward, condition on the *same* original `X_I=x`; translation of the output preserves `L^2`. Mollify, expand the square with only an independent copy of `X_J`, and put `D=X_J-X'_J`. Pure `I` phases cancel, pure `J` phases have modulus one, and averaging the original independent `X_i`, `i in I`, gives the required scalar Fourier factors. Jensen is used in the Hilbert space `L^2`; no conditional density cap is invented.
3. For each weighted `ell`-subset `T`, the map
   `D -> (M_JD,(<c_i,D>)_{i in T})`
   has Gram determinant exactly `S^2 det(C_TC_T^T)`. The baseline product-projection theorem therefore gives the required joint-density Jacobian bound without rotated-coordinate independence.
4. Because `alpha_i<=1/2`, the scalar Fourier-power estimate applies at exponent `1/alpha_i>=2`, with scaled integral `pi sqrt(2e alpha_i)/|t|`.
5. If a random `ell`-subset with law `w` is uniformly ordered, entropy subadditivity gives exactly
   \[
   H(w)+\sum_i\alpha_i\log\alpha_i
   \le \ell\log\ell-\log(\ell!).
   \]
   This cancels the subset/marginal factors and yields (1)--(2).

The promotion tree then gives the marginal-free receivers

\[
\boxed{
\|p_Q\|_\infty
\le C_3 E_3(M)^{-1/6},
\quad
C_3=3\sqrt2\,e(9/2)^{1/6}=14.818337662843\ldots,
}
\tag{3}
\]

with a continuous `C_0` density on that branch, and

\[
\boxed{
\sup_a\mathbb E|Q-a|^{-1/2}
\le C_2 E_2(M)^{-1/8},
\quad
C_2=8\sqrt e\,2^{-1/8}=12.095072570796\ldots .
}
\tag{4}
\]

Equation (4) is deliberately only a half-potential theorem; it is not promoted to an `L^infinity` density bound.

## End-to-end proof of (A)

Normalize `K=s=1`; use the manuscript parameters

\[
\eta=1/100,
\qquad
\kappa=1/80^2.
\]

### No pivot

If `A` has no `eta`-pivot and `s_9(A)>=1`, the audited spectral-to-volume proposition with `k=3` gives

\[
V_3(A)\ge\kappa^3.
\]

A fair physical coordinate cut yields a literal cross block with

\[
E_3(M)\ge4^{-3}\kappa^3,
\quad
E_3(M)^{-1/6}\le160.
\]

By (3),

\[
\|p_Q\|_\infty
\le160C_3
=2370.93402605488\ldots<2400.
\tag{5}
\]

### Scalar pivot

Suppose `|A_hh|>=eta`. Completing the square in the literal original coordinate `X_h` gives the scalar domination profile

\[
p_Q(z)\le |A_{hh}|^{-1/2}\,
\mathbb E|R-z|^{-1/2},
\tag{6}
\]

where the Schur remainder has at least eight unit-scale eigenvalues.

If that Schur remainder has no `eta`-pivot, it in particular has `s_5>=1`; the audited spectral-to-volume proposition at `k=2`, followed by the fair cut and (4), gives

\[
\sup_a\mathbb E|R-a|^{-1/2}
\le C_2\sqrt{160}
=152.99191115498\ldots<153.
\tag{7}
\]

If instead the Schur remainder has a pivot, only two surviving unit directions are needed for the pivot half-potential argument. The sharper completed fleet03/B18 quarter-power transfer gives logarithmic potential `<10`. Therefore the worst inner scalar-pivot truncated half-potential is

\[
H(R)<10(8+3\cdot10)=380,
\]

while the definite and indefinite pair-pivot subcases are smaller. Adding the contribution from `|R-a|>1` gives

\[
\sup_a\mathbb E|R-a|^{-1/2}<381.
\tag{8}
\]

Combining (6)--(8) and `eta^{-1/2}=10`,

\[
\boxed{\|p_Q\|_\infty<3810.}
\tag{9}
\]

### Pair pivots

A definite physical pair is paid directly by the two-dimensional area formula, at `<32` in the normalized variables. An indefinite pair loses only two spectral directions; under `s_9>=1` its Schur remainder still has a unit spectral direction, so the audited hyperbolic/logarithmic-potential argument applies. Even the baseline constant is `<251`, far below (9); the sharper logarithmic constant makes it smaller still.

Thus (9) dominates all normalized branches. For general `K,s`, put `Y=KX` and

\[
\widetilde Q
=Y^T(A/s)Y+(K/s)b^TY+(K^2/s)c,
\qquad
Q=(s/K^2)\widetilde Q.
\]

The coordinates of `Y` have density cap one and `s_9(A/s)>=1`; scalar density scaling proves (A).

## Actual application of designated partner fleet04/B19

The partner result was applied to the same live scalar-pivot inequality, not merely cited. The fleet04/B19 constant ledger proves, for the exact manuscript pivot-half-potential hypotheses,

\[
H(R)<\frac{54049}{125}=432.392<433.
\]

Hence in the `s_9` scalar-pivot branch, whenever the eight-direction Schur remainder itself has an `eta`-pivot,

\[
\sup_a\mathbb E|R-a|^{-1/2}
<1+\frac{54049}{125}
=\frac{54174}{125}=433.392,
\]

and the outer scalar square profile gives the concrete full-law bound

\[
\boxed{
\|p_Q\|_\infty
<10\frac{54174}{125}
=4333.92<4334.
}
\tag{10}
\]

This is a genuine application in the partner theorem's proved scope. Equation (10) independently pays that live subbranch. The sharper fleet03/B18 logarithmic potential is then what reduces the assembled global constant further from `<4334` to `<3810` in (A).

## First unresolved threshold: multiplicity eight

The pivot branches already close with eight large spectral directions. The only surviving multiplicity-eight state is no-pivot. The completed terminal theorem proves the dichotomy

\[
V_3(A)\ge\kappa^3
\]

(which is paid by (3)), or else simultaneously

\[
V_2(A)\ge\kappa^2,
\quad
\Omega_1(A)\ge c_*^2\kappa^2,
\quad
\Xi_2(A)\ge\frac{\delta_*^2}{2}\kappa^2,
\tag{11}
\]

with

\[
c_*=1-3\sqrt2/80,
\qquad
\delta_*=0.8543351401911337\ldots .
\]

A three-color extraction from (11) already forces a literal physical `E_2` packet and the full-law half-potential `<53.338`; that does not by itself imply bounded density. Rank-two indefinite smoothing is genuinely borderline and can have logarithmic density singularities. Therefore the first essential missing implication is now precisely

`QFORM-EIGHT-OVERLAP1-TWOSIDED-COLLAR-RECEIVER-v2`:

> From the quantitative no-pivot packet (11), prove a dimension-free `L^infinity` density endpoint while retaining the overlap/two-sided original-product provenance, arbitrary same-bank curvature, arbitrary affine terms, all signs, and allowing the common physical diagonals to be zero; or force an already-paid `E_3`/physical pivot receiver.

Collapsing (11) merely to `E_2`, a projected bounded joint density, or a conditional density cap is insufficient and is explicitly disallowed by the live correction record.

## Correction and scope discipline

Before this proof assembly I reread the live correction inbox and did not use any refuted premise. In particular:

- no pointwise rough quadratic van-der-Corput decay is used;
- no post-rotation independence is used;
- no arbitrary-joint coarea theorem is used;
- no conditional projection density cap is inferred from an unconditional one;
- no fiber-supremum estimate with dimension loss is used;
- no Monte Carlo histogram or interval-extremality claim is used.

The grouped Fourier proof rotates only deterministic coefficient spaces/Jacobians and duplicates only literal independent original-coordinate banks.

## Status

- Pinned 17-direction theorem: **PASS** in this invocation.
- Complete nine-direction replacement theorem: **PASS** in this independent B19 reconstruction.
- Assembled same-scope nine-direction constant: **`<3810 K^2/s`**.
- Designated partner fleet04/B19 applied to an actual scalar-pivot inequality: **yes**, yielding the independent subbranch bound `<4334 K^2/s` before the sharper B18 transfer.
- Multiplicity eight: **OPEN**, reduced to (11) and the collar receiver above.
- Full three-eigenvalue target: **OPEN / NOT PROVED / NOT DISPROVED**.
- Full-target continuity: **OPEN**; the no-pivot `E_3` branch is `C_0`, but pivot branches here establish essential boundedness only.
- Native learned-memory/brain ingestion: **WITHOUT_VERIFIED_BRAIN**; repository reads/writes are not treated as verified native memory retrieval.
- Model self-report: `GPT-5.6 Sol`; configured reasoning effort/provider thinking counters: `UNKNOWN / NOT_EXPOSED`.
