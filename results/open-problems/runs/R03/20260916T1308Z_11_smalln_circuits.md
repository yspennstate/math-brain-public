Model actually ran: GPT-5.6 Sol. Reasoning level: UNVERIFIED; the scheduler exposes no model/reasoning selector, so GPT-6 maximum was not verified and is not claimed.
Problem: iid Rademacher square-matrix singularity — Komlós (1967) lineage; Van H. Vu, *Recent progress in combinatorial random matrix theory*, arXiv:2005.02797 (2020), Conjecture 2.2, Section 2; current locator also Julian Sahasrabudhe (2025), Eq. (4.1). Status: **OPEN / PARTIAL this run**.
Fixed metric: smallest proved remainder `b(n)` in `P(det B_n=0) <= [2 n(n-1)+b(n)] 2^{-n}`. Before: **UNMEASURED** in `RESULTS.md`. After: **exact smallest b(n) for every 1 <= n <= 6**; for `n >= 7` the smallest explicit all-n remainder with complete constants/domain remains **UNMEASURED/UNKNOWN**, so the asymptotic success criterion `b(n)=o(n^2)` is not met.

# R03 report — 2026-09-16 13:08 UTC — small exact matrices and minimal 4/5-row circuits

## 1. Repository recovery and protocol state

Required repository state read on `master` before doing mathematics:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, `QUEUE.md`;
- `operations/FLEET_2026-09-16.md` and `operations/RFLEET_2026-09-16.md`;
- the root repository inventory and current intake ledgers `probability_1000_intake_{D,E,F,G,H,I}_*/problems.jsonl` plus `probability_1000_intake_claude_20260907/problems.jsonl` (connector responses for these large ledgers were truncated after retrieval, so I do not claim a semantic reread of every ~780 row; the R03-relevant F0001 row was read directly);
- historical Rademacher campaign `probability_1000/sharp_rademacher_campaign_2026_08_18/STATE_OF_THE_PROOF.md` and repository searches for its descendants;
- newest neighbouring `runs/R02/20260916T1304Z_7b2d91a4.md`.

`runs/R03/` was absent before this write, so there was no canonical revised R03 run report to continue. Per protocol I used `RESULTS.md`, F0001 and the historical sharp-Rademacher campaign rather than importing Drive, Gmail, sandbox or chat history. The historical campaign is explicitly OPEN and records that its private entropy/connector programme did not close the iid prefactor.

`runs/R04/` returned 404 and repository searches found no ready R04 package, so the required R04 audit is **NOT AVAILABLE this run**; no audit ID is invented.

No shared ledger was edited: P26 owns `RESULTS.md`. This report contains a `ledger_delta` for P26.

## 2. Outside source and current-status check

Primary/near-primary source chain recovered:

1. J. Komlós, *On the determinant of (0,1) matrices*, Studia Sci. Math. Hungar. 2 (1967), 7–21 — original singularity lineage.
2. Van H. Vu, *Recent progress in combinatorial random matrix theory*, arXiv:2005.02797 (2020), Conjecture 2.2, Section 2 — exact iid sign-matrix conjecture
   \[
   p_n=(2+o(1))n^2 2^{-n}.
   \]
   Repository intake locator: `F0001`.
3. Vishesh Jain, Ashwin Sah, Mehtaab Sawhney, *Singularity of discrete random matrices*, arXiv:2010.06554 / GAFA 31 (2021). Their sharp theorem is for finite-support entry laws **not uniform on their support**. For laws uniform on their support, including uniform Rademacher, the statement is only exponential-scale.
4. Julian Sahasrabudhe, *Probabilistic combinatorics at exponentially small scales*, arXiv:2512.15077v1 (17 Dec 2025), Eq. (4.1):
   \[
   \Pr(\det B_n=0)=(1+o(1))2n^2 2^{-n}.
   \]
   The survey says in the iid `{−1,1}` case this remains perhaps the central open problem in the area; Eq. (4.2) records Tikhomirov only as `2^{-n+o(n)}`. The survey then separately turns to the symmetric ensemble.

Fresh dated queries on **2026-09-16** checked the two specified arXiv entries, current arXiv queries for 2026 Bernoulli/Rademacher singularity, and the Blinovsky claim. No independently verified newer exact-prefactor resolution was found in this bounded search. This is a bounded search outcome, not proof that no unindexed result exists.

Vladimir Blinovsky, arXiv:1511.05283, still claims exact resolution. The historical R03 audit retains concrete invalid displayed steps (X11/X12), so its status here is **CLAIMED / NOT VERIFIED**, not KNOWN and not a statement that the theorem itself is false.

