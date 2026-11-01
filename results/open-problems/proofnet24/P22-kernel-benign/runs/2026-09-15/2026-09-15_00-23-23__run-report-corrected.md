# ProofNet24 P22 — Kernel Benign Audit / Post-Closure Hard-Edge Assistance

**Run timestamp:** 2026-09-15 00:23:23 Asia/Jerusalem  
**Scope:** independent preservation audit of P04 Target 2, then post-certification assistance on the open P04/P20 Target 4. **NO number theory.**

# Executive verdict

P04 Target 2 remains

\[
\boxed{\textbf{PROVED / ProofNet24-CERTIFIED}.}
\]

For every fixed Gaussian-kernel bandwidth \(h>0\), every fixed degree bound \(q_0<\infty\), and every signal sequence

\[
f_d\in\bigoplus_{s=0}^{q_0}\mathcal H_{d,s},
\qquad
\sup_d\|f_d\|_{L^2(S^{d-1})}\le B,
\]

with

\[
d_\ell=2^{2^\ell},
\qquad
n_\ell=2^{2^{2\ell}},
\]

iid inputs \(X_i\sim{\rm Unif}(S^{d_\ell-1})\), iid Gaussian label noise of variance \(\sigma^2\), and the actual minimum-RKHS-norm interpolant for

\[
K_h(x,y)=\exp\!\left(-\frac{\|x-y\|^2}{2h^2}\right),
\]

the realized conditional clean-test excess risk

\[
\mathcal R_\ell
=
E_{X_0}\!\left[
(\widehat f_\ell(X_0)-f_{d_\ell}(X_0))^2
\mid X_{1:n_\ell},\varepsilon_{1:n_\ell}
\right]
\]

satisfies

\[
\boxed{\mathcal R_\ell\xrightarrow{\mathbb P}0.}
\]

The certified proof gives the stronger almost-sure statement along the prescribed super-exponential level sequence under any coupling with the correct levelwise marginals.

The newest P04 report at 23:47 Asia/Jerusalem again records Target 2 as certified and explicitly says that no Target-2 dependency is reopened.  It also records an independent P03 recheck of the two dangerous prescribed-sequence exponents.

Because Target 2 already has the required two complete OTHER-worker audits, this run redirects theorem-sized work to the open quadratic-feature hard-edge track.

The new theorem is:

## `P22-T4-GS-HYPERCONC-13` — PROVED

Let

\[
m=\frac{(d-1)(d+2)}2,
\]

and let

\[
h_1,\dots,h_m\in\mathbb R^m
\]

be iid pure degree-two fixed-radius harmonic rows, normalized so that

\[
Eh_ih_i^\top=I_m,
\qquad
\|h_i\|^2=m
\]

deterministically.

For

\[
S_r=\operatorname{span}(h_1,\dots,h_r),
\]

define the Gram-Schmidt residual

\[
D_r^2
=
\operatorname{dist}(h_{r+1},S_r)^2,
\qquad
0\le r\le m-1.
\]

Then for every \(r\), conditionally on the first \(r\) rows,

\[
E[D_r^2\mid\mathcal F_r]=m-r
\]

and

\[
\operatorname{Var}(D_r^2\mid\mathcal F_r)
\le
(4d+10)\min\{r,m-r\}.
\]

More strongly, if

\[
q=m-r,
\]

then for every \(0<\varepsilon\le1\) in the nontrivial tail regime,

\[
\boxed{
P\left\{
|D_r^2-q|>\varepsilon q
\mid\mathcal F_r
\right\}
\le
2\exp\left[
-c\varepsilon^{1/2}
\frac{q^{1/2}}
{d^{1/4}\min\{q,m-q\}^{1/4}}
\right]
}
\tag{GS-tail}
\]

for a universal \(c>0\).

Consequently, if \(q_d\le m/2\), \(0<\varepsilon_d\le1/2\), and

\[
\boxed{
\frac{
\varepsilon_d^{1/2}
\left(q_d/d\right)^{1/4}
}{
\log d
}
\longrightarrow+\infty,
}
\]

then

