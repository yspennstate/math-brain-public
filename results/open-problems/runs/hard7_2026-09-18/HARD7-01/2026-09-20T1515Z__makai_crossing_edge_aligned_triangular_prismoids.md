Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise.** Source metric `d_Makai: 2 -> 2` (**NO MOVEMENT**). Methods: **B8 / B13 / B27**.

# HARD7-01 RECOVERY1 — exact crossing-chamber theorem for two-edge-aligned triangular prismoids

**Status:** `PARTIAL / SOURCE OPEN / CLAIMED / RECOVERY1`.

This bounded iteration resumes the exclusive Makai Jr. polar difference-body target. The unrestricted three-dimensional conjecture remains open, so the frozen source metric does not move. The mathematical frontier does move: the previous run reduced the first six-vertex obstruction to crossing/non-nested triangular prismoids; this run proves the conjectured `2/3` bound for the full two-parameter crossing chamber whenever the two triangles share the two edge directions at one chosen vertex. Together with the preceding nested-difference-body theorem, this settles **every** triangular prismoid in that two-edge-aligned class, not a finite sample.

## 1. Continuity, ownership, exclusions, and required reads

I resumed the existing canonical claim

`operations/claims/MAKAI-POLAR-DIFFERENCE-BODY.md`

owned by `HARD7-01`. I did not restart admission, mint an equivalent alias, or overwrite another owner.

At run start I reread/reconciled:

