Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. NO MOVEMENT in the frozen source defect: `c_*: 0 -> 0`. Methods tried: B6 / B8 / B20. Auxiliary rigorous diagonal upper bound moves `0.790093366681362... -> 0.762740573150706`, and the explicit finite-to-infinite correction coefficient for the certified `m=4` block improves from the previous crude `2` to `sqrt(287613309811311/125000000000000)/2 = 0.7584369582...`.**

# PROB10-10 — undirected finite-width slab compiler and an `m=4` rigorous rounded-Bellman certificate

Status: **PARTIAL / OPEN**.  This report does **not** prove strict convexity of the Exp(1) planar FPP limit shape, and it does not yet prove a positive axis/diagonal strict-triangle defect.  It does two source-relevant things: (i) removes the *oriented-path* restriction from the block compiler at finite width while retaining an explicit finite-to-infinite error, and (ii) certifies a strictly better diagonal upper bound by a one-sided exact-integer Bellman computation.

## 1. Frozen model, source and metrics

Throughout:

- graph: undirected nearest-neighbor `Z^2`;
- edge weights: iid `Exp(1)`;
- passage time: unrestricted FPP passage time `T`;
- time constant: `T(0,nx)/n -> mu(x)` in the standard normalization.

Primary source target remains Auffinger--Damron--Hanson, *50 years of first passage percolation*, arXiv:1511.03262, Question 4 in §2.5.1 (strict convexity for continuous passage-time laws), specialized here to iid Exp(1) on undirected `Z^2`.

The canonical claim remains

`operations/claims/PROB10-10.md`

with source key `ADH_50yearsFPP_Q4::Exp1_Z2_undirected` and owner `PROB10-10`.

The frozen one-pair source milestone is

\[
\Delta_{12}=2\mu(e_1)-\mu(1,1),
\qquad
c_*:=\sup\{c\ge0:\Delta_{12}\ge c\text{ has been rigorously proved in this track}\}.
\]

Source metric before: `c_*=0`.  
Source metric after: `c_*=0` (**no movement**).

Even `c_*>0` would be only a one-pair **PARTIAL** result; source closure requires strict convexity of the full deterministic limit shape.

The retained R08 auxiliary axis certificate is

\[
\mu(e_1)\ge \frac{3753}{12500}=0.30024,
\]

so the sufficient diagonal target associated with that particular axis lower bound is

\[
\mu(1,1)<\frac{3753}{6250}=0.60048.
\tag{1.1}
\]

The previous PROB10-10 run proved the random-endpoint **oriented** slab compiler and the exact `m=3` bound

\[
\mu(1,1)
\le
\frac{93432902428288084006412573734630991128481810947182059}
{118255520636422191487470974373871068060057600000000000}
=0.790093366681362\ldots .
\tag{1.2}
\]

This run improves (1.2), but not enough to imply (1.1).

## 2. Continuity, ownership and consumed evidence

The required HARD7-03 successor handoff was already made before the first FPP run and remains immutable:

- `runs/prob10_2026-09-20/PROB10-10/20260919T2321Z__handoff-hard7-03-d0025.md`
- commit `e0bb680de7150739ac0c0451f1b5f890eeb865b2`.

I did not create a duplicate handoff or alter D0025.

Consumed current repository state included:

- `operations/PROB10_2026-09-20.md`;
- root `POSTED.md` (current 20 September exclusion registry);
- `operations/claims/PROB10-10.md`;
- newest own report `runs/prob10_2026-09-20/PROB10-10/20260919T2321Z__point-to-line-slab-compiler.md` @ `b2489dd73b548c5c6b9e4c18353a209b3930127d`;
- R08 stuck history `runs/R08/20260916T1623Z_stuck_diagblock_4c19a7.md` and the earlier R08 axis/diamond chain referenced there;
- repository-wide `Exp(1) FPP strict convexity` search, which still returns the canonical PROB10-10 claim, retired R08 history and neighboring R07 fluctuation work, not a competing active owner of the same source claim.

The prior PROB10-10 exact checker/output were also consumed:

