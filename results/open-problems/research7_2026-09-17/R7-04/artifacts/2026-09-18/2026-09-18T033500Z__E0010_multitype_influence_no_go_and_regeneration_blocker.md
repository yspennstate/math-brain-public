Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; GPT-6 / maximum reasoning was requested, but no authenticated runtime reasoning-effort telemetry or binding model/effort selector is exposed.

# E0010 — multitype influence contraction, an all-history no-go theorem, and the positive-phase regeneration blocker

Target: Rick Durrett, *Coexistence in stochastic spatial models*, *Annals of Applied Probability* 19 (2009), 477–496, arXiv:0906.2293, Problem 4. For fixed `beta>4.5`, prove that sufficiently fast stirring gives a unique positive/nontrivial stationary phase in the source convention.

Status of this note: **PARTIAL / source OPEN**. It executes methods **B3 / B15 / B20** selected by the preceding R7-04 report. It does not claim source uniqueness. The fixed source metric remains `Q_SR(beta,epsilon)` and is unchanged.

## 1. Recovered cumulative setup

For an ordered basic coupling `eta<=xi`, use the three colors

\[
A_x=\eta_x,\qquad D_x=\xi_x-\eta_x,\qquad C_x=1-\xi_x.
\]

The source birth rule at a vacant target samples two distinct sites among a finite birth neighborhood of size `n`; with

\[
r_n(k)=\frac{k(k-1)}{n(n-1)},
\]

the preceding R7-04 run proved the exact coupled reaction identity

\[
R D_x
=-D_x-\beta D_xr_n(K_A(x))
+\beta C_x\{r_n(K_A(x)+K_D(x))-r_n(K_A(x))\}.
\tag{1.1}
\]

It also proved, for every translation-invariant stationary ordered coupling with discrepancy density `q=E D_0>0`,

\[
\mathbb E^D[g_{\beta,n}(K_A(0))]\ge0,
\tag{1.2}
\]

where `E^D` is discrepancy-Palm expectation and

\[
g_{\beta,n}(k)
=-1-\beta\frac{k(k-1)}{n(n-1)}+2\beta\left(1-\frac{k}{n}\right).
\tag{1.3}
\]

The same run proved a scalar forward-influence criterion: a history-uniform one-step continuation bound with total path mass `<1` would force the stationary discrepancy field to vanish. The missing source bridge was to obtain such contraction from the fast-stirring mature-block construction without paying the forbidden terminal-Palm factor `1/Q`.

This note first strengthens the scalar criterion, then shows that the most obvious way of applying the strengthening is impossible for structural reasons.

## 2. B3 — a finite-type spectral-radius influence theorem

The scalar path-counting criterion loses information when some coarse environments contract discrepancies and others may temporarily amplify them. The correct algebraic object is a nonnegative transfer matrix.

### Theorem 2.1 (finite-type stationary influence contraction)

Let `V` be any countable coarse spatial set and let the discrepancy mechanism have types `1,...,m`. For each type `i`, let

\[
q_i(v)\ge0,\qquad Q_i:=\sup_{v\in V}q_i(v)<\infty.
\]

Assume that one coarse time slab admits a deterministic nonnegative influence kernel

\[
k_{ji}(u,v)\ge0
\]

such that every stationary law in the class under consideration satisfies

\[
q_j(v)
\le
\sum_{i=1}^m\sum_{u\in V} k_{ji}(u,v)q_i(u)
\qquad(j=1,\ldots,m),
\tag{2.1}
\]

and there is a finite nonnegative matrix `M=(M_{ji})` with

\[
\sup_{v\in V}\sum_{u\in V} k_{ji}(u,v)\le M_{ji}.
\tag{2.2}
\]

If

\[
\boxed{\rho(M)<1,}
\tag{2.3}
\]

then every `q_i(v)` is zero.

#### Proof

Taking the supremum over `v` in (2.1) and using (2.2),

\[
Q_j\le\sum_{i=1}^m M_{ji}Q_i.
\]

Thus, with `Q=(Q_1,...,Q_m)^T`,

\[
0\le Q\le MQ.
\tag{2.4}
\]

Iteration preserves coordinatewise order because `M` is nonnegative:

\[
0\le Q\le M^rQ
\qquad(r\ge1).
\]

Since `rho(M)<1`, `M^r\to0` in every matrix norm. Hence `Q=0`. Therefore every `q_i(v)=0`. QED.

### How a graphical proof supplies (2.1)

It is enough that, after exposing the configuration at the beginning of a slab, fresh graphical marks admit a pathwise or conditional union bound in which an incoming type-`i` discrepancy at `u` contributes to a terminal type-`j` discrepancy at `v` with probability at most the deterministic number `k_{ji}(u,v)`, uniformly over the allowed incoming histories. Independence between different paths is unnecessary. This is exactly the dependence-robust feature sought in the previous scalar criterion.

### Two types

For a proposed `H/L` decomposition (mature/high-common-one versus low/common-one-poor), write

\[
M=
\begin{pmatrix}
a&b\\ c&d
\end{pmatrix}.
\]

The criterion is explicitly

