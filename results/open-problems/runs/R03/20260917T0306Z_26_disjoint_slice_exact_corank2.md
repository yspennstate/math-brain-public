Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED; GPT-6 / maximum was requested, but this task interface exposes no model-family selector, no reasoning-effort selector, and no authenticated applied-runtime telemetry, so GPT-6 maximum is not claimed. METRIC MOVED: `r(10) <= 275.648865953934676... -> 275.608343149922234...`, `r(11) <= 524.988842147013479... -> 524.867906501182802...`; consecutive unchanged count remains `0`. Section-B methods actually used: #11 DUALIZE, #25 COUNT THE SAME THING TWICE, #30 DO ONE PRIME / ONE SCALE / ONE DIRECTION AT A TIME.**

# R03 run26 — product-slice dual caps and exact-corank-two slack reclamation

Run ID: `20260917T0306Z_26_disjoint_slice_exact_corank2`  
Repository / branch: `yspennstate/math-open-problems` / `master`.

## 1. Continuity, source gate, ownership, and frozen metric

I continued from the newest own report

`runs/R03/20260917T0208Z_25_hyperplane_span_corank3.md`

and did not restart the proof or reset any failed route or stagnation count. Before new mathematics I recovered the current campaign controls `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, and `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`; the newest own report; the newest neighboring R04 report; and targeted R03/source/ownership history. The intake JSONL corpus is too large to render literally through the connector in one response, so I used exact R03/source/ownership searches and do **not** claim a byte-for-byte visual reread of all roughly 780 entries.

The current dated source/status record is

`artifacts/R03/20260917T0306Z_26_status_search.md`.

The historical lineage is Komlós, *On the determinant of (0-1) matrices* (1967). The modern source locators retained by R03 are Vu, arXiv:2005.02797, Section 2 / Conjecture 2.2, and Jain--Sah--Sawhney, arXiv:2010.06554, Conjecture 1.1 specialized to the iid uniform Rademacher law. The current JSS arXiv record still distinguishes its sharp theorem for finite-support laws **not uniform on their support** from the uniform-support case, where only exponential-scale full-singularity precision is obtained together with a sharp compressible-vector analysis. Fresh bounded searches dated 2026-09-17 did not surface a later accepted primary-source solution of the iid nonsymmetric Rademacher sharp prefactor. Hunter--Kwan--Sauermann--Sawhney's large-corank theorem and Song--Wang's growing-corank theorem do not settle the corank-one prefactor. This is negative bounded-search evidence, not a novelty certificate.

For two fixed iid sign rows, equality or opposition has probability
\[
2^{-n}+2^{-n}=2^{1-n}.
\]
There are `binom(n,2)` row pairs and the same number of column pairs. Thus the elementary first-order contribution is
\[
2\binom n2 2^{1-n}=n(n-1)2^{1-n}.
\]
Retained C225 controls the overlaps and supplies the matching lower asymptotic. Hence the source-matched target remains
\[
\boxed{
\Pr(\det B_n=0)=(1+o(1))\,n(n-1)2^{1-n}.
}
\tag{1.1}
\]
Let `T_n` denote the exact union of all signed equal/opposite row-pair and column-pair events. The fixed upper metric is
\[
\boxed{
r(n):=2^n\Pr(\det B_n=0,\ T_n^c),
}
\tag{1.2}
\]
and source closure is equivalent to
\[
\boxed{r(n)=o(n^2).}
\tag{1.3}
\]

Under retained C240/C246, putting `m=n-1` converts the collision-free residual into
\[
\mathcal G_m
=
\{A\in\{0,1\}^{m\times m}:\text{all rows and columns are nonzero and pairwise distinct}\}.
\tag{1.4}
\]

Run25's replay-certified baselines were
\[
r(10)\le
\frac{1271206021115125771515}{4611686018427387904}
=275.648865953934676\ldots,
\tag{1.5}
\]
\[
r(11)\le
\frac{4088560671982932827043671156925}
{7787900129957441143457185792}
=524.988842147013479\ldots.
\tag{1.6}
\]
The external exact-count/OEIS consequence `r(10)=222.6104736743...` remains source-backed but not replay-certified and is **not** promoted.

The killed-route ledger is preserved: fixed-`epsilon` JSS diagonalization X27, conditional row/column independence X28, a universally best fixed prime X29, naive left/right-normal multiplication, exponential-rate-only arguments, and the universal-large-modular-rank route killed by the Haemers--Peeters construction. No stagnation counter is reset by relabeling an old obstruction.

## 2. Retained modular majorant and the unspent exact-corank-two slack

Fix an odd prime `p`. For `A in G_m`, write
\[
d_p(A)=m-\operatorname{rank}_{\mathbb F_p}A.
\]
Retained C253 uses
\[
Z_1(d)={d\brack1}_p,
\qquad
Z_2(d)={d\brack2}_p,
\]
and a certified nullity ceiling `D` to obtain the pointwise majorant
\[
\mathbf 1_{\{d\ge1\}}
\le
Z_1(d)-c_{p,D}Z_2(d),
\qquad
c_{p,D}:=\frac{p(p^2-1)}{p^D-1}.
\tag{2.1}
\]
For exact nullity two,
\[
Z_1(2)=p+1,
\qquad
Z_2(2)=1,
\]
so the right side of (2.1) equals `p+1-c_{p,D}`. Relative to the true singular indicator `1`, there is an **exact reclaimable excess**
\[
\boxed{
\sigma_{p,D}(2)=p-c_{p,D}.
}
\tag{2.2}
\]
Run24/run25 spent this slack on the disjoint `(3,3)` support family. Runs20--21 had already credited several other disjoint balanced support pairs to the second projective incidence `M_2`, but only as **plane incidences**. This run asks whether a large explicitly counted subset of those same incidences can be certified to have exact nullity two, permitting the additional subtraction (2.2).

That is a finite quantitative-remainder attack, not a claim that bounded support solves the source asymptotic.

## 3. Method #11 — DUALIZE each balanced Boolean relation slice

For `s>=3`, fix a balanced `+/-1` relation on `s` coordinates, with `floor(s/2)` coefficients `+1` and the rest `-1`. In the finite cases used below there is no modular wrap. Let
\[
S_s\subset\mathbb F_p^{s-1}
\]
be the parameter image of its Boolean solutions after solving linearly for the last coordinate. Its size is
\[
\boxed{
H_s:=|S_s|={s\choose\lfloor s/2\rfloor}.
}
\tag{3.1}
\]
The number of projective balanced relation lines on a fixed support is
\[
\boxed{
L_s=
\begin{cases}
\frac12 {s\choose s/2},&s\text{ even},\\[1mm]
{s\choose\lfloor s/2\rfloor},&s\text{ odd}.
\end{cases}
}
\tag{3.2}
\]
For a linear functional `ell` on the parameter space define its largest fiber on the slice by
\[
q_{p,s}:=
\max_{\ell\ne0}\max_{a\in\mathbb F_p}
|\{x\in S_s:\ell(x)=a\}|.
\tag{3.3}
\]

The new exact finite core exhausts **all projective linear functionals** on every local slice needed this run. It proves the same fiber maxima for `p=7` and `p=11`:
\[
\begin{array}{c|ccccc}
s&3&4&5&6&7\\ \hline
H_s&3&6&10&20&35\\
q_{p,s}&2&4&6&12&20.
\end{array}
\tag{3.4}
\]
The checker archives the complete maximum-fiber histograms, not just the maxima.

This is the useful dual move: rather than attempt to enumerate all matrices immediately, measure how much of a Boolean relation slice **any dual hyperplane can trap**.

## 4. Product slices from two disjoint balanced relations

Choose disjoint supports of sizes `s,t`, and choose one balanced projective relation line on each support. Let `V` be their two-dimensional span. Write
\[
b=m-s-t\ge0.
\]
Since the supports are disjoint, the Boolean slice of the orthogonal complement decomposes as
\[
C_V:=V^\perp\cap\{0,1\}^m
\cong S_s\times S_t\times\{0,1\}^b.
\tag{4.1}
\]
Therefore
\[
\boxed{
h_{m;s,t}:=|C_V|=H_sH_t2^b.}
\tag{4.2}
\]
Also `dim V^perp=m-2`.

### R03-C272a — product-slice hyperplane cap

**STATUS: PROVED for the finite block profiles used below, with the local finite core exhaustively certified.**

Every proper hyperplane `W<V^perp` satisfies
\[
|W\cap C_V|\le Q_{m,p;s,t},
\tag{4.3}
\]
where
\[
\boxed{
Q_{m,p;s,t}
=
\max\left\{
q_{p,s}H_t2^b,
q_{p,t}H_s2^b,
\mathbf1_{\{b>0\}}\frac{h_{m;s,t}}2
\right\}.
}
\tag{4.4}
\]

**Proof.** Express a nonzero linear functional on `V^perp` in the product coordinates (4.1). If it is nonzero on the `S_s` block, condition on every other coordinate. The remaining affine equation has at most `q_{p,s}` solutions in `S_s`, so the total fiber has size at most `q_{p,s}H_t2^b`. The same argument applies if it is nonzero on `S_t`. If it vanishes on both relation blocks, it must depend on a free Boolean bit, and conditioning on the remaining coordinates leaves at most one of its two values, giving `h/2`. Taking the largest of these valid caps proves (4.3). `square`

Independently, the cube/subspace lemma says that a `j`-dimensional linear subspace contains at most `2^j` Boolean vectors. Hence after `j<m-2` independent columns from `C_V` have been chosen, their span traps at most
\[
\min\{2^j,Q_{m,p;s,t}\}
\]
points of `C_V`. Consequently the number of ordered Boolean bases of `V^perp` contained in `C_V` is at least
\[
\boxed{
B_{m,p;s,t}
:=
\prod_{j=0}^{m-3}
\left(h_{m;s,t}-\min\{2^j,Q_{m,p;s,t}\}\right).
}
\tag{4.5}
\]
All factors in every finite family used below are positive.

## 5. Method #25 — count the same constrained matrices twice

The number of distinct disjoint-support planes of type `(s,t)` is
\[
\boxed{
N_{m;s,t}
=
\begin{cases}
{m\choose s}L_s{m-s\choose t}L_t,&s<t,\\[1mm]
\frac12 {m\choose s}L_s{m-s\choose s}L_s,&s=t.
\end{cases}
}
\tag{5.1}
\]
There is no duplicate-plane issue. If `s<t`, the two generators are the unique projective lines in `V` with supports `s` and `t`; every mixed line has support `s+t`. If `s=t`, `V` has exactly two support-`s` projective lines and all mixed lines have support `2s`, so the unordered generator pair is intrinsic.

For one such `V`, choose the first `m-2` matrix columns to be one of the ordered bases counted by (4.5). Then choose the last two matrix columns as ordered distinct unused nonzero vectors of `C_V`. There are
\[
(h_{m;s,t}-m+1)(h_{m;s,t}-m)
\tag{5.2}
\]
ways to do this.

The selected columns span all of `V^perp`, so the left modular nullspace is **exactly** `V`; the modular nullity is exactly two. Since every nonzero vector in `V` has support at least three, `V` contains neither a support-one vector nor a support-two vector. Thus no row is zero, and no two rows are equal. The columns are nonzero and pairwise distinct by construction. Therefore every constructed matrix lies in `G_m`.

### R03-C272b — exact-corank-two count for a disjoint balanced pair

**STATUS: PROVED.** For every finite tuple `(m,p,s,t)` certified below,
\[
\boxed{
E_{m,p;s,t}
:=
N_{m;s,t}B_{m,p;s,t}
(h_{m;s,t}-m+1)(h_{m;s,t}-m)
}
\tag{C272b}
\]
distinct matrices in `G_m` have exact modular nullity two and exact left nullspace equal to one of the type-`(s,t)` planes.

This is also the promised double count. The retained C253/C260 machinery counts each such object as a **matrix--null-plane incidence**, paying the `-c M_2` correction once. The construction above counts the **matrices themselves** and proves their nullspace contains no additional projective plane because its dimension is exactly two. Therefore the remaining per-matrix excess `p-c_{p,D}` from (2.2) may be subtracted without changing or double-counting the old `M_2` payment.

Different support types below are disjoint as matrix families: the exact nullspace is unique and its projective support spectrum determines the type. They are also disjoint from run25's exact-corank-three family by nullity, and from the retained exact `(3,3)` corank-two family by the nullspace support spectrum.

## 6. Method #30 — one prime, one dimension, one active modular branch

I applied C272 only at the two finite dimensions where the currently active modular branches are already fully certified: `m=9,p=7,D=4` and `m=10,p=11,D=5`. This avoids pretending that a local computation at one prime glues asymptotically.

### 6.1 `m=9`, `p=7`, hence sign order `n=10`

The previously credited disjoint balanced plane types not yet given exact-corank-two slack are
\[
(3,5),\qquad(3,6),\qquad(4,5).
\]
The checker obtains:

\[
\begin{array}{c|r|r|r|r}
(s,t)&h&Q&N&E_{9,7;s,t}\\ \hline
(3,5)&60&40&15120&9\,845\,491\,243\,017\,830\,400\\
(3,6)&60&40&2520&1\,640\,915\,207\,169\,638\,400\\
(4,5)&60&40&3780&2\,461\,372\,810\,754\,457\,600.
\end{array}
\tag{6.1}
\]
For all three types the ordered-basis lower bound is
\[
B=245\,534\,248\,960,
\]
with greedy factors
\[
59,58,56,52,44,28,20,
\]
and the two-extra-column factor is `2652`.

Here
\[
c_{7,4}=\frac7{50},
\qquad
p-c_{p,D}=7-\frac7{50}=\frac{343}{50}.
\]
After the standard normalization `2^(m+1-m^2)`, the three additional corrections are approximately
\[
0.028604332244057507,
\quad
0.004767388707342918,
\quad
0.007151083061014377.
\]
Their exact sum is
\[
\boxed{
\Delta_{10}
=
\frac{2919975760805103}{72057594037927936}
=0.0405228040124148\ldots .
}
\tag{6.2}
\]

Subtracting (6.2) from the run25 bound gives
\[
\boxed{
r(10)
\le
\frac{1271019142666434244923}{4611686018427387904}
=275.608343149922234\ldots .}
\tag{C273.1}
\]

### 6.2 `m=10`, `p=11`, hence sign order `n=11`

The corresponding support types are
\[
(3,5),(3,6),(3,7),(4,5),(4,6),(5,5).
\]
The exact checker gives the following additional normalized corrections:
\[
\begin{array}{c|c}
(s,t)&\text{additional correction}\\ \hline
(3,5)&0.06130640120517198\ldots\\
(3,6)&0.02043546706839066\ldots\\
(3,7)&0.0019966096992592446\ldots\\
(4,5)&0.03065320060258599\ldots\\
(4,6)&0.005108866767097665\ldots\\
(5,5)&0.0014351004881634657\ldots .
\end{array}
\tag{6.3}
\]
Their exact sum is
\[
\boxed{
\Delta_{11}
=
\frac{117729341485144277109346125}
{973487516244680142932148224}
=0.120935645830669\ldots .
}
\tag{6.4}
\]
Here
\[
c_{11,5}=\frac{132}{16105},
\qquad
11-c_{11,5}=\frac{177023}{16105}.
\]
Thus
\[
\boxed{
r(11)
\le
\frac{4087618837251051672826796387925}
{7787900129957441143457185792}
=524.867906501182802\ldots .}
\tag{C273.2}
\]

### R03-C273 — replay-certified metric movement

**STATUS: PROVED / exact finite core executed.** Equations (C273.1)--(C273.2) strictly improve the frozen metric from the run25 replay-certified values. The exact-arithmetic checker was independently reexecuted in this run and ends `SELF-CHECK PASS`.

Checker:
`artifacts/R03/20260917T0306Z_26_disjoint_slice_exact_corank2.py`.

Archived output:
`artifacts/R03/20260917T0306Z_26_disjoint_slice_exact_corank2.out`.

The output also archives every local slice maximum-fiber histogram, every basis product, plane multiplicity, exact-corank family size, rational slack, and final rational subtraction.

## 7. Full-n-range envelope is retained

Nothing at smaller or larger `n` is weakened. The exact retained values through `n=9` remain
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
Use C273.1 at `n=10` and C273.2 at `n=11`. For every `n>=12`, retain the pointwise minimum of all previously replay-certified full-domain C249/C252/C253/C255/C256/C269/C271 branches. Therefore the complete-domain R03 upper envelope is rigorously no worse at every `n` and strictly better at `n=10,11`.

This is still only **PARTIAL**. Neither C272 nor C273 proves `r(n)=o(n^2)`.

## 8. Why this route cannot be mistaken for the asymptotic solution

For fixed support sizes `s,t`, put
\[
\alpha_{s,t}=\frac{H_sH_t}{2^{s+t}}<1.
\]
Then `h=alpha*2^m`, the number of planes `N_{m;s,t}` is polynomial in `m`, and even the crude upper bound on the constructed matrices is
\[
E_{m,p;s,t}\le \operatorname{poly}(m)h^m.
\]
After R03's normalized prefactor this gives at most
\[
\operatorname{poly}(m)\,2^m\alpha_{s,t}^m.
\]
For every fixed support pair used here, `2 alpha_{s,t}<1`; hence the entire family is exponentially negligible with `m`. The finite improvement is real, but indefinitely cataloguing bounded-support nullspaces cannot establish the sharp source asymptotic.

This run therefore sharpens, rather than hides, the surviving obstruction:
\[
\boxed{
\text{collision-free, small-corank, dense/unstructured real or primitive-CRT null witnesses at }o(n^2 2^{-n})\text{ scale}.}
\tag{8.1}
\]
Run22's squarefree CRT formulation removes accidental determinant divisibility once the modulus exceeds the Hadamard bound; run23 shows a universal high-rank floor cannot solve the problem; runs24--26 show that exact higher-corank slack can be reclaimed when the nullspace is structurally known. The remaining difficulty is the **dense small-corank** sector, not another bounded sparse support class.

A natural next attack is to combine the squarefree CRT formulation with a distributional inverse Littlewood--Offord statement for primitive dense normals, while using exact-corank incidence only as a cleanup term. Any successful statement must live at the actual target scale `o(n^2 2^(-n))`; an unspecified `exp(-c n)` error is not enough.

## 9. Prior art / novelty discipline

The finite product-slice cap and exact-corank reclamation are presented as R03 internal claims, not as certified publication novelty. The broader cube-hyperplane viewpoint is classical: Voigt--Ziegler relate binary singularity to the expected number of cube vertices in a random spanned hyperplane, and Aichholzer--Aurenhammer study hyperplanes spanned by cube vertices. The bounded dated search did not locate the exact finite formulas C272/C273, but absence from a bounded search is **not** a novelty certificate.

Current JSS source status remains the controlling external fact: their sharp non-uniform-support theorem does not cover the uniform Rademacher law, and their uniform-support result has only exponential precision for full singularity. The 2025/2026 large-corank literature likewise does not close the sharp corank-one prefactor.

## 10. Neighboring R04 audit obligation

The newest recovered R04 report is

`runs/R04/20260917T0217Z_i0027_stuck_thinking_02.md`.

It explicitly makes **no new mathematical theorem claim and creates no new checker**. Its source theorem and quantitative strengthening were already covered by the earlier distinct R03 claim-scoped audits; its current remaining obligation is the designated P26 end-to-end audit. I therefore do **not** manufacture a duplicate R03 audit in this run.

## 11. Model / scheduler escalation

The limitation remains unchanged. The exposed task-control surface provides prompt/title, schedule/timing, and enabled-state controls but no model-family selector, no reasoning-effort selector, and no authenticated per-run applied-runtime telemetry. `GPT-6 / maximum` is therefore prompt text only here.

The historical `You cannot modify this task` response is an authorization/context boundary, not a mathematical or repository setting. `RESULTS.md` records that P26 later updated successfully from another authorized context. The legitimate route to enforce a model/reasoning choice is an owning/admin-authorized product surface that exposes those controls, or platform support. I did not duplicate a task, bypass permissions, or modify scheduler state.

## 12. ledger_delta

```yaml
ledger_delta:
  worker: R03
  source: "iid nonsymmetric Rademacher singularity / Komlos-Vu-Jain-Sah-Sawhney lineage"
  target: "P(det B_n=0)=(1+o(1)) n(n-1) 2^(1-n)"
  metric: "r(n)=2^n P(det B_n=0, T_n^c), full-n-domain pointwise certified upper envelope"
  before:
    r10: "1271206021115125771515/4611686018427387904 = 275.648865953934676..."
    r11: "4088560671982932827043671156925/7787900129957441143457185792 = 524.988842147013479..."
  after:
    r10: "1271019142666434244923/4611686018427387904 = 275.608343149922234..."
    r11: "4087618837251051672826796387925/7787900129957441143457185792 = 524.867906501182802..."
  movement: "MOVED"
  exact_improvement:
    r10: "2919975760805103/72057594037927936 = 0.0405228040124148..."
    r11: "117729341485144277109346125/973487516244680142932148224 = 0.120935645830669..."
  unchanged_count: 0
  status: "PARTIAL / SOURCE OPEN"
  tried_moves: [11, 25, 30]
  new_claims:
    - "R03-C272a: finite product-slice hyperplane cap for the certified support profiles"
    - "R03-C272b: explicit exact-modular-corank-two matrix families on retained disjoint balanced null planes"
    - "R03-C273: strict replay-certified r(10), r(11) upper-bound improvement"
  exact_evidence:
    - "artifacts/R03/20260917T0306Z_26_disjoint_slice_exact_corank2.py"
    - "artifacts/R03/20260917T0306Z_26_disjoint_slice_exact_corank2.out"
  source_evidence:
    - "artifacts/R03/20260917T0306Z_26_status_search.md"
  remaining_obligation: "prove r(n)=o(n^2), now localized to collision-free dense small-corank real/primitive-CRT null witnesses"
  closure_claim: false
  outgoing_audit: []
```

Overall status: **PARTIAL / source OPEN / fixed metric moved / unchanged count 0.** No email, Drive, public posting, purchase, permission change, workflow execution, shared-root ledger edit, peer-file edit, or scheduler change was made.
