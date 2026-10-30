# B15 — sharp arbitrary-bias posterior credit and a 512x wider rare-pivot exclusion

**Classification:** `ESSENTIAL_STEP_APPLIED / FULL_FEI_OPEN`.

Full unrestricted uniform-cube Fourier entropy-influence remains **OPEN / NOT PROVED**.

**Execution:** `WITHOUT_VERIFIED_BRAIN`. Repository controls and mathematical source files were read directly; no authenticated cognitive-brain receiver/context entered the derivation.

## 0. Live candidate and exact peer result consumed

The live all-gate target is
\[
D_\Gamma(G;p)=\sum_i {\operatorname{It}_i(G;p)\over V_{p_i}}
\bigl(\Gamma(p_i)+h_2(V_{p_i})\bigr)
-\Gamma(p_{\rm out})-\widetilde H_G(p)\ge0,
\qquad V_u=4u(1-u),
\]
for every Boolean gate and every product bias. The fixed candidate under test is
\[
C^\dagger=6.521851214,
\qquad
\Gamma^\dagger(u)=\Gamma_0(u)+0.268204856\,u(1-u).
\]
The current source-bound tail premise, proved in fleet01/B18 and reused by the fleet, is: for
\(0<u\le1/2\), with \(L=\log_2(1/u)\),
\[
\Gamma^\dagger(u)>
 u(4.9096L+2.22)+0.268204856\,u(1-u).
\tag{0.1}
\]

The exact other-account theorem consumed and improved is

`proofnet24/P03-fei/fleet-2026-09-21/fleet04/B13/20260922T051245Z-biased-joint-credit-collar/REPORT.md`

(report blob `e77494a14411182d0f20429a349ccfef3d561253`).  For a physical pivot of bias \(t\), restrictions
\(f_b=(-1)^{G_b}=\sum_S a_S^{(b)}\chi_S\), and disagreement
\(\delta=\Pr(f_0\ne f_1)\), it records the exact gluing cocycle
\[
D_\Gamma(G)=qD_\Gamma(G_0)+tD_\Gamma(G_1)+\mathcal R_{\Gamma,j}+\mathcal C_j,
\qquad q=1-t,
\tag{0.2}
\]
where
\[
\mathcal C_j=H(B\mid S)+I(S;J)\ge0.
\tag{0.3}
\]
It proves the arbitrary-bias coarse credit
\[
\mathcal C_j\ge V_t(1-2\delta)^2
\tag{0.4}
\]
and, for balanced children, excludes negative gluing with \(\delta\ge1/4\) only in the rare collar
\(\min(t,1-t)\le2^{-15}\).

The present run identifies the exact negative posterior-entropy mechanism more sharply and widens that collar to \(1/64\), a factor \(512\).

## 1. Posterior geometry and the sharp scalar profile

Put
\[
T_S=q a_S^2+t b_S^2,
\qquad
x_S={t b_S^2\over T_S}
\]
when \(T_S>0\).  Then the latent branch posterior satisfies
\[
H(B\mid S)=\sum_S T_S h_2(x_S).
\tag{1.1}
\]
Define
\[
z_S=2\sqrt{x_S(1-x_S)}
={2\sqrt{tq}\,|a_Sb_S|\over T_S}.
\tag{1.2}
\]
Because the two restrictions are actual Boolean functions,
\[
\sum_S a_Sb_S=\mathbb E[f_0f_1]=1-2\delta.
\tag{1.3}
\]
Therefore
\[
\mathbb E_T z_S
=2\sqrt{tq}\sum_S|a_Sb_S|
\ge \sqrt{V_t}\,|1-2\delta|.
\tag{1.4}
\]

Introduce the one-variable function
\[
\Psi(z):=h_2\!\left({1-\sqrt{1-z^2}\over2}\right),
\qquad 0\le z\le1.
\tag{1.5}
\]
Since \(z=2\sqrt{x(1-x)}\), we have exactly
\[
h_2(x)=\Psi\!\left(2\sqrt{x(1-x)}\right).
\tag{1.6}
\]
The key point is that \(\Psi\) is increasing and convex.  Indeed, writing
\(r=\sqrt{1-z^2}\),
\[
\Psi'(z)
={z\over2r}\log_2{1+r\over1-r}>0,
\tag{1.7}
\]
and
\[
\Psi''(z)
={\log((1+r)/(1-r))-2r\over2r^3\ln2}\ge0,
\tag{1.8}
\]
because \(\log((1+r)/(1-r))=2\operatorname{artanh}r\ge2r\).

Jensen applied to (1.1), (1.4), and (1.6) now gives the sharp arbitrary-bias source-valid credit.

### Theorem B15-SHARP-BIASED-CREDIT

