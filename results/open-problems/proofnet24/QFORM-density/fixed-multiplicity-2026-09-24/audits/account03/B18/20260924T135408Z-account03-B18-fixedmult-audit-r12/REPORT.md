# account03/B18 r12 — complete-audit continuation plus Beckner source transfer

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Run: `20260924T135408Z-account03-B18-fixedmult-audit-r12`  
Pinned manuscript source commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`  
Pinned manuscript blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`  
Pinned manuscript SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`

## Verdict

**PASS for the 17-eigenvalue bounded-density theorem in this B18 audit lineage.** The fresh manuscript blob is unchanged from the pinned source. I reread the full 790-line proof and the current package status, reconstructed the specialized analytic and algebraic steps touched by the new source transfer, and found no new mathematical defect. The earlier account01/B18 Schur-limit objection has been explicitly corrected: the manuscript's moving-threshold singular-value argument is valid.

This is a continuation by the same logical worker, not a new independent reviewer. The release gate still requires genuinely separate complete reviews.

The theorem remains

\[
s_{17}(A)\ge s>0
\Longrightarrow
\|p_{X^TAX+b^TX+c}\|_\infty\le C\,K^2/s
\]

for arbitrary dimension, arbitrary real symmetric `A`, arbitrary affine `b,c`, and independent real coordinate densities bounded by `K`, with no moment, iid, log-concavity, support, smoothness, sign or diagonal-basis assumption. The full three-eigenvalue theorem and full-target continuity remain open.

## Current package/readback

The current root contains the full 790-line manuscript plus `SOURCE_MANIFEST.json`, `proof_map.csv`, `verify.py`, `checks.json` and `DELIVERY_STATUS.md`. The delivery status records a PASS of the finite reproducibility suite (534 exact interpolation seeds, 18 exact volume-sampling cases, 240 floating Schur diagnostics and 30 graph-weight diagnostics), correctly labeled as finite checks rather than proof.

## Source-valid improvement proved this run

William Beckner's sharp Hausdorff–Young theorem gives, for every cap-one probability density `f` and every `q>=2`,

\[
\int|\widehat f(t)|^qdt
\le
2\pi q^{-1/2}
\left(\frac q{q-1}\right)^{(q-1)/2}.
\]

Propagating the exact `q=2/d_i` constants through the manuscript's graph Brascamp–Lieb proof, rather than replacing them by a uniform scalar-power constant, yields

\[
\boxed{
|\phi_{F(X_I)+2X_I^TMX_J+G(X_J)}(t)|
\le
\det\left(I+\frac{2t^2}{\pi^2e^2}M^TM\right)^{-1/8}.}
\]

The proof uses only original-coordinate product independence and arbitrary measurable same-bank phases `F,G` are retained.

This improves both the pinned coefficient `1/(pi^2 e^2)` and this slot's preceding Rudelson–Vershynin coefficient `1/(2 pi^2 e)`.

The full derivation, exact entropy calculation, quarter-power propagation, and arithmetic are saved in the paired improvement file

`improvements/account03/B18/20260924T135408Z-account03-B18-fixedmult-audit-r12/BECKNER_SHARP_GRAPH_AND_CONSTANT_3690.md`.

## Same-scope theorem constant

The new determinant gives the quarter-power concentration constant

\[
C_B=\sqrt2\,e^{3/8}\pi^{-1/4}\Gamma(3/8),
\]

with the explicit coarse bound `C_B<4`. Hence the translated logarithmic potential is `<48/5`. Keeping the manuscript's `eta=1/100` gives scalar-pivot truncated half-potential `<368`.

The indefinite-pair branch is independently `<340` because for `D>=1/100`,

\[
D^{-1/2}(32+4\log(16\sqrt D))
\]

is decreasing and its endpoint value is `10(32+4 log(8/5))<340`. The no-pivot order-three half-potential is `<150` under the new determinant. Thus

\[
s_9(A)\ge1
\Longrightarrow
\sup_a E|Q-a|^{-1/2}<369.
\]

Feeding this into the scalar-pivot branch of the main proof yields the same-scope theorem

\[
\boxed{
 s_{17}(A)\ge s>0
 \Longrightarrow
 \|p_{X^TAX+b^TX+c}\|_\infty
 <3690\,K^2/s.}
\]

No theorem hypothesis changes and continuity is not newly asserted in pivot branches.

## Multiplicity audit

This source improvement does **not** lower 17. Under `s_13(A)>=1` the current structural argument supplies order-four crossing volume, but the strengthened determinant still yields only the endpoint decay `|phi(t)|=O(1/|t|)`. Absolute Fourier inversion remains logarithmically divergent. The prior leverage-gapped result closes every fixed-gap subcase; the heavy-row leverage-to-one endpoint remains.

The package's exact completion examples also show the current `rank R<=3r` and restricted `rank R[L,L]<=r` estimates can saturate, so constant retuning or replacing the global loss by `2r` is not a valid threshold reduction.

Therefore this run proves no unconditional 16- or 13-eigenvalue `L^infinity` theorem. A true threshold reduction still requires a new endpoint order-four receiver, a physical heavy-row/curved-fiber mechanism retaining same-bank phases, or a product-preserving repartition theorem forcing a leverage gap.

## Designated partner application

I consumed account04/B18 r6, which proves for its two-sided-anchor packet

\[
\|p_Q\|_\infty\le 2\sqrt{2\pi}/\sqrt{c_1c_2}.
\]

For

\[
Q_{\varepsilon,\lambda}
=2X_1Y_1+2\varepsilon X_2Y_2+\lambda W^2,
\quad0<\varepsilon<1,\ \lambda\ge1,
\]

the coefficient matrix has eigenvalues `{1,-1,epsilon,-epsilon,lambda}`, so exactly three have modulus at least one. The partner result applies with `c_1=1,c_2=epsilon` and gives

\[
\|p_Q\|_\infty\le 2\sqrt{2\pi}/\sqrt\varepsilon.
\]

At `epsilon=1/2` this is `4 sqrt(pi)`. This is a supporting control application, not a claim that the full three-eigenvalue theorem is solved.

## Primary-source/prior-art status

- Beckner 1975: exact source used this run; sharp Hausdorff–Young, hypothesis match PASS.
- Rudelson–Vershynin: sharp normalized linear-sum density; hypothesis match PASS but weaker for the present Fourier-power constant after propagation.
- Livshyts–Paouris–Pivovarov: sharp product marginal caps; relevant, but does not by itself remove arbitrary same-bank quadratic phases.
- Banks–Garza Vargas–Kulkarni–Srivastava: bilinear-affine density theorem; does not directly cover arbitrary `F(X_I)+G(X_J)` phases after a physical cut.
- Herry–Malicet–Poly: input regularity/iid hypotheses are narrower and do not match the present rough non-iid theorem.

No exact published theorem was found among the checked primary sources that solves the unrestricted three-eigenvalue conjecture with all owner quantifiers.

## Status ledger

- pinned `s_17` theorem: **PASS in this B18 lineage**;
- new determinant coefficient `2/(pi^2 e^2)`: **PROVED**;
- same-scope constant `3810 -> 3690`: **PROVED**;
- unconditional `s_13` L-infinity: **OPEN**;
- full three-eigenvalue L-infinity conjecture: **OPEN**;
- full-target continuity: **OPEN**.
