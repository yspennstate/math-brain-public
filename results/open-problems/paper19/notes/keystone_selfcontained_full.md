# Off-support resolvent law, fully rigorous (constants explicit)

This note replaces the "routine bookkeeping" deferred in Remark `appB:selfcontained`
and items (R1),(R2) of `keystone_selfcontained.md` by a complete proof with named
constants. Nothing below cites a local law; the only external input is the
Hanson–Wright variance bound (Rudelson–Vershynin 2013), used in the elementary
variance form, which we restate and which is allowed.

## 0. Model, hypotheses, statement

Fix the field $\F\in\{\R,\C\}$, $d_\F=\dim_\R\F\in\{1,2\}$. We work in the
**projected-iid model** that App. B actually produces (this matters; see §6):
there is an isometry $U:\F^D\hookrightarrow\F^N$ with $U^*U=I_D$ and i.i.d. vectors
$a_1,\dots,a_n\in\F^N$ ($n:=D-1$) whose **entries** are independent, mean zero, unit
variance, sub-Gaussian with $\max_k\|a_{1,k}\|_{\psi_2}\le K$ (real symmetric / complex
circular law), and the working vectors are
$$
 g_i \;=\; U^* a_i\in\F^D,\qquad i=1,\dots,n .
$$
Then $g_i$ are i.i.d. and **exactly isotropic**, $\E\, g_ig_i^* = U^*\E[a_ia_i^*]\,U=U^*U=I_D$.
Set
$$
 Q=\frac1n\sum_{i=1}^n g_ig_i^*,\qquad \phi:=\frac Dn=1+\frac1{D-1},\qquad
 \eta=\frac1{\log D},\qquad R:=(Q+\eta)^{-1}\succ0 .
$$
Let $m(-\eta)=\dfrac{\sqrt{\eta^2+4\eta}-\eta}{2\eta}$ be the aspect-one Marchenko–Pastur
(MP) Stieltjes transform at $z=-\eta$; as $\eta\to0$, $m(-\eta)=\eta^{-1/2}-\tfrac12+O(\eta^{1/2})\sim\eta^{-1/2}$.

> **Theorem (off-support resolvent law).** There is $C=C(K)<\infty$, depending only on the
> sub-Gaussian parameter $K$ (and through $d_\F$ on the field), such that for all $D$ large,
> $$
>  \sup_{\|w\|=1}\Big|\;\E\big[\langle w,(Q+\eta)^{-1}w\rangle\big]-m(-\eta)\;\Big|
>  \;\le\; C\,\frac{(\log D)^{7/4}}{\sqrt D}\,\;m(-\eta).
> $$
> Consequently $\big\|\E[(Q+\eta)^{-1}]\big\|=\lambda_{\max}\big(\E[(Q+\eta)^{-1}]\big)
> =(1+o(1))\,m(-\eta)\sim\eta^{-1/2}=\sqrt{\log D}$, and via
> $uu^*\preceq\eta(Q+\eta)^{-1}$ (Prop. `appB:resolvent`),
> $\lambda_{\max}(\E[uu^*\mid E])\le(1+o(1))\sqrt\eta=(1+o(1))/\sqrt{\log D}\to0$,
> which is exactly residual `appB:residual`.

Bounded density of the entry law is **not used** in this estimate (only isotropy +
sub-Gaussianity enter); it is used elsewhere in App. B (Lemma `appB:tail`).

Notation: $\|M\|$ is the operator norm, $\|M\|_F=(\tr M^*M)^{1/2}$ the Frobenius norm,
$C,C',c$ absolute constants that may change line to line, all numerical and traceable.
## 1. Exact leave-one-out identities (Sherman–Morrison)

Write $Q^{(i)}=\frac1n\sum_{j\ne i}g_jg_j^*$, $R^{(i)}=(Q^{(i)}+\eta)^{-1}$, so that
$Q+\eta=(Q^{(i)}+\eta)+\frac1n g_ig_i^*$ is a rank-one update of $Q^{(i)}+\eta$. Define the
scalar
$$
 \beta_i:=\frac{1}{1+\frac1n g_i^*R^{(i)}g_i}\in(0,1].
