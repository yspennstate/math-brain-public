# B16 FEI signed transport — coset-entropy diagonal payment and terminal Hilbert ANOVA

**Date:** 21 September 2026  
**Scope:** `account03 / B16`, joint FEI interface C  
**Execution:** **WITHOUT_VERIFIED_BRAIN**  
**Status of unrestricted FEI:** **OPEN / NOT PROVED**  
**Claim level:** exact logarithmic-polarization identities, a dimension-free payment of the complete diagonal logarithmic part of the authentic retained square, and an exact terminal quotient-variance decomposition. The off-diagonal compiler-to-physical-flag contraction remains OPEN. No novelty or publication-priority claim.

## 0. Joint handoff consumed and exact implication attacked

This run follows `FEI-JOINT-FOUR-ACCOUNTS-2026-09-21-192650Z`, interface C. It consumed substantively the completed other-account artifact

`account01/B16/20260921T195223Z-square-first-window-gram/REPORT.md`

at scientific commit `cafaba72f2314eedf5b77398e3550dbf9e182eb0`, report blob `ebd532a214b9b4a293363578e0237fce636bab68`.

That result proves that the authentic retained phase-switch square may enlarge an arbitrary live Borel window to the whole half-line in PSD order, and that the full-line four-sine kernel is the exact eight-term polarization of

\[
F(x)=x^2\log|x|.
\]

It also proves that the diagonal kernel contains the unavoidable scale-separation term
\(\frac12\varepsilon^2\log(1/\varepsilon)\), so a scale-free quartic payment is impossible. Its exact remaining target is

\[
16N^2\,\mathbb E_S\sum_{r,t}\alpha_r\alpha_t
K_\infty(v_{r,S},v_{t,S})\le C J(f),
\tag{0.1}
\]

with the actual terminal weights and with the logarithmic credit retained.

The present run attacks the first nontrivial part of (0.1): **identify and pay the entire diagonal \(r=t\) logarithmic contribution without discarding dual-code multiplicity or the terminal subtraction, then rewrite the full quadratic form so the remaining off-diagonal problem exposes an explicit negative terminal variance credit.**

The physical Boolean phase is kept in the same minimizing-character gauge used by the current signed-flag/phase-switch chain, so after renaming the gauged phase back to \(f\),

\[
I(f)=J(f).
\tag{0.2}
\]

A global sign is chosen so that \(p_-:=\Pr[f=-1]\le 1/2\). This changes neither Fourier entropy nor influence.

No R32 relation is positive-parted. R16/moment refunds and the separate negative entropy credits are not spent below. The terminal subtraction remains exact.

---

## 1. Setup from the authentic retained compiler

Keep the account01 notation

\[
P_0=RM(1,n),\qquad P_1=D_d^\perp,\qquad N=2^n,
\]
\[
L=|P_1|,\qquad \rho=\frac{2N}{L},\qquad \gamma=1-\rho.
\tag{1.1}
\]

The actual retained signed weights are

\[
\alpha_r=\frac1{2N}{\bf1}_{r\in P_0}-\frac1L{\bf1}_{r\in P_1}.
\tag{1.2}
\]

Hence

\[
\alpha_r=
\begin{cases}
\gamma/(2N),&r\in P_0,\\
-\rho/(2N),&r\in P_1\setminus P_0.
\end{cases}
\tag{1.3}
\]

For a Boolean twist \(h\), let

\[
A_r^\pm=\frac1N\sum_{x:f(x)=\pm1}h(x)(-1)^{r_x},
\qquad v_r=(A_r^+,A_r^-).
\tag{1.4}
\]

The retained phase switch is

\[
R_h(s)=-4N\sum_{r\in P_1}\alpha_r
\sin(sA_r^+)\sin(sA_r^-),
\tag{1.5}
\]

and the peer square-first theorem gives, for every Borel live window \(W\subset(0,\infty)\),

