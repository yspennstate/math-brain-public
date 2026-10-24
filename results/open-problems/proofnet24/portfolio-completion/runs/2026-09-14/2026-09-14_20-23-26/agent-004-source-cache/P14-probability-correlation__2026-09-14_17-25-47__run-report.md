# ProofNet24 P14 — Probability correlation

**Run timestamp:** 2026-09-14 17:25:47 Asia/Jerusalem  
**Track:** fixed-apex overlapping non-Gaussian null normals / D-stratified random-pair correlation  
**Scope:** NO number theory  
**Status:** the sharp arbitrary-finite-variance conditional theorem
\[
\mathbb E[(1-\rho^2)^{-1/2}\mid D]\le 1+C_\xi/D
\]
remains OPEN. This run proves a new **averaged finite-variance correlation theorem** that is already sufficient for the fixed-apex correlation-average input in the original probability program: for every fixed \(\eta\in(0,1)\), the ordinary-stratum random-pair determinant kernel has excess
\[
O_{\xi,\eta,\beta}(m^{-1+\eta})
\]
after averaging over the overlap law, and the empirical fixed-apex pair average is \(1+o_{\mathbb P}(1)\). The result preserves all overlap dependence and uses P24's uniform conditional \(D^{-1+\eta}\) theorem plus exact overlap combinatorics. The singular high-correlation edge remains sharp \(O(1/D)\) at pure finite variance. Under the stronger stretched-log tail class from the previous P14 run, the averaged excess improves to \(O(1/m)\).

The main conceptual update is therefore:

\[
\boxed{
\text{sharp conditional }C/D\text{ at pure finite variance is still open,}
}
\]
but
\[
\boxed{
\text{the fixed-apex averaged random-pair correlation input is solved at pure finite variance.}
}
\]

---

## 0. Exact source target reconstructed before work

The persistent source file is:

`probability_open_problem_hourly_latest.md`

Library file id:

`file_00000000415472468cd2b0d1aa84ff58`.

Its exact P1/P14 random-pair reduction is the following.

Let the ambient row dimension be \(m\). Fix an apex and choose two \((m-1)\)-row hyperplanes \(S,T\) from a common pool. Write
\[
D=m-|S\cap T|,
\qquad
A=S\cap T,
\qquad
B=S\setminus T,
\qquad
C=T\setminus S.
\]
Then
\[
|A|=m-D,
\qquad
|B|=|C|=D-1.
\]

Condition on the realized shared block \(A\). Put
\[
E_A=\operatorname{span}(A)^\perp,
\qquad
\dim E_A=D,
\]
and choose an isometry
\[
Q_A:\mathbb R^D\to E_A\subset\mathbb R^m.
\]

For one fresh original product-law row \(X\in\mathbb R^m\), the projected row is
\[
Y=Q_A^\top X.
\]
Its coordinates are generally dependent.

The two private residual matrices
\[
BQ_A,\qquad CQ_A
\]
are conditionally independent \((D-1)\times D\) matrices whose rows are iid copies of \(Y\).

Let
\[
v,w\in S^{D-1}
\]
be their unit null directions. Then the original null-normal overlap is exactly
\[
\rho^2=(v\cdot w)^2.
\]

The source ordinary-stratum target is
\[
\boxed{
\mathbb E\left[(1-\rho^2)^{-1/2}\mid D\right]
\le
1+\frac{C}{D}+\eta_m(D),
\qquad D\ge3,
}
\]
with \(D\le2\) treated separately as high-overlap error.

The source explicitly says that the fixed-apex second-moment argument only needs:

1. a large good family of useful one-normal directions;
2. the correct one-slab probabilities;
3. an **averaged** pair kernel at Gaussian product scale.

The June snapshot therefore asked for a D-stratified theorem because it was a sufficient route, not because the final second moment intrinsically needs a sharp \(C/D\) bound for every \(D\).

---

# 1. Reports read in full this run

## 1.1 Latest P14

`P14_probability_correlation_2026-09-14_16-33-56.md`

Library id:

`file_0000000055e08243a67ce3fb6252a6d9`.

Its strongest results before this run are:

