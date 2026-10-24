Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 at maximum.**

# HARD7-03 idea before code — use the omitted A1-maximal centre cone

Target remains D0025 / Seppäläinen Problem 4, frozen binary K=2 site-disorder case. Previous metric is

\[
L=\frac{25000000}{292367491}\le \Delta_2(Q).
\]

Previous run B1/B11/B15 used only two of the three first-layer maximum cones for the genuinely nonnested centre adjacent pair. This run rotates to **B7/B18/B25** and attacks the omitted cone rather than adding another outer recurrence lemma.

For the left-centre adjacent pair write

\[
R=\max(Y_{-1},Y_0),\quad X=Y_{-2},\quad Z=Y_1,
\quad S=\max(R,X),\quad T=\max(R,Z),
\]

where

\[
Y_{-2}=A_{-1}+B_{-2},\quad
Y_{-1}=\max(A_{-1},A_0)+B_{-1},
\]
\[
Y_0=\max(A_{-1},A_0,A_1)+B_0,\quad
Y_1=\max(A_0,A_1)+B_1,
\]

and all displayed clocks are iid unit exponentials.

## B7 — isolate the last first-layer cone

On the previously unused event

\[
E_3=\{A_1\ge A_{-1},A_0\},
\]

put

\[
m=A_1,\qquad d=A_1-\max(A_{-1},A_0)\ge0.
\]

Then

\[
Z=m+B_1,\qquad R=m+M_d,\qquad
M_d:=\max(B_0,B_{-1}-d).
\]

Whenever `B_1>M_d`, set `g=B_1-M_d`. Then `T=R+g` while always `S>=R`. For the exact two-clock kernel from the previous checkpoint,

\[
K_\theta(s,t)=E\,e^{\theta\min(s+C,t+D)},
\]

coordinatewise monotonicity gives

\[
K_\theta(S,T)-K_\theta(R,R)
\ge K_\theta(R,R+g)-K_\theta(R,R)
=e^{\theta R}\frac{\theta}{q a}(1-e^{-qg}),
\]

where `q=1-theta`, `a=2-theta`. Thus the omitted cone has a strictly positive, exactly integrable contribution.

## B18 — conditional Laplace transform of a delayed maximum

For fixed `d>=0`,

\[
F_{M_d}(u)=(1-e^{-u})(1-e^{-(u+d)}),\qquad u\ge0,
\]

so

\[
f_{M_d}(u)=(1+e^{-d})e^{-u}-2e^{-d}e^{-2u}.
\]

If `B~Exp(1)` is independent, then for fixed `M_d=u`,

\[
\int_u^\infty e^{-b}\bigl(1-e^{-q(b-u)}\bigr)\,db
=\frac q a e^{-u}.
\]

Consequently, with `b=3-theta`,

\[
E[e^{-qM_d}]=\frac{1+e^{-d}}a-\frac{2e^{-d}}b
=\frac1a-\frac{q}{ab}e^{-d},
\]

and hence

\[
H(d):=E\left[e^{\theta M_d}(1-e^{-q(B-M_d)})1_{\{B>M_d\}}\right]
=\frac q{a^2}-\frac{q^2}{a^2b}e^{-d}.
\]

This converts the dependence of the full cone to two scalar first-layer transforms.

## B25 — count the first-layer transform two ways

Define

\[
J_0=E[e^{\theta A_1};E_3],\qquad
J_1=E[e^{\theta A_1-d};E_3].
\]

Direct maximum integration gives

\[
J_0=\int_0^\infty e^{-qx}(1-e^{-x})^2dx
=\frac1q-\frac2a+\frac1b
=\frac{2}{qab}.
\]

For `J_1`, split according to which of `A_{-1},A_0` is larger. If `y=max(A_{-1},A_0)`, symmetry gives

\[
J_1=2\int_{0\le y\le x<\infty}e^{-x-y}\,(1-e^{-y})e^{\theta x-(x-y)}\,dy\,dx.
\]

Integrating first in `y`, equivalently using the spacing variable `d=x-y`, gives the closed form

\[
J_1=2\left(\frac1{a^2}-\frac1a+\frac1b\right)
=\frac{2}{a^2b}.
\]

Therefore the incremental gain from the omitted cone for one centre adjacent pair is

\[
\delta_3
=\frac{\theta}{qa}\left(\frac q{a^2}J_0-\frac{q^2}{a^2b}J_1\right)
=\boxed{\frac{2\theta(5-3\theta)}{q a^5 b^2}}>0.
\]

The previous two-cone gain is already inside the current four-step bound and must not be counted again. There are two reflected centre adjacent pairs and each occurs in two fourth-step predecessor windows, so the *incremental* pair-subtraction gain proposed for this run is exactly `4 delta_3`.

At the inherited rational `theta=723/1250`, the next step is to exact-check this identity, subtract `(4 delta_3)/q` from the current four-step bound, and then search only for a rational `A` whose truncated exponential certificate is strictly positive. No numerical fit will be promoted to proof.