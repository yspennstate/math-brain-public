Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.** Metric moved: `W_3: 0.656515 -> 0.656514`. Methods actually tried: **B1 / B11 / B29**.

# HARD7-06 run 13 — same-degree ACG endpoint, a truncated-entropy area inequality, and an exact sprinkling obstruction

Status: **F0095 OPEN / HARD7-06 PARTIAL.** This run does not prove existence of the constant 3-colourability threshold. It stops decimal optimisation of the ACG variational ansatz and changes category to the missing threshold-location mechanism identified by Bayati--Gamarnik--Tetali.

Repository / branch: `yspennstate/math-open-problems` / `master`.

## 1. Continuity, ownership, exclusions, and current-source check

I resumed the admitted canonical target `F0095`, owned by HARD7-06 in `operations/claims/F0095.md`. I did not reopen the exhausted CKS predecessor, the old random-3-SAT lifecycle, the negative-margin perceptron track, or any posted/settled source. At run start I reread the controlling HARD7 files, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, campaign `INDEX.md` and `RANKING.md`, the F0095 claim and newest HARD7-06 report, and the newest neighbouring hard-CSP ownership state. The latest R14 report explicitly keeps the negative-margin spherical-perceptron target handed off and does not reopen it.

The source target remains Alan Frieze's ICM 2014 chromatic-number conjecture, intake `F0095`:

> **Conjecture:** There exists a sequence `d_k`, `k >= 2`, such that w.h.p. `chi(G_{n,d/n}) = k` for `d_{k-1} < d < d_k`.

The frozen case is `k=3`, i.e. existence of a constant location for the ordinary sparse Erdos--Renyi 3-colourability transition. Achlioptas--Friedgut sharpness gives an `n`-dependent threshold sequence and does not imply convergence of its location.

### Fresh literature/alias screen, 2026-09-19

The most relevant source recovered this run is Mohsen Bayati, David Gamarnik and Prasad Tetali, *Combinatorial approach to the interpolation method and scaling limits in sparse random graphs*, Ann. Probab. 41 (2013), 4080--4115, arXiv:0912.2444. Their Theorem 1 proves existence of the exponential-rate limit

\[
\lim_{N\to\infty}N^{-1}\log p(N,\lfloor cN\rfloor)=p(c)
\]

for colouring, K-SAT and NAE-K-SAT, where `p(N,M)` is the satisfiability/colourability probability. Their **Conjecture 1** asks for a strengthening of Friedgut: above a fixed multiplicative displacement from the sharp threshold sequence, satisfiability should be `O(exp(-gamma N))`. They explicitly explain that this strengthening, together with their scaling-limit theorem, would imply the constant-location satisfiability conjecture. Thus BGT Conjecture 1 is a canonical **stronger route to** F0095, not an equivalent statement and not a competing ownership alias.

Peter Ayre, Amin Coja-Oghlan and Catherine Greenhill, *Lower bounds on the chromatic number of random graphs*, Combinatorica 42 (2022), 617--658, arXiv:1812.09691v4, still states in Section 1.4 that the fixed-`q` sparse colourability threshold is widely conjectured, while Achlioptas--Friedgut only provide the non-uniform threshold sequence. A bounded search dated 2026-09-19 for `random graph 3-colorability threshold`, `q-colorability threshold q=3`, the BGT exponential-tail conjecture, and 2025--2026 follow-ups did not recover a later proof of the fixed ordinary `q=3` threshold. This is bounded negative evidence, not a worldwide novelty certificate.

Repository searches for `log(1+Z) colorings` and `sprinkling colorability` returned no existing fleet version of the two lemmas below. Web searches for the exact same phrases likewise did not recover the exact statements. BGT do have a different one-edge **lower** survival estimate and a `delta`-unusual-colouring argument. Therefore I do not label the lemmas below globally novel; they are a new route in this repository unless later prior art is found.

## 2. Frozen metric and a source-proof correction

The fixed quantity remains

\[
W_3=U_3-L_3,
\]

