Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime model/effort telemetry or binding selector is exposed.

# P0220 — source-native invariance, the corrected finite-k balance equation, and the first generic k=3 identity

Status: **OPEN / PARTIAL under the campaign closure protocol.** This note proves a new source-native invariance theorem for the already recovered candidate stationary law and identifies a coefficient error in equation (43) of the unfinished 1993 Aldous--Diaconis notes. It does **not** claim that the open problem is closed, that the correction is novel, or that the earlier extended-kernel formula has passed an independent audit.

Source target: David Aldous, *A one-dimensional drift-jump particle process*, posted February 2018,

`https://www.stat.berkeley.edu/~aldous/Research/OP/left_Hamm.html`.

Historical source: David Aldous and Persi Diaconis, unfinished 1993 notes *Patience Sorting, Longest Increasing Subsequences and a Continuous Space Analog of the Simple Asymmetric Exclusion Process*, Section 4.1,

`https://www.stat.berkeley.edu/~aldous/Research/OP/patience.pdf`.

The maintained page still asks for a “fairly explicit” stationary distribution. In the 1993 notes, equations (40)--(42) give the finite-time patience-sorting representation and the limiting vector `(Gamma(B(1)),...,Gamma(B(k)))`; equation (43) is printed as a stationary balance equation. The derivation below shows that the drift-divergence term in (43) is missing `(k-1)p_k` for `k>=2`.

## 1. The process and its exact generator

Fix `k>=1` and write

\[
D_k=\{x=(x_1,\ldots,x_k):0<x_1<\cdots<x_k<\infty\},
\qquad x_0:=0.
\]

Between jumps every coordinate obeys

\[
\dot x_i=x_i.
\]

A unit-intensity space-time Poisson point `(y,t)` with

\[
x_{i-1}(t-)<y<x_i(t-)
\]

moves particle `i` to `y`; points to the right of `x_k` do nothing. For a smooth compactly supported test function `f`, define

\[
x^{i\leftarrow y}:=(x_1,\ldots,x_{i-1},y,x_{i+1},\ldots,x_k).
\]

The generator is therefore

\[
\boxed{
(L_k f)(x)
=
\sum_{i=1}^k x_i\partial_i f(x)
+
\sum_{i=1}^k\int_{x_{i-1}}^{x_i}
\bigl[f(x^{i\leftarrow y})-f(x)\bigr]\,dy.
}
\tag{1}
\]

Since the jump intervals partition `(0,x_k)`, their total length is `x_k`. Equivalently,

\[
(L_k f)(x)
=
\sum_{i=1}^k x_i\partial_i f(x)-x_k f(x)
+
\sum_{i=1}^k\int_{x_{i-1}}^{x_i}f(x^{i\leftarrow y})\,dy.
\tag{2}
\]

No balance equation has been used here; (1) is just the stated dynamics.

## 2. Correct adjoint and the coefficient in the source balance equation

Let `p` be a sufficiently regular density on `D_k`, with enough decay that the integrations below are justified. For the deterministic drift,

\[
-\sum_{i=1}^k\partial_i(x_i p)
=-k p-\sum_{i=1}^k x_i\partial_i p.
\tag{3}
\]

For a fixed target state `x`, a jump that lands at coordinate `x_i` can have come from any pre-jump value

\[
z\in(x_i,x_{i+1}),\qquad x_{k+1}:=\infty.
\]

Thus the jump gain density is

\[
G_i p(x)
=
\int_{x_i}^{x_{i+1}}
 p(x_1,\ldots,x_{i-1},z,x_{i+1},\ldots,x_k)\,dz.
\tag{4}
\]

The jump-loss density is `x_k p(x)`. Hence the forward adjoint is

\[
\boxed{
L_k^*p
=-k p-\sum_{i=1}^k x_i\partial_i p-x_kp
+
\sum_{i=1}^k G_i p.
}
\tag{5}
\]

