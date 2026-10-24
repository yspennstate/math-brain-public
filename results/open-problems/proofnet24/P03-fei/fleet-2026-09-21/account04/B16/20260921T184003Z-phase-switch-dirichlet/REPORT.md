# B16 FEI signed transport — global phase-switch Dirichlet reduction and quartic dual-code cancellation

**Date:** 21 September 2026  
**Scope:** `account04 / B16`, FEI signed transport proof  
**Execution:** **WITHOUT_VERIFIED_BRAIN**  
**Status of unrestricted FEI:** **OPEN / NOT PROVED**  
**Claim level:** exact signed quotient identities, sharp current-to-phase-switch constants, and a new retained dual-code phase-switch estimate. No novelty or publication-priority claim.

## 0. Fresh state and route change

This run continued the fresh signed-transport chain after:

1. account04's correlated-noise double-resolvent theorem, which writes the already-signed parity-current energy as a positive clone-pair curvature square and gives the central multiplier
   \[
   \varepsilon_{q,k}
   =2\frac{2^{-q}}q\left(\frac{2^{-k}}k-\frac{2^{-q}}q\right);
   \]
2. account02's fresh actual-parent-mask theorem, which disintegrates that positive central current by doubled coarse parents and proves dimension-free projective parent-mask incidence, while leaving the actual source-curvature-to-physical-Radon pushforward open;
3. account03/B18's fresh physical flag theorem, which proves that once a positive compiler term is legitimately pushed to squared physical dependent-face discrepancies, the complete ordered flag square bank is paid by \(J(f)\);
4. the older exact Borel/MacWilliams representation of the retained potential and the exact active-syndrome dual phase basis.

The remaining bottleneck is therefore not another unsigned frame estimate.  It is to keep the exact signed aggregate long enough to expose an authentic physical object.

This report makes two changes.

* First, it diagonalizes **only the final odd/frustrated projection** of the signed aggregate.  The whole odd syndrome \(L^2\) mass becomes one global phase-switch Dirichlet energy of the retained Borel potential.
* Second, it studies that phase switch directly through the exact dual-code cosine representation.  The naive quadratic term cancels **identically** for every residual code \(E\le C_0\), because \(C_0=RM(1,n)^\perp\) has no weight-two word.  The first possible phase-switch response is quartic.  This is the same four-point scale on which q-flip frustration lives.

No R32 coefficient is absolute-valued before the syndrome aggregation.  The retained terminal subtraction is kept inside one signed potential.  R16 moment refunds, negative \(2\bmod4\) credits, dual-code multiplicity and the separate terminal-band ledger are not re-spent.

---

## 1. Signed active-syndrome field

At one fixed Borel time \(s\), let the retained signed relation coefficient be
\[
c_A(s),\qquad A\in C_0,
\]
with \(c_A=0\) on the terminal code \(D_d\).  Fix a valid q-flip basis and let \(M\) be the active basis coordinates for the actual Boolean phase \(f\).  For a relation \(A\), write
\[
R_A\subseteq M
\]
for its active syndrome.  Then
\[
f_A=(-1)^{|R_A|}.
\]

Aggregate **before squaring**
\[
\boxed{
b_R(s):=\sum_{A:R_A=R}c_A(s).
}
\tag{1.1}
\]
Define the Walsh transform on the active syndrome cube
\[
\boxed{
\Phi_s(S)
=\sum_{R\subseteq M} b_R(s)(-1)^{|S\cap R|}.
}
\tag{1.2}
\]
By the inherited exact compiler dictionary,
\[
\boxed{
\Phi_s(S)
=
\Phi_{C_0,s}(g_S)-\Phi_{D_d,s}(g_S)
=: \Psi_s(g_S),
}
\tag{1.3}
\]
where \(g_S\) is the dual phase represented by syndrome character \(S\).  The actual Boolean phase is the all-active dual product:
\[
[f]=\prod_{v\in M}[g_v].
\tag{1.4}
\]
Thus
\[
g_{S\triangle M}=f\,g_S
\quad\text{modulo an affine character.}
\tag{1.5}
\]
The potentials in (1.3) are affine-gauge invariant.

---

## 2. `P03-B16-ODD-SYNDROME-PHASE-SWITCH` — PROVED

