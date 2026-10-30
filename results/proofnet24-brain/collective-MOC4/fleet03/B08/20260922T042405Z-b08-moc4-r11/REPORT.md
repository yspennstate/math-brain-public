# MOC4-DENSE-CAYLEY-ADVERSARY-v1

Status: **ESSENTIAL STEP APPLIED; parent MOC4 remains OPEN (not proved, not disproved).**

## Scope and mechanism change

This B08 pass follows the exact fleet03/B08 adversary assignment: use genuine unitaries and complex spectra, and test one common real-linear separating direction against all 24 spectral permutation products. It deliberately changes mechanism away from the preceding one-cycle/Givens analysis. The new family uses dense complex rational Cayley unitaries

\[
U=(I-S)(I+S)^{-1},\qquad S^*=-S,
\]

with Gaussian-integer skew-Hermitian generators. This is not a bistochastic surrogate and no conclusion is drawn from signs of formal determinant-expansion coefficients.

## Exact true-unitary stress datum

Use the simple spectra

\[
a=(18-17i,-20+2i,15-22i,-21+2i),
\]
\[
b=(-19+4i,25-5i,18-i,-18+i).
\]

The Cayley search produced the exact unitary

\[
U={1\over3562}
\begin{pmatrix}
-2724-1551i&234+247i&-1219+167i&1106-96i\\
236-101i&-2782+1417i&1+1607i&490+228i\\
1443+39i&845+793i&-2522+702i&234-1534i\\
-820+200i&-416+1144i&-1060-784i&-2910+536i
\end{pmatrix}.
\]

Exact arithmetic verifies \(UU^*=I\). All 16 entries and all 36 two-by-two minors are nonzero. Both spectra are simple, every \(a_i+b_j\neq0\), and all 24 target products

\[
v_\sigma=\prod_{i=1}^4(a_i+b_{\sigma(i)})
\]

are distinct. Thus this is a genuinely dense generic true-unitary datum, not a boundary/block/flat-pair artifact.

With \(A=\operatorname{diag}(a)\) and \(B=U\operatorname{diag}(b)U^*\), exact determinant evaluation gives

\[
D:=\det(A+B)={278808875\over3562}+{24903390\over1781}i.
\]

## Exact common support-direction test

Take the single real-linear functional

\[
L(z)=-5782\,\Re z+19099\,\Im z.
\]

Evaluating this *same* functional on all 24 target vertices gives

\[
M:=\max_{\sigma\in S_4}L(v_\sigma)=-61633500,
\]

attained exactly at the two hull-edge permutations \(1234\) and \(1342\) (one-based notation). The opposite support value is

\[
m=-59822291610.
\]

For the true-unitary determinant,

\[
L(D)=-{2411727095\over13},
\]

hence the exact separating gap has the target-safe sign

\[
M-L(D)={1610491595\over13}>0.
\]

Normalized by the full support width,

\[
{M-L(D)\over M-m}
={322098319\over155377711086}
\approx 0.0020730020847180702.
\]

So this dense complex true-unitary point sits only about **0.2073% of the support width inside** this exposed hull edge, but it does not escape it.

## Exact convex-hull rescue certificate

The datum is not merely support-safe in the displayed direction. It has the exact three-vertex Caratheodory representation

\[
D=\lambda_0v_{1234}+\lambda_1v_{1243}+\lambda_5v_{1432},
\]

where

\[
\lambda_0={73409846651\over406763017440},\qquad
\lambda_1={98803540981\over406763017440},\qquad
\lambda_5={234549629808\over406763017440}.
\]

All three coefficients are nonnegative and sum exactly to one. The three vertices are

\[
v_{1234}=115344+31692i,\quad
v_{1243}=2400-4500i,\quad
v_{1432}=98632+16226i.
\]

This is therefore an exact interior rescue certificate for a dense, near-facet adversary.

## Peer-result consumption and coordination

Named partner **fleet04/B09** was consumed via its current `MOC4-STANDARD-CHANNEL-CEILING-v1` receipt. Its result says that for a fixed spectrum/support direction every genuine-unitary violation must fit the standard-channel reserve inequality \(\gamma\le K_{\rm std}-\Delta\), sharpening the earlier pair-fiber ceiling. The present datum supplies a concrete generic spectrum/support pair with a very small exact target margin on which that partner diagnostic can be evaluated next; B08 does not invent the partner's undefined internal coefficients here.

A second named other-account result was consumed from **fleet01/B07**, `MOC4-BIORIENTATION-PAIR-GATE-v1`. It proves six row/column orientation-swap necessary inequalities at a global true-unitary support maximizer and shows that transport-only/SO(6)-only separators are insufficient. This changes the next adversary search: rather than merely minimizing hull distance over arbitrary unitary samples, optimize the same common support functional over genuine Cayley-unitary coordinates and retain only candidates satisfying the true-unitary stationarity/orientation gates before exact rational enclosure.

## Consequence and next obligation

`MOC4-DENSE-CAYLEY-ADVERSARY-v1` does **not** disprove MOC4. Its value is that it moves the adversarial lane off the already-studied one-cycle mechanism and produces an exact dense generic point extremely close to a genuine target facet, together with a rigorous common-direction test and an exact Caratheodory rescue.

The next sharp task is `MOC4-CAYLEY-STATIONARY-FACET-v1`: for fixed simple spectra, maximize an exposed-edge functional over a dense skew-Hermitian Cayley chart; impose the fleet01/B07 six orientation gates and the fleet04/B09 standard-channel ceiling on candidate maximizers; then either (i) rationally enclose a strict positive violation \(L(D)-M>0\), which would be an actual MOC4 counterexample, or (ii) prove an exact local/global payment inequality preventing the near-facet branch from crossing.

## Reproducibility

`verify_dense_cayley_adversary.py` is a self-contained Python-standard-library exact verifier using `fractions.Fraction`; it checks unitarity, all nonzero two-by-two minors, determinant arithmetic, all 24 common support values, the exact gap, and the three-vertex convex certificate. `verification.txt` records the checked exact output.

Brain status: **WITHOUT_VERIFIED_BRAIN**. No held-out benchmark material, credentials, scheduler mutation, email/Drive/public dispatch, paid model/API/Codex, or cross-account native action was used.
