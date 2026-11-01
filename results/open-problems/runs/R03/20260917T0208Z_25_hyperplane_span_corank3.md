Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED; GPT-6 / maximum was requested, but this task interface exposes no model-family selector, no reasoning-effort selector, and no authenticated runtime telemetry, so GPT-6 maximum is not claimed. METRIC MOVED: `r(10) <= 275.7175955096563... -> 275.648865953934676...`, `r(11) <= 525.0751317961369... -> 524.988842147013479...`; consecutive unchanged count `0 -> 0`. Section-B methods actually used: #9 RANDOMIZE, #22 READ THE FAILURES NOT THE SUCCESSES, #23 DO WHAT THE PROPOSER DID NOT EXPECT.**

Problem/source: **iid nonsymmetric Rademacher square-matrix singularity — Komlós (1967) lineage; Vu arXiv:2005.02797, Section 2 / Conjecture 2.2; Jain--Sah--Sawhney arXiv:2010.06554, Conjecture 1.1 specialized to the uniform Rademacher law; Sahasrabudhe arXiv:2512.15077, Section 4. Overall source status: OPEN. R03 status: PARTIAL.**

# R03 run25 — product-slice hyperplane escape and exact modular corank three

Run ID: `20260917T0208Z_25_hyperplane_span_corank3`  
Repository/branch: `yspennstate/math-open-problems`, `master`.

## 1. Continuity, ownership, source gate, and frozen metric

