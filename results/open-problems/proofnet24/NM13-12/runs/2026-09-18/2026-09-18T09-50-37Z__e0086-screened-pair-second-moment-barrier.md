Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO FROZEN-METRIC MOVEMENT: `C_large = 1/pi -> 1/pi`; Section-B methods actually tried: #5 ADD A PARAMETER AND DIFFERENTIATE, #17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE, #25 COUNT THE SAME THING TWICE. Status: PARTIAL.**

# NM13-12 — E0086 screened two-site Green calculation and the exact lower-bound second-moment barrier

Date: 2026-09-18 UTC  
Repository / branch: `yspennstate/math-open-problems` / `master`  
Track: `NM13-12`  
Category: `HARD OUTSIDE`  
Canonical source / claim: `E0086` / `operations/claims/E0086.md`  
Canonical dedup key: `favorite_sites::op_2`  
Canonical SHA-256 / shard: `a616b4531a1a18ab6b2369a38d555ba54d6cc8cacdf46404e4e8ee26baeecc2c`, residue `11 mod 13`

## 1. Runtime, controls, continuity, and required reads

The prompt requests `GPT-6 / maximum`. That is not the model this invocation can honestly report. The actual model is **GPT-5.6 Sol**. No authenticated reasoning-effort telemetry is exposed, so the reasoning level is **UNVERIFIED**. I do not claim GPT-6 or maximum reasoning was bound at runtime.

The exposed task-control schema still contains title/prompt, schedule or offset, timing mode, enabled state, and task identifiers, but no bindable model-family field and no bindable reasoning-effort field. Thus `GPT-6 / maximum` remains prompt text only. Making it binding would require an owner-authorized product/workspace/API/admin surface exposing persistent model and reasoning controls together with authenticated per-run runtime attestation. The repository's current policy records that historical `You cannot modify this task` failures are authorization-context failures; the lawful workaround is an owning/otherwise-authorized context or platform/admin support, not task cloning or access-control bypass. This run did not create, modify, disable, or duplicate any schedule and does not claim a support escalation.

Before mathematics I read or targeted-search-recovered the current state required by the owner policy:

- `FLEET_RULES.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- later owner-authorized `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`;
- root `QUEUE.md`, `POSTED.md`, and `RESULTS.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- canonical claim `operations/claims/E0086.md`;
- newest own report `proofnet24/NM13-12/runs/2026-09-18/2026-09-18T08-59-30Z__e0086-two-trap-green-upper-bound.md`;
- newest neighboring NM13-11 report recovered as `proofnet24/NM13-11/runs/2026-09-18/2026-09-18T09-04-00Z__e0082-stuck-recovery-1-dual-load.md`;
- newest neighboring NM13-13 report recovered as `proofnet24/NM13-13/runs/2026-09-18/2026-09-18T09-00-00Z__successor-admission-screen-4-i-complete.md`;
- E0086 intake/source material, canonical aliases, historical substantive attempt `E0086-A001`, current/historical ownership material, handoffs, and audit searches.

Large aggregate ledgers can be connector-truncated when rendered wholesale. I therefore used current root files plus exact path/ID searches for E0086 and its aliases rather than pretending a truncated display was a byte-for-byte reread of every historical row. Pre-write `master` was observed at `24a9a49de67a95016d52209c7c8054ef5be2ac16`. The mandatory P0483 handoff remains preserved and was not reopened. E0086 remains exclusively owned by NM13-12. A current repository search recovered no E0086 PASS from P26 or NM13-13 and no release, duplicate owner, POSTED settlement, or source-specific retirement.

The preceding E0086 run proved the finite-time two-trap upper bound and the source-main-regime candidate upper constant

\[
g(\beta)=\frac{4\beta(1-\beta)}\pi,
\]

with an almost-sure version for block-frozen/subpolynomial-entropy witnesses. It left the matching lower bound as the high-value obligation. Its actual methods #11/#20/#28 are spent. Earlier E0086 runs spent #2/#6/#30 and #1/#12/#24. The frozen metric entering this run is `C_large=1/pi`, with `unchanged_runs=2` and `stuck_recoveries=0`.

## 2. Source scope and frozen metric

The source remains Izumi Okada, *Topics and problems on favorite sites of random walks*, arXiv:1606.03787, Open Problem 2. For planar simple random walk,

\[
R(n)=\{S_0,\ldots,S_n\},\qquad
K(n,x)=\sum_{j=0}^n {\bf1}_{\{S_j=x\}},
\]

