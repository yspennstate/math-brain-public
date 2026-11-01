# fleet03/B18 audit addendum and literature-to-proof transfer

Run: `20260924T122639Z-fleet03-B18-fixed-multiplicity-audit-r11`
Current owner objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`
Execution status: `WITHOUT_VERIFIED_BRAIN`

## Source pin

Audited repository: `yspennstate/math-open-problems`, branch `master`.
Pinned baseline manuscript: `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/manuscript.tex`.
Owner baseline commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`.
Pinned git blob reread in full: `183ccd294763214e6a707e8d4749ff9a8cf7006d`.
Declared SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`.
Fresh master immediately before this write: `3eae7c165d9a64a1791bf1bbe7e67371c7337261`; the manuscript blob remained unchanged.

The current owner objective supersedes the older unstructured three-eigenvalue attack for this invocation. The unrestricted three-eigenvalue conjecture remains OPEN.

## Updated verdict

**Mathematical 17-eigenvalue theorem: PASS.** I retain the end-to-end PASS from my preceding B18 audit after rechecking the only new peer challenge that could have changed the verdict. The baseline theorem is

\[
s_{17}(A)\ge s>0\implies
\|p_{X^TAX+b^TX+c}\|_\infty\le 10^4 K^2/s
\]

for independent arbitrary real coordinate densities bounded by `K`, arbitrary real symmetric `A`, arbitrary signature and remaining spectrum, and arbitrary affine `b,c`.

The theorem is an essential-density statement. The manuscript does not prove global continuity in every branch, and it does not prove the full three-eigenvalue conjecture.

## Resolution of the disputed singular Schur step

A later fleet01/B18 audit labeled manuscript lines 205--207 (`lem:schur`, singular ambient case) a repairable GAP because the proof invokes the invertible case at the moving threshold `t-|epsilon|`. A fixed-delta replacement proof supplied there is valid, but after an independent adversarial recheck I agree with the later fleet02/B04 conclusion: **the original manuscript step is already valid**.

Let

`q = N_A(t)-k`.

If `q<=0` there is nothing to prove. For each admissible regularization `A_epsilon=A+epsilon I`, the written argument gives

\[
N_{S_\epsilon}(t-|\epsilon|)\ge q.
\]

Because each `S_epsilon` is symmetric, this is exactly

\[
s_q(S_\epsilon)\ge t-|\epsilon|,
\]

where `s_q` is the q-th ordered eigenvalue modulus / singular value. Since `S_epsilon -> S` in operator norm and ordered singular values are 1-Lipschitz under operator-norm perturbation,

\[
s_q(S)=\lim_{\epsilon\to0}s_q(S_\epsilon)\ge
\lim_{\epsilon\to0}(t-|\epsilon|)=t.
\]

Hence `N_S(t)>=q=N_A(t)-k`. No comparison between the rate of motion of an individual signed eigenvalue and `|epsilon|` is required. The count inequality itself is converted to a scalar ordered-singular-value inequality before taking the limit.

**Status:** PASS as written; the fleet01 fixed-delta argument is a useful clarification, not a necessary repair. Downstream scalar-pivot and indefinite-pair uses remain valid with no changed constant.

## Complete-proof status relative to my prior B18 audit

I reread the exact same 790-line blob in this invocation and rechecked the sensitive dependencies from the current owner objective. No new defect was found in:

- Fourier normalization, Gaussian regularization/inversion and the negative-half-moment identity;
- the heat-flow geometric Brascamp--Lieb proof and rough-law limiting steps;
- deterministic product-projection integration without rotated independence;
- two-copy/four-copy decoupling and the regularized determinant theorem;
- hyperbolic-pair rough-density domination and quarter-power concentration;
- ordered disjoint-minor sampling, nonsymmetric interpolation, support of `R-P`, global `rank R<=3r`, restricted `rank R[L,L]<=r`, and `D=0` on the seed;
- the `m=4k-3` spectral-to-volume contradiction and random physical cut;
- the distinction between truncated and full half potentials in the pivot/nine-direction chain;
- the final four-branch case split and `K^2/s` rescaling.

Thus no mathematical source range is newly UNCHECKED. The package-level supplementary files named by the README/objective (`SOURCE_MANIFEST.json`, `proof_map.csv`, `verify.py`, `checks.json`) were still absent from the root in the observed tree, so the advertised finite diagnostics remain **UNCHECKED / package GAP**, not a symbolic-proof gap.

## Primary-source literature check: new direct prior art

I verified an omitted source that should be cited in any publication version:

**Banks--Garza Vargas--Kulkarni--Srivastava, arXiv:2005.08930, Theorem 2.1, “Density of Quadratic Forms.”** Their theorem treats

\[
q(X,Y)=X^T ZY+X^T U+V^T Y+W
\]

for two genuinely independent random matrices/banks with independent entries having densities bounded by `K`; the proof uses Rudelson--Vershynin projection-density control and singular-value negative moments. This is much closer prior art than a generic projection theorem.

It does **not** subsume the fixed-multiplicity manuscript: the manuscript's physical-cut form is

\[
F(X_I)+2X_I^TMX_J+G(X_J),
\]

where the arbitrary same-bank quadratic phases `F` and `G` are essential and cannot be absorbed into deterministic affine `U,V,W`. Banks et al. therefore close the pure bilinear-affine subclass, not the unrestricted within-bank-curvature case needed here. No exact prior theorem matching all manuscript quantifiers was found in the primary sources checked; this is a scope statement, not a novelty/priority certificate.

The other source matches remain as in the prior B18 audit: Rudelson--Vershynin arXiv:1402.4492 exactly covers linear projections/sums of rough independent bounded-density inputs; Livshyts--Paouris--Pivovarov arXiv:1507.07949 sharpens product marginal density to `2^{d/2}`; Bennett--Carbery--Christ--Tao arXiv:math/0505065 is appropriate Brascamp--Lieb/heat-flow antecedent; Herry--Malicet--Poly arXiv:2303.09488 assumes a substantially narrower iid smooth-Gaussian-field-representable input class.

## Source-valid quantitative transfer: sharp scalar Fourier-power constant

Rudelson--Vershynin Theorem 1.2 gives the sharp bound `sqrt(2)` for every normalized linear combination of independent cap-one coordinates. Applying it to `m` independent copies of `X` and `m` independent copies of `X'` gives a strict improvement of the manuscript's scalar Fourier-power lemma.