\[
\boxed{
P\left\{
\max_{0\le r\le m-q_d}
\left|
\frac{D_r^2}{m-r}-1
\right|
>
\varepsilon_d
\right\}
\longrightarrow0.
}
\tag{GS-unif}
\]

In particular, taking

\[
\boxed{
q_d=d(\log d)^8,
\qquad
\varepsilon_d=\frac1{\log d},
}
\]

gives

\[
\boxed{
\max_{0\le r\le m-d(\log d)^8}
\left|
\frac{D_r^2}{m-r}-1
\right|
\xrightarrow{\mathbb P}0.
}
\tag{GS-strip}
\]

Thus **all but the last \(O(d\log^8 d)\) Gram-Schmidt steps are uniformly asymptotic to their deterministic codimensions**.

This improves P04's previous Chebyshev/union-bound result, which only controlled the first \(o(d^{3/2})\) rows.  The near-square difficulty is now confined to a strip of codimension \(d^{1+o(1)}\), rather than a macroscopic fraction of the \(m\asymp d^2\) rows.

A direct corollary is:

## `P22-T4-PARTIAL-VOLUME-13` — PROVED

With the same choice

\[
q_d=d(\log d)^8,
\]

one has

\[
\boxed{
\sum_{r=0}^{m-q_d}\log D_r^2
=
\sum_{q=q_d}^{m}\log q
+
O_P\!\left(\frac{m}{\log d}\right).
}
\tag{PV}
\]

Equivalently,

\[
\boxed{
\log\prod_{r=0}^{m-q_d}D_r^2
=
\log\frac{m!}{(q_d-1)!}
+
O_P\!\left(\frac{m}{\log d}\right).
}
\]

Thus any genuinely anomalous angular determinant behavior is forced into the last \(d(\log d)^8\) residual dimensions, up to a subleading macroscopic log-volume error.

This does **not** yet provide the polynomially sharp negative-determinant moments required for an ordinary-law/determinant-biased change of measure.  It is a localization theorem, not a hard-edge theorem.

---

# 1. Sources read

## 1.1 Latest full P22

Read in full:

`2026-09-14_23-23-56__run-report-corrected.md`.

That report re-preserved the complete Target-2 proof and proved:

- `P22-T4-ORBIT-INCOHERENCE-12`;
- `P22-T4-HAAR-BOTTOMSUBSPACE-12`;
- `P22-T4-ACTUAL-ORBIT-MEAN-12`;
- `P22-T4-ORBIT-HYPERCONTR-BARRIER-12`.

Its main hard-edge reduction is

\[
\Theta_4(E)
\le
\frac{d-1}{d}
\sup_{u\in S^{d-1}}
\|P_{T(E)}B_u\|^2.
\]

For Haar \(k\)-planes with \(k\le d\), the right-hand side is \(O(d^{-1})\) with probability \(1-e^{-\Omega(d)}\).  For the actual harmonic bottom spectral window, physical symmetry already gives the exact fixed-direction mean \(k/m\).

## 1.2 Latest P04

Latest source:

- Gmail message id `1a0a1b392b8d7a27`;
- subject `[ProofNet24] P04 | Kernel conjectures | 2026-09-14 23:47 Asia/Jerusalem`.

Its ledger remains:

- Target 1: PROVED / candidate complete;
- Target 2: **PROVED / certified**;
- Target 3: PROVED / candidate complete;
- Target 4: OPEN.

Its new Target-4 claims are:

- `P04-T4-ANGULAR-DERAD-16`;
- `P04-T4-PROJ-COMP-16`;
- an early Gram-Schmidt consequence based on Chebyshev;
- a fixed-direction small-ball calibration.

This run independently audits the exact de-radialization identity below.

## 1.3 OTHER RMT worker P20

Read in full from Gmail message

`1a0a19d1007e7aea`

with subject

`[ProofNet24] P20 | Kernel hard-edge audit | 2026-09-14 23:12:21 Asia/Jerusalem`.

Its new facts are:

### `P20-HARMONIC-QF-SCALE-28`

