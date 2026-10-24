Model: GPT-5.6 Sol. Reasoning level: UNVERIFIED; GPT-6 / maximum was requested, but this runtime/scheduler exposes no model selector or reasoning-effort selector, so I do not claim otherwise. **movement — fallback metric UNMEASURED -> 2; Section-B moves tried: 18, 19, 20.**
Problem/source: Chiara Meroni (2026), Randomstrasse 101, *Directional Convexity (problems 34 and 35)*, Conjecture 34 — C29's source-guided fallback is **CLAIMED / PENDING_ADMISSION, not READY**; the originally proposed Burdzy–Scheutzow Problem 7.8 / I0077 remains excluded from C29 by R07's prior exclusive claim.

# C29 — exact functional hull of the four-point irrational-parallelogram lift

Repository / branch: `yspennstate/math-open-problems` / `master`.
Own root: `proofnet24/C29-closure-brownian-shapes`.
Old C29 MUB root preserved unchanged in HARD RESERVE: `proofnet24/C29-mub-six`.
Run date: 2026-09-16.
Delivery: private GitHub only. No email/Gmail, Drive, public posting, paid compute, access changes, or new schedules.

## 1. Continuity and ownership before mathematics

I continued from the immutable C29 transition report

`proofnet24/C29-closure-brownian-shapes/runs/2026-09-16/2026-09-16T16-46-28Z__i0077-exclusion-dc34-fallback.md`

rather than restarting either the Brownian or MUB work.

The proposed Brownian target remains unavailable to C29: `operations/claims/I0077.md` gives Burdzy--Scheutzow Problem 7.8 exclusively to R07, status `PENDING_ADMISSION`, not READY. I did not create a duplicate Brownian claim and did not reopen already-answered Problem 7.5.

C29's create-only fallback reservation remains `operations/claims/RS-2026-DC34.md`. It gives C29 the provisional CLOSABLE OUTSIDE claim on Randomstrasse Conjecture 34 and freezes the metric as:

> for one fixed lifted irrational-parallelogram candidate and the source three-plane cone, the largest integer `N` for which `N` pairwise distinct affine boundary planes/patches of the **same functional D-convex hull** are rigorously certified.

Here and below, to avoid the vacuous operation of subdividing one plane into arbitrarily many subsets, a counted affine patch means a maximal two-dimensional relatively open boundary piece lying in one affine plane, and distinct patches counted for the metric lie in distinct affine planes. This is the convention relevant to Meroni--Raita's stated concern about infinitely many boundary planes.

The previous value was **UNMEASURED**. This run computes the entire functional hull of the fixed candidate and proves that it has exactly two such affine boundary pieces, so the frozen metric moves to

\[
\boxed{N=2.}
\]

This is a restricted theorem and a route exclusion for the source-guided four-point mechanism. It does **not** prove or refute Randomstrasse Conjecture 34.

The old unrestricted six-dimensional MUB attack remains in HARD RESERVE without edits. Its full-domain residual lower bound is still `0`; `11/756` remains only an upper benchmark from an exact phase example, not a positive lower bound and not a nonexistence proof. All restricted positive bounds, exact phase examples, atlas-gauge facts and failed routes remain preserved under `proofnet24/C29-mub-six`.

## 2. Source and current-status check — 16 September 2026

I reread the live Randomstrasse page rather than relying on the queue paraphrase. It defines

\[
K^{(i+1,D)}=
\{\lambda a+(1-\lambda)b:
 a,b\in K^{(i,D)},\ a-b\in D,\ 0\le\lambda\le1\},
\]

with `K^(0,D)=K`, and defines the functional hull by all `D`-convex functions. It states

\[
K^{(\infty,D)}\subseteq \operatorname{conv}_D(K)
\subseteq \operatorname{conv}(K).
\tag{2.1}
\]

Conjecture 34 is still displayed as the assertion that the `D`-convex hull of a finite point set need not be semialgebraic, with the concrete suggested regime of three distinct planes in `R^3` sharing a line.

