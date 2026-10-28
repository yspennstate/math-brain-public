SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B17, 2026-09-23T12:03:07Z.
attacking: the unpaid low-cross-rank/two-diffuse-bank stress family globally in the output level, including off-tip peaks.

# Global exclusion for the singleton plus two opposite diffuse banks

Status: `SUPPORTING_ANALYTIC_WITNESS_CONSTRAINT`; the full QFORM conjecture remains OPEN / NOT PROVED. The full-target continuity conclusion remains OPEN. This report proves a global, level-uniform theorem for one exact nonseparable source-valid family and applies the completed `account04/B17` weighted local Edgeworth theorem to an actual norm inequality.

## 1. Exact finite-dimensional target family

For every integer `m>=3`, let

\[
A_m=[1]\oplus J_m/m\oplus(-J_m/m).
\]

The nonzero spectrum is exactly `\{1,1,-1\}`. Every disjoint physical-coordinate cross block of `A_m` has rank at most two: the singleton contributes no cross entry and each `J_m/m` bank contributes rank at most one. Thus this is an exact stress family for any attempted proof that needs a rank-three physical cross block.

Let `X_m` have an arbitrary probability density `0<=f_m<=1`, and let all variables in the two `m`-coordinate banks be independent `Unif[-1/2,1/2]`, independent also of `X_m`. Put

\[
S_m=m^{-1/2}\sum_{j=1}^m U_j,\qquad
T_m=m^{-1/2}\sum_{j=1}^m V_j.
\]

Then

\[
Q_m=X_m^2+S_m^2-T_m^2.
\tag{1}
\]

No assumption is made on the support, moments, connectedness, symmetry, or centering of the heavy law `X_m`.

## 2. Sharp cap-one square estimate

If `H=X^2` and `X` has density `f<=1`, then for `u>0`

\[
h(u)={f(\sqrt u)+f(-\sqrt u)\over2\sqrt u}\le u^{-1/2}.
\]

Moreover

\[
\int_0^\infty h(u)^{3/2}\,du
\le {1\over\sqrt2}\int_{\mathbb R}f(x)^{3/2}|x|^{-1/2}\,dx
\le {1\over\sqrt2}\sup_{0\le f\le1,\ \int f=1}\int f(x)|x|^{-1/2}dx=2\sqrt2,
\]

where the last bathtub extremizer is `1_{[-1/2,1/2]}`. Hence

\[
\boxed{\|h\|_{3/2}\le2.}
\tag{2}
\]

This estimate is uniform over arbitrary fragmented cap-one heavy laws.

## 3. Apply the completed partner local Edgeworth theorem

Let `g_m` be the density of `S_m`, let `v=1/12`, and let `\gamma_v` denote the `N(0,v)` density. The completed `account04/B17` result proves, with a polynomially weighted integrable remainder,

\[
g_m(y)=\gamma_v(y)\left[1-{1\over20m}H_4(y/\sqrt v)\right]
+O(m^{-2})(1+|y|)^{-8}.
\tag{3}
\]

Partner source: `yspennstate/math-open-problems@2156b76156ad5956c214a881fcfd6d977d6f3b9f`, path `proofnet24/QFORM-density/fleet-2026-09-22/account04/B17/20260922T211900Z-account04-B17-QFORM-r3/REPORT.md`.

Let `a_m` be the density of `S_m^2`, and let `a` be the density of `G^2` for `G~N(0,v)`. Since `g_m` and `\gamma_v` are even,

\[
\|a_m-a\|_{3/2}^{3/2}
=2\int_0^\infty |g_m(y)-\gamma_v(y)|^{3/2}y^{-1/2}\,dy.
\]

Equation (3) therefore gives

\[
\boxed{\|a_m-a\|_{3/2}=O(m^{-1}).}
\tag{4}
\]

The weight `y^{-1/2}` is locally integrable and the partner's polynomially weighted remainder controls the tail, so no pointwise van-der-Corput estimate is used.

Let

\[
k_m=a_m*\widetilde a_m,
\qquad
k=a*\widetilde a,
\]

where `\widetilde a(t)=a(-t)`. These are the densities of `S_m^2-T_m^2` and `G^2-H^2`, respectively, for independent `G,H~N(0,v)`. Young's inequality and (4) imply

\[
\boxed{
\|k_m-k\|_3
\le(\|a_m\|_{3/2}+\|a\|_{3/2})\|a_m-a\|_{3/2}
=O(m^{-1}).
}
\tag{5}
\]

If `h_m` is the density of `X_m^2`, then by (2) and another Young inequality,

\[
\boxed{
\|p_{Q_m}-h_m*k\|_\infty
\le\|h_m\|_{3/2}\|k_m-k\|_3
=O(m^{-1}),
}
\tag{6}
\]