\[
\boxed{
\frac{a+d+\sqrt{(a-d)^2+4bc}}{2}<1.
}
\tag{2.5}
\]

Thus it is not necessary that the low type itself contract in one step. A superunit entry can in principle be tolerated if transitions through the contracting type make the full spectral radius subcritical.

This is a strict strengthening of the preceding scalar `Br<1` criterion.

## 3. B3 strengthening of the local Palm obstruction: an exact mean threshold

Equation (1.2) gives more than a positive probability of low-common-one neighborhoods. The polynomial `g_{beta,n}` is strictly decreasing and concave on the real interval `[0,n]`:

\[
g''_{\beta,n}(k)=-\frac{2\beta}{n(n-1)}<0.
\]

Therefore Jensen gives

\[
g_{\beta,n}(\mathbb E^D K_A)
\ge
\mathbb E^D g_{\beta,n}(K_A)
\ge0.
\tag{3.1}
\]

Let `k_*(beta,n)` be the unique nonnegative real root of `g_{beta,n}`. Solving the quadratic gives

\[
\boxed{
k_*(\beta,n)
=
\frac{-(2n-3)+
\sqrt{(2n-3)^2+4n(n-1)(2-1/\beta)}}{2}.
}
\tag{3.2}
\]

Since `g` is decreasing, (3.1) implies the exact bound

\[
\boxed{
\mathbb E^D K_A(0)\le k_*(\beta,n).
}
\tag{3.3}
\]

In density units,

\[
\frac{k_*(\beta,n)}{n}
\longrightarrow
\sqrt{3-1/\beta}-1
=:a_\dagger(\beta)
\qquad(n\to\infty).
\tag{3.4}
\]

The previous run identified the same limiting threshold and proved that the stable mean-field equilibrium `rho_+(beta)` satisfies `rho_+>a_dagger` for every `beta>9/2`. Equation (3.3) is the finite-neighborhood version: in any translation-invariant persistent-discrepancy coupling, a typical discrepancy must see a common-one neighborhood whose **Palm mean itself** lies on the low side of the exact reaction threshold.

This strengthens the earlier positive-mass obstruction but still does not remove the source's translation-invariance/Palm bridge.

## 4. B15 — deliberately break the symmetry: the all-history contraction route is impossible

The previous report proposed making the influence estimate uniform over every incoming ordered history. That quantifier is too strong for the source.

### Proposition 4.1 (all-history no-go)

Assume `beta` and `epsilon` are in a regime where the sexual-reproduction process has a nontrivial upper invariant law `bar nu`. Then no influence criterion of Theorem 2.1 with `rho(M)<1` can be valid uniformly over **all** stationary ordered couplings of the graphical dynamics.

#### Proof

Take the lower process identically zero,

\[
\eta_t\equiv\mathbf0,
\]

and take the upper process stationary with law `bar nu`. The lower process stays zero under deaths, births and stirring. Under the basic graphical coupling,

\[
D_x(t)=\xi_x(t).
\]

This is a stationary ordered coupling with strictly positive discrepancy density because `bar nu` is nontrivial. If an all-history subcritical matrix criterion applied to this coupling, Theorem 2.1 would force every discrepancy intensity to be zero, contradicting nontriviality of `bar nu`. QED.

### Consequence

Any successful E0010 proof must use the **positive-phase assumption on the lower stationary law** `mu({0-bar})=0`. It cannot be a purely local graphical theorem that contracts every ordered discrepancy, because the zero/upper coupling is an exact stationary counterexample to that stronger assertion.

This also clarifies the low-type row of the proposed `H/L` matrix. In an all-discrepancy region with no `A` particles, the upper discrepancy field evolves as the source process itself. A universally subcritical `L` mechanism is therefore impossible in the supercritical regime. The only plausible route is one in which a discrepancy ancestry generated by a positive lower phase is forced often enough to encounter lower-phase regeneration.

## 5. B15 second obstruction: approximate harmonicity alone permits mesoscopic islands

Earlier R7-04 work proved that normalized discrepancy profiles are `O(epsilon^2)`-approximately harmonic under stirring. That estimate is useful but cannot by itself rule out a localized Palm island.

Let

\[
H(s)=\frac1{1+s^2},
\qquad
h_\varepsilon(x)=H(\varepsilon x_1),
\qquad x\in\mathbb Z^d.
\]

Then `0<h_epsilon<=1` and `h_epsilon(0)=1`. Since `H''` is bounded, the exact second-difference representation

\[
H(s+h)-2H(s)+H(s-h)
=
\int_{-h}^{h}(h-|r|)H''(s+r)\,dr
\]

gives

\[
\boxed{
\|\Delta h_\varepsilon\|_\infty
\le \|H''\|_\infty\varepsilon^2.
}
\tag{5.1}
\]

For each fixed `epsilon>0`, however, the Cesaro average of `h_epsilon` over growing boxes is zero, while its value at the origin remains one. Indeed the one-dimensional average is bounded by a constant times `(epsilon R)^{-1}` for a box of radius `R`.

Thus the pair of facts

- relative `O(epsilon^2)` approximate harmonicity, and
- vanishing large-scale spatial average,