Let
\[
\mathcal O_s:=\sum_{\substack{R\subseteq M\\|R|\ {\rm odd}}}b_R(s)^2.
\tag{2.1}
\]

### Theorem 2.1

For every signed coefficient field,
\[
\boxed{
\mathcal O_s
=
\frac14\,\mathbb E_{S\subseteq M}
\left[
\Phi_s(S)-\Phi_s(S\triangle M)
\right]^2.
}
\tag{2.2}
\]
Equivalently, for the authentic retained compiler,
\[
\boxed{
\mathcal O_s
=
\frac14\,\mathbb E_{S\subseteq M}
\left[
\Psi_s(g_S)-\Psi_s(fg_S)
\right]^2.
}
\tag{2.3}
\]

### Proof

Translation \(S\mapsto S\triangle M\) has Walsh eigenvalue
\[
(-1)^{|R|}.
\]
Therefore
\[
\Phi_s(S)-\Phi_s(S\triangle M)
=
2\sum_{|R|\ {\rm odd}}b_R(s)(-1)^{|S\cap R|}.
\]
Normalized Walsh Parseval gives (2.2).  Equation (2.3) follows from (1.3)--(1.5). \(\square\)

### Same-syndrome correlation form

Let \(K\) be the kernel of active-syndrome restriction:
\[
K=\{\Delta\in C_0:R_\Delta=\varnothing\}.
\]
Define
\[
C_\Delta=\sum_A c_Ac_{A\triangle\Delta},
\qquad
T_\Delta=\sum_A f_Ac_Ac_{A\triangle\Delta}.
\]
Since every \(\Delta\in K\) has \(f_\Delta=+1\),
\[
\boxed{
\mathcal O_s
=
\frac12\sum_{\Delta\in K}
\left(C_\Delta-T_\Delta\right).
}
\tag{2.4}
\]
This is the exact kernel-correlation version of (2.2).  No positive part is taken in either correlation.

---

## 3. Twisted live R32 square identity

Define the character-twisted retained frustrated response
\[
\boxed{
\mathfrak G_{f,h}(s)
:=
\sum_{\substack{A\in C_0\setminus D_d\\f_A=-1}}
c_A(s)(-1)^{h\cdot A}.
}
\tag{3.1}
\]
At \(h=0\), this is exactly the live signed R32/Borel response at time \(s\).

Because
\[
1-f_A=
\begin{cases}
0,&f_A=+1,\\
2,&f_A=-1,
\end{cases}
\]
one has the exact phase derivative
\[
\boxed{
\Psi_s(h)-\Psi_s(fh)
=
2\mathfrak G_{f,h}(s).
}
\tag{3.2}
\]
Consequently Theorem 2.1 becomes

### Corollary 3.1 — `P03-B16-TWISTED-R32-SQUARE`

\[
\boxed{
\mathcal O_s
=
\mathbb E_{S\subseteq M}
\mathfrak G_{f,g_S}(s)^2.
}
\tag{3.3}
\]

The post-cancellation odd syndrome mass is therefore not a relation count.  It is the orbit-average square of the **actual signed frustrated R32 response**, with all \(0\bmod4/2\bmod4\) cancellation and the terminal exclusion already present.

---

## 4. Sharp current domination by one global phase switch

For a paired fine syndrome \(R\), let
\[
q=|R|,
\qquad
k=\#\{\text{clone pairs hit oddly}\}.
\]
On the odd sector, \(q,k\) are odd and \(1\le k\le q\).

The full parity-current multiplier is
\[
e_{q,k}
=
2\left(\frac1{qk}-\frac1{q^2}\right).
\tag{4.1}
\]
The central \(x,y\le1/2\) multiplier is
\[
\varepsilon_{q,k}
=
2\frac{2^{-q}}q
\left(
\frac{2^{-k}}k-\frac{2^{-q}}q
\right).
\tag{4.2}
\]

### Theorem 4.1 — sharp scalar caps

For every allowed odd pair \((q,k)\),
\[
\boxed{
0\le e_{q,k}\le\frac49,
}
\tag{4.3}
\]
and
\[
\boxed{
0\le \varepsilon_{q,k}\le\frac{11}{288}.
}
\tag{4.4}
\]
Both upper bounds are attained at \((q,k)=(3,1)\).  The singleton \((1,1)\) mode is zero.

