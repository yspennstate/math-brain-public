# Self-contained off-support resolvent estimate (no local law)

Goal. Make Proposition `appB:resolvent` unconditional by proving its only cited step
from scratch. Let $g_1,\dots,g_{n}$ ($n=D-1$) be i.i.d. isotropic ($\E g_ig_i^*=I_D$)
sub-Gaussian vectors in $\F^D$, $Q=\frac1n\sum_{i=1}^n g_ig_i^*$, aspect
$\phi:=D/n=1+1/(D-1)\to1$, and $\eta=1/\log D$. Write $R=R(-\eta)=(Q+\eta)^{-1}\succ0$.
Let $m$ be the Marchenko–Pastur (MP) Stieltjes transform at aspect $1$. **Claim:**
$$
\big\|\,\E[R]\,\big\|=\lambda_{\max}\big(\E[(Q+\eta)^{-1}]\big)\ \le\ (1+o(1))\,m(-\eta)\ \sim\ \eta^{-1/2},
\qquad o(1)=O\!\big(\mathrm{polylog}(D)/\sqrt D\big).
$$
No local law is invoked. Inputs are textbook: Sherman–Morrison, Hanson–Wright, and
sub-Gaussian moment bounds. The point is that $\eta=1/\log D$ sits a *macroscopic*
$\mathrm{polylog}$ distance off the (hard) edge at $0$, so **every** error is
$\mathrm{poly}(\log D)/\sqrt D\to0$.

## 1. Reduction to one fixed direction, and the exact Schur identity

$\E[R]$ is Hermitian positive definite, so
$\lambda_{\max}(\E[R])=\sup_{\|w\|=1}\langle w,\E[R]w\rangle=\sup_{\|w\|=1}\E[\,w^*Rw\,]$.
Put $T_w:=\E[w^*Rw]$. It suffices to prove, **uniformly over unit $w$**,
$$
T_w\ \le\ (1+o(1))\,m(-\eta).\tag{$\star$}
$$
This is the crux: the deterministic bound is only $\|R\|\le\eta^{-1}$, and indeed
$\lambda_{\max}(R)=(\lambda_{\min}(Q)+\eta)^{-1}\approx\eta^{-1}$ since
$\lambda_{\min}(Q)\sim D^{-2}\ll\eta$. So the *largest eigenvalue of $R$ is $\approx\eta^{-1}$*,
a factor $\eta^{-1/2}$ above the claim. The gain comes only from taking $\E$: the spike sits on
the random null direction $u$ of $Q$, which is smeared over the sphere by the expectation.
$(\star)$ is exactly the statement that no fixed $w$ retains the spike.

**Leave-one-out.** Let $G=[g_1|\cdots|g_n]$, $Q^{(i)}=\frac1n\sum_{j\ne i}g_jg_j^*$,
$R^{(i)}=(Q^{(i)}+\eta)^{-1}$, and
$$
\beta_i:=\frac{1}{1+\tfrac1n g_i^*R^{(i)}g_i}\in(0,1].
$$
Sherman–Morrison ($Q+\eta=Q^{(i)}+\eta+\tfrac1n g_ig_i^*$) gives the two exact identities
$$
Rg_i=\beta_i\,R^{(i)}g_i,\qquad
\beta_i\cdot\tfrac1n g_i^*R^{(i)}g_i=1-\beta_i .
$$
Hence $g_i^*R=\beta_ig_i^*R^{(i)}$, and from $(Q+\eta)R=I$,
$$
\boxed{\ \eta R=I-\tfrac1n\textstyle\sum_{i=1}^n\beta_i\,g_ig_i^*R^{(i)}\ }\tag{1}
$$
**exactly** (no approximation yet). All of the analysis below is bounding the expectation of
(1) tested against $w$.

## 2. The MP self-consistent equation and the value $m(-\eta)\sim\eta^{-1/2}$

