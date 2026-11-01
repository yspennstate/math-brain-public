# C0032 — exact radial-CDF duality, correction of the printed far-tail exponent, and rational-index Meijer-G reduction

Target: Bordenave–Chafaï, *Around the circular law*, heavy-tailed limiting law `mu_alpha`; underlying scalar characterization and printed tail theorem: Bordenave–Caputo–Chafaï, *Spectrum of non-Hermitian heavy tailed random matrices*, CMP 307 (2011), arXiv:1006.1713v5.

Status: theorem-sized **PARTIAL** progress toward explicit identification of `g_alpha`.  This artifact does not claim source-level closure or novelty.  It does, however, isolate a normalization error in the printed proof of BCC Theorem 1.3 and derives a corrected far-tail asymptotic from the exact scalar law.  The correction is independently certified at `alpha=1` by the exact Struve/Bessel representation obtained in the preceding R7-06 run.

## 1. Recalled exact parameterization

Put

\[
\beta=\alpha/2\in(0,1),\qquad c_\beta=\Gamma(1-\beta),\qquad C_\beta=\Gamma(1-\beta)\Gamma(1+\beta).
\]

Let `S,S'` be independent positive beta-stable variables with BCC normalization

\[
\mathbb E e^{-tS}=\exp[-c_\beta t^\beta].
\tag{1.1}
\]

Write

\[
r=|z|^2,\qquad Y(r)=y_*(r)^2.
\]

The BCC scalar equation is