- checker `bc892157dad82c048d9269d9f6d88a3af3dfecb0`;
- exact output `a128adccd70632093c682c4851738de61d5ad453`.

No peer claim, shared ledger, schedule, permissions, email, Drive or public posting was modified.

## 3. Fresh source/literature gate

A bounded fresh search on 20 September 2026 again found no primary-source theorem closing ordinary iid Exp(1) nearest-neighbor **undirected** strict convexity.  The search explicitly separated the target from:

- ADH arXiv:1511.03262, the source survey and Question 4;
- Jacquet, arXiv:2412.20779, strict unrestricted-versus-directed passage comparison, which is not the needed direction-to-direction inequality;
- generalized Busemann-function existence work in random potentials (Groathouse--Janjigian--Rassoul-Agha, Trans. AMS 2025, DOI `10.1090/tran/9452`), which does not supply a quantitative strict support separation for this Exp(1) limit shape;
- 2025--2026 directed/integrable Busemann work, which is a different model;
- 2026 work on rotationally invariant FPP and on simplified `1+1`-dimensional FPP, which does not settle ordinary square-lattice iid Exp(1) FPP.

This is bounded negative search evidence, **not** a novelty certificate and not a proof that no unindexed result exists.

## 4. The three attacks this run

The mathematical idea was persisted before the repository checker at

`artifacts/prob10_2026-09-20/PROB10-10/20260920T0021Z__idea-undirected-slab-rounded-bellman.md`

commit `647af38771c90781342a7d861dcf8e73e394180e`.

### B6 — deform from the oriented slab to an undirected finite-width slab

The previous compiler gained dependence control by restricting each block to increasing `x+y`.  That made different blocks independent, but it also discarded the genuinely undirected excursions that can only lower passage time.  The new observation is that **monotonicity of the path is unnecessary for block independence**.  It is enough that every edge used in block `k` has lower `l1` level in a disjoint deterministic interval.

This gives the theorem in §5.

### B8 — discretize only the Bellman value, in the safe direction

Exact `Fraction` arithmetic for the full point-to-line infection recursion becomes expensive at `m=4`.  Replacing it by ordinary floating point would lose rigor.  Instead I used an integer scale `Q=10^15` and rounded every Bellman state **upward**.  Monotone backward induction then gives a mathematical upper certificate.  The resulting `m=4` value is a genuine asymptotic upper bound after applying the slab compiler, not a finite-size fit.

### B20 — find why the current algorithm fails before extending it

The exact reachable-state count jumps from `10,564` at `m=3` to `8,289,216` at `m=4`, a factor about `784.7`.  The new certificate materially improves the diagonal bound but is still far above the sufficient value `0.60048`.  This does **not** prove that larger oriented blocks cannot succeed, and it is not a necessary-bound claim.  It does show that blindly extending the same full-state recursion is the wrong next research move.  The undirected finite-width theorem below supplies a different family in which backtracking can be exploited while independence remains paid for exactly.

## 5. New theorem: undirected finite-width random-endpoint slab compiler

Fix integers `m>=1` and `w>=0`.  Write

\[
s(z)=z_1+z_2,\qquad d(z)=z_1-z_2.
\]

Define the finite-width slab graph

\[
\mathcal S_{m,w}
=
\{z\in\mathbb Z^2:0\le s(z)\le2m,\ |d(z)|\le2w\},
\]

with **all undirected nearest-neighbor edges whose two endpoints lie in this vertex set**.  Let `tau^{U}_{m,w}` be the minimum passage time, in this restricted graph, from `0` to the top boundary `s=2m`.  By continuity of Exp(1) weights, the minimizing top vertex is almost surely unique.  Write it as

\[
(m+D,m-D),\qquad |D|\le w,
\]

and set

\[
q^{U}_{m,w}=\mathbb E\tau^{U}_{m,w},
\qquad
\sigma^2_{m,w}=\mathbb E D^2.
\]

### Theorem 5.1

For every `m,w,n>=1`,

