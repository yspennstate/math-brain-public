SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B15, 2026-09-23T23:28:18Z.
attacking: target-level regularity by testing whether the fixed-instance C0 conclusion admits any uniform continuity or heat-recovery modulus; apply the completed account04/B15 same-constant C0 closure to an actual diagonal target inequality.

# account03/B15 auto28 — no target-uniform continuity modulus, even for A=I_3

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T232818Z-account03-B15-qform-auto28`  
Status: **REGULARITY OBSTRUCTION PROVED / PARTNER APPLIED / FULL QFORM OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Result

The qualitative `C_0` conclusion available for every fixed rank-at-least-three target instance cannot be upgraded to any law-uniform modulus of continuity, even in the easiest fixed diagonal target `A=I_3` with all three input laws compactly supported in the same fixed interval `[1,5]`.

More precisely, for every sufficiently large frequency `s` there is a cap-one probability density `f_s=1_{E_s}` supported in `[1,5]` such that for iid `X_1,X_2,X_3~f_s`,

\[
Q_s=X_1^2+X_2^2+X_3^2
\]

has a canonical density `p_s in C_0(R)` with `||p_s||_infty<=pi`, but, for `h_s=pi/s`,

\[
\boxed{\ \|\tau_{h_s}p_s-p_s\|_\infty\ge {1\over292}.\ }
\tag{1.1}
\]

Since `h_s ->0`, there is no universal function `omega(h)->0` such that every target density satisfies

\[
|p_Q(x+h)-p_Q(x)|\le\omega(|h|).
\]

Hence there is no target-uniform Holder, Lipschitz, Dini, or equicontinuity modulus. This obstruction already holds with the matrix fixed equal to `I_3` and with a fixed compact source window.

There is also no target-uniform sup-norm Gaussian heat recovery. If `gamma_r` is the centered Gaussian density with variance `r^2`, then for every `0<r<=1/pi` one can choose such a target instance with

\[
\boxed{\ \|p_Q-p_Q*\gamma_r\|_\infty>6\times10^{-4}.\ }
\tag{1.2}
\]

Thus fixed-instance continuity is genuinely qualitative; it cannot be used as a hidden uniform regularity input in the universal-height proof.

The unrestricted universal `L^infty` conjecture remains OPEN.

## 2. Source boundary and partner theorem actually used

Fresh owner control was read at brain head `d0cdc27c79c6c84d7c89985849aaf286069bc01e`, OWNER CONTROL revision `2026-09-22.15`. The live programme still marks the full conjecture open and retains the phase-aligned-support correction.

The designated completed partner result used at an actual inequality is account04/B15:

`yspennstate/math-open-problems@7b2b0f54db9acbd23a5f69f715178ab666e22d8e`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B15/20260923T221909Z-account04-B15-ruled-trace-c0-r8/REPORT.md`.

Its Theorem 6.1 says: for a fixed rank-at-least-three target/product instance, once an interval estimate

\[
\Pr\{Q\in I\}\le M|I|
\tag{2.1}
\]

has been proved, the law has a representative `p_Q in C_0(R)` with the identical height constant `||p_Q||_infty<=M`.

For the diagonal form `A=I_3`, the elementary same-sign square convolution gives exactly

\[
\Pr\{Q\in I\}\le\pi |I|.
\tag{2.2}
\]

Applying the partner theorem to the actual inequality (2.2) gives

\[
\boxed{p_Q\in C_0(\mathbb R),\qquad \|p_Q\|_\infty\le\pi.}
\tag{2.3}
\]

The construction below shows that the family of these continuous densities is nevertheless not equicontinuous.

## 3. A unit-mass phase-aligned set inside one fixed compact interval

Let

\[
\chi(u)={\bf1}_{\{\operatorname{dist}(u,2\pi\mathbb Z)\le\pi/3\}}.
\]

It is `2pi`-periodic, has mean `1/3`, and Fourier coefficients

\[
\widehat\chi(k)={\sin(k\pi/3)\over \pi k},\qquad k\ne0.
\tag{3.1}
\]

For `s>0`, define

\[
m_s=\int_1^5\chi(sx^2)\,dx.
\]

For `k!=0`, integration by parts gives

\[
I_k(s):=\int_1^5e^{iksx^2}\,dx
=\left[{e^{iksx^2}\over2iksx}\right]_1^5
+\int_1^5{e^{iksx^2}\over2iksx^2}\,dx,
\]

and hence

\[
|I_k(s)|\le {1\over |k|s}.
\tag{3.2}
\]

Indeed the boundary term contributes at most `(1+1/5)/(2|k|s)=3/(5|k|s)` and the integral contributes at most `(1-1/5)/(2|k|s)=2/(5|k|s)`.

The Fourier series of `chi` converges away from its jump set, and that jump set pulls back to a finite set in `[1,5]` for fixed `s`. Using (3.1)-(3.2), the integrated Fourier series is absolutely summable, so

\[
\left|m_s-{4\over3}\right|
\le\sum_{k\ne0}|\widehat\chi(k)||I_k(s)|
\le {2\over\pi s}\sum_{k=1}^\infty{k^{-2}}
={\pi\over3s}.
\tag{3.3}
\]

Therefore, for every `s>=pi`,

\[
m_s\ge1.
\tag{3.4}
\]

Choose a measurable subset

\[
E_s\subset\{x\in[1,5]:\cos(sx^2)\ge1/2\}
\]

of Lebesgue measure exactly one, and let

\[
f_s={\bf1}_{E_s}.
\tag{3.5}
\]

Then `f_s` is an admissible probability density with `0<=f_s<=1`, compactly supported in the fixed interval `[1,5]`, and

\[
g_s(s):=\int e^{isx^2}f_s(x)\,dx
\]

satisfies

