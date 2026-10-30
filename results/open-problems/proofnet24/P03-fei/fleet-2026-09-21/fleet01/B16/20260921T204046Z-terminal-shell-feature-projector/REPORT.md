# B16 FEI signed transport — terminal-shell feature projector and exact Brownian/Laplace source coefficients

**Date:** 21 September 2026  
**Scope:** `fleet01 / B16`, signed transport / noise interpolation, APPROACH 10/13  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Status of unrestricted FEI:** **OPEN / NOT PROVED**  
**Claim level:** exact source-side projection and feature-factorization lemmas for the two positive banks isolated by the newest compiler handoff, plus a rigorous obstruction to destroying the retained shell/syndrome cancellation. No publication-priority claim.

## 0. Fresh peer input and the exact implication attacked

This run follows the joint four-account FEI order and substantively consumes the fresh fleet02/B18 report

`proofnet24/P03-fei/fleet-2026-09-21/fleet02/B18/20260921T200356Z-restriction-kernel-polarization/REPORT.md`.

That report starts from the fleet01 square-first window theorem and proves the exact decomposition

\[
\int_0^\infty \frac{R_h(s)^2}{s^3}\,ds
=N^2\ln 2\,[\mathcal Q_{\mathsf S}(h)+\mathcal Q_{\mathsf P}(h)]
\le N^2\ln2\,\mathcal Q_{\mathsf S}(h)+2N^2\mathcal Q_{\mathsf M}(h),
\]

where the retained terminal coefficients are

\[
\alpha_r=\frac1{|P_0|}{\bf1}_{r\in P_0}-\frac1{|P_1|}{\bf1}_{r\in P_1},
\qquad P_0=RM(1,n),\quad P_1=D_d^\perp,
\]

and

\[
\mathcal Q_{\mathsf S}(h)
=\frac1{\ln2}\int_0^\infty
\frac{\left|\sum_r\alpha_r(e^{-tU_r^2}-e^{-tV_r^2})\right|^2}{t^2}\,dt,
\]
\[
\mathcal Q_{\mathsf M}(h)
=\int_0^1
\left|\sum_r\alpha_r({\bf1}_{u\le V_r^2}-{\bf1}_{u\le U_r^2})\right|^2du,
\]
with `U_r=c_r(h)` and `V_r=c_r(fh)`.  The upper limit in the second display may be written infinity, since the correlations have absolute value at most one.

The fresh report leaves the two exact obligations

\[
N^2\,\mathbb E_S\mathcal Q_{\mathsf M}(g_S)=O(J(f)),
\qquad
N^2\ln2\,\mathbb E_S\mathcal Q_{\mathsf S}(g_S)=O(J(f))
\]
with the terminal signs and negative credits retained.

The present run attacks the **source side** of exactly these two banks.  The main result is that the terminal subtraction is not merely a signed measure: as a convolution operator on the truth-table group it is an **orthogonal Fourier projection onto the retained relation shell** `C_0\D_d`.  For *every scalar feature of the squared dual correlation*, multiplication by the actual Boolean phase then inserts the exact factor `f_A-1`, so only frustrated retained relations survive.  The genuine syndrome average is consequently an exact same-syndrome square with one explicit radial Krawtchouk coefficient per relation size.

This gives a canonical source coefficient for both the Brownian-threshold and Laplace/Shannon banks.  It does not yet prove the physical payment.

The second peer input used below is fleet04/B16's authentic syndrome representation, in particular

\[
\chi_A(q_S)=(-1)^{|S\cap R_A|}
\]
for the dual phase `g_S=(-1)^{q_S}` modulo an affine character.  This is the exact Walsh/syndrome dictionary behind the already-proved same-syndrome aggregation; no synthetic distribution is introduced here.

---

## 1. Truth-table group and terminal signed measure

Let

\[
V=\mathbb F_2^n,\qquad N=|V|=2^n,
\qquad \mathcal G=\mathbb F_2^V.
\]

An element `r in G` is a binary truth-table word.  For `A subseteq V`, write

\[
\chi_A(r)=(-1)^{\langle A,r\rangle}
=(-1)^{\sum_{x\in A}r_x}.
\]

Let

\[
C_0=RM(1,n)^\perp,
\qquad E=D_d\le C_0,
\]

and

\[
P_0=C_0^\perp=RM(1,n),
\qquad P_1=E^\perp.
\]