For fixed \(q\), both multipliers decrease with \(k\), so \(k=1\) is worst.  For the full multiplier,
\[
2\frac{q-1}{q^2}
\]
decreases for odd \(q\ge3\).  For the central multiplier, \(q=3\) gives \(11/288\), while for every odd \(q\ge5\),
\[
\varepsilon_{q,1}
<
\frac{2^{-q}}q
\le\frac1{160}
<
\frac{11}{288}.
\]

Therefore, writing \(\mathcal E_{\rm cur}(s)\) and \(\mathcal E_{\rm cen}(s)\) for the authentic full and central double-resolvent energies at that Borel time,

### Corollary 4.2 — `P03-B16-GLOBAL-PHASE-DIRICHLET-DOMINATION`

\[
\boxed{
\mathcal E_{\rm cur}(s)
\le
\frac49\mathcal O_s
=
\frac19
\mathbb E_S
\left[\Psi_s(g_S)-\Psi_s(fg_S)\right]^2,
}
\tag{4.5}
\]
and
\[
\boxed{
\mathcal E_{\rm cen}(s)
\le
\frac{11}{288}\mathcal O_s
=
\frac{11}{1152}
\mathbb E_S
\left[\Psi_s(g_S)-\Psi_s(fg_S)\right]^2.
}
\tag{4.6}
\]
The constants in the purely syndrome-theoretic comparison are sharp.

This collapses every clone-pair and every syndrome degree in the **upper-bound stage** to one global involution: multiply the dual phase by the actual Boolean phase \(f\).

---

## 5. Exact dual-code phase-switch factorization

The preceding reduction is useful only if the global phase switch has genuine physical structure.  It does.

Let \(E\le C_0=RM(1,n)^\perp\), let
\[
P=E^\perp,
\qquad
N=2^n,
\]
and use the inherited exact dual-code Borel potential
\[
\boxed{
\Phi_{E,s}(h)
=
\frac{2N}{|P|}
\sum_{r\in P}
\cos\!\left(
s\,m(h(-1)^r)
\right),
}
\tag{5.1}
\]
where
\[
m(u)=\frac1N\sum_x u(x).
\]

Fix a Boolean phase \(f\).  Put
\[
\Omega_+=\{x:f(x)=+1\},
\qquad
\Omega_-=\{x:f(x)=-1\},
\]
and
\[
p_\pm=\frac{|\Omega_\pm|}{N}.
\]
For \(r\in P\), define
\[
A_r^\pm
:=
\frac1N\sum_{x\in\Omega_\pm} h(x)(-1)^{r_x}.
\tag{5.2}
\]
Then
\[
m(h(-1)^r)=A_r^++A_r^-,
\qquad
m(fh(-1)^r)=A_r^+-A_r^-.
\]

### Theorem 5.1 — `P03-B16-DUAL-CODE-PHASE-SWITCH`

\[
\boxed{
\Phi_{E,s}(h)-\Phi_{E,s}(fh)
=
-\frac{4N}{|P|}
\sum_{r\in P}
\sin(sA_r^+)\sin(sA_r^-).
}
\tag{5.3}
\]

This is just
\[
\cos(s(a+b))-\cos(s(a-b))
=-2\sin(sa)\sin(sb)
\]
inside the exact MacWilliams sum.

---

## 6. `P03-B16-QUADRATIC-TERM-CANCELLATION` — PROVED

The key new fact is that the apparent quadratic phase-switch response vanishes identically.

### Theorem 6.1

For every \(E\le C_0\),
\[
\boxed{
\sum_{r\in P}A_r^+A_r^-=0.
}
\tag{6.1}
\]
Moreover,
\[
\boxed{
\frac1{|P|}\sum_{r\in P}(A_r^\pm)^2
=
\frac{p_\pm}{N}.
}
\tag{6.2}
\]

### Proof

For \(x,y\in V\),
\[
\frac1{|P|}
\sum_{r\in P}
(-1)^{r_x+r_y}
=
1_{\{e_x+e_y\in E\}}.
\tag{6.3}
\]
Every nonzero word of \(C_0=RM(1,n)^\perp\) has weight at least four.  Since \(E\le C_0\), for distinct \(x\ne y\),
\[
e_x+e_y\notin E.
\]
Expanding the two second moments therefore leaves only \(x=y\), which gives (6.2).