Consequently every stationary smooth density satisfies

\[
\boxed{
x_kp
=-k p-\sum_{i=1}^k x_i\partial_i p
+
\sum_{i=1}^k\int_{x_i}^{x_{i+1}}
 p(x_1,\ldots,x_{i-1},z,x_{i+1},\ldots,x_k)\,dz.
}
\tag{6}
\]

This is the source-native stationary balance equation obtained directly from the stated dynamics.

### Comparison with Aldous--Diaconis equation (43)

The unfinished 1993 notes print equation (43) with `-p_k` where (6) has `-k p_k`. The two formulas agree for `k=1`. For every `k>=2`, their difference is

\[
(k-1)p_k.
\]

Therefore a nonzero density cannot satisfy both equations. In particular the known positive `k=2` stationary density from the same notes cannot satisfy the printed equation (43) if it satisfies the actual process balance equation. The notes themselves place the remark

`xxx result inconsistent -- I'll try to work backwards from the analysis in Theorem 12.`

immediately before the `k=2` calculations. I record the proximity but do **not** infer that the authors had identified this coefficient issue.

The source of the discrepancy is elementary: the divergence of the vector field `(x_1,...,x_k)` is `k`, not `1`.

## 3. Independent invariance theorem for the patience-sorting limit law

The preceding R7-04 work used the historical limiting representation

\[
\mu_k:=\mathcal L\bigl(\Gamma(B(1)),\ldots,\Gamma(B(k))\bigr),
\tag{7}
\]

where `(Gamma(n))` are the points of an independent rate-one Poisson process on space and `(B(i))` are the stabilized top-card labels of the first `k` patience-sorting piles. It also identified this law with first-row hitting times of rate-one poissonized Plancherel growth. The remaining STUCK1 obligation was to verify stationarity directly in the source dynamics, without treating the printed equation (43) or an extended Schur kernel as a premise.

### Theorem 3.1 — source-native invariance

For every finite `k`, the probability law `mu_k` in (7) is invariant for the drift-jump process with generator (1).

#### Proof

The historical construction gives, for each finite `t>0`,

\[
(X_1(t),\ldots,X_k(t))
\overset d=
\bigl(\Gamma(B(M_{e^t},1)),\ldots,
      \Gamma(B(M_{e^t},k))\bigr),
\tag{8}
\]

where `(M_s)` is a rate-one Poisson counting process, independent of the spatial Poisson points `Gamma`. Let `mu_{k,t}` denote this law.

First, `mu_{k,t}=>mu_k` as `t->infinity`. Indeed, `M_{e^t}->infinity` in probability, and for every fixed finite increasing label vector `(b_1,...,b_k)` with `b_1=1`, the probability of the event

\[
(B(n,1),\ldots,B(n,k))=(b_1,\ldots,b_k)
\]

is constant once `n>=b_k`; this is the stabilization stated in equation (41) of the notes. Therefore the finite pile-top vector converges in distribution to `(B(1),...,B(k))`. Composing with the independent spatial Poisson arrival map gives (7).

Second, let `(P_s)_{s>=0}` be the semigroup of the finite-`k` drift-jump process on `D_k`. The process is Feller. To see this, fix `s>0` and a sequence `x^{(n)}->x` in `D_k`. For all large `n`, the largest starting coordinate is bounded by some constant `C`. Jumps only move particles left, while deterministic growth multiplies positions by at most `e^s`; hence throughout `[0,s]`, every particle stays below

\[
M:=e^s C.
\]

Only Poisson points in the finite rectangle `[0,M]x[0,s]` can affect the process, and there are almost surely finitely many such points. Couple all initial states using those same points. Process them in chronological order. Between successive points the deterministic flow is continuous in the initial state. At a Poisson point `(y,t)`, the identity of the closest particle to the right is determined by finitely many strict inequalities. Almost surely `y` is not exactly equal to a just-before-event particle coordinate. Hence, for all sufficiently large `n`, the same particle is selected in the process started from `x^{(n)}` as in the process started from `x`. Induction over the finite event set yields

