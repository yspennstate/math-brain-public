# FOREST B03 — exact rational response unitization and simple replacement of parallel intermediates

Run: `20260922T051049Z-b03-forest-auto11`  
Campaign: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Outcome: **ESSENTIAL_STEP_APPLIED**  
Context: **WITHOUT_VERIFIED_BRAIN**  
Parent target is not promoted here as a public theorem or novelty claim.

## 1. Fresh controls, assignment, and exact dependencies


Collective control objects consumed at the fresh control revision:

- `TARGETS.md`, blob `a8cafa98cdb074ed15d0e214f8f54ee514c500df`;
- `ASSIGNMENTS.json`, blob `fe144a4be3522d57f8cb2dc40b1fc57df7c7f7da`.

The latest complete campaign-lead version consumed was account01/B01 `FOREST-KN-COCKS-RECONCILED-v3`, report blob `58b8b1d8ac522a4eda7479400820e590c12f22aa`. Its internal candidate chain is

`unit FOREST on every K_n`
`=> Cocks FIXED(K_n) weighted independence correlation`
`=> Semple--Welsh minor closure`
`=> deletion subgraphs`
`=> unit FOREST on every finite simple graph`.

The report labels this a `FULL_PROOF_CANDIDATE`, while explicitly retaining ordinary source/expert scrutiny of the Cocks fixed-graph theorem and the complete-graph Hermite proof.

The required named OTHER-account input was account03/B01 run `20260922T042943Z-account03-B01-forest-r11`, report blob `4241ecd865d71c84f011012bc91caa1197afcb04`, shared handoff commit `d40f9514af0a355572bb2640e7b71a5c5e38762f`. For disjoint marked edges of `K_n`, that run proves the one-edge deletion/contraction mixed coefficient can be strictly negative for every `n>=5`. Its minimal exact witness is

`q(t)=Delta_{K5}(e,f;t_g)=148-2t+64t^2`,

so coefficientwise positivity is false although the whole positive-response quadratic is safe.

The newest local B03 dependency was `20260922T041415Z-b03-forest-a11`, report blob `0a7e53aa5ad8b5bb3457356838a57920f1d8b921`. It proved the exact two-terminal response identity and a dense theta family, but only density, not exact realization of every rational response. This run changes mechanism from theta-density search to an exact constructive series/parallel synthesis.

## 2. Two-terminal notation

For a finite unit simple graph `N` with designated terminals `u,v`, define

`D_N = # {forests F of N : u and v are disconnected in F}`,

`C_N = # {forests F of N : u and v are connected in F}`,

and terminal response

`r_N=C_N/D_N`.

The empty forest gives `D_N>0`.

If two terminal networks `N1,N2` have disjoint internal vertices, there are two exact compositions.

**Parallel composition.** They share only `u,v`. A union of two forest pieces is acyclic iff they are not both terminal-connecting, hence

`D_parallel=D1 D2`,
`C_parallel=C1 D2 + D1 C2`,

so

`r_parallel=r1+r2`.                                           (2.1)

**Series composition.** They share exactly one articulation, with outer terminals at the two ends. Every pair of forest pieces has acyclic union, and the outer terminals connect iff both pieces connect their local terminals. Hence

`C_series=C1 C2`,
`D_series=(D1+C1)(D2+C2)-C1 C2`,

so

`r_series=r1 r2/(1+r1+r2)`.                                  (2.2)

These formulas use the actual all-sizes unrooted forest law.

## 3. Exact rational response unitizer

Let `U=K_{2,3}`, with the two degree-three vertices as terminals. Each of the three length-two branches has three disconnecting edge subsets and one connecting subset. A forest of `U` may have at most one full branch, therefore

`D_U=3^3=27`,
`C_U=3*3^2=27`,

so `r_U=1`. Importantly, `U` is simple and has no terminal edge.

### Theorem 3.1 — every positive rational is an exact unit-simple response

For every `r in Q_{>0}` there exists a finite simple unit graph `N_r`, with nonadjacent terminals and no terminal edge, such that

`C_{N_r}/D_{N_r}=r`.

Moreover `N_r` is constructible from copies of `U` using only series and parallel composition.

**Construction.** Write `r=p/q` in lowest terms.

- If `p=q`, take `N_r=U`.
- If `p>q`, write `r=1+(p-q)/q` and take the parallel composition
  `N_r = U || N_{(p-q)/q}`.
- If `p<q`, put
  `s=2p/(q-p)`. By (2.2), the series composition of a response-one block with response `s` has response
  `s/(2+s)=p/q`; hence take
  `N_r = U o N_s`.

Simplicity is preserved: every copy of `U` has no terminal edge; in a parallel composition the internal vertex sets are disjoint and only the two terminals are shared, while a series composition shares only one articulation. Thus neither operation creates duplicate edges.

