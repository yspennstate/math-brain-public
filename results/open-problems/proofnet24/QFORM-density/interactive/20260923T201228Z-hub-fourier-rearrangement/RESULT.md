# A Fourier Rearrangement Criterion for Quadratic Form Densities

## Abstract

We prove a sufficient condition on the characteristic function of an independent linear variable for a dimension-free density bound for an indefinite quadratic form. The other coordinates may have arbitrary probability densities bounded by one, with unrestricted diagonal coefficients and an unrestricted coupled linear statistic. The condition is an explicit Lorentz integral with exponent $3/2$. It yields bounded continuous densities for infinitely fragmented laws whose interval lengths decrease like $j^{-r}$, for every $r>3/2$. An example with interval lengths $6/(\pi^2j^2)$ gives a density bound less than $34$, uniformly in the leakage parameter of the rank-three model. This example admits no finite interval majorant of the type used in the earlier interval-cover estimate.

The unrestricted dimension-free conjecture remains open. In particular, the Fourier condition proved here does not follow from a density bound alone.

## 1. The quadratic form and the Fourier criterion

Let $H,X_1,\ldots,X_m$ be independent real random variables with probability densities bounded by one. Write $X=(X_1,\ldots,X_m)$. Let $w,v\in\mathbb R^m$ satisfy
$
 |w|=|v|=1,\qquad w\cdot v=0,\qquad
 w_i^2+v_i^2\le\frac12\quad(1\le i\le m).
$
Put $L=w\cdot X$ and $V=v\cdot X$. Consider
$
 Q=2H(L+\beta)+\lambda V^2+2L(q\cdot X)
       +\sum_{i=1}^m(d_iX_i^2+b_iX_i+c_i),
 \qquad \lambda\ne0.                                      \tag{1}
$
Here $\beta,q,d_i,b_i,c_i$ are unrestricted. There is no $H^2$ term.

Use the Fourier convention
$
 \widehat f(\xi)=\int_{\mathbb R}e^{i\xi x}f(x)\,dx.
$
For a nonnegative measurable function $\psi$ on $\mathbb R$, let $\psi^*$ denote its nonincreasing rearrangement with respect to Lebesgue measure, and define
$
 \mathcal L(\psi)=\int_0^\infty u^{-1/3}\psi^*(u)\,du.       \tag{2}
$
This fixes the normalization of the $L^{3/2,1}$ Lorentz quantity used below.

**Theorem 1.** Let $\psi=|\widehat f_H|$. If $\mathcal L(\psi)<\infty$, then $Q$ has a continuous density vanishing at infinity, and
$
 \boxed{\;
 \|p_Q\|_\infty\le
 \frac{2^{1/3}e^{2/3}}{\pi^{2/3}}\,
 |\lambda|^{-1/3}\mathcal L(\psi).
 \;}                                                       \tag{3}
$
The numerical multiplier before $|\lambda|^{-1/3}\mathcal L(\psi)$ is less than $1.145$. The estimate is independent of the dimension, the locations of the supports, all moments, and all the coefficients in (1) other than $\lambda$.

The proof actually needs only independence and the Fourier condition for $H$; its density cap is included to keep the hypotheses within the original product-measure problem.

### 1.1. A sharper frozen-slice estimate

We first record the constants in the analytic input. For a complex function $g$ with $|g|\le f$, where $f\le1$ is a probability density, sharp Hausdorff–Young gives, for $p\ge2$,
$
 \int_{\mathbb R}|\widehat g(\xi)|^p\,d\xi
 \le \frac{2\pi}{\sqrt p}
       \left(\frac p{p-1}\right)^{(p-1)/2}
 \le \frac{2\pi\sqrt e}{\sqrt p}.                           \tag{4}
