TASK: B17 ACCOUNT: fleet02 RUN: 2026-09-21T21:54:32.670777Z — selector-phase connected adversary and low-plaquette approximate factorization

MODEL: GPT-5.6 Sol
THINKING LEVEL: UNKNOWN; source=self_report/not_exposed; requested=maximum actually supported
THINKING USAGE: NOT_EXPOSED; provider thinking time=NOT_EXPOSED; coverage=unavailable
ELAPSED WORK: pending finish snapshot; scope=first instrumented observation to report snapshot; not pure thinking
EXECUTION: WITHOUT_VERIFIED_BRAIN
FULL FEI STATUS: OPEN / NOT PROVED
NOVELTY: NOT CLAIMED

## 0. Controls, scope, and last-three comparison

Fresh owner controls were resolved from `yspennstate/math-research-brain` main at
on FEI under `FEI-JOINT-FOUR-ACCOUNTS-2026-09-21-192650Z`, superseding the
older all-installation-only allocation for this slot. No B17/fleet02 pause or
stop was present. A later pre-write main recheck reached
`e03bdcf54679c29c8c76dc780a49d58b8e4feb5e`; comparison from the control-read
commit showed only run/status/work files changed, not protected control files.

Fresh scientific master was re-resolved at
`3d59dcacd918f1f2afb9ee912020a66aa8857e59`, together with the P03-FEI README
and current joint/continuation orders.

The last three substantive B17 mechanisms were:

1. `20260921T184622Z-self-xor-hellinger-difference`: joint spectral difference
   law and a negative Hellinger credit; scalar coordinate marginalization was
   obstructed by Boolean examples.
2. `20260921T194732Z-harmonic-riesz-curvature`: odd majority killed ordinary
   derivative-depth and positive-defect banks; harmonic Riesz rows gave the
   exact mixed bank `I-tau`.
3. `20260921T204329Z-interaction-companion-factorization`: fleet02/B13
   tensor amortization showed the global harmonic residual is FEI-hard, so the
   mechanism changed to exact physical plaquette-factorization before coding
   a connected residual.

**FULL-PROBLEM CHANGE:** none. Full FEI remains open.

**MECHANISM CHANGE:** yes. This run first attacks the newest stop-conditioned
prefix-TC bridge with an exact Boolean interaction-connected family. After it
fails, the replacement is not another global spectral remainder: it is a
physical low-cross-plaquette approximate factorization theorem, with an exact
entropy/influence transfer inequality.

## 1. Named other-account result actually consumed

The named completed cross-account result is:

`fleet03/B12/20260921T211211Z-ordered-parent-flag-nonreuse/REPORT.md`.

For the uniform-prefix edge law of a spectral sample `S`, it proves the exact
stop-conditioned identity

\[
D_{\rm seq}+I\,TC(P\mid T)
=I I(L;T)+I\sum_k I(L;Y_k\mid T)+I\,TC(P\mid L,T),
\]

and the repaired prefix ledger with remainder

\[
R_T:=I\,TC(P\mid T)-\mathbb E\log_2(K!),\qquad K=|S|.
\]

Its explicit remaining question is whether `R_T <= C I` (or a telescoping
variant) can hold for Boolean Fourier spectra. I attack exactly that bridge
below, first globally and then even after imposing the previous B17
interaction-connected-core restriction.

The compatible fleet04/B12 factorial-trigger result was also read: the
negative factorial term genuinely pays robust trigger addresses. Nothing below
drops or upper-bounds away that negative resource. The counterexample instead
makes the stop-conditioned total-correlation term quadratic while the
factorial rebate is only `O(m log m)`.

## 2. Exact Boolean selector family

For each `m>=1` use `m` disjoint 3-variable selector blocks. Block `b` has one
address bit `a_b in {0,1}` and two independent data signs
`y_{b,0}, y_{b,1} in {+1,-1}`. Define

\[
F_m(a,y)=\prod_{b=1}^m y_{b,a_b}.
\tag{2.1}
\]

This is a genuine Boolean function on `3m` uniform-cube coordinates.

Now introduce an address-only Boolean phase

\[
c_m(a)=
\begin{cases}
-1,&a_1=\cdots=a_m=0,\\
+1,&\text{otherwise},
\end{cases}
\]

and set

\[
G_m(a,y)=c_m(a)F_m(a,y).
\tag{2.2}
\]

`G_m` is the adversary used below.

## 3. PROVED: arbitrary address-only phase is invisible to the squared spectrum

This is the key selector identity.

For `t=(t_1,...,t_m) in {0,1}^m`, write

\[
Y_t(y)=\prod_{b=1}^m y_{b,t_b}.
\]

