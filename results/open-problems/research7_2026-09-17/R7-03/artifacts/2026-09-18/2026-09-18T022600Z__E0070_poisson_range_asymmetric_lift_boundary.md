Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime reasoning telemetry or binding model/effort selector is exposed.

# E0070 / Björklund Problem 2 — exact Poisson range, an asymmetric lift, and the boundary charge at infinity

Date: 2026-09-18 UTC  
Worker: R7-03 Boundary-Case Research  
Canonical target: E0070  
Source: Michael Björklund, *Five remarks about random walks on groups*, arXiv:1406.0763v2 (2014), Appendix II §7.1, Problem 2, printed p.24.  
Previous artifact: `research7_2026-09-17/R7-03/artifacts/2026-09-18/2026-09-18T012700Z__E0070_finite_volume_duality.md`.

This note continues the already-complete source-level proof candidate without changing the frozen completion flag `C_E0070=1`.  The aim is to stress-test the mechanism in three directions prescribed by the preceding report: B3 strengthens the theorem from constant defects to the exact Poisson range; B15 deliberately removes ambient symmetry and involutivity; B29 compactifies the star and identifies the nonintegrable boundary charge carried by formal nonzero defects.

## 1. Recalled symmetric quotient kernel

Let

\[
X=\mathbb N_0,\qquad
G=\operatorname{Sym}_{\mathrm{fin}}(X),\qquad
H=\operatorname{Stab}_G(0).
\]

For `n>=1`, let `tau_n=(0 n)`, and choose any strictly positive probability vector `(p_n)_{n>=1}`.  Put `mu(tau_n)=p_n`.  Under `G/H \cong X`, the quotient operator is

\[
(Pu)(0)=\sum_{n\ge1}p_nu(n),
\tag{1.1}
\]

and

\[
(Pu)(n)=p_nu(0)+(1-p_n)u(n),\qquad n\ge1.
\tag{1.2}
\]

The source-valid domain at the center is

\[
\mathcal D_p:=\left\{u:X\to\mathbb C:\sum_{n\ge1}p_n|u(n)|<\infty\right\}.
\tag{1.3}
\]

The earlier proof showed that every `u in D_p` satisfying `Pu=u+c` has `c=0` and is constant.  We now identify the complete range of `P-I` on this domain.

## 2. B3 — exact Poisson-range theorem

For a sequence `d=(d_0,d_1,...)`, define

\[
\ell^1_0(X):=
\left\{d:\sum_{n\ge1}|d_n|<\infty,\quad d_0+\sum_{n\ge1}d_n=0\right\}.
\tag{2.1}
\]

### Theorem 2.1 — exact range and kernel

For the star operator (1.1)-(1.2),

\[
\boxed{\operatorname{Ran}\bigl((P-I)|_{\mathcal D_p}\bigr)=\ell^1_0(X)}
\tag{2.2}
\]

and

\[
\boxed{\ker\bigl((P-I)|_{\mathcal D_p}\bigr)=\{\text{constant functions}\}.}
\tag{2.3}
\]

More explicitly, if `d=(P-I)u`, then for every `n>=1`,

\[
d_n=p_n(u(0)-u(n)),
\tag{2.4}
\]

and

\[
d_0=\sum_{n\ge1}p_nu(n)-u(0).
\tag{2.5}
\]

Conversely, for every `d in ell^1_0(X)` and every arbitrary constant `a in C`,

\[
\boxed{u(0)=a,\qquad u(n)=a-\frac{d_n}{p_n}}
\tag{2.6}
\]

lies in `D_p` and satisfies `(P-I)u=d`.

#### Proof

Let `u in D_p` and put `d=(P-I)u`.  Formula (2.4) follows directly from (1.2).  Therefore

\[
\sum_{n\ge1}|d_n|
\le
\sum_{n\ge1}p_n|u(0)|+
\sum_{n\ge1}p_n|u(n)|
=|u(0)|+\sum_{n\ge1}p_n|u(n)|<\infty.
\tag{2.7}
\]

Moreover, absolute convergence allows us to sum the leaf defects:

\[
\begin{aligned}
\sum_{n\ge1}d_n
&=u(0)\sum_{n\ge1}p_n-\sum_{n\ge1}p_nu(n)\\
&=u(0)-\sum_{n\ge1}p_nu(n)\\
&=-d_0.
\end{aligned}
\tag{2.8}
\]

Thus every range vector belongs to `ell^1_0(X)`.