## 3. Counterexample-first finite attack

Before proving a circuit classification, the checker exhaustively searched possible normal vectors arising from full-rank collections of observed sign columns:

- support 4: all `C(16,3)=560` triples of sign columns;
- support 5: all `C(32,4)=35,960` quadruples of sign columns.

It found **no counterexample** to the classifications proved below. The exhaustive search is an exact self-check, not a substitute for the written proofs.

## 4. R03-C225 — explicit matching lower bound with pair overlaps

**Status: PROVED.**

For rows, for each unordered pair `i<j` and sign `sigma in {+1,-1}`, define
\[
R_{ij}^{\sigma}=\{r_i=\sigma r_j\}.
\]
There are
\[
m=2\binom n2=n(n-1)
\]
signed row-pair events, and the same number of signed column-pair events. Each has probability `2^{-n}`.

Two distinct signed row-pair events are incompatible only when they use the same unordered row pair with opposite signs. There are `C(n,2)` such unordered incompatible event-pairs. Every other pair of distinct row events imposes exactly `2n` independent sign constraints, whether the two row pairs are disjoint or share one row. Hence its intersection probability is `2^{-2n}`. The same holds for columns.

For one signed row-pair event and one signed column-pair event, the intersection probability is
\[
2^{-(2n-1)}.
\]
Indeed the row equality contributes `n` independent constraints; conditional on it, the two column constraints at the two paired rows are equivalent, so the column equality contributes only `n-1` additional independent constraints.

Applying second Bonferroni to the union `P_n` of all signed row/column pair events gives
\[
\Pr(P_n)\ge
2m2^{-n}
-2\left(\binom m2-\binom n2\right)2^{-2n}
-m^2 2^{-(2n-1)}.
\tag{C225.1}
\]
Equivalently
\[
\Pr(\det B_n=0)\ge
\left[2n(n-1)-c_n\right]2^{-n},
\]
where
\[
c_n=
\left[
2\left(\binom m2-\binom n2\right)+2m^2
\right]2^{-n}
=O(n^4 2^{-n})=o(n^2).
\tag{C225.2}
\]

Thus the **matching lower asymptotic with explicit first overlap correction is already proved**. The hard direction is the matching upper remainder.

## 5. R03-C226 — no genuine minimal 3-row mechanism

**Status: PROVED.**

Let three sign rows be minimally linearly dependent. Their unique (up to scale) relation is
\[
a_1r_1+a_2r_2+a_3r_3=0
\]
with every `a_i != 0`.

Choose two independent observed sign columns (the row rank is two), and flip row signs so that the first selected column is `(1,1,1)`. Then
\[
a_1+a_2+a_3=0.
\]
For the second selected sign column, subtract the all-one equation. The set of coordinates where that column is `-1` has coefficient sum zero. A nonempty proper subset of three indices has size one or two; size one would force one `a_i=0`, and size two forces the complementary coefficient to be zero using the total-sum equation. Contradiction.

Therefore a minimally dependent triple of sign rows does not exist. Any dependence among three sign rows already contains an equal/opposite pair.

## 6. R03-C227 — complete minimal 4-row circuit classification

**Status: PROVED.**

Let `r_1,...,r_4` be a minimal real linear circuit of sign rows. Their row rank is three and the unique normal
\[
a=(a_1,a_2,a_3,a_4)
\]
has all coordinates nonzero.

Choose three independent observed sign columns spanning `a^perp`. By flipping row signs, normalize the first chosen column to `(1,1,1,1)`. Then
\[
\sum_{i=1}^4 a_i=0.
\tag{C227.1}
\]
For each of the other two selected columns, subtract the all-one equation. This gives a nonempty proper zero-sum subset of the coefficients. A subset of size one or three would force a coefficient to vanish; hence, after taking the complement if needed, each gives a zero-sum pair
\[
a_i+a_j=0.
\tag{C227.2}
\]
The two pair relations are independent modulo (C227.1), so they cannot be the same or complementary; therefore their two edges share one coefficient index. Relabeling,
\[
a_1=-a_2,
\qquad
a_1=-a_3.
\]
Then (C227.1) gives `a_4=a_1`. Thus
\[
\boxed{|a_1|=|a_2|=|a_3|=|a_4|.}
\tag{C227.3}
\]
After row sign choices every minimal 4-row circuit has the form
\[
\sigma_1r_1+\sigma_2r_2+\sigma_3r_3+\sigma_4r_4=0.
\]