and a finite displacement pattern `H`,

\[
\partial_H G=\{y\in G:y+H\subset G^c\},\qquad
M_H(n)=\max_{y\in\partial_HR(n)}K(n,y).
\]

The source's main moving-pattern regime includes deterministic patterns in

\[
\widetilde D_n\subset D(0,n^\beta)^c\cap D(0,2n^\beta),
\qquad 0<\beta<\frac12. \tag{2.1}
\]

The frozen metric is **not changed** to make the new calculation look like movement:

\[
C_{\rm large}:=\lim_{n\to\infty}\frac{M_{\widetilde D_n}(n)}{(\log n)^2}
\quad\text{in the separate source large-radius regime }a_n\ge n^{1/2+\varepsilon}.
\]

The source-correction run already established `C_large=1/pi`. This run attacks the different main-regime lower-bound mechanism and therefore records honest metric no-movement.

## 3. The three new Section-B attacks

No code was written. The run is an analytic route-finding run, and the finite-volume statements below are proved on the page.

### #5 — ADD A PARAMETER AND DIFFERENTIATE IN IT

The previous upper bound used an outer confinement exponent `alpha>1/2`. For a lower bound, reverse the role of the time scale and introduce an **inner stopping radius**

\[
R_n=n^\alpha,\qquad \beta<\alpha<\frac12. \tag{3.1}
\]

Then `tau_{R_n}=o(n)` on its natural scale, so a source-valid good site can be built before the walk has used most of its time budget. A second parameter

\[
|y-z|=n^{\delta+o(1)},\qquad 0\le\delta\le\alpha, \tag{3.2}
\]

tracks pair separation. Optimizing in `alpha` and differentiating the resulting shell exponent in `delta` isolates an explicit threshold `beta_*` below.

### #17 — LOOK FOR YOUR NUMBERS SOMEWHERE ELSE

A bounded 2026-09-18 search was refreshed around Okada's pair-of-favorite-points paper, planar late-point/thick-point work of Dembo--Peres--Rosen--Zeitouni, and the newer Hao--Li--Okada--Zheng favorite-site paper. The pair-favorite and late-point literature confirms that the right lower-bound bookkeeping is a distance-shell second moment for a log-correlated field. It does **not** directly answer the source event here, because the partner point `y+h_n` is required to have local time exactly zero while `y` is unusually highly visited. The 2025 Hao--Li--Okada--Zheng theorem concerns the number/evolution of ordinary favorite sites, not this translated-boundary quantity. No source-matching later resolution was found in the bounded search. This is negative evidence only; publication novelty remains **UNVERIFIED**.

### #25 — COUNT THE SAME THING TWICE

Count candidate good sites once by the exact one-site killed Green tail, and count ordered pairs of candidates again by separation scale `delta`. The key new object is a **four-point Schur complement**: two candidate sites and their two forbidden translates. It gives a closed formula for the leading eigenvalue that controls the pair survival tail. The resulting exponent arithmetic closes every genuinely mesoscopic pair shell in an explicit beta range and identifies the exact remaining obstruction: macroscopic-pair logarithmic prefactors, not a missing power exponent.

## 4. One-site lower-bound scale inside an inner disk

Fix `beta<alpha<1/2`, let `R=n^alpha`, and let a deterministic singleton displacement satisfy

\[
n^\beta<|h|\le 2n^\beta. \tag{4.1}
\]

Take candidate sites in a fixed interior annulus, for example

\[
\mathcal A_R=\{y\in\mathbb Z^2:R/8\le |y|\le R/5\}. \tag{4.2}
\]

For all large `n`, both `y` and `y+h` lie a fixed positive fraction of `R` away from the disk boundary. Let

\[
\tau_R=\inf\{k:S_k\notin D(0,R)\}.
\]

The preceding run's exact one-trap Schur complement works for every `alpha>beta`, not only for `alpha>1/2`:

\[
G_R^{\neg(y+h)}(y,y)
=G_R(y,y)-\frac{G_R(y,y+h)^2}{G_R(y+h,y+h)}. \tag{4.3}
\]

Uniformly for `y in A_R`, the planar potential-kernel expansion gives