- exact shared-row conditioning and conditional independence;
- for bounded density \(+\;2+\delta\),
  \[
  \mathbb E[\rho^2\mid A]\le C/D
  \]
  and
  \[
  \mathbb E[(1-\rho^2)^{-1/2}\mid D]\le1+C/D;
  \]
- at pure fixed finite variance, the singular edge is already sharp:
  \[
  \int_0^{y_*}
  y^{-3/2}
  \Pr\{1-\rho^2\le y\mid A,v\}\,dy
  \le C_\xi/D;
  \]
- at pure fixed finite variance, P24/P12 give
  \[
  \mathbb E[(1-\rho^2)^{-1/2}\mid A]
  \le
  1+C_{\eta,\xi}D^{-1+\eta}
  \]
  for every fixed \(\eta>0\);
- the exact \(C/D\) bulk theorem was proved under the summable-modulus condition and, concretely, under stretched-log second-moment tails.

The remaining sharp endpoint was the arbitrary finite-variance bulk estimate
\[
\mathbb E[\rho^2\mid A]\stackrel{?}{\le}C_\xi/D.
\]

## 1.2 Latest P13

`P13_fourth_moment_RMT_2026-09-14_17-14-42.md`

Library id:

`file_000000002d70820eab42eb1efd2ecc02`.

P13 now proves the real fixed-law least-singular-value exponent under one fixed centered bounded-density finite-variance law. Its pair geometry needs only a fixed projective separation threshold, not the sharp determinant-kernel expectation.

The exact overlap count used there is
\[
\#\{T:m-|S\cap T|=D\}
=
\binom{m-1}{D-1}
\binom{n_0-m+1}{D-1}.
\]

For \(D=\delta m+O(1)\), the exponent per fixed \(S\) is
\[
g_\beta(\delta)
=
H(\delta)
+
(\beta-1)
H\!\left(\frac{\delta}{\beta-1}\right),
\]
while
\[
\log\binom{n_0}{m-1}
=
h(\beta)m+o(m).
\]

Thus sufficiently high-overlap pairs are exponentially sparse.

## 1.3 Latest P12

`P12_smooth_iid_least_singular_2026-09-14_16-28-34.md`

Library id:

`file_000000008b80820c81fc9448b5c85374`.

P12 supplies:

- Livshyts-based one-normal incompressibility at fixed finite variance;
- fraction averaging over the exponential family;
- fixed-law density-level small-ball control;
- the deterministic two-slab upper bound;
- P24 finite-variance fixed-angle anti-alignment;
- candidate-complete real smooth-iid least-singular-value exponent.

The P12/P24 quadratic theorem at arbitrary finite variance is
\[
\mathbb E[\rho^2\mid A]\le D^{-1+o(1)}
\]
uniformly in the realized apex.

---

# 2. Exact finite-variance conditional input from P24

The newest probability-semigroup report is:

`2026-09-14_15-53-57__run-report.md`

Library id:

`file_0000000092748230ab8d62bdc37f2e28`.

Its exact theorem is:

### P24-P14-FULL-FV-SUBPOWER — PROVED

For one fixed centered variance-one bounded-density law with finite variance, for every fixed \(\eta>0\), there is
\[
C_{\eta,\xi}<\infty
\]
such that, uniformly in every realized full-rank shared apex \(A\),
\[
\boxed{
\mathbb E\left[
(1-\rho^2)^{-1/2}\mid A
\right]
\le
1+C_{\eta,\xi}D^{-1+\eta}.
}
\tag{2.1}
\]

The sharp singular edge already satisfies
\[
\boxed{
\int_0^{y_*}
y^{-3/2}
\Pr\{1-\rho^2\le y\mid A,v\}\,dy
\le
C_\xi/D.
}
\tag{2.2}
\]

The loss from \(D^{-1}\) to \(D^{-1+\eta}\) occurs only in the bulk angular term.

No projected-coordinate independence is used.

---

# 3. Overlap law for a fixed apex

Fix
\[
n_0=\lfloor\beta m\rfloor,
\qquad
\beta>1,
\]
and let
\[
\mathcal H_m
=
\{S\subset[n_0]:|S|=m-1\},
\qquad
L_m=|\mathcal H_m|.
\]