There exist Hilbert-Schmidt-unit coefficient operators for which the harmonic-row quadratic-form variance is \(\Theta(d)\).  Hence the optimal Frobenius-scale concentration assumed by some dependent-coordinate local laws is genuinely false for this row law.

### `P20-INVERSE-RAYLEIGH-28`

For the normalized inverse direction

\[
V=\frac{H^{-1}b}{\|H^{-1}b\|},
\]

\[
\frac{\|HV\|}{\sqrt m}
=
O_P(d^{-1/2}).
\]

### `P20-CRITICAL-S4-GAP-28`

If

\[
\gamma_K(H)
=
\inf_{\operatorname{Tr}(T(v)^4)\ge K/d}
\frac{\|Hv\|}{\sqrt m}
\]

satisfies

\[
\gamma_K(H)\ge c_Kd^{-1/4}
\]

with high probability for sufficiently large fixed \(K\), then the actual inverse direction is fourth-Schatten delocalized:

\[
\operatorname{Tr}(T(V)^4)=O_P(d^{-1}).
\]

The current P20 obstruction is therefore purely angular and genuinely near-square.

---

# 2. Target-2 preservation audit

Put

\[
R=2^\ell,
\qquad
d=2^R,
\qquad
n=d^R,
\qquad
k=R+\ell-1.
\]

The dangerous prescribed-sequence ratios remain

\[
\boxed{
\frac{N_{d,k}}n
=
d^{\delta_*+o(1)},
}
\]

\[
\boxed{
\frac{D_{<k}}n
=
d^{-(1-\delta_*)+o(1)},
}
\]

where

\[
\delta_*
=
\frac1{\log2}-1
=
0.442695\ldots.
\]

Indeed, using \(R=2^\ell\),

\[
\frac{\log(k!)}{\log d}
=
\frac{\log(k!)}{R\log2}
=
\ell-\frac1{\log2}+o(1),
\]

and therefore

\[
k-R-\frac{\log(k!)}{\log d}
=
\frac1{\log2}-1+o(1),
\]

while the degree-\((k-1)\) cumulative block gives

\[
(k-1)-R-\frac{\log((k-1)!)}{\log d}
=
\frac1{\log2}-2+o(1).
\]

No exponent sign changes.

The exact Gaussian-kernel Mercer series remains

\[
\lambda_{d,s}
=
e^{-\gamma}
\sum_{r\ge0}
\frac{\gamma^{s+2r}}
{2^rr!\,d(d+2)\cdots(d+2(s+r)-2)},
\qquad
\gamma=h^{-2}.
\]

The positive series gives the whole-tail ratio

\[
\boxed{
\lambda_{d,s+1}
\le
\frac{\gamma}{d+2s}\lambda_{d,s}.
}
\]

For a pure degree-\(s\) spherical harmonic,

\[
\boxed{
\|Y_s\|_p
\le
(p-1)^{s/2}\|Y_s\|_2,
\qquad
p\ge2,
}
\]

with no hidden degree-dependent constant.

At the proof's moment order \(q=R\),

\[
3^k=d^{\log_2 3+o(1)},
\]

so the first conservative Rosenthal term satisfies

\[
\boxed{
dR\,\frac{3^k}{\sqrt n}
=
d^{-R/2+O(1)}
\to0.
}
\]

Likewise

\[
(2R)^k
=
d^{\ell+1+o(1)},
\]

so

\[
\boxed{
Rd^2\,\frac{(2R)^k}{n}
=
d^{-R+\ell+O(1)}
\to0.
}
\]

The infinite harmonic tail is summed factorially rather than by a fixed-degree truncation.

The KRM application still uses its pre-relaxation row-square/correlation-kernel statistic.  The current primary KRM paper states exactly that its operator-norm method is built from U-statistic decoupling and the noncommutative Khintchine inequality, reducing the kernel-matrix problem to scalar kernel statistics and a correlation-kernel matrix.

The low/high decomposition remains:

\[
\Psi^\top\Psi=n(I+o_{\rm op}(1)),
\]

\[
K_T=\tau(I+o_{\rm op}(1)),
\]

and exact RKHS elimination gives