Then pointwise

\[
F_m(a,y)=\sum_t 1_{\{a=t\}}Y_t(y).
\tag{3.1}
\]

For any address character `chi_A(a)`, the Fourier coefficient attached to the
data monomial `Y_t` and address character `chi_A` equals

\[
\widehat F_m(t,A)=2^{-m}\chi_A(t).
\tag{3.2}
\]

More generally, for **every** Boolean address-only multiplier `c(a)`,

\[
\widehat{(cF_m)}(t,A)=2^{-m}c(t)\chi_A(t).
\tag{3.3}
\]

Therefore

\[
\boxed{\widehat{(cF_m)}(S)^2=\widehat F_m(S)^2
\text{ for every Fourier set }S.}
\tag{3.4}
\]

In particular `F_m` and the connected adversary `G_m` have exactly the same
squared Fourier law, not merely close laws.

The common spectral sample is especially simple:

- independently choose one of the two data coordinates in every block;
- independently include every address coordinate with probability `1/2`.

Thus exactly

\[
K=m+\operatorname{Bin}(m,1/2),\qquad
H(F_m)=H(G_m)=2m,\qquad
I(F_m)=I(G_m)=\frac{3m}{2}.
\tag{3.5}
\]

Hence both families satisfy the easy FEI ratio `H/I=4/3`. They are used only
to refute the stronger coding bridge.

## 4. PROVED: the phase-gauged family is interaction-connected

Represent output signs as `(-1)^P`. A selector block has phase

\[
P_b=u_{b,0}+a_bu_{b,0}+a_bu_{b,1}\pmod2.
\tag{4.1}
\]

Consequently the physical plaquette defect between `a_b` and either data
coordinate in its block is identically one.

The connector phase is the one-point indicator

\[
C_m(a)=\prod_{r=1}^m(1+a_r)\pmod2.
\tag{4.2}
\]

For distinct address coordinates `i,j`,

\[
\Delta_i\Delta_j C_m
=\prod_{r\ne i,j}(1+a_r),
\]

so the cross-address plaquette defect is exactly

\[
\boxed{p_{ij}(G_m)=2^{-(m-2)}=2^{2-m}>0.}
\tag{4.3}
\]

Therefore the interaction graph of `G_m` is connected: every block's two data
coordinates attach to its address, and all addresses form a clique.

This is crucial. The counterexample is not an arbitrary real-row relaxation and
not a disconnected tensor product hidden behind the word "connected". It is an
actual Boolean common potential with nonzero physical cross-block plaquettes.

## 5. REFUTED stronger lemma: even interaction-connected `R_T <= C I` is impossible

Use the uniform-prefix edge law of fleet03/B12. For `0<=t<m`, since every
spectral set has size at least `m`,

\[
\Pr(T=t)=\frac{\Pr(K>t)}{I}=\frac{2}{3m}.
\tag{5.1}
\]

Moreover, conditional on `T=t<m`, the terminal spectral sample has exactly its
original law: size-bias by `K` cancels the `1/K` probability of choosing the
prefix length `t`.

Fix a selector block. Let `X_0,X_1` indicate whether its two data coordinates
occur in the prefix. They are mutually exclusive. By symmetry each has
conditional marginal

\[
q_t=\frac t2\,\mathbb E\!\left[\frac1K\mid T=t\right].
\tag{5.2}
\]

Since `m<=K<=2m`, for

\[
\lceil m/2\rceil\le t\le\lfloor3m/4\rfloor
\]

one has `1/8<=q_t<=3/8`.

For two mutually exclusive Bernoulli variables of common marginal `q`, their
mutual information is

\[
M(q)=2h_2(q)-h_2(2q)-2q.
\tag{5.4}
\]

Its derivative is

\[
M'(q)=2\log_2\frac{1-q}{1-2q}\ge0
\quad(0\le q<1/2).
\tag{5.5}
\]

Hence throughout this interval,

\[
M(q_t)\ge c_0:=M(1/8)
=2h_2(1/8)-h_2(1/4)-1/4
=0.0258507619400599\ldots.
\tag{5.6}
\]

Total correlation dominates the sum of within-block pair mutual informations,
so `TC(P|T=t)>=m c_0`. The interval contains at least `(m-1)/4` integers.
Averaging with (5.1) gives

\[
\boxed{TC(P\mid T)\ge \frac{c_0}{6}(m-1).}
\tag{5.8}
\]

Also `K<=2m`, hence

\[
\mathbb E\log_2(K!)\le\log_2((2m)!)\le2m\log_2(2m).
\tag{5.9}
\]

Since `I=3m/2`,

