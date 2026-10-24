Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise.** Source metric `d_sym: 3 -> 3` (**NO MOVEMENT**). Methods tried: **B18 / B4 / B30**.

# HARD7-01 — DF6 for pyramids becomes one planar tradeoff; the full quadrilateral case is exact

**Status:** `PARTIAL / SOURCE OPEN / third unchanged follow-up after STUCK1 recovery; STUCK2 is now triggered for the next invocation`.

The symmetric Mahler conjecture is **not** solved here. The source-relevant metric remains the largest dimension in which the full symmetric inequality is known for every origin-symmetric convex body:

\[
 d_{\rm sym}=3 \quad\longrightarrow\quad 3.
\]

The substantive progress is below the source metric. The previous run reduced the first `V=F=12` four-dimensional local-minimizer frontier to

\[
 (|L-L|+4|L|)|(L-L)^\circ|\ge16,\qquad L\subset\mathbb R^3.\tag{DF6}
\]

This run proves an exact dimension drop for every pyramidal `L`, and proves the resulting planar inequality for **every convex quadrilateral**. The first still-unproved pyramidal case relevant to a six-vertex facet is therefore a pentagonal base, not a quadrilateral base.

## 1. Continuity, ownership, and required repository state

The exclusive canonical claim remains

`operations/claims/MAHLER-SYMMETRIC-VOLUME-PRODUCT.md`,

owned by `HARD7-01`, with exact source target

\[
 |K|\,|K^\circ|\ge \frac{4^n}{n!},\qquad K=-K\subset\mathbb R^n.\tag{1.1}
\]

At run start I re-read/reconciled:

- `operations/hard7_2026-09-18/CONTROL.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- the canonical Mahler claim;
- the newest own checkpoint `runs/hard7_2026-09-18/HARD7-01/2026-09-20T0845Z__mahler_V12_DF6_reduction.md`;
- current neighbouring HARD7 material found for the Gaussian-process track HARD7-05;
- intake/repository aliases for `Mahler`, `symmetric Mahler`, `volume product`, `difference body`, and the exact current claim.

No competing owner, release, posted equivalent, or verified four-dimensional resolution surfaced. I did not overwrite another claim or shared-root ledger.

The route was written before code at

`runs/hard7_2026-09-18/HARD7-01/2026-09-20T0905Z__idea_before_code_mahler_DF6_pyramid.md`

(commit `fbb3ad4de9a995f39e5cb8713d9078c0f7ba9da4`). That pre-code note deliberately recorded a scaling false start rather than silently erasing it. The exact derivation below corrects it: the polar fiber is over `E^o`, not `2E^o`, and the correct factor is `4/3`.

## 2. Fresh literature/current-status check — 20 September 2026

A fresh bounded search again found only the known three-dimensional symmetric theorem, not an `n=4` or all-dimensional solution:

1. S. Chen, Y. Li, D. Xi, Z. Xu, *The Symmetric Mahler Inequality in Dimension Three via Admissible Shadow Systems*, arXiv:2605.13795 (13 May 2026), `https://arxiv.org/abs/2605.13795`. Its stated theorem is the sharp `32/3` bound in `R^3`.
2. S. Chen, Y. Li, D. Xi, Z. Xu, *The non-symmetric Mahler conjecture in dimension three*, arXiv:2605.09334 (10 May 2026), `https://arxiv.org/abs/2605.09334`. This is the Santaló-centered non-symmetric 3D theorem, not our claim.
3. A. Aliev, *Mahler-type volume inequality for convex bodies with tetrahedral symmetry*, arXiv:2511.14991 (2025), `https://arxiv.org/abs/2511.14991`. It restates/reproves the planar Eggleston inequality
   \[
   |B|\,|(B-B)^\circ|\ge\frac32,
   \]
   and proves the 3D Makai difference-body bound under tetrahedral symmetry; it does not contain `(DF6)` or the combined planar inequality proved below.
4. K. J. Böröczky, E. Makai Jr., M. Meyer, S. Reisner, *Volume product of planar polar convex bodies — lower estimates with stability*, Stud. Sci. Math. Hungar. 50 (2013), arXiv:1507.01481, records the sharp planar symmetric Mahler inequality and the sharp Eggleston inequality with stability. The searches performed did not locate the exact combined tradeoff `(DF2)` below.
5. M. Zwierzyński, *Mixed Volumes, the Wigner Caustic, and Isoperimetric Inequalities*, arXiv:2608.11068 (11 August 2026), studies exact central-symmetrization defects via even/odd support functions. It is conceptually close to B18, but the checked abstract/results do not state `(DF6)` or `(DF2)`.