Conversely, let `d in ell^1_0(X)` and fix any `a in C`.  Define `u` by (2.6).  Then

\[
\sum_{n\ge1}p_n|u(n)|
\le |a|\sum_{n\ge1}p_n+
\sum_{n\ge1}|d_n|
<\infty,
\tag{2.9}
\]

so `u in D_p`.  The leaf equations give immediately

\[
p_n(u(0)-u(n))=d_n.
\tag{2.10}
\]

At the center,

\[
\begin{aligned}
(P-I)u(0)
&=\sum_{n\ge1}p_n\left(a-\frac{d_n}{p_n}\right)-a\\
&=-\sum_{n\ge1}d_n=d_0,
\end{aligned}
\tag{2.11}
\]

using the balance condition in (2.1).  Hence `(P-I)u=d`, proving (2.2).

Finally, if `(P-I)u=0`, (2.4) gives `p_n(u(0)-u(n))=0` for every `n`; strict positivity of `p_n` forces `u(n)=u(0)`, proving (2.3). ∎

### Corollary 2.2 — quasi-harmonic rigidity is an immediate range obstruction

A constant defect `d_x=c` on all of `X` belongs to `ell^1_0(X)` only for `c=0`: if `c != 0`, then the leaf part `(c,c,...)` is not in `ell^1`.  Therefore no source-integrable solution of

\[
Pu=u+c
\tag{2.12}
\]

can have `c != 0`.  For `c=0`, Theorem 2.1 gives constants only.

This recovers the analytic core of E0070 as one line from the exact range theorem and strengthens it to arbitrary summable balanced defects.

### Corollary 2.3 — quotient-space isomorphism

Modulo constants, `(P-I)` is bijective from `D_p/C` onto `ell^1_0(X)`, with explicit inverse (2.6).  The obstruction is therefore not qualitative recurrence folklore: the quotient Poisson equation has an exact algebraic range.

**B3 outcome: SUCCESS.**  The constant-defect theorem extends to a complete characterization of all source-integrable Poisson defects.

## 3. B15 — deliberately destroy symmetry and involutivity

The preceding construction used involutive generators and a symmetric measure.  We now remove both features while keeping the quotient channel exactly the same.

Let

\[
G^\sharp=C_3\times\operatorname{Sym}_{\mathrm{fin}}(\mathbb N_0),
\qquad
H^\sharp=C_3\times\operatorname{Stab}(0),
\tag{3.1}
\]

where `C_3=Z/3Z`.  For every `n>=1`, define

\[
g_n=(1,\tau_n),\qquad \tau_n=(0\ n),
\tag{3.2}
\]

and let

\[
\mu^\sharp(g_n)=p_n.
\tag{3.3}
\]

### Proposition 3.1 — this is a non-symmetric measured group

Every `g_n` has order six and is not an involution.  Its inverse is

\[
g_n^{-1}=(2,\tau_n),
\tag{3.4}
\]

which is not in the support (3.2).  Hence `mu^sharp` is genuinely non-symmetric.

Nevertheless, its support semigroup-generates all of `G^sharp`.

#### Proof

For each `n`,

\[
g_n^2=(2,e),\qquad
g_n^3=(0,\tau_n),\qquad
g_n^4=(1,e).
\tag{3.5}
\]

Thus the generated semigroup contains both central generators `(1,e),(2,e)` and every pure star transposition `(0,tau_n)`.  The latter semigroup-generates `Sym_fin(N_0)` because

\[
(0,\tau_i)(0,\tau_j)(0,\tau_i)=(0,(i\ j)).
\tag{3.6}
\]

Therefore the semigroup contains `C_3 x Sym_fin(N_0)=G^sharp`. ∎

### Proposition 3.2 — the quotient operator is still the same star

The quotient `G^sharp/H^sharp` is naturally identified with `N_0` through the symmetric-group coordinate.  Björklund's left operator uses `check(mu^sharp)`, whose support consists of the inverses `(2,tau_n)`.  The central `C_3` coordinate lies entirely in `H^sharp`, so it disappears on the quotient.  Thus `g_n^{-1}` acts on `G^sharp/H^sharp` exactly as `tau_n`, and the quotient operator is again (1.1)-(1.2).

The source integrability condition is again exactly

\[
\sum_{n\ge1}p_n|u(n)|<\infty.
\tag{3.7}
\]

Hence Theorem 2.1 applies verbatim.

### Corollary 3.3 — an asymmetric source-level solution