\[
\boxed{
\frac{R_T(F_m)}{I(F_m)}
\ge
\frac{c_0}{6}(m-1)-\frac43\log_2(2m)
\longrightarrow+\infty.}
\tag{5.10}
\]

By the exact spectral identity (3.4),

\[
\boxed{R_T(G_m)=R_T(F_m),\qquad I(G_m)=I(F_m).}
\tag{5.11}
\]

Therefore, for every finite constant `C`, some genuine Boolean,
interaction-connected `G_m` violates `R_T(f)<=C I(f)`.

This is **not a counterexample to FEI**. Indeed `H(G_m)/I(G_m)=4/3` for every
`m`. It refutes the stronger stop-conditioned total-correlation payment lemma,
even after the natural exact interaction-connected-core repair.

The obstruction is precise: a tiny address-only Boolean phase can connect all
physical interaction components while being completely invisible to the
squared Fourier law. Exact graph connectedness is therefore too brittle a
criterion for deciding when the prefix representation's within-selector
correlations should be paid globally.

## 6. SAME-RUN replacement: low-cross-plaquette approximate factorization

The replacement uses the **magnitude** of physical cross-cut plaquettes rather
than the zero/nonzero interaction graph.

Let `A,B` partition the coordinates of an arbitrary Boolean `f`, and define

\[
Q_{A,B}(f):=\sum_{i\in A,\;j\in B}p_{ij}(f),
\tag{6.1}
\]

where

\[
p_{ij}(f)=\Pr_x[
f(x)f(x+e_i)f(x+e_j)f(x+e_i+e_j)=-1].
\]

### Theorem 6.1 — physical low-plaquette cut implies approximate multiplicative factorization

There exist Boolean functions `g(x_A)` and `h(x_B)` such that

\[
\boxed{\Pr[f(x_A,x_B)\ne g(x_A)h(x_B)]\le \frac14Q_{A,B}(f).}
\tag{6.2}
\]

#### Proof

Write `f=(-1)^P`. Let `u` be a uniform displacement supported on `A`, and `v`
a uniform displacement supported on `B`. Define the random rectangle defect

\[
\rho_{A,B}
=\Pr_{x,u,v}[
f(x)f(x+u)f(x+v)f(x+u+v)=-1].
\tag{6.3}
\]

Order the active coordinates of `u` and `v`. Repeated discrete telescoping
expresses the rectangle second difference `Delta_u Delta_v P(x)` as an XOR of
one shifted elementary mixed second difference `Delta_i Delta_j P` for every
active cross pair `(i,j)`. The indicator of an XOR being one is at most the sum
of the indicators of its summands. Every shifted base point remains uniform,
and a fixed pair `(i,j)` is simultaneously active with probability `1/4`.
Therefore

\[
\rho_{A,B}\le\frac14\sum_{i\in A,j\in B}p_{ij}
=\frac14Q_{A,B}.
\tag{6.4}
\]

Now choose independent uniform anchors `(a_0,b_0)` and define

\[
q_{a_0,b_0}(a,b)
=f(a,b_0)f(a_0,b)f(a_0,b_0).
\tag{6.5}
\]

This factors as `g(a)h(b)`. Its disagreement with `f(a,b)` is exactly the
rectangle defect with corners `(a,b),(a,b_0),(a_0,b),(a_0,b_0)`. Averaging the
disagreement probability over the anchors gives exactly `rho_{A,B}`. Hence
some anchors achieve error at most `rho_{A,B}`, and (6.2) follows. QED.

### Corollary 6.2 — exact FEI induction transfer across a cheap physical cut

Assume `Q:=Q_{A,B}(f)<=1/4`, and let `q=gh` be the product from Theorem 6.1.
If `epsilon=Pr(f!=q)`, then Parseval and Cauchy--Schwarz give

\[
TV(\widehat f^2,\widehat q^2)
\le \|\widehat f-\widehat q\|_2
=\|f-q\|_2
=2\sqrt\epsilon
\le\sqrt Q.
\tag{6.6}
\]

Consequently the standard finite-alphabet entropy continuity bound gives

\[
H(f)\le H(q)+h_2(\sqrt Q)+n\sqrt Q.
\tag{6.7}
\]

Because `q` is a product on disjoint coordinate sets,

\[
H(q)=H(g)+H(h),\qquad I(q)=I(g)+I(h),
\tag{6.8}
\]

and bounded-observable coupling gives

\[
|I(f)-I(q)|\le n\sqrt Q.
\tag{6.9}
\]

Therefore if the target FEI inequality with constant `C` is already known for
the two lower-dimensional factors,

