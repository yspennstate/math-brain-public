# PROB10-09 idea before code — use Zuk's all-genus surface spectral bound

Frozen parent: Benjamini–Schramm bond-percolation conjecture for every locally finite Cayley graph of a finitely generated nonamenable group. This iteration stays on R20's delimited standard-surface-product quantitative/nonbacktracking lane. The universal parent remains OPEN/PARTIAL; a restricted family is not closure.

## New idea

The immediate predecessor bounded the genus-4 surface factor by the 1997 BCCH Section-3 estimate

\[
\|M_4\|\le \frac{\sqrt{14}}8+\frac1{16}\approx 0.5303,
\qquad
\|A_4\|\le 1+2\sqrt{14}.
\]

But the same BCCH paper explicitly records the later improvement of A. Zuk: for the standard genus-g surface Cayley graph,

\[
\mu_g=\|M_g\|<g^{-1/2}\qquad(g\ge2).
\]

For g=4 this gives the strictly sharper exact inequality

\[
\|A_4\|=16\|M_4\|<8.
\]

Retain Nagnibeda's published genus-3 upper bound \(\|M_3\|\le0.552792=69099/125000\), hence

\[
\|A_3\|\le 12\cdot\frac{69099}{125000}=\frac{207297}{31250}.
\]

Therefore for the Cartesian product \(X_{3,4}\),

\[
\|A_{3,4}\|<\frac{457297}{31250}=14.633504.
\]

With degree D=28 and Q=27, the standard nonbacktracking transfer reduces the uniqueness-side certificate to the larger root \(\beta\) of \(z^2-Rz+27=0\). I will test the exact rational candidate

\[
p_* = \frac{8020563}{10^8}=0.08020563,
\qquad z_*=p_*^{-1}.
\]

If exact arithmetic verifies \(z_*^2-R_*z_*+27>0\) for \(R_*=457297/31250\) and \(z_*>\sqrt{27}\), then \(\beta<z_*\), hence

\[
p_u(X_{3,4})\ge p_{2\to2}(X_{3,4})>p_*.
\]

Combining with the already-certified unchanged \(p_c(X_{3,4})<4540551/10^8\) would move the frozen gap from \(3123709/10^8\) to \(3480012/10^8=0.03480012\).

## Negation test and two genuinely different alternatives

1. **Negation test of the Zuk import.** Check the exact normalization carefully: BCCH define \(M_g=A_g/(4g)\) for the usual symmetric 4g-element generating set, exactly matching R20's surface-factor normalization. Thus \(\mu_4<1/2\) really means \(\|A_4\|<8\), not a differently normalized spectral radius.

2. **Color-split/nonbacktracking improvement.** Before claiming a new 2x2 transfer, test whether the Cartesian product already forces \(\|A_{3,4}\|=\|A_3\|+\|A_4\|\). Since the factors are bipartite self-adjoint Cayley graphs, their positive spectral edges add in the tensor-sum spectrum. If so, a color split cannot improve the scalar asymptotic endpoint-kernel growth without using information beyond adjacency spectral radii; record this as an obstruction rather than inventing a gain.

3. **p_c-side geodesic/cone-type tree.** Explore whether replacing the Freiheitssatz \(T_{10}\) fibre by a larger collision-free geodesic subtree of the genus-3 Cayley graph can improve the already sharp full-tree fibre certificate. Do not use numerical growth alone: any improvement must include an explicit prefix-closed injective language or finite-state tree embedding proving collision-freeness. If no such certificate is obtained in the bounded iteration, record the exact missing injectivity condition.

Only after this idea record will an exact arithmetic checker be written.