Define the actual terminal signed measure on `G`

\[
\boxed{
\alpha(r)=\frac{{\bf1}_{P_0}(r)}{|P_0|}
-\frac{{\bf1}_{P_1}(r)}{|P_1|}.
}
\tag{1.1}
\]

For a function `z:G->H` with values in a real Hilbert space, define convolution

\[
(\mathsf P_Ez)(q)=\sum_{r\in\mathcal G}\alpha(r)z(q+r).
\tag{1.2}
\]

For scalar functions use normalized Walsh coefficients

\[
\widehat z(A)=2^{-N}\sum_{q\in\mathcal G}z(q)\chi_A(q).
\tag{1.3}
\]

---

## 2. PROVED — terminal subtraction is an exact retained-shell orthogonal projector

### Theorem 2.1 — `P03-B16-TERMINAL-SHELL-PROJECTOR`

For every `A subseteq V`,

\[
\boxed{
\sum_{r\in\mathcal G}\alpha(r)\chi_A(r)
={\bf1}_{\{A\in C_0\setminus E\}}.
}
\tag{2.1}
\]

Consequently

\[
\boxed{
\widehat{\mathsf P_Ez}(A)
={\bf1}_{\{A\in C_0\setminus E\}}\widehat z(A).
}
\tag{2.2}
\]

Thus `P_E` is a self-adjoint idempotent orthogonal projection on `L^2(G)` (and componentwise on Hilbert-valued `L^2`):

\[
\boxed{\mathsf P_E^2=\mathsf P_E,\qquad
\|\mathsf P_Ez\|_2\le\|z\|_2.}
\tag{2.3}
\]

### Proof

For a finite linear subspace `P <= G`, character orthogonality gives

\[
\frac1{|P|}\sum_{r\in P}\chi_A(r)
={\bf1}_{\{A\in P^\perp\}}.
\]

Apply this first to `P_0`, whose orthogonal is `C_0`, and then to `P_1=E^\perp`, whose orthogonal is `E`.  Because `E<=C_0`, their difference is exactly the indicator of `C_0\E`, proving (2.1).  The convolution rule for Walsh transforms gives (2.2).  Since the multiplier in (2.2) takes only the values zero and one, (2.3) follows.  \(\square\)

### Meaning for the compiler

The retained `C_0-D_d` terminal subtraction has operator norm **one** before any physical push-forward.  Its signs are precisely the inverse Walsh representation of the hard spectral projector onto the retained relation shell.  In particular, there is no intrinsic total-variation or dual-code-multiplicity loss in the terminal subtraction itself; such a loss appears only if this projection is destroyed by taking absolute values or by scalar parent postcompression.

---

## 3. PROVED — every squared-correlation feature factorizes into retained frustration

Let

\[
m(q)=\frac1N\sum_{x\in V}(-1)^{q_x}.
\tag{3.1}
\]

For a scalar function `phi:[0,1]->R`, define the radial truth-table feature

\[
\vartheta_\phi(q)=\phi(m(q)^2).
\tag{3.2}
\]

Because `vartheta_phi` depends only on the Hamming weight of `q`, its Walsh coefficient depends only on `k=|A|`.  Write

\[
\boxed{
\lambda_k^\phi:=\widehat{\vartheta_\phi}(A),\qquad |A|=k.
}
\tag{3.3}
\]

Explicitly, with

\[
K_k(j)=\sum_{\ell=0}^k(-1)^\ell
\binom{k}{\ell}\binom{N-k}{j-\ell},
\]

one has the Krawtchouk formula

\[
\boxed{
\lambda_k^\phi
=2^{-N}\sum_{j=0}^N
K_k(j)\,
\phi\!\left((1-2j/N)^2\right).
}
\tag{3.4}
\]

In particular `lambda_k^phi=0` for odd `k`, because `vartheta_phi(q+1_V)=vartheta_phi(q)`.

Let `f:V->{+-1}` be the actual Boolean phase and let `b_f in G` be its truth-table word,

\[
f(x)=(-1)^{(b_f)_x}.
\]

For `A subseteq V`, put

\[
f_A=\prod_{x\in A}f(x)=\chi_A(b_f).
\tag{3.5}
\]

For a dual phase `h_q=(-1)^q`, define