I also reread Meroni--Raita, arXiv:2509.07541v2, last revised 4 August 2026, especially Section 5. Their Example 5.3 takes an irrational parallelogram with acute angle `pi/3` and the three planar directions

\[
D_2=\{y(y-\tan(\pi/3)x)(y+\tan(\pi/3)x)=0\}.
\tag{2.2}
\]

They prove that no finite compatible triangulation exists. Their Remark 5.4 says the infinite compatible grid would suggest infinitely many boundary planes after passing to `D=D_2 x R`, but explicitly records the missing point: planes from different refinement stages might coincide. Their Question 2 asks whether a vertical perturbation of the four lifted points can make the resulting functional `D`-convex hull non-semialgebraic.

A bounded current search on 16 September 2026 used the exact arXiv number/title, `Question 2`, `Example 5.3`, `vertical perturbations`, `Directional Convexity`, `Conjecture 34`, and later-author/citation terms. I found the live Randomstrasse statement and arXiv v2, but no later primary source resolving this exact question. That is dated bounded evidence, **not** a proof of worldwide openness or novelty.

## 3. Coordinate model inherited from the previous C29 report

Let the source parallelogram have side vectors `U,V` in two of the three allowed directions. Relabel the two side directions if necessary so that

\[
\alpha:=a/b>1.
\tag{3.1}
\]

The source assumption `a/b notin Q` implies in particular `alpha != 1`. Write a projected point as

\[
p(s,t)=sU+tV,\qquad 0\le s,t\le1.
\]

In these normalized side coordinates, the third allowed planar direction is proportional to

\[
(1,-\alpha).
\tag{3.2}
\]

Indeed, in physical coordinates the three direction lines make angles `0,+pi/3,-pi/3`; expressing the unused line through side vectors of lengths `a,b` gives coefficient ratio `-a/b=-alpha`.

The three-dimensional cone is

\[
D=D_2\times\mathbb R,
\]

i.e. the union of the three vertical planes over the planar allowed directions. Thus a line is a permitted lamination line precisely when its planar projection is parallel to one of

\[
e_s=(1,0),\qquad e_t=(0,1),\qquad d=(1,-\alpha),
\tag{3.3}
\]

(or is purely vertical).

### 3.1 All noncoplanar vertical lifts are equivalent

For completeness I restate the normalization proved in the preceding report, because it is essential for the source Question 2 consequence.

Give the four projected corners arbitrary heights

\[
h_{00},h_{10},h_{01},h_{11}
\]

and set

\[
\delta=h_{11}-h_{10}-h_{01}+h_{00}.
\tag{3.4}
\]

Let `L(s,t)` be the unique affine function taking the first three values at `(0,0),(1,0),(0,1)`. The shear

\[
T(s,t,z)=(s,t,z-L(s,t))
\tag{3.5}
\]

preserves each of the three vertical allowed planes: a vector `(v,r)` in the vertical plane over a planar allowed direction `v` is sent to `(v,r-DL(v))`, which is in the same plane. Hence `T(D)=D`. Composition with an invertible `D`-preserving affine map preserves `D`-convexity, the functional hull, and semialgebraicity.

The shear (3.5) sends the four heights to

\[
(0,0,0,\delta).
\]

If `delta=0`, all four points are coplanar. Both `z` and `-z` are `D`-convex, so the functional hull lies in that plane, and its projection is the whole planar parallelogram; the hull is therefore a planar semialgebraic parallelogram.

If `delta != 0`, the additional invertible vertical scaling `z -> z/delta` also preserves `D` and sends the lift to the single canonical noncoplanar configuration

\[
K=\{(0,0,0),(1,0,0),(0,1,0),(1,1,1)\}.
\tag{3.6}
\]

Consequently **every noncoplanar vertical lift of the fixed projected parallelogram has the same hull geometry up to a `D`-preserving affine equivalence**. There is no generic many-height parameter left after the correct gauge reduction.

## 4. Moves 18, 19 and 20: the new way in

The previous run used moves `2,6,23`, so I did not repeat them.

### B18 — say it in another language