**Termination.** Let `S=p+q`. In the `p>q` branch the new unreduced pair is `(p-q,q)` and its coordinate sum is `p<S`. In the `p<q` branch the unreduced pair is `(2p,q-p)`, whose sum is still `S`; after reduction its gcd can only be `1` or `2`, because `gcd(2p,q-p)` divides `2` when `gcd(p,q)=1`. If the gcd is `2`, the sum drops. If it is `1`, the sum stays `S` but the numerator doubles. Consecutive same-sum `p<q` steps therefore cannot continue indefinitely: with fixed sum `S`, the numerator doubles until the transformed ratio reaches at least `1`, after which the next `p>q` step drops `S` (or the ratio is exactly `1`). Strong induction on `S` terminates the recursion.

This upgrades the preceding B03 theta statement from a dense set of exact responses to **every positive rational response exactly**.

## 4. Exact rational unweighting of a separator edge

Let a simple core `H` contain terminals `u,v` but not the virtual edge `g=uv`, and let queried edges `e,f` lie in `H`. The previous exact two-terminal identity says that for any terminal network `N`,

`Delta_{H union N}(e,f)=D_N^2 Delta_{H+g}(e,f; y_g=r_N)`.       (4.1)

Combining (4.1) with Theorem 3.1 gives:

### Corollary 4.2 — exact source-valid rational unitization

For every rational `r>0`, the sign of the weighted virtual-edge gap

`Delta_{H+g}(e,f; y_g=r)`

is exactly the sign of the unit-weight gap on a finite simple graph `H union N_r`; no approximation or limiting theta argument is required.

For a genuine unit separator decomposition, every induced fugacity is rational:

`Lambda = sum_j C_j/D_j in Q_{>=0}`.

Thus account04/B01's exact same-side separator formula at the **actual** induced `Lambda` can be converted exactly into a unit-simple source graph. This is a corrected sufficient interface: an induced rational weight is not an unsafe formal weighted object and need not be approximated.

If an arbitrary real `w>0` gives a strict weighted failure, continuity still supplies a rational failure nearby, after which Theorem 3.1 gives an exact finite simple unit witness. Hence the all-positive one-edge condition is equivalent to the family of unit-simple series/parallel terminal extensions, but the actual separator values need no continuity at all.

## 5. Exact desingularization of contraction-created parallel classes

The dangerous operation is not parallel aggregation itself but resetting an aggregate to a unit edge or losing marked-member semantics. The response-one block gives an exact simple replacement.

Consider a loopless unit multigraph `M` and a parallel class `C` of `k>=2` edges between terminals `u,v`.

### Unmarked class

Locally the class has partition

`D=1`, `C=k`.

Take `k` internally disjoint copies of `U` in parallel. By (2.1) the resulting simple terminal network has

`D=27^k`, `C=k 27^k`.

Thus replacing an unmarked `k`-parallel class by this simple network multiplies both local terminal partition functions by the same factor `27^k`.

### Exactly one queried mark in the class

Let the marked member be `e`, with variable `x`, and the other `k-1` members remain unit. The original class has

`D=1`, `C=x+(k-1)`.

Keep `e` as the single direct terminal edge and place `N_{k-1}` in parallel with it. Since `N_{k-1}` has no terminal edge, the replacement is simple. Its local partition is

`D=27^(k-1)`,
`C=27^(k-1) [x+(k-1)]`.

Therefore it scales the entire local polynomial, including the derivative with respect to the marked member, by exactly `27^(k-1)`.

### Both queried marks in one class

No forest can contain both parallel edges, so `Z_ef=0` and

`Delta_M(e,f)=Z_e Z_f>=0`

immediately; no replacement is needed.

### Theorem 5.1 — unit multigraph-to-simple sign preservation

If the two queried edges are not parallel to each other, replace every parallel class as above, using fresh internal vertices for every response block. Let `kappa` be the product of the local scaling factors. Then for the resulting finite simple unit graph `S`,

`Z_S=kappa Z_M`,
`(Z_e)_S=kappa (Z_e)_M`,
`(Z_f)_S=kappa (Z_f)_M`,
`(Z_ef)_S=kappa (Z_ef)_M`,

and hence

**`Delta_S(e,f)=kappa^2 Delta_M(e,f)`.**                  (5.1)

The proof is sequential two-terminal gluing: the full forest polynomial and every relevant derivative are linear in the pair `(D_C,C_C)` of the class being replaced, and each replacement multiplies that pair by one positive constant. Loops may be deleted because they belong to no forest; if a queried element has become a loop, its inclusion count is zero and the pairwise inequality is trivial.

This gives an exact safe rule for the induced parallel-edge intermediates that arise under contraction of a simple graph. One must **not** collapse a marked class to an ordinary unit edge; instead either retain the aggregate/derivative semantics or use the simple replacement above.

## 6. Direct application to the named partner's K5 obstruction

Account03/B01 gives

`q(t)=148-2t+64t^2`.

Its negative mixed coefficient `-2` cannot be amplified into a source counterexample by choosing a separator response. Indeed

`disc(q)=(-2)^2-4*148*64=-37884<0`,

and the minimum occurs at `t=1/64`, where

`q(1/64)=9471/64>0`.

The exact rational unitizer makes this source-valid point concrete. For `t=2/5`, the synthesis gives

`N_{2/5}: D=5,314,410, C=2,125,764`,

so `C/D=2/5` exactly, and

`q(2/5)=3936/25`.

