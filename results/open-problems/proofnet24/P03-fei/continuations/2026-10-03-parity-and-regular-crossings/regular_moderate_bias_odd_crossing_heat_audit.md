# Independent audit: ordinary FEI for comparable-weight moderate-bias odd crossings

Date: 2026-10-03. Auditor: `/root/heat_entropy`.

**Verdict: analytic PASS.** I read the complete
[candidate](regular_moderate_bias_odd_crossing_fei_candidate.md), independently
derived its block-resampling influence lower bound before reading the
candidate, then checked every step and numerical constant in the assembled
proof. I found no analytic gap. This is a restricted ordinary FEI theorem,
without an output parity. It does not prove arbitrary-weight or arbitrary-bias
three-crossing FEI, or the full Boolean FEI conjecture. Historical priority
and external peer review remain unverified.

## Scope of the result

After coordinate sign flips, deleting zero weights, and common scaling,
the weights are (1\le w_i\le B). There are (m\ge1) distinct genuine
crossings, (m) odd, all satisfying

\[
 |\theta_r|\le\lambda\sigma,\qquad
 \sigma^2=\sum_i w_i^2.
\]

Between consecutive crossing points the labels alternate. At a crossing
the value may be either adjacent label, independently for each crossing.
There are no additional isolated-point anomalies. Thus the two tails have
opposite labels. For fixed (m,B,\lambda), the candidate proves a constant
ordinary entropy–influence bound in every dimension, uniformly over all
crossing gaps. The adjective moderate refers precisely to this bound on
**every crossing point**, not merely to the probability of the final output.

Deleting zero-weight coordinates leaves entropy and influence unchanged.
Coordinate sign flips only sign some Fourier coefficients, preserving their
squares and physical influences. Common positive scaling preserves the
function and the normalized bias premise. If no coordinates remain the
output is constant and entropy is zero. Genuine real crossings need not all
be witnessed by distinct cube scores; the proof does not silently require
that every interval contain an attained score.

## The entropy bound and its established inputs

