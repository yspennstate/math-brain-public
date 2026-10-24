# account03/B14 independent fixed-multiplicity audit — rough laws, versions, Tonelli

Run: `20260924T123325Z-account03-B14-QFORM-fixed-multiplicity-audit-r11`  
Current objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Execution status: `WITHOUT_VERIFIED_BRAIN`

## Source pin

- Repository: `yspennstate/math-open-problems`, branch `master`.
- Canonical manuscript: `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/manuscript.tex`.
- Owner-pinned initial source commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`.
- Source SHA-256 supplied by owner: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`.
- Git blob read in full: `183ccd294763214e6a707e8d4749ff9a8cf7006d`.
- Fresh master observed during review: `8e34bb60a6ae3a3f59eaaf080d262ca1d4f5f664`; the manuscript there still has blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`.

I read the complete 790-line manuscript rather than relying on prior verdicts. The role-specific lens was rough densities, measurable representatives, Tonelli, and conditional laws, but the audit below is end-to-end.

## Verdict

**Mathematical verdict on the pinned 17-eigenvalue theorem: PASS.** I found no fatal mathematical gap in the claim

\[
s_{17}(A)\ge s>0,\qquad \|f_i\|_{\infty,\mathrm{ess}}\le K
\quad\Longrightarrow\quad
\|p_{X^TAX+b^TX+c}\|_{\infty,\mathrm{ess}}\le 10^4K^2/s,
\]

for arbitrary dimension, signs, remaining spectrum, affine terms, and independent rough coordinate laws.

This is one independent worker review, not a peer-review certificate and not a solution of the unrestricted three-eigenvalue conjecture.

**GAP-PRESENTATION, theorem unaffected:** the statement only assumes the density cap almost everywhere, while several inverse-branch/coarea formulas later write pointwise density values. A single global bounded-Borel-representative convention removes the ambiguity. I prove that compiler below.

**GAP-PACKAGING, non-mathematical:** on fresh master, `SOURCE_MANIFEST.json`, `proof_map.csv`, `verify.py`, and `checks.json` advertised by the root README/AUDIT were not present in the manuscript root. Direct reads of the first two returned 404 and code search did not locate the advertised checker. Therefore I did not count the advertised finite tests as rerun evidence. The mathematical proof is self-contained in `manuscript.tex`.

**Threshold status:** the manuscript proves 17. I found no valid deduction of 16 from the baseline proof. A fresh account03/B08 supporting theorem sharply describes the terminal `r=4` chamber under `s_16>=1`, but explicitly does not close the 16-eigenvalue theorem; I therefore leave 16 as GAP / not proved.

## End-to-end audit table

| Source lines | Item | Status | Independent check |
|---|---|---|---|
| 41–80 | theorem, normalization, architecture | PASS | Quantifiers preserve arbitrary rough independent laws, affine terms and remaining spectrum. Scaling `Y=KX`, `A/s`, then output scaling gives exactly `K^2/s`. |
| 81–160 | Fourier identities, inversion, Riesz half-potential | PASS | Gaussian regularization is integrable; approximate identity is in `L^2`; inversion is obtained from convolved laws rather than assumed. Both Tonelli uses in the Riesz proof are on nonnegative majorants. The `3/4` envelope gives weighted integral `12 sqrt(u)`. |
| 161–220 | singular values, Schur count, diagonal dominance | PASS | Nonsymmetric singular-value perturbation is used in the correct direction. For singular ambient `A`, the moving threshold `t-|eps|` is harmless after passing to the ordered absolute eigenvalue: the `q`-th modulus is at least `t-|eps|` and converges to at least `t`. |
| 221–282 | geometric BL and projection density | PASS | Heat-flow sign is correct; the frame map is a contraction. Compact-support approximation supplies Gaussian domination at large time, and monotone truncation reaches arbitrary integrable inputs. Projection uses only deterministic rotation in the integral, not probabilistic independence after rotation. |
| 283–400 | scalar Fourier powers, decoupling, determinant | PASS | `|hat f|^(2m)` is integrable because it is bounded by `|hat f|^2`; the continuous inversion version inherits the essential density bound at zero. Decoupling uses original-coordinate independent copies and bounded-modulus Fubini. Graph BL weights, regularizer and fourth-root exponent give the displayed determinant `-1/8`. |
| 401–526 | square, definite pair, hyperbolic pair, quarter concentration | PASS after representative convention | All changes of variables can be formulated as nonnegative test-function domination. Hyperbolic tails use an original coordinate with monotone derivative comparable to magnitude; the cap-one/mass-one bathtub step is valid. Quarter concentration keeps product provenance through an original-coordinate cross cut. |
| 527–651 | sampled interpolation, completion, spectral-to-volume, random cut | PASS | Bordered determinant identity and multiplicity inequality are correct. `R-P` is supported in rows `T` or columns `S`, giving global rank `<=3r`; on `L x L`, `R=P`, giving restricted rank `<=r`; `D` vanishes on the seed. The terminal diagonal-dominance slack is positive. |
| 652–720 | singular kernels and pivot half-potentials | PASS | Every singular integral is nonnegative, so Tonelli is legitimate. Scalar-pivot conditioning produces measure domination, not false conditional independence. Definite and indefinite pair bounds are uniform over induced affine shifts. |
| 721–760 | nine-direction half potential and main theorem | PASS | Pivot/no-pivot alternatives exhaust cases. Schur counts lose only pivot dimension. Outside the truncated region the half-kernel costs at most one. Main normalized branch bounds are all below `10^4`. |
| 761–790 | threshold accounting, scope, continuity | PASS | The manuscript correctly distinguishes order-five density inversion from order-three half-potential control and makes no full three-eigenvalue or global continuity claim. |

No substantive source line remains UNCHECKED in this review. The missing supplementary files remain unverified packaging claims, not unchecked manuscript mathematics.

## B14 rough-law compiler

### Lemma 1 — bounded Borel density representatives

If a probability law has a Lebesgue density `f` satisfying `0<=f<=K` almost everywhere, then it has a Borel density representative `g` satisfying `0<=g<=K` **everywhere** and `g=f` almost everywhere.

Proof. Any Lebesgue-measurable function has a Borel representative equal to it almost everywhere. Replace that representative by `min(K,max(0,g))`. The clipping changes it only on a null set because the original cap holds almost everywhere; hence the represented probability law and integral remain unchanged. QED.

Apply this once to every coordinate marginal at the beginning of the proof. It justifies every later pointwise cap, including values appearing on inverse branches or parametrized level curves. No support, smoothness, moment, or connectedness assumption is introduced.

### Lemma 2 — integrated conditional domination

Let `nu` be a positive finite measure on an environment space. For each environment `y`, let `mu_y` be a measurable probability/subprobability kernel on `R`. Let `k(y,z)>=0` be jointly Borel, with `+infinity` allowed. Suppose that for `nu`-almost every `y` and every nonnegative Borel test function `h`,

\[
\int h(z)\,\mu_y(dz)\le \int h(z) k(y,z)\,dz.
\tag{CD}
\]

Then the mixture

\[
\mu(B)=\int \mu_y(B)\,\nu(dy)
\]

is dominated by `K(z) dz`, where

\[
K(z)=\int k(y,z)\,\nu(dy).
\]

In particular, if `K(z)<=C` for almost every `z`, the mixture has a density with essential supremum at most `C`.

Proof. Integrate (CD) in `y`. Both sides are nonnegative; Tonelli gives

\[
\int h\,d\mu
\le \int\!\int h(z)k(y,z)\,dz\,\nu(dy)
=\int h(z)K(z)\,dz.
\]

Testing indicators gives the measure domination. No choice of a conditional-density version and no common exceptional output slice is required. QED.

### Application to the manuscript

For an original-coordinate scalar pivot, after conditioning on the remaining coordinates, the completed-square center and critical value are Borel polynomials/rational affine functions of the environment. Lemma `square`, used through test functions, gives

\[
k(y,z)=|a|^{-1/2}|z-R(y)|^{-1/2}
\]

after dropping the favorable one-sided indicator. Lemma 2 averages this exactly into the profile inequality. The later half-potential estimate bounds the resulting `K(z)`.

For a definite two-coordinate pivot, the same conditioning gives an environment-dependent translation of a fixed definite quadratic part. The deterministic two-dimensional change of variables gives the constant conditional dominator

\[
k(y,z)=\pi/\sqrt{|\det B|}.
\]

For an indefinite pair, the critical value `v(y)` is a Borel quadratic polynomial (the Schur remainder plus affine/constant terms), and the conditional dominator is the extended Borel function

\[
k(y,z)=|\det B|^{-1/2}
\left(6+\log_+\frac{16\sqrt{|\det B|}}{|z-v(y)|}\right),
\]

with value `+infinity` on the critical graph. Lemma 2 legitimizes averaging without selecting pointwise conditional densities on a common exceptional set. Quarter-power concentration of the Schur remainder supplies atomlessness/logarithmic integrability exactly where the main proof invokes it.

This proves that the pivot branches tolerate arbitrary translations, arbitrarily distant fragments and unbounded supports with **no moment bound**. All environment dependence appears only through Borel affine/quadratic shifts; no conditional density cap or rotated-coordinate independence is asserted.

## Exact arithmetic recheck

With `eta=1/100`, `kappa=1/80^2`, and `L0=4+4 log 16`, I independently recomputed:

- scalar-pivot truncated half-potential bound before rounding: `10(20+12 log 16)=532.7106466687737...`;
- hence the same proof actually gives the 17-eigenvalue constant
  `10[10(20+12 log 16)+1] = 2010+1200 log 16 = 5337.106466687737...`, although the manuscript safely states `10000`;
- no-pivot main branch: `800 e = 2174.625462767236...`;
- definite-pair main branch: `10 pi = 31.41592653589793...`;
- displayed indefinite-pair main expression is about `238.997315553...`, hence the manuscript's `<251` is safe;
- terminal manuscript diagonal-dominance slack: `371/400-23/28 = 297/2800 >0`.

The sharper `5337.106...` constant was already separately recorded by another worker; I record it here as an independent confirmation, not a novelty claim.

## Threshold-lowering check

The baseline interpolation argument itself genuinely stalls at 16 in the terminal `r=4` chamber: with global correction rank `12`, `s_16` forces only four large diagonal entries, which is compatible with restricted rank four; the manuscript needs five to contradict that restricted rank. Separately, order-four crossing gives the borderline Fourier exponent `|t|^{-1}`, so direct absolute inversion does not replace the order-five step.

I also read the fresh account03/B08 `QFORM-S16-TERMINAL-R4-SATURATION-v1` result on current master. It proves additional terminal structure — quantitative saturation of the global rank-12 correction, a uniformly invertible four-coordinate interpolation block, an exact rank-four normal form, and physical determinant chains — but explicitly leaves an inverse selected-seed determinant factor unpaid. I found no B14 rough-law/Tonelli step that removes that determinant loss. Therefore:

- 17-eigenvalue theorem: **PASS** under this audit;
- 16-eigenvalue theorem: **GAP / not proved** by the checked material;
- unrestricted three-eigenvalue theorem: **OPEN**.

## Packaging and reproducibility status

The root README/AUDIT advertise `SOURCE_MANIFEST.json`, `proof_map.csv`, `verify.py`, and `checks.json`. These files were absent at the fresh master refs inspected in this run. I therefore classify this as a packaging/reproducibility gap only. I did not infer correctness from the self-audit's finite-test counts. The source manuscript itself was read completely and audited directly.

Changed-file privacy review for this run is trivial: this audit contains only mathematical statements, repository hashes/paths, and nonsecret run identifiers. No credentials, account secrets, personal archives, external private data, or public release action are included.

## Next proof obligation

For threshold reduction, the mathematically unpaid point is not rough-law localization: the bounded-Borel representative and conditional-Tonelli compiler above close that interface. The next hard obligation is to exploit the saturated terminal `s_16` rank-four structure while **aggregating the sampled seed determinant before inversion**, or to prove a direct endpoint receiver that avoids the borderline order-four `|t|^{-1}` absolute-Fourier loss. Any claimed `17 -> 16` theorem must keep arbitrary affine terms and arbitrary cap-bounded product laws.
