Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 at maximum. NO MOVEMENT on `BLANC-RENAUDIE-2026-MEANFIELD-7-10`: `M_A=0 -> 0`; stagnation count remains UNKNOWN. Methods used: #6, #13, #28.**

# R09 — Blanc-Renaudie mean-field `d=7,8,9,10`: an h-free direct-bridge certificate for the mixing bottleneck

Run date: 2026-09-18 UTC  
Repository / branch: private `yspennstate/math-open-problems` / `master`  
Lane: **CLOSABLE OUTSIDE**

## 1. Runtime/control truth and continuity

The prompt requests GPT-6 with maximum reasoning. This invocation actually identifies as **GPT-5.6 Sol**. No authenticated reasoning-effort telemetry is exposed to this worker, so the reasoning level is **UNVERIFIED**. I do not claim GPT-6, maximum reasoning, or an hour-long execution guarantee.

The exposed scheduled-task control surface still has no bindable model-family selector and no bindable reasoning-effort selector. It exposes task text/schedule/enablement controls, not persistent model/effort fields or authenticated per-run routing telemetry. GPT-6/maximum therefore remains prompt text only. The repository continuity also preserves the correction that P26's historical `You cannot modify this task` response was later followed by a successful P26 update from another authorized context; that old denial is not evidence that P26 is globally immutable. The same continuity says R-series edits were denied from that P/C context. The lawful remedy for an actually denied task is an owning/authorized context, authorized ownership/admin transfer, or platform support — not duplication or a permission bypass. I made no scheduler change.

Before research I recovered the current campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, the exclusive R09 claim `operations/claims/BLANC-RENAUDIE-2026-MEANFIELD-7-10.md`, the newest complete R09 report `runs/R09/20260918T1833Z_blanc_shift_tv_fourier_certificate_f3c91a.md`, the related but distinct C0064 intake/attempt evidence, and the newest neighboring admission report that explicitly recognizes the Blanc-Renaudie source as already R09-owned. No conflicting owner was found.

The predecessor's exact state is preserved: Tang Question 4.11, G0013, and the Chen-Wang Gaussian-subuniformity successor remain retired/frozen under their existing R09 handoffs. C0064 remains a distinct older source statement (the critical Fourier infrared bound in nearest-neighbor `d>6`), not silently identified with Blanc-Renaudie's x-space asymptotic.

A fresh dated public search on 2026-09-18 recovered Arthur Blanc-Renaudie's *Markovian renormalisation for percolation in high-dimension: Semi-decidability of mean field behavior*, arXiv:2609.20764, submitted 2026-09-17 and updated/displayed on 2026-09-18. No later source-matching resolution of nearest-neighbor `d=7,8,9,10` surfaced in the bounded search. This is bounded negative evidence, not a worldwide novelty certificate. The source still records nearest-neighbor `d>=11` as known and `7<=d<=10` as the unresolved numerical-proof regime.

The frozen source metric is

\[
M_A:=\#\{d\in\{7,8,9,10\}:\text{a complete rigorous certificate of Blanc-Renaudie Theorem 1.1(a) has been obtained}\}.
\]

No dimension is certified here:

\[
\boxed{M_A:0\longrightarrow0.}
\]

The stagnation count is kept **UNKNOWN**; I do not reconstruct it from incomplete shared-root history.

This run attacks the remaining **uniform-mixing** bottleneck from Theorem 3.14. The previous R09 run already reduced the high-frequency Proposition 3.25 to a finite matching/vertex-cover certificate, and the run before that reduced the Perron lower bound `lambda_p` to a finite exact certificate. The new goal is to avoid the expensive local-modification constants in the source's Section 3.4 by replacing them with a directly checkable bridge-overlap condition.

---

## 2. Source setup used below

Let `S = \vec C^*` be the live pointed-cluster state space. Write

\[
\pi(B):=\mathbb P_p^\otimes(\vec A=B)=\frac{\mu_p(B)}{\Omega\chi(p)},
\]

and write

\[
R(A,B):=\mathbf 1_{(A,B)\notin C_{\rm cut}}.
\]

The killed operator is

\[
(Tf)(A)=\sum_{B\in S}\pi(B)R(A,B)f(B).
\tag{2.1}
\]

