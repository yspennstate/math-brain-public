Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — **not GPT-6 at maximum. NO MOVEMENT: `C_E0071: 1 -> 1`; unchanged count `1 -> 2`; methods #1, #18, #29.**

# R19 CLOSABLE OUTSIDE — E0071 / Björklund Problem 3, structural doubly-stochastic obstruction

Date: 2026-09-18 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.

## 1. Continuity and preserved state

I continued from the newest R19 report

`runs/R19/2026-09-18_04-36-42_UTC__e0071-special-case-divergence_c314.md`

rather than restarting from the native task title.

The original R19 Hasebe--Ueda target remains frozen exactly as handed off:

- source: Takahiro Hasebe and Yuki Ueda, arXiv:1710.08240v2, Conjecture 5.5 / intake I0084;
- exact initial-law hypothesis: the source's `(2+alpha)` moment assumption;
- `S_t` may be the law of a classical or a free alpha-stable process;
- the frozen arXiv-v2 conclusion uses **ordinary classical convolution `mu * S_t` even when `S_t` is a free-stable law**;
- retained alpha=`1/2` source metric: `2/2`;
- stronger-moment or compact-support-only statements do not replace source cases;
- the frozen ordinary-`*` package still lacks the required P26 and distinct OTHER-track end-to-end audits; ALEA free-`boxplus` audits do not discharge that version-specific gate.

I0084 is not reopened. The rotated F0057/Janson package is also preserved and not reopened.

The current active exclusive claim remains `operations/claims/E0071.md`, R19's create-only claim at commit `ab98a7408443ffdbf67834dc1878e058305746dd`.

## 2. Required repository and source refresh