uniformly over the arbitrary heavy law. This is the actual inequality to which the completed partner theorem is applied.

## 4. Exact Gaussian difference kernel

Since `(G-H)` and `(G+H)` are independent `N(0,2v)`, their product has density

\[
k(t)={1\over2\pi v}K_0\!\left({|t|\over2v}\right)
={6\over\pi}K_0(6|t|).
\tag{7}
\]

Using

\[
K_0(z)=\int_0^\infty e^{-z\cosh r}\,dr,
\qquad \cosh r\ge e^r/2,
\]

we obtain the rigorous envelope

\[
K_0(z)\le\int_0^\infty e^{-(z/2)e^r}\,dr=E_1(z/2),
\]

hence

\[
\boxed{k(t)\le {6\over\pi}E_1(3|t|).}
\tag{8}
\]

Here `E_1(z)=\int_z^\infty e^{-u}du/u`.

For every output level `s`,

\[
(h_m*k)(s)=\int_{\mathbb R}f_m(x)k(s-x^2)\,dx.
\]

Because `E_1` is strictly decreasing, bathtub rearrangement says that the right side of the envelope (8) is maximized over `0<=f<=1`, `\int f=1`, by taking the unit-measure set on which `|x^2-s|` is smallest. We now bound that optimum uniformly in `s`.

## 5. Layer-cake formula for the exact bathtub problem

For `s>=0`, define

\[
m_s(\delta)=|\{x:|x^2-s|\le\delta\}|.
\]

Then

\[
m_s(\delta)=
\begin{cases}
2(\sqrt{s+\delta}-\sqrt{s-\delta}),&0\le\delta<s,\\
2\sqrt{s+\delta},&\delta\ge s.
\end{cases}
\tag{9}
\]

If `E_s` is the bathtub-optimal unit-measure set, layer cake gives

\[
U(s):={6\over\pi}\int_{E_s}E_1(3|x^2-s|)dx
={6\over\pi}\int_0^\infty \min(1,m_s(\delta))e^{-3\delta}{d\delta\over\delta}.
\tag{10}
\]

For `s<0`, the optimal set is `[-1/2,1/2]` and `U(s)<=U(0)`.

### 5.1. The vertex level

At `s=0`, the saturation threshold is `\delta=1/4`, so

\[
U(0)={6\over\pi}E_1(3/4)
+4\sqrt{3/\pi}\,\operatorname{erf}(\sqrt3/2).
\tag{11}
\]

A fully elementary rational estimate gives

\[
E_1(3/4)<0.348,
\qquad
4\sqrt{3/\pi}\,\operatorname{erf}(\sqrt3/2)
< {24\cdot57177\cdot50\over143360\cdot157}.
\]

For the first inequality use

\[
E_1(x)=-\gamma-\log x+\sum_{j\ge1}{(-1)^{j+1}x^j\over j\,j!},
\]

`\gamma>0.57`, `\log(4/3)<0.288`, and the alternating sum through its positive fifth term `<0.63`. The elementary bound `\gamma>0.57` follows, for example, from `\gamma>H_{20}-\log20-1/40`, `\log20<3`, and the exact value of `H_{20}`. For the error function, truncate its alternating series after the positive `x^9` term at `x=\sqrt3/2`; the resulting bracket is `(57177/143360)\sqrt3`. Using `\pi>157/50` gives

\[
\boxed{U(0)<3.714.}
\tag{12}
\]

### 5.2. Levels `0<=s<=1/8`

Here the optimal unit-measure set is again `[-1/2,1/2]`. Put `u=1/4-s` and

\[
C=\int_0^1{\sqrt{1+r}-\sqrt{1-r}\over r}\,dr
=2(\sqrt2-\operatorname{arsinh}1)<1.1.
\]

Splitting (10) over `[0,s]`, `[s,u]`, `[u,\infty)` and using

\[
2\sqrt{s+\delta}\le2\sqrt\delta+s/\sqrt\delta
\]

on `[s,u]` gives `U(s)<=(6/\pi)V(s)` with

\[
V(s)=2C\sqrt s+
\int_s^u(2\delta^{-1/2}+s\delta^{-3/2})e^{-3\delta}d\delta
+E_1(3u).
\]

Integration by parts in the `s\delta^{-3/2}` term yields

\[
V(s)-V(0)
\le\sqrt s\left(2C+2e^{-3s}-4\int_0^1e^{-3sy^2}dy\right)+T(u),
\tag{13}
\]

where

\[
T(u)=\int_u^{1/4}e^{-3\delta}(\delta^{-1}-2\delta^{-1/2})d\delta.
\]

Using `e^{-3s}<=1-3s+(9/2)s^2`, `\int_0^1e^{-3sy^2}dy>=1-s`, `C<1.1`, `\sqrt{s}<0.354`, and `u\in[1/8,1/4]`,

