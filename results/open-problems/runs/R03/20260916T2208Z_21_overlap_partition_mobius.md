Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED; GPT-6 / maximum was requested, but the exposed interface has no model-family selector, no reasoning-effort selector, and no authenticated runtime telemetry, so GPT-6 maximum is not claimed. METRIC MOVED: `r(10)` improves from `275.8202561002904...` to `275.751921258717971...`, and `r(11)` from `525.1244565083956...` to `525.118207165694344...`. Section-B methods actually used: #6 DEFORM TO A POINT YOU CAN SOLVE, #14 FIND THE GROUP ACTING, #19 MAKE IT AN ALGORITHM.**

Problem/source: **iid Rademacher square-matrix singularity — Komlós (1967) lineage; Van H. Vu (2020), Section 2, Conjecture 2.2; Jain--Sah--Sawhney (2021), Conjecture 1.1 specialized to uniform Rademacher; Sahasrabudhe (2025), Section 4 / Eq. (4.1). Overall source status: OPEN. R03 status: PARTIAL.**

# R03 run21 — partition Möbius inversion and overlap-one modular planes

Run ID: `20260916T2208Z_21_overlap_partition_mobius`  
Repository: `yspennstate/math-open-problems`, branch `master`.

## 1. Recovery, current source status, and fixed metric

Before new mathematics I recovered/reread the campaign controls `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`; newest own report `runs/R03/20260916T2114Z_20_balanced_plane_packing.md`; newest ready R04 package `runs/R04/20260916T2127Z_i0027_er_cluster_closure.md`; and targeted intake/F0001 material. The large intake JSONL surfaces remain connector-truncated, so I do not claim a visual row-by-row reread of every roughly 780 intake record.

Fresh literature searches are archived in `artifacts/R03/20260916T2208Z_21_status_search.md`. The assigned outside target remains open. Jain--Sah--Sawhney's sharp full theorem applies when the finite-support entry law is not uniform on its support; uniform Rademacher remains only exponential-scale at the full-singularity level. Sahasrabudhe's December 2025 survey still records the precise iid-sign upper asymptotic as open. Orellana Mateo--Urschel--West (arXiv:2608.08998, August 2026) is later adjacent primary literature on strong nonsingularity/LU factorization and exact binary counts, not a resolution of this sharp singularity target. Symmetric Bernoulli matrices remain a separate dependent-entry ensemble.

The exact target normalization is
\[
\Pr(\det B_n=0)
=(1+o(1))\,n(n-1)2^{1-n}
=(1+o(1))\,2n(n-1)2^{-n}.
\]
Let `T_n` be the exact union of signed equal/opposite row-pair and column-pair events. Retained C225 proves the matching lower asymptotic with explicit overlap correction. The fixed R03 upper metric therefore remains
\[
\boxed{r(n):=2^n\Pr(\det B_n=0,\ T_n^c).}
\tag{M}
\]
The source closes exactly if
\[
\boxed{r(n)=o(n^2).}
\]

Retained C240/C246 put `m=n-1` and identify `T_n^c` with
\[
\mathcal G_m=
\{A\in\{0,1\}^{m\times m}:\text{rows and columns are nonzero and pairwise distinct}\}.
\]
For an odd prime `p`, retained C253 bounds the real-singular count inside `\mathcal G_m` by a first projective null incidence minus a positive multiple of the second projective null incidence. The bottleneck of runs18--20 was therefore to count many null 2-planes without losing the row/column collision exclusion.

Prior killed routes remain killed and their stagnation history is not reset: fixed-epsilon JSS diagonalization X27, conditional row/column independence X28, fixed-best-prime X29, naive left/right-normal multiplication, and exponential-rate-only bounds. This run is not a stuck run because the frozen metric moves.

## 2. Method #6 — DEFORM TO A POINT YOU CAN SOLVE: exact row-collision removal by partition Möbius inversion

Run20 counted matrices carrying a fixed null plane by taking distinct nonzero allowed columns and then subtracting row-collision events by a union bound. That leaves avoidable slack. The solvable deformation is to force a prescribed row-equality partition first, count exactly there, and Möbius-invert back to the discrete partition.

