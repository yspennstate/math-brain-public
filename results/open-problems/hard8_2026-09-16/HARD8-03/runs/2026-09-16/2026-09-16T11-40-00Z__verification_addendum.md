# HARD8-03 — verification and strengthening addendum for 2026-09-16T11:18:00Z

This append-only companion records exact GitHub receipts, the completed finite verifier, and one further theorem proved after publication of the primary report.

## 1. Publication/readback receipts

### Mathematical report

- Path: `hard8_2026-09-16/HARD8-03/runs/2026-09-16/2026-09-16T11-18-00Z__report.md`
- Creation commit: `33c8689cfa17473b9bf976f87087536eb851c8eb`
- Exact-commit readback: **VERIFIED**.
- Blob SHA: `d37699148f667a6b7d5db3c1ac7595a1eef590a8`.

### Exact nullity-two verifier

- Path: `hard8_2026-09-16/HARD8-03/artifacts/2026-09-16T11-18-00Z__nullity2_profile_verifier.py`
- Creation commit: `cd58278319b9b31c4659049b3ff12b4ebcea64fa`
- Exact-commit readback: **VERIFIED**.
- Blob SHA: `b5404e64d542334f4dfba1e6d96ca23d42e5a105`.

### Exact verifier output

- Path: `hard8_2026-09-16/HARD8-03/artifacts/2026-09-16T11-18-00Z__nullity2_profile_output.txt`
- Creation commit: `00b48040e6e351f1aa546b6df1b1afc127de0a6d`
- Exact-commit readback: **VERIFIED**.
- Blob SHA: `23324437e722050cb63bbf60bd89c3ea7d5a5b7e`.

No previous report/artifact, peer file, shared index, workflow, branch setting, or access rule was modified.

## 2. Actual exact verifier execution

The archived verifier was executed before publication of its output using only the Python standard library, integer arithmetic, and `fractions.Fraction`. It uses no floating-point acceptance criterion, no randomness, no external solver, and no timeout inference.

It exhaustively enumerated every set of distinct nonzero Boolean columns in ambient dimensions `1,2,3,4` having real nullity exactly two. The counts were:

- dimension 1: `0`;
- dimension 2: `0`;
- dimension 3: `21`;
- dimension 4: `5160`;
- total: **5181** configurations.

For each configuration it independently enumerated all maximal dissociated subsets, all `{-1,0,1}` representations needed to compute exact negative widths, and the whole optimized profile `rho_V(k)` through its vanishing range.

The completed run reported:

- **36,269** maximal-set omission checks;
- **17,489** exact profile-inequality checks;
- **5,181** checks of the support-minimal-relation construction used in Theorem 5.1;
- at most `12` maximal dissociated subsets in any one enumerated configuration;
- `10` distinct profile shapes;
- maximum observed finite ratio `((k+1)rho)/r = 1/2` in this small census;
- terminal status `ALL_CHECKS_PASSED`.

The `1/2` is only a finite observation; the theorem proved in the report is the universal constant-1 inequality for real nullity at most two. No stronger universal constant is claimed.

## 3. Strengthening: signed-relation rank controls the number of omissions

The report bounded the number of omitted columns of a maximal dissociated set by the **real nullity**. There is a sharper intrinsic parameter.

Let

`K_pm(V) = { c in {-1,0,1}^V : sum_{v in V} c_v v = 0 }`

and define the **signed-relation rank**

`sigma(V) = dim_R span_R K_pm(V)`.

Clearly `sigma(V) <= |V|-rank(V)`, because all signed relations lie in the ordinary real kernel.

### Theorem 3.1 (fundamental signed relations are independent)

For every maximal dissociated set `S subset V`, writing `T=V\S`,

`|T| <= sigma(V)`.

Consequently, for every threshold `k`,

`rho_V(k) <= sigma(V)`.                                             `(3.1)`

#### Proof

Fix `t in T`. Maximality of `S` says `S union {t}` is not dissociated, so there is a nonzero signed relation supported on `S union {t}`. Because `S` itself is dissociated, the coefficient of `t` in this relation is nonzero; multiply by `-1` if necessary so that the coefficient at `t` is `+1`. Call the resulting relation vector `c^(t)`.

By construction, on the omitted-coordinate set `T`, the vector `c^(t)` has coordinate `1` at `t` and coordinate `0` at every `u in T\{t}`, since the relation is supported on `S union {t}`. Thus the restrictions

`c^(t)|_T`, `t in T`,

are the standard coordinate vectors of `R^T`. Therefore the signed relation vectors `{c^(t):t in T}` are linearly independent. They all lie in `span_R K_pm(V)`, so

`|T| <= sigma(V)`.

Every heavy column lies outside `S`; hence its rank is at most its cardinality, which is at most `|T|<=sigma(V)`. Minimizing over maximal `S` proves `(3.1)`. QED.

### Corollary 3.2 (new necessary condition for a profile counterexample)

Any finite configuration violating

`(k+1)rho_V(k) <= r`

must satisfy

`sigma(V) > r/(k+1)`.

This is strictly sharper than the corresponding necessary condition stated only in terms of real nullity whenever the ordinary kernel contains many real directions but few signed directions.

The theorem also identifies the canonical independent relations attached to a maximal dissociated set: each omitted column supplies a fundamental signed relation whose restriction to the omitted coordinates is a distinct unit vector. This is likely a better object for the next exchange argument than arbitrary real-kernel nullity.

## 4. Relation to known additive-combinatorics structure

Maximal dissociated subsets and their `{-1,0,1}` spanning property are classical additive-combinatorics objects. A relevant primary reference is:

- V. F. Lev and R. Yuster, *On the Size of Dissociated Bases*, Electronic Journal of Combinatorics 18 (2011), P117, DOI `10.37236/604`, arXiv:1005.0155.

That work proves, among other things, that maximal dissociated subsets of a finite set can differ in size by a logarithmic factor and that the Boolean cube contains dissociated subsets of order `n log n`. This is a warning against trying to replace the profile problem by a crude cardinality-vs-real-rank estimate: large dissociated sets are genuinely possible. The signed-relation-rank theorem above avoids that issue by counting only relations that actually obstruct dissociation.

## 5. Bounded failed optional computation

After the successful primary verifier, a broader optional census intended to enumerate signed-relation ranks over all small configurations was attempted in the bounded container runtime. Two implementations exceeded the allotted execution window (the second after a subset-sum optimization). No claim in this report or addendum depends on that timed-out census, and no nonexistence or universal inference is drawn from the timeout. The successful nullity-two verifier/output above are the only computational evidence used for the main theorem.

## 6. Updated next attack

The most precise next structural target is now a **signed-rank-aware nullity-three theorem**. For a maximal dissociated `S`, the fundamental signed relations of omitted columns form an independent family. To extend `(P_k)` past real nullity two, one needs to exploit the fact that each heavy fundamental relation has more than `k` negative coefficients while these relations are simultaneously independent and have identity restriction on the omitted coordinates.

A useful candidate lemma would bound the rank of the targets of such a family directly from the number of negative coefficients, rather than from the raw real nullity. The equal-sum-block examples from earlier checkpoints remain the calibration family and show that any universal proof must allow near-Markov `1/(k+1)` behavior.

## 7. Review status

The full deterministic log-rank conjecture remains open. The universal profile inequality `(P_k)` remains open for general configurations. The nullity-two theorem and signed-relation-rank lemma above are self-reviewed project results; the former is exhaustively checked on the stated finite census, but neither has independent peer review.