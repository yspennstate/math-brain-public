Model: GPT-5.6 Sol. Reasoning: UNVERIFIED; this run did **not** run on GPT-6 at verified maximum reasoning. Frozen source metric at entry: `T_corr=2`. Methods selected: **B1/B20/B27**, different from the preceding B14/B15/B4 triple.

# HARD7-02 idea checkpoint before code — Q1.9 logarithmic reciprocal-product criterion

## Continuity and source refresh

Active exclusive claim: `operations/claims/CAMPBELL-OROURKE-2022-Q1.9.md`.

Source: Andrew Campbell and Sean O'Rourke, *Spectrum of Heavy-Tailed Elliptic Random Matrices*, EJP 27 (2022), paper 127, arXiv:2010.01261v3, Section 1.3:

> **Question 1.9.** How does the tail behavior of `mu_{alpha,theta_d}` vary with respect to `theta_d`?

The source contrasts the axis-supported i.i.d. case (exponential limiting tail) with the Hermitian case (same heavy-tail behavior as the entries), and Figure 2 explicitly samples real angular laws obtained by taking

`W=(cos omega, sin omega)`,

where `omega` is uniform on the four axis angles `{0,pi/2,pi,3pi/2}` thickened by an interval `[-b pi/4,b pi/4]`.

Fresh bounded 2026-09-19 web checks re-found the 2022 source, Campbell--O'Rourke's 2024 Levy--Khintchine random-Laplacian paper, Carpenter--O'Rourke's 2025 sparse elliptic preprint arXiv:2508.04891, and Girko's 2025 finite-variance elliptic work. I did not locate a later paper claiming a general answer to Question 1.9 or the criterion below. This is bounded negative evidence only.

At run start I also re-read the HARD7 control, both new-method directives, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, campaign `INDEX.md`/`RANKING.md`, the active claim, the latest own report `2026-09-19T19-14-06Z__q19-balanced-phase-amplitude-band-exponent.md`, repository-wide aliases, and the neighboring C0032 terminal handoff. Ownership remains exclusive to HARD7-02; C0032 is the distinct i.i.d. heavy-tailed circular-law density problem.

## New route before any checker

The preceding proof averaged a selected edge over a Haar phase and then used a Mahler-measure lower bound. That looked like the essential symmetry. It is not.

For one selected exceedance edge with normalized pair

`(s Y w_1, s Y w_2)`,

where `Y` is Pareto with `P(Y>y)=y^{-alpha}` for `y>=1`, condition on the entire matrix except this single overshoot and angular mark `W=(w_1,w_2)`. For fixed spectral parameter `z`, the determinant is a **quadratic polynomial in the radial overshoot itself**:

`D(Y)=A+s C(W)Y-s^2 w_1 w_2 B Y^2`,

with `B=det(zI-A^{\setminus{i,j}})`.

If `B != 0` and `w_1w_2 !=0`, factor

`D(Y)=-s^2 w_1w_2 B (Y-r_1)(Y-r_2)`.

The key one-dimensional observation is independent of every phase:

`inf_{c in C} E log|Y-c| >= -2 alpha`.

Indeed `|Y-c|>=|Y-Re(c)|`; the logarithm is negative only on a unit interval about `Re(c)`, the Pareto density is at most `alpha`, and

`int_{-1}^1 log|t| dt = -2`.

Therefore

`E_Y log|D(Y)| >= 2 log s + log|w_1w_2| + log|B| - 4 alpha`.

After averaging in `W`, the only angular hypothesis required by this peeling step is

`ell_theta := (1/theta(S)) int_S log|w_1w_2| d theta(w) > -infinity`.

This removes Haar phase symmetry completely.

## B1 — change category

Instead of classifying angular measures by geometric orbit type, classify them by the scalar logarithmic functional

`ell_theta = E log|W_1W_2|`.

This changes the problem from an angular-support geometry problem to a logarithmic-integrability problem. The axis-supported i.i.d. endpoint has `ell_theta=-infinity`; every angular density with only integrable zeroes at the axes has finite `ell_theta`.

Candidate theorem: for every finite angular measure `theta` satisfying C2(i) and finite `ell_theta`, the radial limiting law has exact power exponent `alpha`.

## B20 — find why the old algorithm fails

The old phase-peeling algorithm appeared to fail for non-Haar angular laws because Jensen/Mahler averaging had no exact phase measure. The quadratic-in-overshoot reformulation shows the failure was self-inflicted: phase was the wrong variable to integrate first. Radial Pareto anti-concentration gives a coefficient-uniform logarithmic lower bound and works for arbitrary phase laws.

The remaining genuine obstruction is now explicit: positive angular mass on `w_1w_2=0` makes `ell_theta=-infinity` and kills the leading quadratic coefficient on that mass. This is exactly where the source's i.i.d. axis-supported exponential-tail endpoint lives.

## B27 — swap the quantifiers

Previous theorem: for each balanced-phase family, prove exponent `alpha` using its symmetry.

Stronger swapped statement to try now:

> There is one angular criterion, `ell_theta>-infinity`, such that **every** C2 angular measure satisfying it has exponent `alpha`.

The proof should use one exact Pareto representative for each `(alpha,theta)` because Campbell--O'Rourke Theorem 1.6 says `mu_{alpha,theta}` depends only on `(alpha,theta)`. Thus no general slowly varying radial law has to be handled separately.

## Direct source-family consequence if the proof closes

Let `theta_b` be the Figure-2 angular law from Campbell--O'Rourke:

`omega = K + T`, where `K` is uniform on `{0,pi/2,pi,3pi/2}` and `T` is uniform on `[-b pi/4,b pi/4]`, and `W=(cos omega,sin omega)`.

For every `b>0`, the zeroes of `cos omega sin omega` are isolated and logarithmic, hence

`E log|cos omega sin omega| > -infinity`.

Its support contains non-collinear angular directions, so C2(i) holds. Therefore the candidate criterion would prove

`lim_{r->infinity} -log mu_{alpha,theta_b}(|z|>r)/log r = alpha`

for every `0<alpha<2` and every `b>0` in this source family, while the exact `b=0` axis-supported endpoint is the known i.i.d.-type exponential-tail regime. That would show a **tail-class discontinuity at zero angular thickness** rather than smooth interpolation.

If this survives full proof, count the source Figure-2 thickened-axis family as one new explicit non-i.i.d., non-Hermitian metric unit, moving `T_corr=2 -> 3`; do not count the general theorem as infinitely many units.

No code or finite certificate was produced before this idea checkpoint.