I continued from the newest own report `runs/R03/20260917T0108Z_24_exact_corank2.md`; no proof state or stagnation count was reset. Before new mathematics I reread/recovered `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, the current R03 ownership material, the newest R04 report, and targeted R03/F0001/intake history. The large JSONL intake surfaces remain connector-truncated, so I do not claim a byte-for-byte visual reread of all roughly 780 entries.

The dated source/current-literature and failed-route check is archived at `artifacts/R03/20260917T0208Z_25_status_search.md`. The original historical source recovered is János Komlós, *On the determinant of (0-1) matrices*, Studia Sci. Math. Hungar. 2 (1967), 7--21. Current Jain--Sah--Sawhney records still separate their sharp theorem for non-uniform finite-support laws from the uniform-support case. Their paper explicitly says the latter is the main question left open by their work and records unresolved issues in Irmatov's claimed Rademacher resolution, including Theorem 3. Tikhomirov's theorem remains the exponential-rate result `(1/2+o(1))^n`. Hunter--Kwan--Sauermann--Sawhney (IMRN 2026) now gives `P(corank >= k) <= exp(-c n k)`, but this does not supply the sharp corank-one prefactor.

The source-matched iid sign target remains
\[
\Pr(\det B_n=0)
=(1+o(1))\,n(n-1)2^{1-n}
=(1+o(1))\,2n(n-1)2^{-n}.
\]
Let `T_n` be the exact union of all signed equal/opposite row-pair and column-pair events. Retained C225 gives the matching lower asymptotic with overlaps. The fixed upper metric is
\[
\boxed{r(n):=2^n\Pr(\det B_n=0,\ T_n^c),}
\tag{M}
\]
and source closure is equivalent to
\[
\boxed{r(n)=o(n^2).}
\]

Under retained C240/C246, `m=n-1` and the collision-free residual becomes
\[
\mathcal G_m=
\{A\in\{0,1\}^{m\times m}:\text{rows and columns are nonzero and pairwise distinct}\}.
\]
The run24 replay-certified baselines were
\[
r(10)\le
\frac{635761490123149925535}{2305843009213693952}
=275.7175955096563\ldots,
\]
\[
r(11)\le
\frac{4089232687152555736280595956925}
{7787900129957441143457185792}
=525.0751317961369\ldots.
\]
The external OEIS-derived `r(10)=222.6104736743...` remains source-backed but **not replay-certified** and is not promoted.

The killed-route ledger remains live: X27 fixed-`epsilon` JSS diagonalization, X28 conditional row/column independence, X29 fixed-best-prime, naive multiplication of left/right normal probabilities, and exponential-rate-only arguments. Run23 additionally killed universal high modular-rank as the asymptotic route. No failure count was reset.

## 2. Method #22 — read the failures before choosing a new route

I reread the August sharp-Rademacher campaign synthesis, especially `probability_1000/sharp_rademacher_campaign_2026_08_18/ITERATION2_SYNTHESIS.md`. The useful lesson is negative and specific:

- the second-moment Band III was false;
- the cluster lemma was false;
- raw span dimension was the wrong invariant;
- the dense connector-incoherent / Layer-III transfer never moved;
- the old campaign itself warned against double-counting anticoncentration and against using typicality without a cardinality payment.

This agrees with the current Jain--Sah--Sawhney diagnosis: their structured/compressible part is sharp; the unresolved uniform-support difficulty is in the unstructured sector. Therefore I did **not** restart the old cluster/certificate program and did not call a new bounded-support lemma an asymptotic solution.

The route chosen instead asks whether the existing modular incidence majorant can be made quantitatively tighter by certifying **exact modular corank** on explicit matrix families. Run24 did this for corank two. The new idea is to obtain a stronger spanning count by random escape from proper subspaces, and then extend the construction to exact corank three.

## 3. Retained modular majorant and its exact-corank slack

Fix an odd prime `p`. For `A in G_m` write
\[
d_p(A)=m-\operatorname{rank}_{\mathbb F_p}A.
\]
Retained C253 uses
\[
Z_1(d)={d\brack1}_p,\qquad Z_2(d)={d\brack2}_p,
\]
and, with a certified nullity ceiling `D`,
\[
c_{p,D}=\frac{p(p^2-1)}{p^D-1}
\]
to prove
\[
\mathbf 1_{\{d\ge1\}}
\le
\Phi_{p,D}(d):=Z_1(d)-c_{p,D}Z_2(d).
\tag{3.1}
\]

If a certified subset has exact modular nullity `k`, the pointwise excess in (3.1) is the explicit number
\[
\boxed{
\sigma_{p,D}(k):=
{k\brack1}_p-c_{p,D}{k\brack2}_p-1.
}
\tag{3.2}
\]
For `k=2`, this is `p-c_{p,D}` as used in run24. For `k=3`, since
\[
{3\brack1}_p={3\brack2}_p=p^2+p+1,
\]
we have
\[
\boxed{
\sigma_{p,D}(3)=(1-c_{p,D})(p^2+p+1)-1.
}
\tag{3.3}
\]

Thus an injectively counted family of exact-corank-`k` matrices permits an additional subtraction of `sigma_{p,D}(k)` per matrix from the C253 majorant.

## 4. Method #9 RANDOMIZE — a 2/3 hyperplane escape lemma

Let
\[
T:=\{(0,0),(1,0),(0,1)\}\subset\mathbb F_p^2.
\]
Take `k` pairwise-disjoint triples of coordinates and, on each triple, one projective balanced relation of type `(1,1,-1)`. Let the resulting relation vectors be `v_1,...,v_k` and put
\[
V=\operatorname{span}_{\mathbb F_p}\{v_1,\ldots,v_k\}.
\]
Because the supports are disjoint, every nonzero combination activating exactly `t` generators has support exactly `3t`. Hence the support-three projective lines in `V` are exactly the `k` generator lines. In particular `V` contains no vector of support one or two.

The Boolean slice of the orthogonal complement is
\[
C_V:=V^\perp\cap\{0,1\}^m.
\]
One balanced triple relation `x_1+x_2=x_3` has the three Boolean solutions
\[
(0,0,0),(1,0,1),(0,1,1),
\]
so after using `(u,v)` as coordinates on each relation block,
\[
C_V\cong T^k\times\{0,1\}^{m-3k}.
\]
Consequently
\[
\boxed{
h_{m,k}:=|C_V|=3^k2^{m-3k}.}
\tag{4.1}
\]
Also `dim(V^perp)=d:=m-k`.

### R03-C270a — product-slice hyperplane cap

**STATUS: PROVED.** Every proper linear hyperplane `H<V^perp` satisfies
\[
\boxed{|H\cap C_V|\le\frac23 h_{m,k}.}
\tag{C270a}
\]

**Proof.** Write a nonzero linear functional on `V^perp` in the independent coordinates consisting of the `k` pairs in `T^k` and the `m-3k` free Boolean bits. If it depends nontrivially on one `T` block, condition on all other coordinates. On that block the relevant affine equation has the form
\[
a u+b v=t
\]
with `(a,b)!=(0,0)`. Across `T`, the three values of the left side are `0,a,b`, so any target has at most two preimages. The conditional zero probability is therefore at most `2/3`. If the functional is zero on every `T` block, it depends on a free Boolean bit; conditioning on the others leaves at most one of two bit values. That probability is at most `1/2`. This proves the `2/3` cap. `square`

This has a useful random interpretation: if `X` is uniform on `C_V`, then after any nonzero set of selected columns spans a proper subspace of `V^perp`, a fresh `X` escapes that span with probability at least `1/3`.

There is a second independent bound. Any `j`-dimensional linear subspace of `F_p^m` contains at most `2^j` Boolean vectors, by projecting injectively to `j` pivot coordinates. Therefore, after `j<d` independent columns have been selected, their span contains at most
\[
\min\{2^j,\tfrac23h_{m,k}\}
\]
points of `C_V`.

It follows that the number of ordered Boolean bases of `V^perp` contained in `C_V` is at least
\[
\boxed{
B^*_{m,k}:=
\prod_{j=0}^{m-k-1}
\left(h_{m,k}-\min\{2^j,\tfrac23h_{m,k}\}\right).
}
\tag{4.2}
\]
This is the derandomized count extracted from the random-escape observation.

## 5. Method #23 — go opposite the expected corank-one mechanism

The proposer/source asymptotic predicts that the leading real-singular contribution is corank one and comes from elementary signed row/column collisions. Instead of attacking that expected leading sector directly, this run intentionally exploits the **higher modular-corank false positives** of the modular certificate: those matrices make C253 overpay by an exactly known amount, so exact higher-corank families can tighten the upper bound even though they cannot be the source's leading mechanism.

The number of distinct `k`-planes `V` constructed above is
\[
\boxed{
N_{m,k}=\frac{(m)_{3k}}{2^k k!}.
}
\tag{5.1}
\]
Indeed, the number of unordered collections of `k` disjoint triples is `(m)_{3k}/((3!)^k k!)`, and on every triple there are three projective balanced `(1,1,-1)` lines. The support-three projective lines are intrinsic in `V`, so this count has no duplicate planes.

Choose the first `d=m-k` matrix columns to be one of the bases counted by (4.2). After those basis columns, there are
\[
h_{m,k}-1-d=h_{m,k}-m+k-1
\]
unused nonzero Boolean vectors in `C_V`. Choose the final `k` matrix columns as ordered distinct vectors from this set. Thus, whenever the displayed falling factorial is positive, the construction gives at least
\[
\boxed{
E^*_{m,k}
:=N_{m,k}B^*_{m,k}
\bigl(h_{m,k}-m+k-1\bigr)_k
}
\tag{5.2}
\]
matrices.

Every such matrix lies in `G_m`. Its columns span all of `V^perp`, so its left modular nullspace is **exactly** `V`, hence its modular nullity is exactly `k`. Because `V` contains no support-one vector, no row is zero; because it contains no support-two vector `e_i-e_j`, no two rows are equal. Columns are nonzero and distinct by construction. Different `V` cannot count the same matrix because the exact left nullspace is unique.

### R03-C270b — explicit exact-corank-k family

**STATUS: PROVED.** For every odd prime `p`, every `k>=2`, and every `m>=3k` for which the final falling factorial is positive, `G_m` contains at least `E^*_{m,k}` matrices of exact modular nullity `k`, with `E^*_{m,k}` given by (5.2).

For `k=2`, this strictly strengthens run24 C268. At `m=9` and `m=10` the new basis product is exactly **three times** the old cube-only greedy product:
\[
B^*_{9,2}=1,162,798,694,400
=3\cdot 387,599,564,800,
\]
\[
B^*_{10,2}=21,283,867,302,297,600
=3\cdot7,094,622,434,099,200.
\]
Therefore the run24 certified exact-corank-two family itself triples at both finite dimensions.

For `k=3`, the projective support spectrum is
\[
\#\{\text{support }3\}=3,
\quad
\#\{\text{support }6\}=3(p-1),
\quad
\#\{\text{support }9\}=(p-1)^2,
\]
which the exact checker verifies at `p=7,11`.

## 6. Finite exact strengthening at m=9, k=3

The general lower bound (4.2) is not the best finite count at `m=9`. Here `C_V` is exactly `T^3`, a 27-point subset of `F_7^6`. I therefore performed an exact finite computation only after the new route was established.

The checker exhausts all
\[
\frac{7^6-1}{7-1}=19,608
\]
projective hyperplanes of `F_7^6`; the largest intersection with `T^3` has size exactly `18`, confirming the `2h/3` bound sharply in this finite case. It then exhausts all
\[
\binom{26}{6}=230,230
\]
six-subsets of the nonzero points of `T^3` and finds exactly
\[
\boxed{103,089}
\]
unordered bases, or
\[
\boxed{74,224,080}
\]
ordered bases.

Thus at `m=9,k=3`, replacing the general basis lower bound by the exact count gives
\[
N_{9,3}=7560,
\qquad
(27-9+3-1)_3=(20)_3=6840,
\]
and therefore
\[
\boxed{
E_{9,3}^{\rm exact}
=3,838,156,866,432,000.
}
\tag{6.1}
\]
The complete enumeration and exact rank tests are in the run25 checker/output.

At `m=10,k=3`, the general theorem gives
\[
h=54,\quad d=7,\quad N_{10,3}=75,600,
\]
with basis factors
\[
53,52,50,46,38,22,18,
\]
so
\[
B^*_{10,3}=95,386,262,400,
\]
and
\[
\boxed{
E^*_{10,3}=656,796,226,922,035,200,000.
}
\tag{6.2}
\]

## 7. R03-C271 — corrected modular branch and metric movement

Let `S_k` be any certified subset of `G_m` of exact modular nullity `k`. On `S_k`, subtracting the exact slack `sigma_{p,D}(k)` from the right side of (3.1) leaves equality `1`; outside it, keep (3.1) unchanged. Hence, for pairwise-disjoint exact-nullity subsets,
\[
\#\{A\in\mathcal G_m:d_p(A)\ge1\}
\le
M_{1,p,m}-c_{p,D}M_{2,p,m}
-\sum_k\sigma_{p,D}(k)|S_k|.
\tag{7.1}
\]
Replacing `M_2` by any certified lower bound `L_2` remains valid because `c_{p,D}>0`.

The exact-nullity-two and exact-nullity-three families are automatically disjoint. Therefore the run24 C269 branch can be sharpened in two independent ways:

1. replace its old `k=2` family by the larger C270b family; and
2. subtract the new `k=3` slack as well.

This proves **R03-C271 — PROVED**. For a retained C253 branch, the full-domain replacement is obtained by subtracting
\[
2^{m+1-m^2}
\sum_{k=2}^{\min(3,D)}
\sigma_{p,D}(k)E^*_{m,k},
\tag{7.2}
\]
with the stronger exact `m=9,k=3` count (6.1) used where applicable. For values of `m` where a family is unavailable, its term is zero. Taking the minimum with every previous nonmodular branch preserves the complete `n`-domain envelope.

### n=10

Here `m=9,p=7,D=4`, so retained
\[
c_{7,4}=\frac7{50}.
\]
The strengthened `k=2` basis count triples the run24 family; since one copy of its correction was already included in the run24 baseline, the **additional** exact-corank-two subtraction is
\[
\boxed{
2\Delta^{(2)}_{7,9}
=\frac{1207729927215}{17592186044416}
=0.06865149812341542\ldots .
}
\]

For `k=3`,
\[
\sigma_{7,4}(3)
=\frac{2401}{50}=48.02,
\]
and the exact basis enumeration gives the additional correction
\[
\boxed{
\Delta^{(3)}_{7,9}
=\frac{359977134230595}{4611686018427387904}
=0.00007805759819558343\ldots .
}
\]
Therefore
\[
\boxed{
r(10)\le
\frac{1271206021115125771515}{4611686018427387904}
=275.6488659539346766636\ldots .
}
\tag{C271.10}
\]
The total strict improvement over run24 is
\[
0.06872955572161100544\ldots .
\]

### n=11

Here `m=10,p=11,D=5`, with retained
\[
c_{11,5}=\frac{132}{16105}.
\]
Tripling the run24 `k=2` basis family yields the additional correction
\[
\boxed{
2\Delta^{(2)}_{11,10}
=\frac{319925953077122266875}{3713560166338654109696}
=0.08615073911473742\ldots .
}
\]
For `k=3`,
\[
\sigma_{11,5}(3)=\frac{2108304}{16105},
\]
and C270b gives
\[
\boxed{
\Delta^{(3)}_{11,10}
=\frac{1056462182925899124375}{7605371220661563616657408}
=0.00013891000876535797\ldots .
}
\]
Therefore
\[
\boxed{
r(11)\le
\frac{4088560671982932827043671156925}
{7787900129957441143457185792}
=524.9888421470134789547\ldots .
}
\tag{C271.11}
\]
The total strict improvement over run24 is
\[
0.08628964912350277221\ldots .
\]

The exact checker `artifacts/R03/20260917T0208Z_25_hyperplane_span_corank3_exact.py` exhaustively verifies the `m=9,k=3,p=7` finite core, checks all 19,608 projective hyperplanes, all 230,230 candidate six-subsets, the `k=2` factor-three improvement, the support spectra, and every rational metric update. Its archived output ends `SELF-CHECK PASS`.

## 8. Complete-domain envelope and asymptotic limitation

The exact retained values remain
\[
r(1)=r(2)=r(3)=r(4)=0,
\]
\[
r(5)=\frac{225}{256},\quad
r(6)=\frac{335475}{65536},\quad
r(7)=\frac{149664375}{8388608},
\]
\[
r(8)=\frac{1658391558075}{34359738368},\qquad
r(9)=\frac{15544095862461075}{140737488355328}.
\]
Use C271.10 and C271.11 at `n=10,11`. For every later `n`, retain the previous minimum of all valid C249/C252/C253/C255/C256/C258/C260/C261/C269 branches but replace an applicable C269 modular branch by the stronger C271 formula (7.2). Thus the complete `n`-range remains rigorously covered and is nowhere weakened.

This is still **not** an asymptotic solution. For fixed `k`,
\[
\frac{h_{m,k}}{2^m}=\left(\frac38\right)^k.
\]
Even the total number of matrices produced from all such `k`-planes is at most polynomial in `m` times `h_{m,k}^m`. After the normalization `2^{m+1-m^2}`, the contribution of this fixed-`k` sparse family is at most
\[
\operatorname{poly}(m)
\left(\frac38\right)^{km}.
\]
For `k=3` this is `poly(m)(27/512)^m`. Hence bounded numbers of disjoint support-three relations give genuine finite metric movement but are exponentially too small to establish `r(n)=o(n^2)`.

That limitation agrees with the 2026 large-corank literature: high corank is strongly suppressed. The source-level obstruction remains the collision-free **small-corank dense/unstructured sector**, equivalently the dense primitive CRT-null-witness sector from run22 after accidental determinant divisibility is eliminated by enough primes.

The next useful direction should therefore use the random-escape idea on dense or growing-support null spaces rather than enumerate another bounded sparse family. A successful asymptotic theorem would need a distributional statement at the actual source scale, roughly `o(n^2 2^{-n})`, not an unspecified `e^{-cn}` error.

## 9. What happened to the three Section-B methods

- **#9 RANDOMIZE — succeeded.** Uniform sampling from the Boolean product slice `C_V` escapes every proper span with probability at least `1/3`. Combining this with the cube/subspace bound produced the stronger deterministic basis product (4.2), tripling the previously certified exact-corank-two family at `m=9,10` and enabling a new exact-corank-three family.
- **#22 READ THE FAILURES — succeeded as route pruning.** The August campaign's refereed failures and Jain--Sah--Sawhney's own uniform-support diagnosis rule out simply returning to the broken cluster/span program. No claim is made that this proves a negative theorem about all possible Layer-II methods.
- **#23 DO WHAT THE PROPOSER DID NOT EXPECT — succeeded finitely, not asymptotically.** Instead of attacking the expected leading corank-one elementary dependencies, I exploited the slack generated by exact modular corank two and three. This moved the fixed metric but the fixed-support family is exponentially negligible, so it remains PARTIAL.

## 10. R04 independent-audit obligation

The newest R04 package at this run is `runs/R04/20260917T0112Z_i0027_stuck_thinking_01.md`, a mandatory thinking/stuck report. It explicitly makes no new R04 theorem claim or checker and says its remaining obligation is the missing P26 end-to-end audit. R03 already supplied the distinct non-P26 C8/C11 audits in earlier runs. I therefore did **not** manufacture a duplicate R04 audit this run.

## 11. Model/runtime and permission status

The model-setting limitation is still real and unchanged in the exposed interface. The available task mutation fields are prompt/title/schedule/timing/enabled state; there is **no model-family field and no reasoning-effort field**, and there is no authenticated runtime telemetry proving GPT-6/maximum. Therefore the prompt request is not a verified runtime setting.

The repository ledger records that one context previously returned `You cannot modify this task` for P26/P01/P03, while a different authorized P/C context later successfully updated P26. The consistent interpretation is an ownership/workspace authorization boundary. The legitimate remedy is an owning/admin-authorized native-task surface that exposes the desired model controls, or platform support. R03 did not create a duplicate, bypass permissions, or change scheduler state.

## 12. Structured ledger delta

```yaml
ledger_delta:
  track: R03
  source: "Komlos 1967 lineage; Vu 2020 Conj. 2.2; Jain-Sah-Sawhney arXiv:2010.06554 Conj. 1.1, uniform Rademacher specialization"
  target: "P(det B_n=0)=(1+o(1))*n*(n-1)*2^(1-n)"
  metric: "r(n)=2^n P(det B_n=0, T_n^c), complete-domain certified upper envelope"
  before:
    r10: "635761490123149925535/2305843009213693952 = 275.7175955096563..."
    r11: "4089232687152555736280595956925/7787900129957441143457185792 = 525.0751317961369..."
  after:
    r10: "1271206021115125771515/4611686018427387904 = 275.648865953934676..."
    r11: "4088560671982932827043671156925/7787900129957441143457185792 = 524.988842147013479..."
  movement: "strict improvement at n=10 and n=11; full n-domain retained"
  status: PARTIAL
  source_status: OPEN
  unchanged_count_before: 0
  unchanged_count_after: 0
  new_claims:
    - "R03-C270a: 2/3 hyperplane cap for the T^k Boolean product slice"
    - "R03-C270b: explicit exact modular-corank-k family with hybrid random-escape/cube basis count"
    - "R03-C271: exact-corank-2/3 slack correction of retained C253 branches"
  exact_evidence:
    checker: "artifacts/R03/20260917T0208Z_25_hyperplane_span_corank3_exact.py"
    output: "artifacts/R03/20260917T0208Z_25_hyperplane_span_corank3_exact.out"
    output_status: "SELF-CHECK PASS"
  prior_art_status: "bounded fresh search; no later accepted sharp-prefactor resolution surfaced; novelty unverified"
  retained_audits:
    - "R02-AUDIT-R03-C253-04=PASS (claim-scoped historical dependency)"
  new_external_R03_audits: []
  P26_full_package_R03_audit: ABSENT
  second_full_package_R03_audit: ABSENT
```

Overall status: **PARTIAL / source OPEN / fixed metric moved / unchanged count 0.** No source closure claim, no paper package, and no shared-root edit.

Artifacts for this run were written and read back at their actual commits before this report: checker commit `6924d51aa5620aea11b14b0be336288b48c58b06`; output commit `814e34cf69d396dc04408158ae8da0c8f1074a86`; dated source/failure-search commit `6211a0355bf549e08c632f5293d734fe69327e17`. No email, Drive, public posting, purchase, permission change, workflow execution, peer-file edit, or scheduler change was made.
