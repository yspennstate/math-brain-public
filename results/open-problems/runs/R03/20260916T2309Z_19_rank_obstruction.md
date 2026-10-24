Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED; GPT-6 / maximum was requested, but the exposed scheduler has no model-family selector, no reasoning-effort selector and no authenticated runtime telemetry, so GPT-6 maximum is not claimed. METRIC MOVED: `r(10)` improves from `275.9747699588589...` to `275.82523635048733...`, and `r(11)` from `525.1348531358815...` to `525.1251348632093...`. Section-B methods actually used: #26 HUNT THE SPORADIC CASE, #27 SWAP THE QUANTIFIERS, #3 PROVE SOMETHING STRONGER.**

Problem: **iid Rademacher square-matrix singularity — Komlós (1967) lineage; Jain--Sah--Sawhney (2021), Conjecture 1.1 specialized to uniform Rademacher; Sahasrabudhe (2025), Eq. (4.1). Overall source status: OPEN / R03 status: PARTIAL.**

# R03 run 19 — collision-free modular rank obstruction

Run ID: `20260916T2309Z_19_rank_obstruction`
Repository: `yspennstate/math-open-problems`, branch `master`.

## 1. Continuity, current source, target and fixed metric

Before new mathematics I recovered/reread the controlling campaign material on `master`: `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, newest own report `runs/R03/20260916T1909Z_18_second_incidence.md`, newest neighboring R02 report `runs/R02/20260916T1942Z_b7e3c9a1.md`, newest discoverable R04 report `runs/R04/20260916T191214Z_i0027_bottleneck_chain.md`, and the F0001/intake lineage by repository search. Large intake JSONL responses remain connector-truncated, so I do not claim a semantic row-by-row reread of every roughly 780 intake row.

Fresh primary-source/status checks on 2026-09-16 are archived separately in `artifacts/R03/20260916T2309Z_19_status_search.md`. The source chain remains:

- J. Komlós, *On the determinant of (0,1) matrices* (1967), historical lineage.
- Vishesh Jain, Ashwin Sah, Mehtaab Sawhney, *Singularity of discrete random matrices*, arXiv:2010.06554 / GAFA 31 (2021), Conjecture 1.1. Their sharp full theorem covers finite-support laws not uniform on their support; uniform-support laws including iid Rademacher remain only exponential-scale for the full singularity probability, while Theorem 1.5 handles the structured/almost-constant contribution sharply. Their introduction also records unresolved issues in the claimed Irmatov exact Rademacher resolution.
- Julian Sahasrabudhe, *Probabilistic combinatorics at exponentially small scales*, arXiv:2512.15077v1 (17 Dec 2025), Eq. (4.1), which records the exact iid sign asymptotic as open; the symmetric Bernoulli ensemble is treated separately.
- Tikhomirov's theorem remains `2^{-n+o(n)}` only.

For uniform signs, zero rows have probability zero and the two signed pair mechanisms give the source normalization

\[
\Pr(\det B_n=0)
=(1+o(1))\,2n(n-1)2^{-n}
=(1+o(1))\,n(n-1)2^{1-n}.
\]

Let `T_n` be the exact union of all signed equal/opposite row-pair and column-pair events. Retained C225 proves the matching lower asymptotic with explicit overlap correction. The fixed owner metric is

\[
\boxed{r(n):=2^n\Pr(\det B_n=0,\ T_n^c).}
\tag{M}
\]

Sharp source closure is equivalent to

\[
\boxed{r(n)=o(n^2).}
\]

Retained C240/C246 normalize to `m=n-1` and identify `T_n^c` with the class

\[
\mathcal G_m=
\{A\in\{0,1\}^{m\times m}:
\text{rows and columns are nonzero and pairwise distinct}\}.
\]

Retain C225--C255 and killed routes X27--X29 without re-derivation. In particular, run18's C253 writes, for a prime `p`,

\[
d_p(A)=m-\operatorname{rank}_{\mathbb F_p}A,
\quad
Z_1(d)={d\brack1}_p,
\quad
Z_2(d)={d\brack2}_p,
\]

and if `d_p(A)<=D`, then

\[
\mathbf 1_{\{d_p(A)\ge1\}}
\le
Z_1(d_p(A))
-
\frac{p(p^2-1)}{p^D-1} Z_2(d_p(A)).
\tag{1.1}
\]

The preceding `D` came only from the crude cube-count rank lower bound `rank >= ceil(log_2(m+1))`. R02 has now independently audited C253: `R02-AUDIT-R03-C253-04 = PASS`, claim scoped.

This run asks whether the collision-free row/column constraints force a *strictly larger modular rank*.

## 2. Method #26 — HUNT THE SPORADIC CASE: try to build the low-rank modular false positives

The modular certificate is weakened by real-nonsingular matrices with unusually large modular nullity. I therefore attacked the negation of the desired rank improvement first.

Suppose `A in G_m` has rank four over `F_p`. Choose four pivot columns whose coordinate projection identifies its row space with `F_p^4`. The `m` rows become distinct nonzero points

\[
U\subset\{0,1\}^4.
\]

Every ambient column becomes a linear form on `F_p^4` which is `{0,1}`-valued on all points of `U`. Since the columns of `A` are nonzero and pairwise distinct, a rank-four counterexample of order `m` requires at least `m` distinct nonzero such linear forms.

This is now a finite exact obstruction rather than a matrix enumeration.

### Exact search

For `p=7`, every 9-point subset of the 15 nonzero Boolean points admits at most **6** nonzero linear forms that are `{0,1}`-valued on all nine points.

For `p=11`, the corresponding maxima are **6** for nine points and **5** for ten points.

So the attempted rank-four collision-free counterexample does not exist at the first relevant sizes.

The checker does not stop there: it verifies the characteristic-stability argument below, so the rank-four obstruction is not just a `p=7` coincidence.

## 3. Method #27 — SWAP THE QUANTIFIERS: from matrices to point/form incidence

The matrix statement has two coupled distinctness conditions. The dual point/form statement separates them:

> instead of asking whether there exists an `m x m` collision-free binary matrix of rank four, ask whether there exists an `m`-point Boolean set `U` supporting `m` distinct nonzero linear forms that are simultaneously Boolean-valued on `U`.

This lets us prove a uniform characteristic statement.

### R03-C256a — universal rank-five floor for primes at least seven

**STATUS: PROVED; finite exact core.**

Let `p>=7` be prime and `A in G_m` with `m>=9`. Then

\[
\boxed{\operatorname{rank}_{\mathbb F_p} A\ge5.}
\tag{C256a}
\]

#### Proof

Assume rank four. As above, projection to four pivot columns produces `m` distinct nonzero points in the 4-cube and every matrix column becomes a nonzero linear form that is Boolean-valued on these points.

Take any nine projected rows. Nine distinct nonzero Boolean points cannot lie in a 3-dimensional linear subspace: projection of a 3-space to pivot coordinates is injective and hence contains at most `2^3-1=7` nonzero Boolean points. Thus these nine points span dimension four.

Choose four independent points among them and put them as rows of a Boolean `4 x 4` matrix `B`. A valid linear form is uniquely specified by its values `b in {0,1}^4` on this basis. Cramer's rule writes, for every Boolean point `u`,

\[
\ell(u)=\frac{N(B,b,u)}{\det B}.
\]

The exact checker exhausts all 940 invertible Boolean row bases, all 16 Boolean `b`, and all 15 nonzero Boolean `u`. It verifies

\[
\det B\in\{\pm1,\pm2,\pm3\},
\]

\[
|N(B,b,u)|\le5,\qquad
|N(B,b,u)-\det B|\le5.
\tag{3.1}
\]

For `p>=7`, therefore, `ell(u)` is congruent to `0` or `1` modulo `p` iff the corresponding rational value is exactly `0` or `1`: neither numerator in (3.1) can wrap by a nonzero multiple of `p`. Conversely each rational valid form reduces modulo 7, because `det B` is not divisible by 7.

Hence the number of valid forms on any nine-point set is characteristic-independent for all primes `p>=7`. The exact `p=7` enumeration gives maximum 6, but a collision-free rank-four `m x m` matrix would require at least `m>=9` distinct valid nonzero forms. Contradiction. QED.

The checker also exhibits rank-five collision-free matrices at `m=9` and `m=10`; thus C256a is not hiding a rank-six statement at those dimensions.

## 4. Method #3 — PROVE SOMETHING STRONGER: the next rank threshold

The rank-four obstruction suggested asking for the exact next cutoff rather than merely improving the coefficient at `n=10`.

### R03-C256b — rank six over F7 from order 12 onward

**STATUS: PROVED WITH EXHAUSTIVE FINITE CORE.**

For every `A in G_m` with `m>=12`,

\[
\boxed{\operatorname{rank}_{\mathbb F_7} A\ge6.}
\tag{C256b}
\]

Moreover, there exists an explicit `A in G_{11}` with `rank_{F_7} A=5`, so the threshold `m=12` is sharp at rank five.

#### Proof

If rank five, pivot-column projection gives a spanning set `U subset {0,1}^5 \ {0}` and the `m` distinct nonzero matrix columns become at least `m` distinct nonzero `F_7`-linear forms taking only values 0 or 1 on `U`.

It suffices to exclude the case `|U|=12`: if `m>12`, choose five rows forming a basis and add seven arbitrary other rows, producing a spanning 12-subset; every form valid on all `m` rows remains valid on this subset.

The exact checker enumerates all `7^5-1=16806` nonzero linear forms, stores for each of the 31 nonzero Boolean points the forms that are Boolean-valued there, and recursively exhausts all spanning 12-point subsets that could retain at least 12 candidate forms. Branches are pruned only after the candidate-form count falls below 12. It visits

\[
1,714,334
\]

search nodes and performs 6,825 terminal rank checks. No rank-five 12-point system survives. This proves the obstruction.

For sharpness at `m=11`, the checker contains literal 11-point and 11-form factors, verifies their product is a binary `11 x 11` matrix with nonzero pairwise-distinct rows and columns, and verifies exact `F_7` rank five. QED.

### R03-C256c — large-characteristic transfer

**STATUS: PROVED; finite exact core.**

For every prime `p>=31` and every `m>=12`,

\[
\boxed{\operatorname{rank}_{\mathbb F_p} A\ge6
\quad\text{for all }A\in\mathcal G_m.}
\tag{C256c}
\]

The checker exhausts all five-element subsets of the 31 nonzero Boolean 5-vectors and verifies that the maximum absolute determinant of a Boolean `5 x 5` matrix is 5. Thus in Cramer's rule each coordinate numerator is at most 5 in absolute value. For any Boolean `u` the numerator of `ell(u)` has absolute value at most 25, and its difference from `det B` has absolute value at most 30. Therefore for every prime `p>=31`, modular `{0,1}`-valuedness on a spanning Boolean set is equivalent to rational `{0,1}`-valuedness. Rational valid forms reduce modulo 7 because `|det B|<=5`. The p=7 rank-five obstruction from C256b therefore transfers to every prime `p>=31`. QED.

This stronger statement matters to the growing-prime modular route: the low-rank false positives are now ruled out uniformly, rather than prime by prime, at the first two nontrivial rank levels.

## 5. Metric update through C253

Run18 already certified exact first-incidence values `M_1` and rigorous lower bounds `M_2^{lb}` for the relevant sparse null 2-planes.

For `m=9,p=7`, C256a improves the modular-nullity ceiling from five to four, so (1.1) may use

\[
c_{7,9}
=\frac{7(7^2-1)}{7^4-1}
=\frac7{50}.
\]

Substituting the retained exact values gives

\[
\boxed{
r(10)
\le
\frac{159002423250871502925}{576460752303423488}
=
275.82523635048733\ldots .
}
\tag{C257.1}
\]

The run18 bound was `275.9747699588589...`, so the strict improvement is

\[
\boxed{0.1495336083715546\ldots .}
\]

For `m=10,p=11`, C256a gives modular nullity at most five and

\[
c_{11,10}
=\frac{11(11^2-1)}{11^5-1}
=\frac{132}{16105}.
\]

Hence

\[
\boxed{
r(11)
\le
\frac{4089622106045106025499398988925}
{7787900129957441143457185792}
=
525.1251348632093\ldots .
}
\tag{C257.2}
\]

The run18 bound was `525.1348531358815...`, giving strict improvement

\[
0.009718272672236305\ldots .
\]

Call (C257.1)--(C257.2) **R03-C257 — PROVED WITH EXECUTED EXACT CHECKER**.

### Complete-domain envelope retained

The exact collision-subtracted values remain

\[
r(1)=r(2)=r(3)=r(4)=0,
\]

\[
r(5)=225/256,\quad
r(6)=335475/65536,\quad
r(7)=149664375/8388608,
\]

\[
r(8)=1658391558075/34359738368,\quad
r(9)=15544095862461075/140737488355328.
\]

Use C257.1 at `n=10` and C257.2 at `n=11`.

For `n>=12`, retain the run18 full-domain minimum of C249, the exact projective first-incidence branches, and C255's analytic second-incidence family. C256 now strengthens the allowed nullity ceiling in every C253/C255 branch as follows:

\[
\operatorname{rank}_{\mathbb F_p}A
\ge
\max\{5,\lceil\log_2(m+1)\rceil\}
\quad(p\ge7,m\ge9),
\]

and

\[
\operatorname{rank}_{\mathbb F_p}A
\ge
\max\{6,\lceil\log_2(m+1)\rceil\}
\]

for `p=7,m>=12` and for every prime `p>=31,m>=12`.

Accordingly the coefficient `p(p^2-1)/(p^D-1)` in C253/C255 may use `D=m-rank_lower` rather than the old crude `m-ceil(log_2(m+1))`. This gives a rigorously no-worse complete-domain envelope and a strict improvement whenever the corresponding second-incidence lower bound is positive.

This is still **not** an `o(n^2)` bound. A constant increase in modular rank cannot by itself close the asymptotic target.

## 6. What the three methods changed

**#26 HUNT THE SPORADIC CASE.** I explicitly searched for the modular low-rank false positives that could make C253 sharp. Rank four disappears already at collision-free order nine for every prime at least seven. At rank five, the first genuine p=7 survivor exists at order eleven but disappears at order twelve. This gives a concrete obstruction and a sharp boundary, not a renamed coupling lemma.

**#27 SWAP THE QUANTIFIERS.** The useful object is not a matrix but a pair `(U,F)` consisting of Boolean points and linear forms, with every form Boolean-valued on every point. Row distinctness becomes distinct points; column distinctness becomes distinct forms. This dual incidence language is what makes exact rank cutoffs feasible.

**#3 PROVE SOMETHING STRONGER.** Instead of only improving the numerical `n=10` certificate, the run proves characteristic-uniform rank floors and a sharp p=7 rank-five cutoff. Those stronger statements feed the metric automatically and also constrain any future growing-prime modular argument.

The next methods should not repeat these three.

## 7. Prior-art boundary and exact obstruction still open

A bounded current search found adjacent results such as Bondy's induced-subsets theorem / witness-set formulations and modern work on binary matrices with distinct rows, but no exact finite-field rank threshold matching C256. This is not a novelty certificate.

The asymptotic obstruction is now clearer. The modular route still pays every *real-nonsingular but mod-p singular* matrix. C256 shows that the worst false positives cannot hide in very small modular rank, but the remaining nullity can still be linear in `m`. To reach `r(n)=o(n^2)` one needs one of:

1. a collision-conditioned determinant-residue theorem for a useful growing modulus, strong on the `2^{-n}` scale; or
2. a general rank-versus-order theorem for collision-free Boolean matrices strong enough that the projective incidence weights themselves become negligible; or
3. a return to the real corank-one / nonfat-hyperplane formulation with a weighted count that avoids modular false positives entirely.

The finite threshold data suggest defining the extremal parameter

\[
s_p(r)=
\max\{m:\exists A\in\mathcal G_m,\ 
\operatorname{rank}_{\mathbb F_p}A\le r\}.
\]

This run proves `s_p(4)<=8` for every prime `p>=7`, and `s_7(5)=11`. Understanding the growth of `s_p(r)` is a concrete new route, but it is an intermediate object, not a replacement source conjecture and not source closure.

Killed routes remain retained: X27 fixed-epsilon JSS diagonalization, X28 naive conditional row/column independence, X29 a fixed universally optimal prime, naive left/right-normal multiplication, and any exponential-rate estimate presented as though it resolved the polynomial prefactor.

## 8. Independent neighboring audit — R04

Newest R04 package actually read:
`runs/R04/20260916T191214Z_i0027_bottleneck_chain.md`.

I independently audited the new structural claim `R04-I0027-C3`, not the parent source conjecture.

### `R03-AUDIT-R04-I0027-C3-06 = PASS` — claim scoped

Assume `K(G_n)>=kappa n^3`. The retained elementary `K<=diam(G)m<=nm` yields `m>=(kappa+o(1))n^2`, hence the degree-weighted resistance sum `R*=2mK >= (2kappa^2-o(1))n^5`.

R04's uniform-spanning-tree cut identity gives an expected sum of `Q(e)=vol(A_e)vol(B_e)/|partial A_e|` equal to `R*`. Non-high edges with `Q<kappa^2 n^4` contribute at most `(kappa^2+o(1))n^5`, while every edge has `Q<=n^4/4`. Therefore some spanning tree has at least `(4kappa^2-o(1))n` high edges.

For every high edge, `vol(A)vol(A^c)>=kappa^2 n^4 |partial A|`, while the product is at most `n^4/4`; hence `|partial A|<=1/(4kappa^2)+o(1)`. Boundary at least one also forces both volumes at least `kappa^2n^2`, and simplicity converts these to side sizes at least `(kappa-o(1))n`.

Rooting the selected tree makes the high child-subtrees a laminar family. Any antichain is disjoint and each member has at least `(kappa-o(1))n` vertices, so its width is at most `1/kappa+o(1)`. Dilworth then yields a nested chain of length at least `(4kappa^3-o(1))n`, exactly as claimed.

**Audit verdict: PASS at the stated claim scope.** Novelty was not audited. This does not close Aldous--Fill 6.13.

## 9. Model/runtime and permission status

The model-setting limitation remains unchanged. The exposed native automation mutation schema has fields for title, prompt, schedule, timing mode and enabled state, but no model-family field and no reasoning-effort field; no authenticated runtime telemetry is exposed. Thus `GPT-6 / maximum` remains prompt text only.

Repository policy records that P26/P01/P03 modification probes once returned `You cannot modify this task`. Current `RESULTS.md` also records that P26 later updated successfully from a different authorized context. This is consistent with an ownership/workspace permission boundary, not a repository setting. The legitimate fix is to use the owning/admin-authorized native-task context if it exposes the desired model controls, or escalate to platform support. No duplicate task, permission bypass or scheduler mutation was attempted here.

## 10. Exact evidence

Executed checker:
`artifacts/R03/20260916T2309Z_19_rank_obstruction_exact.py`

Archived output:
`artifacts/R03/20260916T2309Z_19_rank_obstruction_exact.out`

Status/prior-art record:
`artifacts/R03/20260916T2309Z_19_status_search.md`

Checker output ends `SELF-CHECK PASS`.

Local SHA-256 of the executed compact checker:
`62d1ed75ccc41cc4fc1e8a25689382f95e1255326bbb30e5d5340a0fee7ceb61`.

Local SHA-256 of archived mathematical output:
`4d2944d0726783629db7cb995c217b448ef570b8d933c25d31c97dbfcab3462a`.

The Python environment emitted an unrelated spreadsheet-runtime warmup warning after the mathematical checker had completed successfully; it does not enter any proof step or output certificate.

## 11. Cumulative status ledger

- Exact source asymptotic: **OPEN**.
- Matching trivial-pair lower asymptotic with overlaps, C225: **PROVED**.
- Sign-to-binary collision-free normalization C240/C246: **PROVED / retained**.
- Fixed minimal-circuit supports 3--7 and growing support window: **PAID / retained; partition taxonomy partly known prior art**.
- JSS structured/almost-constant contribution: **KNOWN published reduction / retained**.
- C253 second projective-incidence correction: **PROVED; R02 independent claim-scoped audit PASS**.
- C254/C255 sparse null 2-plane lower bounds: **PROVED / retained**.
- **C256a rank >=5 for every p>=7, m>=9: PROVED NEW.**
- **C256b rank_F7 >=6 for m>=12, sharp at m=11: PROVED NEW.**
- **C256c rank >=6 for p>=31, m>=12: PROVED NEW.**
- **C257 strict metric improvements at n=10,11: PROVED NEW.**
- `r(10)<=275.82523635048733...`: **current strict certified value**.
- `r(11)<=525.1251348632093...`: **current strict certified value**.
- Full `r(n)=o(n^2)`: **OPEN**.
- P26 full-package R03 audit: **NONE YET**.
- Second independent full-package R03 audit: **NONE YET**.
- R02 C253 audit: **PASS, claim scoped**.
- R03 audit of newest R04 C3: **PASS, claim scoped**.

This is not a stuck episode: the frozen metric moved. The next run should not repeat methods #26/#27/#3. The most useful new direction is to attack the growth of `s_p(r)` or the determinant-residue false-positive mass with a genuinely asymptotic method, rather than adding another fixed-support circuit enumeration.

## ledger_delta

```yaml
source:
  historical: "Komlos 1967, On the determinant of (0,1) matrices"
  modern_locator: "Jain--Sah--Sawhney 2021, Conjecture 1.1; Sahasrabudhe 2025, Eq. (4.1)"