\[
\boxed{
H(f)\le C I(f)+(C+1)n\sqrt Q+h_2(\sqrt Q).}
\tag{6.10}
\]

This is an exact source-admissible induction transfer, not a non-Boolean
relaxation.

## 7. Why the replacement resolves the new adversary's precise failure

Cut `G_m` between `k` whole selector blocks and the remaining `m-k` blocks.
All cross-block plaquettes vanish except address-address plaquettes from the
one-point connector. From (4.3),

\[
\boxed{Q_{A,B}(G_m)=k(m-k)2^{2-m}.}
\tag{7.1}
\]

Although the interaction graph is connected for every finite `m`, a balanced
cut has exponentially small total physical cross weight. Theorem 6.1 therefore
recovers an approximate product:

\[
\Pr(G_m\ne gh)\le k(m-k)2^{-m}.
\tag{7.2}
\]

For comparison, the obvious exact tensor product `F_m` itself differs from
`G_m` on only `2^{-m}` of inputs.

The entropy/influence induction penalty is controlled by

\[
n\sqrt Q
=3m\sqrt{k(m-k)2^{2-m}},
\tag{7.3}
\]

which tends to zero for balanced `k~m/2`. Thus the phase connector that defeats
**exact** component factorization is automatically recognized as a cheap
physical cut by the new mechanism.

## 8. New remaining universal implication

The exact zero/nonzero interaction graph should no longer be used as the
factor-first stopping criterion.

A concrete replacement programme is to recursively split across physical cuts
with small `Q_{A,B}`, charging the explicit penalty
`(C+1)n sqrt(Q)+h_2(sqrt(Q))` from (6.10), and stop only on
**plaquette-expander cores** for which every nontrivial cut has quantitatively
large cross weight.

The remaining universal obligation is now an amortization/core dichotomy:

\[
\boxed{
\text{pay the sum of low-cut penalties over an adaptive factorization tree by }
O(I(f)),
\text{ or prove an }O(I)\text{ entropy code on the terminal
plaquette-expander cores.}}
\tag{8.1}
\]

This route is materially different from the killed strict-superset receiver
flow, global phase/rank/l1 budgets, raw derivative-depth payment, global
harmonic-Riesz residual payment, and global/connected stop-conditioned
TC payment.

## 9. Decisive checks

`check_stop_conditioned_connected_adversary.py` performs:

1. exact truth-table checks for `F_m,G_m`, `m=1..4`;
2. exact balance and every-coordinate influence `1/2`;
3. exact equality of the complete squared spectra of `F_m,G_m`;
4. exact connectedness and cross-address plaquette formula `p_ij=2^{2-m}`;
5. exact prefix-law construction for `m=1..3`;
6. exhaustive verification of Theorem 6.1 for all `256` Boolean functions on
   three variables and the three unordered nontrivial coordinate cuts (`768`
   cut checks);
7. formula diagnostics for the all-dimensional lower bound, which is already
   positive at `m=5000` and diverges thereafter.

No finite enumeration is used as the proof of the universal statements.

Checker SHA-256:
`c6b920b63d99f299aee7006ecc8107b92a6d132fcc782e2078bf5ad1fa66ec76`

Output SHA-256:
`6a26ea53a0bd3ca0f25f4a3535b2a8a12020598b2257bd5fe38a9822b5df50fb`

## 10. Literature applicability check

A fresh primary-literature search this run checked O'Donnell--Tan (2013)
composition, Hod (2017) recursive lower bounds/Lipschitz behavior,
González--MacManus--Pereyra (May 29, 2026) restriction/stopping results, and
Potapov (Sep 18, 2026) plateaued/partially-bent classes. Those are relevant
prior mechanisms or structured-class results; none supplies a universal FEI
proof in the material checked here. No novelty claim is made for generic
continuity or for Theorem 6.1; search absence is not a novelty certificate.

## 11. Before / after

Before this run:
- global harmonic-Riesz residual payment was already identified as FEI-hard;
- exact plaquette connected components were the replacement factor-first
  mechanism;
- fleet03/B12 had repaired an unconditional prefix-TC obstruction by
  conditioning on prefix length `T`, leaving `R_T` as a plausible residual.

After this run:
- exact Boolean `G_m` is physically interaction-connected yet has exactly the
  same squared spectrum as a disjoint tensor of selector blocks;
- `R_T(G_m)/I(G_m)->infinity`, so both global and interaction-connected
  `R_T<=CI` are false for every finite `C`;
- low cross-plaquette weight, rather than exact connectedness, now gives a
  proved approximate multiplicative factorization and an explicit FEI
  induction-transfer penalty.

Full FEI remains OPEN / NOT PROVED.