For any one-dimensional probability density `f<=1` and any `p>=2`, put `m=floor(p/2)`, so `m>=p/4`. Since `|fhat|<=1`,

\[
\int |\widehat f(t)|^pdt
\le \int |\widehat f(t)|^{2m}dt.
\]

The right side is `2*pi` times the density at zero of

\[
S=\sum_{j=1}^m(X_j-X'_j).
\]

The normalized sum `S/sqrt(2m)` has density at most `sqrt(2)` by Rudelson--Vershynin, hence

\[
p_S(0)\le 1/\sqrt m,
\qquad
\boxed{\int |\widehat f(t)|^pdt\le \frac{4\pi}{\sqrt p}.}
\]

This replaces the manuscript's `2*pi*sqrt(2e)/sqrt(p)` by `4*pi/sqrt(p)`.

Running the manuscript's graph-frame/Brascamp--Lieb calculation unchanged with this source-valid bound allows the regularizer

\[
\alpha=8\pi^2e
\]

instead of `(2*pi*e)^2`, and yields

\[
\boxed{
|\phi_Z(t)|\le
\det\!\left(I+\frac{t^2}{2\pi^2e}M^TM\right)^{-1/8}.}
\]

Consequently, with the manuscript's crossing volume `Z_k(M)`, one may take

\[
u_k=\pi\sqrt{2e}\, Z_k(M)^{-1/(2k)}
\]

in the power envelope. The two concrete downstream bounds become

\[
\boxed{\|p_Z\|_\infty\le 5\sqrt{2e}\,Z_5(M)^{-1/10}}
\]

and

\[
\boxed{\sup_a\mathbb E|Z-a|^{-1/2}
\le 12(e/2)^{1/4} Z_3(M)^{-1/12}.}
\]

For the manuscript's no-pivot random-cut estimate `Z_k^{-1/(2k)}<=160`, this improves the order-five branch from `800e=2174.625...` to

\[
800\sqrt{2e}=1865.315...,
\]

and the order-three full half-potential bound from `12*sqrt(80e)=176.959...` to

\[
12(e/2)^{1/4}\sqrt{160}=163.892... .
\]

This transfer does **not** lower the multiplicity threshold 17: the current unconditional mechanism still needs order five for an integrable Fourier envelope and the worst sampled ratio index `r=4` still requires `m>=4r+1=17` in the rank/diagonal-dominance contradiction.

## Overall constant and threshold accounting

Independently checking the fleet01/B18 arithmetic, even without the sharper source transfer above the manuscript's own exact scalar-pivot estimate already improves the headline `10000` to

\[
\boxed{C_*=2010+1200\log 16=5337.106466687737\ldots}
\]

because the scalar-pivot branch dominates all other branches if one retains `10(20+12 log 16)` rather than rounding the nine-direction half potential to `600`. This is a valid quantitative corollary of the repaired/validated proof; it changes no hypothesis and no multiplicity.

I found no unconditional reduction below 17. The same proof skeleton has a sharp internal barrier at 17: order-five Fourier integrability permits a bad ratio seed `r=4`; global correction rank `3r=12` and restricted rank `r=4` force the contradiction only when `m-3r>=r+1`, i.e. `m>=17`. Lowering the theorem requires a genuine order-four endpoint/high-leverage receiver or a better rank/support interpolation, not a constant optimization.

## Review state

This report does not self-award a global peer-review certificate. It records one fleet03/B18 complete review plus the new dispute resolution and literature transfer. A separate fleet02/B04 full audit on the same source also reports PASS and independently gives the ordered-singular-value resolution of the Schur paragraph; consolidation of the global validation state belongs to the owner/keeper.

The unrestricted three-eigenvalue conjecture and unrestricted continuity remain OPEN.