\[
c_r(h_q)=\frac1N\sum_x h_q(x)(-1)^{r_x}=m(r+q).
\tag{3.6}
\]

Therefore

\[
c_r(fh_q)=m(r+q+b_f).
\tag{3.7}
\]

Define the source feature difference

\[
\mathscr D_\phi(q)
:=\sum_r\alpha(r)
\left[
\phi(c_r(fh_q)^2)-\phi(c_r(h_q)^2)
\right].
\tag{3.8}
\]

### Theorem 3.1 — `P03-B16-FEATURE-SHELL-FRUSTRATION-FACTORIZATION`

For every scalar feature `phi`,

\[
\boxed{
\widehat{\mathscr D_\phi}(A)
={\bf1}_{\{A\in C_0\setminus E\}}
(f_A-1)\lambda_{|A|}^\phi.
}
\tag{3.9}
\]

Equivalently,

\[
\boxed{
\mathscr D_\phi(q)
=-2\!
\sum_{\substack{A\in C_0\setminus E\\f_A=-1}}
\lambda_{|A|}^\phi\,\chi_A(q).
}
\tag{3.10}
\]

### Proof

By (3.6)--(3.7),

\[
\mathscr D_\phi
=\mathsf P_E\bigl[\tau_{b_f}\vartheta_\phi-\vartheta_\phi\bigr],
\]

where `(tau_b v)(q)=v(q+b)`.  Translation by `b_f` multiplies Walsh coefficient `A` by `chi_A(b_f)=f_A`.  Theorem 2.1 then gives

\[
\widehat{\mathscr D_\phi}(A)
={\bf1}_{C_0\setminus E}(A)
(f_A-1)\widehat{\vartheta_\phi}(A),
\]
which is (3.9), and Walsh inversion gives (3.10). \(\square\)

### Two structural consequences

First, the terminal projector and the Boolean phase switch commute in the strongest possible way: **unretained relations disappear exactly, and retained unfrustrated relations disappear exactly**.  No positive part or relation count is used.

Second, `mathscr D_phi` is invariant under affine-character ambiguity.  If `p in P_0` then every `A in C_0` satisfies `chi_A(p)=1`, hence

\[
\boxed{\mathscr D_\phi(q+p)=\mathscr D_\phi(q).}
\tag{3.11}
\]

Thus (3.10) is well-defined on the authentic dual phases `g_S`, which are represented only modulo affine character.

---

## 4. PROVED — authentic syndrome averaging gives an exact same-syndrome radial square

Use the active-syndrome notation from the current compiler.  For each retained relation `A`, let `R_A subseteq M` be its active syndrome.  The genuine dual phase `g_S=(-1)^{q_S}` satisfies

\[
\chi_A(q_S)=(-1)^{|S\cap R_A|}.
\tag{4.1}
\]

### Theorem 4.1 — `P03-B16-RADIAL-SAME-SYNDROME-SQUARE`

For every scalar feature `phi`,

\[
\boxed{
\mathbb E_{S\subseteq M}
|\mathscr D_\phi(q_S)|^2
=
4\sum_{R\subseteq M}
\left(
\sum_{\substack{A\in C_0\setminus E\\
 f_A=-1,\ R_A=R}}
\lambda_{|A|}^\phi
\right)^2.
}
\tag{4.2}
\]

### Proof

Insert (3.10) and (4.1).  As a function of `S`, every relation contributes the Walsh character indexed by its syndrome `R_A`.  Normalized Walsh Parseval on the syndrome cube groups exactly the relations having the same syndrome, giving (4.2). \(\square\)

This is the desired source-side coefficient map.  It says that the two banks isolated by fleet02/B18 are not abstract MMDs once the authentic source is restored: they are **the original signed same-syndrome square again**, but with a new universal radial coefficient depending only on the relation size.

No dual-code multiplicity has been dropped; opposite signs inside one syndrome remain inside the inner sum.

---

## 5. Brownian threshold bank: exact coefficient formula

Take

\[
\phi_u(x)={\bf1}_{\{u\le x\}},\qquad 0\le u\le1,
\]

and write

\[
\lambda_k^{\rm th}(u)=\lambda_k^{\phi_u}.
\]

Since the Brownian bank of the fresh fleet02/B18 report is precisely

\[
\mathcal Q_{\mathsf M}(g_S)
=\int_0^1|\mathscr D_{\phi_u}(q_S)|^2du,
\]