For (6.1), one index lies in \(\Omega_+\) and the other in the disjoint set \(\Omega_-\), so \(x\ne y\) in every summand.  Equation (6.3) kills every term. \(\square\)

### Meaning

The phase-switch response of every admissible dual-code Borel potential starts only at **four-point order**.  The degree-two term is forbidden by the distance-four relation code.  This is exactly the scale at which q-flip/plaquette frustration first exists.

It is not an analogy: it is the same dual-code distance statement.

---

## 7. A dimension-free quartic phase-switch bound

Use the global inequalities
\[
|\sin z|\le|z|,
\qquad
|\sin z-z|\le\frac{|z|^3}{6}.
\]
Because (6.1) removes the \(s^2A_r^+A_r^-\) term,
\[
\begin{aligned}
&\left|
\sin(sA_r^+)\sin(sA_r^-)
-s^2A_r^+A_r^-
\right|
\\
&\qquad\le
\frac{s^4}{6}
|A_r^+A_r^-|
\left((A_r^+)^2+(A_r^-)^2\right).
\end{aligned}
\tag{7.1}
\]
Also
\[
|A_r^\pm|\le p_\pm.
\]
By (6.2) and Cauchy--Schwarz,
\[
\frac1{|P|}
\sum_r|A_r^+A_r^-|
\le
\frac{\sqrt{p_+p_-}}{N}.
\tag{7.2}
\]

### Theorem 7.1 — single-code quartic estimate

For every \(E\le C_0\),
\[
\boxed{
\left|
\Phi_{E,s}(h)-\Phi_{E,s}(fh)
\right|
\le
\frac23\,s^4
(p_+^2+p_-^2)\sqrt{p_+p_-}.
}
\tag{7.3}
\]
The coarser all-scale quadratic estimate is
\[
\boxed{
\left|
\Phi_{E,s}(h)-\Phi_{E,s}(fh)
\right|
\le
4s^2\sqrt{p_+p_-}.
}
\tag{7.4}
\]

These bounds are independent of \(n\), \(|E|\), and dual-code multiplicity.

---

## 8. The terminal subtraction can stay inside the same estimate

Now take
\[
E_0=C_0,\qquad E_1=D_d,
\]
and
\[
P_0=RM(1,n),\qquad P_1=D_d^\perp.
\]
Write
\[
L=|P_1|,
\qquad
\rho_d:=\frac{2N}{L}\in(0,1].
\tag{8.1}
\]
Since \(P_0\subseteq P_1\), the retained potential is
\[
\Psi_s=\Phi_{E_0,s}-\Phi_{E_1,s}.
\]

Instead of bounding the two terms separately, keep their signed dual weights together:
\[
\alpha_r
=
\frac1{2N}1_{\{r\in P_0\}}
-\frac1L1_{\{r\in P_1\}}.
\tag{8.2}
\]
Both normalized quadratic averages vanish by Theorem 6.1, hence the **signed retained quadratic term is also exactly zero before an absolute value is taken**.

A direct weighted Cauchy calculation gives
\[
\sum_r|\alpha_r|(A_r^\pm)^2
=
\frac{2p_\pm}{N}(1-\rho_d).
\tag{8.3}
\]

### Theorem 8.1 — `P03-B16-RETAINED-QUARTIC-PHASE-SWITCH`

\[
\boxed{
\left|
\Psi_s(h)-\Psi_s(fh)
\right|
\le
\frac43\,s^4(1-\rho_d)
(p_+^2+p_-^2)\sqrt{p_+p_-}.
}
\tag{8.4}
\]
Also
\[
\boxed{
\left|
\Psi_s(h)-\Psi_s(fh)
\right|
\le
8s^2(1-\rho_d)\sqrt{p_+p_-}.
}
\tag{8.5}
\]

The factor \(1-\rho_d\) is the exact \(L^1\) size of the **signed terminal subtraction** in this dual average.  If \(D_d=C_0\), then \(\rho_d=1\) and the retained potential is zero, as (8.4)--(8.5) correctly record.