Instead of following the infinite compatible planar grid, I rewrote the problem as a one-dimensional convexification problem on the fibers of the third direction. The invariant fiber coordinate is

\[
r=t+\alpha s.
\tag{4.1}
\]

On such a fiber, the upper surface generated from the four corners is a concave quadratic. This turns the apparently infinite grid refinement into an elementary chord-filling problem.

### B19 — make it an algorithm

The translation gives a finite constructive algorithm: one lamination round builds the two side edges, a second builds the whole quadratic upper graph, and a third fills every third-direction fiber down to its endpoint chord. The proof below shows this **already equals the functional hull**.

### B20 — find why the algorithm fails

The source-guided infinite-grid mechanism fails for this four-point lift because all later third-direction refinements collapse onto the same endpoint-chord envelope. There is no infinite sequence of new supporting planes: the construction stabilizes after three lamination rounds. This is a structural failure of the proposed mechanism, not a numerical accident.

## 5. Main theorem: exact canonical hull

Define on the square `[0,1]^2`

\[
g(s,t)=st,
\tag{5.1}
\]

\[
q(s,t)=st-\alpha^{-1}t(1-t)
       =\frac{t(t+\alpha s-1)}{\alpha},
\tag{5.2}
\]

and

\[
\ell(s,t)=s+t-1,
\qquad
h(s,t)=\max\{0,q(s,t),\ell(s,t)\}.
\tag{5.3}
\]

Let

\[
R_\alpha=
\{(s,t,z):0\le s,t\le1,\ h(s,t)\le z\le g(s,t)\}.
\tag{5.4}
\]

### Theorem C29-DC34-EXACT-HULL-03

For every `alpha>1` and the cone (3.3), the canonical four-point lift (3.6) satisfies

\[
\boxed{
K^{(3,D)}=K^{(\infty,D)}=\operatorname{conv}_D(K)=R_\alpha.
}
\tag{5.5}
\]

In particular the functional `D`-convex hull is semialgebraic and the lamination construction stabilizes after three rounds.

### Proof, part I: two global `D`-convex separators

The Hessian of `g=st` is

\[
\nabla^2g=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]

Its second directional derivatives along the three projected allowed directions are

\[
D^2_{e_s}g=0,
\qquad
D^2_{e_t}g=0,
\qquad
D^2_d g=-2\alpha<0.
\tag{5.6}
\]

Therefore

\[
F_+(s,t,z)=z-g(s,t)
\tag{5.7}
\]

is `D`-convex in three dimensions: the `z` term is affine and `-g` is convex on every allowed projected line. At all four points of `K`, `F_+=0`. The defining inequality for the functional hull gives

\[
z\le g(s,t)
\tag{5.8}
\]

for every hull point.

Next compute for `q`:

\[
D^2_{e_s}q=0,
\qquad
D^2_{e_t}q=2/\alpha>0,
\qquad
D^2_dq=0.
\tag{5.9}
\]

Thus `q` is `D_2`-convex. The functions `0` and `ell` are affine, hence `D_2`-convex. A pointwise maximum of finitely many convex functions remains convex on every line, so `h` is `D_2`-convex. Consequently

\[
F_-(s,t,z)=h(s,t)-z
\tag{5.10}
\]

is `D`-convex. Again `F_-=0` on all four points of `K`: at the first three corners `h=g=0`, and at `(1,1)`, `h=g=1`. Hence every functional-hull point satisfies

\[
z\ge h(s,t).
\tag{5.11}
\]

All affine functions are `D`-convex, so the general inclusion (2.1) also confines the projected coordinates to the ordinary convex hull `[0,1]^2`. Equations (5.8) and (5.11) therefore prove

\[
\operatorname{conv}_D(K)\subseteq R_\alpha.
\tag{5.12}
\]

### Proof, part II: two lamination rounds produce the whole upper graph

In the first lamination round, the permitted `t`-direction segments on the left and right sides give

\[
(0,t,0),\qquad (1,t,t),\qquad 0\le t\le1,
\tag{5.13}
\]

inside `K^(1,D)`. Indeed their endpoint differences lie in the vertical plane over `e_t`.