with `L_3=4.03` the rigorous w.h.p. 3-colourable endpoint and `U_3` a rigorous w.h.p. non-3-colourable endpoint in the same ordinary sparse Erdos--Renyi model.

The preceding run recorded

\[
U_3=4.686515,\qquad W_3=0.656515,
\]

using an exact rational law `a` for which its checker proved

\[
\Sigma^*_{4.686514,3}(a)<0.
\tag{2.1}
\]

That report inserted one micro-unit of slack because Theorem 1.3 is stated as `d>d_3^*`. Reading the proof of Theorem 1.3 itself removes that artificial slack. ACG's proof starts with the strictly stronger hypothesis

\[
\Sigma^*_{d,q}<0
\]

**at the same value `d`**, invokes Proposition 2.12 to obtain finite `y,beta>0` with `phi_{beta,y}<0`, then Corollary 2.11 and Corollary 2.3 to conclude non-`q`-colourability w.h.p. at that same `d`. Since (2.1) is an explicit witness, it implies the infimum `\Sigma^*_{4.686514,3}<0`. Therefore

\[
\boxed{\chi(G(n,4.686514/n))>3\quad\text{w.h.p.}}
\tag{2.2}
\]

without increasing `d` to `4.686515`.

Thus the rigorous source-relevant endpoint moves by exactly one micro-unit:

\[
\boxed{U_3:4.686515\to4.686514,\qquad
W_3:0.656515\to0.656514.}
\tag{2.3}
\]

This uses the preceding run's already-executed exact certificate; no new finite checker is needed or useful.

### Exponential strengthening already implicit in the ACG proof

There is a second consequence worth recording because it connects directly to BGT Conjecture 1. ACG Proposition 2.1 gives exponential concentration of `log Z_beta` around its expectation. Under `Sigma^*_{d,q}<0`, Proposition 2.12 and Corollary 2.11 give some finite `beta>0` and `delta>0` such that for all large `n`,

\[
\mathbb E\log Z_\beta(G(n,d/n))\le-\delta n.
\]

If the graph is `q`-colourable, then `Z_beta>=1`, hence `log Z_beta>=0`. Proposition 2.1 therefore yields, for some `xi=xi(d,q)>0`,

\[
\boxed{\mathbb P\{\chi(G(n,d/n))\le q\}\le e^{-\xi n}}
\tag{2.4}
\]

for all sufficiently large `n`. ACG state only the w.h.p. conclusion in Corollary 2.3, but (2.4) follows immediately from the exponential tail in Proposition 2.1 and the proof they give. I treat (2.4) as an **extracted consequence of their proof**, not as a novelty claim.

In particular the exact HARD7 witness at `d=4.686514` lies in the exponential non-colourability region. This does not settle BGT Conjecture 1 near the unknown sharp-threshold sequence; it identifies exactly what has to be transported downward.

## 3. B1 — change category: from a colour-count optimisation to the BGT exponential-tail gap

The previous ACG finite-support search can keep shaving decimals, but it does not attack the source-level missing implication. BGT isolate the structural gap: the existence of the scaling limit of `N^{-1} log p(N,cN)` is known, yet Friedgut gives only `p->0` above an `N`-dependent threshold, whereas BGT need **exponential** decay at a fixed relative displacement.

So this run changes the object. Work in the uniform simple graph process `G_{n,m}` and write

\[
Z_m=\#\{\text{proper 3-colourings of }G_{n,m}\},\qquad
p_m=\mathbb P(Z_m>0),
\]

and introduce the boundary-regularised hard entropy

\[
H_m=\mathbb E\log(1+Z_m).
\tag{3.1}
\]

The `+1` is deliberate: ordinary `log Z_m` is singular on the uncolourable event, exactly where the source problem lives.

The first question is whether a deterministic one-edge inequality links the decrement of (3.1) to `p_m`. It does.

## 4. B11 — dualise edge addition through the uniform solution measure

Let

\[
N=\binom n2,
\]

and let