\[
G_0
=
\tau\Lambda^{-1}+\Psi^\top W\Psi
\succeq cnI.
\]

Therefore

\[
\|G_0^{-1}\|=O(n^{-1}),
\]

and

\[
E_\varepsilon[\mathcal R_\ell\mid X]
\le
C\left[
\sigma^2\left(
\frac{D_{<k}}n+\frac n{N_k}
\right)
+
B^2\left(
\frac{d^{2q_0}}{n^2}
+
\frac{d^{2q_0}}{nN_k}
\right)
\right]
\to0.
\]

No nonuniform estimate was found.

### `P22-T2-RECHECK-13`

**Verdict:** PASS.  Target 2 remains certified.

---

# 3. Audit of P04's new angular de-radialization theorem

## `P22-AUDIT-P04-ANGULAR-DERAD-13`

**Source:** Gmail `1a0a1b392b8d7a27`  
**Claim ID:** `P04-T4-ANGULAR-DERAD-16`  
**Verdict:** **PROVED / PASS.**

Let

\[
E=\operatorname{Sym}_d^0,
\qquad
m=\frac{(d-1)(d+2)}2,
\]

and choose a Frobenius-orthonormal basis \(E_a\) of \(E\).

For \(u\sim{\rm Unif}(S^{d-1})\),

\[
h_a(u)
=
\sqrt{\frac{d(d+2)}2}\,u^\top E_au.
\]

For \(g=ru\sim N(0,I_d)\),

\[
\phi_a(g)
=
\frac{g^\top E_ag}{\sqrt2}.
\]

Then exactly

\[
\boxed{
\phi(g)=a(r)h(u),
\qquad
a(r)=\frac{r^2}{\sqrt{d(d+2)}}.
}
\]

The radial variable \(a(r)\) is independent of \(h(u)\).

Because \(r^2\sim\chi_d^2\),

\[
Er^4=d(d+2),
\]

so

\[
\boxed{Ea^2=1.}
\]

Also

\[
Er^8=d(d+2)(d+4)(d+6),
\]

hence

\[
\boxed{
Ea^4
=
s_d
=
\frac{(d+4)(d+6)}{d(d+2)}.
}
\]

For self-adjoint \(B:E\to E\), put

\[
X=h^\top Bh,
\qquad
\mu=EX=\operatorname{Tr}B.
\]

Then

\[
\phi^\top B\phi=a^2X,
\]

and independence gives

\[
E(\phi^\top B\phi)^2
=
s_dE X^2.
\]

Therefore

\[
\operatorname{Var}_G(\phi^\top B\phi)
=
s_d\operatorname{Var}_h(X)
+
(s_d-1)\mu^2.
\]

Using P04's already-audited Gaussian chaos identity

\[
\operatorname{Var}_G(\phi^\top B\phi)
=
8\|C(B)\|_F^2
+
6\|K(B)\|^2,
\]

one obtains exactly

\[
\boxed{
\operatorname{Var}_h(h^\top Bh)
=
\frac{
8\|C(B)\|_F^2
+
6\|K(B)\|^2
-
(s_d-1)(\operatorname{Tr}B)^2
}{s_d}.
}
\]

Finally,

\[
s_d-1
=
\frac{(d+4)(d+6)-d(d+2)}{d(d+2)}
=
\boxed{
\frac{8(d+3)}{d(d+2)}.
}
\]

Every constant checks.

P04's projection corollary also checks: for a rank-\(k\) projection \(P\),

\[
0\le C(P)\le\frac md I,
\qquad
\operatorname{Tr}C(P)=k,
\]

so

\[
\|C(P)\|_F^2\le\frac md k,
\qquad
\|K(P)\|^2\le k.
\]

Thus

\[
\operatorname{Var}(h^\top Ph)
\le
(4d+10-8/d)k,
\]

and because \(\|h\|^2=m\) deterministically,

\[
\boxed{
\operatorname{Var}(h^\top Ph)
\le
(4d+10)\min\{k,m-k\}.
}
\]

This complement-sensitive variance estimate is the key input to the new theorem below.

---

# 4. Degree-four hypercontractive tail lemma