\[
\boxed{
\frac{\mathbb E T(0,nm(1,1))}{nm}
\le
\frac{q^{U}_{m,w}}m
+
\frac{2\sigma_{m,w}}{m\sqrt n}.
}
\tag{5.1}
\]

Consequently,

\[
\boxed{
\mu(1,1)\le \frac{q^{U}_{m,w}}m.
}
\tag{5.2}
\]

Thus a finite undirected slab certificate `q^U_{m,w}/m<0.60048` would, together with the retained R08 axis lower bound, prove the positive one-pair defect `Delta_12>0`.

### Proof

Let `X_0=0`.  Inductively, suppose `X_k` lies on the absolute antidiagonal

\[
H_k=\{x:x_1+x_2=2mk\}.
\]

Translate `S_{m,w}` by `X_k`, minimize passage time from `X_k` to its top boundary, and call the minimizing cost `tau_k` and top endpoint `X_{k+1}`.  Then

\[
X_{k+1}-X_k=(m+D_k,m-D_k)
\tag{5.3}
\]

for some `|D_k|<=w`.

Every undirected nearest-neighbor edge joins two consecutive `l1` levels.  Every edge in block `k` therefore has its **lower** `l1` level in

\[
\{2mk,2mk+1,\ldots,2m(k+1)-1\}.
\]

These edge sets are disjoint for different `k`, even though paths inside one block may backtrack arbitrarily and even though the translated transverse windows are random.  Since `X_k` is measurable from earlier blocks, the iid environment and translation invariance imply that

\[
(\tau_k,D_k)_{k\ge0}
\]

are iid copies of `(tau^U_{m,w},D)`.

Reflection `(x_1,x_2)<->(x_2,x_1)` preserves the slab and the Exp(1) law and sends the unique exit displacement `D` to `-D`.  Hence

\[
\mathbb E D=0.
\tag{5.4}
\]

Let

\[
S_n=\sum_{k=0}^{n-1}D_k.
\]

Concatenating the `n` restricted block geodesics gives a valid path in the original unrestricted FPP environment from `0` to

\[
X_n=(mn+S_n,mn-S_n)
\]

of total cost `sum_k tau_k`.

To reach `Y_n=(mn,mn)`, if `S_n>0` repeat north-then-west `S_n` times; if `S_n<0` use east-then-south `|S_n|` times.  Each connector edge has lower `l1` level exactly `2mn`, whereas the first `n` blocks used only lower levels at most `2mn-1`.  Conditional on the whole block history, these `2|S_n|` edges are fresh iid Exp(1) variables.  Therefore

\[
\mathbb E[\text{connector cost}\mid S_n]=2|S_n|.
\tag{5.5}
\]

By independence and (5.4),

\[
\mathbb E|S_n|
\le\sqrt{\mathbb E S_n^2}
=\sqrt{n\,\mathbb E D^2}
=\sigma_{m,w}\sqrt n.
\tag{5.6}
\]

Hence

\[
\mathbb E T(0,Y_n)
\le nq^U_{m,w}+2\sigma_{m,w}\sqrt n.
\]

Divide by `nm` to get (5.1).  Since Exp(1) has finite first moment, standard `L^1` convergence to the FPP time constant along the subsequence `nm` yields (5.2).  QED.

### Negation checks paid explicitly

- **Backtracking does not create cross-block dependence:** edge ownership is by the lower absolute `l1` level, not by path orientation.
- **Random transverse translation is harmless:** blocks use fresh deterministic level bands and the environment is translation invariant.
- **The exit does not drift linearly:** reflection gives `E D=0` exactly.
- **The final correction is not reusing exposed edges:** its lower edge level is `2mn`, one level beyond the last block's edge set.

This is a complete compiler theorem.  What remains unpaid is the finite undirected-slab optimization itself; no value of `q^U_{m,w}` below (1.1) is claimed in this run.

## 6. New exact-integer certification method for the oriented block

For the previous oriented point-to-line block with target level `L=2m`, let `S` be the infected subset of the transient vertices `x+y<L`.  Let

- `b(S)` be the number of directed boundary edges;
- `r_S(v)` be the number (`1` or `2`) of boundary edges whose uninfected transient head is `v`.