Choose an ordered pair \(S,T\) uniformly from \(\mathcal H_m^2\). The diagonal \(S=T\) is harmless and may also be removed; its mass is \(L_m^{-1}=e^{-\Theta(m)}\).

For fixed \(S\), the number of \(T\)'s at overlap distance
\[
D=m-|S\cap T|
\]
is exactly
\[
\boxed{
N_D
=
\binom{m-1}{D-1}
\binom{n_0-m+1}{D-1}.
}
\tag{3.1}
\]

Indeed \(T\) is obtained by deleting \(D-1\) elements of \(S\) and replacing them by \(D-1\) elements from the complement of \(S\).

For
\[
D=\delta m+O(1),
\]
Stirling gives
\[
\frac1m\log N_D
=
g_\beta(\delta)+o(1),
\]
where
\[
\boxed{
g_\beta(\delta)
=
H(\delta)
+
(\beta-1)
H\!\left(\frac{\delta}{\beta-1}\right).
}
\tag{3.2}
\]

Also
\[
\frac1m\log L_m
=
h(\beta)+o(1),
\qquad
h(\beta)
=
\beta\log\beta-(\beta-1)\log(\beta-1).
\tag{3.3}
\]

Since
\[
g_\beta(\delta)\downarrow0
\qquad(\delta\downarrow0),
\]
there are fixed
\[
\delta_0=\delta_0(\beta)>0,
\qquad
\kappa=\kappa(\beta)>0
\]
such that
\[
\boxed{
\Pr\{D<\delta_0m\}
\le
e^{-\kappa m}
}
\tag{3.4}
\]
for all large \(m\).

This is a deterministic counting statement; no probability concerning the matrix entries is used.

Consequently, for every fixed
\[
0<\eta<1,
\]
\[
\begin{aligned}
\mathbb E[
D^{-1+\eta};D\ge3
]
&\le
(\delta_0m)^{-1+\eta}
+
\Pr\{3\le D<\delta_0m\}\\
&\le
C_{\beta,\eta}m^{-1+\eta}
+
e^{-\kappa m}.
\end{aligned}
\tag{3.5}
\]

Thus
\[
\boxed{
\mathbb E[
D^{-1+\eta};D\ge3
]
=
O_{\beta,\eta}(m^{-1+\eta}).
}
\tag{3.6}
\]

When the sharper conditional \(C/D\) theorem is available,
\[
\boxed{
\mathbb E[D^{-1};D\ge3]=O_\beta(m^{-1}).
}
\tag{3.7}
\]

---

# 4. New theorem P14-AVG-FV-01

Define
\[
K_{S,T}
=
(1-\rho_{S,T}^2)^{-1/2}
\]
on the ordinary strata \(D\ge3\).

### Theorem P14-AVG-FV-01 — PROVED

Let \(\xi\) be one fixed centered variance-one real law satisfying
\[
\|f_\xi\|_\infty<\infty,
\qquad
\mathbb E\xi^2=1.
\]
For the overlapping-null-normal model above, with \(n_0/m\to\beta>1\), for every fixed
\[
0<\eta<1,
\]
\[
\boxed{
\mathbb E[
K_{S,T}\,1_{\{D\ge3\}}
]
\le
1+
C_{\xi,\beta,\eta}
m^{-1+\eta}.
}
\tag{P14-AVG-FV-01}
\]

Equivalently,
\[
\boxed{
\mathbb E[
(K_{S,T}-1)\,1_{\{D\ge3\}}
]
=
O_{\xi,\beta,\eta}(m^{-1+\eta}).
}
\tag{4.1}
\]

### Proof

Condition on the selected pair and then on its shared block \(A\). By P24-P14-FULL-FV-SUBPOWER,
\[
\mathbb E[K_{S,T}\mid A]
\le
1+C_{\eta,\xi}D^{-1+\eta}.
\]

Therefore
\[
\begin{aligned}
\mathbb E[
(K_{S,T}-1)1_{\{D\ge3\}}
]
&\le
C_{\eta,\xi}
\mathbb E[
D^{-1+\eta};D\ge3
]\\
&\le
C_{\xi,\beta,\eta}
m^{-1+\eta},
\end{aligned}
\]
by (3.6).

QED.