The source constructs a positive Perron eigenfunction `h` and maximal eigenvalue `lambda` satisfying

\[
Th=\lambda h,
\qquad 0<\lambda\le1,
\tag{2.2}
\]

and its Doob transform has transition kernel

\[
P(A,B)=\frac{\pi(B)R(A,B)h(B)}{\lambda h(A)}.
\tag{2.3}
\]

The source's Lemma 3.19 gives, if `H=||h||_infty` and `m=E_pi h`,

\[
\lambda m\ge \lambda^2 H,
\qquad\text{hence}\qquad
m\ge\lambda H.
\tag{2.4}
\]

Theorem 3.14 seeks exponential mixing

\[
\sum_B|P^k(A,B)-v(B)|\le c^k\chi(p),
\qquad c<1,
\tag{2.5}
\]

uniformly in the initial live pointed cluster `A`, once `(C)` holds and `chi(p)` is large enough. The source obtains this through Proposition 3.16, Corollary 3.17, Lemma 3.18, and then the weighted coupling argument in Lemmas 3.19--3.22 and Proposition 3.23.

The key observation of this run is that the **later weighted-coupling algebra does not intrinsically need the local modifications**. It only needs an h-free three-step bridge-overlap inequality and a small exceptional set. Those can, in principle, be certified directly by finite cluster enumeration plus a rigorous tail bound.

---

## 3. Method #6 — DEFORM TO A SOLVABLE POINT: the Doob row is an exact conditional law of one common measure

The solvable endpoint is the no-cut kernel `R\equiv1`, for which the transformed chain is i.i.d. in one step. Rather than perturbing the eigenfunction, we can keep the exact cut relation and rewrite every transformed row as a conditioning of a *single common probability measure*.

Define the h-tilted base law

\[
q_h(B):=\frac{\pi(B)h(B)}{m},
\qquad m=\sum_B\pi(B)h(B),
\tag{3.1}
\]

and, for a state `A`, let

\[
N(A):=\{B:R(A,B)=1\}.
\]

### Proposition 3.1 — exact conditional-measure representation

For every live state `A`,

\[
\boxed{
P(A,\cdot)=q_h(\,\cdot\mid N(A)).
}
\tag{3.2}
\]

#### Proof

By the Perron equation,

\[
q_h(N(A))
=\frac1m\sum_B\pi(B)R(A,B)h(B)
=\frac{\lambda h(A)}m.
\tag{3.3}
\]

Therefore

\[
q_h(B\mid N(A))
=\frac{\pi(B)h(B)R(A,B)/m}{\lambda h(A)/m}
=\frac{\pi(B)R(A,B)h(B)}{\lambda h(A)}
=P(A,B).
\]

This is exact. `square`

This turns the Doob-chain geometry into a family of conditionings of one measure `q_h`. In the no-cut limit every `N(A)=S`, so all rows are exactly `q_h` and mixing occurs in one step.

Let the **base cut mass** of a row be

\[
c(A):=\pi(N(A)^c).
\tag{3.4}
\]

Since `h<=H` and `m>=lambda H`, (2.4) gives

\[
q_h(N(A)^c)
\le\frac{H\pi(N(A)^c)}m
\le\frac{c(A)}\lambda.
\tag{3.5}
\]

For two states `A,A'`, the overlap of the two conditional laws has the exact form