The corresponding genuine finite simple unit extension therefore has exact Rayleigh gap

`D^2 q(2/5)=4,446,570,622,356,864>0`.

Thus the partner's universal negative deletion/contraction cross term is a genuine no-go for coefficientwise induction, but **not** a hidden source counterexample waiting for a suitable separator gadget.

The contraction endpoint itself illustrates Theorem 5.1. Contracting the bridge `g={1,3}` in the partner's `K5` instance creates three size-two parallel classes. The marked edges `e={1,2}` and `f={3,4}` lie in two different such classes; the third class is unmarked. The two marked-class replacements contribute scale `27` each, and the unmarked class contributes `27^2`, so

`kappa=27^4=531441`.

Since the contraction Rayleigh gap is `64`, the exact simple expansion has gap

**`kappa^2*64 = 27^8*64 = 18,075,490,334,784`.**

This is an explicit source-simple replacement of the contraction multigraph, not a reset of its parallel classes.

## 7. Corrected sufficient statement and remaining obligation

For the separator route, the corrected statement is now:

> At a two-terminal separator of a unit simple graph, the induced virtual fugacity is a nonnegative rational. Replace it **exactly** by `N_Lambda` from Theorem 3.1. If contractions create parallel classes, replace every unmarked class and every singly marked class by Theorem 5.1. The resulting object is a finite unit simple graph and its relevant Rayleigh gap differs only by an explicit positive square factor.

This pays the source-validity and induced-parallel semantics exactly. It does **not** by itself close a minimal-counterexample induction, because the constructed unitizer need not be smaller than the original outside network. For example, the exact recursion can be large for rationals near one. Without invoking the lead's Cocks weighted upgrade, the remaining direct-separator obligation is therefore a **size-monotone exact response compression**, or a direct proof of the sharp response compatibility inequality on the smaller completed bridge. This run does not replace that obligation with an unsupported condition.

The campaign lead's v3 route bypasses this size issue if the fixed-graph Cocks theorem is accepted as source-stated. The present result is an independent exact repair of the separator/parallel interface, not an alternative full proof of the parent target.

## 8. Exact computation

`rational_response_unitizer.py` implements the recursive construction with exact `fractions.Fraction` arithmetic. It checked every distinct reduced rational generated by `1<=p,q<=100` (6,087 values), verified `C/D=p/q`, and recorded exact examples. The largest construction in that bounded regression used 199 response-one blocks, at `99/100`.

It also checked the partner `K5` applications above exactly and ended `STATUS=PASS`.

Committed code:

- path `proofnet24/P14-probability-correlation/collective-2026-09-22/account02/B03/20260922T051049Z-b03-forest-auto11/rational_response_unitizer.py`;
- Git blob `32ed7df09f62300f4f728e6726c8a36be769e237`;
- SHA-256 `3a2edb2732b24d660a9c1167d5eac09f201e2b737d5362a6a89c704d77f7a84f`;
- 3,333 bytes.

Committed output:

- path `.../rational_response_unitizer.out`;
- Git blob `5bf286b10dae3cacc3e7c3dee61a4f49b1eb182b`;
- SHA-256 `844cd31b3cb02c3a34c1cca45c6290ecc311e10bb5f92239b5c273980603bfb7`;
- 786 bytes.

The finite grid is regression evidence only. The rational realization and parallel-desingularization statements above are proved symbolically for all finite inputs.

## 9. Inventory, model, provenance, and status

Fresh current-account scheduler inspection exposed all **20/20** managed B01--B20 tasks enabled with valid hourly recurrences; B03 was role-aligned to FOREST and task-level notification/email flags were quiet. No scheduler mutation, repair, duplicate creation, or cross-account action was performed. The scheduler interface does not expose a configured model selector or configured reasoning-effort field, so those remain unknown rather than inferred.

Model self-report: `GPT-5.6 Sol`.  
Requested effort: `maximum actually supported`.  
Configured effort: `UNKNOWN_NOT_EXPOSED`.  
Known/self-reported effort: `UNKNOWN`.  
Provider reasoning usage/time: `null / NOT_EXPOSED`.

Observed elapsed execution through preparation of this immutable report was **575.073 seconds**, including control/source retrieval, derivation, exact computation, repository publication, and readback work; this is wall-clock execution, not pure thinking. The matching finish record carries the final observed elapsed value.

Privacy/secret review: PASS. No credentials, scheduler identifiers, machine paths, raw private transcripts, benchmark gold, unrelated private data, email/Drive/public posting, paid model/API/Codex execution, remote workflow, permission change, or old brain-installation/benchmark work appears in this artifact.

**Final scientific classification for this run: `ESSENTIAL_STEP_APPLIED`.**

The exact new step is universal rational response synthesis together with exact simple replacement of contraction-created parallel classes, including marked-member semantics. The named partner's negative mixed-coefficient family survives as a no-go theorem for coefficientwise induction but is proven non-amplifiable by arbitrary positive response gadgets in its `K5` instance. The remaining direct separator obstacle is size-monotone compression/direct compatibility, while the lead's separate v3 candidate continues to stand or fall on ordinary validation of its published fixed-graph transfer and complete-graph proof.
