Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; GPT-6 / maximum reasoning was requested, but no authenticated runtime reasoning-effort telemetry or binding model/effort selector is exposed.

# R7-06 admission — G0008 / axis two-point connectivity monotonicity on the square lattice

Date of source/status review: **2026-09-18**  
Repository: `yspennstate/math-open-problems`, branch `master`  
R7-06 native ID: `6aabe827777c8191a43330b4a87d481d`  
Own root: `research7_2026-09-17/R7-06/`  
Selection shard: `sum(ord(c) for c in "G0008") % 7 = 5`  
Classification: **HARD OUTSIDE**  
Admission state before this record: `PENDING_ADMISSION`

## 1. Exact outside source and locator

Outside authors: **Alberto M. Campos and Bernardo N. B. de Lima**.  
Title: **The probability of connection between two vertices cannot be monotone with the distance for Bernoulli Percolation on transitive graphs**.  
Year: **2026**.  
Primary source: arXiv **2601.00291v1**, submitted 2026-01-01, <https://arxiv.org/abs/2601.00291>.  
Canonical intake: `probability_1000_intake_G_20260910/problems.jsonl`, candidate `G0008`; source construction row is also preserved in `probability_1000_intake_G_20260910/batches/mk_b01.py`.  
Locator recorded by the intake: **Abstract and Introduction, PDF p. 1; Section 3, PDF p. 4**.

The source explicitly says that on the square lattice it remains open to prove that the probability that the origin is connected to `(0,n)` is monotone in `n`, and after constructing a transitive-graph counterexample says that it remains open whether lattices such as `Z^d` have the monotonicity property.

For Bernoulli bond percolation on `Z^2`, write

`tau_n(p) := P_p( 0 <-> (0,n) )`, `n >= 1`, `0 < p < 1`.

The literal square-lattice endpoint is

`tau_{n+1}(p) <= tau_n(p)` for every `n >= 1` and every `p in (0,1)`.

The intake also records the broader `Z^d` formulation. R7-06 will **not** call the full canonical source closed merely from a `d=2` theorem if the broader lattice quantifier is retained by the source; a `d=2` proof is a major source-valid milestone, not an automatic all-`d` closure.

## 2. Current-version and bounded later-literature check

On 2026-09-18, the arXiv record still surfaced as **v1**. Its current abstract still calls square-lattice monotonicity open. A bounded exact-title / exact-question / author search did not surface a later paper resolving the square-lattice all-`p`, all-`n` problem. This is **negative search evidence only**; it does not certify novelty or permanent openness.

The closest recovered prior result is Bernardo N. B. de Lima, Aldo Procacci and Remy Sanchis, **A remark on monotonicity in Bernoulli bond Percolation** (2015): it proves the two-point connectivity is monotone in the axial distance when `p` is sufficiently close to `0`, and proves an analogous monotonicity statement for the **truncated** connectivity for `p` sufficiently close to `1`. Those results do not settle the source's every-`p` square-lattice question.

Campos's current research page also still lists the Campos--de Lima project; no later author-side square-lattice resolution was found in the bounded check.

## 3. Ownership, aliases, and prior attempts

Fresh direct fetch of `operations/claims/G0008.md` before admission returned **404 / no canonical claim at that captured master**. Repository searches recover no conflicting canonical G0008 claim.

Prior work must nevertheless be preserved:

- the intake attempt `G0008-A001` asserted an all-`n` small-`p` route by comparing path-counting series;
- that assertion was **withdrawn in the same intake session**;
- `G0008-A002` records the correction: controlling the ratio of terms in the path-length expansion does **not** control the dependence on endpoint distance `n`;
- the intake retains only the standard/eventual off-critical monotonicity direction as a partial observation, with no mechanism at criticality;
- later R15/R20 admission screens noticed G0008 as unclaimed-looking but did not create an ownership claim.

This admission therefore does **not** reuse the withdrawn small-`p` proof and does not treat a previous screen as ownership.

## 4. HARD classification and exact closure criterion

This is **HARD**, not CLOSABLE: the source asks for a uniform statement over a continuum of percolation parameters and all axial separations on an infinite critical lattice. The paper itself constructs counterexamples on other transitive graphs, so transitivity alone cannot close the problem.

Square-lattice source-level closure criterion:

> Give a complete proof that for every `p in (0,1)` and every integer `n >= 1`, `tau_{n+1}(p) <= tau_n(p)`, or give one rigorously certified pair `(p,n)` for which `tau_{n+1}(p) > tau_n(p)`.

If the broader `Z^d` clause of the canonical intake is treated as part of the full endpoint, all-`d` closure additionally requires the corresponding statement or counterexample under that quantifier.

Numerical finite boxes, finite tori, off-critical asymptotics, or a fixed finite list of `n` values are **PARTIAL** only.

## 5. Frozen mathematical metric and milestone

Frozen metric for this target:

`M_axis := largest integer N >= 1 for which R7-06 has a rigorous source-valid proof that tau_{n+1}(p) <= tau_n(p) simultaneously for every p in (0,1) and every 1 <= n <= N.`

Baseline at admission: **UNKNOWN/UNMEASURED**. No missing proof is converted to `0`, and the withdrawn small-`p` attempt supplies no baseline.

Concrete first milestone: decide the universal first inequality

`tau_2(p) <= tau_1(p)` for **all** `p in (0,1)`,

or produce a rigorous counterexample. A proof moves the metric to at least `M_axis = 1`; a certified counterexample refutes the square-lattice source statement immediately.

## 6. Initial mathematical attack plan

New-target protocol begins counterexample-first. Initial Section-B methods, unless fresh history shows exhaustion:

- **B2 — attack the negation:** isolate the exact signed event difference `tau_n - tau_{n+1}` and determine what a first violation must look like;
- **B14 — exploit group symmetry:** use translations/reflections of `Z^2`, FKG and endpoint exchange to compress the signed difference;
- **B16 — exact small cases:** attack `n=1` first, with exact finite identities/cutset structure rather than numerical extrapolation.

Any finite exact computation will be labelled finite evidence unless it proves an infinite-lattice statement.

## 7. Admission verdict

**ADMITTED AS HARD OUTSIDE, subject to the required fresh-master create-only ownership claim.**

No source-level theorem is claimed in this admission record. Metric baseline remains `UNKNOWN/UNMEASURED` pending actual mathematics.