\[
\int_W\frac{R_h(s)^2}{s^3}\,ds
\le
\int_0^\infty\frac{R_h(s)^2}{s^3}\,ds
=16N^2\sum_{r,t}\alpha_r\alpha_tK_\infty(v_r,v_t).
\tag{1.6}
\]

We now analyze the diagonal of this exact signed quadratic form.

---

## 2. PROVED — one diagonal logarithmic kernel is a conditional entropy plus Jensen-Shannon information

Put

\[
K_{\rm diag}(a,b):=K_\infty((a,b),(a,b)).
\]

The peer polarization gives

\[
K_{\rm diag}(a,b)=\frac14\Big[
(a-b)^2\log|a-b|+(a+b)^2\log|a+b|
-2a^2\log|a|-2b^2\log|b|
\Big].
\tag{2.1}
\]

Let

\[
M=a^2+b^2,\qquad p=\frac{a^2}{M},\qquad
q=\frac{(a+b)^2}{2M}
\tag{2.2}
\]

when \(M>0\), and use continuous zero values when \(M=0\). Let

\[
h(u)=-u\log u-(1-u)\log(1-u)
\tag{2.3}
\]

be binary entropy in nats.

### Theorem 2.1 — `P03-B16-DIAGONAL-ENTROPY-POLARIZATION` — PROVED

For every real \(a,b\),

\[
\boxed{
K_{\rm diag}(a,b)
=\frac14\left\{M h(p)+M[\log2-h(q)]\right\}.
}
\tag{2.4}
\]

Moreover

\[
\boxed{
0\le M[\log2-h(q)]\le Mh(p),
}
\tag{2.5}
\]

and consequently

\[
\boxed{
0\le K_{\rm diag}(a,b)\le\frac12Mh(p).
}
\tag{2.6}
\]

### Proof

Let \(X=(a+b)^2\), \(Y=(a-b)^2\). Then \(X+Y=2M\). Since
\(x^2\log|x|=\frac12x^2\log x^2\), direct expansion of (2.1) gives (2.4).

For (2.5), it is enough to prove the elementary binary entropic uncertainty inequality

\[
h(p)+h(q)\ge\log2.
\tag{2.7}
\]

Set

\[
x=|2p-1|,\qquad y=|2q-1|.
\]

Because \(p=a^2/M\) and \(q=(a+b)^2/(2M)\),

\[
x^2+y^2=1.
\tag{2.8}
\]

For \(0\le z\le1\), define

\[
g(z)=h\!\left(\frac{1+z}{2}\right)-(1-z^2)\log2.
\]

Then \(g(0)=g(1)=0\),

\[
g'(z)=-\operatorname{artanh}z+2z\log2,
\qquad
g''(z)=2\log2-\frac1{1-z^2}.
\]