Fix a prime `p`, an integer `m`, and a subspace
\[
V\le\mathbb F_p^m.
\]
Adjoin an artificial row `0`, identically zero, to the `m` actual rows. Let `Pi_{m+1}` be the set-partition lattice of
\[
\{0,1,\ldots,m\}.
\]
For `pi in Pi_{m+1}`, let `B_0(pi)` be its block containing `0`, and define `h_V(pi)` to be the number of Boolean column vectors
\[
y\in V^\perp\cap\{0,1\}^m
\]
which vanish on `B_0(pi)\setminus\{0\}` and are constant on every other block of `pi`.

The partition-lattice Möbius function from the discrete partition is
\[
\mu(\hat0,\pi)
=\prod_{B\in\pi}(-1)^{|B|-1}(|B|-1)!.
\tag{2.1}
\]

### R03-C260 — exact collision-free incidence formula

**STATUS: PROVED.** For every prime `p`, every `m`, and every subspace `V<=F_p^m`,
\[
\boxed{
C_m(V)
:=
\#\{A\in\mathcal G_m:V\le\ker(A^T\bmod p)\}
=
\sum_{\pi\in\Pi_{m+1}}
\mu(\hat0,\pi)\,(h_V(\pi)-1)_m.
}
\tag{C260}
\]
Here `(x)_m=x(x-1)\cdots(x-m+1)`.

### Proof

For an ordered `m`-tuple of columns, define its equality partition `sigma` on rows `0,1,...,m`: indices belong to the same block precisely when the corresponding row vectors are equal, with row `0` the all-zero row. The condition that all actual rows are nonzero and pairwise distinct is exactly
\[
\sigma=\hat0.
\]

Fix a partition `pi`. Requiring `sigma>=pi` means each selected column is constant on every block of `pi` and zero on the block containing row `0`. Requiring `V<=ker(A^T mod p)` means each selected column belongs to `V^perp`. Thus there are exactly `h_V(pi)` allowed Boolean column values, one of which is the zero column. The definition of `\mathcal G_m` also requires all columns nonzero and pairwise distinct, so the number of ordered column choices compatible with `pi` is exactly
\[
(h_V(\pi)-1)_m.
\]
Möbius inversion on the partition lattice isolates the discrete equality partition and gives C260. QED.

This removes the run20 row-collision union-bound slack exactly, for any fixed modular null subspace. It is a reusable theorem, not tied to the two finite metrics below.

The exact checker independently verifies C260 against brute-force enumeration of all `2^16` binary `4x4` matrices in two cases: a nonzero null-line instance where both sides equal `120`, and a genuine 2-plane instance where both sides equal `0`.

## 3. Method #14 — FIND THE GROUP ACTING: overlap-one balanced plane orbits

Run20's new null planes used two balanced `+-1` relations on disjoint supports. The next natural orbit is one-coordinate overlap. The group is coordinate permutation together with projective rescaling of the two relation lines. The useful invariant is the multiset of projective support sizes inside the plane.

Take
\[
s\in\{3,4\},\qquad t\ge5,\qquad s<t,
\qquad s+t-1\le m.
\]
Choose supports `S,T` with
\[
|S|=s,\qquad |T|=t,\qquad |S\cap T|=1,
\]
and balanced projective `+-1` relation lines `[v]`, `[w]` on `S,T`. Put
\[
V=\operatorname{span}_{\mathbb F_p}\{v,w\}.
\]
For odd `p`, orient representatives so the coefficient at the common coordinate is `+1` for each line.

Among the `p-1` projective mixed lines `[v+\lambda w]`, exactly one ratio cancels the common coordinate. Hence the projective support spectrum is
\[
\boxed{
\operatorname{suppspec}(V)
=
\{s,t,s+t-2,
\underbrace{s+t-1,\ldots,s+t-1}_{p-2\text{ times}}\}.
}
\tag{3.1}
\]
Because `s>=3`,
\[
s+t-2>t,
\]
so `[v]` and `[w]` are the unique projective lines of supports `s` and `t`. Thus the generators, their supports, and their balanced line classes are intrinsic to `V`; no two distinct choices in the orbit count below generate the same plane.