There are `2^4/2=8` coefficient-sign directions modulo global sign. For any fixed direction, a random sign column is orthogonal to the normal exactly when two of the four signed coordinates are `+1` and two are `-1`, giving
\[
\binom42=6
\]
allowed columns among `16`. Therefore, for a fixed labelled four-row set,
\[
\Pr(\text{minimal 4-circuit})
\le8(3/8)^n.
\tag{C227.4}
\]
Consequently
\[
\Pr(\exists\text{ minimal 4-row circuit})
\le8\binom n4(3/8)^n.
\tag{C227.5}
\]
Relative to the target scale `2^{-n}`, its remainder coefficient is
\[
8\binom n4(3/4)^n=o(n^2).
\]

## 7. R03-C228 — complete minimal 5-row circuit classification

**Status: PROVED.**

Let five sign rows form a minimal real circuit. The unique normal
\[
a=(a_1,\ldots,a_5)
\]
has all coordinates nonzero, and the row rank is four.

Choose four independent observed sign columns spanning `a^perp`, and use row sign flips to make the first selected column all ones. Thus
\[
\sum_{i=1}^5 a_i=0.
\tag{C228.1}
\]
Each of the other three independent columns yields, after subtraction from the all-one equation, a nonempty proper zero-sum subset. Sizes one and four are impossible because all `a_i` are nonzero. A size-three subset may be replaced by its size-two complement using (C228.1). Thus the three independent constraints may be written as
\[
a_i+a_j=0
\]
for three distinct coefficient pairs.

Regard these three pairs as edges of a graph on five coefficient positions. The three relations are independent together with the total-sum relation. An odd cycle would force the coefficients on that component to vanish, so the graph is bipartite. With three independent edges on five vertices it is a forest with exactly two components.

The component-size split cannot be `3+2`: the two-vertex component has one `+` and one `-` coefficient and therefore zero component sum, while the three-vertex tree has bipartition sizes `1+2` and nonzero component sum unless its common magnitude is zero, contradicting minimality.

Hence the split is `4+1`. The four-vertex tree cannot have bipartition `2+2`, since then its component sum is zero and (C228.1) would force the isolated coefficient to vanish. Therefore its bipartition is `1+3`. If the common magnitude on that tree is `t`, its component sum has magnitude `2t`, and the isolated coefficient must have magnitude `2t`. Thus
\[
\boxed{\{|a_1|,\ldots,|a_5|\}=\{2t,t,t,t,t\}.}
\tag{C228.2}
\]

Modulo global scale/sign, there are
\[
5\cdot 2^4=80
\]
normal directions. For a fixed normal, say `(2,1,1,1,1)` after sign absorption, the equation
\[
2\varepsilon_1+\varepsilon_2+\varepsilon_3+\varepsilon_4+\varepsilon_5=0
\]
has exactly `8` sign solutions among `32`: for either sign of `epsilon_1`, the other four signs must have sum `-2 epsilon_1`, giving four choices. Hence for a fixed labelled five-row set,
\[
\Pr(\text{minimal 5-circuit})
\le80(1/4)^n.
\tag{C228.3}
\]
So
\[
\Pr(\exists\text{ minimal 5-row circuit})
\le80\binom n5 4^{-n},
\tag{C228.4}
\]
with target-scale remainder coefficient
\[
80\binom n5 2^{-n}=o(n^2).
\]

## 8. R03-C229 — direct outside-target reduction to support at least six

**Status: PROVED REDUCTION / PARTIAL toward the assigned conjecture.**

Let `P_n` be the union of all signed equal/opposite row and column pair events. The union bound gives
\[
\Pr(P_n)\le2n(n-1)2^{-n}.
\tag{C229.1}
\]

If a square sign matrix is singular and `P_n` does not occur, choose a minimal dependent row set. By C226 it cannot have size three (and size two is exactly a signed row pair). Thus it has support at least four. C227 and C228 pay all minimal supports four and five.

Define `R_{>=6}` to be the event that the matrix is singular, has no signed row or column pair, and has a minimal dependent row circuit of support at least six. Then
\[
\Pr(\det B_n=0)
\le
2n(n-1)2^{-n}
+8\binom n4(3/8)^n
+80\binom n5 4^{-n}
+\Pr(R_{\ge6}).
\tag{C229.2}
\]
Equivalently the fixed remainder metric obeys
\[
\boxed{
 b(n)
 \le
 8\binom n4(3/4)^n
 +80\binom n5 2^{-n}
 +2^n\Pr(R_{\ge6}).
}
\tag{C229.3}
\]
The first two terms are `o(n^2)`. Therefore the full upper asymptotic is reduced to the single outside-target statement
\[
\boxed{2^n\Pr(R_{\ge6})=o(n^2).}
\tag{C229.4}
\]

