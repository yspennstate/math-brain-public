Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED; GPT-6 / maximum was requested, but the exposed task interface still has no model-family selector, no reasoning-effort selector, and no authenticated applied-runtime telemetry, so GPT-6 maximum is not claimed. METRIC MOVED: `r(10) <= 275.608343149922234... -> 275.140487580978781...`, `r(11) <= 524.867906501182802... -> 523.907004072269228...`; consecutive unchanged count remains `0`. Section-B methods actually used: #1 CHANGE THE CATEGORY, #24 FIND THE EXTREMAL OBJECT, #16 COMPUTE EVERY SMALL CASE AND STARE AT THE SEQUENCE.**

# R03 run27 — overlap-one affine evaluation codes and exact-corank-two slack reclamation

Run ID: `20260917T0408Z_27_overlap1_affine_code`  
Repository / branch: `yspennstate/math-open-problems` / `master`.

## 1. Continuity, source gate, ownership and fixed metric

I continued from the newest own report

`runs/R03/20260917T0306Z_26_disjoint_slice_exact_corank2.md`

at commit `afe25db30b26411870114907ee05646afc7c8c58`. I did not restart the problem, reset the failed-route ledger, or substitute a differently normalized metric.

Before new mathematics I recovered the current campaign controls `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, and `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`; targeted the canonical intake row `F0001`; read the newest own report; and read the newest neighboring R04 report `runs/R04/20260917T0310Z_i0027_retirement_handoff.md`. The large intake corpus cannot be rendered byte-for-byte through one connector response, so I used exact target/source/ownership search and do not claim that every roughly 780 historical row was literally displayed.

The dated source/current-status record for this run is

`artifacts/R03/20260917T0408Z_27_status_search.md`.

Fresh 2026-09-17 arXiv/web searches still recover Jain--Sah--Sawhney, arXiv:2010.06554, with the sharp full theorem restricted to entry laws not uniform on their support. For laws uniform on their support, including iid Rademacher, the abstract still states only `(1+o(1))^n`-level precision for full singularity plus a sharp compressible-vector analysis. Hunter--Kwan--Sauermann--Sawhney, arXiv:2510.12933, and Song--Wang, arXiv:2607.00495, strongly control large/growing corank but do not determine the corank-one polynomial prefactor. A bounded fresh search surfaced no later primary-source proof of the exact iid nonsymmetric Rademacher asymptotic. This is negative bounded-search evidence, not a novelty certificate.

For two fixed iid sign rows, equality or opposition has probability `2^(1-n)`, and there are `binom(n,2)` row pairs and the same number of column pairs. Retained C225 controls the overlaps, so the source-matched target remains

\[
\boxed{
\Pr(\det B_n=0)=(1+o(1))\,n(n-1)2^{1-n}.
}
\tag{1.1}
\]

Let `T_n` be the exact union of all signed equal/opposite row-pair and column-pair events. The fixed metric remains

\[
\boxed{r(n):=2^n\Pr(\det B_n=0,\ T_n^c),}
\tag{1.2}
\]

and source closure is equivalent to

\[
\boxed{r(n)=o(n^2).}
\tag{1.3}
\]

Under retained C240/C246, with `m=n-1`, the residual is identified with real-singular matrices in

\[
\mathcal G_m=
\{A\in\{0,1\}^{m\times m}:\text{all rows and columns are nonzero and pairwise distinct}\}.
\tag{1.4}
\]

The replay-certified run26 baselines were

\[
r(10)\le
\frac{1271019142666434244923}{4611686018427387904}
=275.608343149922234\ldots,
\tag{1.5}
\]

\[
r(11)\le
\frac{4087618837251051672826796387925}
{7787900129957441143457185792}
=524.867906501182802\ldots.
\tag{1.6}
\]

The external exact-count/OEIS consequence `r(10)=222.6104736743...` remains source-backed but not replay-certified and is not promoted.

The killed routes remain killed: fixed-epsilon JSS diagonalization X27, conditional row/column independence X28, a universally best fixed prime X29, naive multiplication of left/right-normal probabilities, exponential-rate-only arguments, and the universal-large-modular-rank route killed by the Haemers--Peeters reduced-matrix construction.

## 2. Retained modular majorant and where run26 still overpays

For an odd prime `p` and `A in G_m`, write

\[
d_p(A)=m-\operatorname{rank}_{\mathbb F_p}A.
\]

Retained C253 gives, for a certified nullity ceiling `D`,

\[
\mathbf 1_{\{d\ge1\}}
\le
{d\brack1}_p-c_{p,D}{d\brack2}_p,
\qquad
c_{p,D}=\frac{p(p^2-1)}{p^D-1}.
\tag{2.1}
\]

For exact modular nullity two,

\[
{2\brack1}_p=p+1,
\qquad
{2\brack2}_p=1,
\]

so the majorant pays

\[
p+1-c_{p,D}
\]

instead of `1`. Once a family is certified to have exact nullity two, the remaining safely reclaimable per-matrix slack is therefore

\[
\boxed{\sigma_{p,D}(2)=p-c_{p,D}.}
\tag{2.2}
\]

Run26 reclaimed this slack for disjoint-support balanced relation planes. Run21 had already credited a much larger family of **overlap-one** balanced relation planes to the second projective incidence `M_2`, but only at the matrix--plane incidence level. This run changes the category: it treats the Boolean orthogonal slice of an overlap-one plane as a restricted affine evaluation code and asks for its extremal hyperplane fiber. That converts many of those old incidences into exact-nullity-two matrices and unlocks the extra slack (2.2).

## 3. Method #1 — CHANGE THE CATEGORY: overlap-one slices as two-fiber affine evaluation codes

Retain the run21 overlap-one plane family. Take balanced projective `+-1` relation lines `[v]`, `[w]` on supports `S,T` with

\[
s:=|S|\in\{3,4\},\qquad t:=|T|\ge5,\qquad s<t,
\]

\[
|S\cap T|=1,
\qquad s+t-1\le m.
\]

Let `c` be the common coordinate and orient both relation representatives so their coefficient at `c` is `+1`. Put

\[
V=\operatorname{span}_{\mathbb F_p}\{v,w\}.
\]

Run21 proved that the projective support spectrum is

\[
\{s,t,s+t-2,
\underbrace{s+t-1,\ldots,s+t-1}_{p-2\text{ times}}\},
\tag{3.1}
\]

so the two generating lines and their support sizes are intrinsic to `V`; the orbit count has no duplicate planes. In particular every nonzero vector of `V` has support at least three.

Set the overlap bit

\[
z=x_c\in\{0,1\}.
\]

For one relation of support `r`, fixing its relative sign class and fixing `z`, eliminate one of its `r-1` residual coordinates by the relation. This leaves a Boolean parameter slice

\[
A_{r,\alpha}(z)\subset\mathbb F_p^{r-2}.
\]

For a nonzero linear functional `ell` on this parameter space define its largest affine fiber

\[
q_{r,\alpha}(z)
:=
\max_{\ell\ne0}\max_{a\in\mathbb F_p}
|\{u\in A_{r,\alpha}(z):\ell(u)=a\}|.
\tag{3.2}
\]

For an overlap-one plane of class pair `(alpha,beta)`, with

\[
b=m-(s+t-1),
\]

the Boolean orthogonal slice is a two-fiber union

\[
C_V:=V^\perp\cap\{0,1\}^m
\cong
\bigsqcup_{z\in\{0,1\}}
\{z\}\times A_{s,\alpha}(z)
\times A_{t,\beta}(z)\times\{0,1\}^b.
\tag{3.3}
\]

Write

\[
a_z=|A_{s,\alpha}(z)|,
\qquad b_z=|A_{t,\beta}(z)|,
\]

so

\[
\boxed{
h:=|C_V|=(a_0b_0+a_1b_1)2^b.}
\tag{3.4}
\]

This two-fiber affine-code viewpoint is the new structural move of the run.

## 4. Method #24 — FIND THE EXTREMAL OBJECT: the largest proper hyperplane fiber

The extremal object needed by the greedy spanning argument is the proper hyperplane of `V^perp` that captures the most Boolean slice points.

Let

\[
q^s_z=q_{s,\alpha}(z),
\qquad q^t_z=q_{t,\beta}(z).
\]

Define

\[
Q_s=(q^s_0b_0+q^s_1b_1)2^b,
\tag{4.1}
\]

\[
Q_t=(q^t_0a_0+q^t_1a_1)2^b,
\tag{4.2}
\]

\[
Q_z=\max\{a_0b_0,a_1b_1\}2^b,
\tag{4.3}
\]

and, when `b>0`,

\[
Q_f=h/2.
\tag{4.4}
\]

Finally put

\[
\boxed{Q=\max\{Q_s,Q_t,Q_z,Q_f\}},
\tag{4.5}
\]

omitting `Q_f` when `b=0`.

### R03-C274a — overlap-one affine hyperplane cap

**STATUS: PROVED for every finite class used below.** Every proper linear hyperplane `H<V^perp` satisfies

\[
\boxed{|H\cap C_V|\le Q.}
\tag{C274a}
\]

**Proof.** Write the defining nonzero linear functional of `H` in the coordinates of (3.3). If its `A_s` parameter part is nonzero, condition on `z`, the `A_t` parameters and all free Boolean coordinates. For fixed conditioned data the remaining equation is one affine fiber of a nonzero functional on `A_{s,alpha}(z)`, so it has at most `q^s_z` solutions. Summing over the conditioned choices gives `Q_s`. The same argument gives `Q_t` if the `A_t` part is nonzero. If both relation-block parts vanish but a free Boolean coefficient is nonzero, condition on all other free bits; at most one of the two values of that bit survives, giving `h/2`. If only the overlap-bit coefficient remains, at most one overlap fiber survives, bounded by `Q_z`. These cases exhaust every nonzero functional. `square`

Independently, the cube/subspace lemma gives

\[
|W\cap\{0,1\}^m|\le2^{\dim W}
\tag{4.6}
\]

for every linear subspace `W`. Every proper `j`-dimensional span in `V^perp` lies in a hyperplane, so after `j<m-2` independent Boolean columns have been selected, at most

\[
\min\{2^j,Q\}
\]

points of `C_V` are trapped in their span. Therefore the number of ordered Boolean bases of `V^perp` contained in `C_V` is at least

\[
\boxed{
B_V=
\prod_{j=0}^{m-3}
\left(h-\min\{2^j,Q\}\right).
}
\tag{4.7}
\]

After choosing these `m-2` basis columns, there are

\[
(h-m+1)(h-m)
\tag{4.8}
\]

ordered choices for two additional distinct unused nonzero Boolean columns.

The resulting `m` columns span exactly `V^perp`, so the left modular nullspace is exactly `V` and the modular nullity is exactly two. Since (3.1) has no support-one or support-two vector, no row is zero and no two rows are equal. The columns are nonzero and pairwise distinct by construction. Thus every constructed matrix lies in `G_m`.

### R03-C274b — exact-corank-two overlap-one family

Let `N_{m;s,t,alpha,beta}` be the run21 exact orbit multiplicity for the corresponding overlap-one plane class. Then

\[
\boxed{
E_{m,p;s,t,\alpha,\beta}
:=
N_{m;s,t,\alpha,\beta}
B_V(h-m+1)(h-m)
}
\tag{C274b}
\]

counts distinct matrices in `G_m` of exact modular nullity two and exact left nullspace equal to one of those planes.

Different planes cannot yield the same counted matrix because an exact two-dimensional left nullspace is unique. These matrices are disjoint from run26's disjoint-support exact-corank-two families by the projective support spectrum, and from run25's exact-corank-three family by nullity.

## 5. Method #16 — exact small-case extremal fibers

The global thirty-move inventory had only #1 and #24 unused before this run. The instruction nevertheless requires three moves; after exhausting those last two new entries I reused #16, last used many runs ago, rather than repeating run26's triple.

Executed checker:

`artifacts/R03/20260917T0408Z_27_overlap1_affine_code_exact.py`.

Archived output:

`artifacts/R03/20260917T0408Z_27_overlap1_affine_code_exact.out`.

The checker exhausts one projective representative of **every nonzero local functional** needed for the support classes through `r=8`, computes each maximum affine fiber exactly, reconstructs every run21 overlap-one orbit multiplicity, checks the total plane counts

\[
275940\quad(m=9),
\qquad
1524600\quad(m=10),
\]

and then evaluates the exact-corank-two basis lower bounds and C253 slack corrections using rational arithmetic. Output ends `SELF-CHECK PASS`.

The local overlap-conditioned slice data are independent of `p` for the two primes used here. Representative values include

\[
\begin{array}{c|cc}
r,\text{class}&(|A(0)|,q(0))&(|A(1)|,q(1))\\ \hline
3,\text{minority}&(1,1)&(2,1)\\
3,\text{majority}&(2,1)&(1,1)\\
4,\text{even}&(3,2)&(3,2)\\
5,\text{minority}&(4,3)&(6,4)\\
5,\text{majority}&(6,4)&(4,3)\\
6,\text{even}&(10,6)&(10,6)\\
7,\text{minority}&(15,10)&(20,12)\\
7,\text{majority}&(20,12)&(15,10)\\
8,\text{even}&(35,20)&(35,20).
\end{array}
\tag{5.1}
\]

These are finite exact facts, not an asymptotic theorem.

## 6. Exact metric movement

### 6.1 `m=9`, `p=7`, sign order `n=10`

Summing C274b over **all** run21 overlap-one plane classes gives

\[
\boxed{
E^{\mathrm{ov1}}_{9,7}
=161033925481239358800
}
\tag{6.1}
\]

certified exact-corank-two matrices.

The retained nullity ceiling is `D=4`, hence

\[
c_{7,4}=\frac7{50},
\qquad
7-c_{7,4}=\frac{343}{50}.
\]

Because run21 already paid each of these exact null planes once in `M_2`, C253 may now subtract the remaining exact-nullity-two slack. Under the retained sign/binary normalization, the additional normalized correction is

\[
\boxed{
\Delta_{10}
=2^{10-81}\frac{343}{50}E^{\mathrm{ov1}}_{9,7}
=
\frac{138086591100162750171}
{295147905179352825856}
}
\tag{6.2}
\]

\[
=0.4678555689434811735781083019\ldots .
\]

Therefore

\[
\boxed{
r(10)
\le
\frac{81207138539551628924901}
{295147905179352825856}
=275.1404875809787806891\ldots .}
\tag{C275.1}
\]

### 6.2 `m=10`, `p=11`, sign order `n=11`

Summing over all run21 overlap-one classes gives

\[
\boxed{
E^{\mathrm{ov1}}_{10,11}
=54110299527722427720192000.
}
\tag{6.3}
\]

The retained ceiling is `D=5`, so

\[
c_{11,5}=\frac{132}{16105},
\qquad
11-c_{11,5}=\frac{177023}{16105}.
\]

The additional normalized correction is

\[
\boxed{
\Delta_{11}
=
\frac{467713259438281607534743575}
{486743758122340071466074112}
}
\tag{6.4}
\]

\[
=0.9609024289135819502579666570\ldots .
\]

Hence

\[
\boxed{
r(11)
\le
\frac{4080135425100039167106240490725}
{7787900129957441143457185792}
=523.9070040722692279998\ldots .}
\tag{C275.2}
\]

This is a strict replay-certified improvement over run26 at both finite dimensions.

## 7. Full-domain envelope and honest limitation

The full `n`-domain is preserved. All exact values through `n=9` remain unchanged. Replace the run26 entries at `n=10,11` by C275.1--C275.2. For every `n>=12`, retain the previous pointwise minimum of all certified branches; C274 is an additional exact-corank cleanup mechanism and cannot invalidate any earlier bound.

This remains **PARTIAL**. It does not prove `r(n)=o(n^2)`.

Indeed for fixed support types `(s,t,alpha,beta)`, the overlap-one Boolean slice has

\[
h=C_{s,t,\alpha,\beta}\,2^{m-(s+t-1)}
\]

with fixed `C<2^{s+t-1}`. Thus, after normalization by `2^{m^2}`, the total mass of any fixed bounded-support family is polynomial in `m` times an exponentially decaying factor. This is the same asymptotic warning reached by the disjoint-support work: **bounded sparse support can sharpen finite metrics but cannot be the source-level asymptotic engine.**

The remaining source-level obstruction is therefore still the collision-free small-corank **dense / unstructured** sector. Run22's sufficiently large squarefree CRT modulus removes accidental one-prime determinant divisibility; run23 shows worst-case rank floors cannot eliminate exceptional low-rank matrices; runs24--27 show how to reclaim incidence slack when exact corank and enough structure are available. The next genuinely source-level target is a distributional inverse Littlewood--Offord estimate for dense primitive CRT null witnesses at the actual

\[
o(n^2 2^{-n})
\]

scale.

## 8. Neighboring track and model/runtime status

The newest R04 report is `runs/R04/20260917T0310Z_i0027_retirement_handoff.md`, commit `4545249b426e89d92c2f8a945ea930c5b189d37f`. It is a retirement/handoff report after six unchanged runs and contains no new theorem requiring a fresh R03 audit. I did not manufacture a duplicate audit.

The model-setting limitation is still true. The exposed task mutation schema provides prompt/title, schedule or relative start, timing mode, and enabled state, but **no model-family or reasoning-effort field** and no authenticated applied-runtime telemetry. `RESULTS.md` records that some edits returning `You cannot modify this task` in one context later succeeded from another authorized context. The legitimate workaround is therefore the owning/admin-authorized native-task context if it exposes model controls, or platform support; duplicating a task or bypassing authorization is not appropriate. No scheduler mutation was attempted in this run.

## 9. Status and ledger delta

C274a/b: **PROVED NEW**, finite local core exhaustively checked.  
C275.1/C275.2: **PROVED NEW**, exact rational metric improvement.  
Source asymptotic: **OPEN**.  
R03: **PARTIAL**.  
Consecutive unchanged count: `0` because the fixed metric moved.  
No source closure, no novelty certificate, no paper package, and no new audit claim.

```yaml
ledger_delta:
  worker: R03
  source: "iid nonsymmetric Rademacher singularity / Komlos-Vu-Jain-Sah-Sawhney lineage"
  target: "P(det B_n=0)=(1+o(1)) n(n-1) 2^(1-n)"
  metric: "r(n)=2^n P(det B_n=0,T_n^c), full-n-domain certified upper envelope"
  before:
    r10_upper: "1271019142666434244923/4611686018427387904 = 275.608343149922234..."
    r11_upper: "4087618837251051672826796387925/7787900129957441143457185792 = 524.867906501182802..."
  after:
    r10_upper: "81207138539551628924901/295147905179352825856 = 275.140487580978780689..."
    r11_upper: "4080135425100039167106240490725/7787900129957441143457185792 = 523.907004072269227999..."
  movement: true
  status: PARTIAL
  source_status: OPEN
  unchanged_count: 0
  methods: [1, 24, 16]
  new_claims: [R03-C274a, R03-C274b, R03-C275.1, R03-C275.2]
  checker: "artifacts/R03/20260917T0408Z_27_overlap1_affine_code_exact.py"
  checker_output: "artifacts/R03/20260917T0408Z_27_overlap1_affine_code_exact.out"
  source_record: "artifacts/R03/20260917T0408Z_27_status_search.md"
  next_obligation: "dense small-corank primitive-CRT null-witness control at o(n^2 2^-n) scale"
```

No shared root ledger, peer track file, email, Drive file, public post, purchase, permission, workflow, or scheduler state was modified.