$$
Sherman–Morrison, $(A+\tfrac1n vv^*)^{-1}=A^{-1}-\dfrac{\tfrac1n A^{-1}vv^*A^{-1}}{1+\tfrac1n v^*A^{-1}v}$
with $A=Q^{(i)}+\eta$, $v=g_i$, gives the **exact** identities (no error term):
$$
 R=R^{(i)}-\tfrac1n\beta_i\,R^{(i)}g_ig_i^*R^{(i)},\qquad
 Rg_i=\beta_i\,R^{(i)}g_i,\qquad
 \beta_i\cdot\tfrac1n g_i^*R^{(i)}g_i=1-\beta_i. \tag{1.1}
$$
*Proof of the middle/right relations.*
$Rg_i=R^{(i)}g_i-\tfrac1n\beta_iR^{(i)}g_i(g_i^*R^{(i)}g_i)
=R^{(i)}g_i\big(1-\tfrac1n\beta_i g_i^*R^{(i)}g_i\big)$, and
$1-\tfrac1n\beta_ig_i^*R^{(i)}g_i=1-(1-\beta_i)=\beta_i$ by the definition of $\beta_i$
(which rearranges to $\tfrac1n\beta_ig_i^*R^{(i)}g_i=1-\beta_i$). $\square$

Taking adjoints, $g_i^*R=\beta_ig_i^*R^{(i)}$, hence $g_ig_i^*R=\beta_ig_ig_i^*R^{(i)}$.
From $(Q+\eta)R=I$, i.e. $\eta R=I-QR=I-\frac1n\sum_i g_ig_i^*R$,
$$
 \boxed{\;\eta R=I-\frac1n\sum_{i=1}^n \beta_i\,g_ig_i^*R^{(i)}\;}\tag{1.2}
$$
**exactly**. Two deterministic facts used repeatedly:
$$
 0\preceq R,\,R^{(i)}\preceq\eta^{-1}I,\qquad
 \|R^{(i)}\|\le\eta^{-1},\qquad
 \|R^{(i)}\|_F\le \tr(R^{(i)})^{1/2}\,\eta^{-1/2}\le \sqrt D\,\eta^{-1}, \tag{1.3}
$$
the last since $\|R^{(i)}\|_F^2=\tr(R^{(i)})^2\le\|R^{(i)}\|\,\tr R^{(i)}\le\eta^{-1}\cdot D\eta^{-1}$.

**Normalized trace.** Apply $\frac1D\tr$ to (1.2). Since
$\tr(g_ig_i^*R^{(i)})=g_i^*R^{(i)}g_i$ and $\frac1n\beta_i g_i^*R^{(i)}g_i=1-\beta_i$,
$$
 \eta\,m_D=1-\frac1D\sum_{i=1}^n(1-\beta_i)=1-\frac nD+\frac1D\sum_{i=1}^n\beta_i,
 \qquad m_D:=\tfrac1D\tr R. \tag{1.4}
$$
This is exact; the only randomness on the right is $\frac1n\sum_i\beta_i$.
## 2. Hanson–Wright, in exact variance form, and the projection transfer

**Lemma 2.1 (quadratic-form variance; Rudelson–Vershynin 2013, elementary form).**
Let $a\in\F^N$ have independent entries, mean $0$, $\E|a_k|^2=1$, with
$\mu_4:=\sup_k\E|a_k|^4\le C_4K^4$ ($C_4$ absolute, finite since sub-Gaussian).
For any Hermitian $M\in\F^{N\times N}$,
$$
 \E[a^*Ma]=\tr M,\qquad
 \Var(a^*Ma)\;\le\; b_\F\,\|M\|_F^2,\qquad b_\F:=\big(2+|\,\mu_4-d_\F-1\,|\big)\le C_{\mathrm{HW}}K^4 .
\tag{2.1}
$$
*Real case ($\F=\R$, $M=M^\top$).* The exact identity is
$\Var(a^\top Ma)=2\tr(M^2)+(\mu_4-3)\sum_kM_{kk}^2$. Since $\sum_kM_{kk}^2\le\|M\|_F^2=\tr(M^2)$,
$\Var\le(2+|\mu_4-3|)\|M\|_F^2$. *Complex circular case* gives
$\Var=\tr(MM^*)+|\,\E a_k^2\,|^2(\dots)+(\mu_4-2)\sum_k|M_{kk}|^2$ with $\E a_k^2=0$, so
$\Var\le(2+|\mu_4-2|)\|M\|_F^2$ ($d_\F=2$). In both cases the constant is explicit and
$\le C_{\mathrm{HW}}K^4$ with $C_{\mathrm{HW}}$ absolute (using $\mu_4\le C_4K^4$ and $K\ge c_0$
forced by unit variance). $\square$

