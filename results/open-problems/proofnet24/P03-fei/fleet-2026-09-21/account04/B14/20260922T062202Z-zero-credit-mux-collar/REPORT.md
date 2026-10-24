# B14 — a uniform three-dimensional collar around the exact MUX zero-credit lines

**Date:** 22 September 2026  
**Run:** `B14-20260922T061206Z-fei`  
**Classification:** `ESSENTIAL_STEP_APPLIED / ZERO-CREDIT-MUX-COLLAR / FULL_FEI_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`. Authenticated repository sources were used directly; no authenticated installed mathematical-brain receiver/context entered the mathematics.  
**Full uniform-cube FEI:** **OPEN / NOT PROVED.**  
**Publication priority:** unverified; no novelty claim.

## 0. Later-owner precedence and live target

The fresh owner control is revision `2026-09-22.2`. Its later natural-language instruction supersedes the older posterior-crossing-only slot wording where they conflict and converges the FEI fleet on the equivalent all-gate formulation. The older exact physical-restriction identities and counterexamples remain invariants and are not weakened here.

The live source candidate is

\[
C^\dagger=6.521851214,
\qquad C_0=6.4548,
\qquad a^\dagger=4(C^\dagger-C_0)=0.268204856,
\]
\[
\Gamma^\dagger(u)=\Gamma_0(u)+a^\dagger u(1-u).
\]

For a Boolean gate `G` under product bias `p`, write

\[
D_\Gamma(G;p)=
\sum_i {\operatorname{It}_i(G;p)\over V_{p_i}}
[\Gamma(p_i)+h_2(V_{p_i})]
-\Gamma(p_{\rm out})-\widetilde H_G(p),
\qquad V_u=4u(1-u).
\]

A nonnegative `D_{Gamma^dagger}` for every Boolean gate and every product bias would imply full FEI with constant `C^dagger`; that universal statement remains open.

This run changes method from the preceding truth-table transposition calculation. It attacks the exact selector-information interface on the one-bit MUX and proves a quantitative **full-dimensional collar** around both zero-credit lines.

## 1. Exact dependencies consumed

### 1.1 account01/B18 curvature-refunded physical restriction

I read the completed source

`proofnet24/P03-fei/fleet-2026-09-21/account01/B18/20260921T1856Z-curvature-refunded-crossing/REPORT.md`.

In the median-centered gauge it proves, for every physical block `A`,

\[
\mathcal J(g)-\mathbb E_z\mathcal J(g_{A=z})=I_A+C_A,
\tag{1.1}
\]

and for an `F/J`-critical core,