\[
X^{x^{(n)}}(s)\longrightarrow X^x(s)
\qquad\text{almost surely}.
\]

Thus `P_s f(x^{(n)})->P_s f(x)` for every bounded continuous `f`, proving the Feller property.

Third, the historical finite-time construction is the same time-homogeneous process, so for every `t>0` and `s>=0`,

\[
\mu_{k,t+s}=\mu_{k,t}P_s.
\tag{9}
\]

Now let `f` be bounded continuous. Feller continuity and weak convergence give

\[
\begin{aligned}
\int P_s f\,d\mu_k
&=\lim_{t\to\infty}\int P_s f\,d\mu_{k,t}\\
&=\lim_{t\to\infty}\int f\,d\mu_{k,t+s}\\
&=\int f\,d\mu_k.
\end{aligned}
\tag{10}
\]

Therefore `mu_k P_s=mu_k` for every `s>=0`. QED.

### Consequence

This proof makes the candidate law stationary **without** using equation (43), the disputed multi-time extended-kernel normalization, or uniqueness. The source also gives an almost-sure finite coupling of arbitrary finite initial configurations; that is consistent with uniqueness/attraction but is not needed in Theorem 3.1.

Combining Theorem 3.1 with the already proved RSK bridge gives the source-native stationary representation

\[
\boxed{
(X_1,\ldots,X_k)_{\rm stat}
\overset d=
(\tau_1,\ldots,\tau_k),
\qquad
\tau_j:=\inf\{t:\Lambda_1(t)\ge j\},
}
\tag{11}
\]

for rate-one poissonized Plancherel growth `Lambda(t)`.

## 4. Explicit interior density from the pile-top law

Let

\[
q_k(b_2,\ldots,b_k)
:=\Pr(B(2)=b_2,\ldots,B(k)=b_k),
\]

with

\[
1=b_1<b_2<\cdots<b_k.
\]

Conditional on this vector, the Poisson arrival indices `b_j` have joint density

\[
e^{-x_k}
\prod_{j=2}^k
\frac{(x_j-x_{j-1})^{b_j-b_{j-1}-1}}
     {(b_j-b_{j-1}-1)!}
\tag{12}
\]

on `D_k`; the `j=1` factor is one because `b_1=1`. Hence

\[
\boxed{
p_k(x_1,\ldots,x_k)
=e^{-x_k}
\sum_{1=b_1<\cdots<b_k}
q_k(b_2,\ldots,b_k)
\prod_{j=2}^k
\frac{(x_j-x_{j-1})^{b_j-b_{j-1}-1}}
     {(b_j-b_{j-1}-1)!}.
}
\tag{13}
\]

On every compact subset of `D_k` the series and its termwise derivatives are dominated by the corresponding exponential series in the positive gaps, so `p_k` is smooth in the interior. Theorem 3.1 and the generator calculation therefore imply that (13) satisfies the corrected strong balance equation (6).

For `k=2`, (13) is exactly the source series subsequently resummed in the preceding R7-04 note into the modified-Bessel density. Thus the historical two-particle density provides an immediate analytic consistency check: it satisfies (6) with coefficient `-2p_2`; if it also satisfied the printed `-p_2` equation, subtraction would force `p_2=0`, impossible because (13) is strictly positive.

## 5. B30: the first genuinely multi-coordinate source-native identity, k=3

The mandatory STUCK1 recovery asked for a generic `k=3` calculation before any generalization. Introduce the gap variables

\[
u=x_1,\qquad a=x_2-x_1,\qquad b=x_3-x_2.
\]

From (13), write

\[
p_3(x_1,x_2,x_3)=e^{-x_3}F(a,b),
\tag{14}
\]

where