\[
\begin{aligned}
G_R(y,y)&=\frac{2\alpha}{\pi}\log n+O(1),\\
G_R(y+h,y+h)&=\frac{2\alpha}{\pi}\log n+O(1),\\
G_R(y,y+h)&=\frac{2(\alpha-\beta)}\pi\log n+O(1).
\end{aligned} \tag{4.4}
\]

Hence

\[
G_R^{\neg(y+h)}(y,y)
=\left[\sigma_1(\alpha,\beta)+o(1)\right]\log n,\qquad
\boxed{\sigma_1(\alpha,\beta)=\frac2\pi\left(2\beta-\frac{\beta^2}{\alpha}\right).} \tag{4.5}
\]

Starting from `y`, the number of visits to `y` before `T_{y+h}\wedge\tau_R`, including time zero, is geometric with mean (4.3). Standard disk potential-kernel estimates also give uniformly in `y in A_R`

\[
P_0(T_y<T_{y+h}\wedge\tau_R)=\Theta((\log n)^{-1}),\qquad
P_y(\tau_R<T_{y+h})=\frac\beta\alpha+o(1). \tag{4.6}
\]

The first relation follows from the equilibrium measure of the two-point set `{y,y+h}` viewed from a point a fixed fraction of `R` away; the second follows from

\[
P_y(T_{y+h}<\tau_R)=\frac{G_R(y,y+h)}{G_R(y+h,y+h)}
=1-\frac\beta\alpha+o(1). \tag{4.7}
\]

For `m=c(\log n)^2`, let `B_y` be the event that the walk reaches `y` before its forbidden translate and exit, accumulates at least `m` visits to `y`, and then exits `D(0,R)` before ever hitting `y+h`. Strong Markov at the first hit and at the `m`th visit gives

\[
P(B_y)
=n^{-c/\sigma_1+o(1)}. \tag{4.8}
\]

The suppressed factor is only polylogarithmic and the terminal escape probability in (4.6) is bounded away from zero. Since `|A_R|=n^{2\alpha+o(1)}`, for

\[
Z=\sum_{y\in\mathcal A_R}{\bf1}_{B_y}
\]

we have

\[
EZ=n^{2\alpha-c/\sigma_1+o(1)}. \tag{4.9}
\]

Thus the one-site first-moment threshold is

\[
\boxed{c_\alpha=2\alpha\sigma_1
=\frac4\pi(2\alpha\beta-\beta^2).} \tag{4.10}
\]

As `alpha up to 1/2`,

\[
c_\alpha\uparrow \frac{4\beta(1-\beta)}\pi=g(\beta), \tag{4.11}
\]

exactly the upper-bound constant found in the preceding run. This agreement is the reason to continue the route rather than discard it.

## 5. Exact four-point elimination for a candidate pair

Let `A={y,z}` and let the two forbidden translates be

\[
H=\{y+h,z+h\}.
\]

Write `G` for the disk Green matrix on `A union H`, in block form

\[
G=\begin{pmatrix}G_{AA}&G_{AH}\\G_{HA}&G_{HH}\end{pmatrix}.
\]

Killing on `H` before disk exit gives the exact two-site Green matrix

\[
\boxed{F_A=G_{AA}-G_{AH}G_{HH}^{-1}G_{HA}.} \tag{5.1}
\]

This is the two-point version of (4.3). It follows either by applying the strong Markov property at the first hit of `H` to each matrix entry or by block Gaussian elimination of the Green resolvent.

For points staying in a fixed interior fraction of `D(0,R)`, the potential-kernel identity gives uniformly

\[
G_R(u,v)=\frac2\pi\bigl(\log R-\log(|u-v|\vee1)\bigr)+O(1),\quad u\ne v, \tag{5.2}
\]

and `G_R(u,u)=(2/pi)log R+O(1)`.

Assume

\[
|y-z|=n^{\delta+o(1)},\qquad 0\le\delta\le\alpha. \tag{5.3}
\]

If `delta>beta`, then both cross distances `|y-(z+h)|` and `|z-(y+h)|` have exponent `delta`; if `delta<beta`, both have exponent `beta`. At `delta=beta`, one cross distance can be smaller only in a near-cancellation geometry. The cancellation case can only lower the leading Perron eigenvalue in the calculation below; exact coincidence with a forbidden translate makes `B_y cap B_z` impossible.

### Proposition 5.1 — screened pair Green eigenvalue

Let `lambda_max(F_A)` denote the largest eigenvalue of (5.1). Then