\[
1=\mathbb E\bigl(r/S+Y(r)S'\bigr)^{-\beta}.
\tag{1.2}
\]

Define

\[
a=\frac r{Y(r)},\qquad F(a)=\mathbb E(S'+a/S)^{-\beta}.
\tag{1.3}
\]

Then exactly

\[
Y(a)=F(a)^{1/\beta},\qquad r(a)=aF(a)^{1/\beta},\qquad r(a)^\beta=a^\beta F(a).
\tag{1.4}
\]

The preceding run proved that `a -> r(a)` is a smooth increasing bijection of `[0,infinity)` and that

\[
\mathcal M F(s)=c_\beta^{-1+2s/\beta}
\frac{\Gamma(s)\Gamma(1-s/\beta)^2}
{\Gamma(1+\beta)\Gamma(1-s)},
\qquad 0<\Re s<\beta.
\tag{1.5}
\]

Let

\[
M(r)=\mu_\alpha\{|z|^2\le r\}
\]

be the squared-radius CDF.

## 2. B11 — one-transform radial CDF and a quantile representation

Let `T=SS'` and

\[
q(a):=1-M(r(a)).
\]

The previous parameterization gave

\[
M(r(a))=aK(a),\qquad K(a)=\mathbb E\frac1{a+T},
\]
so

\[
q(a)=\mathbb E\frac{T}{a+T}.
\tag{2.1}
\]

For `0<Re s<beta`, Tonelli and the beta integral give

\[
\begin{aligned}
\mathcal M q(s)
&=\int_0^\infty a^{s-1}\mathbb E\frac{T}{a+T}\,da\\
&=\Gamma(s)\Gamma(1-s)\,\mathbb E T^s.
\end{aligned}
\]

The stable moment identity

\[
\mathbb E S^s=c_\beta^{s/\beta}
\frac{\Gamma(1-s/\beta)}{\Gamma(1-s)}
\]
then yields

\[
\mathcal M q(s)=c_\beta^{2s/\beta}
\frac{\Gamma(s)\Gamma(1-s/\beta)^2}{\Gamma(1-s)}.
\tag{2.2}
\]

Comparing (2.2) with (1.5),

\[
\mathcal M q(s)=C_\beta\,\mathcal M F(s).
\]

Both functions are positive and possess Mellin transforms on the same nonempty strip, so Mellin uniqueness gives the exact identity

\[
\boxed{1-M(r(a))=C_\beta F(a)}.
\tag{2.3}
\]

Since `F(0)=1/C_beta`, the identity also extends continuously to `a=0`.

Combining (2.3) with (1.4),

\[
\boxed{1-M(r(a))=C_\beta\frac{r(a)^\beta}{a^\beta}}.
\tag{2.4}
\]

Differentiating (2.3),

\[
\boxed{\pi\widetilde g_\alpha(r(a))=-C_\beta\frac{F'(a)}{r'(a)}},
\qquad \widetilde g_\alpha(r)=g_\alpha(\sqrt r).
\tag{2.5}
\]

Thus `K` and `J` are not independent data: the entire radial law is controlled by the single scalar transform `F`.

There is also a useful probabilistic dual coordinate.  If `E_1,E_2` are iid Exp(1), independent of `T`, then `R=E_1/E_2` has CDF `x/(1+x)`.  Therefore

\[
M(r(a))=\mathbb E\frac{a}{a+T}=\mathbb P\{TR\le a\}.
\tag{2.6}
\]

So `a(u)` is exactly the ordinary quantile function of

\[
W=SS'\,\frac{E_1}{E_2}.
\]

Equation (1.4) then maps this ordinary one-dimensional quantile to the spectral radius coordinate.

## 3. B7 — a factor-beta inconsistency in the printed BCC tail proof

BCC Lemma 4.3 uses exactly the normalization (1.1).  Their own expansion in the proof of Lemma 4.8 gives

\[
g_\beta(x)=\beta x^{-\beta-1}+O(x^{-2\beta-1})
\qquad(x\to\infty)
\tag{3.1}
\]

for the density of `S`.  Integrating (3.1) immediately yields

\[
\boxed{
\mathbb E[S^\beta;S\le t]
=\beta\log t+C+O(t^{-\beta})
}
\tag{3.2}
\]

for a finite constant `C`.  Indeed, on `[1,t]`,

\[
x^\beta g_\beta(x)=\beta x^{-1}+O(x^{-\beta-1}).
\]

However, the printed statement of BCC Lemma 4.8 is

\[
\mathbb E[S^\beta;S\le t]=\log t+c_0+o(1),
\tag{3.3}
\]

with the factor `beta` missing.  This is not a convention issue: (3.1) and (3.3) occur in the same lemma under the same normalization (1.1), and (3.2) follows directly from (3.1).

The missing factor propagates.  In BCC Lemma 4.10, their displayed relation

\[
r^\beta=\log(ry_*^{-2})+O(1)
\]
comes from (3.3).  With (3.2), the corresponding leading relation is instead

\[
\boxed{r^\beta=\beta\log(ry_*^{-2})+O(1)}.
\tag{3.4}
\]

Equivalently, since `a=r/Y=ry_*^{-2}`,

\[
\log a\sim r^\beta/\beta.
\]

This already predicts a far-tail exponential `exp(-r^beta)` for the radial law, rather than the printed `exp(-beta r^beta)`.

### 3.1 Exact Mellin extraction of the constant

The correction can be made precise without reusing BCC's Tauberian decomposition.  In (1.5), the first right-hand singularity is a double pole at `s=beta`.  Write `s=beta+epsilon`.  Since

\[
\Gamma(1-s/\beta)=\Gamma(-\epsilon/\beta)
=-\frac\beta\epsilon-\gamma_E+O(\epsilon),
\]

we obtain

\[
\mathcal M F(\beta+\epsilon)
=\frac\beta{\epsilon^2}+\frac{B_\beta}{\epsilon}+O(1),
\tag{3.5}
\]

where

\[
B_\beta=2\gamma_E+2\log\Gamma(1-\beta)
+\beta\{\psi(\beta)+\psi(1-\beta)\}.
\tag{3.6}
\]

Shift the Mellin-inversion contour to the right past `s=beta`.  Because `a^{-s}` closes clockwise for `a>1`, the contribution is minus the residue.  Stirling's formula gives exponential decay on vertical lines, and choosing `0<delta<beta` avoids the next pole at `2beta`.  Hence

\[
\boxed{
F(a)=a^{-\beta}\bigl(\beta\log a+\eta_\beta\bigr)
+O(a^{-\beta-\delta})
}
\tag{3.7}
\]

for any fixed sufficiently small `delta>0`, where

\[
\boxed{
\eta_\beta=-2\gamma_E-2\log\Gamma(1-\beta)
-\beta\{\psi(\beta)+\psi(1-\beta)\}.
}
\tag{3.8}
\]

Equation (1.4) therefore gives

\[
\boxed{r(a)^\beta=\beta\log a+\eta_\beta+o(1)}.
\tag{3.9}
\]

Consequently

\[
a^\beta=e^{r^\beta-\eta_\beta}(1+o(1)).
\tag{3.10}
\]

Using the exact CDF identity (2.4),

\[
\boxed{
1-M(r)\sim D_\beta r^\beta e^{-r^\beta}
},
\tag{3.11}
\]

where

\[
\boxed{
D_\beta=C_\beta e^{\eta_\beta}
=\frac{\Gamma(1+\beta)}{\Gamma(1-\beta)}
\exp\!\left[-2\gamma_E-\beta\{\psi(\beta)+\psi(1-\beta)\}\right].
}
\tag{3.12}
\]

Differentiating the Mellin asymptotic (equivalently, differentiating (3.11) after using the derivative version of the same contour shift) yields

\[
M'(r)\sim \beta D_\beta r^{2\beta-1}e^{-r^\beta}.
\]

Since `M'(r)=pi g_alpha(sqrt(r))`, we obtain the corrected planar-density tail

\[
\boxed{
 g_\alpha(\rho)
\sim A_\alpha\,\rho^{2\alpha-2}e^{-\rho^\alpha},
\qquad \rho\to\infty,
}
\tag{3.13}
\]

with

\[
\boxed{
A_\alpha=\frac\beta\pi D_\beta,
\qquad \beta=\alpha/2.
}
\tag{3.14}
\]

The printed BCC Theorem 1.3 instead states the same polynomial power multiplied by `exp[-(alpha/2) rho^alpha] = exp[-beta rho^alpha]`.  Equations (3.1)–(3.4) pinpoint the missing factor in the printed proof, while (3.5)–(3.14) give a self-contained corrected derivation from the exact scalar law.

### 3.2 Independent alpha=1 certificate

For `alpha=1` (`beta=1/2`), the preceding R7-06 run proved

\[
F(a)=\frac\pi{2\sqrt a}
\left[\mathbf H_0\!\left(\frac\pi{2\sqrt a}\right)
-Y_0\!\left(\frac\pi{2\sqrt a}\right)\right].
\tag{3.15}
\]

The standard small-argument expansion gives

\[
F(a)=a^{-1/2}
\left[\frac12\log a+\log(4/\pi)-\gamma_E+o(1)\right].
\tag{3.16}
\]

This matches (3.7) exactly and independently rules out the printed coefficient in Lemma 4.10.  Here

\[
D_{1/2}=2e^{-\gamma_E},
\]

so

\[
\boxed{
1-M(r)\sim2e^{-\gamma_E}\sqrt r\,e^{-\sqrt r},
\qquad
 g_1(\rho)\sim\frac{e^{-\gamma_E}}\pi e^{-\rho}.
}
\tag{3.17}
\]

Thus at `alpha=1` the exact special-function formula forces exponential rate `e^{-rho}`, while the printed BCC theorem would give `e^{-rho/2}`.

## 4. B30 — exact Meijer-G reduction for every rational beta

Let

\[
\beta=p/q\in(0,1),\qquad \gcd(p,q)=1,
\]

and define

\[
\mathcal A_m=\{0,1/m,\ldots,(m-1)/m\}.
\]

Set `s=pt` in the Mellin inversion (1.5).  Applying Gauss's multiplication formula separately to `Gamma(pt)`, `Gamma(1-pt)`, and the two copies of `Gamma(1-qt)` gives the standard Meijer-G integral.  With the convention

\[
G_{P,Q}^{m,n}\!\left(z\middle|\begin{matrix}a_1,\dots,a_P\\b_1,\dots,b_Q\end{matrix}\right)
=\frac1{2\pi i}\int
\frac{\prod_{j=1}^m\Gamma(b_j+s)\prod_{j=1}^n\Gamma(1-a_j-s)}
{\prod_{j=m+1}^Q\Gamma(1-b_j-s)\prod_{j=n+1}^P\Gamma(a_j+s)}
z^{-s}ds,
\]

one obtains

\[
\boxed{
F_{p/q}(a)=
\frac{q(2\pi)^{1-q}}{C_\beta}
G_{2q,2p}^{p,2q}\!\left(
Z\middle|
\begin{matrix}
\mathcal A_q,\mathcal A_q\\
\mathcal A_p,\mathcal A_p
\end{matrix}
\right),
}
\tag{4.1}
\]

where the first copy of `A_p` is in the `m=p` numerator block, all `2q` upper parameters are in the `n=2q` numerator block, and

\[
\boxed{
Z=\frac{q^{2q}a^p}{p^{2p}\Gamma(1-\beta)^{2q}}.
}
\tag{4.2}
\]

Proof of the prefactor: after `s=pt`, the powers from Gauss multiplication combine as

\[
c_\beta^{2qt}p^{2pt}q^{-2qt}a^{-pt}=Z^{-t},
\]

while the constant factors reduce to

\[
\frac{q(2\pi)^{1-q}}{c_\beta\Gamma(1+\beta)}
=\frac{q(2\pi)^{1-q}}{C_\beta}.
\]

Because (2.3) and (2.5) express the radial CDF and density solely through `F` and `F'`, (4.1) gives a standard named-function description of the entire one-parameter radial law for every rational `alpha/2`.

Three low-denominator cases are:

- `beta=1/2`: `Z=16a/pi^2` and
  \[
  F(a)=\frac{2}{\pi^2}G_{4,2}^{1,4}
  \left(\frac{16a}{\pi^2}\middle|
  \begin{matrix}0,1/2,0,1/2\\0,0\end{matrix}\right),
  \]
  equivalent to (3.15).
- `beta=1/3`:
  \[
  F(a)=\frac{3}{4\pi^2C_{1/3}}
  G_{6,2}^{1,6}\left(
  \frac{729a}{\Gamma(2/3)^6}\middle|
  \begin{matrix}0,1/3,2/3,0,1/3,2/3\\0,0\end{matrix}\right).
  \]
- `beta=2/3`:
  \[
  F(a)=\frac{3}{4\pi^2C_{2/3}}
  G_{6,4}^{2,6}\left(
  \frac{729a^2}{16\Gamma(1/3)^6}\middle|
  \begin{matrix}0,1/3,2/3,0,1/3,2/3\\0,1/2,0,1/2\end{matrix}\right).
  \]

This reduction is consistent with the classical literature expressing rational positive-stable densities and transforms through Meijer-G functions (e.g. Zolotarev; Penson–Górska; Demni), but the present object is the specific BCC product-stable transform entering the heavy-tailed circular law.

## 5. What is and is not settled

1. The BCC scalar self-consistency is globally eliminated by the monotone parameter `a` (preceding run).
2. The radial CDF and density now depend on only one transform `F`, via (2.3) and (2.5).
3. The printed BCC far-tail exponent contains a factor-beta inconsistency traceable to Lemma 4.8; (3.13) is the corrected asymptotic under the same source normalization, with an explicit multiplicative constant.
4. Every rational `beta` has an explicit Meijer-G representation (4.1).
5. The full C0032 source target is still **OPEN/PARTIAL** because, for arbitrary irrational `beta`, the inversion from the monotone parameter `a` to a direct named expression `g_alpha(rho)` remains unresolved, and the survey's word “explicit” has no formal closure convention.
6. No P26 audit, distinct OTHER-track audit, or source-scope paper package exists; no closure label is warranted.

## 6. Dated source/prior-art check — 2026-09-18 UTC

- Bordenave–Caputo–Chafaï, arXiv:1006.1713v5 (last revised 2011-10-14), Theorem 1.3 and Lemmas 4.8–4.11 were checked directly.  The printed theorem states `rho^{2(alpha-1)} exp[-(alpha/2)rho^alpha]` up to multiplicative constant; the factor-beta discrepancy above is internal to the printed proof.
- Bordenave–Chafaï, arXiv:1109.3343v4 / Probability Surveys 9 (2012), remains the source survey posing explicit identification of the heavy-tailed density as an open descriptive problem.
- Penson–Górska (PRL 105, 210604, 2010), Górska–Penson (PRE 83, 061125, 2011), and Demni (arXiv:1009.4926) provide rational positive-stable special-function formulae; they do not directly provide the BCC radial spectral law derived here.
- A bounded current search found no corrigendum or later source-matching paper correcting BCC Theorem 1.3 or giving the all-irrational direct density.  Search absence is not a novelty or openness certificate.

## 7. Next mathematical attack

The frozen campaign metric `M_jet` is already saturated and should not be replaced.  A nonrepeating next triple should attack source-level explicitness rather than more origin coefficients:

- **B1**: change category — study `v(a)=C_beta F(a)` as a generalized Stieltjes/completely monotone function and ask whether its inverse belongs to a canonical Bernstein/Stieltjes inverse class;
- **B12**: for rational `beta`, derive the exact linear ODE annihilating the Meijer-G `F`, then eliminate `a` to obtain an algebraic-differential equation for the radial CDF/density;
- **B29**: compactify the `a=infinity` endpoint using `v=1-M` and construct the full tail transseries, checking whether the corrected exponent can be promoted to a rigorous asymptotic expansion uniform in `beta` on compact subsets of `(0,1)`.