\[
\boxed{
F(a,b)
=
\sum_{r,s\ge0}q_{r,s}\frac{a^r}{r!}\frac{b^s}{s!},
\qquad
q_{r,s}:=\Pr(B(2)=r+2,\ B(3)=r+s+3).
}
\tag{15}
\]

The Euler vector field transforms as

\[
\sum_{i=1}^3 x_i\partial_{x_i}
=u\partial_u+a\partial_a+b\partial_b.
\tag{16}
\]

For the three gain terms in (6), after factoring out `e^{-x_3}` one obtains

\[
\begin{aligned}
e^{x_3}G_1p_3
&=\int_0^a F(c,b)\,dc,\\
e^{x_3}G_2p_3
&=\int_0^b F(a+c,b-c)\,dc,\\
e^{x_3}G_3p_3
&=\int_b^\infty e^{-(c-b)}F(a,c)\,dc.
\end{aligned}
\tag{17}
\]

Substitution into the **corrected** `k=3` balance equation cancels the `x_3F` terms and gives the exact functional identity

\[
\boxed{
3F(a,b)+aF_a(a,b)+bF_b(a,b)
=
\int_0^a F(c,b)\,dc
+\int_0^b F(a+c,b-c)\,dc
+\int_b^\infty e^{-(c-b)}F(a,c)\,dc.
}
\tag{18}
\]

This is the first generic three-coordinate source-native stationary identity for the candidate law. It is not a boundary specialization such as `s=t` or `t=u`.

If one uses the coefficient printed in equation (43) of the historical notes, the left side of (18) becomes

\[
F+aF_a+bF_b,
\]

which differs by `2F`. Since `F(a,b)>0` for `a,b>0`, the printed equation cannot hold for this stationary law. Thus `k=3` independently exposes the same coefficient defect found from the generator.

## 6. B20: attempt to falsify the earlier multi-time Schur-kernel normalization

The previous R7-04 Fredholm artifact used the factor

\[
\Phi_{\rm old}(t,z)=e^{z-t/z}.
\tag{19}
\]

The STUCK1 diagnosis noticed a convention risk. The positive nested-partition law is safer because it can be read directly from Plancherel growth. In the standard Schur-process “plus before / minus after” bookkeeping, physical elapsed time `t` accumulates a Plancherel specialization `rho_t` on the **plus** side, while the final Plancherel factor supplies the fixed specialization `rho_1` on the **minus** side. Since

\[
H(\rho_c;z)=e^{cz},
\]

the literal physical-growth specialization has the ratio

\[
\boxed{
\Phi_{\rm grow}(t,z)=e^{t z-z^{-1}},
}
\tag{20}
\]

under that convention, not (19).

At one time, (19) and (20) both reduce after a scaling/inversion to the same poissonized-Plancherel/discrete-Bessel law with parameter `t`; this explains why all previous scalar Bessel checks could pass while failing to test the physical time orientation. At multiple times, however, swapping the accumulated plus specialization and the fixed minus specialization is a genuine orientation change. A transpose, inversion, particle-hole transform, time reversal, or determinantal gauge may still relate the two kernels, but such a relation must be proved on the actual half-line gap events; it cannot be assumed from equal one-time marginals.

Therefore the result of B20 is:

- the old factor (19) is **falsified as the literal plus-before/minus-after specialization of the forward physical Plancherel growth path**;
- this does **not** by itself prove that every Fredholm determinant written from (19) is numerically wrong, because a hidden symmetry/gauge equivalence may exist;
- the safe full joint law remains the positive nested-partition formula already derived from (11);
- the natural forward factor to audit against the exact Schur-process theorem is (20).

I do not promote a corrected double-contour kernel here because that requires carrying the exact Okounkov--Reshetikhin power convention, particle coordinates, and contour nesting through the specialization. The point of this recovery run is to remove circularity and localize the remaining convention check, not to replace one unverified contour formula with another.