Moreover, `V` has exactly one projective line of support at most four, namely `[v]`. Every run18 support-3/4 plane has at least two distinct projective lines of support at most four, so the new family is disjoint from all previously credited run18 planes. It is also disjoint from the run20 disjoint-support family: there all `p-1` mixed projective lines have the same support `s+t`, whereas (3.1) has one exceptional cancellation support `s+t-2` and `p-2` lines of support `s+t-1`.

For a balanced support size `r`, the projective line classes relative to the distinguished overlap coordinate are explicit. If `r=2a` is even, there is one class, of multiplicity
\[
L_r=\frac12\binom r a,
\]
and after orienting the overlap coefficient positive, the remaining coefficients contain `a-1` pluses and `a` minuses. If `r=2a+1` is odd, there are two classes: overlap in the minority sign, multiplicity
\[
\binom{r-1}{a-1},
\]
and overlap in the majority sign, multiplicity
\[
\binom{r-1}{a}.
\]
These sum to the usual number `\binom r a` of balanced projective lines on a fixed odd support.

The number of support configurations is
\[
\binom ms\,s\,\binom{m-s}{t-1}.
\tag{3.2}
\]
Multiplying (3.2) by the appropriate two line-class multiplicities and by the exact C260 count for one canonical representative gives the exact matrix--plane incidence for that orbit.

### R03-C261 — overlap-one balanced plane packing

**STATUS: PROVED.** Summing the exact C260 incidence over all class pairs and all
\[
s\in\{3,4\},\quad 5\le t,\quad s<t,\quad s+t-1\le m
\]
gives a valid additional lower bound for the second projective null incidence `M_2`, and this entire contribution is disjoint from both the retained run18 sparse-plane family and run20's disjoint-support family.

No matrix-level disjointness is required: `M_2` itself counts matrix--2-plane incidences, so if one matrix carries several credited planes it is supposed to be counted once for each of those planes.

## 4. Method #19 — MAKE IT AN ALGORITHM: exact partition-orbit evaluator

C260 is directly algorithmic. Enumerate set partitions of `0,...,m` as restricted-growth strings. For each partition:

1. compute `mu(hat0,pi)` by (2.1);
2. aggregate each basis vector of `V` over the nonzero partition blocks;
3. enumerate the Boolean block values to obtain `h_V(pi)` exactly;
4. add `mu(hat0,pi)(h_V(pi)-1)_m`.

At `m=9,10` this is small enough for exact `cpp_int` arithmetic. The checker also enumerates the support spectra and all orbit multiplicities, so no Monte Carlo or floating-point decision enters the finite certificate.

Executed checker:
`artifacts/R03/20260916T2208Z_21_overlap_partition_mobius_exact.cpp`.

Archived output:
`artifacts/R03/20260916T2208Z_21_overlap_partition_mobius_exact.out`.

Source SHA-256:
`c7d2b25a8c6ef4711b5d5604e7594f40c27f4c09572b5e253fb9299e97d8f3c7`.

Output SHA-256:
`9b6f095280d144817e8aabd8c9d934f18d9f4d5ad6d3cf3caa367c4addc8f2bc`.

Output ends `SELF-CHECK PASS`.

## 5. Exact finite movement

### `m=9,p=7` / `n=10`

Replacing run20's row-union-bound counts by C260 gives the exact retained disjoint-family contribution
\[
M_{2,\mathrm{disj}}^{\mathrm{exact}}
=87598110053204352000.
\tag{5.1}
\]
The new overlap-one contribution is
\[
\boxed{
\Delta M_{2,7,9}^{\mathrm{ov1}}
=1148904504446444928000,
}
\tag{5.2}
\]
coming from `275940` distinct projective 2-planes. By support-spectrum separation, (5.1), (5.2), and the retained run18 support-3/4 contribution are pairwise disjoint plane families.