\[
M_n:=\min_{n_1+n_2+n_3=n}\sum_{i=1}^3\binom{n_i}{2}
=r\binom{a+1}{2}+(3-r)\binom a2,
\tag{4.1}
\]

where `n=3a+r`, `r in {0,1,2}`. Thus `M_n` is the exact minimum number of monochromatic pairs in any 3-colouring of `n` labelled vertices.

### Proposition 4.1 — exact truncated-entropy area inequality

For every `n>=4` and `0<=m<N`,

\[
\boxed{
H_m-H_{m+1}
\ge
\frac67\frac{M_n}{N-m}\,p_m.}
\tag{4.2}
\]

Consequently, for every integer `t>=1` with `m+t<=N`,

\[
\boxed{
p_{m+t}
\le
\frac{7(N-m)}{6M_n t}\,[H_m-H_{m+t}].}
\tag{4.3}
\]

#### Proof

Couple `G_{n,m+1}` from `G=G_{n,m}` by choosing one uniformly random missing edge `e={u,v}`. Fix `G` and set `z=Z(G)`. If `z=0`, adding an edge leaves `z=0`, so the conditional increment of `log(1+z)` is zero.

Assume `z>0`. For a missing edge `e`, let

\[
q_e=\frac1z\#\{\sigma:\sigma\text{ proper for }G,\ \sigma(u)=\sigma(v)\}.
\]

Adding `e` kills exactly the fraction `q_e` of proper colourings, so

\[
\log(1+Z(G+e))-\log(1+z)
=
\log\left(1-\frac{z}{1+z}q_e\right)
\le
-\frac{z}{1+z}q_e.
\tag{4.4}
\]

Whenever a graph on `n>=4` vertices is 3-colourable, `z>=6`: if it has an edge, the `S_3` action on every proper colouring is free because at least two colours occur; if it is edgeless, `z=3^n`. Hence

\[
\frac{z}{1+z}\ge\frac67.
\tag{4.5}
\]

For every proper colouring `sigma` with colour-class sizes `n_1,n_2,n_3`, every monochromatic pair is necessarily a missing edge of `G`, and there are at least `M_n` such pairs. Double-counting pairs `(sigma,e)` therefore gives