## 7. What this run changes and what it does not

### Newly proved here

1. Exact finite-`k` generator (1) for the source process.
2. Correct stationary adjoint/balance equation (6), with coefficient `-k p_k`.
3. The printed historical equation (43) misses `(k-1)p_k` for `k>=2`.
4. A direct Feller/entrance-law proof that the patience-sorting limit law (7) is invariant for the actual drift-jump process.
5. The explicit all-`k` interior density series (13) and its source-native stationarity.
6. The generic `k=3` functional identity (18).
7. A precise diagnosis of why the earlier multi-time Schur factor is not the literal forward-growth specialization.

### Retained from earlier work

- the RSK/Plancherel hitting-time representation (11);
- all scalar Bessel/Toeplitz determinant marginals;
- the positive nested-partition full-joint formula and certified Poisson-tail truncation;
- the exact two-particle Bessel formulas and the exact positive `k=3` triple-survival series.

### Still not established

- a fully reconciled forward extended-Schur contour kernel with all gauge/orientation conventions proved;
- an exhaustive prior-art certificate showing that the source-specific composition is absent from the literature;
- the required independent P26 audit;
- the required distinct OTHER-track audit;
- a campaign-compliant `paper_<name>/` package.

For those reasons the honest campaign label remains **OPEN / PARTIAL**, despite the stronger source-native mathematics.

## 8. Dated literature/status check — 2026-09-19

The maintained Aldous problem page is live and still asks for a fairly explicit stationary law. The unfinished 1993 notes still display equations (40)--(43) exactly in the form used above. A bounded search on 2026-09-19 for the exact problem title together with `stationary distribution`, `balance equation`, `patience sorting`, `leftmost Hammersley`, `Schur process`, `extended Bessel`, and `Fredholm determinant` found no publication explicitly recording the coefficient correction or completing the entire source-specific chain. This is **negative search evidence only**, not proof of novelty or current openness.

Relevant prior machinery remains:

- Nica, *Decorated Young Tableaux and the Poissonized Robinson-Schensted Process* (SPA 2017 / arXiv:1404.4015): the poissonized RS trajectory is a Schur process/nonintersecting Poisson ensemble;
- Borodin--Olshanski, *Stochastic dynamics related to Plancherel measure on partitions* (2004/2006): dynamical Plancherel correlations;
- Okounkov--Reshetikhin, *Correlation function of Schur process with application to local geometry of a random 3-dimensional Young diagram* (2001/2003): general Schur-process determinantal kernel;
- classical Gessel/discrete-Bessel determinant machinery for fixed-time Plancherel marginals.

No novelty is assigned to those general tools.

## 9. Metric and next attack

The admission-frozen metric cannot move further:

`K_Bessel: infinity -> infinity` (**NO MOVEMENT**).

This is the first ordinary recovery run after STUCK1, so the ordinary unchanged count becomes `3 -> 4`; stuck recoveries remain `1`.

Methods used: **B3 / B20 / B30**.

- **B3 (prove something stronger):** proved direct invariance for the full finite-`k` candidate law, not merely another marginal identity.
- **B20 (find why the algorithm/formula fails):** localized the old extended-kernel problem to a plus/minus physical-time orientation mismatch and refused to defend it from one-time checks.
- **B30 (one scale/dimension at a time):** derived the full generic `k=3` corrected stationary identity before generalizing.

Next nonrepeating triple: **B6 / B10 / B12**.

- **B6:** deform from the solved source-native generator identity to an exact forward Schur kernel and identify the unique convention that preserves (18).
- **B10:** make the positive nested-partition full joint law into a finite explicit determinant/algorithm without relying on the disputed multi-time kernel orientation.
- **B12:** exploit stationarity to derive conserved generator identities/moments that can independently test any proposed joint formula.

The next run should prioritize a theorem-level reconciliation or source-closure package, not more scalar Bessel identities.