\[
\lambda_{\max}(F_A)
\le \left[\frac2\pi L_{\alpha,\beta}(\delta)+o(1)\right]\log n, \tag{5.4}
\]

where

\[
\boxed{
L_{\alpha,\beta}(\delta)=
\begin{cases}
\displaystyle
\frac{(2\beta-\delta)(4\alpha-2\beta-\delta)}{2\alpha-\delta},
&0\le\delta\le\beta,\\[1.2ex]
\displaystyle
2\beta-\frac{\beta^2}{2\alpha-\delta},
&\beta\le\delta\le\alpha.
\end{cases}} \tag{5.5}
\]

Away from the near-cancellation geometry at `delta=beta`, (5.4) is an equality at leading order.

#### Proof

Suppress the common factor `(2/pi) log n` and write only leading dimensionless matrices.

**Case 1: `delta>=beta`.** The candidate block and trap block are both

\[
A_0=\begin{pmatrix}\alpha&\alpha-\delta\\\alpha-\delta&\alpha\end{pmatrix},
\]

while

\[
B_0=\begin{pmatrix}\alpha-\beta&\alpha-\delta\\\alpha-\delta&\alpha-\beta\end{pmatrix}.
\]

All three matrices diagonalize in the symmetric/antisymmetric basis. The candidate eigenvalues are

\[
a_+=2\alpha-\delta,\qquad a_-=\delta,
\]

and the cross-block eigenvalues are

\[
b_+=2\alpha-\beta-\delta=a_+-\beta,\qquad
b_-=\delta-\beta=a_--\beta.
\]

Therefore the two Schur-complement eigenvalues are

\[
\ell_+=a_+-\frac{b_+^2}{a_+}
=2\beta-\frac{\beta^2}{2\alpha-\delta}, \tag{5.6}
\]

and

\[
\ell_-=a_--\frac{b_-^2}{a_-}
=2\beta-\frac{\beta^2}{\delta}. \tag{5.7}
\]

Since `delta<=alpha`, `2alpha-delta>=delta`, so `ell_+>=ell_-`. This gives the second line of (5.5).

**Case 2: `delta<=beta`.** Now both cross distances have exponent `beta`, so

\[
B_0=\begin{pmatrix}\alpha-\beta&\alpha-\beta\\\alpha-\beta&\alpha-\beta\end{pmatrix}.
\]

The antisymmetric mode is untouched and has eigenvalue `delta`. The symmetric mode becomes

\[
\ell_+
=(2\alpha-\delta)-\frac{4(\alpha-\beta)^2}{2\alpha-\delta}
=\frac{(2\beta-\delta)(4\alpha-2\beta-\delta)}{2\alpha-\delta}. \tag{5.8}
\]

Moreover

\[
\ell_+-\delta
=\frac{2(4\alpha\beta-3\alpha\delta-2\beta^2+\delta^2)}{2\alpha-\delta}>0, \tag{5.9}
\]

because the numerator is decreasing on `[0,beta]` and at `delta=beta` equals `2beta(alpha-beta)>0`. Hence the symmetric mode is the Perron mode and gives the first line of (5.5).

At the boundary `delta=beta`, suppose one cross distance has smaller exponent `eta<=beta` while the other remains at exponent `beta`. Direct substitution in (5.1) gives, after the same normalization,

\[
F_A=
\begin{pmatrix}
\displaystyle\frac{\eta(4\alpha\beta-\alpha\eta-2\beta^2)}{\beta(2\alpha-\beta)}
&\displaystyle\frac{\eta(\alpha-\beta)}{2\alpha-\beta}\\[1.1ex]
\displaystyle\frac{\eta(\alpha-\beta)}{2\alpha-\beta}
&\displaystyle\frac{\beta(3\alpha-2\beta)}{2\alpha-\beta}
\end{pmatrix}. \tag{5.10}
\]

Every nonconstant entry in this nonnegative symmetric matrix is increasing in `eta` on `[0,beta]`; therefore its Perron eigenvalue is maximized at `eta=beta`, the generic value already covered by (5.5). This proves the asserted upper bound in the cancellation case as well. `square`

## 6. Trace-chain tail and the pair-shell exponent

Let the walk be killed on `H` or on exiting the disk, and trace it on `A={y,z}`. If `Q_A` is the substochastic transition matrix of successive visits to `A`, then

\[
F_A=(I-Q_A)^{-1}. \tag{6.1}
\]