still allows an order-one plateau on a mesoscopic scale of order `epsilon^{-1}`. The source proof must use the reaction/regeneration structure, not only the stirring elliptic estimate.

## 6. B20 — run the obvious ancestry algorithm backward and identify exactly where it fails

A discrepancy in the basic coupling has three relevant graphical events.

1. **Stirring:** the discrepancy is transported.
2. **Death or lower catch-up:** an existing discrepancy can be killed. In particular, when the lower configuration has two suitable `A` parents, a lower birth at a `D` target changes the target from `D` to `A` and destroys the discrepancy.
3. **Upper-only birth:** a discrepancy can be created at a `C` target only when the upper process has a legal occupied parent pair that is not simultaneously an `A,A` pair for the lower process. Therefore at least one parent carries `D`. Backward in time, every newly created discrepancy has at least one discrepancy ancestor.

This gives a natural constructive algorithm: trace a terminal discrepancy backward through stirring and through one of its discrepancy parents at each upper-only birth, and attempt to stop the lineage whenever it enters a mature lower-phase block where the `A` density is on the contracting side of the threshold.

The source block construction supplies high ordinary probability of mature high-density descendants once a lower-phase seed is present. Earlier R7-04 work also proved that every positive stationary law assigns positive probability to every finite all-one seed. The tempting conclusion would be that the backward discrepancy lineage must encounter mature blocks at a uniform positive rate.

That conclusion does not follow.

### Exact algorithmic failure

For each fixed positive stationary law `mu` and each fixed finite seed `F`, nucleation gives only

\[
\mu(\eta\equiv1\text{ on }F)>0.
\]

It gives no source-uniform lower bound over all positive stationary laws. More importantly, selecting a terminal discrepancy changes the environment to the discrepancy-Palm law. An ordinary bad-block estimate `P(B)<=delta` still yields only

\[
P^D(B)=\frac{P(D_0=1,B)}{P(D_0=1)}
\le\frac{\delta}{Q},
\tag{6.1}
\]

which is useless precisely when the uniqueness gap `Q` is small.

Proposition 4.1 shows that replacing (6.1) by a worst-history estimate cannot work either: the all-zero lower phase is an exact admissible graphical history for the stronger theorem and supports persistent discrepancies.

Therefore the missing lemma is neither ordinary block success nor all-history block success.

## 7. The surviving source-specific lemma

A sufficient bridge must be **phase-qualified**. One usable formulation is:

> **POSITIVE-PHASE PALM REGENERATION.** For each fixed `beta>4.5`, for all sufficiently small `epsilon`, construct finitely many ancestry/block types and a deterministic nonnegative transfer matrix `M_{beta,epsilon}` such that every stationary ordered coupling `(eta,xi)` with lower marginal `mu({0-bar})=0` satisfies the one-slab influence inequality (2.1)-(2.2), with the kernel allowed to use the fact that the lower marginal is in the positive phase, and
> \[
> \rho(M_{\beta,\varepsilon})<1.
> \]

The phrase “allowed to use the positive phase” is essential. The estimate need not, and by Proposition 4.1 cannot, hold for the coupling `(0-bar,bar nu)`.

A two-type `H/L` implementation would combine:

- the exact high-common-one reaction contraction already proved by R7-04;
- the new Palm mean restriction (3.3), which says a persistent discrepancy must preferentially occupy the low side;
- a source-specific regeneration statement showing that a discrepancy ancestry issued from a **positive** lower stationary phase cannot remain in `L` often enough for the two-type spectral radius to reach one.

At present the third bullet is unproved. It is the exact source-level blocker.

## 8. Why the sixth run still does not move `Q_SR`

Theorem 2.1 is conditional on a subcritical influence matrix. Proposition 4.1 proves that the naive all-history version of that matrix estimate is impossible. Equations (3.2)-(3.3) sharpen the Palm geometry, but only under translation invariance. The positive-phase Palm-regeneration lemma remains missing.

Therefore

`Q_SR(beta,epsilon): UNKNOWN/UNMEASURED -> UNKNOWN/UNMEASURED`.

This is the sixth ordinary unchanged CLOSABLE research run in the recovered R7-04 accounting. Under the owner protocol E0010 must now receive an immutable handoff and be retired from this slot's active research rather than receiving a seventh unchanged attack.

## 9. Dated source/literature refresh — 2026-09-18

The primary source remains Durrett 2009, arXiv:0906.2293, whose Problem 4 explicitly asks for the uniqueness theorem above after recalling the fast-stirring survival result. A bounded exact-phrase/model-specific search on 2026-09-18 did not recover a later theorem resolving this exact Problem 4.

A later Durrett paper with Xiangying Huang, *Motion by mean curvature in interacting particle systems* (PTRF 181 (2021), arXiv:2006.03090), describes its method as opening the possibility of proving a discontinuous phase transition for the fast-stirred sexual-reproduction model; it does not state the Problem-4 uniqueness conclusion. Cooperative-branching work such as Sturm--Swart (2015) supplies useful structural analogies but not this source theorem.

These bounded search results are negative evidence only. They are not a global openness or novelty certificate.