For each fixed `t`, join these two points in the vertical plane over `e_s`. At parameter `s`, this gives

\[
(s,t,st).
\tag{5.14}
\]

Hence the full upper graph

\[
\Gamma_g=\{(s,t,g(s,t)):0\le s,t\le1\}
\tag{5.15}
\]

lies in `K^(2,D)`.

### Proof, part III: a one-dimensional chord lemma fills each third-direction fiber

Fix

\[
r=t+\alpha s\in[0,\alpha+1].
\]

The corresponding third-direction line meets the unit square in the interval

\[
A_r\le s\le B_r,
\qquad
A_r=\max\left(0,\frac{r-1}{\alpha}\right),
\qquad
B_r=\min\left(1,\frac r\alpha\right),
\tag{5.16}
\]

with `t=r-alpha s`. Along this line the upper graph is

\[
\phi_r(s)=g(s,r-\alpha s)=s(r-\alpha s),
\qquad
\phi_r''(s)=-2\alpha<0.
\tag{5.17}
\]

So `phi_r` is concave.

We use the following elementary chord fact.

**Chord lemma.** Let `phi` be concave on `[A,B]`, and let `L` be the affine chord through `(A,phi(A))` and `(B,phi(B))`. For every `x in [A,B]` and every `y` with

\[
L(x)\le y\le\phi(x),
\tag{5.18}
\]

there exist `u<=x<=v` in `[A,B]` such that `(x,y)` lies on the chord between `(u,phi(u))` and `(v,phi(v))`.

**Proof of the chord lemma.** If `x=A` or `x=B` there is nothing to prove. Otherwise fix the left endpoint `u=A` and let `v` vary continuously from `x` to `B`. The value at abscissa `x` of the chord from `(A,phi(A))` to `(v,phi(v))` depends continuously on `v`; at `v=x` it equals `phi(x)`, while at `v=B` it equals `L(x)`. The intermediate-value theorem supplies every value between them. Concavity guarantees `L(x)<=phi(x)`. QED.

Both endpoints used in the chord lemma lie on `Gamma_g subset K^(2,D)`, and their base difference is in the third allowed direction. Therefore every point vertically between `phi_r` and the endpoint chord belongs to `K^(3,D)`.

It remains only to compute that endpoint chord.

### Proof, part IV: the endpoint chord is exactly `h`

There are three regimes.

**Regime 1: `0<=r<=1`.** Here

\[
A_r=0,\qquad B_r=r/\alpha.
\]

Both endpoint heights are zero, so the endpoint chord is

\[
L_r=0.
\tag{5.19}
\]

**Regime 2: `1<=r<=alpha`.** Here

\[
A_r=(r-1)/\alpha,\qquad B_r=r/\alpha,
\]

and the corresponding endpoint `t`-coordinates are `1` and `0`. The function `q` in (5.2) is affine along the third direction by (5.9), and on the fiber it has the form

\[
q=\frac{t(r-1)}\alpha.
\tag{5.20}
\]

At the two endpoints this equals the respective `g` heights. Therefore

\[
L_r=q.
\tag{5.21}
\]

**Regime 3: `alpha<=r<=alpha+1`.** Here

\[
A_r=(r-1)/\alpha,\qquad B_r=1.
\]

The affine function `ell=s+t-1` agrees with `g` at both endpoints, so

\[
L_r=\ell.
\tag{5.22}
\]

Now compare these three expressions with `h`.

If `r<=1`, then

\[
q=\frac{t(r-1)}\alpha\le0,
\qquad
\ell=s+t-1\le r-1\le0,
\]

where `r-(s+t)=(alpha-1)s>=0`. Hence `h=0`.

If `1<=r<=alpha`, then `q>=0`, and

\[
q-\ell
=\frac{(t-1)(r-\alpha)}\alpha\ge0,
\tag{5.23}
\]

because both factors in the numerator are nonpositive. Hence `h=q`.

If `r>=alpha`, then

\[
t\ge\alpha(1-s)
\]

and therefore