No terminal contribution is paid twice in deriving these estimates.

---

## 9. Folded physical influence enters by one legal affine gauge

Relation signs and every potential above are invariant under multiplying \(f\) by an affine character.  Choose the standard minimizing-character gauge \(F=f\chi_a\) for which
\[
I(F)=J(f)
=
\sum_i\min\{I_i(f),1-I_i(f)\}.
\tag{9.1}
\]
Let \(p_\pm\) now denote the two sign densities of \(F\).

Cube Poincare gives
\[
1-(\mathbb EF)^2
\le I(F)=J(f).
\]
Since
\[
p_+p_-=\frac{1-(\mathbb EF)^2}{4},
\]
\[
\boxed{
p_+p_-\le\frac{J(f)}4.
}
\tag{9.2}
\]
Also \(p_+^2+p_-^2\le1\).

Thus Theorem 8.1 yields the pointwise-in-\(s\) retained estimate
\[
\boxed{
\left|
\Psi_s(h)-\Psi_s(fh)
\right|
\le
(1-\rho_d)\sqrt{J(f)}
\min\left\{
4s^2,\frac23s^4
\right\}.
}
\tag{9.3}
\]

Combining with the global phase Dirichlet domination gives:

### Corollary 9.1 — a genuine fixed-scale \(J\)-payment

\[
\boxed{
\mathcal E_{\rm cen}(s)
\le
\frac{11}{1152}(1-\rho_d)^2J(f)
\min\left\{
16s^4,\frac49s^8
\right\}.
}
\tag{9.4}
\]
In particular, on the quartic branch,
\[
\boxed{
\mathcal E_{\rm cen}(s)
\le
\frac{11}{2592}
s^8(1-\rho_d)^2J(f).
}
\tag{9.5}
\]
Likewise
\[
\boxed{
\mathcal E_{\rm cur}(s)
\le
\frac19(1-\rho_d)^2J(f)
\min\left\{
16s^4,\frac49s^8
\right\}.
}
\tag{9.6}
\]

This is a real dimension-free physical-influence payment for the fully signed current at every **fixed Borel time**.  It does not close the full Borel corridor because the displayed envelope grows with \(s\).

---

## 10. What remains open

This run does **not** prove full FEI.

The new reduction isolates a narrower problem than the previous generic q-flip frame:

> control the Borel-time integral of the retained global phase-switch Dirichlet energy
> \[
> \mathbb E_{S\subseteq M}
> [\Psi_s(g_S)-\Psi_s(fg_S)]^2
> \]
> using the already-paid high-resolvent/R16 and terminal ledgers at large \(s\), while using the quartic distance-four cancellation at small \(s\).

The small-\(s\) obstruction is no longer combinatorial multiplicity: the quadratic response vanishes identically and the first possible response is four-point/q-flip order.

The large-\(s\) bound (8.5) is still too crude to integrate through the entire live corridor without potentially losing scale.  The next calculation should therefore keep the exact sine product in (5.3), insert the physical ordered-flag/Radon decomposition **before** absolute values, and ask whether the random-order Hardy kernel suppresses the large-\(s\) phase-switch energy.  If that fails, preserve the exact counterexample rather than reverting to unit-weight arbitrary-q-flip incidence, one-resolvent transport, generic endpoint \(L^2\), or an unsigned relation sum.

---

## 11. Decisive calculations

`check_phase_switch_dirichlet.py` checks the algebra independently of FEI certificate machinery.

It verifies:

- 350 exact rational odd-syndrome/phase-switch Parseval identities for syndrome dimensions \(0\) through \(6\);
- 405 exact rational same-syndrome correlation identities;
- all 1,275 allowed odd \((q,k)\) pairs through \(q=99\), including the sharp maxima \(4/9\) and \(11/288\);
- exact dual-code quadratic cancellation on \(C_0\) subcodes in dimensions \(n=2,3\);
- numerical reconstruction of the cosine/sine phase-switch factorization;
- the single-code quartic and quadratic estimates;
- the retained signed-terminal quartic and quadratic estimates on representative terminal subcodes.

The finite calculations are falsification checks.  The universal statements above are proved algebraically.

**Full unrestricted FEI remains OPEN / NOT PROVED.**