We will only need (2.1) and, once, the matching fourth-moment bound for a linear form:
for a deterministic $c\in\F^N$,
$$
 \E|a^*c|^2=\|c\|^2,\qquad \E|a^*c|^4\le C_4'K^4\|c\|^4. \tag{2.2}
$$
(Both are standard sub-Gaussian linear-form moments; $C_4'$ absolute.)

**Transfer through $U$ (no loss).** For $M$ acting on $\F^D$,
$$
 g_i^*Mg_i=a_i^*\,(UMU^*)\,a_i,\qquad
 \|UMU^*\|_F=\|M\|_F,\quad \|UMU^*\|=\|M\|, \tag{2.3}
$$
because $U^*U=I_D$ gives $\tr\big((UMU^*)^2\big)=\tr\big(UM^2U^*\big)=\tr(M^2U^*U)=\tr(M^2)$.
Thus a quadratic form in the **dependent**-coordinate vector $g_i=U^*a_i$ equals a quadratic
form in the **independent**-coordinate vector $a_i$, and Lemma 2.1 applies to $a_i$ with $M':=UMU^*$
**with no loss**. *This is the one place where the projected-iid structure is essential*: $g_i$ alone
need not have independent coordinates, so Hanson–Wright cannot be applied to it directly (see §6).
Conditionally on the isometry $E$ and on $\{a_j\}_{j\ne i}$, the matrix $M'=UR^{(i)}U^*$ is
deterministic and $a_i$ is independent of it; (2.1)–(2.3) then apply conditionally.

**Corollary 2.2 (quadratic-form concentration).** Writing $s_i:=\frac1n g_i^*R^{(i)}g_i$ and
$t_i:=\frac1n\tr R^{(i)}=\phi\, m_D^{(i)}$ (with $m_D^{(i)}:=\frac1D\tr R^{(i)}$), we have
$\E[s_i\mid R^{(i)}]=t_i$ and, by (2.1) and (1.3),
$$
 \Var(s_i\mid R^{(i)})\le \frac{b_\F}{n^2}\|R^{(i)}\|_F^2\le \frac{b_\F\,\eta^{-2}\,D}{n^2}
 \le \frac{2\,b_\F\,\eta^{-2}}{D}\qquad(\text{using }D/n^2\le2/D). \tag{2.4}
$$
## 3. Trace concentration, the MP fixed point, and the averaged law (item R1)

**Lemma 3.1 (deterministic one-swap bound).** For each $j$,
$$
 0\;\le\;\tr R^{(j)}-\tr R\;=\;\tfrac1n\beta_j\|R^{(j)}g_j\|^2\;\le\;\eta^{-1}. \tag{3.1}
$$
*Proof.* The equality is the trace of the first identity in (1.1) (with
$\tr(R^{(j)}g_jg_j^*R^{(j)})=\|R^{(j)}g_j\|^2$). For the bound: $Q=Q^{(j)}+\frac1n g_jg_j^*$ is a
rank-one PSD perturbation, so the eigenvalues interlace,
$\lambda_1\ge\mu_1\ge\lambda_2\ge\mu_2\ge\cdots\ge\lambda_D\ge\mu_D\ge0$, where
$\lambda_k=\lambda_k(Q)$, $\mu_k=\lambda_k(Q^{(j)})$ (decreasing). Since $x\mapsto(x+\eta)^{-1}$
is decreasing,
$$
 \tr R^{(j)}-\tr R=\sum_{k=1}^D\big[(\mu_k+\eta)^{-1}-(\lambda_k+\eta)^{-1}\big]\ge0,
$$
and using $\mu_k\ge\lambda_{k+1}$ ($k<D$), $\mu_D\ge0$,
$\sum_k(\mu_k+\eta)^{-1}\le\sum_{k=2}^D(\lambda_k+\eta)^{-1}+\eta^{-1}$, whence the difference is
$\le\eta^{-1}-(\lambda_1+\eta)^{-1}\le\eta^{-1}$. $\square$

**Corollary 3.2 (trace concentration; explicit).** The $g_1,\dots,g_n$ are independent, and
resampling $g_j\to g_j'$ changes $\tr R$ by $\le\eta^{-1}$ in absolute value (both values lie in
$[\tr R^{(j)}-\eta^{-1},\tr R^{(j)}]$ by (3.1)). Hence by Efron–Stein,
$\Var(\tr R)\le\frac12\sum_{j=1}^n\eta^{-2}=\frac n2\eta^{-2}$, i.e.
$$
 \Var(m_D)\le\frac{n}{2D^2}\eta^{-2}\le\frac{\eta^{-2}}{2D},
 \qquad
 \PP\big(|m_D-\E m_D|>t\big)\le2\exp\!\Big(-\frac{2D^2t^2}{n\eta^{-2}}\Big), \tag{3.2}