\[
\sqrt s(\cdots)<0.071,
\qquad
T(u)\le\log2-2+\sqrt2<0.109.
\]

Thus `V(s)-V(0)<0.180`; with `6/\pi<300/157` and (12),

\[
\boxed{U(s)<4.057\qquad(0\le s\le1/8).}
\tag{14}
\]

### 5.3. Levels `s>=1/8`

Now `E_s` is the union of two symmetric intervals `[-a,-b]\cup[b,a]` with `a-b=1/2` and `r=\sqrt s\in[b,a]`. On `[b,a]`,

\[
|x^2-s|=|x-r|(x+r)\ge r|x-r|\ge {1\over2\sqrt2}|x-r|.
\]

One-dimensional symmetric rearrangement on an interval of length `1/2` therefore gives, with `c=3/(2\sqrt2)`,

\[
U(s)\le {24\over\pi}\int_0^{1/4}E_1(cy)dy.
\tag{15}
\]

The exact antiderivative is

\[
\int_0^L E_1(cy)dy=L E_1(cL)+{1-e^{-cL}\over c}
\le L(E_1(cL)+1).
\]

Here `cL=3/(8\sqrt2)`. The alternating expansion for `E_1`, together with `\gamma>1/2`, `\log4<1.4`, and `3/(8\sqrt2)<0.266`, gives `E_1(cL)<1.166`. Therefore, again using `\pi>157/50`,

\[
\boxed{U(s)<{3249\over785}=4.1388536\ldots<4.14\qquad(s\ge1/8).}
\tag{16}
\]

Combining (12), (14), and (16), and recalling the negative-level comparison,

\[
\boxed{
\sup_{0\le f\le1,\ \int f=1}\|p_{X^2+G^2-H^2}\|_\infty<4.14.
}
\tag{17}
\]

Since `\sqrt2>7/5`,

\[
4.14<4.2<3\sqrt2.
\tag{18}
\]

Thus the entire limiting family lies a strict distance below the known sharp obstruction.

## 6. Uniform finite-bank consequence and partner comparison

Combining (6) and (17), uniformly over arbitrary `m`-dependent cap-one heavy laws,

\[
\boxed{
\limsup_{m\to\infty}\sup_{0\le f_m\le1,\ \int f_m=1}
\|p_{X_m^2+S_m^2-T_m^2}\|_\infty\le4.14<3\sqrt2.
}
\tag{19}
\]

The same completed `account04/B17` report supplies the exact genuinely rotated source-valid witness

\[
p_{Q_m^{\rm partner}}(0)=3\sqrt2\left(1-{5295\over21952m}+O(m^{-2})\right),
\]

so every universal constant satisfies `C_*>=3\sqrt2`. Consequently

\[
\boxed{
\limsup_m\sup_{f_m}\|p_{Q_m}\|_\infty
\le4.14<3\sqrt2\le C_*.
}
\tag{20}
\]

This is a global off-tip exclusion, not merely a cone-tip calculation: no output level in the singleton-plus-two-opposite-diffuse-bank architecture can asymptotically realize the present `3\sqrt2` lower bound.

## 7. Continuity in this scope

The limit kernel `k` belongs to `L^3` because `K_0` has only a logarithmic singularity at zero and exponential decay at infinity. Equation (2) gives `h_m\in L^{3/2}`. Hence `h_m*k` is uniformly continuous: translation continuity in `L^3` and Hoelder give

\[
|(h_m*k)(s+t)-(h_m*k)(s)|
\le\|h_m\|_{3/2}\|\tau_tk-k\|_3\to0.
\]

For `m>=3`, the same argument with `k_m\in L^3` gives continuity of the finite-family output density even for arbitrary merely measurable cap-one heavy densities. This is only family-level continuity; the owner's full-target continuity conclusion remains open.

## 8. Scope and next sharp-witness mechanism

The theorem is exact for `A_m=[1]\oplus J_m/m\oplus(-J_m/m)` and arbitrary cap-one heavy `X_m`, with both diffuse banks built from independent centered unit intervals. It does not control arbitrary low-cross-rank matrices or arbitrary laws in the diffuse banks, and therefore is not a proof of full QFORM.

What it does remove is a natural unresolved stress mechanism: an arbitrary macroscopic coordinate plus two opposite minimum-variance diffuse banks, including all off-tip peaks and arbitrarily fragmented heavy support. A witness above `3\sqrt2`, if one exists, must leave this architecture, for example by retaining several non-collinear mesoscopic physical rows or by making the surviving non-Gaussian component interact nontrivially with more than one diffuse spectral mode.


Execution status: `WITHOUT_VERIFIED_BRAIN`; repository retrieval and durable writes are genuine, but no authenticated native learned-memory receiver-use event was observed.