$
Indeed $\|g\|_{p'}\le1$, and the first inequality is exactly the sharp Hausdorff–Young constant in the stated Fourier convention.

Let $u_i=(w_i,v_i)$ and $a_i=|u_i|^2$. The geometric Brascamp–Lieb inequality, using
$\sum_i u_iu_i^{\mathsf T}=I_2$ and $a_i\le1/2$, implies
$
 \int_{\mathbb R^2}\prod_i
  |\widehat g_i(zw_i+uv_i+s_i)|\,dz\,du
 \le (2\pi\sqrt e)^2.                                      \tag{5}
$
For clarity, the factor belonging to row $i$ in this application is
$
 \left(a_i^{-1/2}
       \int|\widehat g_i(\xi)|^{1/a_i}\,d\xi\right)^{a_i}
 \le(2\pi\sqrt e)^{a_i}.
$
Zero rows can be omitted, and $\sum_i a_i=2$. Translations $s_i$ do not affect the scalar integrals.

For a fixed real number $a$, put
$
 Y_a=\lambda V^2+2a(q\cdot X)
           +\sum_i(d_iX_i^2+b_iX_i+c_i).
$
Let $\mu_{a,\ell}$ be the unnormalized slice of the joint law of
$(L,Y_a)$ at $L=\ell$. Its total mass is $\rho_L(\ell)$, where $\rho_L$ is the density of $L$.

Fresnel linearization in $V$, (5), and Fourier inversion in $L$ give, for each fixed $a$, for almost every $\ell$,
$
 |\widehat\mu_{a,\ell}(t)|
 \le\min\left\{\rho_L(\ell),
          \frac{e\sqrt\pi}{\sqrt{|t\lambda|}}\right\},
 \qquad t\ne0.                                             \tag{6}
$
To check the constant, the Fresnel prefactor is
$(4\pi|t\lambda|)^{-1/2}$; multiplying by (5) and then by
$(2\pi)^{-1}$ for the inversion in $L$ gives
$e\sqrt\pi/\sqrt{|t\lambda|}$. All operations can first be carried out with Gaussian damping. The integrable bound (5) permits its removal. The disintegration identifies the slice transform almost everywhere; for the application below, a common null set for each countable set of frozen parameters suffices.

### 1.2. Freezing without an exceptional-slice substitution

Set
$
 A=\frac{e\sqrt\pi}{\sqrt{|\lambda|}}.
$
Partition the $L$-axis into intervals of length $h$, and let $L_h$ be a chosen endpoint of the interval containing $L$. Replace only the leakage term $2L(q\cdot X)$ by $2L_h(q\cdot X)$ in (1), obtaining $Q_h$.

For a fixed $h$, only countably many frozen parameters occur. Integrate $H$ first and then apply (6) on each cell. This gives
$
 |\varphi_{Q_h}(t)|
 \le\int_{\mathbb R}
   \psi(2t(\ell+\beta))
   \min\{\rho_L(\ell),A|t|^{-1/2}\}\,d\ell.                 \tag{7}
$
There is no substitution of a varying parameter into an almost-everywhere statement. Since $Q_h\to Q$ almost surely, bounded convergence proves (7) with $Q_h$ replaced by $Q$.

### 1.3. Rearrangement and the critical exponent

If $0\le w\le b$ and $\int w\le1$, the bathtub principle gives
$
 \int w(x)\Psi(x)\,dx
 \le b\int_0^{1/b}\Psi^*(u)\,du.
$
Apply this to (7), with $b=A|t|^{-1/2}$. If
$
 F(r)=\int_0^r\psi^*(u)\,du,
$
then scaling and translation of the argument of $\psi$ give
$
 |\varphi_Q(t)|
 \le\frac{A}{2|t|^{3/2}}\,
       F\!\left(\frac{2|t|^{3/2}}A\right).                 \tag{8}
$
The right side is at most one because $\psi\le1$.

Use $r=2t^{3/2}/A$ on the positive half-line and then Tonelli:
$
\begin{aligned}
 \int_{\mathbb R}|\varphi_Q(t)|\,dt
 &\le\frac43\left(\frac A2\right)^{2/3}
          \int_0^\infty F(r)r^{-4/3}\,dr\\
 &=4\left(\frac A2\right)^{2/3}
          \int_0^\infty\psi^*(u)u^{-1/3}\,du.
\end{aligned}                                               \tag{9}
$
Fourier inversion now proves continuity, vanishing at infinity, and
$
 \|p_Q\|_\infty
 \le\frac2\pi\left(\frac A2\right)^{2/3}\mathcal L(\psi),
$
which is (3). This proves Theorem 1.

## 2. A fractional Sobolev condition

The following criterion makes Theorem 1 applicable without estimating the rearrangement directly.

**Proposition 2.** Suppose $1/6<s<1/2$ and
$
 W_s(f_H)=\int_{\mathbb R}
       (1+|\xi|^{2s})|\widehat f_H(\xi)|^2\,d\xi<\infty.
$
Then
$
 \mathcal L(|\widehat f_H|)
 \le
 \left[
 \frac{2^{1/3}\pi}{2s\sin(\pi/(6s))}\,W_s(f_H)
 \right]^{1/2}.                                            \tag{10}
$

**Proof.** Rearrangement against the increasing weight gives
$
 \int_0^\infty
      \left(1+(u/2)^{2s}\right)\psi^*(u)^2\,du
 \le W_s(f_H).                                             \tag{11}
$
For example, the weighted part follows by layer cake from the fact that a centered interval minimizes
$\int_E|\xi|^{2s}\,d\xi$ among sets of prescribed measure.

Cauchy–Schwarz in (2) now proves (10), because
$
 \int_0^\infty
   \frac{u^{-2/3}}{1+(u/2)^{2s}}\,du
 =\frac{2^{1/3}\pi}{2s\sin(\pi/(6s))}.                     \tag{12}
$
The integral at infinity converges precisely when $s>1/6$. The beta integral evaluates it as displayed. ∎

The regularity condition is imposed only on the single hub law. No regularity is imposed on any of the light coordinate densities.

## 3. Infinitely many support intervals

Let $I_j$ be disjoint intervals of lengths $\ell_j>0$, with
$\sum_j\ell_j=1$, and let
$
 f_H=\mathbf1_{\bigcup_j I_j}.
$
Their locations are arbitrary. For $0<s<1/2$, define
$
 S_s=\sum_j\ell_j^{\,1-2s}.
$

**Proposition 3.** If $S_s<\infty$ for some $s>1/6$, then Theorem 1 applies, and
$
 W_s(f_H)\le
 2\pi+
 \frac{2\Gamma(1+2s)\sin(\pi s)}{s(1-2s)}\,S_s.            \tag{13}
$
Consequently, if
$
 \ell_j=\frac{j^{-r}}{\zeta(r)},\qquad r>\frac32,
$
then every form (1) has a bounded continuous density with a bound depending only on $r$ and $|\lambda|$. In particular, the bound is independent of the number and positions of the support components and of all the other coefficients of (1).

**Proof.** Let $f=f_H$. Since $f$ is an indicator,
$
 \|f(\cdot+h)-f\|_2^2
 =\|f(\cdot+h)-f\|_1
 \le 2\sum_j\min\{|h|,\ell_j\}.
$
It follows by Tonelli that
$
 \int_{\mathbb R}
   \frac{\|f(\cdot+h)-f\|_2^2}{|h|^{1+2s}}\,dh
 \le \frac{2}{s(1-2s)}
             \sum_j\ell_j^{\,1-2s}.                       \tag{14}
$
Plancherel and another application of Tonelli give
$
 \int_{\mathbb R}
   \frac{\|f(\cdot+h)-f\|_2^2}{|h|^{1+2s}}\,dh
 =\frac{1}{\Gamma(1+2s)\sin(\pi s)}
      \int_{\mathbb R}|\xi|^{2s}|\widehat f(\xi)|^2\,d\xi.
                                                                  \tag{15}
$
Here we used
$
 \int_{\mathbb R}\frac{1-\cos u}{|u|^{1+2s}}\,du
 =\frac{\pi}{\Gamma(1+2s)\sin(\pi s)}.
$
This identity also follows directly by a Laplace integral for
$|u|^{-1-2s}$. Since $\|f\|_2^2=1$, equations (14)–(15) prove (13).

For the polynomial lengths, choose
$
 \frac16<s<\frac{1-1/r}{2}.
$
Such an $s$ exists exactly when $r>3/2$, and then
$r(1-2s)>1$, so $S_s<\infty$. Apply Proposition 2 and Theorem 1. ∎

This is a sufficient threshold for this argument. No necessity statement about the quadratic-form density is asserted when $r\le3/2$.

## 4. An explicit rank-three example with density less than 34

Set
$
 c=\frac6{\pi^2},\qquad
 I_j=[10^j,\,10^j+cj^{-2}],\qquad
 f_H=\sum_{j=1}^\infty\mathbf1_{I_j}.                       \tag{16}
$
This is a probability density bounded by one. It has infinitely many support components, infinite total variation, and infinite first moment.

Take $s=1/5$. Then
$
 S_s=c^{3/5}\zeta(6/5),
$
and (10)–(13) imply
$
 \|p_Q\|_\infty\le C_{\rm ex}|\lambda|^{-1/3},
$
where the explicit constant is
$
\begin{aligned}
 C_{\rm ex}
 &=
 \frac{2^{1/3}e^{2/3}}{\pi^{2/3}}
 \left[
 5\pi\,2^{1/3}
 \left(
 2\pi+\frac{50}{3}\Gamma(7/5)\sin(\pi/5)
                c^{3/5}\zeta(6/5)
 \right)
 \right]^{1/2}\\
 &\approx 33.116<34.                                      \tag{17}
\end{aligned}
$
A simple upper bound sufficient to verify $C_{\rm ex}<34$ is
$
 \zeta(6/5)
 \le1+2^{-6/5}+\int_2^\infty x^{-6/5}\,dx
 =1+2^{-6/5}+5\,2^{-1/5};
$
inserting this upper bound in (17) gives less than $33.608$.

In particular, let $w,v,p$ be orthonormal light vectors, retain
$w_i^2+v_i^2\le1/2$, and put $P=p\cdot X$. For
$
 Q_\varepsilon=2HL+V^2+2\varepsilon LP,\qquad
                         \varepsilon\in\mathbb R,
$
we have
$
 \boxed{\quad
 \sup_{\varepsilon\in\mathbb R}\|p_{Q_\varepsilon}\|_\infty<34
 \quad}                                                    \tag{18}
$
for the hub law (16) and every admissible choice of the independent light laws.

The nonzero eigenvalues of the matrix of $Q_\varepsilon$ are
$
 1,\qquad \sqrt{1+\varepsilon^2},\qquad
             -\sqrt{1+\varepsilon^2}.
$
Thus this is a family inside the original three-large-eigenvalue problem. The conclusion includes uniformity as $\varepsilon\to0$. No light statistic is treated as independent of another light statistic.

### 4.1. Why the earlier interval-cover theorem cannot give this example

The earlier sufficient condition was an interval majorant
$
 f_H\le\sum_k a_k\mathbf1_{J_k},\qquad
 a_k\ge0,\qquad
 \sum_k a_k|J_k|^{1/3}<\infty.                              \tag{19}
$
For (16), even an arbitrary choice of overlapping intervals and weights cannot satisfy (19).

To prove this, put $\ell_j=cj^{-2}$ and define the locally finite measure
$
 \nu(dx)=\sum_j\ell_j^{-2/3}\mathbf1_{I_j}(x)\,dx.
$
For every bounded interval $J$,
$
 \nu(J)\le |J|^{1/3}.                                      \tag{20}
$
If $J$ meets only one $I_j$, this follows from
$
 \ell_j^{-2/3}\min\{|J|,\ell_j\}\le|J|^{1/3}.
$
If it meets at least two support intervals, let $b\ge2$ be the largest index it meets. Then
$
 |J|\ge 8\cdot10^{b-1},\qquad
 \nu(J)\le\sum_{j\le b}\ell_j^{1/3}\le b
            \le(8\cdot10^{b-1})^{1/3}.
$
This proves (20).

On the other hand,
$
 \int f_H\,d\nu=\sum_j\ell_j^{1/3}
              =c^{1/3}\sum_jj^{-2/3}=\infty.
$
Integrating a putative majorant (19) against $\nu$, which is absolutely continuous, and applying Tonelli and (20), would give
$
 \infty\le\sum_k a_k\nu(J_k)
       \le\sum_k a_k|J_k|^{1/3}<\infty,
$
a contradiction. Thus Theorem 1 covers an explicit law outside the previous interval-majorant class.

## 5. The Fourier condition is not automatic

The critical Fourier quantity in (2) is not uniformly bounded over cap-one probability densities. This prevents (3), by itself, from completing the unrestricted problem.

For an integer $N\ge1$, take
$
 f_N(x)=\sum_{j=1}^N
   \mathbf1_{[2\pi3^j,\,2\pi3^j+1/N]}(x).
$
These are genuine one-dimensional probability densities bounded by one. Their characteristic functions satisfy
$
 |\widehat f_N(\xi)|
 =
 \left|\frac{\sin(\xi/(2N))}{\xi/(2N)}\right|
 \frac1N\left|\sum_{j=1}^N e^{2\pi i3^j\xi}\right|.        \tag{21}
$
Let $S_N(\xi)$ denote the sum in (21). On a period of length one,
$
 \int_0^1|S_N|^2\,d\xi=N,\qquad
 \int_0^1|S_N|^4\,d\xi=2N^2-N.
$
The second identity follows because base-three representation makes the unordered pair $\{j,k\}$ uniquely determined by $3^j+3^k$. Paley–Zygmund therefore gives
$
 \left|\{\xi\in[0,1]:|S_N(\xi)|^2\ge N/2\}\right|
 \ge\frac18.
$
By periodicity, the corresponding set in $[0,N]$ has measure at least $N/8$. The sinc factor there is at least
$
 b_0=\frac{\sin(1/2)}{1/2}>0.
$
Consequently
$
 \boxed{\quad
 \mathcal L(|\widehat f_N|)
 \ge\frac{3b_0}{8\sqrt2}\,N^{1/6}.
 \quad}                                                    \tag{22}
$
This diverges. It is an obstruction to a uniform use of this Fourier criterion, not a counterexample to bounded quadratic-form density.

For comparison, the simpler condition $\widehat f_H\in L^1$ already follows when the hub is a sum of two independent bounded-density variables with nonzero coefficients. That smoothing mechanism is covered by the spread-linear-hub result in the existing paper. The new assertions here are the critical rearrangement criterion, its fractional Sobolev consequence, and the interval-fragmentation extension beyond (19).

## 6. What remains

Theorem 1 allows arbitrary fragmentation whenever the hub has the stated fractional Fourier regularity. The polynomial interval family with $r>3/2$ is one concrete consequence. Arbitrary cap-one hub laws need not satisfy the criterion, as (22) shows.

To close the unrestricted rank-three leakage model, an estimate must retain more interaction between the light slice and the locations of the hub's Fourier mass than the separate rearrangement bound (7)–(8) retains. A bound for this specific model would still need to be combined with the structural reductions for arbitrary indefinite matrices and their remaining spectrum. Neither implication is claimed here.

## References

1. W. Beckner, “Inequalities in Fourier analysis,” *Annals of Mathematics* **102** (1975), 159–182. [Publisher](https://annals.math.princeton.edu/1975/102-1/p11).
2. F. Barthe, “On a reverse form of the Brascamp–Lieb inequality,” *Inventiones Mathematicae* **134** (1998), 335–361. [DOI](https://doi.org/10.1007/s002220050267).
3. *Density Bounds for Quadratic Forms under Product Measures*, section “Quadratic forms with hub coordinates,” especially the frozen-slice, interval-supported-hub, bounded-variation, and spread-linear-hub results. [Paper sources](https://github.com/yspennstate/math-open-problems/tree/33aeb8660cba4fa0c0d8ae7849499daf5cbf5c98/proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper).
4. *Quadratic forms with fragmented hub densities*, the preceding interval-envelope result. [Proof](https://github.com/yspennstate/math-open-problems/blob/d5094e2e13951a8b77ebf220a51425474fd4b2f1/proofnet24/QFORM-density/interactive/20260923T195310Z-hub-interval-envelopes/RESULT.md).
