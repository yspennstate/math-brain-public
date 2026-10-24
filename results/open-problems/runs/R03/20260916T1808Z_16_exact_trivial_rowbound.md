Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED; GPT-6 / maximum was requested, but the exposed scheduler has no model or reasoning selector or authenticated runtime telemetry, so GPT-6 maximum is not claimed. METRIC MOVED: under the owner's exact-trivial-collision normalization, the retained C243 theorem translates to `r(10)<=449.6973203902413...`, and the new F3 hyperplane-tier refinement gives `r(10)<=437.96141105148837...`. Section-B methods actually used: #15 BREAK THE SYMMETRY, #25 COUNT THE SAME THING TWICE, #30 ONE PRIME / ONE SCALE / ONE DIRECTION.**
Problem: **iid Rademacher square-matrix singularity — Komlós (1967) lineage; Van H. Vu (2020), Section 2, Conjecture 2.2. Overall status: OPEN / PARTIAL.**

# R03 run 16 — exact trivial-collision subtraction and a refined F3 hyperplane sieve

Run ID: `20260916T1808Z_16_exact_trivial_rowbound`  
Repository: `yspennstate/math-open-problems`, branch `master`.

## 1. Recovery, source, target, metric

Before new work I reread/recovered the campaign controls `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, and `operations/NEW_METHODS_2026-09-16.md`; recovered newest own report `runs/R03/20260916T1708Z_15_f3_hyperplane_geometry.md`; searched the current intake/source records including R03's F0001 lineage; and checked the newest discoverable R04 package `runs/R04/20260916T161226Z_r04_riccati_siegel.md`. Large intake responses remain connector-truncated, so I do not claim a semantic row-by-row reread of every intake row.

Current source chain checked 2026-09-16:

1. J. Komlós, *On the determinant of (0,1)-matrices* (1967).
2. Van H. Vu, *Recent progress in combinatorial random matrix theory*, arXiv:2005.02797 (2020), Section 2, Conjecture 2.2. Section 2 is iid Rademacher; the symmetric ensemble is separate in Section 3.
3. Vishesh Jain, Ashwin Sah, Mehtaab Sawhney, *Singularity of discrete random matrices*, arXiv:2010.06554 / GAFA 31 (2021). Their sharp full asymptotic is for finite-support laws not uniform on support; uniform support, including iid Rademacher, remains exponential-scale for full singularity.
4. Julian Sahasrabudhe, *Probabilistic combinatorics at exponentially small scales*, arXiv:2512.15077v1 (17 Dec 2025), Eq. (4.1) exact iid sign target and Eq. (4.2) Tikhomirov's `2^{-n+o(n)}` theorem.
5. Thomas Voigt and Günter M. Ziegler, *Singular 0/1-matrices, and the hyperplanes spanned by random 0/1-vectors* (2006).
6. Miodrag Živković, *Classification of small (0,1) matrices* (2006).

No independently verified 2026 source-matching resolution was found in the bounded search. Exact query/provenance notes are in `artifacts/R03/20260916T1808Z_16_exact_trivial_rowbound_status_search.md`.

The source target is

\[
P(\det B_n=0)=(1+o(1))n(n-1)2^{1-n}=(1+o(1))2n(n-1)2^{-n}.
\]

Let `T_n` be the exact union of all signed equal/opposite row-pair and column-pair events. The owner-fixed metric is

\[
\boxed{r(n):=2^n P(\det B_n=0,\ T_n^c).}
\tag{M}
\]

Retained C225 already proves

\[
P(T_n)=2n(n-1)2^{-n}+O(n^4 4^{-n})
\]

with explicit overlap correction, so sharp closure is equivalent to `r(n)=o(n^2)`.

The preceding report did not ledger (M) explicitly, but retained C243 plus the exact `T_n^c` count proved below yields the reconstructed comparison baseline

\[
r(10)\le 449.6973203902413\ldots.
\]

This run strictly improves it.

Retain without re-deriving: C225; C226--C237 fixed/growing-support circuit payments; C238/C239 JSS structured reduction; C240 sign-to-binary normalization; C242/C243 F3 sieve; C244 corank>=2 target-negligibility; C245 Voigt--Ziegler hyperplane recoding; X27 invalid fixed-epsilon JSS diagonalization; and the killed naive left/right-normal multiplication route.

## 2. #15 BREAK THE SYMMETRY — row-good first, then glue columns

Retained C240 normalizes an iid sign matrix by

\[
N_{ij}=B_{ij}B_{i1}B_{1j}B_{11},\qquad A_{ij}=(1-N_{i+1,j+1})/2,
\]

where `A` is uniform binary of order `m=n-1`, and

\[
\det N=(-2)^m\det A.
\tag{2.1}
\]

Because the first normalized row/column is all `+1`:

- no signed row collision in `B` iff `A` has no zero row and pairwise-distinct rows;
- no signed column collision iff `A` has no zero column and pairwise-distinct columns.

Current exact binary sequences split the mechanisms:
`A000410(m)` = row-good singular matrices modulo row permutations;
`A000409(m)` = row-good singular matrices still having a zero/equal column;
`A116527(m)` = singular matrices good on both sides. Current identity:

\[
\boxed{A116527(m)=A000410(m)-A000409(m).}
\tag{2.2}
\]

### R03-X28 — exact obstruction to conditional row/column independence

**DISPROVED ROUTE.** At binary order `m=4`, labeled counts are

\[
S=42976,\quad R_{good}=C_{good}=4!\,425=10200,\quad B_{good}=4!\,75=1800.
\]

Conditional independence inside the singular class would require

\[
B_{good}S=R_{good}C_{good}.
\]

But

\[
1800\cdot42976=77356800\ne104040000=10200^2.
\]

Thus naive left/right or row/column probability multiplication fails already in the first nontrivial finite case.

## 3. #25 COUNT THE SAME THING TWICE — exact trivial complement

### R03-C246 — exact `T_n^c` probability

**PROVED.** Let `s(n,k)` be the signed Stirling number of the first kind. Then

\[
\boxed{
P(T_n^c)=2^{-n^2}\sum_{c,d=1}^n s(n,c)s(n,d)2^{2n-c-d+cd}.
}
\tag{C246.1}
\]

Equivalently, with `m=n-1`,

\[
\boxed{
P(T_n^c)=\frac{m!Q_m}{2^{m^2}},\qquad
Q_m=\sum_{k=1}^{m+1}s(m+1,k){2^{k-1}-1\choose m}.
}
\tag{C246.2}
\]

Here `Q_m` is OEIS A094000: binary `m x m` matrices with no zero rows/columns and all rows/columns distinct, modulo row permutations.

**Proof of (C246.2).** The normalization above preserves signed row/column-pair relations. Since the first normalized coordinate is `+1`, a signed pair becomes an equal pair. Equality of two non-first rows is equality of the corresponding binary rows; equality to the first row is a zero binary row. The same holds for columns. Hence `T_n^c` is exactly the event that `A` has nonzero pairwise-distinct rows and columns. A094000 counts those matrices modulo row permutations, and every orbit has size `m!`, proving (C246.2).

**Independent proof of (C246.1).** Inclusion-exclude over signed row and column pair constraints. Fix an underlying simple row graph `G` with `c` components. Balanced edge-signings are exactly vertex signings modulo one global flip per component, hence `2^(n-c)`; inconsistent signings have empty intersection. Similarly a column graph `H` with `d` components has `2^(n-d)` balanced signings. Given compatible signed `(G,H)`, one free matrix sign remains for every row-component/column-component pair, hence exactly `2^(cd)` sign matrices satisfy the constraints. Therefore the inclusion-exclusion numerator is

\[
\sum_{G,H}(-1)^{e(G)+e(H)}2^{n-c(G)}2^{n-c(H)}2^{c(G)c(H)}.
\]

The chromatic/Fortuin--Kasteleyn identity

\[
\sum_{G:c(G)=c}(-1)^{e(G)}=s(n,c)
\]

gives (C246.1). QED.

The checker exhausts all sign matrices through `n=4`, verifies the normalization/collision equivalence matrix-by-matrix, and checks (C246.1)=(C246.2) for `2<=n<=12`.

**Prior art.** The binary enumeration mechanism is not claimed novel: A094000 and related T0-hypergraph/binary-matrix families already encode it. The direct signed-graph proof is retained because it matches the exact R03 collision event without changing normalization.

## 4. R03-C247 — exact integer form of the residual

**PROVED identity; strict finite promotion through published binary order 8 only.** Let `a_m` count singular binary `m x m` matrices with no zero rows/columns and all rows/columns distinct, modulo row permutations (the A116527 object). Then

\[
\boxed{P(\det B_n=0,T_n^c)=\frac{m!a_m}{2^{m^2}},\qquad m=n-1,}
\tag{C247.1}
\]

so

\[
\boxed{r(n)=\frac{2^{m+1}m!a_m}{2^{m^2}}.}
\tag{C247.2}
\]

Thus the source conjecture after exact trivial subtraction is equivalent to

\[
\boxed{a_m=o\!\left(\frac{m^2 2^{m^2-m-1}}{m!}\right).}
\tag{C247.3}
\]

Živković's published classification covers binary orders through 8, giving strict exact R03 values

\[
\begin{array}{c|c}
n&r(n)\\ \hline
1,2,3,4&0\\
5&225/256\\
6&335475/65536\\
7&149664375/8388608\\
8&1658391558075/34359738368\\
9&15544095862461075/140737488355328.
\end{array}
\]

The current A116527 direct page has the order-9 term `1448479166136642150`, added 16 Jul 2026, implying the source-backed arithmetic value

\[
r(10)=\frac{2053219217998690247625}{9223372036854775808}=222.61047367431684\ldots.
\tag{C247.4}
\]

**Not promoted to the strict metric.** The corresponding A046747 order-9 total-singular term was added in July 2026, and the current TheoremDB audit records that no primary paper or independently replayable orbit certificate was located. The checker verifies the arithmetic but does not enumerate `2^81` matrices.

## 5. #30 ONE PRIME / FINAL HYPERPLANE SCALE

### R03-C248 — exact F3 nonfat hyperplane tiers

**PROVED.** Let

\[
H_a=\{x\in F_3^m:a\cdot x=0\},\quad a\ne0,
\]

projectively modulo `-1`. Let `s=|supp a|`; among nonzero coefficients let `p` be `+1` and `q` be `-1`. For uniform `U in {0,1}^m`,

\[
\boxed{\rho(a)=P(U\in H_a)=\frac13+\frac23 2^{-s}\cos((p-q)\pi/3).}
\tag{C248.1}
\]

The fat hyperplanes have density `1/2` and are exactly `x_i=0` and `x_i=x_j`. Among nonfat hyperplanes, `rho<=3/8`; equality occurs only for (i) support 3 with a `2+1` sign split, or (ii) support 4 with two plus and two minus coefficients. Their number is

\[
\boxed{N_{high}(m)=3{m\choose3}+3{m\choose4}.}
\tag{C248.2}
\]

Every other nonfat hyperplane satisfies

\[
\boxed{\rho\le11/32.}
\tag{C248.3}
\]

**Proof.** Let `omega=e^{2 pi i/3}`. Fourier inversion gives

\[
P(a\cdot U=0)=\frac13\sum_{t=0}^2\prod_{i:a_i\ne0}\frac{1+\omega^{t a_i}}2.
\]

Since `(1+omega)/2=(1/2)e^{i pi/3}` and its conjugate has phase `-pi/3`, (C248.1) follows. For support 1 the density is 1/2. For support 2, opposite coefficients give 1/2 and equal coefficients 1/4. For support 3, exactly the `2+1` split gives 3/8; modulo global sign there are 3 patterns per support. For support 4, exactly the balanced `2+2` split gives 3/8; again 3 projective patterns per support. For support 5 parity forces maximum cosine 1/2, giving at most 11/32; support 6 permits cosine 1, again giving 11/32; for support at least 7, `1/3+(2/3)2^{-7}<11/32`. QED.

The exact checker verifies every projective coefficient type through ambient dimension 12.

### R03-C249 — refined final-step F3 certificate

**PROVED; metric movement.** Retain C243 up to the first `m-1` rows and let `L^-_m` be its lower bound for their F3 independence probability. Let

\[
N_{fat}=m+{m\choose2}.
\]

Let `A_{m-1}` be C243's upper bound on ordered Boolean bases of a partition hyperplane (for dimension <=8, the minimum of the distinct-nonzero bound and the published real-invertible binary count; afterward, the distinct-nonzero bound). Put

\[
U_{fat}=\min\{1,N_{fat}A_{m-1}/2^{m(m-1)}\}.
\tag{C249.1}
\]

A high nonfat hyperplane has `h_m=3*2^(m-3)` Boolean points, one zero. Any ordered basis uses `m-1` distinct nonzero points, hence at most `(h_m-1)_{m-1}` ordered bases. Thus

\[
U_{high}=\min\left\{1,
\frac{(3{m\choose3}+3{m\choose4})(h_m-1)_{m-1}}{2^{m(m-1)}}\right\}.
\tag{C249.2}
\]

Then

\[
\boxed{\widetilde L_m=\frac{21}{32}L^-_m-\frac1{32}U_{high}-\frac5{32}U_{fat}}
\tag{C249.3}
\]

is a lower bound for F3 invertibility, hence for real invertibility.

**Proof.** Conditional on first `m-1` rows independent, their span is a hyperplane `H`. The final Boolean row hits ordinary nonfat `H` with probability at most `11/32`, high nonfat with `12/32`, and fat with `16/32`. Therefore

\[
P(I_m)\ge \frac{21}{32}P(I_{m-1})-\frac1{32}P(H\ high,I_{m-1})-\frac5{32}P(H\ fat,I_{m-1}).
\]

Substitute `L^-_m` and the counting upper bounds (C249.1)--(C249.2). QED.

At `m=9`,

\[
\widetilde L_9=\frac{245789156451795009795}{590295810358705651712}=0.4163830271850245\ldots,
\]

versus retained C243 `L_9=0.4049221782213986...`.

Since C246 gives exact `P(T_n^c)`, for every `n>=10`

\[
\boxed{r(n)\le R^{tier}_{F3}(n):=2^n\left[\frac{(n-1)!Q_{n-1}}{2^{(n-1)^2}}-\widetilde L_{n-1}\right]_+.}
\tag{C249.4}
\]

At `n=10`,

\[
\boxed{r(10)\le\frac{4039481031913758122055}{9223372036854775808}=437.96141105148837\ldots.}
\tag{C249.5}
\]

The retained C243 translation was `449.6973203902413...`, so the improvement is `11.73590933875294...`.

As a side effect, translating to the older leading-coefficient metric gives

\[
2^{10}P(\det B_{10}=0)-180\le417.6237801625349\ldots,
\]

improving the preceding `429.35968950128785...`. This remains a finite/uniform certificate, not target-scale asymptotics.

## 6. #30 continued — corank before gluing

### R03-C250 — at corank one, good columns iff the row span is nonfat

**PROVED REDUCTION.** Let `A` be a binary `m x m` matrix with nonzero pairwise-distinct rows and real corank one. Let `H` be its row-span hyperplane. Then

\[
\boxed{A\text{ has no zero/equal columns}\iff H\notin\{x_i=0,\ x_i=x_j\}.}
\tag{C250}
\]

If column `i` is zero, all rows lie in `x_i=0`; since both are hyperplanes, `H=x_i=0`. If columns `i,j` agree, similarly `H=x_i=x_j`. The converses are immediate. QED.

Retained C244 gives `P(corank B_n>=2)=2^{-2n+o(n)}`, so its target-normalized contribution is negligible. Hence the true asymptotic residual is localized to **corank-one nonfat real cube hyperplanes**, exactly the Voigt--Ziegler geometry, without multiplying left/right probabilities.

## 7. Methods outcome and limitations

- **#15:** succeeded as exact row-first decomposition and produced X28.
- **#25:** succeeded as two exact counts of `T_n^c`, binary and signed-graph.
- **#30:** succeeded quantitatively; the F3 final-hyperplane density tier improves the current certified residual envelope.

Retained failures/limits, without reset: Tikhomirov's exponential rate is not the prefactor; X27 fixed-epsilon JSS diagonalization is invalid; fixed-support enumeration alone is not asymptotic; modular F3 certificates have many real-nonsingular false positives and therefore are not asymptotically sharp; the July-2026 order-9 binary database term is not promoted without replayable primary certification; private entropy-defect conjectures remain intermediate only.

The remaining source obligation is

\[
\boxed{r(n)=2^nP(\det B_n=0,T_n^c)=o(n^2).}
\]

## 8. Exact evidence

Checker: `artifacts/R03/20260916T1808Z_16_exact_trivial_rowbound_exact.py`  
Output: `artifacts/R03/20260916T1808Z_16_exact_trivial_rowbound_exact.out`  
Status search: `artifacts/R03/20260916T1808Z_16_exact_trivial_rowbound_status_search.md`.

The checker exhausts all sign matrices through `n=4`, verifies both C246 formulas through `n=12`, checks current finite sequence arithmetic, marks the source-backed `n=10` exact candidate as **NOT PROMOTED**, verifies X28, verifies every F3 projective coefficient type through dimension 12, evaluates C249, and ends `SELF-CHECK PASS`.

Source SHA-256: `0f8c4a413ad0f8b87b3ccaeb2641656a92a3c77a2aa54dea9cc552b4314e7657`.  
Output SHA-256: `a16fccac6c48220bddea7ebc24a32e4ca39250f73f3e9c0e091aa55a15d37be3`.

## 9. R04 audit status

Newest R04 package found remains `runs/R04/20260916T161226Z_r04_riccati_siegel.md`. The preceding R03 run already independently audited its covariance claim and recorded `R03-AUDIT-R04-FM-C6-04=PASS` claim-scoped. No newer R04 package was found; no duplicate audit was manufactured.

## 10. Model/task interface

The native task-update schema still exposes prompt/title/schedule/enablement/timing but no model selector and no reasoning-effort selector. Prompt text can request GPT-6/maximum but cannot authenticate that runtime choice here. Repository policy records that some contexts returned `You cannot modify this task` for P26/P01/P03 while another authorized context later updated P26. This is an ownership/workspace authorization boundary. Legitimate remedy: use a task-owning authorized account/workspace context or platform support/owner intervention; do not duplicate the task or bypass permissions. No scheduler mutation was attempted.

## 11. Ledger

| Item | Status |
|---|---|
| Sharp iid source asymptotic | **OPEN** |
| C225 matching lower asymptotic incl. overlaps | **PROVED retained** |
| Supports 3--7 + C237 growing window | **PROVED/paid retained** |
| C244 corank>=2 target-negligible | **PROVED reduction retained** |
| C245 Voigt--Ziegler recoding | **KNOWN equivalence + synthesis** |
| **C246 exact trivial-complement count** | **PROVED NEW** |
| **C247 exact residual/A116527 identity** | **PROVED NEW identity** |
| Exact strict `r(n)` | **exact n=1..9** |
| Source-backed candidate `r(10)=222.61047...` | **NOT PROMOTED** |
| **X28 row/column independence** | **DISPROVED NEW** |
| **C248 F3 hyperplane tiers** | **PROVED NEW** |
| **C249 refined F3 envelope** | **PROVED NEW; metric moved** |
| **strict `r(10)` upper** | **437.96141105148837...** |
| **C250 corank-one nonfat equivalence** | **PROVED NEW** |
| Full `r(n)=o(n^2)` | **OPEN** |
| P26 full-package audit | **NONE YET** |
| second OTHER-track full-package audit | **NONE YET** |
| retained R02 audit C227 | **PASS claim-scoped** |
| retained R03 audit R04-C6 | **PASS claim-scoped** |

## 12. Next attack

C247/C250 identify the next object as corank-one nonfat hyperplanes spanned by Boolean points. Do not make support-eight enumeration the main route. Next triple should be **#3 PROVE SOMETHING STRONGER**, **#5 ADD A PARAMETER**, **#28 REPLACE FOR ALL WITH TYPICAL**: prove a density-tier theorem that includes spanning probability, optimize an entropy-vs-density threshold, and show a random spanned nonfat hyperplane has substantially lower typical cube density than the pointwise extremal bound. In Voigt--Ziegler language, the missing weighted estimate is that the expected nonfat contribution is `o(m^2)`.

## 13. structured ledger_delta

```yaml
ledger_delta:
  track: R03
  source: "Komlos 1967; Vu 2020 Section 2 Conjecture 2.2; JSS arXiv:2010.06554; Sahasrabudhe arXiv:2512.15077"
  target: "P(det B_n=0)=(1+o(1))*2*n*(n-1)*2^(-n), iid uniform signs"
  metric: "smallest R03-rigorous full-domain upper envelope for r(n)=2^n P(singular AND no signed row/column pair)"
  before_recorded: "UNMEASURED under newly owner-fixed exact-trivial normalization"
  before_reconstructed_from_C243:
    n10_upper: "4147725689935874803575/9223372036854775808 = 449.6973203902413..."
  after:
    exact_domain: "n=1..9"
    n_ge_10: "r(n) <= 2^n[(n-1)! A094000(n-1)/2^((n-1)^2) - L_tier(n-1)]_+"
    n10_upper: "4039481031913758122055/9223372036854775808 = 437.96141105148837..."
    improvement: "11.73590933875294..."
  source_backed_not_promoted:
    n10_candidate: "2053219217998690247625/9223372036854775808 = 222.61047367431684..."
  status: PARTIAL
  source_status: OPEN
  stagnation_count: UNKNOWN
  methods: [15,25,30]
  exact_evidence:
    - "artifacts/R03/20260916T1808Z_16_exact_trivial_rowbound_exact.py"
    - "artifacts/R03/20260916T1808Z_16_exact_trivial_rowbound_exact.out"
    - "artifacts/R03/20260916T1808Z_16_exact_trivial_rowbound_status_search.md"
  proof_ids: [R03-C246,R03-C247,R03-C248,R03-C249,R03-C250]
  killed_routes_new: [R03-X28]
  incoming_audits: ["R02-AUDIT-R03-C227-01=PASS retained claim-scoped"]
  outgoing_audits: ["R03-AUDIT-R04-FM-C6-04=PASS retained; no newer package"]
  full_package_audits: "P26 NONE; second OTHER-track NONE"
```

No shared root ledger, peer file, Gmail, Drive, email, public posting, purchase, permission change, workflow execution or scheduler state was changed.