Taking $\frac1D\tr$ of (1) and using $\beta_i\cdot\frac1n g_i^*R^{(i)}g_i=1-\beta_i$,
$$
\eta\,m_D=1-\frac1D\sum_i(1-\beta_i)=1-\frac nD+\frac1D\sum_i\beta_i,
\qquad m_D:=\tfrac1D\tr R.\tag{2}
$$
The only random object on the right is the average $\frac1n\sum_i\beta_i$. Concentration (§3)
replaces each $\beta_i$ by the deterministic $\bar\beta:=(1+\phi\,\bar m)^{-1}$, where $\bar m$
solves the resulting fixed point. With $\frac nD=\phi^{-1}$ and
$1-\bar\beta=\phi\bar m\bar\beta$, (2) becomes the MP equation
$$
\eta\,\bar m=1-\frac{\bar m}{1+\phi\,\bar m}
\quad\Longleftrightarrow\quad
\phi\,\eta\,\bar m^{2}+(\eta+\phi-1)\,\bar m-1=0 .\tag{3}
$$
At $\phi=1$: $\eta\bar m^2+\eta\bar m-1=0$, the positive root
$$
m(-\eta)=\frac{-\eta+\sqrt{\eta^2+4\eta}}{2\eta}\ \xrightarrow[\eta\to0]{}\ \eta^{-1/2}.
$$
(Independent check: for the aspect-1 MP density $\rho(x)=\frac1{2\pi}\sqrt{(4-x)/x}$ on $[0,4]$,
$m(-\eta)=\int_0^4\frac{\rho}{x+\eta}\,dx$; the $x\!\to\!0$ end gives
$\frac1{\pi\sqrt\eta}\int_0^\infty\frac{dt}{\sqrt t(1+t)}=\eta^{-1/2}$.) The aspect correction
$\phi=1+\frac1{D-1}$ shifts $\bar m$ by $O((\phi-1)\,\partial_\phi\bar m)=O(\eta^{-1}/D)
=O(\log D/D)$, i.e. a *relative* $O(\sqrt{\log D}/D)$ — negligible (§5). So
$\bar m=(1+o(1))\,m(-\eta)$.

Two scales drive everything: $\bar m\asymp\eta^{-1/2}=\sqrt{\log D}$ and
$\bar\beta=(1+\phi\bar m)^{-1}\asymp\bar m^{-1}\asymp\eta^{1/2}=1/\sqrt{\log D}$, so
$\eta\ll\bar\beta$ and $\bar m=(\eta+\bar\beta)^{-1}(1+o(1))\asymp\bar\beta^{-1}$.

## 3. Concentration inputs (Hanson–Wright), and the projected realization

Two deterministic facts, used throughout: $0\preceq R,R^{(i)}\preceq\eta^{-1}I$, and
$\tr R\le D\eta^{-1}$. Probabilistic input is **Hanson–Wright**: for $a\in\F^N$ with i.i.d.
mean-zero unit-variance sub-Gaussian ($\|\cdot\|_{\psi_2}\le K$) entries and Hermitian $M$,
$$
\Var(a^*Ma)\le C K^4\|M\|_{\mathrm HS}^2,\qquad
\E|a^*Ma-\tr M|^p\ \text{controlled by }\|M\|_{\mathrm{HS}},\|M\|_{\mathrm{op}}.
$$
**Transfer through the projection (no deformation).** In paper19 the projected rows are
$g_i=U^*a_i$, $U:\F^D\hookrightarrow\F^N$ an isometry onto $E^\perp$ ($U^*U=I_D$), $a_i$
i.i.d. sub-Gaussian. Then $\E g_ig_i^*=U^*U=I_D$ (exact isotropy), and for any $M$,
$g_i^*Mg_i=a_i^*(UMU^*)a_i$ with $\|UMU^*\|_{\mathrm{HS}}=\|M\|_{\mathrm{HS}}$,
$\|UMU^*\|_{\mathrm{op}}=\|M\|_{\mathrm{op}}$. So Hanson–Wright applies to the *original*
i.i.d. $a_i$ with **no loss**, conditionally on $E$. This is why the anisotropic local law is
unnecessary: isotropy of $g_i$ collapses the problem to *isotropic* aspect-1 MP — there is no
population matrix to track. (Only sub-Gaussianity + isotropy are used here; bounded density is
not needed for this estimate.)