\[
\frac1{N-m}\sum_{e\notin E(G)}q_e
=
\frac1z\sum_\sigma\frac{\#\{e\notin E(G):\sigma(u)=\sigma(v)\}}{N-m}
\ge\frac{M_n}{N-m}.
\tag{4.6}
\]

Average (4.4), use (4.5)--(4.6), and then average over `G_{n,m}`. This proves (4.2).

For (4.3), sum (4.2) from `j=m` to `m+t-1`. In the standard edge-addition coupling, `p_j` is non-increasing in `j`, while `(N-j)^{-1}>=(N-m)^{-1}`. Hence

\[
H_m-H_{m+t}
\ge
\frac67\frac{M_n}{N-m}\,t\,p_{m+t},
\]

which rearranges to (4.3). `square`

### Consequence and exact remaining obstruction

If for edge densities `c_1<c_2` the limits

\[
h(c)=\lim_{n\to\infty}\frac1n H_{\lfloor cn\rfloor}
\]

exist and satisfy `h(c_1)=h(c_2)`, then (4.3), with `t=(c_2-c_1)n+O(1)`, forces

\[
p_{\lfloor c_2n\rfloor}\to0.
\tag{4.7}
\]

Thus a plateau of the boundary-regularised hard entropy is already enough to certify non-colourability w.h.p. at its right endpoint. Conversely, any interval on which colourability stays bounded away from zero must make `h` decrease at a definite rate.

This is not yet the source theorem: existence and sufficiently rigid structure of the limit `h(c)` in (3.1) are unproved here. BGT prove several free-energy/scaling limits, but their results do not simply identify this boundary-regularised hard entropy. The point of (4.2) is to isolate a concrete thermodynamic object whose slope directly sees colourability probability rather than only the typical MAX-CSP defect.

## 5. B29 — add the boundary point explicitly, then test it by sprinkling

The `+1` in (3.1) resolves the `Z=0` logarithmic singularity, but it does not resolve the other boundary: a rare colourable graph can have exponentially many proper colourings. To expose that obstruction exactly, sprinkle `t` edges.

Let

\[
C_n:=\max_{n_1+n_2+n_3=n}\sum_{i<j}n_in_j=\left\lfloor\frac{n^2}{3}\right\rfloor.
\tag{5.1}
\]

For `m+t<=N`, define

\[
R_{n,m,t}:=
\frac{\binom{C_n-m}{t}}{\binom{N-m}{t}},
\tag{5.2}
\]

with the numerator interpreted as zero when `C_n-m<t`.

### Proposition 5.1 — exact colourability-sprinkling bound

Under the monotone coupling obtained by adding a uniformly random `t`-subset of the missing edges,

\[
\boxed{
\mathbb P(G_{n,m+t}\text{ is 3-colourable}\mid G_{n,m}=G)
\le \min\{1,Z(G)R_{n,m,t}\}.}
\tag{5.3}
\]

Consequently, for every `s>=0`,

\[
\boxed{
p_{m+t}
\le
\mathbb P\{Z_m>e^{sn}\}
+e^{sn}R_{n,m,t}\,p_m.}
\tag{5.4}
\]

If `p_m>0`, equivalently

\[
\boxed{
\frac{p_{m+t}}{p_m}
\le
\mathbb P\{\log Z_m>sn\mid Z_m>0\}
+e^{sn}R_{n,m,t}.}
\tag{5.5}
\]

#### Proof

Fix a proper colouring `sigma` of `G`, with class sizes `n_1,n_2,n_3`. At most `C_n` vertex pairs are bichromatic under `sigma`, and every existing edge of `G` is among them. Hence among the `N-m` missing edges, at most `C_n-m` may be added while preserving `sigma`. A uniformly random `t`-subset of missing edges preserves this fixed colouring with probability at most the hypergeometric ratio (5.2).

If the sprinkled graph is 3-colourable, at least one of the `Z(G)` original proper colourings survives. A union bound gives (5.3). Split its expectation according to `Z_m>e^{sn}` and `0<Z_m<=e^{sn}` to obtain (5.4); division by `p_m` yields (5.5). `square`

If `m=cn+o(n)` and `t=tau n+o(n)` for fixed `c,tau>0`, then every factor in the hypergeometric product has ratio `2/3+o(1)` uniformly over the `O(n)` sprinkled edges, so

\[
\frac1n\log R_{n,m,t}=\tau\log(2/3)+o(1).
\tag{5.6}
\]

Thus raw solution-count sprinkling would exponentially amplify a non-colourability probability across `tau n` extra edges if, conditional on colourability, the high-entropy tail above any `s<tau log(3/2)` were itself exponentially negligible.

### Why this does not close BGT Conjecture 1

Equation (5.5) is useful because it fails for a precise reason. Near the conjectured 3-colourability transition the raw number of colourings can remain exponentially large even when the relevant **number of clusters/covers** is small. Local recolourings and other internal cluster entropy make `Z_m` the wrong multiplicity to union-bound for arbitrarily small `tau`. Therefore a route that simply combines Friedgut sharpness with raw colouring-count sprinkling cannot prove BGT Conjecture 1 without an additional theorem suppressing or quotienting this internal entropy.

This is the main mathematical conclusion of B29: the missing boundary object is not merely `Z=0`; it is the quotient of the colour space by high-overlap clusters. That points directly toward the cover/whitening objects already used in rigorous upper-bound work, but with a new objective: prove an exponential **sprinkling survival** bound for cluster representatives rather than optimise another one-point ACG witness.

## 6. What the three moves accomplished

**B1 (change category).** The run moved from finite-support optimisation of `Sigma^*` to the exact BGT obstruction: exponential decay above the moving sharp-threshold sequence. This prevents wasting further runs on decimal polishing that cannot imply constant-location convergence.

**B11 (dualise).** Edge addition was dualised against the uniform measure on proper colourings. The collision statistic `q_e` yields the exact area inequality (4.2)--(4.3). Separately, rereading the ACG finite-temperature dual proof removes the previous artificial `+10^{-6}` endpoint slack and shows exponential non-colourability at every strict variational witness.

**B29 (add the points at infinity/boundary).** Replacing `log Z` by `log(1+Z)` handles the uncolourable boundary exactly. The sprinkling calculation then exposes the opposite boundary -- exponentially many highly correlated solutions -- and identifies cluster entropy rather than raw entropy as the next object that must be controlled.

The source conjecture remains OPEN. The fixed metric nevertheless moved because the existing exact variational witness applies at its own degree, not only at a strictly larger degree.

## 7. Next checkpoint

The next run should **not** return to B1/B11/B29. The most promising distinct triple is:

- **B3 — prove something stronger:** target an exponential sprinkling-survival inequality for a cluster/cover count, which would directly address the BGT strengthening rather than only w.h.p. non-colourability;
- **B18 — say it in another language:** rewrite clusters as minimal whitening/cover objects or as frozen-core messages and express sprinkling survival as a hitting problem on their forbidden-edge sets;
- **B20 — find why the algorithm fails:** construct the sharpest family showing why raw-colouring union bounds fail, then prove that quotienting by the resulting local moves removes exactly that obstruction.

A useful intermediate theorem would be a deterministic bound of the form

\[
\#\{\text{sprinkling-distinct colour clusters}\}
\le e^{o(n)}
\]

in the critical near-satisfiable window under source-valid hypotheses, or any weaker statement that makes the analogue of the first term in (5.5) exponentially small. No such claim is made here.

No Section-I trigger occurs because `W_3` moved this run.

## 8. Verification / artifact policy

No finite exhaustive claim was introduced this run. Propositions 4.1 and 5.1 are theorem-sized symbolic claims and their full proofs are on the page. Creating an arithmetic checker for identities such as `4.686514-4.03=0.656514` would violate the owner's 90/10 instruction by manufacturing a certificate with no mathematical value, so no new artifact file was created.

The exact finite witness used in (2.1) is inherited from the preceding run's executed `fractions.Fraction` checker and archived output, which ended `ALL_EXACT_CHECKS_PASS = True`. This run changes only the logical use of that already-certified strict negativity by reading the ACG proof at the same `d`.

## 9. Capability honesty

The actual runtime identifies the model as **GPT-5.6 Sol**. The reasoning-effort level is **UNVERIFIED**. I therefore do not claim GPT-6 maximum.

The exposed scheduler interface still offers title, prompt, schedule/timing and enabled state, but no model selector, no reasoning-effort selector and no guaranteed run duration. GPT-6 maximum remains request text only. A guaranteed change would require the platform to expose and honor model/reasoning fields for scheduled runs or authenticated runtime telemetry.

The policy record's earlier `You cannot modify this task` errors for P26/P01/P03 were context-specific. Current `RESULTS.md` says P26's full update later succeeded in another authorized context, while some other native IDs remain denied in the current context. The allowed remedy for any genuine permission failure is resolving task/account/workspace ownership in the authorized interface or platform support; creating a duplicate task or bypassing permissions is not an allowed workaround.

## 10. Ledger delta

```yaml
ledger_delta:
  track: HARD7-06
  target: F0095
  target_status: OPEN
  worker_status: PARTIAL
  metric: W_3 = U_3 - L_3
  before: 0.656515
  after: 0.656514
  L_3: 4.03
  U_3_before: 4.686515
  U_3_after: 4.686514
  reason_for_endpoint_move: strict ACG witness applies at the same d in the proof of Theorem 1.3
  new_route_1: exact truncated-entropy area inequality
  new_route_2: exact hypergeometric sprinkling survival bound
  source_alias_checked: Bayati-Gamarnik-Tetali Conjecture 1 (stronger route, not equivalent)
  closure: false
  new_exact_artifact: none warranted
  next_methods: [B3, B18, B20]
```

No shared root ledger was edited by this worker; this delta is for the designated reconciler.