For every actual Boolean pair of restrictions, every interior pivot bias \(t\), and
\(\delta=\Pr(f_0\ne f_1)\),
\[
\boxed{
\mathcal C_j\ge H(B\mid S)
\ge
\Psi\!\left(\sqrt{V_t}\,|1-2\delta|\right).
}
\tag{1.9}
\]
No arbitrary probability-law relaxation is used; the only nontrivial input is the signed Boolean overlap (1.3).

Since \(h_2(x)\ge4x(1-x)\), one has \(\Psi(z)\ge z^2\).  Thus (1.9) strictly strengthens the fleet04/B13 bound (0.4).  At \(t=1/2\), it becomes
\[
\Psi(|1-2\delta|)
=h_2\!\left({1-2\sqrt{\delta(1-\delta)}\over2}\right),
\tag{1.10}
\]
which exactly recovers the sharp center theorem previously available only at the unbiased pivot.

This is the requested negative-entropy term in source-exact form: the branch label is *not* charged as a free \(h_2(t)\) bit; its unrevealed posterior entropy (1.9) is retained with the favorable sign in the gluing cocycle.

## 2. Insertion into the local gluing residual

Fleet04/B13 gives
\[
\begin{aligned}
\mathcal R_{\Gamma,j}={}&
q\Gamma(r_0)+t\Gamma(r_1)-\Gamma(qr_0+tr_1)\\
&+\delta\bigl(\Gamma(t)+h_2(V_t)\bigr)
-h_2(t)-h_2(V_t\delta).
\end{aligned}
\tag{2.1}
\]
For balanced children \(r_0=r_1=1/2\), the potential Jensen term vanishes exactly.  By symmetry write
\[
u=\min(t,1-t),\qquad V=4u(1-u).
\]
Then (1.9) and (2.1) give
\[
\mathcal R_{\Gamma^\dagger,j}+\mathcal C_j
\ge F_u(\delta),
\tag{2.2}
\]
where
\[
\boxed{
F_u(\delta)=
\delta\bigl(\Gamma^\dagger(u)+h_2(V)\bigr)
-h_2(u)-h_2(V\delta)
+\Psi\!\left(\sqrt V\,|1-2\delta|\right).
}
\tag{2.3}
\]
The problem is now a two-scalar inequality with the negative posterior entropy preserved exactly.

## 3. Monotonicity in the normalized influence on the collar \(u\le1/64\)

Assume
\[
0<u\le {1\over64},\qquad {1\over4}\le\delta\le1.
\tag{3.1}
\]
Then \(L=\log_2(1/u)\ge6\), \(V\le1/16\).

For \(\delta\in[1/2,1]\), the \(\Psi\)-term in (2.3) is increasing.  Also
\[
h_2(V)\ge V\log_2(1/V),
\qquad
h_2'(V\delta)\le\log_2(2/V).
\]
Consequently
\[
F_u'(\delta)
\ge\Gamma^\dagger(u)-V
>u(4.9096L+2.22)-4u>0.
\tag{3.2}
\]