\[
\ell=s+t-1\ge(\alpha-1)(1-s)\ge0.
\tag{5.24}
\]

Equation (5.23) now has one nonpositive and one nonnegative factor, so `q<=ell`; hence `h=ell`.

Thus in all cases

\[
L_r=h.
\tag{5.25}
\]

The preceding C29 report also had the second quadratic separator

\[
q_1=st-\alpha s(1-s).
\]

There is no contradiction: in fiber coordinates

\[
q_1=s(r-\alpha).
\tag{5.26}
\]

so `q_1<=0` for `r<=alpha`; while for `r>=alpha`,

\[
q_1-\ell=(s-1)(r-1)\le0.
\tag{5.27}
\]

Therefore `q_1` is everywhere dominated by `max{0,ell}` when it could matter, and

\[
\max\{q_0,q_1,q_2\}=\max\{0,\ell,q\}=h.
\tag{5.28}
\]

Combining the chord lemma with (5.25), every point of `R_alpha` belongs to `K^(3,D)`. Hence

\[
R_\alpha\subseteq K^{(3,D)}
\subseteq K^{(\infty,D)}
\subseteq\operatorname{conv}_D(K).
\tag{5.29}
\]

Together with (5.12), all inclusions are equalities, proving (5.5). QED.

## 6. Semialgebraicity and exact affine-patch count

The theorem gives the finite description

\[
0\le s,t\le1,
\qquad
z\le st,
\qquad
z\ge0,
\qquad
z\ge s+t-1,
\qquad
\alpha z\ge\alpha st-t(1-t).
\tag{6.1}
\]

Since `alpha>0` is a fixed real parameter, these are finitely many polynomial inequalities. Thus `R_alpha` is semialgebraic.

The two-dimensional upper boundary is `z=g=st`. Its Hessian determinant is

\[
\det\nabla^2g=-1,
\tag{6.2}
\]

so it contains no nonempty open two-dimensional affine patch.

The lower boundary has three open regimes:

\[
h=
\begin{cases}
0,&r<1,\\
q,&1<r<\alpha,\\
s+t-1,&r>\alpha.
\end{cases}
\tag{6.3}
\]

The middle quadratic has

\[
\nabla^2q=\begin{pmatrix}0&1\\1&2/\alpha\end{pmatrix},
\qquad
\det\nabla^2q=-1,
\tag{6.4}
\]

so it too has no nonempty open two-dimensional affine patch. The seams `r=1` and `r=alpha` are only one-dimensional. On each side of the base square the upper and lower heights agree, so there is no additional two-dimensional vertical side face.

Therefore the hull has exactly two maximal two-dimensional affine planar boundary pieces:

\[
\boxed{
\begin{aligned}
&z=0 &&\text{over }r<1,\\
&z=s+t-1 &&\text{over }r>\alpha.
\end{aligned}}
\tag{6.5}
\]

They lie in distinct affine planes. Under the frozen metric, this proves

\[
\boxed{N=2.}
\tag{6.6}
\]

## 7. Consequence for Meroni--Raita Question 2

The normalization in Section 3 plus Theorem (5.5) gives a stronger restricted conclusion than the metric alone.

### Corollary C29-DC34-VERTICAL-LIFT-04

For the four projected vertices of Meroni--Raita Example 5.3 and `D=D_2 x R`, **every choice of four vertical heights has a semialgebraic functional `D`-convex hull**.

**Proof.** If `delta=0`, Section 3.1 reduces the hull by a `D`-preserving affine shear to the planar parallelogram, which is semialgebraic. If `delta!=0`, the shear and vertical scaling reduce it to the canonical set `K`, whose hull is the semialgebraic set (6.1). Invertible affine maps preserve semialgebraicity. QED.

Thus the specific vertical-perturbation proposal in Meroni--Raita Question 2 has a **negative answer**: no small or large vertical perturbation of those same four projected vertices can produce a non-semialgebraic functional hull.

Scope is crucial. This does **not** refute Randomstrasse Conjecture 34. Conjecture 34 permits other finite configurations, other projected point sets, and potentially mechanisms not reducible to this four-point fiber geometry. C29 remains **PARTIAL / PENDING_ADMISSION** for Conjecture 34.