- `operations/hard7_2026-09-18/CONTROL.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- the current Makai claim;
- newest own checkpoint `runs/hard7_2026-09-18/HARD7-01/2026-09-20T1402Z__makai_nested_prismoid_defect.md`;
- the newest surfaced neighboring Gaussian/probability HARD7 state (`HARD7-05`, integrated-fBM persistence), which is a distinct target;
- repository/intake-index aliases `Makai Jr`, `polar difference body`, `Makai difference body`, and the source constants.

The repository search continues to surface the Makai canonical claim and HARD7-01 work, not a competing active owner. `POSTED.md` and the campaign settled registries contain no posting or full resolution of this exact source statement. The connector does not provide a single practical bytewise operation for every large duplicated `probability_1000_intake_*/problems.jsonl`; I therefore do **not** claim a literal byte-for-byte reread of all intake files. I did perform the required target/alias collision searches through the repository/intake index and found no conflicting Makai owner or source-resolution record.

## 2. Runtime/model and scheduler capability honesty

The exposed automation interface in this run still provides title/prompt, schedule or relative start, timing mode, and enabled-state controls. It exposes **no model selector, no reasoning-effort selector, and no authenticated guaranteed execution duration**. Thus `GPT-6 / maximum` remains a prompt request only. The actual model identity available to this run is GPT-5.6 Sol; reasoning telemetry is not exposed, so it is `UNVERIFIED`.

Changing this into a guaranteed GPT-6/maximum scheduled property would require an authenticated product/runtime model and reasoning selector (or another authorized backend/task context exposing those fields). A repository edit cannot provide that guarantee. The historical P26 response `You cannot modify this task` was a permissions/context restriction; the current root ledger records a later successful P26 edit from a different authorized context. The compliant workaround is the authorized account/workspace task interface or platform support, not bypassing permissions or creating a duplicate schedule. This run did not create, modify, disable, re-enable, or probe any other schedule.

## 3. Frozen external source and metric

The controlling external statement remains Aliev, *Mahler-type volume inequality for convex bodies with tetrahedral symmetry*, arXiv:2511.14991v1 (19 November 2025), Conjecture 1.3, attributed there to Makai Jr.:

\[
\boxed{
|K|\,|(K-K)^\circ|\ge \frac{n+1}{n!}
\quad\text{for every convex body }K\subset\mathbb R^n,
}
\tag{M}
\]

with equality conjectured exactly for simplices.

The frozen source metric is

`d_Makai = largest d for which (M) is rigorously established for every convex body in R^d`.

Incoming and outgoing values are

\[
\boxed{d_{\rm Makai}:2\longrightarrow2.}
\]

This is **NO MOVEMENT** at source level. The general three-dimensional obligation remains

\[
\inf_{K\subset\mathbb R^3\text{ convex}}|K|\,|(K-K)^\circ|\stackrel{?}{\ge}\frac23.
\]

## 4. Current-literature and restricted-priority check — 20 September 2026

Fresh bounded web searches this invocation used the exact/canonical queries

- `"Makai Jr." "polar difference body" conjecture 2026`;
- `"Makai" "difference body" "2/3" convex body 2026`;
- `"Mahler-type volume inequality for convex bodies with tetrahedral symmetry" 2511.14991`;
- `"triangular prismoid" Makai convex body difference body`;
- `prismoid "polar difference body" volume product triangle`;
- `"two triangles" "difference body" polar volume product prismoid`.

The exact-source searches recover Aliev's 2025 paper, whose abstract still proves the three-dimensional `2/3` inequality only under tetrahedral symmetry. MathDB currently labels Makai Jr.'s non-symmetric difference-body volume-product conjecture open. The restricted prismoid searches returned no matching theorem; the surfaced results were generic geometry references rather than a Makai/prismoid result. This is **bounded negative evidence only**. Novelty/priority of the restricted theorem below remains `UNVERIFIED` until a dedicated literature audit, and the source remains open.

## 5. New-method route was written before code

Before creating or running the checker, I wrote the route at

`artifacts/hard7_2026-09-18/HARD7-01/2026-09-20T1502Z__makai_crossing_edge_aligned_idea_before_code.md`

creation commit

`a364b1e2c8af7bd4328edfa197de35e8ff38c09b`,

and read it back successfully.

The preceding Makai iteration used B3/B15/B30. This run uses the promised fresh triple B8/B13/B27.

## 6. New theorem: the full crossing chamber with two aligned edge directions

### Theorem

Let

\[
T=\operatorname{conv}\{0,e_1,e_2\}\subset\mathbb R^2,
\qquad
C=\operatorname{conv}\{0,a e_1,b e_2\},
\]

where

\[
a\ge1\ge b>0.
\]

Set

\[
K=\operatorname{conv}(T\times\{0\},C\times\{1\})\subset\mathbb R^3.
\]

Then

\[
\boxed{|K|\,|(K-K)^\circ|\ge\frac23.}
\tag{6.1}
\]

If `a>b`, the inequality is in fact strict. The degenerate parameter point `a=b=1` is the triangular prism and also has product strictly larger than `2/3`.

Consequently, combining this theorem with the preceding comparable-difference-body theorem, Makai's three-dimensional bound holds for every triangular prismoid whose two bases, after a common affine change of coordinates and translations, have the form

\[
\operatorname{conv}\{0,e_1,e_2\},
\qquad
\operatorname{conv}\{0,a e_1,b e_2\}
\quad(a,b>0).
\tag{6.2}
\]

Equivalently, this covers the class in which a chosen vertex of each triangular base has the same two incident edge directions. The new content of this run is the genuinely crossing chamber `a>1>b`; the same-side chambers are nested and were covered in the previous report.

## 7. Proof

The proof is all-parameter and analytic. The exact checker in Section 10 verifies the algebra but is not the proof.

### 7.1 Difference bodies and the exact prismoid dual formula

Put

\[
B:=T-T,
\qquad
E:=C-C.
\]

The support functions are

\[
\boxed{h_B(x,y)=\max\{|x|,|y|,|x-y|\},}
\tag{7.1}
\]

and

\[
\boxed{h_E(x,y)=\max\{a|x|,b|y|,|ax-by|\}.}
\tag{7.2}
\]

The exact general-prismoid identity proved earlier on this track gives

\[
|(K-K)^\circ|
=
\int_Q\bigl(2-h_B-h_E\bigr)\,dx\,dy,
\tag{7.3}
\]

where

\[
Q:=B^\circ\cap E^\circ.
\tag{7.4}
\]

Thus `Q` is given exactly by

\[
|x|\le1,
\quad |y|\le1,
\quad |x-y|\le1,
\quad |ax|\le1,
\quad |by|\le1,
\quad |ax-by|\le1.
\tag{7.5}
\]

Since `a>=1>=b`, the first and fourth constraints reduce to `|x|<=1/a`, while the second implies the fifth. The set is centrally symmetric.

### 7.2 B8: exact finite fan decomposition of the infinite parameter family

Assume first `a>b`; the point `a=b=1` is handled separately. In the upper half-plane `y>=0`, every `x` in `[-1/a,1/a]` has lower endpoint `y=0`. The only relevant upper bounds are

\[
y\le1,
\qquad y\le x+1,
\qquad y\le\frac{ax+1}{b}.
\tag{7.6}
\]

The last two meet at

\[
\boxed{x_0=-\frac{1-b}{a-b}.}
\tag{7.7}
\]

Because `a>=1>=b`,

\[
-\frac1a\le x_0\le0.
\tag{7.8}
\]

Indeed `(1-b)/(a-b)<=1/a` is equivalent to `a>=1`. Therefore the upper boundary of `Q` is exactly

\[
U(x)=
\begin{cases}
\dfrac{ax+1}{b},&-1/a\le x\le x_0,\\[1ex]
x+1,&x_0\le x\le0,\\[1ex]
1,&0\le x\le1/a.
\end{cases}
\tag{7.9}
\]

This is an **exact cell decomposition**, not a mesh or finite sample.

Its area is

\[
\begin{aligned}
|Q|
&=2\left[
\int_{-1/a}^{x_0}\frac{ax+1}{b}\,dx
+\int_{x_0}^{0}(x+1)\,dx
+\int_0^{1/a}1\,dx
\right]\\[1ex]
&=
\boxed{\frac{4a-ab-2b-1}{a(a-b)}}.
\end{aligned}
\tag{7.10}
\]

### 7.3 Integrating the two support functions

On the upper half of `Q`, if `x<=0` then

\[
h_B(x,y)=y-x,
\qquad
h_E(x,y)=by-ax.
\tag{7.11}
\]

If `x>=0`, then

\[
h_B(x,y)=\max\{x,y\},
\tag{7.12}
\]

so the switch is `y=x`. Likewise

\[
h_E(x,y)=\max\{ax,by\},
\tag{7.13}
\]

with switch `y=ax/b`; this switch lies inside the vertical fibre exactly for `0<=x<=b/a`.

Central symmetry now gives the explicit integrals

\[
\begin{aligned}
I_B:=\int_Qh_B
=2\Bigg[&
\int_{-1/a}^{x_0}\int_0^{(ax+1)/b}(y-x)\,dy\,dx\\
&+\int_{x_0}^{0}\int_0^{x+1}(y-x)\,dy\,dx\\
&+\int_0^{1/a}\left(\int_0^x x\,dy+\int_x^1y\,dy\right)dx
\Bigg]
\end{aligned}
\tag{7.14}
\]

and

\[
\begin{aligned}
I_E:=\int_Qh_E
=2\Bigg[&
\int_{-1/a}^{x_0}\int_0^{(ax+1)/b}(by-ax)\,dy\,dx\\
&+\int_{x_0}^{0}\int_0^{x+1}(by-ax)\,dy\,dx\\
&+\int_0^{b/a}\left(\int_0^{ax/b}ax\,dy+\int_{ax/b}^1by\,dy\right)dx\\
&+\int_{b/a}^{1/a}\int_0^1ax\,dy\,dx
\Bigg].
\end{aligned}
\tag{7.15}
\]

Elementary integration yields

\[
\boxed{
I_B=
\frac{6a^3-2a^3b-3a^2b-b}{3a^3(a-b)},
}
\tag{7.16}
\]

\[
\boxed{
I_E=
\frac{6a-b^3-3b-2}{3a(a-b)}.
}
\tag{7.17}
\]

Substituting (7.10), (7.16), and (7.17) into (7.3),

\[
\boxed{
J:=|(K-K)^\circ|
=
\frac{12a^3-4a^3b+a^2b^3-6a^2b-4a^2+b}
{3a^3(a-b)}.
}
\tag{7.18}
\]

### 7.4 The primal volume

The general prismoid formula is

\[
|K|=\frac{|T|+V(T,C)+|C|}{3},
\tag{7.19}
\]

where `V(T,C)` is planar mixed area in the convention

\[
|T+tC|=|T|+2tV(T,C)+t^2|C|.
\]

Here

\[
|T|=\frac12,
\qquad |C|=\frac{ab}{2}.
\tag{7.20}
\]

For `T=conv{0,e_1,e_2}`, the edge-normal support formula gives

\[
2V(T,C)
=h_C(0,-1)+h_C(1,1)+h_C(-1,0).
\tag{7.21}
\]

The first and third terms vanish, while `h_C(1,1)=max(a,b)=a` in the present chamber. Hence

\[
V(T,C)=\frac a2
\]

and therefore

\[
\boxed{|K|=\frac{1+a+ab}{6}.}
\tag{7.22}
\]

### 7.5 B13: a monotone cleared defect

Combining (7.18) and (7.22), direct algebra gives

\[
|K|J-\frac23
=
\frac{D(a,b)}{18a^3(a-b)},
\tag{7.23}
\]

where

\[
\begin{aligned}
D(a,b)={}&-4a^4b^2+8a^4b
+a^3b^4+a^3b^3-6a^3b^2-2a^3b+8a^3\\
&+a^2b^3-6a^2b-4a^2
+ab^2+ab+b.
\end{aligned}
\tag{7.24}
\]

The denominator in (7.23) is positive for `a>b>0`. Introduce the crossing distances

\[
X:=a-1\ge0,
\qquad
Y:=1-b\in[0,1).
\tag{7.25}
\]

Then the numerator becomes

\[
D(1+X,1-Y)
=c_4(Y)X^4+c_3(Y)X^3+c_2(Y)X^2+c_1(Y)X+c_0(Y),
\tag{7.26}
\]

with

\[
c_4(Y)=4(1-Y^2),
\tag{7.27}
\]

\[
c_3(Y)=Y^4-5Y^3-13Y^2+7Y+18,
\tag{7.28}
\]

\[
c_2(Y)=3Y^4-16Y^3-12Y^2+24Y+21,
\tag{7.29}
\]

\[
c_1(Y)=3Y^4-17Y^3+24Y+6,
\tag{7.30}
\]

\[
c_0(Y)=Y(Y^3-6Y^2+3Y+6).
\tag{7.31}
\]

Every coefficient is nonnegative on `0<=Y<=1`. The verification is elementary and is the actual sign proof:

\[
c_4(Y)\ge0,
\tag{7.32}
\]

and, using `Y^3<=Y^2`,

\[
c_3(Y)
\ge18+7Y-18Y^2
\ge\min\{18,7\}=7,
\tag{7.33}
\]

because the displayed quadratic is concave. Similarly

\[
c_2(Y)
\ge21+24Y-28Y^2
\ge\min\{21,17\}=17.
\tag{7.34}
\]

Using `Y^3<=Y`,

\[
c_1(Y)
\ge6+7Y
\ge6.
\tag{7.35}
\]

Finally, since `Y^2<=Y`,

\[
c_0(Y)
\ge Y(6-3Y)
\ge0.
\tag{7.36}
\]

Hence

\[
D(a,b)\ge0
\]

throughout the crossing chamber, proving (6.1). In fact if `(X,Y)\ne(0,0)`, then either `c_0(Y)>0` when `Y>0`, or a positive coefficient multiplies a positive power of `X`; thus `D>0`. This proves strictness whenever `a>b`.

The point `a=b=1` is a triangular prism and is already in the comparable-difference-body class; in particular its product is not an equality case for the source bound.

This completes the proof. `QED`.

## 8. B27: the quantifier swap actually closes the entire chamber

The refutation-first temptation would be to sample many crossing ratios `(a,b)` and search for a bad one. Instead the argument above fixes an arbitrary contraction `0<b<=1` and proves the cleared defect nonnegative for **every** expansion `a>=1`; then `b` is arbitrary as well. Thus the conclusion is

\[
\forall b\in(0,1]\ \forall a\in[1,\infty):
\quad |K_{a,b}|\,|(K_{a,b}-K_{a,b})^\circ|\ge\frac23,
\]

not a numerical statement.

For the opposite crossing orientation `b>=1>=a`, interchange the coordinate axes. For `a,b<=1`, one has `C-C\subset T-T`; for `a,b>=1`, one has `T-T\subset C-C` (equivalently apply the first inclusion to the inverse diagonal map and swap the bases). Hence the previous nested-difference-body theorem plus the present crossing theorem proves the corollary for every `a,b>0` in (6.2).

## 9. What genuinely changed and what did not

The source metric did **not** move:

`d_Makai: 2 -> 2`.

The restricted frontier did move from

`all crossing/non-nested triangular-prismoids`

to

`crossing triangular-prismoids whose relative triangle map has genuine shear/misalignment (no common pair of incident edge directions)`.

In a normalization with lower base `T`, the next simplest unresolved finite-parameter family can be taken as

\[
C=\operatorname{conv}\{0,(a,0),(s,b)\}
\]

with `s\ne0` in a chamber where `C-C` and `T-T` cross. The new diagonal theorem is the `s=0` face of that family. This is a changed mathematical obligation, not a re-check of the preceding nested theorem.

## 10. Exact symbolic self-check — secondary to the proof

Only after the route note and proof algebra were developed, I created

`artifacts/hard7_2026-09-18/HARD7-01/2026-09-20T1508Z__makai_crossing_edge_aligned_check.py`

at commit

`f8780cdcf038a9184b3b27ac4217b34cf7c0dcde`.

The script was executed with exact SymPy symbolic/rational arithmetic. Its archived output is

`artifacts/hard7_2026-09-18/HARD7-01/2026-09-20T1508Z__makai_crossing_edge_aligned_check.out`

at commit

`823d35da8aae388915de715954ce0a917b5274e1`.

The checker independently integrates the exact cells (7.14)--(7.15), verifies (7.10), (7.16)--(7.18), verifies the defect identity (7.23)--(7.31), and evaluates five exact rational spot checks. The spot checks are explicitly **not** an exhaustive certificate for the continuum. The all-parameter theorem rests on the written cell decomposition and coefficient sign proof. The archived output ends

`ALL_EXACT_CHECKS_PASS = True`.

Both checker and output were read back from their creation commits.

## 11. Section-B outcomes

### B8 — GO THE OTHER WAY AND DISCRETIZE: SUCCESS

The continuum polar intersection was converted to three exact roof pieces plus two support-function switch lines. This produced closed rational formulas over the entire crossing chamber, not a sampled mesh.

### B13 — FIND WHAT ONLY INCREASES: SUCCESS

After `X=a-1`, `Y=1-b`, the cleared defect is a polynomial in `X` with nonnegative coefficient functions of `Y`. Thus moving farther in the expansion direction cannot make the cleared defect negative within this chamber.

### B27 — SWAP THE QUANTIFIERS: SUCCESS

Instead of finding a favorable `a` for each `b`, the coefficient proof establishes the inequality uniformly for every `a>=1` and every `0<b<=1` at once.

The next run must use a different triple. A natural genuinely new triple for the one-shear family is **B14 / B20 / B29**: quotient the finite triangle relabeling symmetry, identify exactly where the diagonal cell compiler changes when shear is introduced, and include the cell-boundary/infinite-shear limits rather than losing them to case splits.

## 12. Closure status and next obligation

This is **PARTIAL**, not `PROVED` for the source. No audit is requested or counted by this worker, and no paper folder is created. Closure of Makai's source conjecture would still require an argument for arbitrary three-dimensional convex bodies, exact finite certification where a finite core is used, a dedicated prior-art review, and two independent OTHER-track audits under the fleet protocol.

The next concrete obligation is the shear/misalignment extension of the triangular-prismoid formula, beginning with `C=conv{0,(a,0),(s,b)}`. If that route ceases to change the remaining obligation through the Section-I limit, this hard target must be handed off/rotated according to the controlling policy rather than producing receipt-only lemmas.

## 13. Immutable ledger delta

```text
track: HARD7-01
source_target: MAKAI-POLAR-DIFFERENCE-BODY
owner: HARD7-01
status: PARTIAL / SOURCE OPEN / CLAIMED / RECOVERY1
source_metric: d_Makai
before: 2
after: 2
movement: NO MOVEMENT
methods: B8 / B13 / B27
new_theorem_claim: Makai 2/3 bound for the full two-edge-aligned crossing triangular-prismoid chamber
normalized_crossing_family: T=conv(0,e1,e2), C=conv(0,a e1,b e2), a>=1>=b>0
exact_dual_formula: J=(12a^3-4a^3b+a^2b^3-6a^2b-4a^2+b)/(3a^3(a-b))
exact_primal_formula: |K|=(1+a+ab)/6
proof_mechanism: exact polar fan decomposition + nonnegative cleared-defect coefficients after a=1+X,b=1-Y
restricted_frontier_before: crossing/non-nested triangular prismoids
restricted_frontier_after: crossing triangular prismoids with genuine shear/misalignment
checker_commit: f8780cdcf038a9184b3b27ac4217b34cf7c0dcde
output_commit: 823d35da8aae388915de715954ce0a917b5274e1
output_terminal: ALL_EXACT_CHECKS_PASS = True
next_methods: B14 / B20 / B29
closure: NO
```