$$
the tail by McDiarmid (bounded differences $\eta^{-1}$). The same holds for $m_D^{(i)}$ with $n-1$
in place of $n$. Thus $m_D$ concentrates around $\E m_D$ with std $\le\eta^{-1}/\sqrt{2D}$;
relative to the scale $m_D\asymp\eta^{-1/2}$ established below this is $O(\sqrt{\log D/D})$, and
whp $m_D=(1+O(\sqrt{\log D/D}\cdot\sqrt{\log\log D}))\,\E m_D$.

**The MP fixed point.** Let $\bar m$ be the positive root of the aspect-$\phi$ self-consistent
equation obtained by replacing $\beta_i$ in (1.4) by $(1+\phi\bar m)^{-1}=:\bar\beta$:
$$
 \eta\bar m=1-\frac nD+\frac nD\,\bar\beta
 \;\Longleftrightarrow\;
 \eta\bar m=1-\frac{\bar m}{1+\phi\bar m}
 \;\Longleftrightarrow\;
 \phi\eta\,\bar m^2+(\eta-\phi+1)\,\bar m-1=0, \tag{3.3}
$$
equivalently $(\eta+\bar\beta)\,\bar m=1$, i.e. $\boxed{\;\bar m=(\eta+\bar\beta)^{-1}\;}$ and
$1-\bar\beta=\phi\bar m\bar\beta$. At $\phi=1$: $\eta\bar m^2+\eta\bar m-1=0$, root
$\bar m=m(-\eta)$. Scales: $\bar m\asymp\eta^{-1/2}$, $\bar\beta=(1+\phi\bar m)^{-1}\asymp\eta^{1/2}$,
so $\eta\ll\bar\beta$ and $\bar m=(\eta+\bar\beta)^{-1}\asymp\bar\beta^{-1}\asymp\eta^{-1/2}$.
The aspect shift is negligible: implicit differentiation of (3.3) gives
$|\partial_\phi\bar m|\asymp(2\eta)^{-1}$ near $\phi=1$, so
$\bar m=m(-\eta)\big(1+O((\phi-1)\eta^{-1}/\bar m)\big)=m(-\eta)\big(1+O(\sqrt{\log D}/D)\big)$.