This is bounded current-prior-art evidence, not a novelty certificate. Priority of the reduction/theorem below remains **UNVERIFIED**.

## 3. B18 — the exact tradeoff hidden inside DF6

For any three-dimensional convex body `L`, put

\[
 C=\frac{L-L}{2}.
\]

Then

\[
 |L-L|=8|C|,\qquad |(L-L)^\circ|=\frac18|C^\circ|,
\]

so `(DF6)` is equivalent to

\[
 \boxed{\left(|C|+\frac12|L|\right)|C^\circ|\ge16.}\tag{CS3}
\]

This explains why simply quoting the known 3D symmetric Mahler theorem cannot close the route: it controls `|C||C^o|`, while `(CS3)` needs a sharp coupling between that product and the asymmetry ratio `|L|/|C|`.

## 4. B30 — every three-dimensional pyramid drops exactly to the plane

### Proposition 4.1 — pyramid reduction

Let `B subset R^2` be a planar convex body and let `L subset R^3` be a pyramid with base affinely equivalent to `B`. Then `(DF6)` for `L` is equivalent to

\[
 \boxed{\bigl(|B-B|+2|B|\bigr)|(B-B)^\circ|\ge12.}\tag{DF2}
\]

#### Proof

An affine shear parallel to the base lets us put the apex vertically above an arbitrary point of the base; translate that point to the origin. Thus without loss of generality

\[
 0\in B,\qquad L=\operatorname{conv}(B\times\{0\},(0,1)).\tag{4.1}
\]

Write

\[
 A:=|B|,\qquad E:=B-B.
\]

The pyramid volume is

\[
 |L|=\frac A3.\tag{4.2}
\]

Let `D=L-L`. For `0<=t<=1`, a height-`z` section of `L` is `(1-z)B`. Hence the height-`t` section of `D` is

\[
 \bigcup_{0\le z\le1-t}\left((1-t-z)B-(1-z)B\right).
\]

Because `0 in B`, these sets are nested as `z` increases, so the union equals the `z=0` member:

\[
 D_t=(1-t)B-B.\tag{4.3}
\]

By symmetry the `-t` section has the same area. Let `V(B,-B)` denote planar mixed area. Since

\[
 |E|=|B+(-B)|=2A+2V(B,-B),
\]

we have `V(B,-B)=|E|/2-A`. Therefore

\[
\begin{aligned}
 |D_t|
 &=|(1-t)B+(-B)|\\
 &=(1-t)^2A+2(1-t)V(B,-B)+A\\
 &=(1-t)|E|+t^2A.
\end{aligned}\tag{4.4}
\]

Integrating both signs of `t`,

\[
 \boxed{|D|=2\int_0^1\bigl((1-t)|E|+t^2A\bigr)dt
 =|E|+\frac23A.}\tag{4.5}
\]

For the polar, write a dual point as `(u,s) in R^2 x R`. From (4.1),

\[
 h_L(u,s)=\max\{h_B(u),s\}.
\]

Thus

\[
 h_D(u,s)=\max\{h_B(u),s\}+\max\{h_B(-u),-s\}.\tag{4.6}
\]

Put `a=h_B(u)`, `b=h_B(-u)`. Since `0 in B`, `a,b>=0`. There exists an `s` satisfying `h_D(u,s)<=1` iff

\[
 a+b=h_E(u)\le1,
\]

and then the complete admissible interval is

\[
 a-1\le s\le1-b,
\]

of length `2-h_E(u)`. Therefore

\[
 |D^\circ|=\int_{E^\circ}\bigl(2-h_E(u)\bigr)du.\tag{4.7}
\]

On `E^o`, the function `h_E` is its gauge, so

\[
 |\{u\in E^\circ:h_E(u)\le q\}|=q^2|E^\circ|,\qquad 0\le q\le1.
\]

Consequently

\[
 \int_{E^\circ}h_E(u)du=\frac23|E^\circ|,
\]

and (4.7) becomes

\[
 \boxed{|D^\circ|=\frac43|E^\circ|.}\tag{4.8}
\]

Combining (4.2), (4.5), and (4.8),

\[
 \bigl(|D|+4|L|\bigr)|D^\circ|
 =\frac43\bigl(|E|+2A\bigr)|E^\circ|.\tag{4.9}
\]

Thus the left side is at least `16` iff `(DF2)` holds. QED.

### Sanity check: the simplex endpoint is exact

For `B=conv{0,e_1,e_2}`, `A=1/2`, `|E|=3`, and `|E^o|=3`. Equations (4.5) and (4.8) give