Retain
\[
M_{1,7,9}=651685823418402269683200,
\]
\[
M_{2,7,9}^{\rm old}\ge2942127020232812160000,
\]
and run19's modular-nullity ceiling `D=4`. C253 therefore uses
\[
c_{7,4}=\frac{7(7^2-1)}{7^4-1}=\frac7{50}.
\]
Substitution gives
\[
\boxed{
r(10)
\le
\frac{635840639911659887775}{2305843009213693952}
=275.751921258717971\ldots .}
\tag{C262.1}
\]
Run20 had `275.8202561002904...`, so the exact gain is
\[
\boxed{
\frac{630277666901780877}{9223372036854775808}
=0.0683348415724005925\ldots .}
\tag{5.3}
\]

### `m=10,p=11` / `n=11`

The exact C260 disjoint-family contribution is
\[
M_{2,\mathrm{disj}}^{\mathrm{exact}}
=52931740503953446248960000,
\tag{5.4}
\]
and the new overlap-one contribution is
\[
\boxed{
\Delta M_{2,11,10}^{\mathrm{ov1}}
=470241266783248111979520000,
}
\tag{5.5}
\]
from `1524600` distinct projective 2-planes.

Retain
\[
M_{1,11,10}=325043331888785398807391827200,
\]
\[
M_{2,11,10}^{\rm old}\ge807305539038902680414176000,
\]
and the run19 ceiling `D=5`, giving
\[
c_{11,5}=\frac{11(11^2-1)}{11^5-1}=\frac{132}{16105}.
\]
Then
\[
\boxed{
r(11)
\le
\frac{4089568153828729532838706676925}
{7787900129957441143457185792}
=525.118207165694344\ldots .}
\tag{C262.2}
\]
Run20 had `525.1244565083956...`; the exact gain is
\[
\boxed{
\frac{1520914276110635813224125}
{243371879061170035733037056}
=0.00624934270129197302\ldots .}
\tag{5.6}
\]

Call (C262.1)--(C262.2) **R03-C262 — PROVED WITH EXECUTED EXACT CHECKER**.

## 6. Complete-domain metric and what did not close

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
r(8)=1658391558075/34359738368,
\qquad
r(9)=15544095862461075/140737488355328.
\]
Use C262.1 at `n=10` and C262.2 at `n=11`. For `n>=12`, the complete-domain guarantee remains the previous minimum of the retained C249/C252/C253/C255 branches with C256 modular-rank ceilings; C260/C261 can only lower those modular branches when evaluated. Thus the full `n`-domain remains rigorously covered, with strict improvement at `n=10,11`.

This does **not** establish `r(n)=o(n^2)`. C260 is exact and C261 materially improves the finite certificate, but bounded sparse-null-plane packing is not by itself an asymptotic proof. A balanced relation of support `s` cuts the Boolean cube at density on the order of `s^{-1/2}`; two independent sparse constraints still incur a substantial column-wise penalty. The asymptotic residual continues to be dense modular normals / accidental determinant divisibility after all elementary collisions are removed.

A second new route was explored but not promoted: intersecting projective null-line incidences at two small primes. The extra prime removes matrices singular modulo only one prime but introduces enough projective multiplicity that the small-prime pilot did not beat the best single-prime collision-conditioned branch. No theorem claim is made from that pilot. A useful modular asymptotic proof still appears to require a growing modulus together with target-scale determinant-residue or cokernel control conditional on `\mathcal G_m`.

The strategic value of this run is therefore twofold: the finite metric moves by a larger amount than run20, and C260 replaces a recurring union-bound bookkeeping loss by an exact universal formula. The next attack should use C260 as the exact finite engine while the research effort shifts to a dense-normal/growing-prime statement rather than enumerating indefinitely many bounded support pairs.

## 7. Independent R04 audit — source-closing tau0 theorem

Newest ready package actually read:
`runs/R04/20260916T2127Z_i0027_er_cluster_closure.md`.

