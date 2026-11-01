# HARD10-03 — exclusion-confinement sharpening and delivery addendum

This is an append-only addendum to

`proofnet24/HARD10-03/runs/2026-09-16/2026-09-16T01-21-30Z__report.md`.

The full `d=3` Tóth conjecture remains open.

## 1. Sharpening of NEW-L45

The main report used a deliberately simple binomial estimate and obtained the sufficient condition

\[
e^2|S|q_\beta<1,
\qquad q_\beta=p_\beta(0,0).
\]

A sharper summation is available without changing the probabilistic argument.

From NEW-L44,

\[
\mathbb P(C_0\subseteq S)
\le
\sum_{\ell=1}^{s}
\binom{s-1}{\ell-1}(\ell q_\beta)^\ell,
\qquad s=|S|.
\tag{1.1}
\]

Use only

\[
\binom{s-1}{\ell-1}
\le
\frac{(s-1)^{\ell-1}}{(\ell-1)!}.
\]

Putting

\[
x=(s-1)q_\beta,
\]

gives

\[
\mathbb P(C_0\subseteq S)
\le
q_\beta
\sum_{\ell\ge1}
\frac{\ell^\ell}{(\ell-1)!}x^{\ell-1}.
\tag{1.2}
\]

Let the rooted-tree function

\[
T(x)=\sum_{n\ge1}\frac{n^{n-1}}{n!}x^n
\]

be the solution in `[0,1)` of

\[
T=xe^T,
\qquad 0\le x<e^{-1}.
\]

Writing `D=x d/dx`,

\[
D^2T
=
\sum_{n\ge1}\frac{n^{n+1}}{n!}x^n
=
\frac{T}{(1-T)^3}.
\]

Since

\[
\frac{n^n}{(n-1)!}=\frac{n^{n+1}}{n!},
\]
we obtain the exact majorant identity

\[
\sum_{\ell\ge1}
\frac{\ell^\ell}{(\ell-1)!}x^{\ell-1}
=
\frac1xD^2T(x)
=
\frac{e^{T(x)}}{(1-T(x))^3}.
\tag{1.3}
\]

Therefore:

### NEW-L45A — PROVED

Whenever

\[
(s-1)q_\beta<e^{-1},
\]

\[
\boxed{
\mathbb P(C_{\pi_\beta}(0)\subseteq S)
\le
q_\beta
\frac{e^{T((s-1)q_\beta)}}
{\bigl(1-T((s-1)q_\beta)\bigr)^3}.
}
\tag{1.4}
\]

Thus for every fixed `a<e^{-1}` there is a finite constant

\[
C(a)=\frac{e^{T(a)}}{(1-T(a))^3}
\]

such that

\[
(s-1)q_\beta\le a
\quad\Longrightarrow\quad
\mathbb P(C_0\subseteq S)\le C(a)q_\beta.
\tag{1.5}
\]

The qualitative conclusion of NEW-L45 is unchanged, but the natural dimensionless volume threshold furnished by this particular majorant is improved from `e^2 s q_beta<1` to approximately `s q_beta<1/e`.

Exactly the same summation sharpens the conditional NEW-L46: with

\[
\alpha=\sup_{a,x\in S}K^\mathscr F(a,x),
\]
if

\[
(|S|-1)\alpha<e^{-1},
\]
then

\[
\boxed{
\mathbb P(C_P(u)\subseteq S\mid\mathscr F)
\le
\alpha
\frac{e^{T((|S|-1)\alpha)}}
{\bigl(1-T((|S|-1)\alpha)\bigr)^3}.
}
\tag{1.6}
\]

No new external hypothesis is used in this sharpening.

## 2. Finite-state sanity checker

A checker was executed on homogeneous interchange processes on `path4`, `cycle4`, `cycle5`, and `star5`, and on a genuinely time-inhomogeneous four-vertex process with two deterministic forced transpositions interspersed with random symmetric-exclusion segments.

For every subset `A` containing root `0`, it checked

\[
\mathbb P(C_0=A)
\le
\mathbb P(P(A)=A)
\le
\prod_{x\in A}\sum_{a\in A}K(a,x).
\]

All tested cases passed to matrix-exponential precision. In the conditional time-inhomogeneous example, the conditional one-particle kernel had maximum asymmetry

\[
0.04410230391835285,
\]

so the test is not accidentally confined to a reversible conditional kernel.

These computations are sanity checks only; the proof is the strong-Rayleigh/negative-association argument in the main report.

## 3. Delivery receipts

### Main mathematical report

Path:

`proofnet24/HARD10-03/runs/2026-09-16/2026-09-16T01-21-30Z__report.md`

Commit:

`931e2938a37e6541db2fcfb907d952a201f284b0`

Exact-commit readback blob:

`15c3c18e6cd860c298247a50d3e163c9ec5924dc`

Delivery status: **VERIFIED**.

### Checker

Path:

`proofnet24/HARD10-03/artifacts/2026-09-16T01-34-00Z__exclusion_negative_dependence_check.py`

Commit:

`4997a6073684255cf672f0e0d15e69eaa5802aec`

Exact-commit readback blob:

`4e609c878d57bfd8bfecb4726073d85ad9c499ac`

Delivery status: **VERIFIED**.

### Executed checker output

Path:

`proofnet24/HARD10-03/artifacts/2026-09-16T01-34-00Z__exclusion_negative_dependence_check_output.json`

Commit:

`3146a66df5b55f0b5cfc94f185ca843971258221`

Exact-commit readback blob:

`398cc4a261e2a99bd3caa0f545f60df462e7d303`

Delivery status: **VERIFIED**.

No earlier or peer file was overwritten. No Gmail/email or Google Drive action was attempted.