The second derivative is strictly decreasing, positive initially and negative near one. Hence \(g'\) rises from zero and then falls through zero exactly once; therefore \(g\ge0\) on \([0,1]\). Applying this to \(x\) and \(y\) and using (2.8) yields

\[
h(p)+h(q)
\ge(1-x^2)\log2+(1-y^2)\log2=\log2.
\]

This proves (2.5) and (2.6). \(\square\)

### Meaning

The logarithm that defeated a pure quartic estimate is not an uncontrolled scalar loss. It is exactly the sum of:

1. a side-label conditional entropy \(Mh(p)\); and
2. a Jensen-Shannon / polarization information \(M[\log2-h(q)]\),

with the second term bounded by the first **pointwise**.

---

## 3. PROVED — affine-coset diagonal = conditional side entropy + spectral JS divergence

Let \(C=q_0+P_0\) be one affine coset of \(P_0\) inside \(P_1\), and put

\[
w=h(-1)^{q_0}.
\]

Modulo the constant affine bit, index the \(N\) ordinary Walsh frequencies by \(\xi\). Define

\[
a_\xi=\widehat{w\,1_{\{f=+1\}}}(\xi),
\qquad
b_\xi=\widehat{w\,1_{\{f=-1\}}}(\xi).
\tag{3.1}
\]

Then

\[
u_\xi=(a_\xi+b_\xi)^2=\widehat w(\xi)^2,
\qquad
v_\xi=(a_\xi-b_\xi)^2=\widehat{fw}(\xi)^2,
\]
\[
m_\xi=a_\xi^2+b_\xi^2=\frac{u_\xi+v_\xi}{2}.
\tag{3.2}
\]

All three \(u,v,m\) are probability distributions. Define

\[
C_C:=\sum_\xi m_\xi\,h\!\left(\frac{a_\xi^2}{m_\xi}\right),
\tag{3.3}
\]

and the Jensen-Shannon divergence

\[
JS_C:=H_{\rm nat}(m)-\frac12H_{\rm nat}(u)-\frac12H_{\rm nat}(v).
\tag{3.4}
\]

### Theorem 3.1 — `P03-B16-COSET-DIAGONAL-ENTROPY` — PROVED

For each coset,

\[
\boxed{
\frac12\sum_{r\in C}K_{\rm diag}(A_r^+,A_r^-)
=\frac14(C_C+JS_C).
}
\tag{3.5}
\]

Furthermore

\[
\boxed{
0\le JS_C\le C_C\le h(p_-).
}
\tag{3.6}
\]

### Proof

Each linear frequency occurs twice in the affine coset, differing only by the constant bit; \(K_{\rm diag}\) is invariant under simultaneous sign change. Summing (2.4) over the unique frequencies gives (3.5): the first term is exactly (3.3), while the second is the coordinate formula for the Jensen-Shannon divergence of \(u\) and \(v\).

The inequality \(JS_C\le C_C\) follows by summing (2.5). For the final inequality, the nonnegative masses \(a_\xi^2,b_\xi^2\) form a joint distribution of `frequency` and `side`, with side marginal

\[
\sum_\xi b_\xi^2=p_-,
\qquad
\sum_\xi a_\xi^2=p_+,
\]

by Parseval. Thus \(C_C=H(\text{side}\mid\text{frequency})\le H(\text{side})=h(p_-)\). \(\square\)

This theorem keeps the full affine-coset multiplicity. No single representative is substituted for a dual-code orbit.

---

## 4. PROVED — the complete terminal-weighted diagonal is paid dimension-independently by J

The quotient \(P_1/P_0\) has

\[
M_q=\frac{L}{2N}=\frac1\rho
\tag{4.1}
\]

cosets. Let \(C_0\) denote the base coset and let an overline denote the uniform average over nonzero quotient cosets.

From (1.3), the squared terminal weights have the exact normalized mixture

\[
\frac{\alpha_r^2}{\sum_t\alpha_t^2}
=
\gamma\,\operatorname{Unif}(P_0)
+\rho\,\operatorname{Unif}(P_1\setminus P_0),
\tag{4.2}
\]

because

\[
\sum_r\alpha_r^2=\frac{\gamma}{2N}.
\tag{4.3}
\]

Set \(T_C=C_C+JS_C\). Define the diagonal part of the full retained square by

\[
D_h:=16N^2\sum_{r\in P_1}\alpha_r^2K_{\rm diag}(A_r^+,A_r^-).
\tag{4.4}
\]

### Theorem 4.1 — `P03-B16-TERMINAL-DIAGONAL-PAYMENT` — PROVED

Exactly,

\[
\boxed{
D_h=2\gamma\left[\gamma T_{C_0}+\rho\,\overline{T}_{C\ne C_0}\right].
}
\tag{4.5}
\]

Hence, for every Boolean twist \(h\),

\[
\boxed{
D_h\le4\gamma h(p_-).
}
\tag{4.6}
\]

In the minimizing-character gauge,

\[
\boxed{
D_h\le4\gamma(\log2)J(f).
}
\tag{4.7}
\]

### Proof

Equation (4.5) is obtained by inserting the two values in (1.3) and the coset sum (3.5). By (3.6), every \(T_C\le2h(p_-)\), proving (4.6).

For (4.7), use the standard edge-isoperimetric inequality on the Boolean cube. For the minority sign set of density \(p_-\le1/2\),

\[
I(f)\ge2p_-\log_2(1/p_-).
\tag{4.8}
\]

Also, for \(0\le p\le1/2\),

\[
h(p)\le2p\log(1/p).
\tag{4.9}
\]

(The difference \(p\log(1/p)-(1-p)\log(1/(1-p))\) is nonnegative on this interval; its derivative has one sign change.) Combining (4.8)--(4.9) gives

\[
h(p_-)\le(\log2)I(f)=(\log2)J(f),
\]

where the final equality is the fixed minimizing-character gauge (0.2). \(\square\)

### Live-window consequence

Account04/B16 gives

\[
\mathcal E_{\rm cur}(s)\le\frac19\mathbb E_S R_{g_S}(s)^2,
\qquad
\mathcal E_{\rm cen}(s)\le\frac{11}{1152}\mathbb E_S R_{g_S}(s)^2.
\tag{4.10}
\]

The account01 square-first theorem permits enlargement of every live Borel window after squaring. Therefore the **diagonal logarithmic portion of the resulting full-line quadratic upper bound** costs at most

\[
\boxed{
\frac{4\gamma\log2}{9}J(f)
=0.308065413582\ldots\,\gamma J(f)
}
\tag{4.11}
\]

for the full current, and

\[
\boxed{
\frac{11\gamma\log2}{288}J(f)
=0.026474371480\ldots\,\gamma J(f)
}
\tag{4.12}
\]

for the central current.

These are payments only for the diagonal part of the signed full-line form. The off-diagonal terms are not declared nonnegative and are not absolute-valued.

---

## 5. PROVED — exact terminal quotient ANOVA exposes a negative variance credit

The preceding theorem pays the logarithmic diagonal. The remaining off-diagonal problem should not be attacked by dropping the terminal signs. There is an exact Hilbert-space identity that makes the terminal cancellation visible.

Let

\[
\varphi_r(s)=\sin(sA_r^+)\sin(sA_r^-)
\]

as an element of

\[
\mathcal H=L^2((0,\infty),s^{-3}ds).
\]

For each quotient coset \(C\in P_1/P_0\), define

\[
m_C=\frac1{2N}\sum_{r\in C}\varphi_r,
\qquad
\bar m=\mathbb E_C m_C.
\tag{5.1}
\]

Then (1.2) gives the exact identity

\[
\sum_r\alpha_r\varphi_r=m_{C_0}-\bar m.
\tag{5.2}
\]

### Theorem 5.1 — `P03-B16-TERMINAL-QUOTIENT-ANOVA` — PROVED

\[
\boxed{
\left\|m_{C_0}-\bar m\right\|_{\mathcal H}^2
=
\mathbb E_C\left\|m_{C_0}-m_C\right\|_{\mathcal H}^2
-
\mathbb E_C\left\|m_C-\bar m\right\|_{\mathcal H}^2.
}
\tag{5.3}
\]

Equivalently, if

\[
R_C^{(0)}(s):=-4N m_C(s)
\tag{5.4}
\]

is the base-code \(C_0\) phase-switch response after twisting by a representative of the coset \(C\), then

\[
\boxed{
\int_0^\infty\frac{R_h(s)^2}{s^3}ds
=
\mathbb E_C\int_0^\infty\frac{(R_{C_0}^{(0)}-R_C^{(0)})^2}{s^3}ds
-
\mathbb E_C\int_0^\infty\frac{(R_C^{(0)}-\overline R^{(0)})^2}{s^3}ds.
}
\tag{5.5}
\]

### Proof

Equation (5.3) is the Hilbert-space variance decomposition

\[
\mathbb E\|a-X\|^2=\|a-\mathbb EX\|^2+\mathbb E\|X-\mathbb EX\|^2
\]

with \(a=m_{C_0}\). Equation (5.5) follows from (1.5), (5.2) and multiplication by \(16N^2\). \(\square\)

### Compiler meaning

If \(\theta_C=(-1)^{q_C}\) is a quotient-coset phase representative, then

\[
R_{C_0}^{(0)}-R_C^{(0)}
=
\Delta_{\theta_C}\Delta_f\Phi_{C_0,s}(h).
\tag{5.6}
\]

So the full retained terminal square is an average of authentic two-phase mixed differences **minus a nonnegative quotient-variance refund**. This negative term is part of the actual terminal multiplicity; dropping it would be a real loss, not a harmless simplification.

No negative entropy credit or R16 moment credit has been used to obtain (5.5).

---

## 6. Attempted refutation / dead routes

### REFUTED by the consumed peer result

A scale-free bound

\[
K_{\rm diag}(a,b)\le C\min(a^2,b^2)
\]

is false because \(K_{\rm diag}(1,\varepsilon)\sim\frac12\varepsilon^2\log(1/\varepsilon)\). This run does not retry that route; Theorem 2.1 instead identifies the logarithm as entropy/information.

### REFUTED as an admissible simplification

Replacing the retained terminal square by the first positive term in (5.5) and forgetting the second term throws away the exact quotient-variance credit. Such a one-sided enlargement may still be useful if separately paid, but it is **not** an identity and is not used here to claim closure.

### OPEN, not assumed

The quotient phase \(\theta_C\) in (5.6) is not automatically a single original-coordinate ordered physical flag. Therefore it would be invalid to feed every term of (5.6) directly into the account03/B18 signed curvature bank merely because that bank is dimension-free. The authentic contraction from the quotient mixed difference to the ordered physical \(\kappa_i(W)\) source is still missing.

---

## 7. Exact remaining implication and next recipient

The account03/B18 signed physical sink proves, in the same minimizing gauge,

\[
\sum_i\mathbb E_W\kappa_i(W)\le2J(f),
\qquad
\sum_i\mathbb E_W\kappa_i(W)^2\le4J(f),
\tag{7.1}
\]

while preserving the opposite-orientation component.

After Theorems 4.1 and 5.1, the remaining interface-C implication can be stated narrowly:

> **OPEN contraction.** For the actual quotient phases \(\theta_C\) generated by the retained \(C_0-D_d\) compiler and the genuine syndrome twists \(h=g_S\), prove a PSD/no-reuse contraction of the signed average of the mixed differences
> \[
> \Delta_{\theta_C}\Delta_f\Phi_{C_0,s}(g_S)
> \]
> into the ordered physical signed-curvature flags \(\kappa_i(W)\), while retaining the negative variance term in (5.5), or identify the exact residual that must be paid by the reserved R16/negative-entropy/terminal ledgers.

The diagonal logarithmic component no longer belongs to that gap: it is already paid by (4.11)--(4.12).

**Next recipient:** `account03/B18`, with `account02/B16` as the source-side parent/mask partner. The useful handoff is (5.5)--(5.6) together with the paid diagonal (4.7), not an unsigned support bank.

Full FEI remains **OPEN / NOT PROVED**.

---

## 8. Falsification/self-check calculations

The companion deterministic checker is new for this run and does not rerun the settled read-once certificate. It reports:

- 20,001 scalar amplitude ratios for (2.4)--(2.6); maximum observed \(K_{\rm diag}/[Mh(p)] = 1/2\), at \(|a|=|b|\);
- 30 small-cube coset tests of (3.5), with maximum identity error \(8.33\times10^{-17}\) and direct JS mismatch \(3.89\times10^{-16}\);
- all 65,804 nonconstant Boolean functions in dimensions \(1\) through \(4\) for the edge-entropy consequence \(h(p_-)\le(\log2)I\), maximum ratio exactly 1 within floating arithmetic;
- seven exact rational Hilbert-ANOVA instances;
- nineteen exact rational terminal \(\alpha^2\)-mixture count checks.

The analytic proofs above, not these finite checks, support the universal statements.
