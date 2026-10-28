SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B17, 2026-09-23T21:29:32Z.
attacking: two-heavy zero-physical-pivot exact rotated witnesses; derive a global density cap below the 3sqrt(2) obstruction while allowing an arbitrary fragmented third marginal.

# Two-heavy zero-pivot global stress theorem

## Status

This report proves a new source-valid supporting theorem for an exact genuinely rotated target matrix with spectrum `{1,1,-1}` and a zero physical diagonal pivot. Two original coordinates are cap-one centered uniforms; the third coordinate is allowed to have an arbitrary probability density `0<=f<=1`, with no moment, connected-support, compact-support, log-concavity, or Gaussian assumption. The entire output density is bounded and continuous, with an explicit global ceiling strictly below the current `3 sqrt(2)` lower obstruction.

This does **not** prove the unrestricted QFORM conjecture. In particular, the first two original-coordinate laws are specialized to centered uniforms. Full-target continuity also remains open.


The designated partner result actually applied is account04/B17:

`yspennstate/math-open-problems@2156b76156ad5956c214a881fcfd6d977d6f3b9f`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B17/20260922T211900Z-account04-B17-QFORM-r3/REPORT.md`.

That completed exact finite cap-one rotated construction proves

\[
p_{Q_m}(0)=3\sqrt2\left(1-\frac{5295}{21952m}+O(m^{-2})\right),
\]

hence every possible universal constant `C_*` satisfies

\[
C_*\ge 3\sqrt2.
\tag{P}
\]

## Theorem

Let `X,Y` be independent `Unif[-1/2,1/2]`. Let `Z` be independent of `(X,Y)` and have an arbitrary probability density `f` satisfying `0<=f<=1`. Put

\[
A=\begin{pmatrix}
\frac12&-\frac12&-\frac1{\sqrt2}\\
-\frac12&\frac12&-\frac1{\sqrt2}\\
-\frac1{\sqrt2}&-\frac1{\sqrt2}&0
\end{pmatrix}
\]

and

\[
Q=(X,Y,Z)A(X,Y,Z)^T.
\]

Then `A` has exact spectrum `{1,1,-1}`, its third physical diagonal entry is exactly zero, and `Q` has a continuous density satisfying

\[
\boxed{
\|p_Q\|_\infty\le 2^{9/4}-1
=3.7568284600108842668\ldots .
}
\tag{1}
\]

In particular, using (P),

\[
\boxed{
\|p_Q\|_\infty
\le 2^{9/4}-1
<3\sqrt2
\le C_*.
}
\tag{2}
\]

Thus an arbitrary fragmented or remote third marginal cannot turn this exact two-heavy zero-pivot geometry into a sharper witness than the diffuse `3 sqrt(2)` obstruction.

Moreover, at the cone tip the optimizing third marginal is exactly the centered unit interval (up to null sets):

\[
\sup_{0\le f\le1,\ \int f=1}p_Q(0)
=2r+2c\log\frac{c}{r^2}
=2.5524125937767022553\ldots,
\tag{3}
\]

where

\[
c=2^{-1/2},\qquad
r=\frac{\sqrt{1+4c}-1}{2}.
\]

The supremum in (3) is attained by `f=1_{[-1/2,1/2]}`.

## 1. Exact target-valid rotated matrix

Let

\[
n=\left(\frac12,\frac12,\frac1{\sqrt2}\right).
\]

Then `|n|=1` and

\[
A=I-2nn^T.
\]

Therefore

\[
A^2=I,
\qquad
\operatorname{tr}A=1,
\]

so its eigenvalues are exactly `{1,1,-1}`. All three eigenvalues have absolute value one. The matrix is not diagonal in the independent physical coordinates, and `A_{33}=0`, so this is a genuine zero-physical-pivot stress family rather than a diagonal control.

Make the orthogonal change in the first two **physical** coordinates

\[
a=\frac{x+y}{\sqrt2},\qquad
b=\frac{x-y}{\sqrt2},\qquad
c=\frac1{\sqrt2}.
\]

The unit square `(x,y) in [-1/2,1/2]^2` becomes the diamond

\[
D=\{(a,b): |a|+|b|\le c\}
\]

with joint density exactly one, because the change has Jacobian one. Direct substitution gives the exact quadratic identity

\[
\boxed{Q=b^2-2aZ.}
\tag{4}
\]

No claim of independence between `a` and `b` is made or needed.

## 2. Conditional density kernel

Fix `z` with `t=|z|>0`. For each fixed `b`, solving

\[
s=b^2-2az
\]

for `a` has derivative magnitude `2t`. The root belongs to the diamond exactly when

\[
\left|\frac{b^2-s}{2z}\right|+|b|\le c,
\]

i.e.

\[
|s-b^2|\le2t(c-|b|).
\]

By the symmetry `b -> -b`, define

\[
L_t(s)=\left|\left\{b\in[0,c]: |s-b^2|\le2t(c-b)\right\}\right|.
\tag{5}
\]

The conditional density of `Q` given `Z=z` is therefore

\[
\boxed{k_t(s)=\frac{L_t(s)}{t}.}
\tag{6}
\]

For each fixed `t>0`, `L_t(s)` is continuous in `s`; this also follows directly from the explicit quadratic endpoints below.

## 3. Exact overlap lemma

### Lemma

For `0<t<=c`,

\[
\boxed{\sup_sL_t(s)=2\sqrt{ct}-t.}
\tag{7}
\]

For `t>=c`, the trivial geometric bound

\[
\boxed{L_t(s)\le c}
\tag{8}
\]

is sufficient.

### Proof

For `b in [0,c]`, write

\[
\ell_t(b)=b^2+2tb-2tc,
\qquad
U_t(b)=b^2-2tb+2tc.
\]

Then the condition in (5) is

\[
\ell_t(b)\le s\le U_t(b).
\tag{9}
\]

The function `ell_t` is strictly increasing, while

\[
U_t(b)=(b-t)^2+s_*,
\qquad
s_*=2tc-t^2.
\]

Assume first `0<t<=c`, so the minimum of `U_t` occurs inside `[0,c]`.

If `s<=s_*`, then `U_t(b)>=s` for all `b`; the admissible set is an initial interval cut only by `ell_t(b)<=s`. Its length is increasing in `s`, hence maximal at `s=s_*`. At that level the endpoint is

\[
b_*=-t+\sqrt{t^2+2tc+s_*}
=2\sqrt{ct}-t.
\tag{10}
\]

Since `t<=c`, one has `t<=b_*<=c`.

Now let `s=s_*+d^2` with `d>0`. The upper condition removes the central interval `(t-d,t+d)` (intersected with `[0,c]`), while the lower condition gives the initial cutoff

\[
b\le b_\ell(d):=-t+\sqrt{4ct+d^2}.
\tag{11}
\]

If `0<d<t` and `b_ell(d)<=t+d`, the surviving length is at most `t-d<=t<=b_*`. If `b_ell(d)>t+d`, its length is at most

\[
b_\ell(d)-2d.
\]

The derivative of this quantity is

\[
\frac{d}{\sqrt{4ct+d^2}}-2<0,
\]

so it is strictly smaller than its value `b_*` at `d=0`.

If `d>=t`, the left component has disappeared and any surviving right component has length at most

\[
b_\ell(d)-t-d.
\]

This is strictly decreasing in `d`, because its derivative is

\[
\frac{d}{\sqrt{4ct+d^2}}-1<0.
\]

At `d=t`, direct squaring gives

\[
\sqrt{4ct+t^2}-3t\le2\sqrt{ct}-t=b_*.
\]

Clipping against either endpoint `0` or `c` can only decrease these lengths. This proves (7). Equation (8) is immediate because the set in (5) lies inside an interval of length `c`. `square`

Combining (6)-(8), define the even decreasing envelope

\[
H(t)=
\begin{cases}
2\sqrt{c/t}-1,&0<t\le c,\\
c/t,&t\ge c.
\end{cases}
\tag{12}
\]

Then

\[
\boxed{k_t(s)\le H(t)\quad\text{for every }s,t.}
\tag{13}
\]

The two formulas agree at `t=c`; both pieces are decreasing. Near zero, `H(t)=O(t^{-1/2})`, so the singularity is integrable against every cap-one density.

## 4. Bathtub step and global bound

Averaging the conditional kernels gives a density representative

\[
p_Q(s)=\int_{\mathbb R}f(z)k_{|z|}(s)\,dz.
\tag{14}
\]

Using (13),

\[
p_Q(s)\le\int f(z)H(|z|)\,dz.
\tag{15}
\]

Because `H(|z|)` is even and nonincreasing in `|z|`, the one-dimensional bathtub principle over all probability densities `0<=f<=1` gives

\[
\int f(z)H(|z|)\,dz
\le\int_{-1/2}^{1/2}H(|z|)\,dz.
\tag{16}
\]

Since `1/2<c=1/sqrt(2)`, only the first line of (12) enters, and

\[
\begin{aligned}
\int_{-1/2}^{1/2}H(|z|)\,dz
&=2\int_0^{1/2}\left(2\sqrt{c/t}-1\right)dt\\
&=8\sqrt{\frac c2}-1\\
&=2^{9/4}-1.
\end{aligned}
\tag{17}
\]

This proves (1).

The strict comparison with the partner obstruction is completely algebraic. Put `u=2^{1/4}>1`. Then

\[
3\sqrt2-(2^{9/4}-1)
=3u^2-4u+1
=(3u-1)(u-1)>0.
\tag{18}
\]

Combining (18) with the completed partner result (P) gives the actual inequality (2).

## 5. Continuity in this scoped family

For every fixed `t>0`, the endpoint description in the overlap lemma shows that `k_t(s)` is continuous in `s`. Equation (13) supplies the common integrable majorant `f(z)H(|z|)`: near zero use `f<=1` and `H(t)=O(t^{-1/2})`, while away from zero use that `f` has total mass one and `H` is bounded. Dominated convergence in (14) therefore proves

\[
\boxed{p_Q\in C_0(\mathbb R).}
\tag{19}
\]

This is a family-level continuous-density theorem only. It does not establish continuity for all QFORM inputs.

## 6. Exact cone-tip optimizer for the arbitrary third law

At `s=0`, (5) reduces to

\[
b^2\le2t(c-b).
\]

Thus

\[
L_t(0)=-t+\sqrt{t^2+2ct}
\]

and

\[
k_t(0)=\sqrt{1+\frac{2c}{t}}-1.
\tag{20}
\]

The right side is strictly decreasing in `t`. A second bathtub application therefore proves that the cone-tip value over all admissible third laws is uniquely maximized (up to null sets) by the centered unit interval.

For that law, the equivalent direct formula is

\[
p_Q(0)=2\int_0^r\log\frac{c-b}{b^2}\,db,
\qquad
r^2+r=c,
\]

which evaluates to

\[
\boxed{
p_Q(0)=2r+2c\log\frac{c}{r^2}
=2.5524125937767022553\ldots .
}
\tag{21}
\]

This is far below both the global envelope (1) and the sharper universal lower obstruction `3 sqrt(2)`.

## 7. What this rules out and what remains

This theorem rules out a broad exact zero-pivot witness mechanism: two fixed macroscopic cap-one interval coordinates coupled through a genuinely rotated `{1,1,-1}` reflection cannot be made sharper by choosing an adversarial third cap-one law, even if that law has infinitely many fragments, unbounded support, or remote phase-aligned pieces. The proof is global in the output level and preserves the original product coordinates throughout.

It does **not** handle adversarial laws simultaneously on the first two coordinates, two or more arbitrary macroscopic shared rows, arbitrary dimension, or arbitrary additional spectrum. Those are the relevant next witness directions. The full QFORM bounded-density conjecture and its full continuity conclusion remain OPEN.

## Deterministic checks

Sibling `verify_twoheavy.py` verifies `A^2=I`, the exact characteristic polynomial, the closed-form constants, and the exact factorization (18). Its recorded output ends `PASS QFORM_TWOHEAVY_ZEROPIVOT_GLOBAL`.