Theorem 4.1 gives the exact identity

\[
\boxed{
\mathbb E_S\mathcal Q_{\mathsf M}(g_S)
=4\sum_R\int_0^1
\left(
\sum_{\substack{A\in C_0\setminus E\\
 f_A=-1,\ R_A=R}}
\lambda_{|A|}^{\rm th}(u)
\right)^2du.
}
\tag{5.1}
\]

This is a strict reduction of the open C-phase obligation: the only source coefficients to be pushed into the physical signed-flag bank are the explicit Krawtchouk threshold coefficients `lambda_k^th(u)`.

### Threshold coefficient energy identities

Put

\[
\mu_k:=\int_0^1\lambda_k^{\rm th}(u)^2du.
\tag{5.2}
\]

Two exact global identities are useful diagnostics.

### Theorem 5.1 — `P03-B16-THRESHOLD-KRAWTCHOUK-ENERGY`

\[
\boxed{
\sum_{k=0}^N\binom Nk\mu_k=\frac1N.
}
\tag{5.3}
\]

Moreover, if `epsilon_1,...,epsilon_{N-1}` are independent uniform signs,

\[
\boxed{
\sum_{k=0}^N k\binom Nk\mu_k
=\frac1N\,
\mathbb E\left|\epsilon_1+\cdots+\epsilon_{N-1}\right|.
}
\tag{5.4}
\]

In particular the right side of (5.4) is

\[
\sqrt{\frac{2}{\pi N}}\,(1+o(1)).
\tag{5.5}
\]

### Proof of (5.3)

For fixed `u`, Parseval on `G` gives

\[
\sum_A\widehat{\phi_u(m^2)}(A)^2
=\mathbb E_q\phi_u(m(q)^2)^2
=\mathbb P_q[m(q)^2\ge u].
\]

Integrating from zero to one and using layer cake gives

\[
\sum_A\int_0^1\widehat{\phi_u(m^2)}(A)^2du
=\mathbb E_q m(q)^2=\frac1N.
\]

Grouping by `|A|` proves (5.3).

### Proof of (5.4)

For any scalar Boolean-valued function `theta` on `G`,

\[
\sum_{A:x\in A}\widehat\theta(A)^2
=\frac14\mathbb E_q[\theta(q)-\theta(q+e_x)]^2.
\]

Apply this to `theta_u(q)=1_{u<=m(q)^2}`, sum over the `N` truth-table coordinates `x`, and integrate in `u`.  Layer cake turns the squared indicator difference into

\[
|m(q)^2-m(q+e_x)^2|.
\]

Write `epsilon_y=(-1)^{q_y}`.  Flipping coordinate `x` gives

\[
|m(q)^2-m(q+e_x)^2|
=\frac4{N^2}
\left|\sum_{y\ne x}\epsilon_x\epsilon_y\right|.
\]

The sum inside the absolute value has the law of a sum of `N-1` independent signs.  Summing over `x` and multiplying by `1/4` gives (5.4). \(\square\)

The identities (5.3)--(5.4) are **not** the desired FEI payment; they are the exact size/degree budget of the universal radial Brownian feature before the retained shell and same-syndrome cancellation are used.

---

## 6. Laplace/Shannon bank: exact coefficient formula

Take

\[
\phi_t(x)=e^{-tx},\qquad t>0,
\]

and put

\[
\lambda_k^{\rm Lap}(t)=\lambda_k^{\phi_t}.
\]

The sign in fleet02/B18's definition of `Q_S` is the opposite of (3.8), which disappears after squaring.  Hence

\[
\boxed{
\mathbb E_S\mathcal Q_{\mathsf S}(g_S)
=\frac4{\ln2}
\sum_R\int_0^\infty
\frac1{t^2}
\left(
\sum_{\substack{A\in C_0\setminus E\\
 f_A=-1,\ R_A=R}}
\lambda_{|A|}^{\rm Lap}(t)
\right)^2dt.
}
\tag{6.1}
\]

Thus the unavoidable logarithm has also been localized to a single explicit radial Krawtchouk family.  The reserved negative entropy/R16 ledgers need only be matched against these coefficients, not against an arbitrary full-line four-sine kernel.

The relation code has minimum weight four, so the retained shell automatically deletes the constant and quadratic truth-table Fourier modes.  This is the same distance-four cancellation seen in the phase-switch theorem, now expressed at the level of **every** scalar squared-correlation feature.