For every strictly positive probability vector `(p_n)`, the non-symmetric measured group `(G^sharp,mu^sharp)` with infinite-index subgroup `H^sharp` has no nonconstant source-valid left harmonic functions and no nonconstant source-valid left quasi-harmonic functions on `G^sharp/H^sharp`.

So ambient symmetry, reversibility and involutive support are **not** essential to the construction.  The essential object is the quotient star channel together with semigroup generation upstairs.

**B15 outcome: SUCCESS.**  The source problem admits an explicit genuinely non-symmetric, non-involutive realization with exactly the same quotient rigidity.

## 4. B29 — add the point at infinity and identify the escape charge

Because `(p_n)` is a positive summable probability vector,

\[
p_n\to0.
\tag{4.1}
\]

For any formal function `u` on the star, define the scaled boundary coordinate

\[
z_n:=p_n\bigl(u(n)-u(0)\bigr).
\tag{4.2}
\]

By the leaf equation,

\[
(P-I)u(n)=-z_n.
\tag{4.3}
\]

Thus, whenever the leaf defects have a limit, the one-point compactification of the leaf set has a natural boundary trace

\[
\operatorname{Tr}_\infty(u)
:=\lim_{n\to\infty}p_n(u(n)-u(0))
=-\lim_{n\to\infty}(P-I)u(n).
\tag{4.4}
\]

### Proposition 4.1 — source-valid functions have zero boundary trace

If `u in D_p`, then the sequence `(z_n)` lies in `ell^1`, hence

\[
\boxed{\operatorname{Tr}_\infty(u)=0.}
\tag{4.5}
\]

whenever the trace is read through (4.2).

#### Proof

By (4.2),

\[
\sum_{n\ge1}|z_n|
\le |u(0)|+\sum_{n\ge1}p_n|u(n)|<\infty.
\tag{4.6}
\]

Every `ell^1` sequence tends to zero. ∎

### Proposition 4.2 — nonzero limiting defect is a nonintegrable charge at infinity

Suppose a formal solution has leaf defects

\[
d_n:=(P-I)u(n)\to\delta\ne0.
\tag{4.7}
\]

Then

\[
p_n(u(n)-u(0))\to-\delta,
\tag{4.8}
\]

so `u(n)` escapes at the exact scale `1/p_n`, and `u` cannot lie in `D_p`.

There is a second, center-mass formulation.  Let

\[
A_N:=\sum_{n=1}^Np_nu(n),\qquad
S_N:=\sum_{n=1}^Np_n.
\tag{4.9}
\]

From `u(n)=u(0)-d_n/p_n`,

\[
\boxed{A_N=u(0)S_N-\sum_{n=1}^Nd_n.}
\tag{4.10}
\]

If `d_n->delta`, Cesaro summation yields

\[
\sum_{n=1}^Nd_n=N\delta+o(N),
\]

and since `S_N->1`,

\[
\boxed{A_N=-N\delta+o(N)+u(0).}
\tag{4.11}
\]

Thus the center integral cannot converge when the boundary charge is nonzero.

For the quasi-harmonic case `d_n=c` exactly,

\[
A_N=u(0)S_N-Nc,
\tag{4.12}
\]

so the divergence is exactly linear rather than merely asymptotic.

This gives a geometric interpretation of the earlier integrability contradiction.  A formal nonzero quasi-harmonic defect is a nonzero charge at the added point at infinity.  Björklund's source integrability condition excludes precisely that charge.

**B29 outcome: SUCCESS.**  The nonintegrable formal solutions are classified at their natural compactification scale, and the source-valid domain is exactly the zero-boundary-charge side of that dichotomy.

## 5. Consequences for the source proof

The three methods are independent stress tests of the same admitted construction:

1. B3 shows that the quotient Poisson equation is exactly solvable for every and only balanced `ell^1` defect, so constant nonzero defects are excluded structurally.
2. B15 shows that neither ambient symmetry nor involutivity is needed: a non-symmetric measured-group lift gives the same quotient theorem.
3. B29 shows that the formal nonzero-defect profiles live at a genuine boundary point and fail source integrability by an explicit nonzero boundary charge.

None of these changes the frozen source-completion flag, because the preceding runs had already supplied a complete source-valid construction.  They materially reduce the audit surface: the analytic core can now be checked either by direct leaf equations, by finite-volume flux, or by the exact range theorem.

The mathematical status remains **PROVED CANDIDATE / protocol closure open** until the required independent P26 and distinct OTHER-track audits are actually present.  This R7-03 note is self-review and is not an independent audit.