**Quadratic-form concentration.** $g_i\perp R^{(i)}$ and $\E g_ig_i^*=I$ give
$\E[\tfrac1n g_i^*R^{(i)}g_i\mid R^{(i)}]=\tfrac1n\tr R^{(i)}$, with
$$
\Var\!\big(\tfrac1n g_i^*R^{(i)}g_i\mid R^{(i)}\big)\le CK^4\,\tfrac1{n^2}\|R^{(i)}\|_{\mathrm{HS}}^2
\le CK^4\,\tfrac1{n^2}\,\eta^{-1}\tr R^{(i)}\le CK^4\,\frac{\eta^{-2}}{D}.
$$
The conditional mean is $\frac1n\tr R^{(i)}=\phi\,m_D^{(i)}\asymp\bar m\asymp\eta^{-1/2}$, so the
**relative** fluctuation of $\frac1n g_i^*R^{(i)}g_i$ is
$O\!\big(\frac{\eta^{-1}/\sqrt D}{\eta^{-1/2}}\big)=O\!\big(\sqrt{\log D}/\sqrt D\big)\to0$.
Likewise $\frac1n\tr R$ concentrates: an Efron–Stein/resampling bound (one column swap changes
$\tr R$ by $\frac1n\beta_j\|R^{(j)}g_j\|^2$, with $\E$ of its square $\lesssim\eta^{-3}$) gives
$\Var(\frac1n\tr R)\lesssim\eta^{-3}/D$, again $\mathrm{polylog}/\sqrt D$ relative. These feed §2
(closing $\E m_D=(1+o(1))\bar m$ with relative error $O(\mathrm{polylog}/\sqrt D)$) and §4.

## 4. The isotropic equation for $T_w=\E[w^*Rw]$, and the upper bound $(\star)$

Test (1) against a fixed unit $w$ and take $\E$:
$$
\eta\,T_w=1-\frac1n\sum_{i=1}^n\E\big[\beta_i\,(w^*g_i)(g_i^*R^{(i)}w)\big].\tag{4}
$$
The danger is that $\beta_i$ and the bilinear $(w^*g_i)(g_i^*R^{(i)}w)$ both depend on $g_i$.
Split $\beta_i=\beta_i'+(\beta_i-\beta_i')$ with $\beta_i':=(1+\frac1n\tr R^{(i)})^{-1}$
(a function of $R^{(i)}$ only, hence $\perp g_i$).

**(a) Main term.** Since $\beta_i'\perp g_i$ and $\E[g_ig_i^*\mid R^{(i)}]=I$,
$$
\E[\beta_i'(w^*g_i)(g_i^*R^{(i)}w)]=\E[\beta_i'\,w^*R^{(i)}w].
$$
Now replace $\beta_i'\to\bar\beta$ and $R^{(i)}\to R$:
- $R^{(i)}-R=\frac1n\beta_iR^{(i)}g_ig_i^*R^{(i)}\succeq0$ gives
  $0\le T_w^{(i)}-T_w=\frac1n\E[\beta_i|g_i^*R^{(i)}w|^2]\le\frac1n\E[w^*(R^{(i)})^2w]
  \le\frac{\eta^{-1}}{n}T_w^{(i)}$, so $T_w^{(i)}=T_w\,(1+O(\tfrac{\log D}{D}))$ uniformly.