Because the original killed walk is reversible with counting measure and `F_A` is symmetric, `Q_A=I-F_A^{-1}` is symmetric. Hence, with `rho(Q_A)` its Perron eigenvalue,

\[
\rho(Q_A)=1-\frac1{\lambda_{\max}(F_A)}. \tag{6.2}
\]

Starting from either point of `A`, the probability that the trace survives for at least `r` visits is at most

\[
\sqrt2\,\rho(Q_A)^{r-1}. \tag{6.3}
\]

If both `B_y` and `B_z` occur, then the trace has made at least `2m` visits to `A` before either forbidden translate is hit. Combining (5.4)--(6.3), for `m=c(log n)^2`, gives the power-scale upper bound

\[
P(B_y\cap B_z)
\le n^{-2c/\sigma_2(\delta)+o(1)},\qquad
\sigma_2(\delta):=\frac2\pi L_{\alpha,\beta}(\delta). \tag{6.4}
\]

There are

\[
n^{2\alpha+2\delta+o(1)} \tag{6.5}
\]

ordered candidate pairs at separation exponent `delta`. Since `(EZ)^2=n^{4\alpha-2c/\sigma_1+o(1)}`, the exponent of the contribution of this shell relative to `(EZ)^2` is

\[
D_c(\delta)
=2(\delta-\alpha)+2c\left(\frac1{\sigma_1}-\frac1{\sigma_2(\delta)}\right). \tag{6.6}
\]

This is the exact quantity the lower-bound route has to keep nonpositive.

At the first-moment threshold `c=c_alpha=2alpha sigma_1`, the algebra becomes explicit.

For `beta<=delta<=alpha`,

\[
\boxed{
D_{c_\alpha}(\delta)
=-\frac{2(\alpha-\delta)(4\alpha-3\beta-2\delta)}{4\alpha-\beta-2\delta}.} \tag{6.7}
\]

For `0<=delta<=beta`,

\[
\boxed{
D_{c_\alpha}(\delta)
=-\frac{2\delta\,[4\alpha^2-12\alpha\beta+3\alpha\delta+6\beta^2-\delta^2]}
{(2\beta-\delta)(4\alpha-2\beta-\delta)}.} \tag{6.8}
\]

Both identities follow by substituting (4.5) and (5.5) into (6.6) and cancelling positive factors.

In the first interval the numerator factor `4alpha-3beta-2delta` is minimized at `delta=alpha`, so (6.7) is nonpositive whenever `beta/alpha<=2/3`.

In the second interval the bracket

\[
H(\delta)=4\alpha^2-12\alpha\beta+3\alpha\delta+6\beta^2-\delta^2 \tag{6.9}
\]

is increasing on `[0,beta]`, because `H'(delta)=3alpha-2delta>0`. Thus its minimum is `H(0)`, and

\[
H(0)\ge0
\iff 4\alpha^2-12\alpha\beta+6\beta^2\ge0
\iff \frac\beta\alpha\le 1-\frac1{\sqrt3}. \tag{6.10}
\]

The latter condition is stronger than `beta/alpha<=2/3`. Therefore

\[
\boxed{
\frac\beta\alpha\le1-\frac1{\sqrt3}
\quad\Longrightarrow\quad
D_{c_\alpha}(\delta)\le0\text{ for every }0\le\delta\le\alpha.} \tag{6.11}
\]

For every fixed `c<c_alpha`, the inequality is strict for every `delta<alpha`, because `sigma_2(delta)>sigma_1` there and lowering `c` strictly decreases (6.6).

Letting `alpha up to 1/2` identifies the source-scale window

\[
\boxed{
0<\beta<\beta_*:=\frac12\left(1-\frac1{\sqrt3}\right)
=0.2113248654\ldots .} \tag{6.12}
\]

### Corollary 6.1 — all genuinely mesoscopic pair shells are power-negligible

Fix `beta<beta_*` and `c<g(beta)`. Then one can choose `alpha<1/2`, arbitrarily close to `1/2`, with `beta/alpha<1-1/sqrt(3)` and `c<c_alpha`. For every fixed `epsilon>0`, the contribution to `E Z^2` from pairs satisfying

\[
|y-z|\le n^{\alpha-\varepsilon} \tag{6.13}
\]

is

\[
o((EZ)^2) \tag{6.14}
\]

at the level of the complete power law, with enough fixed exponent slack to absorb every polylogarithmic factor suppressed in (4.8) and (6.4).

#### Proof

