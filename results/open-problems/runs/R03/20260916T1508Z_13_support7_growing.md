Model actually ran: GPT-5.6 Sol. Reasoning level: UNVERIFIED; the scheduler exposes no model/reasoning selector, so GPT-6 maximum was not verified and is not claimed. Fixed metric: **no movement** — the exact smallest `b(n)` is still known on the complete domain `1 <= n <= 9`, with the run-12 values unchanged; the all-n condition `b(n)=o(n^2)` is not proved.
Problem: iid Rademacher square-matrix singularity — Komlós (1967) lineage; Van H. Vu, *Recent progress in combinatorial random matrix theory*, arXiv:2005.02797 (2020), Conjecture 2.2, Section 2; Jain–Sah–Sawhney, arXiv:2010.06554, Conjecture 1.1 / Theorem 1.5; Julian Sahasrabudhe, arXiv:2512.15077v1 (2025), Eq. (4.1). Status: **OPEN / PARTIAL**.

# R03 report — 2026-09-16 15:08 UTC — exact support seven and reduction to the unstructured linear-support regime

## 1. Repository recovery and protocol state

Before new mathematics I reread on `master`:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/FLEET_2026-09-16.md` and `operations/RFLEET_2026-09-16.md`;
- newest own report `runs/R03/20260916T1408Z_12_support6_exactn9.md`;
- newest neighboring R02 report `runs/R02/20260916T1405Z_1bc8ce78.md`;
- newest R04 report `runs/R04/20260916T140957Z_r04_block_minami.md`, which is ready for the directed R03 audit below;
- the relevant intake/dedup hits for `F0001` and searches over the probability intake families.

The large intake JSONL files are connector-truncated, so I do **not** claim a semantic reread of every approximately 780 row. The relevant `F0001` source row remains the iid Rademacher singularity target. P26 remains the sole shared-root-ledger writer, so I did not edit `RESULTS.md`, `QUEUE.md`, or `POSTED.md`.

The previous R03 report is binding. Retain without re-derivation: C225 matching lower asymptotic with explicit row/column-pair overlap correction; C226 no genuine minimal support-three circuit; C227/C228 exact support-four/five classifications and target-scale payments; C232/C233 exact support-six classification/payment; C234 reduction to minimal circuit support at least seven; C231 exact iid sign singularity metric through `n=9`.

R02 has independently audited the support-four classification as `R02-AUDIT-R03-C227-01 = PASS` (claim-scoped, not a closure audit). No P26 full R03 audit and no second full-package closure audit exist.

## 2. Outside source and current-status check — 2026-09-16

Dated bounded source/current-status queries were archived in `artifacts/R03/20260916T1508Z_13_status_search.md`.

1. J. Komlós, *On the determinant of (0,1) matrices*, Studia Sci. Math. Hungar. 2 (1967), 7–21: original lineage.
2. Van H. Vu, *Recent progress in combinatorial random matrix theory*, arXiv:2005.02797 (2020), Section 2, **Conjecture 2.2**: iid Rademacher model. The symmetric model is separate in Section 3.
3. Vishesh Jain, Ashwin Sah, Mehtaab Sawhney, *Singularity of discrete random matrices*, arXiv:2010.06554 / GAFA 31 (2021), **Conjecture 1.1**. The sharp full singularity theorem assumes the entry law is not uniform on its finite support; the Rademacher law is in the uniform-support residual case. The paper nevertheless proves a sharp structured/almost-constant theorem, Theorem 1.5, which is used below.
4. Julian Sahasrabudhe, *Probabilistic combinatorics at exponentially small scales*, arXiv:2512.15077v1, 17 Dec 2025, **Eq. (4.1)**: records the conjectural iid sign asymptotic and describes the exact prefactor as still open; Eq. (4.2) records Tikhomirov's `2^{-n+o(n)}` scale.
5. Konstantin Tikhomirov, *Singularity of random Bernoulli matrices*, Ann. Math. 191 (2020): exponential rate, not the fixed metric target.

Current 2026 arXiv/web queries did not locate an independently verified exact-prefactor resolution. This is a bounded-search statement, not proof that no unindexed result exists. Symmetric Bernoulli results were excluded as a different dependent-entry ensemble. Historical Irmatov/Blinovsky resolution claims remain unverified in this portfolio because the cumulative R03 record contains concrete proof defects.

For the finite metric, OEIS A055165 and Živković's classification still give the total number of nonsingular `(0,1)` matrices only through order 8. Živković obtains determinant-value data at order 9 but not the total nonsingular count needed for exact `b(10)`. Therefore the complete exact metric domain does not move beyond `n=9` this run.

## 3. Counterexample-first support-seven search

The previous residual began at minimal row-circuit support seven. I first searched the complete finite support-seven space rather than assuming the support-six pattern continued.

Let seven labelled sign rows be minimally dependent. Their `7 x n` submatrix has row rank six and a unique normal direction

\[
a=(a_1,\dots,a_7),\qquad a_i\ne0.
\]

Six actual sign columns span the hyperplane `a^perp`. By row sign flips normalize one basis column to the all-one vector. Projectivize the other sign columns by requiring their first coordinate to be `+1`. Relative to the all-one column, each other projective class is determined by a nonempty subset of the remaining six coordinates, hence by one of the 63 nonzero six-bit masks.

If the five additional basis columns correspond to masks `S_1,...,S_5`, subtracting their orthogonality equations from the all-one equation gives

\[
\sum_{j\in S_i} a_{j+1}=0,\qquad i=1,\dots,5.
\]

Thus the exact search consists of

\[
\binom{63}{5}=7,028,847
\]

five-row binary systems in six unknowns. Rank five gives a one-dimensional kernel. The checker computes the exact cofactor null vector, restores `a_1=-\sum_{j=2}^7 a_j`, rejects zero coordinates, divides by the gcd, and counts all 128 sign columns orthogonal to the resulting primitive normal.

This is exhaustive: every actual minimal seven-row circuit has six independent actual columns; after the row-sign/projective normalization, five of them appear as exactly one enumerated five-mask frame. No probabilistic or floating-point step enters the classification.

## 4. R03-C235 — complete minimal seven-row circuit classification

**Status: PROVED WITH EXECUTED EXACT FINITE CORE.**

The exact enumeration gives:

- projective frames: `7,028,847`;
- rank-six frames: `6,029,142`;
- rank-six frames whose primitive seven-coordinate normal has no zero coordinate: `405,636`;
- absolute primitive normal types: exactly **14**.

They are:

| absolute primitive normal type | zero sign columns / 128 | frame count |
|---|---:|---:|
| `(2,1,1,1,1,1,1)` | 30 | 106260 |
| `(2,2,2,1,1,1,1)` | 24 | 90720 |
| `(3,2,1,1,1,1,1)` | 22 | 40824 |
| `(3,2,2,2,1,1,1)` | 20 | 68040 |
| `(3,3,2,1,1,1,1)` | 18 | 20160 |
| `(3,3,2,2,2,1,1)` | 16 | 15120 |
| `(4,1,1,1,1,1,1)` | 12 | 42 |
| `(4,2,2,1,1,1,1)` | 16 | 7560 |
| `(4,3,2,2,1,1,1)` | 16 | 30240 |
| `(4,3,3,1,1,1,1)` | 12 | 630 |
| `(4,3,3,2,2,1,1)` | 14 | 15120 |
| `(5,2,2,2,1,1,1)` | 12 | 840 |
| `(5,3,3,2,1,1,1)` | 12 | 2520 |
| `(5,4,3,2,2,1,1)` | 12 | 7560 |

The maximum atom is therefore

\[
\boxed{30/128=15/64<1/2.}
\]

The exact checker is `artifacts/R03/20260916T1508Z_13_support7_growing_exact.cpp`; the archived output is the adjacent `.out` file and ends `SELF-CHECK PASS`.

## 5. R03-C236 — explicit support-seven target-scale payment

**Status: PROVED.**

For a primitive absolute type with multiplicities, the number of signed/permuted normal directions modulo global sign is

\[
2^6\frac{7!}{\prod_j m_j!}.
\]

Aggregating the fourteen exact types by zero atom gives:

| zero columns | normal directions modulo global sign |
|---:|---:|
| 30 | 448 |
| 24 | 2240 |
| 22 | 2688 |
| 20 | 8960 |
| 18 | 6720 |
| 16 | 47040 |
| 14 | 40320 |
| 12 | 123648 |

Thus for a fixed labelled seven-row set,

\[
\begin{aligned}
P_7(n)\le{}&448(15/64)^n+2240(3/16)^n+2688(11/64)^n\\
&+8960(5/32)^n+6720(9/64)^n+47040(1/8)^n\\
&+40320(7/64)^n+123648(3/32)^n.
\end{aligned}
\]

Union over the `C(n,7)` row sets. After dividing by the target scale `2^{-n}`, the coefficient is

\[
\binom n7\left[
448(15/32)^n+2240(3/8)^n+2688(11/32)^n+8960(5/16)^n
+6720(9/32)^n+47040(1/4)^n+40320(7/32)^n+123648(3/16)^n
\right]=o(n^2).
\]

Hence support seven is paid completely and explicitly.

## 6. R03-C237 — explicit growing-support payment through `3 sqrt(n)/4`

**Status: PROVED.**

This is the first non-fixed-support statement in the row-circuit route.

Fix a labelled set of `k` rows supporting a minimal circuit. Its row rank is `k-1`, so its sign columns span a hyperplane. There are exactly `2^(k-1)` projective sign-column classes in `R^k`; therefore the number of candidate hyperplanes spanned by `k-1` independent sign columns is at most

\[
H_k\le \binom{2^{k-1}}{k-1}\le2^{(k-1)^2}.
\tag{6.1}
\]

Now let `a_1,...,a_k` be any nonzero normal coefficients. Absorb their signs into the independent Rademacher signs, so all weights may be taken positive. A zero sign sum

\[
\sum_i a_i\varepsilon_i=0
\]

corresponds to a subset whose positive weight sum is exactly half the total. The family of all such subsets is an antichain: one cannot strictly contain another because all weights are positive. Sperner's theorem therefore gives the self-contained Littlewood--Offord bound

\[
\rho(a):=P\left(\sum_i a_i\varepsilon_i=0\right)
\le p_k:=2^{-k}\binom{k}{\lfloor k/2\rfloor}.
\tag{6.2}
\]

The central probabilities are nonincreasing in pairs, and for every `k>=7`,

\[
p_k\le p_7=p_8=35/128.
\tag{6.3}
\]

For a fixed row set, union over the candidate hyperplanes; then union over row sets. For any `K>=7`,

\[
2^nP(\exists\text{ minimal circuit with }7\le k\le K)
\le
\sum_{k=7}^K n^k2^{(k-1)^2}(35/64)^n.
\tag{6.4}
\]

Take `n>=4096` and

\[
K=\left\lfloor\frac34\sqrt n\right\rfloor.
\]

For `n>=4096`,

\[
\log_2 n\le\frac14\sqrt n,
\]

(the inequality holds at `4096`, and its difference has positive derivative thereafter). Hence

\[
k\log_2 n\le\frac{3}{16}n,
\qquad
(k-1)^2\le\frac{9}{16}n.
\]

Therefore each summand in (6.4) is at most

\[
2^{-\gamma n},
\qquad
\gamma=\log_2(64/35)-\frac34>0.
\]

The positivity is certified exactly by

\[
64^4-8\,35^4=4,772,216>0.
\]

There are fewer than `n` summands, so

\[
\boxed{
2^nP\left(\exists\text{ minimal row circuit with }7\le k\le\left\lfloor\frac34\sqrt n\right\rfloor\right)
\le n2^{-\gamma n},\quad n\ge4096.
}
\tag{C237}
\]

This is an explicit all-constants payment, independent of the private entropy-defect programme.

## 7. R03-C238 — published sharp structured theorem pushes the residual to linear support

**Status: PROVED REDUCTION using Jain--Sah--Sawhney Theorem 1.5 plus explicit Bonferroni.**

Jain--Sah--Sawhney Theorem 1.5 states: for every fixed discrete entry law `xi`, there exist `delta,rho,eta>0` such that for all sufficiently large `n` and `t<=1`,

\[
P\left[\inf_{x\in\mathrm{Cons}(\delta,\rho)}\|M_n(\xi)x\|_2\le t\right]
\le nP(E_{e_1})+\binom n2\{P(E_{e_1-e_2})+P(E_{e_1+e_2})\}
+(t+P(E_{e_1-e_2}))e^{-\eta n}.
\tag{7.1}
\]

For uniform Rademacher entries,

\[
P(E_{e_1})=0,
\qquad
P(E_{e_1-e_2})=P(E_{e_1+e_2})=2^{-n}.
\]

With `t=0`, write `A_col` for the event that there is an almost-constant right null vector. If `m=n(n-1)` is the number of signed column-pair events, then

\[
P(A_{col})\le m2^{-n}+2^{-n}e^{-\eta n}.
\tag{7.2}
\]

Let `U_col` be the union of those signed column-pair events. For sufficiently large `n`, every pair vector lies in `Cons(delta,rho)`, so `U_col subset A_col`. Every two distinct compatible signed pair constraints impose two independent sign equations per row and have intersection probability `4^{-n}`; opposite signs on the same unordered pair are incompatible. Second Bonferroni therefore gives the safe lower bound

\[
P(U_{col})\ge m2^{-n}-\binom m2 4^{-n}.
\tag{7.3}
\]

Subtracting (7.3) from (7.2),

\[
\boxed{
P(A_{col}\setminus U_{col})
\le \binom m2 4^{-n}+2^{-n}e^{-\eta n}.
}
\tag{7.4}
\]

Apply the same theorem to the transpose. A unit left-null vector supported on at most `delta n` coordinates has at least `(1-delta)n` zero coordinates and therefore lies in `Cons(delta,rho)` with center `lambda=0`. Consequently, after excluding signed row pairs,

\[
\boxed{
P(\exists\text{ left null vector of support }\le\delta n\text{ and no signed row pair})
\le \binom m2 4^{-n}+2^{-n}e^{-\eta n}.
}
\tag{C238}
\]

On the target scale the right side contributes at most

\[
\binom m2 2^{-n}+e^{-\eta n}=o(n^2).
\]

Thus the fixed-support tables C227/C228/C233/C236 are exact finite mechanism data, but asymptotically the published JSS structured theorem already pays **every** minimal row circuit of support at most `delta n`, up to an `o(n^2)2^{-n}` remainder after the elementary pair events are removed.

The constants `delta,rho,eta` and the sufficiently-large-`n` threshold are existential in the cited theorem; therefore C238 does **not** move the owner's fixed metric, which requires complete numerical constants and domain.

## 8. R03-C239 — outside-target residual is the genuinely unstructured linear-support event

**Status: PROVED REDUCTION / PARTIAL toward the source conjecture.**

Let `R_unstr` be the event that:

1. `B_n` is singular;
2. there is no signed equal/opposite row or column pair;
3. every nonzero left null vector has support greater than `delta n` (equivalently for this purpose, no sparse left null vector belongs to the JSS structured class).

Combining the elementary pair upper bound with C238 gives, for the existential JSS constants and all sufficiently large `n`,

\[
P(\det B_n=0)
\le
2n(n-1)2^{-n}
+\binom{n(n-1)}2 4^{-n}
+2^{-n}e^{-\eta n}
+P(R_{unstr}).
\]

Therefore

\[
\boxed{
b(n)
\le
\binom{n(n-1)}2 2^{-n}+e^{-\eta n}+2^nP(R_{unstr}).
}
\tag{C239}
\]

The first two terms are `o(n^2)`. The matching lower asymptotic with overlap corrections is already retained C225. Hence the exact outside problem is now isolated to

\[
\boxed{2^nP(R_{unstr})=o(n^2).}
\tag{8.1}
\]

This is precisely the kind of unstructured/collision-conditioned inverse Littlewood--Offord contribution that JSS identify as the unresolved uniform-support obstruction. It is not replaced by any private entropy-defect conjecture.

## 9. Fixed metric and exact small matrices

**No metric movement this run.** The exact smallest values remain:

\[
\begin{array}{c|rrrrrr}
n&1&2&3&4&5&6\\\hline
b(n)&0&-2&-7&-215/16&-1217/64&-651073/32768
\end{array}
\]

and

\[
b(7)=-162946621/16777216,
\]
\[
b(8)=1447302462939/68719476736,
\]
\[
b(9)=3025524941051491/35184372088832.
\]

No exact total nonsingular `(0,1)` matrix count of order 9 was found in the bounded current search, so exact `b(10)` is not claimed.

## 10. Retained failed routes / exact obstruction

Retain all previous killed routes. In source-facing terms the important ones are:

- exponential-rate-only bounds do not address the polynomial prefactor;
- fixed-support enumeration cannot by itself close a residual with support growing linearly in `n`;
- naive hyperplane counting grows like `2^{Theta(k^2)}` and therefore stops naturally around `k=Theta(sqrt n)`; C237 makes that limitation explicit;
- the private `9*4^ell+ell` entropy-defect estimate is not linear, connector absorption remains separate, and the centered required-order random-normal transfer remains open; those are intermediate routes only;
- Irmatov/Blinovsky announced exact-resolution routes are not accepted without a verified argument.

The fixed metric has now failed to move for **one** consecutive run after run 12 moved it, so the three-run stuck protocol is not triggered.

## 11. Exact checker / execution evidence

Executed locally with

`g++ -O3 -march=native -std=c++17 artifacts/R03/20260916T1508Z_13_support7_growing_exact.cpp`.

The exact enumeration completed in approximately `1.27 s` in the execution environment and output `SELF-CHECK PASS`.

Local SHA-256 values of the executed bytes:

- checker source: `443be5742fcb20e4be51844523d5d4b354f96557108122c3a81c9947c1772055`;
- output: `e7ffd71759e8a1d88761e264caaed00764443ec2d78b6aaf4580a87c52ccc71c`.

GitHub creation/readback evidence:

- checker created at commit `1915cb6069b8919e8963a91331795dff7d99d731`, blob `a8d9f3b8c48b045f24d91cf97f6823ed7c58ebeb`, and read back at that commit;
- output created at commit `e3868ad090726ba3f7030782fe4cb2bcbc260505`, blob `21b5e9b45205c07ded558c864e9c4d327d4e2af2`, and read back at that commit;
- current-status log created at commit `024185ec6ccb70b135c1ffa831d56cf447ea5657`, blob `70247c46b160e04f015bdc608616631f4af93c7f`, and read back at that commit.

## 12. Directed independent audit of R04

Ready package audited: `runs/R04/20260916T140957Z_r04_block_minami.md`.

### R03-AUDIT-R04-FM-C2-02 — PASS for the stated block-GOE second-moment theorem

**Scope audited:** R04-FM-C2, the covariance embedding and resulting uniform finite-`N` factorial/second-moment bound on the stated domain `2W+1<=N`. I do not promote the full Fyodorov--Mirlin crossover problem to solved.

R04 freezes the real symmetric Gaussian circular band matrix with upper-triangular coordinate variance

\[
v=(2W+1)^{-1}
\]

on the band and interval `I_N=[-pi/N,pi/N]`. Put

\[
s=W+1,
\qquad K=\lceil N/s\rceil,
\qquad q=\lfloor N/K\rfloor.
\]

Partition the indices into `K` consecutive balanced blocks, of sizes `m_j in {q,q+1}`. Since `K>=N/s`, every block has `m_j<=s=W+1`, so every within-block coordinate is a legitimate band coordinate.

The lower bound used by R04 is correct:

\[
q\ge\left\lceil\frac{2W+1}{3}\right\rceil.
\]

For `K=2`, `N>=2s-1` gives `q>=s-1`, which is enough. For `K>=3`, integer ceiling gives `N>=(K-1)s+1`, and hence

\[
q\ge s-\left\lceil\frac{s-1}{K}\right\rceil
\ge s-\left\lceil\frac{s-1}{3}\right\rceil
=\left\lceil\frac{2s-1}{3}\right\rceil.
\]

(The `K=1` edge case forces `s=1` under the retained domain and is immediate.)

Set

\[
a^2=\frac{q}{2(2W+1)}=\frac{vq}{2}.
\]

Peled--Schenker--Shamis--Sodin define deformed block-Gaussian matrices with arbitrary positive block sizes `N_j`, independent GOE blocks, and arbitrary deterministic real-symmetric deformation; their Theorem 3 gives the factorial-moment Minami estimate uniformly in those block sizes. Their GOE normalization has off-diagonal variance `1/m_j` and diagonal variance `2/m_j`.

Therefore `a V_j` has within-block variances

\[
\operatorname{Var}(aV_{aa})=v\frac q{m_j}\le v,
\qquad
\operatorname{Var}(aV_{ab})=v\frac q{2m_j}\le v.
\]

Subtract these nonnegative variances coordinatewise from the target band covariance, place every inter-block band coordinate in the remainder, and obtain an independent Gaussian real-symmetric `R` with

\[
H_N\stackrel d=R+a\bigoplus_jV_j.
\]

Condition on `R` and divide by `a`; this is exactly the PSSS deformed block-Gaussian setup. Since `sum m_j=N` and `|I_N|=2pi/N`, Theorem 3 gives, with its universal symbolic constant `C_PSSS`,

\[
E X_N\le Y,
\qquad
E(X_N)_2\le Y^2,
\qquad
Y=\frac{2\pi C_{PSSS}}a.
\]

Thus

\[
E X_N^2\le Y+Y^2.
\]

Finally the exact `q` bound gives

\[
a^{-2}=\frac{2(2W+1)}q\le6,
\]

hence

\[
\boxed{E X_N^2\le2\pi\sqrt6\,C_{PSSS}+24\pi^2C_{PSSS}^2}
\]

on the same domain `2W+1<=N`. Along `W=floor(c sqrt N)`, `q/W->1`, so `a^{-1}->2` and R04's sharper limsup

\[
4\pi C_{PSSS}+16\pi^2C_{PSSS}^2
\]

also follows.

**Audit verdict:** `R03-AUDIT-R04-FM-C2-02 = PASS` for R04-FM-C2. The published PSSS theorem was checked in the journal/arXiv source: its deformed model permits arbitrary block sizes, and Theorem 3 is the stated Minami/factorial-moment theorem. This is a claim-scoped independent audit, not closure of the critical random-band-matrix point-process problem.

## 13. Cumulative ledger

| Item | Status |
|---|---|
| Exact iid sharp prefactor `(1+o(1))2n(n-1)2^{-n}` | **OPEN** |
| C225 matching lower bound with explicit pair overlaps | **PROVED** |
| C226 support 3 exclusion | **PROVED** |
| C227 support 4 classification/payment | **PROVED; R02 claim audit PASS** |
| C228 support 5 classification/payment | **PROVED** |
| C232/C233 support 6 classification/payment | **PROVED** |
| **C235/C236 support 7 classification/payment** | **PROVED NEW; exact finite core** |
| **C237 explicit growing-support payment through `3 sqrt(n)/4`** | **PROVED NEW** |
| **C238 JSS structured reduction to linear support** | **PROVED NEW REDUCTION using published theorem** |
| **C239 residual isolated to unstructured linear-support event** | **PROVED NEW REDUCTION / source still PARTIAL** |
| Exact smallest `b(n)` | **known exactly for `1<=n<=9`; no movement this run** |
| All-n `b(n)=o(n^2)` | **OPEN** |
| Unstructured linear-support inverse Littlewood--Offord contribution | **OPEN / principal obstruction** |
| Private entropy-defect programme | **INTERMEDIATE ONLY; not source closure** |
| Blinovsky/Irmatov announced exact routes | **NOT VERIFIED** |
| P26 full-package R03 audit | **NONE YET** |
| second full-package OTHER-track audit | **NONE YET** |
| R03 audit of R04-FM-C2 | **PASS: `R03-AUDIT-R04-FM-C2-02`** |

## 14. Next attack

The finite-support frontier is no longer the real bottleneck. C237 pays an explicit growing range, while C238 shows that the published sharp structured theorem pays every sparse left-null vector up to an unspecified positive linear fraction of `n` after pair mechanisms are removed.

The next run should therefore **not** spend the hour merely enumerating support eight. The exact blocker is the source-matching unstructured event

\[
\boxed{
2^n P(R_{unstr})=o(n^2),
}
\]

where all null vectors are outside the JSS almost-constant class. The useful routes are now:

1. extract from the JSS unstructured entropy argument the precise point where uniform support loses the sharp prefactor, and seek a collision-conditioned strengthening after excluding all pair hyperplanes;
2. formulate a quantitative inverse Littlewood--Offord statement for normal vectors conditioned to avoid the elementary pair structure, with an entropy count compatible with `2^{-n}` rather than merely `(1/2+o(1))^n`;
3. use support-seven exact data only as an adversarial test set for any proposed structural lemma, not as the main asymptotic method.

No private conjecture is substituted for the outside target.

## 15. Structured `ledger_delta` for P26

```yaml
ledger_delta:
  worker: R03
  category: HARD OUTSIDE
  source:
    lineage: "Komlos 1967 random sign-matrix singularity"
    exact_problem_locator: "Van H. Vu, Recent progress in combinatorial random matrix theory, arXiv:2005.02797 (2020), Conjecture 2.2, Section 2"
    primary_sharp_literature: "Jain-Sah-Sawhney arXiv:2010.06554, Conjecture 1.1 / Theorem 1.5; Sahasrabudhe arXiv:2512.15077v1 Eq. (4.1)"
  target: "P(det B_n=0)=(1+o(1))*2*n*(n-1)*2^(-n) for iid uniform signs"
  fixed_metric: "smallest proved remainder b(n) in P(det B_n=0) <= [2*n*(n-1)+b(n)]*2^(-n), with complete n-domain/constants"
  before: "exact smallest b(n) for every 1<=n<=9; all-n o(n^2) not proved"
  after: "NO MOVEMENT in fixed metric: exact smallest b(n) still for every 1<=n<=9; all-n o(n^2) not proved"
  unchanged_count: 1
  status: PARTIAL
  new_exact_evidence:
    - "artifacts/R03/20260916T1508Z_13_support7_growing_exact.cpp @ 1915cb6069b8919e8963a91331795dff7d99d731"
    - "artifacts/R03/20260916T1508Z_13_support7_growing_exact.out @ e3868ad090726ba3f7030782fe4cb2bcbc260505; SELF-CHECK PASS"
    - "artifacts/R03/20260916T1508Z_13_status_search.md @ 024185ec6ccb70b135c1ffa831d56cf447ea5657"
  new_claims:
    - "C235/C236: exact minimal support-seven classification and o(n^2) target-scale payment"
    - "C237: explicit payment for supports 7 <= k <= floor(3 sqrt(n)/4), n>=4096"
    - "C238/C239: JSS Theorem 1.5 plus Bonferroni reduces the source upper-bound obstruction to genuinely unstructured linear-support null vectors"
  retained_metric_evidence: "runs/R03/20260916T1408Z_12_support6_exactn9.md"
  audit_ids_for_R03:
    - "R02-AUDIT-R03-C227-01: PASS (claim-scoped only)"
    - "P26 full-package audit: NONE_YET"
    - "second OTHER-track full-package audit: NONE_YET"
  directed_audit_performed_this_run: "R03-AUDIT-R04-FM-C2-02 = PASS"
```

**NO CLOSURE CLAIM.**