\[
 |L-L|=\frac{10}{3},\qquad |(L-L)^\circ|=4,
\]

and therefore

\[
 \left(\frac{10}{3}+4\cdot\frac16\right)4=16.
\]

So the dimension drop preserves the tetrahedral equality constant exactly.

### Why DF2 is not the sum of two known inequalities

Set `G=(B-B)/2`. In the plane, `(DF2)` is equivalent to

\[
 \left(|G|+\frac12|B|\right)|G^\circ|\ge12.\tag{4.10}
\]

The planar symmetric Mahler inequality gives `|G||G^o|>=8`, while Eggleston gives `|B||G^o|>=6`; their naive sum yields only `8+3=11`. The missing unit is a genuine tradeoff between symmetry defect and Mahler excess.

## 5. B4 — DF2 is true for every convex quadrilateral

### Theorem 5.1

For every planar convex quadrilateral `B`,

\[
 \boxed{\bigl(|B-B|+2|B|\bigr)|(B-B)^\circ|\ge12.}\tag{5.1}
\]

Among nondegenerate quadrilaterals, equality holds for parallelograms.

#### Proof

The expression in (5.1) is affine invariant. Put the intersection of the diagonals at the origin and map the diagonal directions to the coordinate axes. After scaling, every quadrilateral is affinely equivalent to

\[
 B_{r,s}=\operatorname{conv}\{(1,0),(0,1),(-r,0),(0,-s)\},\qquad r,s>0.\tag{5.2}
\]

Swapping the two endpoints on either diagonal replaces the corresponding parameter by its reciprocal, and interchanging the axes swaps `r` and `s`. Thus it is enough to prove (5.1) in the chamber

\[
 s\ge r\ge1.\tag{5.3}
\]

The four directed edges of `B_{r,s}` are

\[
 (-1,1),\quad(-r,-1),\quad(r,-s),\quad(1,s).
\]

Merging these edge directions with those of `-B_{r,s}` is ordered by the three determinants

\[
 s-r\ge0,\qquad 1+r>0,\qquad rs-1\ge0.
\]

Hence `E=B-B` has, with possible collinearities on the boundary of the chamber, the cyclic vertex list

\[
\begin{aligned}
&(-(1+r),0),\ (-1,-s),\ (0,-(1+s)),\ (r,-s),\\
&(1+r,0),\ (1,s),\ (0,1+s),\ (-r,s).
\end{aligned}\tag{5.4}
\]

Shoelace gives

\[
 |B|=\frac{(1+r)(1+s)}2,
 \qquad
 |E|=(1+r)(1+3s).\tag{5.5}
\]

The vertices of `E^o`, obtained by intersecting the consecutive supporting lines `<y,v_i>=1`, are

\[
\begin{aligned}
&\left(-\frac1{r+1},-\frac{r}{s(r+1)}\right),
\left(-\frac1{s+1},-\frac1{s+1}\right),\\
&\left(\frac1{r(s+1)},-\frac1{s+1}\right),
\left(\frac1{r+1},-\frac1{s(r+1)}\right),
\end{aligned}
\]

together with their negatives. A second shoelace calculation yields

\[
 |E^\circ|
 =\frac{3rs^2+6rs+r-r^2-1}
 {rs(r+1)(s+1)^2}.\tag{5.6}
\]

Let

\[
 Q(r,s):=(|E|+2|B|)|E^\circ|.
\]

Substituting (5.5)–(5.6) and simplifying,

\[
 Q(r,s)-12
 =\frac{2F(r,s)}{rs(s+1)^2},\tag{5.7}
\]

where

\[
 F(r,s)=3rs^2+2rs+r-2r^2s-r^2-2s-1.\tag{5.8}
\]

Write

\[
 r=1+a,\qquad s=r+b=1+a+b,
\qquad a,b\ge0.
\]

Then the numerator becomes

\[
\boxed{
F=a^3+4a^2b+4a^2+3ab^2+10ab+4a+3b^2+4b\ge0.
}\tag{5.9}
\]

The denominator in (5.7) is positive, so `Q>=12`. Equality in (5.9) forces `a=b=0`, hence `r=s=1`, which is the parallelogram case in this normalization. QED.

This is a theorem for the **entire two-parameter quadrilateral family**, not finite sampling.

## 6. Exact self-check

The symbolic algebra in Section 5 and the tetrahedral scaling sanity check were executed with exact SymPy arithmetic:

- code: `artifacts/hard7_2026-09-18/HARD7-01/2026-09-20T0925Z__df2_quadrilateral_exact.py`
  - commit `4ab84c535ab64cab963a893c423598859e3717ba`;