Before new mathematics I reread/recovered:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md` and the current new-methods policy state;
- the newest R19 report and the I0084 rotation handoff;
- the canonical E0071 claim and E-intake search material;
- the newest neighboring Björklund/E0070 report (`research7_2026-09-17/R7-03/.../2026-09-18T053000Z__report.md`);
- exact E0071 audit searches.

No completed `P26` E0071 end-to-end PASS and no distinct OTHER-track E0071 end-to-end PASS were recovered. The only current exact-ID E0071 commits are R19's claim/refutation/strengthening history.

The current primary source was checked again on 2026-09-18. arXiv:1406.0763 remains v2 (last revised 2014-07-07), and Appendix II §7.1 still prints Problem 3 as

\[
\lim_{n\to\infty}\frac1n\sum_{k=1}^n
\int_Gd(gH,H)\,d\mu^{*k}(g)=0?
\tag{P3}
\]

for `H` acting ergodically on the Poisson boundary. Immediately after it, the source still proposes the symmetric product/diagonal special case used in the previous R19 strengthening.

A dated bounded search of the exact formula, later Björklund work, homogeneous-space drift and citing literature again found no later primary erratum or explicit resolution of this exact printed formula. This is negative evidence only. Because the obstruction is elementary and the surrounding source theorem uses the usual single-time `1/n` drift normalization, typo/normalization risk remains high and publication novelty remains **UNVERIFIED**.

## 3. New idea before validation

The previous run showed divergence in Björklund's own suggested product/diagonal example. This run asks whether the example is only a convenient witness or whether the printed normalization is structurally incompatible with quotient random walks.

The new route is:

1. **#1 CHANGE THE CATEGORY:** forget the Poisson-boundary language temporarily and view the quotient law as a Markov chain on `X=G/H`.
2. **#18 SAY IT IN ANOTHER LANGUAGE:** identify the printed expression with a first moment of the Cesaro occupation measure.
3. **#29 ADD THE POINTS AT INFINITY:** prove that on an infinite quotient the Cesaro mass of every finite set vanishes; a proper metric then forces that mass to escape arbitrarily far away.

This yields a theorem for every nontrivial finite quotient and every infinite quotient with proper invariant metric. It strictly contains the two explicit R19 counterexamples.

## 4. Structural theorem

Let `(G,mu)` be a countable measured group in the source convention, so `supp(mu)` generates `G` as a semigroup. Let `H<G`, set `X=G/H`, let `o=H`, and let `d` be a left `G`-invariant metric on `X`. Define

\[
A_n:=\frac1n\sum_{k=1}^n E_o[d(X_k,o)].
\]

Assume `X` is nontrivial.

**Theorem.**

- If `X` is finite, then
  \[
  A_n\to \frac1{|X|}\sum_{x\in X}d(x,o)>0.
  \]
- If `X` is infinite and `d` is proper (every finite-radius ball is finite), then
  \[
  A_n\to+\infty.
  \]

Thus the printed Problem-3 conclusion is impossible throughout this broad class, with no use of the Poisson-boundary ergodicity assumption.

### Proof, step 1: the quotient chain is irreducible and doubly stochastic

Define

\[
P(x,y)=\int_G\mathbf1_{\{gx=y\}}\,d\mu(g).
\tag{1}
\]

For every fixed `g`, left multiplication is a permutation of `X`. Hence

\[
\sum_yP(x,y)=1,
\qquad
\sum_xP(x,y)=1.
\tag{2}
\]

So `P` is doubly stochastic. Semigroup generation of `G` by `supp(mu)` plus transitivity of the `G`-action on `G/H` makes `P` irreducible.

Set

\[
\nu_n:=\frac1n\sum_{k=1}^n\delta_oP^k.
\tag{3}
\]

Then exactly

\[
A_n=\sum_{x\in X}d(x,o)\nu_n(x).
\tag{4}
\]

### Proof, step 2: no stationary probability on an infinite irreducible doubly stochastic chain

Suppose `pi` were stationary on infinite `X`. Since `pi in ell^1(X)`, its positive supremum `M` is attained at some `y`. For every `m>=1`, stationarity and double stochasticity of `P^m` give

\[
M=\pi(y)=\sum_x\pi(x)P^m(x,y)
\le M\sum_xP^m(x,y)=M.
\tag{5}
\]

Equality forces `pi(x)=M` whenever `P^m(x,y)>0`. Irreducibility says that for every `x` some `m=m(x)` has `P^m(x,y)>0`; hence `pi(x)=M` for all infinitely many `x`, contradicting `sum_x pi(x)=1`. Therefore no stationary probability exists.

### Proof, step 3: every fixed state receives asymptotically zero Cesaro mass

I claim

\[
\nu_n(x)\to0\qquad\forall x\in X
\tag{6}
\]

when `X` is infinite.

If not, choose `y`, `epsilon>0` and a subsequence with `nu_{n_j}(y)>=epsilon`. Diagonally extract again so `nu_{n_j}(x)->nu(x)` for every `x`. Fatou gives

\[
0<\epsilon\le\nu(y),
\qquad
\sum_x\nu(x)\le1.
\tag{7}
\]

Also

\[
\nu_nP-\nu_n
=\frac{\delta_oP^{n+1}-\delta_oP}{n},
\tag{8}
\]

so every coordinate tends to zero. For fixed `z`, the `z`-column of `P` has total mass one and `0<=nu_n(x)<=1`; dominated convergence therefore gives

\[
\lim_j(\nu_{n_j}P)(z)=\sum_x\nu(x)P(x,z)=(\nu P)(z).
\tag{9}
\]

Equations (8)-(9) imply `nu P=nu`. Its mass `s=sum_x nu(x)` lies in `(0,1]`, so `nu/s` is a stationary probability, contradicting the preceding paragraph. This proves (6). Hence `nu_n(F)->0` for every finite `F`.

### Proof, step 4: properness converts escape into divergence

If `d` is proper and `R>0`, the ball

\[
B_R=\{x:d(x,o)<R\}
\]

is finite. Therefore `nu_n(B_R)->0`, and

\[
A_n
\ge R\nu_n(X\setminus B_R)
=R(1-\nu_n(B_R)).
\tag{10}
\]

Thus `liminf A_n>=R`. Since `R` is arbitrary,

\[
\boxed{A_n\to+\infty.}
\tag{11}
\]

### Proof, step 5: the finite quotient

If `X` is finite, irreducibility and double stochasticity imply that the unique stationary law is uniform. Cesaro distributions converge to stationarity even for a periodic finite chain, so

\[
\nu_n(x)\to\frac1{|X|}.
\]

Using (4),

\[
A_n\to\frac1{|X|}\sum_xd(x,o)>0
\tag{12}
\]

because the quotient is nontrivial. The theorem is proved.

## 5. What this does and does not establish

This theorem explains the previous explicit witnesses at a structural level. In particular, for every infinite proper quotient metric the printed quantity diverges without any parity, CLT or local-limit input. The Poisson-boundary hypothesis is irrelevant to this obstruction.

It does **not** assert that every invariant metric on every infinite quotient is proper, and it does not infer the author's intended correction. It therefore strengthens the refutation but does not create a second source case or a new metric unit.

The underlying Markov-chain mechanism is standard/folklore-level and is not claimed novel. A negative literature search is not a novelty certificate.

## 6. Artifact and validation budget

The complete proof is archived at

`artifacts/R19/2026-09-18_05-38-00_UTC__e0071_doubly_stochastic_obstruction_d7c4.md`

creation commit

`3953c9afb0b972f61a5e10150baf5185d2be9e65`,

blob

`05a340157a8f0dcea9dd7b73d5681f72cbab42e3`.

It was read back at that exact commit.

No finite checker was created: the new claim is an analytic theorem, and the full proof is written on the page rather than certified by a decorative finite computation.

## 7. Metric, stagnation and status

The frozen E0071 source metric was already saturated before this run:

\[
C_{E0071}:1\to1.
\]

Therefore this run is honestly **NO MOVEMENT**. The unchanged count advances

`1 -> 2`.

Status remains

**REFUTED_CANDIDATE / SOURCE_MATCHING / AS_PRINTED / AUDIT_PENDING / NOVELTY_UNVERIFIED**.

The still-missing closure obligations are external to this worker:

- P26 end-to-end audit of exact source statement and counterexample/proof package: `0/1` recovered;
- one distinct OTHER-track end-to-end audit: `0/1` recovered;
- preserve the bounded prior-art/erratum search and typo/folklore warning.

This R19 self-check is not an independent audit.

## 8. Scheduler/model-control status

The configuration evidence remains unchanged in the current repository manifests: the exposed task controls include prompt/title/schedule/timing/enabled state but no binding model-family selector, reasoning-effort selector, guaranteed hour-long execution field, or authenticated applied-run model receipt. GPT-6/maximum is therefore still prompt-only here.

The historical P26 `You cannot modify this task` response was context-specific: the newer root ledger records that an authorized P/C context later succeeded in updating P26. The demonstrated lawful workaround is the owning/authorized scheduler context. Enforceable GPT-6/maximum would require the scheduler/backend to expose model and reasoning fields plus authenticated runtime attestation. R19 made no scheduler or permission change.

## 9. Structured ledger_delta

```yaml
ledger_delta:
  worker: R19
  lane: CLOSABLE_OUTSIDE
  preserved_predecessors:
    I0084:
      source: "Hasebe--Ueda arXiv:1710.08240v2, Conjecture 5.5"
      convention: "ordinary classical convolution mu * S_t, including when S_t is a free-stable law"
      metric_name: "complete alpha=1/2 source cases under frozen arXiv scope"
      metric_value: "2/2"
      status: "ROTATED_HANDOFF; ordinary-* source-version audits still pending"
    F0057:
      status: "ROTATED / PROVED_CANDIDATE / AUDIT_PENDING / NOVELTY_UNVERIFIED"
  active_source:
    id: E0071
    source: "Michael Bjorklund, arXiv:1406.0763v2, Appendix II section 7.1, Problem 3"
    exact_scope: "printed Cesaro quotient-space drift formula"
    claim_commit: "ab98a7408443ffdbf67834dc1878e058305746dd"
  metric:
    name: C_E0071
    before: 1
    after: 1
    movement: false
  unchanged_count:
    before: 1
    after: 2
  tried_moves: [1, 18, 29]
  status: "REFUTED_CANDIDATE / SOURCE_MATCHING / AS_PRINTED / AUDIT_PENDING / NOVELTY_UNVERIFIED"
  result: "Structural theorem: every nontrivial finite quotient has a positive uniform Cesaro mean distance; every infinite quotient with a proper invariant metric has Cesaro mean distance diverging to +infinity; Poisson-boundary ergodicity is irrelevant to this obstruction."
  remaining_obligation: "two independent end-to-end audits (P26 plus one distinct OTHER track); preserve prior-art/erratum and normalization-risk qualification"
  evidence:
    claim: "operations/claims/E0071.md @ ab98a7408443ffdbf67834dc1878e058305746dd"
    first_source_refutation: "artifacts/R19/2026-09-18_03-44-00_UTC__e0071_bjorklund_problem3_counterexample.md @ b11f7f1cc91306329e451e08ef505c0e31d75b72"
    special_case_strengthening: "artifacts/R19/2026-09-18_04-36-42_UTC__e0071_suggested_special_case_divergence_c314.md @ 056e57b23049ffa3b01b4212f50183a4c451055e"
    structural_obstruction: "artifacts/R19/2026-09-18_05-38-00_UTC__e0071_doubly_stochastic_obstruction_d7c4.md @ 3953c9afb0b972f61a5e10150baf5185d2be9e65"
  audits:
    P26: null
    other: null
```