## 8. Exact symbolic self-check

I wrote the mathematics first. Only after the exact formula (5.5) was obtained did I add a symbolic self-check:

`proofnet24/C29-closure-brownian-shapes/artifacts/2026-09-16T17-35Z__check_dc34_exact_hull.py`

with archived executed output

`proofnet24/C29-closure-brownian-shapes/artifacts/2026-09-16T17-35Z__check_dc34_exact_hull.out`.

The checker uses exact SymPy algebra only. It verifies:

- the three directional second derivatives of `g` and `q`;
- the fiber form `q=t(alpha*s+t-1)/alpha`;
- the exact factorization `q-ell=(t-1)(alpha*s-alpha+t)/alpha`;
- the middle- and upper-regime endpoint identities;
- the Hessian determinants `det Hess(g)=det Hess(q)=-1`.

The archived output terminates

`ALL_EXACT_CHECKS_PASS`.

This is explicitly a **self-check**. The written proof in Sections 5--7 carries the theorem.

## 9. Directed second-audit duty: newest C30 claim

C29's directed audit duty is C30. I did not repeat the already-completed order-nine enumeration audit. The newest durable C30 mathematical report at run time is

`proofnet24/C30-sidorenko/runs/2026-09-16/2026-09-16T17-14-40Z__report.md`

at commit `def46ff300f5dbd56038817b2a2cb9db345dc01e`. Its new structural claim is `C30-REGULAR-MOMENT-TRANSFER-01`.

I independently rederived the finite moment/transfer part as follows.

For a finite uniform symmetric nonnegative normalized kernel `A`, define

\[
C_{ijk}=\frac1n\sum_u A_{ui}A_{uj}A_{uk}.
\tag{9.1}
\]

C30's transfer matrix on ordered-pair states is

\[
T_{(i,j),(j,k)}=\frac{C_{ijk}}n,
\tag{9.2}
\]

and zero if the first coordinate of the target state is not `j`. Let

\[
R(i,j)=(j,i),\qquad S=RT.
\tag{9.3}
\]

Then

\[
S_{(i,j),(p,q)}=0\quad\text{unless }p=i,
\]

so `S` is block diagonal by the first coordinate. In block `i`,

\[
S_i(j,q)=\frac{C_{ijq}}n
=\frac1{n^2}\sum_u A_{ui}A_{uj}A_{uq}.
\tag{9.4}
\]

For every real vector `v`,

\[
v^\top S_i v
=\frac1{n^2}\sum_u A_{ui}
 \left(\sum_j A_{uj}v_j\right)^2\ge0,
\tag{9.5}
\]

because `A` is nonnegative. Therefore every block and hence `S` itself is positive semidefinite. Since `R^2=I`,

\[
T=RS.
\tag{9.6}
\]

Finally, expanding the trace around a length-five closed walk of pair states gives

\[
\operatorname{Tr}(T^5)
=\frac1{n^5}\sum_{i_0,\ldots,i_4}
\prod_{j\in\mathbb Z/5\mathbb Z}
 C_{i_j,i_{j+1},i_{j+2}},
\tag{9.7}
\]

which is exactly the uniform finite version of the five-variable common-neighbor contraction obtained by integrating the five degree-three vertices of `H=K_{5,5}\setminus C_{10}`. Thus

\[
t_H(A)=\operatorname{Tr}(T^5)
=\operatorname{Tr}((RS)^5),
\qquad S\succeq0.
\tag{9.8}
\]

The regular-kernel rescaling used immediately before this is also normalized correctly: if a `d`-regular graphon is `W=dA`, then `e(H)=15` gives `t_H(W)=d^{15}t_H(A)` and `t(K_2,W)=d`, so the Sidorenko inequality on the regular slice becomes `t_H(A)>=1`.

I treat C30's cited Coregliano--Razborov regular-graphon reduction as an external dependency, not as something this audit newly proves. I also do not infer Zhao's universal conjugacy-average comparison, the full Sidorenko conjecture for this `H`, or any order-eleven finite coverage.