\[
B_A\ge \rho I_A+
\sum_{j\notin A}(\rho+\mathfrak j'(p_j))c_j(A).
\tag{1.2}
\]

**Exact source-to-next-arrow use.** The theorem says that a valid physical-restriction induction may not erase the nonmodular information/crossing refund. In the all-gate MUX cocycle the corresponding nonmodular Boolean information is the exact selector joint credit. The derivation below therefore starts from the source-exact MUX scalar collapse in which that credit has already been retained; at the balanced selector it appears as the signed-overlap/angular term. I use only a sign consequence of that exact term, never a credit-free replacement.

The addressing obstruction to prescribed-coordinate Shannon payment remains active. Nothing below asserts a bound for every prescribed coordinate, and (1.1) is preserved exactly.

### 1.2 account04/B18 exact unequal-MUX joint-credit collapse

I use

`proofnet24/P03-fei/fleet-2026-09-21/account04/B18/20260922T045533Z-mux-joint-credit-collapse/REPORT.md`.

For

\[
M(A;D_0,D_1)=\begin{cases}D_0,&A=0,\\D_1,&A=1,\end{cases}
\]

with selector bias `t` and data biases `q_0,q_1`, its balanced-selector theorem gives, with

\[
a=1-2q_0,\qquad b=1-2q_1,
\qquad \delta={1-ab\over2},
\]

\[
\boxed{
D_\Gamma(M;1/2,q_0,q_1)
=
-\Lambda_\Gamma(q_0,q_1)+C\delta-2
+{a^2+b^2\over2}
\left[1+\Phi\!\left({2|ab|\over a^2+b^2}\right)\right],
}
\tag{1.3}
\]

where

\[
\Lambda_\Gamma(q_0,q_1)
=\Gamma\!\left({q_0+q_1\over2}\right)
-{\Gamma(q_0)+\Gamma(q_1)\over2},
\quad C=\Gamma(1/2),
\]

and

\[
\Phi(x)=
h_2\!\left({1-\sqrt{1-x^2}\over2}\right)
-h_2\!\left({1-x\over2}\right).
\]

Its exact zero-credit locus is

\[
t=1/2,
\qquad q_0=1/2\quad\text{or}\quad q_1=1/2.
\tag{1.4}
\]

The same report gives the general six squared spectral masses

\[
\begin{aligned}
w_\varnothing&=(1-2r)^2,\\
w_A&=V_t(q_1-q_0)^2,\\
w_0&=(1-t)^2V_0,\\
w_1&=t^2V_1,\\
w_{A0}&={V_tV_0\over4},\\
w_{A1}&={V_tV_1\over4},
\end{aligned}
\tag{1.5}
\]

with `r=(1-t)q_0+tq_1`, and the exact defect representation

\[
D_{\Gamma^\dagger}(M)
=dB(t)+(1-t)B(q_0)+tB(q_1)-\Gamma^\dagger(r)-H(w),
\tag{1.6}
\]

where

\[
d=q_0+q_1-2q_0q_1,
\qquad B(u)=\Gamma^\dagger(u)+h_2(V_u).
\]

### 1.3 account01/B18 zero-credit line and source envelope

I use the newest completed scalar frontier

`proofnet24/P03-fei/fleet-2026-09-21/account01/B18/20260922T052537Z-zero-credit-mux-line/REPORT.md`.

It proves for every `s in [0,1]`

\[
Z(s):=C^\dagger-2+{1\over2}\Gamma^\dagger(s)
-\Gamma^\dagger\!\left({1\over4}+{s\over2}\right)>0,
\tag{1.7}
\]

and its piecewise proof actually supplies the uniform lower floor

\[
\boxed{Z(s)\ge z_0:=0.0167628035.}
\tag{1.8}
\]

Indeed `Z(0)=z_0`; the first source-segment branch is increasing from that endpoint, the next branch is above `0.0479544`, and the large-`s` branch is above `0.26545`; symmetry gives the other half.

The same pinned h96 source gives, for `0<z<=1/2`, writing `x=log_2(1/z)`,

\[
\Gamma_0(z)=zG(x),
\]

\[
G(x)<4.9096x+8.629,
\qquad |G'(x)|<31.
\tag{1.9}
\]

These are source bounds, not a newly regenerated candidate.

## 2. A source-valid center Lipschitz bound

We first isolate the only analytic estimate on the candidate needed below.

### Lemma 2.1

On every point whose symmetric representative

\[
z=\min(u,1-u)
\]

satisfies `z>=0.2498`, the live candidate is `66`-Lipschitz:

\[
\boxed{|(\Gamma^\dagger)'(u)|<66}
\tag{2.1}
\]

on every interpolation segment, hence globally by continuity.

### Proof

If `z>=0.2498`, then `x=log_2(1/z)<2.002`. From (1.9), the source interpolation formula, `1/ln2<3/2`, and the quadratic lift,

\[
\begin{aligned}
|(\Gamma^\dagger)'(z)|
&\le |G(x)|+{|G'(x)|\over\ln2}+a^\dagger\\
&<4.9096(2.002)+8.629+{93\over2}+0.268204856\\
&<66.
\end{aligned}
\]

Symmetry gives the same bound above `1/2`. The candidate is continuous and piecewise `C^1`, so the segmentwise bound implies the global Lipschitz estimate. `square`

We also need a crude global bound on `B`. The source envelope gives

\[
\Gamma^\dagger(z)
\le z[4.9096\log_2(1/z)+8.629]+a^\dagger z(1-z).
\]

Since `z log_2(1/z)<0.54` on `(0,1/2]`, `z<=1/2`, and `z(1-z)<=1/4`,

\[
\Gamma^\dagger(z)<7.033.
\]

Therefore

\[
\boxed{0\le B(u)<9\qquad(0\le u\le1).}
\tag{2.2}
\]

The constants are intentionally loose.

## 3. New theorem: a uniform balanced-selector collar around the hard lines

Because both binary entropies occurring in `Phi` lie in `[0,1]`,

\[
\Phi(x)\ge-1,
\]

so the retained Boolean angular term in (1.3) is nonnegative:

\[
{a^2+b^2\over2}[1+\Phi(\cdots)]\ge0.
\tag{3.1}
\]

This simple sign is exactly where the nonmodular selector information from the physical cocycle is retained instead of being replaced by a credit-free scalar bound.

Fix arbitrary `s in [0,1]` and perturb one zero-credit line by

\[
q_0={1\over2}+\varepsilon,
\qquad q_1=s,
\qquad t={1\over2}.
\]

Then `a=-2epsilon`, `b=1-2s`, and

\[
\delta={1\over2}+\varepsilon b.
\]

Let

\[
r_0={1\over4}+{s\over2}.
\]

Subtracting the exact zero-credit value `Z(s)` from (1.3) gives the potential increment

\[
{1\over2}[\Gamma^\dagger(1/2+\varepsilon)-C^\dagger]
-[\Gamma^\dagger(r_0+\varepsilon/2)-\Gamma^\dagger(r_0)],
\]

the scalar increment `C^dagger epsilon b`, and the nonnegative angular reserve.

If

\[
|\varepsilon|\le {1\over4400},
\tag{3.2}
\]

then every candidate argument above has symmetric representative at least

\[
{1\over4}-{1\over8800}>0.2498,
\]

so Lemma 2.1 gives

\[
D_{\Gamma^\dagger}(M;1/2,1/2+\varepsilon,s)
\ge
Z(s)-(66+C^\dagger)|\varepsilon|.
\tag{3.3}
\]

Using (1.8),

\[
\boxed{
D_{\Gamma^\dagger}(M;1/2,1/2+\varepsilon,s)
>
0.0002805645
}
\tag{3.4}
\]

uniformly in `s` whenever (3.2) holds.

By exchanging the two data inputs, the same statement holds with `q_0,q_1` interchanged.

### Theorem 3.1 — balanced-selector zero-credit collar

For arbitrary `q_0,q_1 in [0,1]`, if

\[
t={1\over2},
\qquad
\min\{|q_0-1/2|,|q_1-1/2|\}\le {1\over4400},
\tag{3.5}
\]

then

\[
\boxed{D_{\Gamma^\dagger}(M;t,q_0,q_1)>2.8056\times10^{-4}.}
\tag{3.6}
\]

Boundary biases follow by continuity; the all-gate theorem itself only needs interior points.

This is already a true collar around both exact zero-credit lines inside the balanced-selector plane, with the other data bias completely unrestricted.

## 4. Extend the collar off the balanced selector

We now release `t=1/2`. Keep a point satisfying (3.5), and write

\[
t={1\over2}+\sigma,
\qquad |\sigma|\le10^{-6}.
\tag{4.1}
\]

We compare (1.6) at `t` and at `1/2` without discarding any child defect; selector restriction terminalizes the MUX to literals.

### 4.1 Candidate and leaf-price terms

The address price changes by at most

\[
66|\sigma|+h_2(4\sigma^2),
\tag{4.2}
\]

because `V_t=1-4sigma^2`, `d<=1`, and all center candidate arguments remain in the region of Lemma 2.1.

By (2.2), the data-price mixture changes by at most

\[
9|\sigma|.
\tag{4.3}
\]

The output bias changes by

\[
r-r_0=\sigma(q_1-q_0),
\]

so its potential changes by at most

\[
66|\sigma|.
\tag{4.4}
\]

The collar (3.5) and (4.1) keep the symmetric representative of every output argument above `0.2498`, so the same source Lipschitz bound is valid.

### 4.2 Exact six-mass entropy perturbation

Use (1.5). Relative to `t=1/2`, the six absolute mass changes satisfy

\[
\begin{aligned}
|\Delta w_\varnothing|&\le4|\sigma|,\\
|\Delta w_A|&\le4\sigma^2,\\
|\Delta w_0|+|\Delta w_1|&\le2|\sigma|+2\sigma^2,\\
|\Delta w_{A0}|+|\Delta w_{A1}|&\le2\sigma^2.
\end{aligned}
\]

Hence

\[
\boxed{\|w^t-w^{1/2}\|_1\le6|\sigma|+8\sigma^2,}
\tag{4.5}
\]

so the total variation distance is below `4*10^-6` under (4.1).

Fannes--Audenaert on the six-point alphabet yields

\[
|H(w^t)-H(w^{1/2})|
\le h_2(\delta)+\delta\log_2 5
\le \delta\log_2{5e\over\delta}.
\]

For `delta<=4*10^-6`, `e<3` and `3.75*10^6<2^22`, so

\[
\boxed{|H(w^t)-H(w^{1/2})|<88\times10^{-6}.}
\tag{4.6}
\]

Also

\[
h_2(4\sigma^2)<2\times10^{-10}
\tag{4.7}
\]

for `|sigma|<=10^-6`, using `h_2(x)<=x log_2(e/x)` and `7.5*10^11<2^40`.

Combining (4.2)--(4.7), the total possible decrease in the gate defect from releasing the selector is less than

\[
(66+9+66)10^{-6}+88\times10^{-6}+2\times10^{-10}
<0.0002290002.
\tag{4.8}
\]

Subtract this from (3.4).

### Theorem 4.1 — full three-dimensional zero-credit collar

For every one-bit MUX with

\[
\boxed{
\left|t-{1\over2}\right|\le10^{-6},
\qquad
\min\{|q_0-1/2|,|q_1-1/2|\}\le {1\over4400},
}
\tag{4.9}
\]

and arbitrary value of the other data bias,

\[
\boxed{
D_{\Gamma^\dagger}(M;t,q_0,q_1)
>5.15\times10^{-5}>0.
}
\tag{4.10}
\]

Thus the live candidate is rigorously safe on a genuine three-dimensional open collar around **both** exact selector-zero-credit lines. The collar is uniform along the entire line; it is not a finite grid and does not require the other data bias to be complementary, near-complementary, or bounded away from the endpoints.

## 5. Relation to the newest MUX tubes

The newest account04/B18 theorem proves a different three-parameter tube around the complementary-data surface,

\[
|t-1/2|\le q^2/8192,
\qquad |q_1-(1-q_0)|\le q^2/2^{18},
\]

with a quantitative margin reserve. Theorem 4.1 above is complementary geometry: it surrounds the **two exact zero-information-credit lines** uniformly in the unconstrained data coordinate. Neither theorem contains the other.

The current MUX obstruction is therefore pushed into the region simultaneously separated from

1. the complementary-data tube already certified by account04/B18, and
2. the two zero-credit collars (4.9).

The next source-valid step is to lower-bound the exact selector credit on the remaining compact region and intersect that floor with account04/B12's simultaneous negative data-pivot residual conditions. That is a finite-dimensional analytic/interval target, not a return to prescribed-coordinate payment.

## 6. Preserved exclusions and exact status

* The known addressing obstruction to prescribed-coordinate Shannon payment remains intact.
* The exact centered block drift remains
  \[
  \mathcal J-\mathbb E\mathcal J_{\rm child}=I_A+C_A.
  \]
* No every-coordinate payment is asserted.
* No nonmodular Boolean information term is silently deleted; the balanced proof starts from the exact joint-credit collapse and retains its angular reserve.
* No benchmark gold, mock proof, paid/remote compute, workflow dispatch, email/Drive, unrelated private data, notification change, or permission change is used.
* Full uniform-cube FEI remains **OPEN / NOT PROVED**.
* Execution is `WITHOUT_VERIFIED_BRAIN`.

## 7. Old/new missing implication

**Before this run:** account01/B18 had closed the exact zero-credit lines and explicitly asked for a quantitative collar around them; account04/B18 had separately opened a small genuinely unequal-data tube around complementary data.

**New proved implication:** the current candidate is safe on the explicit uniform collar (4.9), with defect reserve (4.10).

**New first missing implication:** on the compact MUX region outside the complementary tube and outside both zero-credit collars, prove that the exact selector credit plus the two data-pivot cross-deficit constraints force nonnegative defect, or exhibit a source-valid negative point. Closing the full MUX remains strictly weaker than closing arbitrary composition-prime gates.

**Full FEI:** open / not proved.