**Averaged law (closes R1).** Let $\mu:=\E m_D$, $\bar t:=\phi\,\E m_D=\phi\mu$, $f(x):=(1+x)^{-1}$
($0\le-f'\le1$, $0\le f''\le2$ on $x\ge0$). Then $\E\beta_i=\E f(s_i)$, and we compare to
$f(\bar t)=(1+\phi\mu)^{-1}$:
$$
 |\E\beta_i-f(\bar t)|\le\underbrace{|\E[f(s_i)-f(t_i)]|}_{\text{(A)}}
 +\underbrace{|\E[f(t_i)-f(\bar t)]|}_{\text{(B)}}.
$$
*(A)* Conditioning on $R^{(i)}$ (so $\E[s_i-t_i\mid R^{(i)}]=0$) and Taylor with $0\le f''\le2$,
$|\E[f(s_i)-f(t_i)\mid R^{(i)}]|\le\Var(s_i\mid R^{(i)})\le 2b_\F\eta^{-2}/D$ by (2.4); take $\E$.
*(B)* $\E[t_i-\bar t]=\phi\,\E(m_D^{(i)}-m_D)$, and by (3.1) $0\le m_D^{(i)}-m_D\le\eta^{-1}/D$, so
$|\E[t_i-\bar t]|\le\eta^{-1}/D$; the quadratic Taylor term is
$\le\E|t_i-\bar t|^2=\Var(t_i)+(\E t_i-\bar t)^2\le\phi^2\eta^{-2}/(2(n-1))+\eta^{-2}/D^2\le 2\eta^{-2}/D$.
Hence
$$
 |\E\beta_i-(1+\phi\mu)^{-1}|\le C_1\,b_\F\,\frac{\eta^{-2}}{D}\quad(\forall i),\qquad
 C_1\ \text{absolute}. \tag{3.4}
$$
Insert into the expectation of (1.4): with $\Phi(x):=1-\tfrac nD+\tfrac nD(1+\phi x)^{-1}-\eta x$,
(3.4) gives $|\Phi(\mu)|=\big|\,\eta\mu-1+\tfrac nD-\tfrac1D\sum_i\E\beta_i\,\big|
\le C_1 b_\F\eta^{-2}/D=:\epsilon_D$, while $\Phi(\bar m)=0$. Since
$\Phi'(x)=-(1+\phi x)^{-2}-\eta\le-\eta<0$ for all $x\ge0$, the mean value theorem yields
$$
 |\,\E m_D-\bar m\,|=|\mu-\bar m|\le\frac{|\Phi(\mu)-\Phi(\bar m)|}{\inf|\Phi'|}\le\frac{\epsilon_D}{\eta}
 =C_1b_\F\frac{\eta^{-3}}{D},
 \quad\text{i.e.}\quad
 \E m_D=\bar m\Big(1+O\!\big(b_\F\tfrac{(\log D)^{5/2}}{D}\big)\Big). \tag{3.5}
$$
The lower bound $\inf|\Phi'|\ge\eta$ is the rigorous form of "fixed-point stability at the
off-support point"; no contractivity of the naive iteration is needed (indeed its derivative is
$\asymp1$, which is exactly why we use the $\Phi$-formulation with $|\Phi'|\ge\eta$).
## 4. The direction-uniform law for $T_w=\E[w^*Rw]$ (item R2, with constants)

Fix a unit $w$. Testing (1.2) against $w$ and taking $\E$ (note
$w^*g_ig_i^*R^{(i)}w=(w^*g_i)(g_i^*R^{(i)}w)$):
$$
 \eta\,T_w=1-\frac1n\sum_{i=1}^n\E\big[\beta_i\,(w^*g_i)(g_i^*R^{(i)}w)\big],
 \qquad T_w:=\E[w^*Rw]. \tag{4.1}
$$
Both $\beta_i$ and the bilinear form depend on $g_i$. Split $\beta_i=\beta_i'+(\beta_i-\beta_i')$
with $\beta_i':=(1+t_i)^{-1}=(1+\tfrac1n\tr R^{(i)})^{-1}$, a function of $R^{(i)}$ **only**
(independent of $g_i$).

Two a priori facts. (i) $T_w\le\eta^{-1}$ deterministically. (ii) Monotone removal: from (1.1),
$w^*R^{(i)}w-w^*Rw=\frac1n\beta_i|g_i^*R^{(i)}w|^2\ge0$, and
$\E[|g_i^*R^{(i)}w|^2\mid R^{(i)}]=w^*(R^{(i)})^2w\le\eta^{-1}w^*R^{(i)}w$, so with $T_w^{(i)}:=\E[w^*R^{(i)}w]$,
$$
 0\le T_w^{(i)}-T_w=\tfrac1n\E[\beta_i|g_i^*R^{(i)}w|^2]\le\tfrac{\eta^{-1}}{n}T_w^{(i)}
 \;\Rightarrow\;
 T_w\le T_w^{(i)}\le T_w\big(1-\tfrac{\eta^{-1}}{n}\big)^{-1}=T_w\big(1+O(\tfrac{\log D}{D})\big), \tag{4.2}
$$
uniformly in $i,w$ (since $\eta^{-1}/n=\frac{\log D}{D-1}\to0$).

**(a) Main term.** Because $\beta_i'R^{(i)}$ is $\perp g_i$ and $\E[g_ig_i^*\mid\{g_j\}_{j\ne i}]=I$
(exact isotropy),
$$
 \E\big[\beta_i'(w^*g_i)(g_i^*R^{(i)}w)\big]=\E\big[\beta_i'\,w^*\E[g_ig_i^*]\,R^{(i)}w\big]
 =\E\big[\beta_i'\,w^*R^{(i)}w\big]. \tag{4.3}
$$
This identity is **exact** and is where isotropy kills the $w$-dependence of the leading term.
Now replace $\beta_i'\to\bar\beta$: with $|\beta_i'-\bar\beta|\le|t_i-\bar t|$ ($|f'|\le1$) and the
already-bounded $\E|t_i-\bar t|^2\le2\eta^{-2}/D$ (from (B) above, $\bar t=\phi\bar m$ vs $\phi\mu$
differ by $O(\eta^{-3}/D)$, lower order),
$$
 \big|\E[(\beta_i'-\bar\beta)w^*R^{(i)}w]\big|
 \le\big(\E|\beta_i'-\bar\beta|^2\big)^{1/2}\big(\E(w^*R^{(i)}w)^2\big)^{1/2}
 \le \frac{\sqrt2\,\eta^{-1}}{\sqrt D}\cdot\eta^{-1/2}(T_w^{(i)})^{1/2}, \tag{4.4}
$$
using $(w^*R^{(i)}w)^2\le\eta^{-1}(w^*R^{(i)}w)$ so $\E(w^*R^{(i)}w)^2\le\eta^{-1}T_w^{(i)}$. By (4.2),
$\bar\beta\,T_w^{(i)}=\bar\beta T_w(1+O(\tfrac{\log D}{D}))$. Hence
$$
 \E[\beta_i'\,w^*R^{(i)}w]=\bar\beta\,T_w\big(1+O(\tfrac{\log D}{D})\big)
 +O\!\Big(\frac{\eta^{-3/2}T_w^{1/2}}{\sqrt D}\Big). \tag{4.5}
$$

**(b) Cross term.** By Cauchy–Schwarz,
$$
 \big|\E[(\beta_i-\beta_i')(w^*g_i)(g_i^*R^{(i)}w)]\big|
 \le\big(\E|\beta_i-\beta_i'|^2\big)^{1/2}\big(\E\,|w^*g_i|^2|g_i^*R^{(i)}w|^2\big)^{1/2}. \tag{4.6}
$$
*First factor.* $|\beta_i-\beta_i'|\le|s_i-t_i|=\frac1n|g_i^*R^{(i)}g_i-\tr R^{(i)}|$, so by (2.4),
$\E|\beta_i-\beta_i'|^2\le\E\,\Var(s_i\mid R^{(i)})\le2b_\F\eta^{-2}/D$; first factor
$\le\sqrt{2b_\F}\,\eta^{-1}/\sqrt D$.
*Second factor.* Condition on $R^{(i)}$ and use Cauchy–Schwarz in $g_i$ then (2.2) (with
$w^*g_i=(Uw)^*a_i$, $\|Uw\|=1$, and $g_i^*R^{(i)}w=(UR^{(i)}w)^*a_i$, $\|UR^{(i)}w\|=\|R^{(i)}w\|$):
$$
 \E[|w^*g_i|^2|g_i^*R^{(i)}w|^2\mid R^{(i)}]
 \le\big(\E|w^*g_i|^4\big)^{1/2}\big(\E|g_i^*R^{(i)}w|^4\big)^{1/2}
 \le C_4'K^4\,\|R^{(i)}w\|^2,
$$
and $\|R^{(i)}w\|^2=w^*(R^{(i)})^2w\le\eta^{-1}w^*R^{(i)}w$, so the second factor in (4.6) is
$\le (C_4'K^4)^{1/2}\eta^{-1/2}(T_w^{(i)})^{1/2}$. Therefore each cross term is
$$
 \big|\E[(\beta_i-\beta_i')(\cdots)]\big|\le C_2K^2\sqrt{b_\F}\,\frac{\eta^{-3/2}T_w^{1/2}}{\sqrt D},
 \qquad C_2\ \text{absolute}. \tag{4.7}
$$

**Closing the equation.** Summing (4.5),(4.7) over $i$ (the $\frac1n\sum_i$ averages, sizes uniform)
and inserting into (4.1):
$$
 \eta\,T_w=1-\bar\beta\,T_w\big(1+O(\tfrac{\log D}{D})\big)
 +\mathcal E_w,\qquad
 |\mathcal E_w|\le C_3K^2\sqrt{b_\F}\,\frac{\eta^{-3/2}T_w^{1/2}}{\sqrt D},
$$
i.e., using $\bar m=(\eta+\bar\beta)^{-1}$,
$$
 (\eta+\bar\beta)\,T_w=1+\mathcal E_w',\qquad
 |\mathcal E_w'|\le C\Big(\tfrac{\log D}{D}\,\bar\beta T_w+K^2\sqrt{b_\F}\,\tfrac{\eta^{-3/2}T_w^{1/2}}{\sqrt D}\Big).
 \tag{4.8}
$$

**Bootstrap (no circularity).** Use only the a priori $T_w\le\eta^{-1}$ to bound the right side of
(4.8): $\frac{\log D}{D}\bar\beta T_w\le\frac{\log D}{D}\eta^{1/2}\eta^{-1}=\frac{(\log D)^{3/2}}{D}$ and
$K^2\sqrt{b_\F}\frac{\eta^{-3/2}T_w^{1/2}}{\sqrt D}\le K^2\sqrt{b_\F}\frac{\eta^{-2}}{\sqrt D}
=K^2\sqrt{b_\F}\frac{(\log D)^2}{\sqrt D}$. Both $\to0$, so $|\mathcal E_w'|=o(1)$ and
$(\eta+\bar\beta)T_w=1+o(1)$, giving $T_w=\bar m(1+o(1))\asymp\eta^{-1/2}$. **Re-inserting**
$T_w\asymp\eta^{-1/2}$ (hence $T_w^{1/2}\asymp\eta^{-1/4}$, $\bar\beta T_w\asymp1$) into (4.8) sharpens
the error to
$$
 |\mathcal E_w'|\le C\Big(\tfrac{\log D}{D}+K^2\sqrt{b_\F}\,\tfrac{\eta^{-7/4}}{\sqrt D}\Big)
 \le C'K^4\,\frac{(\log D)^{7/4}}{\sqrt D}, \tag{4.9}
$$
the second term dominating. Therefore, **uniformly in $\|w\|=1$**,
$$
 T_w=\bar m\Big(1+O\!\big(K^4\tfrac{(\log D)^{7/4}}{\sqrt D}\big)\Big)
 =m(-\eta)\Big(1+O\!\big(K^4\tfrac{(\log D)^{7/4}}{\sqrt D}\big)\Big), \tag{4.10}
$$
the last step by the aspect estimate $\bar m=m(-\eta)(1+O(\sqrt{\log D}/D))$ of §3. This is the
Theorem; taking $\sup_w$ and using $\E[R]\succeq0$ Hermitian gives
$\lambda_{\max}(\E R)=\sup_wT_w=(1+o(1))m(-\eta)$.
## 5. Regime check and the error budget

**$\eta=1/\log D$ is in the valid off-support regime.** The hard edge of $Q$ is at $0$: with
$n=D-1<D$, $Q$ has an exact null vector $u$ ($\lambda_{\min}(Q)=0$) and the smallest nonzero
eigenvalue is at the hard-edge scale $\sim D^{-2}$. We evaluate the resolvent at distance
$\eta=1/\log D$ from $0$, which is **macroscopically** (polylog) off the edge:
$\eta\gg D^{-2}$ and $\eta\gg$ any microscopic scale. Every negative power of $\eta$ produced
above is a power of $\log D$, dominated by $\sqrt D$. Concretely:

| quantity | value/scale | relative error proved |
|---|---|---|
| $m(-\eta)=\bar m$ | $\sim\eta^{-1/2}=\sqrt{\log D}$ | aspect: $O(\sqrt{\log D}/D)$ |
| $\E m_D$ (trace law, R1) | $\bar m$ | $O\!\big((\log D)^{5/2}/D\big)$ (3.5) |
| $\mathrm{std}(m_D)$ | $\eta^{-1}/\sqrt{2D}$ | $O(\sqrt{\log D/D})$ (3.2) |
| $T_w=\E[w^*Rw]$ (R2, uniform $w$) | $\bar m$ | $O\!\big((\log D)^{7/4}/\sqrt D\big)$ (4.10) |

The **largest** (binding) error is the direction-uniform one,
$O\!\big(K^4(\log D)^{7/4}/\sqrt D\big)$; its exponent is $7/4$ on $\log D$ and $-1/2$ on $D$.
Since $m(-\eta)\sim\sqrt{\log D}$, the absolute error is
$O\!\big(K^4(\log D)^{9/4}/\sqrt D\big)\to0$, so the $o(1)$ relative bound holds with room to spare.
Feeding into Prop. `appB:resolvent`: $\lambda_{\max}(\E[uu^*\mid E])\le\eta\|\E R\|
=(1+o(1))\eta\,m(-\eta)=(1+o(1))\sqrt\eta=(1+o(1))/\sqrt{\log D}\to0$, which is `appB:residual`.

## 6. Honest accounting: is anything left?

**No conditional black box remains.** Items (R1) (averaged law at the moving point
$\eta=1/\log D$, eq. (3.5)) and (R2) (per-direction error lemmas with constants, §4) are proved
from: the exact Sherman–Morrison identities (1.1)–(1.4); the Hanson–Wright variance bound in the
elementary form Lemma 2.1 (the single permitted citation, Rudelson–Vershynin 2013); the
deterministic interlacing bound Lemma 3.1; Efron–Stein/McDiarmid (3.2); and MVT stability
$|\Phi'|\ge\eta$ (3.5). All constants are explicit and of the form $C(K)=\mathrm{poly}(K)$ with
$K$-dependence entering as $K^4$ (two quadratic forms). The MP value
$m(-\eta)=\frac{\sqrt{\eta^2+4\eta}-\eta}{2\eta}$ is derived in place, not quoted.

**One genuine hypothesis to state precisely (not a gap, but more than "routine").** Lemma 2.1
needs *independent coordinates*. A generic isotropic sub-Gaussian vector need **not** have them,
and Hanson–Wright can fail for such a vector. The proof uses, at (2.3), that the working vectors
are $g_i=U^*a_i$ with $a_i$ genuinely independent-coordinate sub-Gaussian — the projected-iid
structure App. B actually produces. So the Theorem is **unconditional for paper19's ensemble**, and
the honest statement of hypotheses is "projected-iid sub-Gaussian," or equivalently "isotropic
sub-Gaussian satisfying a Hanson–Wright/convex-concentration inequality," **not** the bare
"isotropic sub-Gaussian." This was already flagged in §3 of the skeleton; we make it a named
hypothesis rather than paper over it.

**Sharpness (honest).** The proved rate $O((\log D)^{7/4}/\sqrt D)$ is rigorous but not tight: the
$1/\sqrt D$ comes from Cauchy–Schwarz on the cross term (4.6)–(4.7) and on (4.4), where we used
$\E(w^*R^{(i)}w)^2\le\eta^{-1}T_w^{(i)}$ instead of the (smaller, harder) genuine variance
$\Var(w^*R^{(i)}w)$. Replacing those by an Efron–Stein bound on the single bilinear form
$w^*Rw$ would presumably yield $O(\mathrm{polylog}/D)$, matching the simulated $(1+o(1))/D$ rate
(Rademacher, $D=40$–$320$). This sharpening is **not needed**: `appB:residual` only requires
$\lambda_{\max}(\E[uu^*])=o(1)$, which $\sqrt\eta=o(1)$ already gives. We do not claim the sharp
rate.

**Least-certain ingredient.** Everything is checked; if one ingredient is to be pinned to a
reference rather than recomputed, it is the **explicit Hanson–Wright variance constant $b_\F$ in
Lemma 2.1 for the complex circular case** (eq. (2.1)). The $K^4$ form is certain and the real-case
identity $2\tr(M^2)+(\mu_4-3)\sum M_{kk}^2$ is exact; the complex Hermitian prefactor I would cite
from Rudelson–Vershynin (2013, Thm 1.1) / Hanson–Wright rather than re-derive the cumulant
bookkeeping, but it does not exceed $C_{\mathrm{HW}}K^4$ and changes no exponent above.

**Conclusion.** The off-support resolvent law is now proved in full, with explicit constants and
worst relative error $O\!\big(K^4(\log D)^{7/4}/\sqrt D\big)$, under the projected-iid sub-Gaussian
hypothesis that App. B supplies. Remark `appB:selfcontained` is thereby discharged; no local law,
and no further deferred step, is invoked.