### Audit verdict

\[
\boxed{
\texttt{C29-AUDIT-C30-REGULAR-MOMENT-TRANSFER-01 = PASS (claim-scoped)}.
}
\tag{9.9}
\]

Scope: the algebraic common-neighbor contraction, transfer representation, reversal factorization, PSD block structure, and normalization. It is not a full-source closure audit.

## 10. Model / scheduler escalation status

The requested configuration remains unavailable in the exposed scheduler API. The actual runtime identifies as GPT-5.6 Sol; no separate reasoning-effort metadata is exposed, hence `UNVERIFIED`. The scheduler update surface available to this worker has fields for title, prompt, schedule, timing mode and enablement, but **no model-family field and no reasoning-effort field**. Therefore GPT-6 / maximum remains a prompt request only.

To make it enforceable rather than requested, the product/backend or an authorized higher-level task configuration must expose and persist model and reasoning selectors. This worker cannot manufacture such fields.

The fleet policy also records native modification probes for P26, P01 and P03 returning `You cannot modify this task`. That is an ownership/permission boundary. The permitted workaround is modification from the task's owning account/workspace by an authorized owner/admin, or platform support if the authorized owner still lacks the control. A repository edit is not a scheduler repair; I did not bypass the denial and did not create a duplicate schedule.

## 11. What changed conceptually

The source mechanism suggested that an irrational compatible planar grid might force infinitely many distinct boundary planes after vertical perturbation. For the exact four-point Example 5.3 projection, the opposite happens: after the correct affine gauge reduction, the entire three-dimensional functional hull is generated by three lamination rounds and has only two affine two-dimensional boundary planes.

This is not merely a failure to find the infinite planes. It identifies **why** they collapse: on each third-direction fiber the upper graph is one concave quadratic, so all permitted third-direction chords fill exactly the strip down to one endpoint chord. The endpoint chord has only three formulas (`0`, `q`, `ell`), and only two are affine on open two-dimensional regions.

The natural next research question is therefore no longer whether the four-point vertical perturbation produces infinitely many planes; it does not. A genuine route toward Conjecture 34 must break this one-dimensional fiber stabilization, for example by using more projected points or a configuration in which the relevant fiber envelopes acquire infinitely many distinct active endpoint pairs.

## 12. `ledger_delta` for P26 only

C29 does not edit `RESULTS.md`, `POSTED.md`, `QUEUE.md`, or peer-track files. Requested reconciliation:

```yaml
ledger_delta:
  track: C29
  allocation: CLOSABLE OUTSIDE
  source: Chiara Meroni (2026), Randomstrasse Conjecture 34
  claim: RS-2026-DC34
  admission: PENDING_ADMISSION
  status: PARTIAL
  metric_name: maximal distinct affine boundary planes/patches certified for the single frozen four-point source candidate
  metric_before: UNMEASURED
  metric_after: 2
  new_claim: C29-DC34-EXACT-HULL-03
  new_claim_scope: exact functional and lamination hull of the canonical noncoplanar four-point Example-5.3 lift; hull stabilizes at K^(3,D) and is semialgebraic
  source_adjacent_corollary: C29-DC34-VERTICAL-LIFT-04; every vertical lift of the four Example-5.3 projected vertices has semialgebraic functional D-convex hull, giving a negative answer to Meroni-Raita Question 2 for that four-point mechanism
  source_conjecture_34: OPEN in bounded current search; not resolved by this restricted theorem
  old_mub: HARD RESERVE unchanged; full-domain lower-bound metric remains 0; 11/756 remains an upper benchmark only
  i0077: excluded from C29 by R07 exclusive claim; not reopened
  directed_audit: C29-AUDIT-C30-REGULAR-MOMENT-TRANSFER-01 = PASS (claim-scoped)
  next_methods: choose three methods different from 18,19,20; seek a configuration that breaks finite fiber stabilization rather than refining the same four-point grid
```

No closure, READY certification, public posting, or extra audit is claimed.