I record
\[
\boxed{\texttt{R03-AUDIT-R04-I0027-C8-08 = PASS}}
\]
for the **mathematical argument of R04-I0027-C8**, the `tau_0`/Kemeny half of Aldous--Fill Open Problem 6.13. This audit does not certify novelty and does not audit the separate `tau_2` half.

The critical external input was checked directly: Alev--Anari--Lau--Oveis Gharan, *Graph Clustering using Effective Resistance*, ITCS 2018, Theorem 3, does give for sufficiently large `delta>1` a partition with cross-edge weight `O(w(E)/delta)` and induced-cluster effective-resistance diameter `O(delta^3 n/w(E))`, with universal implied constants. Thus R04's use with an unweighted dense extremizer and `delta_n=n^(1/10)` is source-faithful.

I independently checked the internal proof chain:

- the balanced-barbell family supplies the `1/54` lower coefficient, consistent with the published barbell formulas of Faught--Kempton--Knudson / earlier barbell computations;
- `K(G)<=m(n-1)` forces any maximizer achieving that lower scale to have `m=Theta(n^2)`;
- the Alev partition then has `q=O(m/delta_n)=o(n^2)` cross edges and cluster resistance diameter `epsilon_n=O(delta_n^3/n)=o(1)`;
- retaining one cross edge along a quotient spanning tree and deleting the others changes Kemeny's constant by `o(n^3)` via R04-C4. Expanding `d^G=d^H+r`, Rayleigh monotonicity and `R_H<=n-1` reproduces C4's stated error exactly;
- in the quotient-tree graph, effective resistance is the sum of unit bridge resistances plus within-cluster entry/exit resistances. Hence R04-C7's error is at most `m n epsilon_n=o(n^3)`;
- R04-C6's bridge-block identity is exact: after deleting bridges, with `w_i=m_i+1`, `W=m+1` and independent quotient samples with probabilities `p_i=w_i/W`, the bridge contribution equals
  \[
  \frac{(m+1)^2}{m}E d_Q(X,Y)
  -\frac{(2m+1)|E(Q)|}{2m}.
  \]
  The large/small-block split, simple-graph capacity, and Hölder inequality
  \[
  1\le(\sum \widetilde p_i^2)(\sum\sqrt{\widetilde p_i})^2
  \]
  reduce the normalized bridge term to
  \[
  \frac{s^2(1-s)}8\le\frac1{54},
  \]
  with equality at `s=2/3`;
- combining the sparse-deletion comparison, cluster-resistance error and C6 gives the `1/54` upper coefficient.

I found no mathematical gap in this chain. R04's own governance label remains appropriate: **PROVED BY R04 / audit-gated**, because the fleet closure protocol still requires P26 plus a second independent OTHER-track audit; this R03 audit can serve as the distinct non-P26 audit if P26 independently passes the same source-closing package. Novelty remains unverified by this mathematical audit.

## 8. Model/runtime escalation status

The model-setting limitation is unchanged. The exposed task mutation interface has prompt/title/schedule/timing/enabled controls but no model-family or reasoning-effort field and no authenticated runtime telemetry. Therefore GPT-6/maximum can only be requested in prompt text in this context; it cannot be verified or forced by R03.

The current root ledger records that a P26 update succeeded from one authorized native context while another context had returned `You cannot modify this task`; this is consistent with task/workspace ownership or authorization, not a hidden model field. The legitimate escalation path is an owning/admin-authorized native-task context that actually exposes model/reasoning controls, or platform support. R03 does not create a duplicate or bypass the permission boundary. No scheduler state was changed this run.

## 9. Cumulative ledger and failed routes