\[
\sum_B\min(P(A,B),P(A',B))
=\frac{q_h(N(A)\cap N(A'))}{\max(q_h(N(A)),q_h(N(A')))}.
\tag{3.6}
\]

Hence, using (3.5),

\[
\boxed{
d_{\rm TV}(P(A,\cdot),P(A',\cdot))
\le \frac{c(A)+c(A')}\lambda.
}
\tag{3.7}
\]

In particular, on

\[
G_\delta:=\{A:c(A)\le\delta\},
\]

we have

\[
\boxed{
\sup_{A,A'\in G_\delta}
d_{\rm TV}(P(A,\cdot),P(A',\cdot))
\le \frac{2\delta}{\lambda}.
}
\tag{3.8}
\]

Thus any directly certified `delta<lambda/2` gives a strict one-step Dobrushin contraction on that typical set.

There is also a clean exceptional-mass estimate. If

\[
\varepsilon:=\mathbb E_\pi[c(A)]=\mathbb P_{\pi\otimes\pi}(R(A,B)=0),
\]

then Markov's inequality and (2.4) give

\[
\pi(G_\delta^c)\le\varepsilon/\delta,
\qquad
q_h(G_\delta^c)
\le\frac{\varepsilon}{\lambda\delta}.
\tag{3.9}
\]

### What this route does and does not solve

The identities (3.2)--(3.9) are useful because they remove all explicit eigenfunction ratios from local row comparisons. However, they do **not** by themselves prove Theorem 3.14. The source's Proposition 3.8 proves a small average cut probability for the **modified** relation `C_cut^r`, not a sufficiently small uniform or average cut probability for the actual `C_cut` entering (2.3). Transferring the `C_cut^r` estimate to (3.7) without proof would be invalid.

So method #6 succeeds structurally but exposes the precise missing number: a source-valid small-cut or bridge-overlap statistic for the **actual** killed kernel.

---

## 4. Method #13 — FIND WHAT ONLY INCREASES: projective contraction is invariant under the unknown h-transform

The second route treats the unknown Perron eigenfunction as a diagonal gauge that disappears from cross-ratios.

For every `n>=1`,

\[
P^n=\lambda^{-n}D_h^{-1}T^nD_h,
\tag{4.1}
\]

where `D_h` is diagonal multiplication by `h`. Therefore whenever the four entries are positive,

\[
\boxed{
\frac{P^n(A,B)P^n(A',B')}{P^n(A,B')P^n(A',B)}
=
\frac{T^n(A,B)T^n(A',B')}{T^n(A,B')T^n(A',B)}.
}
\tag{4.2}
\]

So the Hilbert projective diameter

\[
\Delta_n
:=
\log\sup_{A,A',B,B'}
\frac{P^n(A,B)P^n(A',B')}{P^n(A,B')P^n(A',B)}
\tag{4.3}
\]

is exactly the corresponding projective diameter of the raw killed kernel `T^n`. No approximation of `h` is required.

For a finite positive kernel, the classical Birkhoff--Hopf theorem gives projective contraction factor

\[
\boxed{
\tau_n\le\tanh(\Delta_n/4)<1.
}
\tag{4.4}
\]

The contraction coefficients are submultiplicative under composition. Thus once a finite truncation has a power whose raw entries are all positive, one can compute the worst cross-ratio exactly from rational entries and obtain a rigorous projective contraction certificate for the corresponding finite Doob chain **without ever solving the Perron eigenvector**.

This is a useful monovariant: the raw positive-kernel projective diameter controls the transformed chain, and diagonal h-reweighting cannot make it worse because it cancels identically in (4.2).

This mechanism is classical Perron--Frobenius/Birkhoff theory; I make no novelty claim for it. A bounded literature search recovered modern treatments of Dobrushin/Hilbert-projective contraction, including Gaubert--Qu's work on Dobrushin coefficients on cones, and quasi-stationary/Doob-transform mixing criteria. The source-specific point is that Blanc-Renaudie's unknown `h_p` is **not** an obstacle to a finite cross-ratio calculation.

### Why #13 is not yet a source certificate

Zeros remain the obstruction on the infinite state space. A finite truncation can have finite `Delta_n` while the full chain still has mass outside the truncation, and normalizing a raw killed row can amplify a tail when `h(A)` is small. The source's universal lower bound

\[
\inf_A h(A)/\|h\|_\infty
\ge \frac{(1-p)^\Omega}{\Omega\chi(p)}
\]

only gives a tail-completion loss of order `chi(p)`. That is compatible with the prefactor in Theorem 3.14, but it must be combined with a **constant contraction on a high-mass core**. This points directly to method #28 below.

---

## 5. Method #28 — REPLACE “FOR ALL” WITH “FOR TYPICAL”: a direct h-free bridge criterion that substitutes for the local-modification part of Section 3.4

This is the main result of the run.

Define the one-step incoming/outgoing killed masses exactly as in the source:

\[
\nu^\uparrow(A)=\pi(A)\sum_B\pi(B)R(A,B),
\tag{5.1}
\]

\[
\nu^\downarrow(B)=\pi(B)\sum_A\pi(A)R(A,B),
\tag{5.2}
\]

and

\[
Z:=\sum_A\nu^\uparrow(A)=\sum_B\nu^\downarrow(B)
=\mathbb P_{\pi^{\otimes2}}(R(A_1,A_2)=1).
\tag{5.3}
\]

For fixed endpoints define the raw three-transition joint mass

\[
J_A(B)
:=
\mathbb P_{\pi^{\otimes4}}
(A_1=A,A_4=B,
R_{12}=R_{23}=R_{34}=1).
\tag{5.4}
\]

Equivalently,

\[
J_A(B)=\pi(A)\,[T^3](A,B).
\tag{5.5}
\]

For a constant `gamma in (0,1)` define the **direct bridge overlap**

\[
\mathcal B_\gamma(A)
:=
\sum_B
\min\bigl(J_A(B),\,\gamma\nu^\uparrow(A)\nu^\downarrow(B)\bigr).
\tag{5.6}
\]

This quantity is completely h-free.

### Theorem 5.1 — direct bridge-overlap replacement for the source's local-modification input

Assume a certified lower bound

\[
\lambda\ge \ell>0.
\tag{5.7}
\]

Set the conservative source-compatible thresholds

\[
\rho' := \frac{\ell^2}{3},
\qquad
\rho'' := \frac{\ell^8}{6}.
\tag{5.8}
\]

Suppose there exists a set `G subset S` and `gamma>0` such that

\[
\boxed{
\nu^\uparrow(G^c)\le \rho'' Z,
}
\tag{D1}
\]

and, for every `A in G`,

\[
\boxed{
\mathcal B_\gamma(A)
\ge
\gamma(1-\rho')\nu^\uparrow(A)Z.
}
\tag{D2}
\]

Then the local-modification-dependent portion of the source's mixing proof can be replaced by (D1)--(D2): Lemma 3.20 and Proposition 3.21 hold with explicit constants depending only on `ell` and `gamma`, and the weighted-norm argument of Proposition 3.23 gives a four-step contraction alternative with constants depending only on `ell,gamma`. Consequently the proof of Theorem 3.14 yields exponential mixing of the form

\[
\sum_B|P^k(A,B)-v(B)|\le C_*c_*^k\chi(p),
\qquad c_*<1,
\tag{5.9}
\]

with `C_*,c_*` depending only on `ell,gamma,d,L` (and the same harmless fixed p-range bounds used by the source).

In particular, to certify the mixing ingredient at a proposed initialization point, it is enough to certify `lambda>=ell` together with the h-free inequalities (D1)--(D2). One does **not** need to extract the source's local-modification multiplicity constants.

#### Proof — Step 1: direct replacement for Lemma 3.20

Fix `A in G` and define

\[
v_A(B)
:=
\bigl(\gamma\nu^\uparrow(A)\nu^\downarrow(B)-J_A(B)\bigr)_+.
\]

By `min(x,y)=y-(y-x)_+` and (D2),

\[
\|v_A\|_1
=
\gamma\nu^\uparrow(A)Z-\mathcal B_\gamma(A)
\le
\gamma\rho'\nu^\uparrow(A)Z.
\tag{5.10}
\]

The source's Lemma 3.19 gives

\[
\|h\,v_A\|_1
\le \lambda^{-2}Z^h\|v_A\|_1,
\tag{5.11}
\]

where `Z^h=sum_B h(B)nu^downarrow(B)`. Since `Z<=1`, `rho'<=lambda^2/3`, and (5.10),

\[
\|h\,v_A\|_1
\le
\frac\gamma3\nu^\uparrow(A)Z^h.
\tag{5.12}
\]

Exactly as in the source's proof of Lemma 3.20, rewriting `h v_A` through the Doob transform gives

\[
\sum_B
\min\left(
\frac{h(A)}{\eta^\uparrow(A)}P^3(A,B),
\gamma h(B)\nu^\downarrow(B)
\right)
\ge
\frac{2\gamma}{3}Z^h,
\tag{5.13}
\]

where

\[
\eta^\uparrow(A)=\frac{\nu^\uparrow(A)}{\pi(A)}.
\]

Thus (D2), with no modification map `f_r`, gives exactly the quantitative input needed later.

#### Step 2: the second typical set is automatic

Let

\[
G':=\{A:\eta^\uparrow(A)\ge\rho''\}.
\]

Since `nu^uparrow(A)=pi(A)eta^uparrow(A)`, we have

\[
\nu^\uparrow((G')^c)
\le \rho''\sum_A\pi(A)
=\rho''
\le\frac{\lambda^8}{6}.
\tag{5.14}
\]

For `A,A' in G cap G'`, applying (5.13) twice and the source's inequality `min(x,z)>=min(x,y)+min(y,z)-y` gives the same common-mass conclusion as Proposition 3.21. Using `Z^h>=lambda^2 H>=ell^2H`,

\[
\left\|\min(P^3(h\cdot v),P^3(h\cdot w))\right\|_1
\ge
\frac{\gamma}{3}\ell^2\rho''H\min(\|v\|_1,\|w\|_1)
\tag{5.15}
\]

for nonnegative vectors supported on `G cap G'` in the same normalization as the source.

#### Step 3: bad-set contributions are small enough for Proposition 3.23

Condition (D1) and `Z<=1` imply

\[
\nu^\uparrow(G^c)
\le\rho''
=\frac{\ell^8}{6}
\le\frac{\lambda^8}{6}.
\tag{5.16}
\]

The same upper bound holds for `nu^uparrow((G')^c)` by (5.14). Therefore the two bad pieces in the source's decomposition satisfy, after the two `lambda^{-2}` losses appearing in (3.29), the conservative bound

\[
\text{each bad contribution}
\le \frac{\ell^4}{6}
\times\text{the incoming h-weighted norm}.
\tag{5.17}
\]

If the good-core h-weight of one side is below

\[
a:=\frac{\ell^7}{6}
\tag{5.18}
\]

times the incoming h-weight, the source's displayed calculation therefore gives

\[
\frac{\|P^4v\|_{h+}}{\|v\|_{h+}}
\le
\frac{\ell^4}{2}
<1,
\tag{5.19}
\]

and similarly for the negative side.

If both sides have good-core h-weight at least `a`, (5.15), `rho''=ell^8/6`, and the source's lower bound `||v||_{h+}>=1/H` for normalized disjoint probability differences give a four-step common mass at least

\[
\boxed{
\varepsilon_0
:=
\frac{\gamma\ell^{17}}{108}>0.
}
\tag{5.20}
\]

Hence in this remaining case

\[
\frac{\|P^4(v-w)\|_1}{\|v-w\|_1}
\le1-\varepsilon_0.
\tag{5.21}
\]

So every four steps at least one of three quantities contracts: the `l1` distance by `1-epsilon_0`, the positive h-weight by at most `ell^4/2`, or the negative h-weight by at most `ell^4/2`.

#### Step 4: exponential mixing

Let `N` be any integer such that

\[
(1-\varepsilon_0)^N\le\ell^8/2.
\tag{5.22}
\]

For zero-mass signed vectors define, as in the source,

\[
F(v)=\|v\|_1^N\|v\|_{h+}\|v\|_{h-}.
\]

The Markov property keeps the `l1` norm non-increasing, while the source's Lemma 3.22 gives at most a factor `lambda^{-4}<=ell^{-4}` on each h-weight over four steps. Thus:

- in the `l1`-contraction case, (5.22) compensates the possible `ell^{-8}` growth of the two h-weights;
- in either h-weight-contraction case, `(ell^4/2)ell^{-4}=1/2`.

Therefore

\[
F(P^4v)\le\frac12F(v).
\tag{5.23}
\]

Iteration gives the source's exponential mixing argument. Finally, Lemma 3.1 supplies

\[
\frac{H}{\inf h}
\le\frac{\Omega\chi(p)}{(1-p)^\Omega},
\]

and the source already restricts `p<1/2`, so converting (5.23) back to total variation costs only the allowed `O(chi(p))` prefactor with fixed dimension-dependent constants. This proves (5.9). `square`

### Interpretation

This theorem identifies a **different finite target** for the mixing bottleneck:

> Do not quantify the geometry of `f_r^up,f_r^down`. Instead, certify directly that a high-`nu^up`-mass set of endpoint states has enough three-step raw bridge overlap.

That target is exactly what the later source proof consumes.

---

## 6. The direct bridge criterion is finitely certifiable with exact arithmetic

No numerical instance is certified in this run, so I did **not** manufacture a checker. But (D1)--(D2) admit a finite exact certificate at rational `p` once combined with the previous R09 Simon--Lieb susceptibility upper bound.

Suppose a finite Simon--Lieb block gives

\[
\chi(p)\le U
\]

and choose a finite pointed-cluster family `F`. Let

\[
M_F=\sum_{A\in F}\mu_p(A).
\]

Then

\[
t_F:=1-\frac{M_F}{\Omega U}
\]

is a rigorous upper bound on `pi(F^c)`.

For `A in F`:

1. `nu^up(A)` is `pi(A)` times a one-state sum. Summing allowed targets in `F` gives a lower bound; adding at most `t_F` gives an upper bound.
2. `nu^down(A)` is treated the same way with incoming allowed states.
3. `Z` is a two-i.i.d.-state allowed probability. The `F x F` sum gives a lower bound, while the omitted contribution is at most `2t_F` by a union bound.
4. `J_A(B)` uses two intermediate iid states. Restricting both intermediates to `F` gives a lower bound; the omitted conditional mass is at most `2t_F`.
5. A rigorous lower bound for `B_gamma(A)` is obtained by summing over `B in F` the minima of certified lower bounds for the two terms in (5.6).
6. To certify (D2), compare this lower bound with an upper bound for `gamma(1-rho')nu^up(A)Z`.
7. For a chosen finite good set `G subset F`, a sufficient exact test for (D1) is

\[
Z_{\rm up}-\sum_{A\in G}\nu^\uparrow_{\rm low}(A)
\le
\rho'' Z_{\rm low}.
\tag{6.1}
\]

All finite cluster probabilities `mu_p(A)` are reliability polynomials evaluated at rational `p`, so every finite sum above is rational. The only non-enumerated quantity, `chi(p)`, enters through the previously certified rational interval. Thus the whole bridge test can be implemented with exact rational arithmetic plus a finite cluster enumeration and a Simon--Lieb tail certificate.

This is substantially closer to the owner's requested end product than unpacking the source's local-modification constants: it directly tests the property that the subsequent mixing proof requires.

---

## 7. Prior-art and ownership check

Fresh 2026-09-18 searches covered:

- exact arXiv ID `2609.20764` and exact title;
- Blanc-Renaudie later/current papers surfaced by the search;
- `Doob h transform` + Dobrushin/minorization/quasi-stationary mixing;
- Hilbert/Birkhoff projective contraction for positive kernels.

No later paper resolving the `d=7,8,9,10` source suite surfaced. Classical projective contraction and Dobrushin methods are prior art; I explicitly do **not** claim novelty for Birkhoff--Hopf, conditional-measure coupling, or general quasi-stationary mixing ideas. A representative modern source is Gaubert--Qu on Dobrushin coefficients and Hilbert's projective metric; another is Oliver Tough's work on Dobrushin-type criteria for convergence to quasi-stationarity.

The potentially new/source-specific content here is the exact specialization:

1. the common-`q_h` conditional representation (3.2) for Blanc-Renaudie's pointed-cluster Doob chain;
2. the observation that all projective cross-ratios are h-invariant in this exact kernel;
3. the direct bridge-overlap conditions (D1)--(D2) as a **drop-in replacement** for Proposition 3.16/Corollary 3.17/Lemma 3.18 in the source's Section 3.4 mixing proof;
4. the exact finite-tail recipe of Section 6.

Priority for this source-specific packaging is **unverified** pending independent literature/audit review.

Repository ownership is unchanged. `operations/claims/BLANC-RENAUDIE-2026-MEANFIELD-7-10.md` remains exclusively R09-owned. A neighboring HARD admission worker explicitly recorded that the same new source was already claimed by R09 and did not start parallel research. No ownership conflict was found.

---

## 8. What actually moved conceptually, and what did not

The source-level metric did not move:

\[
\boxed{M_A=0.}
\]

No dimension is proved. The result is **PARTIAL / OPEN**.

But the remaining certificate architecture is materially simpler than at the start of the run:

- **Perron lower bound `lambda_p`:** previous R09 finite exact certificate.
- **High-frequency Proposition 3.25:** previous R09 finite matching/vertex-cover certificate.
- **Mixing Theorem 3.14:** this run gives a direct h-free finite bridge-overlap certificate that can replace the source's local-modification constants if (D1)--(D2) are verified.

Therefore the next useful computation is not another analytic local-modification bound. It is a **small exact cluster enumeration to measure the bridge margin**

\[
\mathfrak B_F
:=
\min_{A\in G_F}
\frac{\mathcal B_\gamma(A)}{\gamma\nu^\uparrow(A)Z},
\tag{8.1}
\]

with rigorous tail intervals, starting in the dimension most favorable after normalization. The target is to see whether `mathfrak B_F` can clear `1-rho'` before the state space becomes prohibitive. If it cannot even in tiny exact truncations, that is evidence to abandon this route quickly rather than spend runs producing bookkeeping.

I am **not** changing the frozen source metric to `mathfrak B_F`; it is only a diagnostic for the next new-method run.

---

## 9. Three method outcomes

### #6 — DEFORM TO A POINT YOU CAN SOLVE

**Succeeded structurally.** The no-cut endpoint becomes an i.i.d. chain, and the exact chain at any cut geometry is a conditioning of one common h-tilted law. This yields the explicit typical-row Dobrushin bound (3.7). It fails as a complete proof because the source only gives a small average cut probability for a modified relation, not the actual relation.

### #13 — FIND WHAT ONLY INCREASES

**Succeeded as a finite diagnostic.** The projective contraction coefficient is immune to diagonal h-reweighting: all cross-ratios are those of the raw killed kernel. Finite truncated powers can therefore be certified without computing h. The infinite tail/zero-support issue still needs a high-mass core.

### #28 — REPLACE FOR ALL WITH FOR TYPICAL

**Produced the main theorem.** The direct bridge-overlap criterion (D1)--(D2), checked only on a high-`nu^up`-mass set, is enough to rerun the source's weighted coupling and obtain exponential mixing. It is h-free and finitely certifiable with exact arithmetic plus a Simon--Lieb tail bound.

---

## 10. Next fresh attacks

The previous triple was `#11/#17/#19`; this run used `#6/#13/#28`. Do not repeat this triple next run.

Reserved fresh methods for the next run:

- **#16 COMPUTE EVERY SMALL CASE:** build the *smallest* exact pointed-cluster family that gives nontrivial direct-bridge overlap, and compute the normalized margin (8.1) in `d=7,8,9,10` before committing to a large state space.
- **#24 FIND THE EXTREMAL OBJECT:** among small endpoint clusters, identify which geometry minimizes the bridge ratio in (8.1). If the extremizer stabilizes, exploit it to reduce the universal endpoint check.
- **#10 DERANDOMIZE:** replace brute-force intermediate-cluster enumeration by an explicit deterministic bridge map only for the finitely many empirically extremal endpoint classes — a much smaller modification problem than the source's all-state construction.

Only build a checker if the #16 enumeration produces a genuinely nontrivial finite bridge margin worth certifying.

---

## 11. Structured ledger delta

```yaml
ledger_delta:
  worker: R09
  lane: CLOSABLE OUTSIDE
  active_source: BLANC-RENAUDIE-2026-MEANFIELD-7-10
  source_arxiv: 2609.20764
  metric_name: M_A
  metric_before: 0
  metric_after: 0
  movement: false
  stagnation_count_before: UNKNOWN
  stagnation_count_after: UNKNOWN
  status: PARTIAL / OPEN
  methods_used: [6, 13, 28]
  new_results:
    - exact common-q_h conditional representation of every Doob row
    - h-free typical-row Dobrushin bound in terms of base cut masses
    - h-invariance of projective cross-ratios for every kernel power
    - direct bridge-overlap criterion D1-D2 replacing local-modification inputs to the mixing proof
    - exact finite-tail recipe for checking D1-D2 at rational p
  source_closed: false
  dimension_certified: []
  finite_numeric_claim_this_run: false
  checker_created: false
  next_methods: [16, 24, 10]
  next_obligation: exact small-state bridge-margin computation before any larger certificate build
  shared_root_edits: false
  peer_file_edits: false
  email_or_drive: false
  public_posting: false
  scheduler_change: false
```

No shared root, peer-track file, email, Drive object, public post, permission, workflow, or scheduler state was modified in this run.