---

# 5. Sharp averaged corollary for the stretched-log class

The previous P14 run proved, under the stretched-log second-moment tail condition,
\[
\mathbb E[K_{S,T}\mid A]
\le
1+\frac{C_\xi}{D}.
\]

Combining with (3.7):

### Corollary P14-AVG-SLOG-01 — PROVED

Under the previous P14 stretched-log hypotheses,
\[
\boxed{
\mathbb E[
(K_{S,T}-1)1_{\{D\ge3\}}
]
=
O_{\xi,\beta}(m^{-1}).
}
\tag{5.1}
\]

Thus the averaged fixed-apex kernel has the exact Haar order \(1+O(1/m)\) throughout a class strictly larger than every fixed \(2+\delta\)-moment class.

---

# 6. Empirical fixed-apex pair average

The source fixed-apex proof uses the actual empirical family of hyperplanes, not an independently resampled pair.

For a realized base pool, define
\[
\mathcal E_m
=
\frac1{L_m(L_m-1)}
\sum_{\substack{S\ne T\\D(S,T)\ge3}}
(K_{S,T}-1).
\tag{6.1}
\]

Every term is nonnegative.

By exchangeability of the base rows and a uniformly sampled ordered pair,
\[
\mathbb E\mathcal E_m
=
\mathbb E[
(K_{S,T}-1)1_{\{D\ge3\}}
].
\]

Hence P14-AVG-FV-01 gives
\[
\boxed{
\mathbb E\mathcal E_m
\le
C_{\xi,\beta,\eta}
m^{-1+\eta}.
}
\tag{6.2}
\]

Markov then yields, for example,
\[
\boxed{
\Pr\left\{
\mathcal E_m>
m^{-(1-\eta)/2}
\right\}
\le
C_{\xi,\beta,\eta}
m^{-(1-\eta)/2}.
}
\tag{6.3}
\]

Therefore
\[
\boxed{
\mathcal E_m=o_{\mathbb P}(1).
}
\tag{P14-EMP-AVG-FV}
\]

No independence between the exponentially many pair terms is asserted or needed.

This is exactly the correct use of exchangeability for the fixed-apex family.

---

# 7. Restriction to the useful good family

Let
\[
\mathcal G_m\subset\mathcal H_m
\]
be any random family satisfying
\[
|\mathcal G_m|
=
(1-o_{\mathbb P}(1))L_m.
\tag{7.1}
\]

In particular, P12's Livshyts/fraction argument gives such a family of fixed-parameter incompressible normals, with exponentially small bad fraction.

Define the ordinary-stratum good-family excess
\[
\mathcal E_m^{\rm good}
=
\frac1{|\mathcal G_m|(|\mathcal G_m|-1)}
\sum_{\substack{S,T\in\mathcal G_m\\S\ne T\\D\ge3}}
(K_{S,T}-1).
\]

Since
\[
K_{S,T}-1\ge0,
\]
the numerator is bounded by the full-family numerator. Hence
\[
\mathcal E_m^{\rm good}
\le
\frac{L_m(L_m-1)}
{|\mathcal G_m|(|\mathcal G_m|-1)}
\mathcal E_m.
\]

By (7.1), the prefactor is
\[
1+o_{\mathbb P}(1).
\]

Therefore:

### Theorem P14-GOOD-AVG-FV — PROVED

\[
\boxed{
\mathcal E_m^{\rm good}
=
o_{\mathbb P}(1).
}
\tag{P14-GOOD-AVG-FV}
\]

Thus deleting an \(o_{\mathbb P}(1)\) fraction of bad hyperplanes cannot destroy the ordinary-stratum averaged determinant-kernel estimate.

This conclusion uses positivity, not pairwise independence.

---

# 8. High-overlap strata remain negligible

The high-overlap strata are not inserted into the singular kernel.

For \(D=1\),
\[
T=S.
\]
There are exactly \(L_m\) ordered diagonal pairs.

For \(D=2\), for each fixed \(S\),
\[
N_2
=
(m-1)(n_0-m+1).
\]

Therefore
\[
\boxed{
\frac{
\#\{(S,T):D\le2\}
}{
L_m^2
}
\le
e^{-c_\beta m}
}
\tag{8.1}
\]
after absorbing polynomial factors.