| Claim / route | Status |
|---|---|
| Source iid Rademacher asymptotic | **OPEN** |
| C225 exact trivial-collision lower asymptotic with overlaps | **PROVED / retained** |
| Exact collision-subtracted `r(n)`, `1<=n<=9` | **PROVED / retained** |
| C240/C246 sign-to-binary normalization and exact `G_m` collision-free class | **PROVED / retained** |
| C251 first projective modular incidence | **PROVED / retained** |
| C253 second-incidence correction | **PROVED / retained; R02 claim-scoped audit PASS** |
| C255/C258 prior sparse 2-plane lower-bound families | **PROVED / retained** |
| C256 modular rank floors | **PROVED / retained** |
| **C260 exact partition-Möbius collision-free incidence** | **PROVED NEW** |
| **C261 overlap-one balanced null-plane packing** | **PROVED NEW** |
| **C262 improved `r(10),r(11)`** | **PROVED NEW / exact checker** |
| `r(n)=o(n^2)` | **OPEN** |
| Dense modular normal / growing-prime collision-conditioned residue control | **OPEN** |
| X27 fixed-epsilon JSS diagonalization | **KILLED / retained** |
| X28 conditional row-column independence | **KILLED / retained** |
| X29 fixed best prime | **KILLED / retained** |
| Blinovsky/Irmatov announced exact routes | **NOT VERIFIED / retained** |
| R03 audit of R04 source-closing C8 | **PASS NEW, mathematical claim scope** |
| P26 full R03 package audit | **ABSENT** |
| second full-package R03 audit | **ABSENT** |

No claim here upgrades a bounded-support or modular finite certificate to source closure. The asymptotic source target remains open.

## 10. Next attack

Do not spend the next main run merely adding support-overlap-two, support-overlap-three, and so on. C260 is now the exact finite engine. The asymptotic attack should instead split modular singularity into sparse/high-concentration normals and dense normals at a growing prime `p=p(n)`.

The sparse side should be paid by an entropy sum over C260-counted projective subspaces, using the support/high-atom classification already accumulated. The dense side needs a collision-conditioned determinant-residue/cokernel theorem strong enough that the probability of a real-nonsingular matrix in `G_m` becoming singular mod `p(n)` is `o(n^2 2^{-n})`. Existing generic exponential-error finite-field universality is not automatically at that precision. A proof that achieves this split would directly feed C253 and the fixed source metric; a proof that shows such a growing-prime split cannot reach target scale would be an equally useful killed route.

## 11. Structured ledger_delta

```yaml
ledger_delta:
  track: R03
  source: "Komlos 1967 lineage; Vu 2020 Conj. 2.2; Jain-Sah-Sawhney 2021 Conj. 1.1; Sahasrabudhe 2025 Eq. (4.1)"
  target: "P(det B_n=0)=(1+o(1)) n(n-1) 2^(1-n) for iid uniform signs"
  metric: "r(n)=2^n P(det B_n=0 and no signed equal/opposite row/column pair)"
  before:
    r10_upper: "2543992837313541331977/9223372036854775808 = 275.8202561002904..."
    r11_upper: "4089616823085565073184729848925/7787900129957441143457185792 = 525.1244565083956..."
  after:
    r10_upper: "635840639911659887775/2305843009213693952 = 275.751921258717971..."
    r11_upper: "4089568153828729532838706676925/7787900129957441143457185792 = 525.118207165694344..."
  status: PARTIAL
  source_status: OPEN
  unchanged_count: 0
  exact_evidence:
    checker: "artifacts/R03/20260916T2208Z_21_overlap_partition_mobius_exact.cpp"
    output: "artifacts/R03/20260916T2208Z_21_overlap_partition_mobius_exact.out"
    source_sha256: "c7d2b25a8c6ef4711b5d5604e7594f40c27f4c09572b5e253fb9299e97d8f3c7"
    output_sha256: "9b6f095280d144817e8aabd8c9d934f18d9f4d5ad6d3cf3caa367c4addc8f2bc"
  own_claims_new: [R03-C260, R03-C261, R03-C262]
  own_audits_retained: [R02-AUDIT-R03-C253-04]
  peer_audit_new: [R03-AUDIT-R04-I0027-C8-08]
  p26_full_package_audit: NONE
  second_full_package_audit: NONE
```

No shared ledger, peer file, email, Drive, public posting, purchase, permission, workflow, or scheduler state was changed.