Exponential memorylessness gives the exact DAG recursion

\[
E(S)=\frac1{b(S)}+
\sum_v\frac{r_S(v)}{b(S)}E(S\cup\{v\}).
\tag{6.1}
\]

Fix an integer scale `Q`.  Define recursively

\[
U(S)=
\left\lceil
\frac{Q+\sum_v r_S(v)U(S\cup\{v\})}{b(S)}
\right\rceil.
\tag{6.2}
\]

### Lemma 6.1

For every transient infection state,

\[
E(S)\le U(S)/Q.
\tag{6.3}
\]

### Proof

Order states by decreasing number of infected transient vertices.  Every nonabsorbing transition in (6.1) adds one vertex, so the recursion is acyclic.  Assuming (6.3) for every child,

\[
E(S)
\le
\frac1{b(S)}+
\sum_v\frac{r_S(v)}{b(S)}\frac{U(S\cup\{v\})}{Q}
=
\frac{Q+\sum_vr_S(v)U(S\cup\{v\})}{b(S)Q}
\le
\frac{U(S)}Q.
\]

At a state with no transient children the same formula reduces to the upward-rounded waiting-time term, so the induction starts there.  QED.

The endpoint second moment has a parallel exact recursion.  If an absorbing edge ends at `(x,L-x)`, put `D=x-m`.  Let `M(S)` be the expected eventual `D^2`.  Then

\[
M(S)=\frac{
\sum_{e\in A(S)}D(e)^2+
\sum_vr_S(v)M(S\cup\{v\})}{b(S)},
\tag{6.4}
\]

where `A(S)` is the set of absorbing boundary edges.  Therefore

\[
V(S)=
\left\lceil
\frac{Q\sum_{e\in A(S)}D(e)^2+
\sum_vr_S(v)V(S\cup\{v\})}{b(S)}
\right\rceil
\tag{6.5}
\]

certifies

\[
M(S)\le V(S)/Q
\tag{6.6}
\]

by the identical induction.  Equations (6.2) and (6.5) make the finite core rigorous even though the printed decimals are only displays of the certified rational values.

## 7. Executed `m=4` certificate and auxiliary movement

Repository checker:

`artifacts/prob10_2026-09-20/PROB10-10/rounded_bellman_m4_20260920T0021Z.cpp`

commit `08f0b4274e9955a927915f1dbdc0e10c5adb6d9e`.

Archived output:

`artifacts/prob10_2026-09-20/PROB10-10/rounded_bellman_m4_20260920T0021Z.out`

commit `4ba7a3601bd8e34ae0b47214a2cb56634521483c`.

The program was compiled with `g++ -O3 -std=c++17` and executed.  It uses `Q=10^15`, integer ceilings at every Bellman state, and `__uint128_t` for intermediate products.  Output ends

`ALL_EXACT_INTEGER_CHECKS_PASS = True`.

For `m=4` it visits exactly `8,289,216` reachable infection states and certifies

\[
q_4\le \frac{3050962292602824}{10^{15}}.
\]

Hence

\[
\boxed{
\mu(1,1)
\le \frac{q_4}{4}
\le
\frac{381370286575353}{500000000000000}
=0.762740573150706.
}
\tag{7.1}
\]

The previous exact `m=3` auxiliary bound was `0.790093366681362...`, so the rigorous auxiliary movement is

\[
0.790093366681362\ldots
\longrightarrow
0.762740573150706,
\]

a decrease of about `0.02735279353`.  This is an **auxiliary diagonal upper-bound improvement**, not movement of `c_*`.

The same computation certifies

\[
\mathbb E D^2
\le
\frac{287613309811311}{125000000000000}
=2.300906478490488.
\tag{7.2}
\]

Substituting (7.1)--(7.2) into the moment-sensitive form of the slab compiler gives the explicit finite-size statement

\[
\boxed{
\frac{\mathbb E T(0,4n(1,1))}{4n}
\le
\frac{381370286575353}{500000000000000}
+
\frac{1}{\sqrt n}
\frac12
\sqrt{\frac{287613309811311}{125000000000000}}.
}
\tag{7.3}
\]