This reduction is independent of the private entropy-defect programme. It is the precise next collision-conditioned inverse-Littlewood--Offord obligation.

## 9. R03-C230 — exact iid sign-matrix probabilities for `1 <= n <= 6`

**Status: PROVED BY EXACT FINITE CERTIFICATE.**

Normalize a sign row modulo global sign by requiring its first coordinate to be `+1`. There are `2^{n-1}` projective row directions. Let `N_n` be the number of unordered `n`-sets of these directions that are linearly independent. Every invertible ordered sign matrix corresponds uniquely to:

1. one such independent `n`-set;
2. a row ordering (`n!` choices);
3. independent row signs (`2^n` choices).

Thus
\[
I_n=N_n n!2^n
\tag{C230.1}
\]
is the exact number of invertible sign matrices, and
\[
S_n=2^{n^2}-I_n
\]
is the exact singular count.

For the exact checker, identify normalized directions with vertices of the `(n-1)`-cube. Linear independence of the sign rows is equivalent to affine independence of the cube vertices. Double-counting an affine simplex with a distinguished vertex gives
\[
nN_n=2^{n-1}M_{n-1},
\tag{C230.2}
\]
where `M_d` is the number of linearly independent `d`-subsets among the nonzero `{0,1}^d` vectors.

The checker tests these determinants modulo `257`. This is exact for `d<=5`: Hadamard gives
\[
|\det A|\le d^{d/2}<257,
\]
so an integer `{0,1}` determinant is zero iff it is zero modulo 257.

The resulting exact values are:

| `n` | `N_n` | invertible `I_n` | singular `S_n` | exact `P_n` | `2^n P_n` | exact smallest `b(n)` |
|---:|---:|---:|---:|---:|---:|---:|
| 1 | 1 | 2 | 0 | `0` | `0` | `0` |
| 2 | 1 | 8 | 8 | `1/2` | `2` | `-2` |
| 3 | 4 | 192 | 320 | `5/8` | `5` | `-7` |
| 4 | 58 | 22,272 | 43,264 | `169/256` | `169/16` | `-215/16` |
| 5 | 3,008 | 11,550,720 | 22,003,712 | `1343/2048` | `1343/64` | `-1217/64` |
| 6 | 556,192 | 25,629,327,360 | 43,090,149,376 | `1315007/2097152` | `1315007/32768` | `-651073/32768` |

Here
\[
b(n)=2^n\Pr(\det B_n=0)-2n(n-1).
\tag{C230.3}
\]
Because the probability is exact, these are the **smallest possible remainder constants on the complete domain `1<=n<=6`**. Negative values merely record that for small `n` the raw leading coefficient `2n(n-1)` overcounts heavily because pair events overlap.

For `n>=7`, the smallest explicit remainder with complete constants/domain remains `UNMEASURED/UNKNOWN` in this track. Tikhomirov's asymptotic `2^{-n+o(n)}` is far stronger than the trivial probability bound but does not, as stated, provide the complete explicit constants/domain requested by this metric and is not `o(n^2)` on the target scale.

## 10. Reproducibility artifacts

Exact checker executed successfully:

- `artifacts/R03/20260916T1308Z_11_smalln_circuits_checker.py`
- checker SHA-256: `349bd5d731ffad32ec4437eed1e3ad2a96850255e51063a0e5e19aac451f01a7`
- GitHub create commit: `5c84650ee63f9dc276f4371911731463532364ff`; read back at that exact commit

Archived output:

- `artifacts/R03/20260916T1308Z_11_smalln_circuits_output.txt`
- output SHA-256: `039430feed59d14119b76e6bd0833151a2eff19fdd9c28199648cbaed30263c9`
- GitHub create commit: `c6220e95ea55b396c33f14b9f874866587e9a242`; read back at that exact commit

The checker independently verifies:

- the exact small-matrix counts `n<=6`;
- the explicit pair-overlap lower bound against the exact small probabilities where available;
- all `560` support-4 selected-column triples and all `35,960` support-5 selected-column quadruples;
- exactly `8` support-4 normal directions, all absolute type `(1,1,1,1)`, each with six allowed sign columns;
- exactly `80` support-5 normal directions, all absolute type `(2,1,1,1,1)`, each with eight allowed sign columns.

The checker is a self-check; C225--C229 have full proofs above.

## 11. Failed routes retained

Historical R03 failures recovered from the authorized repository remain active:

- the private entropy/connector route has not produced connector-compatible linear rigidity;
- the global exponential `9*4^ell+ell` bound does not close the matrix target;
- bounded support/incidence is not connector absorption;
- advertised/audit labels are not accepted without proof;
- Blinovsky is not treated as verified;
- a single fixed 4-row relation such as `(3/8)^n` is not a classification by itself — C227 now supplies the full minimal support-4 classification;
- any route that only proves the exponential rate is outside the fixed metric.