\[
\Re g_s(s)\ge {1\over2},\qquad |g_s(s)|\ge {1\over2}.
\tag{3.6}
\]

This is the phase-aligned-support mechanism from the live correction ledger, now placed inside one fixed compact interval with exact unit mass.

## 4. Failure of every uniform pointwise continuity modulus

Take iid `X_1,X_2,X_3~f_s` and

\[
Q_s=X_1^2+X_2^2+X_3^2.
\]

Its characteristic function factors because the ORIGINAL coordinates remain independent:

\[
\phi_s(t)=\mathbb E e^{itQ_s}=g_s(t)^3.
\]

At the chosen frequency,

\[
|\phi_s(s)|\ge {1\over8}.
\tag{4.1}
\]

By (2.3), the output has a continuous density `p_s` with height at most `pi`. Since every input lies in `[1,5]`,

\[
\operatorname{supp}p_s\subset[3,75].
\tag{4.2}
\]

Put

\[
h_s={\pi\over s}\le1.
\]

For `q_s=\tau_{h_s}p_s-p_s`, the Fourier transform at frequency `s` is

\[
\widehat q_s(s)=(e^{ish_s}-1)\widehat p_s(s),
\]

up to the harmless Fourier-sign convention. Therefore

\[
\|q_s\|_1\ge|\widehat q_s(s)|
=2|\phi_s(s)|\ge {1\over4}.
\tag{4.3}
\]

The union of the supports of `p_s` and its translate has length at most `72+h_s<=73`. Hence

\[
{1\over4}
\le\|q_s\|_1
\le73\|q_s\|_\infty,
\]

which proves

\[
\boxed{\ \|\tau_{h_s}p_s-p_s\|_\infty\ge {1\over292}.\ }
\tag{4.4}
\]

Since `s` can tend to infinity while the matrix remains `I_3` and all source supports remain inside `[1,5]`, the family is not equicontinuous. In particular no universal Holder estimate

\[
|p_Q(x+h)-p_Q(x)|\le C|h|^\alpha
\]

can hold for any `alpha>0`, and no weaker law-uniform modulus tending to zero can hold either.

## 5. Failure of uniform Gaussian heat recovery

Let `gamma_r` be the centered Gaussian density with variance `r^2`. For any `0<r<=1/pi`, set `s=1/r`; then `s>=pi` and the preceding construction applies.

Let

\[
u_s=p_s-p_s*\gamma_r.
\]

At frequency `s`, Gaussian convolution multiplies the Fourier transform by `e^{-r^2s^2/2}=e^{-1/2}`. Therefore, by (4.1),

\[
\|u_s\|_1
\ge|\widehat u_s(s)|
=(1-e^{-1/2})|\phi_s(s)|
\ge {1-e^{-1/2}\over8}
=:c_0.
\tag{5.1}
\]

Now enlarge `[3,75]` to

\[
J=[2,76],\qquad |J|=74.
\]

Outside `J`, `p_s=0`, hence `|u_s|=p_s*\gamma_r`. Since the original support is at distance at least one from `J^c`,

\[
\int_{J^c}|u_s(x)|\,dx
\le\Pr\{|G|\ge1/r\}
=\Pr\{|G|\ge s\}
\le\Pr\{|G|\ge\pi\},
\tag{5.2}
\]

where `G~N(0,1)`. Thus

\[
\int_J|u_s|
\ge {1-e^{-1/2}\over8}-\Pr\{|G|\ge\pi\}.
\tag{5.3}
\]

The bracket is positive; numerically it is approximately `0.04750`. Hence

\[
\|u_s\|_\infty
\ge {1\over74}
\left({1-e^{-1/2}\over8}-\Pr\{|G|\ge\pi\}\right)
>6\times10^{-4}.
\tag{5.4}
\]

This proves (1.2). In particular,

\[
\liminf_{r\downarrow0}
\sup_{\substack{A=I_3\\ f_1=f_2=f_3\le1\\ \operatorname{supp}f_i\subset[1,5]}}
\|p_Q-p_Q*\gamma_r\|_\infty
>0.
\tag{5.5}
\]

So the fixed-instance heat convergence used in earlier B15 reductions cannot be made uniform over the target class. Any successful universal-height proof must obtain its bound before invoking qualitative continuity, not from a target-uniform heat/translation modulus.

## 6. What this does and does not prove

Proved here:

1. Every constructed `Q_s` is an exact owner-target instance: `n=3`, `A=I_3`, and the three eigenvalues all equal one.
2. Each source marginal is an arbitrary rough cap-one probability density, compactly supported in the same fixed interval `[1,5]`.
3. The actual diagonal interval estimate `P(Q_s in I)<=pi|I|` plus the completed account04/B15 theorem gives `p_s in C_0` with `||p_s||_infty<=pi`.
4. Nevertheless, the continuous target densities admit no uniform pointwise continuity modulus and no uniform sup-norm Gaussian heat-recovery modulus.

Not proved here:

- no counterexample to the universal-height conjecture;
- no failure of continuity for any fixed target instance;
- no obstruction to the existing fixed-instance `C_0` theorem;
- no obstruction to using heat kernels as a positive height representation at a fixed scale or after a height estimate is already known.

The first remaining implication for the full problem is still a universal interval/height estimate in the dense product-preserving geometry. This run shows that one should not expect the missing estimate to be supplied by compactness of a uniformly equicontinuous family of output densities.

## 7. Computation check

For reference,

\[
{1-e^{-1/2}\over8}=0.0491836675359\ldots,
\]

\[
\Pr\{|G|\ge\pi\}=0.00168031633653\ldots,
\]

and therefore the explicit heat lower bound in (5.4) is

\[
0.00064193717837\ldots.
\]

These decimals are checks only; the proof uses the exact expressions above.