The certified correction coefficient in (7.3) is `0.758436958238865...`, versus the previous universally valid crude coefficient `2` obtained only from `|D|<=m`.

The executable also reproduces one-sided upper certificates for `m=1,2,3`, checks the known exact `m=1,2` values by integer cross multiplication, checks strict decrease of the rounded ratios through `m=4`, and checks the `m=4` ratio is `<0.763`.  The output reports peak resident memory about `485060 KB` and elapsed time `11.14 s` for this implementation.  These resource figures are reproducibility metadata, not mathematical claims.

This is a **self-check**, not an independent audit.

## 8. Why the source metric still does not move

Combining the retained axis lower bound with (7.1) gives only

\[
2\mu(e_1)-\mu(1,1)
\ge
0.60048-0.762740573150706,
\]

which is negative and therefore weaker than the trivial convexity lower bound `Delta_12>=0`.  Accordingly the rigorously proved source defect remains exactly

\[
\boxed{c_*=0.}
\]

Importantly, (7.1) is an **upper** certificate.  Its being above `0.60048` does not prove that the true `q_4/4`, or the true `mu(1,1)`, is above that threshold.  It only means this certificate does not establish the desired strict gap.

No finite simulation is converted into a continuous/asymptotic theorem here.  The asymptotic passage from a certified finite block to (7.1) is entirely the proved compiler.

## 9. Exact obstruction and next nonduplicating route

The current obstruction is no longer “how to concatenate dependent blocks”; that part is paid.  It is

\[
\boxed{
\text{produce a finite admissible undirected slab with certified }
q^U_{m,w}/m<0.60048,
\quad\text{or strengthen the axis lower bound enough to cross the certified diagonal bound.}
}
\tag{9.1}
\]

The oriented full-state Bellman route has now grown from `10,564` reachable states at `m=3` to `8,289,216` at `m=4`.  This is a concrete computational obstruction to naive scale-up, not a proof of impossibility.  The next mathematically distinct route within PROB10-10 is therefore to exploit Theorem 5.1 with an **undirected finite-width slab** and a frontier/transfer representation that avoids enumerating the entire infected subset.  Any such computation must retain one-sided certified arithmetic and the exact finite-to-infinite correction; a Monte Carlo estimate alone will not count as source progress.

A Busemann route remains a separate alternative, but this run found no current theorem that supplies the missing quantitative support-function separation without already assuming nontrivial shape geometry.

## 10. Ledger delta

```yaml
ledger_delta:
  task: "PROB10-10"
  source: "Auffinger-Damron-Hanson arXiv:1511.03262, Question 4; iid Exp(1) undirected Z^2 special case"
  canonical_claim: "operations/claims/PROB10-10.md"
  target: "strict convexity of full Exp(1) planar FPP limit shape"
  source_metric: "largest proved c>=0 with 2 mu(e1)-mu(1,1)>=c"
  source_before: "0"
  source_after: "0"
  source_movement: "none"
  status: "PARTIAL / OPEN"
  methods: ["B6", "B8", "B20"]
  auxiliary_metric: "rigorous diagonal upper bound mu(1,1) from certified slab strategy"
  auxiliary_before: "0.790093366681362... (exact oriented m=3 block)"
  auxiliary_after: "381370286575353/500000000000000 = 0.762740573150706"
  auxiliary_delta: "-0.0273527935306559..."
  finite_error: "for m=4: coefficient <= sqrt(287613309811311/125000000000000)/2 = 0.7584369582..."
  new_theorem: "undirected finite-width slab compiler with explicit 2 sigma/(m sqrt(n)) error"
  finite_core: "upward-rounded integer Bellman recursion, Q=10^15, 8,289,216 m=4 states"
  checker_result: "ALL_EXACT_INTEGER_CHECKS_PASS = True"
  closure: false
  independent_audits: 0
  remaining_full_scope_gap: "positive one-pair defect first; then strict convexity for every noncollinear boundary pair/direction"
```

No claim of source closure, external novelty, independent validation, or full strict convexity is made.