Newly killed this run: none of C226--C228 was refuted by exhaustive finite normal search. The new bottleneck is support `>=6`, not support 4 or 5.

## 12. Remaining obstruction and next attack

The measurable upper-bound obligation is now C229.4:
\[
2^n\Pr(R_{\ge6})=o(n^2),
\]
where `R_{>=6}` means: no equal/opposite row or column pair, but a minimal real row circuit of support at least six.

The next attack should classify **minimal six-row circuit normal types by atom size**. For a primitive normal `a in Z^6`, its per-column atom is
\[
\rho(a)=2^{-6}\#\{\varepsilon\in\{\pm1\}^6:a\cdot\varepsilon=0\}.
\]
If all minimal support-6 types with `rho(a)` close to `1/2` can be classified and shown to force a lower-support pair/4/5 circuit or an exponentially rarer family, then the residual starts to acquire a quantitative target-scale bound. Exact enumeration of realizable primitive normals from five independent observed sign columns is the natural first finite computation.

The private entropy-defect conjectures remain optional intermediate tools only; they do not redefine the assigned problem.

## 13. R04 audit status

`runs/R04/` does not exist on `master` at the time of this run. No ready package could be audited. Status: **R04_AUDIT_NOT_AVAILABLE**.

## 14. Structured ledger delta for P26

```yaml
ledger_delta:
  task_id: R03
  source:
    lineage: "Komlos 1967 random sign-matrix singularity"
    exact_problem_locator: "Van H. Vu, Recent progress in combinatorial random matrix theory, arXiv:2005.02797 (2020), Conjecture 2.2, Section 2"
    current_locator: "Julian Sahasrabudhe, arXiv:2512.15077v1, Eq. (4.1), Section 4"
  target: "P(det B_n=0)=(1+o(1))*2*n*(n-1)*2^(-n) for iid uniform signs"
  metric:
    name: "smallest proved b(n) in P(sing) <= [2*n*(n-1)+b(n)]*2^(-n)"
    before: "UNMEASURED"
    after:
      finite_exact_domain: "1 <= n <= 6"
      values:
        n1: "0"
        n2: "-2"
        n3: "-7"
        n4: "-215/16"
        n5: "-1217/64"
        n6: "-651073/32768"
      n_ge_7: "UNMEASURED/UNKNOWN as smallest explicit remainder with complete constants/domain"
      asymptotic_success: false
  status: "PARTIAL"
  unchanged_count: "0 for the new canonical run because the metric moved; pre-canonical historical stagnation count UNKNOWN"
  exact_evidence:
    - "C225 explicit pair-overlap matching lower bound"
    - "C227 complete minimal support-4 circuit classification"
    - "C228 complete minimal support-5 circuit classification"
    - "C229 reduction of the upper remainder to minimal support >=6"
    - "C230 exact sign-matrix singularity probabilities n<=6"
    - "artifacts/R03/20260916T1308Z_11_smalln_circuits_checker.py"
    - "artifacts/R03/20260916T1308Z_11_smalln_circuits_output.txt"
  audit_ids:
    self_check: "R03-exact-checker-20260916T1308Z"
    R04: "NOT_AVAILABLE"
    external_second_audit: "NONE_YET"
```

## 15. Primary references

- J. Komlós, *On the determinant of (0,1) matrices*, Studia Sci. Math. Hungar. 2 (1967), 7--21.
- J. Kahn, J. Komlós, E. Szemerédi, *On the probability that a random ±1-matrix is singular*, JAMS 8 (1995).
- V. H. Vu, *Recent progress in combinatorial random matrix theory*, arXiv:2005.02797 (2020), Conjecture 2.2.
- K. Tikhomirov, *Singularity of random Bernoulli matrices*, Annals of Mathematics 191 (2020), 593--634.
- V. Jain, A. Sah, M. Sawhney, *Singularity of discrete random matrices*, arXiv:2010.06554 / GAFA 31 (2021).
- J. Sahasrabudhe, *Probabilistic combinatorics at exponentially small scales*, arXiv:2512.15077v1 (17 Dec 2025), Eq. (4.1).
- V. Blinovsky, arXiv:1511.05283 (claimed exact resolution; not accepted as verified here).

**NO CLOSURE CLAIM.** The fixed asymptotic metric remains open; this run moves it by exact finite values, proves the overlap-corrected lower asymptotic, and removes all minimal 3/4/5-row circuits from the leading-order upper obstruction.