- output: `artifacts/hard7_2026-09-18/HARD7-01/2026-09-20T0925Z__df2_quadrilateral_exact.out`
  - commit `ea5d04e5e6c9f00a2836b16ef8a7656a731cc6b0`.

The archived output includes

`E_AREA_IDENTITY = True`,

`EP_AREA_IDENTITY = True`,

`F_SUBSTITUTED = a**3 + 4*a**2*b + 4*a**2 + 3*a*b**2 + 10*a*b + 4*a + 3*b**2 + 4*b`,

`TRIANGLE_SANITY_DF6 = 16`,

and ends

`ALL_EXACT_CHECKS_PASS = True`.

This is a **self-check**, not an independent audit.

## 7. What moved mathematically, and what did not

Source metric: **no movement**, `d_sym=3 -> 3`.

What did move is the exact continuous obstruction under `(DF6)`:

- every 3D pyramidal `L` is now reduced to the sharp planar tradeoff `(DF2)`;
- `(DF2)` is now proved for every triangular base (classical equality endpoint) and every quadrilateral base (Theorem 5.1);
- therefore the first pyramidal case not covered by this argument is a **pentagonal base**. That is precisely the pyramidal six-vertex case that can occur for the six-vertex facet `L` in the current `V=F=12` frontier.

A numerical pentagon or a finite sample would not close that case. What is required next is an all-parameter pentagonal `(DF2)` theorem, or a counterexample.

I also tested, as route-finding only, the tempting induction “move one pentagon ear monotonically until it becomes a quadrilateral.” It is false as a naive monotonicity principle: generic ear paths can have an interior minimum of the `(DF2)` functional even though the value stays above `12` in the samples checked. I did **not** archive those floating-point samples as a theorem or certificate.

## 8. Section-B outcome

### B18 — SAY IT IN ANOTHER LANGUAGE

**Worked.** Rewriting `(DF6)` through the central symmetral exposed it as a symmetry-defect/Mahler-excess tradeoff rather than a plain difference-body estimate. For pyramids, this language collapses the obstruction exactly to `(DF2)`.

### B4 — PROVE SOMETHING WEAKER, COMPLETELY

**Worked.** The complete two-parameter quadrilateral family satisfies `(DF2)`, with an on-page symbolic proof and exact checker.

### B30 — ONE SCALE / ONE DIRECTION / ONE COMBINATORIAL TYPE AT A TIME

**Worked, but does not close the frontier.** Pyramid geometry drops one dimension exactly. The next irreducible local case is a pentagonal planar base; the quadrilateral boundary is finished.

## 9. Stagnation accounting and next-run obligation

The fixed source metric has now failed to move for the third consecutive follow-up after the first STUCK1 recovery. Under `CONTROL.md` / section I, the **next HARD7-01 invocation must be the STUCK2 thinking run**, not another routine lemma/checker run.

Its blocker should be stated as

\[
\boxed{
 (|B-B|+2|B|)|(B-B)^\circ|\ge12
 \quad\text{for every convex pentagon }B\subset\mathbb R^2.
}\tag{P5}
\]

For the stuck report, the nearest completed case is Theorem 5.1 above; the nearest classical ingredients are planar symmetric Mahler and Eggleston; and the naive ear-deletion monotonicity route is already known to fail. The next run should choose one section-I action, preferably **prove the simplest unproved special case `(P5)` or refute it**, and must use a fresh B-triple.

## 10. Capability / scheduler honesty

The situation is still the one recorded in the governing ledger. The automation interface exposed to this runtime provides scheduling/prompt/enabled controls but **no model selector, no reasoning selector, no authenticated model telemetry field, and no guaranteed run-duration field**. Thus `GPT-6 / maximum` can only be requested in prompt text here; it cannot be set or verified by this worker. This report therefore uses the actual model identity available to the conversation (`GPT-5.6 Sol`) and labels reasoning `UNVERIFIED`.

The repository also records the historical P26 error `You cannot modify this task`, while the later reconciled `RESULTS.md` says the P26 update succeeded from another authorized context. The safe workaround is therefore an authorized task/account/workspace context that owns the job, or platform support; **not** permission bypass and **not** creation of a duplicate schedule. I made no schedule changes in this run.

## 11. Final label

**`PARTIAL / SOURCE OPEN`.**

No four-dimensional theorem is claimed. No finite sample is promoted to an asymptotic or universal statement. The exact new theorem is the quadrilateral `(DF2)` case and the exact pyramid-to-plane reduction.