Fix a deterministic orthogonal projection \(P\) on the harmonic coefficient space.

The function

\[
u\mapsto h(u)^\top Ph(u)
\]

is an even spherical polynomial of degree at most four.

Its spherical-harmonic decomposition has degrees \(0,2,4\).

After centering,

\[
X_P
=
h^\top Ph-\operatorname{Tr}P
=
F_2+F_4,
\]

with \(F_2\) and \(F_4\) orthogonal in \(L^2(S^{d-1})\).

The pure-harmonic hypercontractive estimate already used and audited in Target 2 gives, for \(p\ge2\),

\[
\|F_2\|_p
\le
(p-1)\|F_2\|_2,
\]

\[
\|F_4\|_p
\le
(p-1)^2\|F_4\|_2.
\]

Therefore

\[
\begin{aligned}
\|X_P\|_p
&\le
(p-1)\|F_2\|_2
+
(p-1)^2\|F_4\|_2
\\
&\le
(p-1)^2
\left(
\|F_2\|_2+\|F_4\|_2
\right)
\\
&\le
\boxed{
\sqrt2\,(p-1)^2\|X_P\|_2.
}
\end{aligned}
\tag{HC4}
\]

Thus, writing

\[
\sigma_P^2=\operatorname{Var}(h^\top Ph),
\]

for \(t/\sigma_P\) larger than a universal constant,

\[
\boxed{
P\{|X_P|>t\}
\le
2\exp\left[
-c\sqrt{\frac{t}{\sigma_P}}
\right]
}
\tag{SW4}
\]

for a universal \(c>0\).

Indeed, Markov gives

\[
P\{|X_P|>t\}
\le
\left[
\frac{\sqrt2\,p^2\sigma_P}{t}
\right]^p.
\]

Choosing

\[
p
\asymp
\sqrt{\frac{t}{\sigma_P}}
\]

makes the bracket a fixed number below one and yields (SW4).

This is the exact degree-four sub-Weibull scale expected from hypercontractivity.

No stronger exponential concentration is claimed.

---

# 5. Proof of `P22-T4-GS-HYPERCONC-13`

Let

\[
\mathcal F_r
=
\sigma(h_1,\dots,h_r).
\]

Almost surely every prefix is linearly independent because the full square harmonic matrix is invertible almost surely.

Condition on \(\mathcal F_r\).

Let \(P_r^\perp\) be the orthogonal projector onto \(S_r^\perp\).

Its rank is

\[
q=m-r.
\]

Then

\[
D_r^2
=
h_{r+1}^\top P_r^\perp h_{r+1}.
\]

Isotropy gives

\[
\boxed{
E[D_r^2\mid\mathcal F_r]=q.
}
\]

P04's complement-sensitive variance theorem gives

\[
\boxed{
\operatorname{Var}(D_r^2\mid\mathcal F_r)
\le
(4d+10)\min\{q,m-q\}.
}
\tag{5.1}
\]

Let

\[
\sigma_r
=
\sqrt{
\operatorname{Var}(D_r^2\mid\mathcal F_r)
}.
\]

Apply (SW4) with

\[
t=\varepsilon q.
\]

Then

\[
\sqrt{\frac{t}{\sigma_r}}
\ge
c\varepsilon^{1/2}
\frac{
q^{1/2}
}{
d^{1/4}\min\{q,m-q\}^{1/4}
},
\]

which proves (GS-tail).

Now fix \(q_d\le m/2\).

There are two ranges.

### Early and middle range: \(q\ge m/2\)

Then

\[
q^{1/2}\gtrsim d,
\qquad
\min\{q,m-q\}\le m/2\lesssim d^2.
\]

Hence the exponent in (GS-tail) is at least

\[
c\varepsilon_d^{1/2}d^{1/4}.
\]

### Late but noncritical range: \(q_d\le q<m/2\)

Then

\[
\min\{q,m-q\}=q,
\]

so the exponent is at least

\[
c\varepsilon_d^{1/2}
\left(\frac{q_d}{d}\right)^{1/4}.
\]

Therefore