On the compact range `0<=delta<=alpha-epsilon`, continuity of (6.6) and the strict inequality just proved give `sup D_c(delta)=-eta` for some `eta>0`. A finite mesh of distance shells, with the `o(1)` terms in (5.4) made uniform, bounds their total by `n^{-eta/2+o(1)}(EZ)^2`. `square`

This is a complete quantitative finite-volume statement. It says that below `beta_*`, the lower-bound route does **not** fail because of any power-law cluster of nearby candidate sites.

## 7. The attempted matching lower bound stops at one exact missing prefactor

The natural hope was now to apply Paley--Zygmund to `Z` and obtain a positive probability of a singleton site carrying `c(log n)^2` visits while its translate remains unvisited, then transfer from `tau_R=o(n)` to deterministic time `n` and finally use a tail/zero-one argument. Sections 4--6 show that the first moment has the correct candidate threshold and that every fixed mesoscopic distance scale is harmless for `beta<beta_*`.

The route **does not yet close**, and I do not claim the matching lower bound.

The obstruction is the endpoint `delta=alpha`, i.e. candidate pairs at macroscopic separation comparable with `R`. At that endpoint

\[
\sigma_2(\alpha)=\sigma_1,
\qquad
D_c(\alpha)=0 \tag{7.1}
\]

for every `c`; therefore power exponents alone cannot decide the second moment. The crude trace-survival inequality (6.3) forgets the balanced requirement

\[
L_y\ge m\quad\text{and}\quad L_z\ge m \tag{7.2}
\]

and remembers only `L_y+L_z>=2m`. It also forgets the two-point entrance normalization. At macroscopic separation, a single prescribed site is first reached with probability `Theta(1/log n)`. The product of two one-site probabilities therefore carries `(log n)^(-2)`, whereas the total-trace bound can retain only one common entrance factor. With the present inequality this leaves, in the worst bookkeeping, an unresolved logarithmic factor in `EZ^2/(EZ)^2`. A bound of order `O(log n)` there would give only a Paley--Zygmund lower bound of order `1/log n`, insufficient for the intended direct positive-probability/zero-one transfer.

So the missing statement has now been localized sharply:

\[
\boxed{
\text{Obtain a two-site occupation bound that retains (7.2), with the correct macroscopic entrance/prefactor,}
} \tag{7.3}
\]

or replace `Z` by a cluster-normalized count for which the common-entrance logarithm cancels.

This is materially more specific than “need a second moment.” The four-point Green calculation proves that there is no hidden adverse **power exponent** below `beta_*`; the only remaining obstruction in that window is the endpoint logarithmic normalization/balanced-occupation estimate. A multiscale argument is not being assumed: the scale variable, pair induction target, and exact unsummed endpoint error are displayed.

## 8. Why the route is still source-valid

The inner stopping radius satisfies `R^2=n^{2alpha}=o(n)`. Standard exit-time tails therefore make `P(tau_R>n/2)=o(1)`. If a pre-exit good site is eventually obtained, after exit its forbidden translate lies a distance of order `R` from the walk, and the standard planar point-avoidance estimate from radius `n^alpha` to time `n` is bounded below by a positive constant depending on `alpha`. Thus deterministic-time transfer does not cost a power of `n`. The present failure occurs **before** that transfer, in the macroscopic pair prefactor of the finite-volume second moment.

This run therefore does not use a finite computation as evidence for an asymptotic exponent and does not silently replace the source process by a disk-exit problem. The disk is an intermediate source-valid stopping construction whose remaining transfer cost has been identified.

## 9. Literature refresh, dated scope, and access limits

Fresh bounded searches on 2026-09-18 included combinations of:

- `Izumi Okada Open Problem 2 favorite sites planar random walk`;
- `favorite sites planar random walk translated boundary Okada`;
- `Favorite Sites for Simple Random Walk in Two and More Dimensions Hao Li Okada Zheng`;
- `pairs of nearly favorite points Okada planar random walk`;
- `late points thick points pair exponent planar random walk`.

The original source remains Okada, arXiv:1606.03787 (2016). Okada's 2019 paper on exponents for pairs of nearly favorite points gives the closest pair-distance-shell machinery. Dembo--Peres--Rosen--Zeitouni's late/thick-point work gives the analogous log-correlated multiscale template. Hao--Li--Okada--Zheng, arXiv:2409.00995 / *Probability Theory and Related Fields* (accepted 2025), concerns the number and evolution of ordinary favorite sites and does not state the translated-boundary asymptotic in E0086.