target: "P(det B_n=0)=(1+o(1))*2*n*(n-1)*2^{-n}"
metric: "r(n)=2^n P(det B_n=0, T_n^c), full-domain certified upper envelope"
before:
  r10: "3564857875550413515432975/12917332537615113519104 = 275.9747699588589..."
  r11: "446298905163058911334081193175/849874851189084309818441728 = 525.1348531358815..."
after:
  r10: "159002423250871502925/576460752303423488 = 275.82523635048733..."
  r11: "4089622106045106025499398988925/7787900129957441143457185792 = 525.1251348632093..."
status: PARTIAL
unchanged_count: 0
proof_ids: [R03-C256a, R03-C256b, R03-C256c, R03-C257]
exact_evidence:
  - "artifacts/R03/20260916T2309Z_19_rank_obstruction_exact.py"
  - "artifacts/R03/20260916T2309Z_19_rank_obstruction_exact.out"
  - "artifacts/R03/20260916T2309Z_19_status_search.md"
audit_ids:
  - "R02-AUDIT-R03-C253-04=PASS (prior imported claim, scoped)"
  - "P26 full-package R03 audit: NONE"
  - "second full-package R03 audit: NONE"
peer_audit_this_run:
  - "R03-AUDIT-R04-I0027-C3-06=PASS (claim scoped)"
```

No shared ledger, peer file, email, Drive, public posting, purchase, permission, workflow or scheduler state was changed.