\[
P\left\{
\max_{0\le r\le m-q_d}
\left|
\frac{D_r^2}{m-r}-1
\right|
>
\varepsilon_d
\right\}
\]

is bounded by

\[
m
\exp\left[
-c\varepsilon_d^{1/2}
\left(\frac{q_d}{d}\right)^{1/4}
\right]
+
m
\exp\left[
-c\varepsilon_d^{1/2}d^{1/4}
\right].
\]

The assumed ratio-to-\(\log d\) condition forces both terms to zero, uniformly over the unknown universal tail constant.

Thus (GS-unif) holds.

For

\[
q_d=d(\log d)^8,
\qquad
\varepsilon_d=(\log d)^{-1},
\]

the late-range exponent is

\[
\varepsilon_d^{1/2}
\left(\frac{q_d}{d}\right)^{1/4}
=
(\log d)^{-1/2}(\log d)^2
=
(\log d)^{3/2},
\]

which dominates \(\log m=O(\log d)\).

Hence (GS-strip) follows.

QED.

---

# 6. Proof of `P22-T4-PARTIAL-VOLUME-13`

On the event in (GS-strip),

\[
\left|
\frac{D_r^2}{m-r}-1
\right|
\le
\frac1{\log d}
\]

for all \(r\le m-q_d\).

For large \(d\), \(1/\log d<1/2\), and therefore

\[
|\log(1+x)|
\le
2|x|
\qquad
(|x|\le1/2).
\]

Thus

\[
\left|
\log D_r^2
-
\log(m-r)
\right|
\le
\frac{2}{\log d}
\]

uniformly over those \(r\).

Summing at most \(m\) terms,

\[
\boxed{
\sum_{r=0}^{m-q_d}\log D_r^2
=
\sum_{r=0}^{m-q_d}\log(m-r)
+
O_P\left(\frac{m}{\log d}\right).
}
\]

Reindexing \(q=m-r\),

\[
\sum_{r=0}^{m-q_d}\log(m-r)
=
\sum_{q=q_d}^{m}\log q
=
\log\frac{m!}{(q_d-1)!}.
\]

This proves (PV).

QED.

---

# 7. What the new theorem does and does not solve

The P04 Chebyshev argument controlled only

\[
r=o(d^{3/2})
\]

from the start of Gram-Schmidt.

The new hypercontractive estimate reaches all the way to

\[
m-r
=
d(\log d)^8.
\]

Since

\[
m\asymp d^2,
\]

this confines the uncontrolled region to a vanishing fraction

\[
\frac{d(\log d)^8}{m}
=
O\left(\frac{(\log d)^8}{d}\right)
\to0.
\]

This is relevant to:

- determinant-volume bias;
- coordinate/Gram-Schmidt peel arguments;
- early/middle reciprocal resistance.

It does **not** identify the microscopic square hard edge.

It also does **not** imply the P20 restricted S4 gap

\[
\gamma_K(H)\gtrsim d^{-1/4},
\]

because that theorem asks for a uniform Rayleigh gap on an adaptive coefficient cone, not row-by-row residual concentration.

The last \(d(\log d)^8\) residual dimensions still contain all possible hard-edge pathology.

---

# 8. Relation to the previous orbit-incoherence route

The previous P22 theorem reduced bottom-subspace fourth-Schatten delocalization to

\[
\sup_u
\|P_{T(E_k)}B_u\|^2
=
O_P(d^{-1}).
\]

The present Gram-Schmidt theorem attacks a different branch.

The orbit theorem controls **right spectral geometry**.

The Gram-Schmidt theorem controls **row-volume geometry**.

Both indicate that the only genuinely difficult behavior is near the square edge:

- fixed-direction means are already isotropic;
- Haar bottom subspaces have the desired orbit incoherence;
- row residuals are deterministic through all but \(d^{1+o(1)}\) final codimensions.

This increasingly localizes any non-Wishart mechanism to the final near-kernel layer.

---

# 9. Imported-result verification

The Target-2 primary kernel-matrix source remains:

**Kaushik–Romberg–Muthukumar, arXiv:2511.03892.**

Its stated method uses:

- decoupling for U-statistics;
- noncommutative Khintchine;
- scalar kernel statistics;
- a correlation-kernel matrix.

This matches the P22 application and does not require an iid-entry model for the empirical kernel matrix.

For the new Gram-Schmidt theorem, no new external theorem beyond the already-certified pure spherical-harmonic hypercontractive inequality is imported.

The degree-four estimate is obtained by decomposing a centered quadratic form in the degree-two harmonic row into its degree-2 and degree-4 spherical-harmonic components and applying the same pure-degree inequality separately.

---

# 10. Counterexample search

## 10.1 Could the degree-four tail be Gaussian?

No such claim is made.

Hypercontractivity gives only

\[
\exp[-c(t/\sigma)^{1/2}],
\]

the natural degree-four sub-Weibull tail.

The proof uses exactly that weaker scale.

## 10.2 Does row residual concentration imply a smallest-singular-value bound?

No.

A triangular matrix may have well-behaved early QR diagonals while the final few diagonals create the entire small singular value.

The theorem only confines where pathology can occur.

## 10.3 Does partial log-volume concentration imply determinant change-of-measure control?

Not at the polynomial precision needed for hard-edge universality.

The error

\[
O_P(m/\log d)
\]

is small compared with the macroscopic \(\Theta(m\log d)\) log-volume, but exponentiating it is still enormous.

## 10.4 Can the uncontrolled strip be reduced to \(O(d)\) with the same simple argument?

Not while taking a vanishing uniform relative error and paying a union bound over all rows.

At \(q\asymp d\), the degree-four hypercontractive exponent at fixed relative error is only \(O(1)\), so a different near-square argument is required.

This identifies a genuine transition around the residual dimension \(q\asymp d\), consistent with the critical scale seen in P20.

---

# 11. Updated ledger

## PROVED — Target 2

- exact Gaussian-kernel Mercer eigenvalues;
- whole-tail Mercer ratio;
- exact critical cutoff;
- harmonic multiplicity asymptotics;
- dimension-free growing-degree spherical hypercontractivity;
- factorial infinite-tail summation;
- conservative Rosenthal closure;
- KRM proof-level row-square/correlation-kernel decoupling step;
- low harmonic matrix Chernoff;
- exact low/high RKHS elimination;
- inverse-Gram control;
- fixed-degree signal bias;
- high-frequency noise leakage;
- conditional excess risk \(\to0\) in probability;
- almost-sure prescribed-sequence strengthening;
- two complete OTHER-worker audits;
- ProofNet24 certification;
- `P22-T2-RECHECK-13` PASS this run.

## PROVED — post-closure Target-4 assistance

Inherited:

- traceless Haar fourth moment;
- right-invariant inverse-direction Haar benchmark;
- S4 bottom-window split;
- orbit-incoherence reduction;
- Haar bottom-subspace theorem;
- actual fixed-orbit mean isotropy;
- hypercontractive barrier.

New this run:

- **`P22-AUDIT-P04-ANGULAR-DERAD-13`** — PASS;
- **degree-four harmonic projection tail** `(SW4)`;
- **`P22-T4-GS-HYPERCONC-13`**;
- **`P22-T4-PARTIAL-VOLUME-13`**.

## CONDITIONAL / OPEN

1. P20 restricted S4 gap:
   \[
   \gamma_K(H)\ge c_Kd^{-1/4}.
   \]

2. Fixed-orbit exponential bottom-spectral-projector tail.

3. Consequently:
   \[
   \Theta_4(E_k)=O_P(d^{-1}).
   \]

4. Inverse-tail mass:
   \[
   \eta_k=O_P(d^{-1/4}).
   \]

5. Fourth-Schatten delocalization of the inverse direction.

6. Final \(d^{1+o(1)}\) Gram-Schmidt/hard-edge strip.

7. Growing bottom spectral tail.

8. Annealed graph-factor \(L^1\) control.

9. Early/middle reciprocal resistance at the precision needed by the secular proof.

10. Full fixed-\(t\) hard-edge universality.

## DISPROVED / INSUFFICIENT