---

## 7. A rigorous obstruction: diagonalizing away the shell/syndrome structure is catastrophically too expensive

The new factorization also shows exactly what not to do next.

Suppose one tries to pay the Brownian source coefficient-by-coefficient, discarding both the retained-shell restriction and the signed same-syndrome sum.  The natural full-cube diagonal cost is

\[
\mathscr R_N(f)
:=4N^2\sum_{A:f_A=-1}\mu_{|A|}.
\tag{7.1}
\]

This quantity is **not** asserted to equal or lower-bound the authentic `Q_M`; it is the cost of the forbidden termwise diagonal payment scheme.

For the one-point defect, with `f=-1` at one physical vertex `x_0` and `f=+1` elsewhere,

\[
f_A=-1\quad\Longleftrightarrow\quad x_0\in A.
\]

By symmetry and (5.4),

\[
\sum_{A:x_0\in A}\mu_{|A|}
=\frac1N\sum_A|A|\mu_{|A|}
=\frac1{N^2}\,
\mathbb E|\epsilon_1+\cdots+\epsilon_{N-1}|.
\]

Therefore

\[
\boxed{
\mathscr R_N(f)
=4\,\mathbb E|\epsilon_1+\cdots+\epsilon_{N-1}|
\sim4\sqrt{\frac{2N}{\pi}}.
}
\tag{7.2}
\]

On the actual `n`-cube, `N=2^n`, while the folded influence of the one-point defect is

\[
J(f)=\frac{2n}{N}.
\tag{7.3}
\]

Hence

\[
\boxed{
\frac{\mathscr R_N(f)}{J(f)}
\sim
2\sqrt{\frac2\pi}\,
\frac{N^{3/2}}{\log_2N}
\longrightarrow\infty.
}
\tag{7.4}
\]

So a proof that replaces (5.1) by independent absolute/diagonal payments for the radial coefficients is not merely non-sharp; it has the wrong dimension scale even on the simplest folded one-point defect.  The **retained relation shell and same-syndrome signed aggregation are essential data**, exactly as demanded by the live owner route.

This is an obstruction to that proof method, not a counterexample to FEI and not a lower bound on the authentic signed bank.

---

## 8. What moved and the next precise implication

### Proved in this run

1. The terminal signed measure `alpha` is exactly the orthogonal projector multiplier `1_{C_0\D_d}`.
2. For every scalar feature of a squared dual correlation, multiplication by `f` contributes exactly `(f_A-1)` on relation `A`.
3. Therefore every Brownian/Laplace source coefficient is supported **only** on retained frustrated relations.
4. Under the authentic syndrome orbit, the source bank is exactly a same-syndrome square with one radial Krawtchouk coefficient `lambda_|A|` per relation.
5. The Brownian threshold coefficients satisfy the exact total-energy and degree-energy identities (5.3)--(5.4).
6. A full-cube termwise diagonal payment is rigorously ruled out by the one-point defect scaling (7.4).

### Still open

The universal physical contraction is now the narrower statement

\[
4N^2\sum_R\int_0^1
\left(
\sum_{\substack{A\in C_0\setminus D_d\\
 f_A=-1,\ R_A=R}}
\lambda_{|A|}^{\rm th}(u)
\right)^2du
\le C_M J(f),
\tag{8.1}
\]

and the Shannon/credit analogue is

\[
\frac{4N^2}{\ln2}\sum_R\int_0^\infty\frac1{t^2}
\left(
\sum_{\substack{A\in C_0\setminus D_d\\
 f_A=-1,\ R_A=R}}
\lambda_{|A|}^{\rm Lap}(t)
\right)^2dt
\le C_S J(f)
\tag{8.2}
\]

after the reserved terminal/negative-entropy/R16 credits are inserted without reuse.

The next nonoverlapping source-side attack should compute a **signed Hardy/finite-difference representation of the radial sequences** `lambda_k^th` and `lambda_k^Lap` in the ordered q-flip basis.  The desirable statement is not a bound on `|lambda_k|` separately; (7.4) shows why.  It is a bounded operator on the *same-syndrome sums* in (8.1)--(8.2), preserving the terminal shell.  Fleet03/B18's physical signed-curvature bank is then the natural recipient.

Full FEI remains **OPEN / NOT PROVED**.