The source probability program already has a separate one-/two-dimensional projection-density fallback for these strata.

Thus the singularity of
\[
\mathbb E(1-\rho^2)^{-1/2}
\]
at \(D=2\) is not an obstruction to the fixed-apex second moment.

---

# 9. High-correlation tail status at pure finite variance

The high-correlation edge is sharper than the bulk.

Let
\[
Y=1-\rho^2.
\]

P24 proves, uniformly in the realized apex and the first private line,
\[
\boxed{
\Pr\{Y\le y\mid A,v\}
\le
[C_K(Dy)^{1/3}]^{D-1}
}
\tag{9.1}
\]
for the ultra-edge \(Dy\) sufficiently small.

It also proves fixed \(a_0,y_*,c_\xi>0\) such that
\[
\boxed{
\Pr\{Y\le y\mid A,v\}
\le
e^{-c_\xi D}
}
\tag{9.2}
\]
through the mesoscopic range
\[
a_0/D\le y\le y_*.
\]

Finally,
\[
\boxed{
\int_0^{y_*}
y^{-3/2}
\Pr\{Y\le y\mid A,v\}\,dy
\le
C_\xi/D.
}
\tag{9.3}
\]

Thus the source's no-near-parallel requirement is already solved at pure finite variance.

The arbitrary-finite-variance loss is **not** in the singular edge. It is entirely in the bulk quadratic angular mixing.

---

# 10. Averaged quadratic decorrelation

Because
\[
(1-x)^{-1/2}\ge1+\frac{x}{2},
\qquad
0\le x<1,
\]
P14-AVG-FV-01 implies
\[
\boxed{
\mathbb E[
\rho^2\,1_{\{D\ge3\}}
]
=
O_{\xi,\beta,\eta}(m^{-1+\eta})
}
\tag{10.1}
\]
for every fixed \(\eta>0\).

Under the stretched-log hypotheses,
\[
\boxed{
\mathbb E[
\rho^2\,1_{\{D\ge3\}}
]
=
O_{\xi,\beta}(m^{-1}).
}
\tag{10.2}
\]

This is an **averaged-over-overlap** theorem.

It does not upgrade the sharp fixed-apex conditional claim
\[
\mathbb E[\rho^2\mid A]\le C_\xi/D
\]
at arbitrary finite variance.

---

# 11. Consequence for the original probability-open-problem route

The June probability snapshot says that its fixed-apex second-moment reduction needs:

- a large useful one-normal family;
- correct one-slab asymptotics;
- an averaged pair correlation kernel;
- separate handling of \(D\le2\).

This run proves that the **random-pair correlation-average/high-correlation side** of that reduction no longer needs the sharp conditional \(C/D\) endpoint theorem.

At one fixed bounded-density finite-variance law:

\[
\boxed{
\text{ordinary pair-kernel empirical excess}=o_{\mathbb P}(1),
}
\]
and
\[
\boxed{
\text{near-parallel singular edge}=O(1/D)\text{ conditionally}.
}
\]

The remaining distinction is one-normal/local-CLT regularity.

For the bounded-density **subgaussian** route in the June snapshot, Nguyen--Vu supplies the required strong normal delocalization and the saved deterministic local-CLT module already supplies the one-/two-slab asymptotics. Therefore the correlation theorem is no longer the missing input in that source route.

For arbitrary fixed finite variance, P12's random-rounding theorem gives fixed-parameter incompressibility, enough for its staged proof, but not automatically the stronger RV-scale max-coordinate delocalization used by the old Gaussian-product-scale local-CLT reduction. Thus this run does **not** claim that every historical direct fixed-apex local-CLT proof transfers verbatim to arbitrary finite variance.

The fixed-law extremal least-singular exponent is nevertheless already proved by P12/P13 through the staged graph method.

---

# 12. Independent peer audit

## AUDIT_FOR=P12 — `P12-PAIR-GEOM-FV`

**Source:**  
`P12_smooth_iid_least_singular_2026-09-14_16-28-34.md`

**Library file id:**  
`file_000000008b80820c81fc9448b5c85374`

**Claim ID:**  
`P12-PAIR-GEOM-FV`