I reopened the author-hosted primary
[Klivans–O'Donnell–Servedio manuscript](https://www.cs.columbia.edu/~rocco/Public/focs02.pdf).
Theorem 18, printed page 9, uses independent bit **flips** and gives the
stated bias-sensitive halfspace estimate with coefficient 20.5. Corollary 19
already gives a smaller bias-free coefficient, and Theorem 21 supplies the
union-bound estimate for a function of finitely many halfspaces. The
candidate's use of the looser (20.5\sqrt\varepsilon) estimate is valid.

For each crossing, an increasing halfspace can include or exclude the tie
as required. On the finite cube-score set, either tie convention is a genuine
halfspace obtained by a sufficiently small threshold perturbation. These
perturbations are used only for the noise input; the original crossing points
continue to be used in the influence proof. The product of the (m)
halfspaces, times a constant sign, reproduces the alternating-label function
including the independently chosen crossing labels. Thus

\[
 \operatorname{NS}_\varepsilon(g)\le20.5m\sqrt\varepsilon.
\]

The spectral noise identity has a factor 2 on the left. At noise
(1/(2k)), degree at least (k\ge1) contributes at least (1-e^{-1})
to that identity; (k=1) is valid because all positive degrees contribute
one. The resulting tail coefficient is exactly

\[
 A=\frac{41}{\sqrt2(1-e^{-1})},\qquad
 \Pr[D\ge k]\le Am/\sqrt k.
\]

For real (t>0), using (\lceil t\rceil) gives the same upper bound
(Am/\sqrt t). Condition on spectral degree to obtain

\[
 H(g)\le\log_2(n+1)
       +\frac1{\ln2}\mathbb E[D\ln(en/D)].
\]

The function (b(t)=t\ln(en/t)), with (b(0)=0), is increasing on
([0,n]), and its derivative is (\ln(n/t)). Tail integration yields

\[
 \mathbb E b(D)\le Am\int_0^n t^{-1/2}\ln(n/t)\,dt
                 =4Am\sqrt n.
\]

The choice of (\Pr[D\ge t]) instead of (\Pr[D>t]) makes no difference
to this integral. Finally (\ln(n+1)\le\sqrt n) for (n\ge1): its
difference has nonnegative derivative and is positive at one. Therefore

\[
 H(g)\le C_H\sqrt n,
 \qquad C_H=(1+4Am)/\ln2.                         \tag{A}
\]

The within-degree and degree-entropy terms include all spectral atoms,
including degree zero. The candidate does not claim that (A) by itself
is FEI, nor does it treat this generic noise-to-entropy step as new.

## Signed translation and open pivotal intervals

Fix block scores (u,v\in\mathbb R). The translated outputs differ only
between the smallest and largest translated crossing point. Remove all
translated crossing points and retain each open interval on which the
outputs differ. Denote the resulting set by (A^\circ_{u,v}).

There are at most (2m) distinct translated crossing points. The exterior
open intervals are never pivotal. Hence at most (2m) bounded open
components suffice. This deliberately loose bound also covers coincident
translated crossings where deleting a point splits an otherwise pivotal
interval. Arbitrary legal tie choices can alter endpoint pivotality; the
proof lower-bounds using only open components and therefore loses no valid
lower-bound information at discrete atoms.

If (a_+,a_-) are the right and left tail labels, then

\[
 \int_{\mathbb R}[F(r+v)-F(r+u)]\,dr
       =(v-u)(a_+-a_-).
\]

This follows by integrating over a long finite interval and cancelling
the common part after translation; only two tail pieces remain. Because
(a_+=-a_-), the absolute signed integral is (2|v-u|). The absolute
integrand is two on the pivotal set and zero elsewhere, up to finitely many
endpoints. Consequently

\[
 |A^\circ_{u,v}|\ge|u-v|.                         \tag{B}
\]

This argument is independent of gap sizes and is the critical odd-crossing
input. It cannot be transferred to even crossing count by dropping the
opposite-tail condition.

## The cutoff and Gaussian lower density

The candidate sets

\[
 d=\frac{e^{-(\lambda+1)^2}}{\sqrt{2\pi}},\quad
 c_D=\sqrt{2/3},\quad E=2.24\sqrt2,
\]

\[
 K=\max\left\{1,\left\lceil
             \left(\frac{2EmB}{dc_D}\right)^2\right\rceil\right\},
 \qquad
 N_0=\left\lceil\max\{2KB^2,K^2B^2\}\right\rceil.
\]

For (n\ge N_0), every fixed (K)-subset (J) satisfies

\[
 \sigma^2\ge n\ge2KB^2,
 \quad s^2=\sum_{i\notin J}w_i^2\ge\sigma^2/2>0,
 \quad |u|,|v|\le KB\le\sqrt n\le\sigma.
\]

The pivotal open intervals thus lie in
([-(\lambda+1)\sigma,(\lambda+1)\sigma]). On this whole range the
density of (N(0,s^2)) is at least (d/\sigma): its prefactor is at
least (1/(\sqrt{2\pi}\sigma)), and (r^2/(2s^2)\le(\lambda+1)^2).

I also reopened O'Donnell's author-hosted
[book](https://www.cs.cmu.edu/~odonnell/papers/Analysis-of-Boolean-Functions-by-Ryan-ODonnell.pdf).
Its unnumbered Berry–Esseen theorem in Section 11.5, printed page 350,
explicitly accepts coefficient .56 for independent, potentially nonidentical
summands. Applied to the remaining weighted signs, it gives CDF distance

\[
 \delta\le0.56\frac{\sum_{i\notin J}w_i^3}{s^3}
         \le0.56 B/s\le0.56\sqrt2B/\sigma.
\]

For a bounded open interval ((a,b)), the discrete mass is
(F_R(b^-)-F_R(a)). Taking a left limit in the Kolmogorov bound is valid
because the Gaussian CDF is continuous. Thus its discrete probability is
at least its Gaussian probability minus (2\delta), including when either
endpoint is an attained score atom. Summing over at most (2m) open
components costs at most

\[
 4m\delta\le(2.24\sqrt2)mB/\sigma=EmB/\sigma.
\]

Combining with (B) yields exactly

\[
 \Pr[F(R+u)\ne F(R+v)]
       \ge[d|u-v|-EmB]/\sigma.                    \tag{C}
\]

The numerator may be negative for some (u,v); averaging a valid lower
bound of this type is legitimate.

## Block displacement moments and the one-half factor

Given (J), old and fresh block signs are independent of each other and
of the remaining signs. Let (D_J=U-V), and (a_J=\sum_{i\in J}w_i^2).
For one sign difference, its second moment is 2 and fourth moment is 8.
Independence gives

\[
 \mathbb E D_J^2=2a_J,
 \qquad
 \mathbb E D_J^4=12a_J^2-4\sum_{i\in J}w_i^4\le12a_J^2.
\]

Hölder interpolation then gives

\[
 \mathbb E|D_J|
 \ge\frac{(\mathbb E D_J^2)^{3/2}}{\sqrt{\mathbb E D_J^4}}
 \ge\sqrt{2a_J/3}\ge c_D\sqrt K.                 \tag{D}
\]

Averaging (C), using (D), and using the definition of (K) yields

\[
 \operatorname{NS}_J(g)
 \ge\frac{dc_D\sqrt K-EmB}{\sigma}
 \ge\frac{dc_D\sqrt K}{2\sigma}
 \ge\frac{dc_D\sqrt K}{2B\sqrt n}.                \tag{E}
\]

Resample the selected coordinates one at a time. Every intermediate input
remains uniform. The probability that replacing coordinate (i) by an
independent fresh uniform sign changes the function is (I_i(g)/2), since
the fresh sign agrees with the old sign with probability one half. A union
bound yields (\operatorname{NS}_J(g)\le\frac12\sum_{i\in J}I_i(g)).
Choose (J) uniformly among all (K)-subsets, independently of all signs:

\[
 \mathbb E_J\operatorname{NS}_J(g)
       \le\frac K{2n}I(g).                       \tag{F}
\]

Combining (E) and (F) gives

\[
 I(g)\ge\frac{dc_D}{B\sqrt K}\sqrt n.            \tag{G}
\]

The factor one half in (F) cancels the denominator two in (E). This is a
lower bound on total physical influence, not on a signed Chow sum, and it
does not assume that individual coordinates have comparable influences.

## Finish, constants, and verification

For large (n), dividing (A) by (G) gives the candidate's second constant

\[
 \frac{(1+4Am)B\sqrt K}{(\ln2)dc_D}.
\]

For (1\le n<N_0), the previously audited weak logarithmic inequality
(H(g)\le(\log_2n+3)I(g)) gives the first constant
(\log_2N_0+3). Constants and dimension zero are handled without dividing
by influence. Thus the maximum of the two displayed constants is valid.
The cutoffs are deliberately very large; no practical or optimized numerical
constant is claimed.

The independent script
[verify_regular_odd_crossing_heat.py](verify_regular_odd_crossing_heat.py)
imports no author helper. Its
[report](regular_odd_crossing_heat_checks.json) separately records rational
translation integrals, arbitrary legal crossing ties, exact block moments,
halfspace product realization, fixed-mask resampling, and averaged one-half
normalization. Gaussian open-interval/CDF comparisons and cutoff arithmetic
are numerical supplements. The large-dimensional cutoff itself is too large
for truth-table enumeration; the analytic argument above establishes it.

The independent checker completed successfully: 2,400 exact rational
translation pairs, 18,166 legal endpoint assignments, 300 exact displacement
moment checks, 168 cube functions, 3,048 fixed resampling masks, 168 uniform
mask averages, 905 numerical Gaussian open-interval comparisons, and 64
numerical cutoff calculations. The hybrid upper bound was attained in some
finite cases, independently confirming the normalization factor.

**Scope remains restricted:** all genuine crossings have bounded normalized
location, and all nonzero weights have bounded ratio. The lower bound (G)
need not hold for even crossing count, extremely biased locations, or
arbitrarily uneven weights. Prior noise, normal-approximation and weak FEI
tools are credited; the historical novelty of this particular consequence
has not been certified.
