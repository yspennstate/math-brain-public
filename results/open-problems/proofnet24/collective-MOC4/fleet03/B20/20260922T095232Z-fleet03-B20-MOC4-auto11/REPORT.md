# fleet03/B20 MOC4 — exact axis antitransport and global equality-leaf propagation

**Directive:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Run:** `20260922T095232Z-fleet03-B20-MOC4-auto11`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`. Full MOC4 remains **OPEN / NOT PROVED / NOT DISPROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.

## 1. Exact target and source-bound state

The target is the full complex-normal four-dimensional Marcus-de Oliveira statement

\[
\det(A+B)\in\operatorname{conv}\left\{\prod_{i=1}^4(a_i+b_{\sigma(i)}):\sigma\in S_4\right\}
\]

for every complex normal `4 x 4` pair, with singular and repeated spectra included.
No arbitrary bistochastic array, independently selected compound minor, or common-lift surrogate is used below.

The newest complete campaign-lead input consumed is fleet03/B07 run
`20260922T074824Z-fleet03-B07-MOC4-r13`, report blob
`7724d19f793eb934c5fcc2b469bb9d0a108da4eb`, especially
`MOC4-MSQR-CROSS-BLOCK-ANNIHILATION-v1` and
`MOC4-MSQR-CROSS-SPLIT-RESERVE-v1`. On a mixed-Schur pair boundary at a genuine global support maximizer, the pair null vector is a full-Hessian null vector, cross Hessian couplings vanish, and the fourth-order Lyapunov-Schmidt condition contains the nonnegative cross reserve

\[
q_4+3R_{\rm pair}+3R_{\rm cross}\le0.
\]

The immediately preceding B20 result, report blob
`197308f44d9e273a0d73ba89f691d3e85b4c23aa`, made the cross reserve quantitative in adjacent true-unitary root directions.

The freshest compatible cross-account result consumed is fleet02/B07 run
`20260922T093424Z-b07-c8697991`, report blob
`52c8681b4b72cbdb5655c9668ed36d87376ceec9`, theorem
`MOC4-MSQR-BILATERAL-EQUALITY-CIRCLE-v1`. At simple pair-LS saturation it derives exact left and right same-pair equality circles and the full-coupling axis relation only up to parallelism/scale.

The exact assigned OTHER-account partner is fleet04/B09. Its newest complete run consumed here is
`20260922T084040Z-b09-moc4-r38`, report blob
`eff32b1a75051281bca2cf1b8b552060f4d285d8`, theorem
`MOC4-ZERO-FACE-ALIGNED-EXTERNAL-ONE-THIRD-CAP-v1`. It proves, on a genuine zero face, an exact one-third cap for every aligned Drury external coefficient using both complementary channels, and it refutes an anti-linear-only payment mechanism. This is used below as the correct target-safe endpoint for any axis-degenerate branch that is subsequently reduced to a zero face; it also rules out replacing the full-coupling argument by a one-channel distance estimate.

## 2. Simple pair-LS normal form

Use the same exact pole normal form as the source results. Put

\[
A=s_a^2>0,\qquad B=s_b^2>0,\qquad t=\sqrt{AB}=s_as_b>0,
\]
\[
M=\operatorname{diag}(t,m),\qquad D=AB-m^2>0,
\]

and impose the mixed-kernel cubic cancellation

\[
r_1=s_b\rho,\qquad s_1=-s_a\rho.
\]

Write

\[
Z=\begin{pmatrix}
t&0&r_1\\
0&m&r_2\\
s_1&s_2&z
\end{pmatrix},
\quad
p=(-r_1,-r_2,A-z),
\quad
q=(-s_1,-s_2,B-z),
\]
\[
H=A+B-2z.
\]

Define the pair-LS residual

\[
Q:=D(H-\rho^2)-\bigl(Ar_2^2+2mr_2s_2+Bs_2^2\bigr). \tag{2.1}
\]

Thus `Q=0` is exactly the simple pair-LS equality condition.
Following fleet02/B07, set

\[
k_L={Ar_2+ms_2\over D},\qquad
k_R={Bs_2+mr_2\over D},
\]
\[
w_L=(0,1,-k_L),\qquad w_R=(0,1,-k_R),
\]
\[
a_L=p\times w_L,\qquad a_R=q\times w_R. \tag{2.2}
\]

The vectors `a_L,a_R` are the distinguished axes orthogonal to the left/right trust-plane data.

## 3. New theorem — `MOC4-MSQR-EXACT-AXIS-ANTITRANSPORT-v1`

Before imposing pair-LS equality, direct multiplication in the normal form gives the **residual identities**

\[
\boxed{Z^Ta_L+t a_R=-{tQ\over D}e_1},\qquad
\boxed{Za_R+t a_L=-{tQ\over D}e_1}. \tag{3.1}
\]

Consequently, at exact simple pair-LS saturation `Q=0`,

\[
\boxed{Z^Ta_L=-\sqrt{AB}\,a_R},\qquad
\boxed{Za_R=-\sqrt{AB}\,a_L}. \tag{3.2}
\]

This sharpens the inherited statement `Z^Ta_L || a_R`, `Za_R || a_L`: the proportionality sign is forced negative and its scale is exactly `sqrt(AB)`.

### Proof

Substitute (2.2) into `Z^Ta_L+t a_R` and `Za_R+t a_L`. The second and third coordinates cancel identically using only
`r_1=s_b rho`, `s_1=-s_a rho`; the first coordinate in both expressions is

\[
-{t\over D}
\left[D(H-\rho^2)-(Ar_2^2+2mr_2s_2+Bs_2^2)\right],
\]

which is `-tQ/D`. This proves (3.1), and `Q=0` proves (3.2). QED.

Two finite consequences are immediate.
First, taking the scalar product of the first identity in (3.2) with `a_R` and using the second gives

\[
\boxed{\|a_L\|=\|a_R\|}. \tag{3.3}
\]

Second, because `t>0`,

\[
\boxed{a_L=0\iff a_R=0}. \tag{3.4}
\]

So the source report's apparent one-sided degeneracy alternative is actually bilateral.

The bilateral-degenerate branch also has a compact scalar form. Since
`(a_L)_3=-s_b rho`, equation `a_L=0` forces

\[
\rho=0.
\]

At `Q=0` and `rho=0`, direct simplification gives

\[
(a_L)_1={Ar_2^2-Bs_2^2-(A-B)D\over 2D},
\]

so bilateral degeneracy is equivalent to the additional exact condition

\[
\boxed{Ar_2^2-Bs_2^2=(A-B)(AB-m^2)}. \tag{3.5}
\]

Thus the degenerate residual is no longer an unspecified full-`Z` multiplicity branch: in this pole normal form it lies on the explicit codimension-two algebraic locus `rho=0` plus (3.5). The inherited full-`Z` singular-value multiplicity statement remains valid on that locus.

## 4. New global consequence — `MOC4-MSQR-GLOBAL-EQUALITY-LEAF-v1`

At `Q=0`, fleet02/B07 proves that the left trust equality set is a nondegenerate genuine same-pair circle

\[
\mathcal C_L=\{n\in S^2:w_L\cdot n+k_L=0\},
\]

and that, at every regular point, the complementary optimizer

\[
m(n)={q+Z^Tn\over L-p\cdot n}
\]

lies on the corresponding right equality circle and attains exactly the same pair-orbit support value `L` as the base point.

Now use the fact that the base point under discussion is a **full** `U(4)` global support maximizer. The same-pair orbit is a subset of the full unitary orbit. Hence every regular point of this equality circle with support `L` is itself a full global maximizer, not merely a same-pair maximizer.

Let `tau` be the tangent to this equality leaf at any such regular point. Since the support is constant on the leaf,

\[
D^2F(\tau,\tau)=0.
\]

But at a full global maximizer `-D^2F` is positive semidefinite. A zero quadratic value of a positive-semidefinite operator places `tau` in its kernel. Therefore

\[
\boxed{D^2F(\tau,Y)=0\quad\text{for every true-unitary tangent }Y} \tag{4.1}
\]

at **every regular point of the entire equality leaf**.

Thus pair-LS equality does more than give one full-Hessian kernel at the base point: it propagates a full-Hessian null direction around a genuine one-parameter family of full global maximizers. This is a new continuum of cross-split annihilation equations, all coming from the same true unitary orbit.

No higher derivative restricted to the already-flat same-pair circle can add information; useful leverage must come from the cross-split equations (4.1), their structured spectral coefficients, or the bilateral-degenerate algebraic locus (3.5).

## 5. Exact verification

`VERIFY_EXACT_AXIS_ANTITRANSPORT.py` uses only Python standard-library `Fraction` arithmetic. It checks (3.2)-(3.5) on three exact rational calibrations:

1. the fleet02/B07 source calibration `A=B=1`, `m=0`, `rho=1/3`, `r2=1/4`, `s2=1/5`;
2. an unequal-sector calibration `A=4`, `B=9`, `m=1`, `rho=2/7`, `r2=1/5`, `s2=-3/8`;
3. the bilateral-degenerate point `A=B=1`, `m=0`, `rho=0`, `r2=s2=1/3`.

It returns `PASS MOC4-MSQR-EXACT-AXIS-ANTITRANSPORT-v1` exactly. The verifier blob is
`5ec396c1f341b2bc25fcb3d883e2d39777801722`; captured output blob is
`858fb4ff1f2d75a0b6c793de97ebe3dea7444018`.
The code checks transcription/algebra only; the proof above is analytic and does not promote MOC4 itself.

## 6. Application of the assigned fleet04/B09 partner result

The fleet04/B09 r38 theorem is used to sharpen the proof tree rather than as decoration.
Its one-third cap is an exact same-unitary restriction on any zero-entry representative reached from the present branch, while its sharp example proves that the anti-linear channel alone cannot pay a bad external vertex. Therefore:

- the **generic** axis branch must exploit the full signed antitransport (3.2) together with the lead's cross-Hessian annihilation, rather than a one-channel metric hole;
- the **bilateral-degenerate** branch is first reduced to the finite locus `rho=0` and (3.5); if the existing zero-face reduction is triggered there, the partner theorem immediately caps every aligned bad external coefficient by `1/3` and reduces its entire isolated external excess by a factor of three;
- that coefficient cap is not itself enough to close MOC4, because fleet04/B09 proves it is sharp. A universal closure must additionally force target-safe companion support or a strict sub-endpoint deficit.

This preserves common-unitary compatibility throughout.

## 7. What is now unpaid

The exact next implication is

**`MOC4-MSQR-LEAF-CROSSSPLIT-RIGIDITY-v1` (OPEN):**

> Starting from a positive-gap true-unitary global maximizer on simple pair-LS saturation, combine the exact antitransport equations (3.2), the continuum of full-Hessian cross-annihilation equations (4.1), the lead's same-unitary `P/R/D` and exterior-square identities, and the structured spectral/Vandermonde coefficients. Prove that the generic axis branch is target-safe or collapses to a known common-block/zero-face boundary. On the bilateral-degenerate locus `rho=0`, (3.5), either complete the zero-face reduction and apply the fleet04/B09 directional-payment machinery, or prove target safety directly.

A strict true-unitary/spectral solution of all those equations with positive separation from all 24 permutation products would instead be a genuine MOC4 counterexample.

The all-negative-definite (`NDI`) branch remains separate.

**Status:** `ESSENTIAL_STEP_APPLIED`; full MOC4 remains **OPEN / NOT PROVED / NOT DISPROVED**.