**Verdict:** **PROVED / PASS.**

### 12.1 High-overlap count

For fixed
\[
S,\qquad |S|=m-1,
\]
a set \(T\) with
\[
D=m-|S\cap T|
\]
has
\[
D-1
\]
elements removed from \(S\) and
\[
D-1
\]
new elements chosen from the complement of size
\[
n_0-m+1.
\]

Therefore
\[
\#T
=
\binom{m-1}{D-1}
\binom{n_0-m+1}{D-1}.
\]

For \(D=\delta m+O(1)\), Stirling gives exactly
\[
g_\beta(\delta)
=
H(\delta)
+
(\beta-1)
H\left(\frac{\delta}{\beta-1}\right).
\]

Meanwhile
\[
\log L_m
=
h(\beta)m+o(m).
\]

Because
\[
g_\beta(\delta)\to0
\quad(\delta\downarrow0)
\]
and
\[
h(\beta)>0,
\]
one can choose \(\delta_0>0\) so
\[
\sup_{0\le\delta\le\delta_0}g_\beta(\delta)
<
h(\beta)-2\kappa
\]
for some \(\kappa>0\).

Summing over at most \(m\) values of \(D\),
\[
\#\{(S,T):D<\delta_0m\}
\le
e^{-\kappa m}L_m^2
\]
after decreasing \(\kappa\).

This part is correct.

### 12.2 Low-overlap near-parallel pairs

For
\[
D\ge\delta_0m,
\]
P24-MIDEDGE-FV gives, conditional on the shared block and first private line,
\[
\Pr\{1-\rho^2\le y_*\}
\le
e^{-c_\xi D}
\le
e^{-c_\xi\delta_0m}.
\]

Thus the expected fraction of low-overlap near-parallel pairs is exponentially small.

Markov at half the exponent gives, with exponentially high probability, an exponentially small empirical fraction.