No source-matching later resolution of Open Problem 2, and no paper visibly giving the screened constant `4 beta(1-beta)/pi` or the threshold (6.12), surfaced in this bounded search. That is **not** proof of worldwide openness or novelty. The potential-kernel, Schur-complement, trace-chain, and distance-shell mechanisms are standard/folklore ingredients; publication novelty of their present combination is **UNVERIFIED**.

Access limits: search snippets and accessible abstracts/full-text mirrors were used where available; I did not claim an exhaustive citation-graph or paywalled full-text review.

## 10. Status, counters, audits, and forced next-run protocol

The frozen metric did not move:

```text
C_large: 1/pi -> 1/pi
unchanged_runs: 2 -> 3
stuck_recoveries: 0 -> 0
```

The source status stays **PARTIAL / OPEN**. This run proves the screened two-site Green eigenvalue and a complete exponent-level second-moment closure for all nonmacroscopic pair scales below the explicit threshold `beta_*`, but it does **not** prove the matching singleton lower bound and does not change the source large-radius frozen metric.

No closure is claimed. Required independent audits remain:

```text
P26: NOT PASSED / no E0086 PASS recovered
NM13-13: NOT PASSED / no E0086 PASS recovered
```

Because this is now the third consecutive frozen-metric no-movement run, the **next NM13-12 invocation must be the owner's Section-I thinking-only stuck recovery**. It must not add another ordinary lemma. The exact blocker to place at the center of that report is (7.3); that report must inventory every E0086 route, state the simplest still-unproved special case, identify the nearest solved pair-thick-point problem and the ingredient it has that (7.3) lacks, then choose exactly one permitted recovery. A plausible recovery to evaluate there is to port the pair-favorite/late-point balanced occupation calculation rather than continue the total-trace spectral bound. Fresh method candidates for that recovery are #3 PROVE SOMETHING STRONGER, #7 TAKE THE LIMIT, and #22 READ THE FAILURES, but they are **not** counted as tried in this run.

No substantive artifact was created because there is no finite claim needing an exact-arithmetic certificate and no checker would resolve the missing macroscopic prefactor. No shared root, canonical claim, peer namespace, workflow, permission, public surface, email/Drive resource, paid compute, or schedule was modified.

## 11. Structured ledger delta for P26

```yaml
ledger_delta:
  track: NM13-12
  category: HARD_OUTSIDE
  source_id: E0086
  claim_id: E0086
  canonical_dedup_key: favorite_sites::op_2
  status_before: PARTIAL
  status_after: PARTIAL
  frozen_metric:
    name: C_large
    scope: source large-radius regime a_n >= n^(1/2+epsilon)
    before: 1/pi
    after: 1/pi
    movement: false
  methods_actual:
    - 5  # ADD A PARAMETER AND DIFFERENTIATE IN IT
    - 17 # LOOK FOR YOUR NUMBERS SOMEWHERE ELSE
    - 25 # COUNT THE SAME THING TWICE
  mathematical_progress:
    - exact four-point Green Schur-complement reduction for two candidate sites and their forbidden translates
    - proved piecewise leading Perron coefficient L_{alpha,beta}(delta)
    - proved pair-shell exponent formulas D_{c_alpha}(delta)
    - proved all fixed mesoscopic pair shells are power-negligible for beta < beta_star and c < 4 beta(1-beta)/pi
    - isolated the remaining macroscopic balanced-occupation/prefactor obstruction
  explicit_threshold:
    beta_star: (1/2)*(1-1/sqrt(3))
    decimal: 0.2113248654
  matching_lower_bound_status: NOT_PROVED
  blocker: retain L_y>=m and L_z>=m plus correct macroscopic entrance prefactor; total-trace survival loses a logarithm
  unchanged_runs_before: 2
  unchanged_runs_after: 3
  stuck_recoveries_before: 0
  stuck_recoveries_after: 0
  next_run_protocol: SECTION_I_STUCK_RECOVERY_1_THINKING_ONLY
  next_blocker: macroscopic two-site balanced-occupation estimate / cluster-normalized second moment
  audits:
    P26: NOT_PASSED
    NM13-13: NOT_PASSED
  literature_checked: 2026-09-18
  literature_result: bounded search found no source-matching later resolution; novelty UNVERIFIED
  artifacts_created: none
```