- Target 2 requires a microscopic hard-edge theorem;
- fixed-degree constants can be extrapolated to the growing critical degree;
- KRM can be replaced by max-entry control;
- physical \(O(d)\) invariance implies coefficient-space Haar behavior;
- mean isotropy implies uniform fourth-Schatten delocalization;
- generic degree-two hypercontractivity closes the bottom-subspace supremum;
- P04's Gaussian contraction lower bound survives unchanged after fixed-radius conditioning;
- early Gram-Schmidt concentration alone determines the hard edge;
- partial log-volume control at \(O(m/\log d)\) is enough for determinant change of measure.

---

# 12. Exact dependency graph after this run

The certified Target-2 chain is unchanged:

\[
\text{exact Mercer spectrum}
+
\text{multiplicity gap}
+
\text{growing-degree hypercontractivity}
+
\text{factorial tail}
\]

\[
\Downarrow
\]

\[
\text{Rosenthal + KRM row-square/correlation-kernel control}
\]

\[
\Downarrow
\]

\[
K_T=\tau(I+o_{\rm op}(1)).
\]

Separately,

\[
\text{addition theorem + matrix Chernoff}
\Longrightarrow
\Psi^\top\Psi=n(I+o_{\rm op}(1)).
\]

Exact elimination then gives \(G_0\succeq cnI\), and both noise and signal errors vanish.

The post-closure hard-edge picture is now:

\[
\boxed{
\text{fixed-radius harmonic projection variance}
}
\]

\[
\Downarrow
\]

\[
\boxed{
\text{degree-four hypercontractive tail}
}
\]

\[
\Downarrow
\]

\[
\boxed{
D_r^2=(m-r)(1+o_P(1))
}
\]

uniformly through

\[
m-r\ge d(\log d)^8.
\]

Thus:

\[
\boxed{
\text{all nontrivial angular volume / hard-edge pathology is confined to the last }d^{1+o(1)}\text{ residual dimensions.}
}
\]

In parallel, the previous P22/P20 route requires:

\[
\boxed{
\text{bottom spectral orbit incoherence}
}
+
\boxed{
\text{inverse-tail mass control}
}
\]

to obtain fourth-Schatten delocalization.

---

# 13. Highest-value next attack

The next P22 run should attack the final strip rather than re-prove macroscopic isotropy.

Two concrete targets are now available.

## Route A — `P22/P20-T4-FIXED-ORBIT-TAIL-14`

For \(k=\lfloor\sqrt d\rfloor\) and fixed \(u\),

\[
P\left\{
\|P_{E_k}T^{-1}(B_u)\|^2>\frac Cd
\right\}
\le e^{-cd}.
\]

This would close the bottom-subspace S4 branch by a physical sphere net.

## Route B — `P22-T4-FINAL-STRIP-RESISTANCE-14`

Use the new uniform Gram-Schmidt theorem to strip off the first

\[
m-d(\log d)^8
\]

rows and prove only the coarse reciprocal resistance needed for the remaining

\[
d(\log d)^8
\]

near-square block.

This route no longer needs to pay weak concentration errors over \(m\asymp d^2\) stages.

The second route may be particularly compatible with P04's coordinate-peel / Schur recursion.

---

# Bottom line

Target 2 remains rigorously closed and certified.

The new theorem extends fixed-radius harmonic Gram-Schmidt concentration from P04's first \(o(d^{3/2})\) rows to **all but the final \(d(\log d)^8\) residual dimensions**, with a vanishing uniform relative error:

\[
\boxed{
\max_{0\le r\le m-d(\log d)^8}
\left|
\frac{D_r^2}{m-r}-1
\right|
\xrightarrow{\mathbb P}0.
}
\]

The proof uses only:

- P04's exact angular de-radialization and complement-sensitive variance;
- the same dimension-free pure spherical-harmonic hypercontractivity already certified in Target 2;
- a degree-\(\le4\) harmonic decomposition;
- a union bound.

This does not solve the hard edge, but it sharply confines the unresolved angular pathology to a final \(d^{1+o(1)}\) near-square strip.

That localization is the principal new progress of this run.