Combining the two regimes gives
\[
\boxed{
e_0\le e^{-\kappa' m}L_m^2
}
\]
with probability
\[
1-e^{-\kappa' m}
\]
after reducing \(\kappa'\).

The dependence among all pair indicators is irrelevant because only their expectation and Markov's inequality are used.

I find no hidden union bound over the exponential pair family and no illicit independence assumption.

This independently confirms `P12-PAIR-GEOM-FV`.

---

# 13. Low-dimensional and exact benchmark checks

For two independent Haar lines in \(\mathbb R^D\),
\[
Y=1-\rho^2
\sim
\operatorname{Beta}\left(\frac{D-1}{2},\frac12\right).
\]

Hence
\[
\mathbb E Y^{-1/2}
=
\frac{
\Gamma(D/2)\Gamma((D-2)/2)
}{
\Gamma((D-1)/2)^2
}.
\]

At
\[
D=3,
\]
\[
\boxed{
\mathbb E Y^{-1/2}
=
\pi/2.
}
\]

At
\[
D=4,
\]
\[
\boxed{
\mathbb E Y^{-1/2}
=
4/\pi.
}
\]

At
\[
D=2,
\]
the expectation diverges logarithmically.

This is why the source's \(D\le2\) fallback is mathematically necessary rather than a proof artifact.

The large-\(D\) benchmark is
\[
1+\Theta(1/D),
\]
so the sharp \(C/D\) conditional target has the correct order.

---

# 14. Updated failed-route graveyard

1. **Unconditional independence of overlapping null normals.**  
   Invalid. Independence appears only after conditioning on the shared block.

2. **Projected private-row coordinates are iid.**  
   Invalid.

3. **Apply iid rectangular least-singular-value theorems directly to the projected residual matrices.**  
   Invalid.

4. **Exact angular isotropy for a general non-Gaussian product law.**  
   False.

5. **Raw inverse determinant moments.**  
   Invalid even in the Gaussian benchmark.

6. **Finite variance automatically makes the one-step anisotropy debt summable.**  
   False as a consequence of the available generic moduli; finite variance permits arbitrarily slow tails.

7. **The sharp \(C/D\) conditional theorem is necessary for the original fixed-apex second moment.**  
   **REJECTED this run.**  
   The uniform \(D^{-1+\eta}\) theorem is enough after averaging over the overlap law because typical \(D\) is linear in \(m\).

8. **The averaged theorem proves the sharp D-stratified endpoint.**  
   False. Averaging can hide a subpower loss at each fixed \(D\).

9. **The averaged theorem alone transfers the old RV-local-CLT proof to every finite-variance law.**  
   False. The old local-CLT module assumes stronger directional delocalization than fixed-parameter incompressibility.

10. **High-correlation singularity remains the finite-variance obstruction.**  
    False. The singular edge is already sharp \(O(1/D)\).

---

# 15. Updated ledger

## PROVED

- `P14-R1`: exact shared-row residual reduction.
- `P14-R2`: conditional independence of private residual null lines given the apex.
- `P14-R3`:
  \[
  \mathbb E[(v\cdot w)^2\mid A]=\operatorname{tr}(M_A^2).
  \]
- `P14-COF-ISO`: exact cofactor-volume weighted second-order isotropy.
- `P14-SIZEBIAS`: size-biased exact 2-design comparison.
- `P14-WHITE`: exact complementary whitening identity.
- `P14-PARSEVAL-COUNTEREXAMPLE`.
- `P14-FULL-(2+\delta)`:
  \[
  \mathbb E[(1-\rho^2)^{-1/2}\mid D]\le1+C/D.
  \]
- `P24/P14-EDGE-FV`: sharp finite-variance singular-edge \(C/D\).
- `P24-P14-FULL-FV-SUBPOWER`:
  \[
  \mathbb E[(1-\rho^2)^{-1/2}\mid A]
  \le
  1+C_{\eta,\xi}D^{-1+\eta}.
  \]
- `P14-BULK-MOD`: summable one-step anisotropy defect implies sharp \(C/D\) bulk.
- `P14-BULK-SLOG` and `P14-FULL-SLOG`: stretched-log second-moment tails give the exact sharp theorem.
- **`P14-AVG-FV-01` — NEW:** arbitrary fixed finite variance gives ordinary-stratum overlap-averaged kernel excess
  \[
  O(m^{-1+\eta})
  \]
  for every fixed \(\eta>0\).
- **`P14-EMP-AVG-FV` — NEW:** empirical fixed-apex ordinary-pair kernel average is
  \[
  1+o_{\mathbb P}(1).
  \]
- **`P14-GOOD-AVG-FV` — NEW:** the same remains true after restriction to any \(1-o_{\mathbb P}(1)\) good family.
- **`P14-AVG-SLOG-01` — NEW:** stretched-log tails improve the averaged excess to \(O(1/m)\).
- **`P14-AVG-QUAD-FV` — NEW:** averaged quadratic decorrelation is
  \[
  O(m^{-1+\eta})
  \]
  at pure finite variance and \(O(1/m)\) in the stretched-log class.
- **`P14-AUDIT-P12-PAIR-GEOM-FV` — NEW:** PASS.

## CONDITIONAL / protocol

- The sharp arbitrary-finite-variance D-stratified theorem remains open.
- The previous new `P14-BULK-MOD/SLOG` results still need OTHER-worker audits for portfolio certification.
- P24's finite-variance edge theorem has one complete P14 audit; another OTHER audit is still required by the portfolio protocol.
- Reassembling the historical direct fixed-apex finite-variance local-CLT proof requires verifying the exact one-normal directional-delocalization hypothesis, not merely fixed-parameter incompressibility.
- The bounded-density subgaussian source route has all named correlation-side inputs; a full independent assembly audit is still appropriate.

## DISPROVED / REJECTED

- Post-projection iid replacement.
- Exact non-Gaussian angular isotropy.
- Full-pool Parseval isotropy as a probabilistic mixing substitute.
- Raw inverse determinant control.
- Naive fourth-moment global-norm splitting for the singular edge.
- Automatic \(\delta\downarrow0\) continuation of the \(2+\delta\) proof.
- “Sharp conditional \(C/D\) is necessary for the source fixed-apex correlation average.”
- “Averaged \(1+o(1)\) implies the sharp D-stratified theorem.”
- “Fixed-parameter incompressibility automatically implies the old RV-scale local CLT.”

## OPEN

1. **P14-FULL-FV**
   \[
   \mathbb E[(1-\rho^2)^{-1/2}\mid D]
   \stackrel{?}{\le}
   1+C_\xi/D.
   \]
2. **P14-BULK-FV**
   \[
   \mathbb E[\rho^2\mid A]
   \stackrel{?}{\le}
   C_\xi/D.
   \]
3. Blockwise/Hilbert-Schmidt angular mixing avoiding
   \[
   \sum_k\varepsilon_k/k.
   \]
4. Direct cofactor-volume de-biasing at arbitrary finite variance.
5. A clean complete assembly audit of the now-solved bounded-density subgaussian fixed-apex correlation route.
6. Complex analogue.
7. Second independent audits required by the ProofNet protocol.

---

# 16. Exact dependency graph after this run

### Conditional finite variance

\[
\text{finite variance + bounded density}
\]
gives
\[
\boxed{
\mathbb E[K\mid A]
\le
1+C_{\eta,\xi}D^{-1+\eta}
}
\]
and a sharp \(O(1/D)\) singular edge.

### Overlap combinatorics

\[
D<\delta_0m
\]
has exponentially small pair fraction.

Thus
\[
\boxed{
\mathbb E[D^{-1+\eta}]
=
O(m^{-1+\eta}).
}
\]

### Random-pair average

Therefore
\[
\boxed{
\mathbb E[(K-1)1_{D\ge3}]
=
O(m^{-1+\eta}).
}
\]

### Empirical fixed-apex average

Exchangeability + positivity + Markov give
\[
\boxed{
\frac1{L_m^2}
\sum_{S,T,D\ge3}(K_{S,T}-1)
=
o_{\mathbb P}(1).
}
\]

Restriction to a \(1-o_{\mathbb P}(1)\) good family preserves the result.

The sharp conditional \(C/D\) theorem is therefore no longer needed for the **averaged** fixed-apex correlation input.

---

# 17. Next theorem-sized attack

The sharp endpoint remains mathematically interesting and is now cleanly separated from the source-average need.

The highest-value next P14 theorem is still:

## P14-BULK-BLOCK-FV

Prove a blockwise second-order contraction for the random hyperplane process that controls
\[
\operatorname{tr}(M_A^2)
\]
directly rather than multiplying worst-direction operator-norm defects one dimension at a time.

A productive target is a dyadic block estimate of the form
\[
\boxed{
\mathbb E\|P_{\lfloor K/2\rfloor}q\|^4
\le
\frac14
\left(
1+\varepsilon_K^{\rm block}
\right)
}
\]
with
\[
\sum_j
\varepsilon_{2^j}^{\rm block}
<
\infty
\]
under only finite variance.

This would exploit that P14 needs Hilbert-Schmidt purity
\[
\operatorname{tr}(M_A^2),
\]
not the worst eigenvalue of \(M_A\).

The competing route remains the cofactor-size-bias theorem:
control
\[
D\operatorname{tr}(M_A^2)-1
\]
through the endogenous cofactor-volume bias without requiring negative determinant moments.

---

# 18. Bottom line

The exact sharp arbitrary-finite-variance D-stratified theorem is still open:

\[
\boxed{
\mathbb E[(1-\rho^2)^{-1/2}\mid D]
\stackrel{?}{\le}
1+\frac{C_\xi}{D}.
}
\]

But the source probability program asked for that theorem as a route to an **averaged fixed-apex second moment**.

That averaged correlation obstacle is now removed at pure finite variance:

\[
\boxed{
\mathbb E[
((1-\rho^2)^{-1/2}-1)
1_{\{D\ge3\}}
]
=
O_{\xi,\beta,\eta}(m^{-1+\eta})
}
\]
for every fixed \(\eta>0\),

and, for the actual exponentially dependent fixed-apex family,

\[
\boxed{
\text{empirical ordinary-pair kernel average}
=
1+o_{\mathbb P}(1).
}
\]

The high-correlation singular edge is already sharp \(O(1/D)\), and the high-overlap \(D\le2\) strata are exponentially sparse and remain handled separately.

Thus the remaining P14 frontier is now a **sharp conditional bulk-mixing theorem**, not the fixed-apex averaged correlation input.