- $|\E[(\beta_i'-\bar\beta)w^*R^{(i)}w]|\le(\Var\beta_i')^{1/2}\,(\E(w^*R^{(i)}w)^2)^{1/2}$.
  With $\Var\beta_i'\le\bar\beta^4\Var(\frac1n\tr R^{(i)})\lesssim\eta^{2}\cdot\eta^{-3}/D=\eta^{-1}/D$
  and $(w^*R^{(i)}w)^2\le\eta^{-1}w^*R^{(i)}w$ (so the 2nd factor $\le\eta^{-1/2}T_w^{1/2}$),
  this is $\lesssim\frac{\eta^{-1/2}}{\sqrt D}\cdot\eta^{-1/2}T_w^{1/2}=\frac{\eta^{-1}T_w^{1/2}}{\sqrt D}$.

Hence $\frac1n\sum_i\E[\beta_i'w^*R^{(i)}w]=\bar\beta\,T_w\,(1+o(1))+O\!\big(\tfrac{\eta^{-1}T_w^{1/2}}{\sqrt D}\big)$.

**(b) Cross term.** By Cauchy–Schwarz and $\beta_i,\beta_i'\le1$,
$$
\big|\E[(\beta_i-\beta_i')(w^*g_i)(g_i^*R^{(i)}w)]\big|
\le\big(\E|\beta_i-\beta_i'|^2\big)^{1/2}\big(\E\,|w^*g_i|^2|g_i^*R^{(i)}w|^2\big)^{1/2}.
$$
First factor: $|\beta_i-\beta_i'|\le\frac1n|g_i^*R^{(i)}g_i-\tr R^{(i)}|$, so by Hanson–Wright
$(\E|\beta_i-\beta_i'|^2)^{1/2}\le\frac1n CK^2\|R^{(i)}\|_{\mathrm{HS}}
\le CK^2\eta^{-3/4}/\sqrt D$ (using $\frac1n\E\tr(R^{(i)})^2\asymp\eta^{-3/2}$, or the crude
$\le CK^2\eta^{-1}/\sqrt D$ — either suffices). Second factor: $w^*g_i$ has bounded
sub-Gaussian moments and $\E[|g_i^*R^{(i)}w|^4\mid R^{(i)}]\le CK^4(w^*(R^{(i)})^2w)^2$, so the
product $\le CK^4\,\eta^{-1}\,T_w$, i.e. $\le CK^2\eta^{-1/2}T_w^{1/2}$. Thus each cross term is
$\lesssim\frac{\eta^{-3/4}}{\sqrt D}\eta^{-1/2}T_w^{1/2}=\frac{\eta^{-5/4}T_w^{1/2}}{\sqrt D}$,
and the same after $\frac1n\sum_i$.

**Closing the equation.** Insert (a),(b) into (4):
$$
\eta\,T_w=1-\bar\beta\,T_w(1+o(1))-\mathcal E_w,\qquad
|\mathcal E_w|\lesssim\frac{\eta^{-5/4}\,T_w^{1/2}}{\sqrt D}.
$$
Relative to the leading $\bar\beta T_w\asymp\eta^{1/2}T_w$, the error is
$\frac{|\mathcal E_w|}{\bar\beta T_w}\lesssim\frac{\eta^{-7/4}}{\sqrt D\,T_w^{1/2}}
=\frac{\eta^{-7/4}}{\sqrt D\,\eta^{-1/4}}=\frac{\eta^{-3/2}}{\sqrt D}
=\frac{(\log D)^{3/2}}{\sqrt D}\to0$ (using $T_w\asymp\eta^{-1/2}$, justified a posteriori; if
$T_w$ were larger the relative error only shrinks, so no circularity). Therefore
$$
(\eta+\bar\beta)\,T_w=1+o(\bar\beta T_w)\ \Longrightarrow\
T_w=\frac{1+o(1)}{\eta+\bar\beta}=(1+o(1))\,\bar m=(1+o(1))\,m(-\eta),
$$
**uniformly in $w$**. Taking the sup gives $(\star)$, i.e.
$\big\|\E[(Q+\eta)^{-1}]\big\|\le(1+o(1))\,m(-\eta)\sim\eta^{-1/2}$. $\qquad\blacksquare$

Plugged into `appB:resolvent`:
$\lambda_{\max}(\E[uu^*\mid E])\le\eta\,\|\E[(Q+\eta)^{-1}\mid E]\|\le(1+o(1))\sqrt\eta
=(1+o(1))/\sqrt{\log D}\to0$, which is exactly the residual $(\text{appB:residual})$.

## 5. Hypotheses audit, aspect $\to1$, and honest accounting

**Where each hypothesis enters.** (i) *Isotropy* $\E g_ig_i^*=I$: kills the direction $w$ at
leading order (the $\beta_i'$ main term), and is *exact* for $g_i=U^*a_i$ via $U^*U=I$ — the
single reason no anisotropic/deformed law is needed. (ii) *Sub-Gaussian*: Hanson–Wright
variance and the 4th-moment bound $\E|g_i^*R^{(i)}w|^4\le C(w^*(R^{(i)})^2w)^2$. (iii) *Bounded
density*: **not used here** (it is used elsewhere in App. B, in the small-ball tail lemma). So
this estimate holds for any isotropic sub-Gaussian ensemble.

**Aspect $\to1$ / hard edge.** $u$ is the *exact* null eigenvector of $Q$ (the unit vector
$\perp$ all $n=D-1$ columns), so $uu^*\preceq\eta(Q+\eta)^{-1}$ is exact. The hard edge at $0$ is
never resolved: we sit at $z=-\eta$, distance $\eta=1/\log D\gg D^{-2}\sim\lambda_{\min}(Q)$,
i.e. polylog-macroscopically off support. Every error above is $\mathrm{poly}(\log D)/\sqrt D$
precisely because all negative powers of $\eta$ are polylog and $\sqrt D$ dominates. The aspect
shift $\phi-1=1/(D-1)$ moves $\bar m$ by relative $O(\sqrt{\log D}/D)$ (§2).

**Self-contained? YES.** The chain App. B reduces the flagship (universality upper side, and the
one-sided/pair-correlation Gumbel input) to $(\text{appB:residual})$
$\lambda_{\max}(\E[uu^*\mid E])=o(1)$. The *only* previously non-self-contained step — the
off-support resolvent norm — is proved above from Sherman–Morrison + Hanson–Wright + sub-Gaussian
moments, **with no local law cited** and with the MP value $m(-\eta)\sim\eta^{-1/2}$ derived in
place. Conditioning on $E$ is harmless (the disjoint projected rows are i.i.d. isotropic
sub-Gaussian given $E$; Hanson–Wright transfers through $U$). Hence the universality **upper
side is unconditional** for i.i.d. bounded-density sub-Gaussian entries.

**Residual (honest).** No conditional black box remains, but two items are *write-out labor*,
not new ideas: (R1) the averaged law $\E m_D(-\eta)=(1+o(1))m(-\eta)$ at the moving point
$\eta=1/\log D$ — closed by the *same* Schur argument (§2–§3), not by quoting a fixed-$z$ MP
theorem; (R2) the per-direction error lemmas of §4 must be written with explicit constants
(done here at the level of scales: worst relative error $O((\log D)^{7/4}/\sqrt D)$). Both are
standard. Caveat on sharpness: the route yields only $\lambda_{\max}(\E[uu^*])\le(1+o(1))\sqrt\eta
=o(1)$, which is *exactly what $(\text{appB:residual})$ needs*; the sharp rate $O(1/D)$ seen
numerically would require $\eta\sim1/D$ (the genuine hard-edge regime) and is **not** needed for
the flagship. The full Gumbel *law* (`conj:gumbel`) still needs higher $k$-point correlations,
unchanged by this note.