For \(\delta\in[1/4,1/2]\), put
\(z=\sqrt V(1-2\delta)\le\sqrt V/2\le1/8\).  From (1.7),
\[
\Psi'(z)
\le {z\over2\sqrt{1-z^2}}\log_2{4\over z^2}.
\tag{3.3}
\]
On \([0,1/8]\), the function \(z\log_2(4/z^2)\) is increasing.  Moreover
\[
\sqrt{1-z^2}\ge\sqrt{63/64}>{63\over64}.
\]
Thus
\[
2\sqrt V\,\Psi'(z)
\le {32\over63}V\log_2{16\over V}.
\tag{3.4}
\]
Because \(V\delta\ge V/4\),
\[
h_2(V)-Vh_2'(V\delta)\ge-2V.
\tag{3.5}
\]
Also
\[
\log_2{16\over V}
=L+2+\log_2{1\over1-u}
\le L+2+{1\over42},
\tag{3.6}
\]
using \(-\ln(1-u)\le u/(1-u)\le1/63\) and \(\ln2>2/3\).
Dropping the positive quadratic lift in (0.1), (3.4)--(3.6) give
\[
{F_u'(\delta)\over u}
>
\left(4.9096-{128\over63}\right)L
+2.22-8-{128\over63}\left(2+{1\over42}\right).
\tag{3.7}
\]
The right side is increasing in \(L\) and at \(L=6\) equals
\[
7.3752568405\ldots>0.
\tag{3.8}
\]
Hence
\[
\boxed{F_u'(\delta)>0\quad\text{for all }u\le1/64,\ \delta\ge1/4.}
\tag{3.9}
\]
So the entire region is reduced to the single boundary \(\delta=1/4\).

## 4. The boundary \(\delta=1/4\): the posterior credit pays the entropy loss

At \(\delta=1/4\),
\[
F_u(1/4)
={1\over4}\Gamma^\dagger(u)-h_2(u)+K(V),
\tag{4.1}
\]
where
\[
K(V):={1\over4}h_2(V)-h_2(V/4)+\Psi(\sqrt V/2).
\tag{4.2}
\]
We now show \(K(V)\ge0\) throughout \(0<V\le1/16\).

Let
\[
g(V)=h_2(V/4)-{1\over4}h_2(V).
\]
Then
\[
g'(V)={1\over2}+{1\over4}\log_2{1-V/4\over1-V}.
\tag{4.3}
\]
For \(V\le1/16\),
\[
\log_2{1-V/4\over1-V}
\le\log_2{1\over1-V}
\le {1\over10},
\tag{4.4}
\]
again using \(-\ln(1-V)\le V/(1-V)\le1/15\) and \(\ln2>2/3\).  Since \(g(0)=0\),
\[
\boxed{g(V)\le {21\over40}V.}
\tag{4.5}
\]

For the credit term set
\[
y={1-\sqrt{1-V/4}\over2}.
\]
Then
\[
{V\over16}\le y\le {V\over8}\le{1\over128}.
\tag{4.6}
\]
On this interval both \(y\log_2(1/y)\) and \(y(1-y)\) are increasing, and
\[
\begin{aligned}
\Psi(\sqrt V/2)=h_2(y)
&\ge y\log_2(1/y)+y(1-y)\\
&\ge {V\over16}\log_2{16\over V}
   +{V\over16}\left(1-{V\over16}\right)\\
&\ge V\left({1\over2}+{255\over4096}\right)
={2303\over4096}V.
\end{aligned}
\tag{4.7}
\]
Since \(2303/4096>21/40\), equations (4.5)--(4.7) prove
\[
\boxed{K(V)>0\qquad(0<V\le1/16).}
\tag{4.8}
\]

Therefore, using (0.1) and the elementary bound
\(h_2(u)\le u[L+\log_2e]<u(L+3/2)\),
\[
\begin{aligned}
{F_u(1/4)\over u}
&>{1\over4}(4.9096L+2.22)-L-{3\over2}\\
&=0.2274L-0.945\\
&\ge0.4194>0.
\end{aligned}
\tag{4.9}
\]

Combining (3.9) and (4.9) proves the main exclusion.

### Theorem B15-WIDE-RARE-PIVOT

For the live \(\Gamma^\dagger\), if a physical pivot has balanced Boolean children and
\[
\boxed{\min(t,1-t)\le1/64,\qquad
\delta={\operatorname{It}_j\over V_t}\ge1/4,}
\tag{4.10}
\]
then
\[
\boxed{\mathcal R_{\Gamma^\dagger,j}+\mathcal C_j>0.}
\tag{4.11}
\]
Hence such a pivot cannot occur as a negative local-gluing step in a minimum-essential-arity counterexample.

This widens fleet04/B13's analytically proved rare-bias collar from \(2^{-15}\) to \(2^{-6}\), exactly a factor \(512\), while using a *stronger* source-valid negative entropy credit rather than more sampling.

## 5. Exact old/new missing implications

**Old missing implication (source-current):** prove LOCAL-GLUING for every physical pivot under the fixed `Gamma^dagger`, or exhibit a genuine Boolean violating gate.  fleet04/B13 left, even on balanced children, intermediate pivot biases together with \(\delta<1/4\) or the region between its center theorem and \(2^{-15}\) collar.

**New proved inference:** the posterior branch-entropy term admits the sharp arbitrary-bias lower bound (1.9), and on balanced children it excludes every negative gluing node with \(\delta\ge1/4\) throughout the much larger collar \(\min(t,1-t)\le1/64\).

**New first missing implication:** close the compact balanced-child region
\[
1/64<\min(t,1-t)<1/2,
\qquad \delta\ge1/4,
\]
using the same sharp profile (1.9), and then address \(\delta<1/4\) and unequal child measures where the potential Jensen term is nonzero.  A finite interval proof on the compact strip would be a legitimate next move because the singular rare-bias endpoint is now removed analytically.

This is not a full FEI proof and is not evidence that every remaining prime gate is safe.

## 6. Source discipline

No ambient coordinate labels, dimension charges, unsigned replacement of (1.3), half-band positive-current assumptions, arbitrary spectral-law relaxation, or circular potential construction were used.  The result uses the exact source signs through \(\sum_Sa_Sb_S=1-2\delta\), the exact gluing cocycle, the exact negative posterior entropy, and the already source-certified `Gamma^dagger` tail premise.
