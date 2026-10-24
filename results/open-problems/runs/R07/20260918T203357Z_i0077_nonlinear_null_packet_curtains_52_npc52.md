Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. METRIC MOVEMENT: `51 -> 52` genuinely distinct nonparabolic shape families; methods actually used: #3 PROVE SOMETHING STRONGER, #21 ASK WHO ELSE HAS THIS SHAPE, #27 SWAP THE QUANTIFIERS.**

# R07 CLOSABLE OUTSIDE — nonlinear null-packet curtains via simultaneous phase control

Run date: 2026-09-18 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Source: Krzysztof Burdzy and Michael Scheutzow, *Forward Brownian Motion*, Probab. Theory Relat. Fields 160 (2014), 95–126; arXiv:1302.6958, Problem 7.8 / intake I0077.  
Overall source status after this run: **PARTIAL**.

The fixed metric remains the number of genuinely distinct nonparabolic space-time shape families for which R07 has a complete source-appropriate theorem, under the frozen convention that Brownian rescaling/reflection/constant translation and mere parameter changes inside one structural family do not create new metric points.

The immediately preceding authoritative own report is

`runs/R07/20260918T1925Z_i0077_ballistic_null_packet_curtains_51_bn51.md`,

which moved `50 -> 51` and used moves `#2,#18,#25`. The present triple is different. All thirty Section-B move labels have already appeared somewhere in the long I0077 chain, so there is no honest way to choose three labels globally unused on this problem; I preserve that history rather than inventing one.

## 1. Required continuity, admission, ownership, and repository read

Before new mathematics I reread or exact-target-recovered:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/NEW_METHODS_2026-09-16.md` and the controlling `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- canonical reservation `operations/claims/I0077.md`;
- the newest R07 report, its theorem/equivalence chain, and searchable earlier I0077 reports most likely to collide with the new family (runs 31, 43–51, plus the searchable full chain);
- the newest neighboring R15 report and its controlling I0076 handoff state;
- targeted intake/attempt searches for `I0077`, `1302.6958`, `Problem 7.8`, the exact source wording, nonlinear/moving/null-packet variants, and duplicate ownership.

`INDEX.md`/`RANKING.md` settle Burdzy–Scheutzow Problem 7.5, not Problem 7.8. `POSTED.md` does not list Problem 7.8 as settled or posted. `QUEUE.md` still lists I0077 separately. The canonical claim still literally says `PENDING_ADMISSION, not READY`, with R07 as exclusive provisional owner; I preserve that shared status while following the owner's explicit R07 assignment. R15's distinct Problem 7.2 / I0076 remains `OPEN / PARTIAL / RETIRED-HANDOFF` at its historical carried `2/4` and is not reopened. The old R07 KPZ/FPP line remains preserved by its immutable handoff and is not deleted or resumed.

The large `probability_1000_intake_*/problems.jsonl` mirrors cannot be rendered byte-for-byte through the connector without truncation. The intake reread is therefore honestly **targeted/partial due connector limits**: the exact I0077 row/source/ownership/exclusions and searchable prior attempts were rechecked. I do not claim a literal reread of every unrelated intake row.

Entering metric: **51**.  
Entering unchanged count: **0**.

## 2. Primary-source benchmark recovered again

The primary PDF was rechecked, including Definition 2.1, Theorem 4.3, and the open-problem page.

An FBM is a continuous real-indexed process `X` admitting random witness times `S_j -> -infinity` such that for each fixed witness index `j`,

\[
B^{(j)}_s:=X_{S_j+s}-X_{S_j},\qquad s\ge0,
\tag{2.1}
\]

is **unconditional standard Brownian motion**.

For `-infinity <= c_1<c_2<=infinity`, Theorem 4.3 uses the killed Ornstein–Uhlenbeck exponent `lambda_0(c_1,c_2)` and states, in full:

1. if `lambda_0(c_1,c_2)>=1`, every FBM has the corresponding far-past normalized limsup/liminf escape obstruction;
2. if `lambda_0(c_1,c_2)<=1`, there exists a decomposable FBM with the corresponding normalized asymptotic confinement;
3. if `c_1<=0<=c_2` and `lambda_0(c_1,c_2)<1`, there exists a decomposable FBM confined pointwise to the exact parabolic strip `c_1 sqrt(|t|) <= X_t <= c_2 sqrt(|t|)` for every `t<=0`.

Problem 7.8 is exactly:

> Can one generalize Theorem 4.3 from parabolas to other space-time shapes?

The following forward-Lévy sentence is Problem 7.9 and is not part of I0077.

## 3. Fresh literature pass — the missing tool was corrected only recently

Fresh dated 2026-09-18 searches included:

- the exact Problem-7.8 wording and the exact paper title/arXiv id;
- later Burdzy publications and citation-oriented searches around *Forward Brownian Motion*;
- Brownian local time on moving/Hölder curves, uniform local-time bounds, and occupation density for moving targets;
- the 2001 Bass–Burdzy paper, its 2002 erratum, and the later corrected theorem.

The decisive external ingredient is now a **current corrected theorem**, not the flawed 2001 proof in its original range:

- R. F. Bass and K. Burdzy, *The supremum of Brownian local times on Hölder curves*, Ann. Inst. H. Poincaré Probab. Statist. 37 (2001), 627–642;
- erratum, Ann. Inst. H. Poincaré Probab. Statist. 38 (2002), 799–800;
- R. F. Bass and K. Burdzy, *The supremum of Brownian local times on Hölder curves revisited*, Ann. Inst. H. Poincaré Probab. Statist. 61 (2025), 890–892, DOI 10.1214/23-AIHP1447; preprint arXiv:2307.13001.

The 2025 paper proves the original claim for every `alpha>1/2`: after choosing a simultaneous version, the local time along `f` is continuous in `f` (sup norm) on the unit `alpha`-Hölder class and its supremum over that class is finite almost surely. It explicitly notes that the earlier proof had an error, the 2002 repair only reached `alpha>5/6`, and the 2025 result restores all `alpha in (1/2,1]`.

The 2001 paper's Section 2 also records the crucial equivalence for Lipschitz curves: local time of Brownian motion along `f` agrees with semimartingale local time at zero of `B-f`. Its heat-kernel estimates are uniform in the starting spatial point. By deterministic time subdivision, Brownian scaling, and spatial translation, the corrected 2025 theorem yields the following standard bounded-ball corollary, which I use below:

> **Uniform bounded-Hölder-ball corollary.** Fix `T,C,M<infinity` and `alpha>1/2`. For Brownian motion on `[0,T]`, one may choose simultaneous curve local times so that, almost surely,
> \[
> \sup\{L_T^f:\ \|f\|_\infty\le M,\ [f]_{C^\alpha}\le C\}<\infty.
> \tag{3.1}
> \]
> The statement also holds simultaneously for all integer choices of `T,C,M` after a countable intersection.

The bounded current search found no accessible later paper explicitly claiming to resolve exact Burdzy–Scheutzow Problem 7.8 or stating the nonlinear-FBM theorem below. That is **bounded negative evidence only**; publication novelty remains **UNVERIFIED**. The Bass–Burdzy local-time theorem itself is prior art and is not claimed new.

## 4. First attack: why the obvious random-phase occupation proof is invalid

Run 51 left a precise frontier: replace affine packet tracks `v u+b+A` by a nonlinear moving target `q(u)+A`.

A tempting but invalid proof is:

1. choose the FBM witness `S_j`;
2. put the random phase `U=-S_j`;
3. regard
   \[
   s\mapsto q(U-s)-q(U)
   \]
   as a deterministic drift;
4. apply the ordinary semimartingale occupation formula to `B_s-[q(U-s)-q(U)]`.

This is not justified: `U` can depend on the Brownian witness path. Pointwise occupation theorems for each deterministic `U` do not automatically survive substitution of a path-dependent `U`. This is the same null-set/quantifier problem that the original Bass–Burdzy paper emphasizes at the critical side of its curve-local-time theorem.

I also tried the stronger extension with an unrestricted uncountable family of tracks. It is false for a trivial exact reason: with singleton packet `A={0}` and constant tracks `q_a(u)=a`, `a in R`, the gate fiber is all of `R`. Thus some control on the track family is mathematically necessary. This is a failed proposed extension, not a refutation of Problem 7.8.

The route that survives is to prove the required occupation-zero statement **simultaneously in the phase before the FBM witness is inserted**.

## 5. Section-B moves actually used

### #3 PROVE SOMETHING STRONGER — success

Rather than prove one explicit nonlinear example, I prove T69 below for a countable family of arbitrary locally Lipschitz tracks, each carrying an arbitrary compact Lebesgue-null packet. The nonlinear logarithmic example is then a corollary.

### #21 ASK WHO ELSE HAS THIS SHAPE — success

The relevant object is not primarily a moving-boundary first-passage problem. It is a **uniform local-time-on-curves** problem. Bass–Burdzy's corrected 2025 theorem supplies exactly the missing compactness/uniformity mechanism for Hölder exponent `>1/2` (and in particular Lipschitz curves).

### #27 SWAP THE QUANTIFIERS — success

The proof does not say “for every deterministic phase `U`, a probability-one event exists.” It constructs one probability-one event on which the null-occupation conclusion holds for **every phase `U` and every spatial translate `c` simultaneously**. Only after that event is fixed do I substitute the random FBM witness phase.

## 6. Simultaneous phase-null occupation lemma

Let `B` be standard Brownian motion on `[0,T]`. Let

\[
q:(0,\infty)\to\mathbb R
\]

be deterministic and locally Lipschitz, and let `A subset R` be compact with `|A|=0`. For `U>T`, define

\[
g_U(s):=q(U-s)-q(U),\qquad 0\le s\le T.
\tag{6.1}
\]

### Lemma 6.1 — simultaneous phase-null occupation

There is a probability-one event such that, **simultaneously for every `U>T` and every `c in R`**, one has

\[
\boxed{
\left|\{s\in[0,T]: B_s-g_U(s)\in c+A\}\right|=0.
}
\tag{6.2}
\]

### Proof

Fix first a compact phase interval

\[
J=[a,b]\subset(T,\infty).
\]

Since `q` is locally Lipschitz, there is a deterministic constant `L_J<infinity` such that `q` is `L_J`-Lipschitz on `[a-T,b]`. Hence for every `U in J`,

\[
\|g_U\|_\infty\le L_JT,
\qquad
\operatorname{Lip}(g_U)\le L_J.
\tag{6.3}
\]

Moreover, for `U,V in J`,

\[
\|g_U-g_V\|_\infty
\le 2L_J|U-V|.
\tag{6.4}
\]

Let `D=J cap Q`. For each deterministic `r in D`,

\[
Y^{(r)}_s:=B_s-g_r(s)
\tag{6.5}
\]

is a continuous semimartingale because `g_r` is deterministic Lipschitz (hence finite variation). Let `ell_r(y)` denote its local time at level `y` by time `T`, chosen jointly continuous in `y`. The occupation-density formula gives, for every Borel set `E`,

\[
\int_0^T 1_E(Y^{(r)}_s)\,ds
=
\int_E \ell_r(y)\,dy.
\tag{6.6}
\]

For a fixed deterministic pair `(r,y)`, Section 2 of Bass–Burdzy identifies `ell_r(y)` (up to the common normalization convention, which is immaterial for finiteness) with Brownian local time along the Lipschitz curve

\[
f_{r,y}(s)=g_r(s)+y.
\tag{6.7}
\]

Now fix an integer `M>=1`. By (6.3), all curves `f_{r,y}` with `r in D` and `|y|<=M` lie in one deterministic bounded Lipschitz ball. Apply (3.1). Intersect additionally over the countable set of rational pairs `(r,y)`; equality of semimartingale and curve local time then holds there. Because `y -> ell_r(y)` is continuous and the corrected Bass–Burdzy version is continuous in the curve under sup norm, equality extends from rational `y` to every real `y`. Consequently, on one probability-one event,

\[
C_{J,M}(\omega)
:=
\sup_{r\in D}\sup_{|y|\le M}\ell_r(y)
<\infty.
\tag{6.8}
\]

Take now arbitrary `U in J` and `c in R`; these may be chosen after seeing the Brownian path. Let

\[
H=\{s\in[0,T]:B_s-g_U(s)\in c+A\}.
\tag{6.9}
\]

Choose rationals `r_n in D` with `r_n -> U`, and set

\[
\delta_n:=\|g_{r_n}-g_U\|_\infty.
\]

By (6.4), `delta_n -> 0`. If `s in H`, then

\[
B_s-g_{r_n}(s)
\in (c+A)^{\delta_n},
\tag{6.10}
\]

where `E^delta` denotes the open `delta`-neighborhood of `E`. Therefore, by (6.6),

\[
|H|
\le
\int_{(c+A)^{\delta_n}}\ell_{r_n}(y)\,dy.
\tag{6.11}
\]

Because `A` is compact, for all sufficiently large `n` the bounded set `(c+A)^{\delta_n}` is contained in `[-M,M]` for some integer `M` (depending on the realized `c`, which is harmless because (6.8) is available simultaneously for every integer `M`). Hence

\[
|H|
\le
C_{J,M}(\omega)\, |A^{\delta_n}|.
\tag{6.12}
\]

Translation does not change Lebesgue measure. Since `A` is compact and null, the nested-neighborhood continuity of Lebesgue measure gives

\[
|A^{\delta_n}|\longrightarrow |A|=0.
\tag{6.13}
\]

Thus `|H|=0`.

Finally cover `(T,infinity)` by countably many compact phase intervals with rational endpoints and intersect the corresponding probability-one events. This proves (6.2) simultaneously for every phase `U>T` and every translate `c`. `QED`

### Quantifier audit

The only occupation formulas applied above are for deterministic rational phases `r`. The random phase is reached solely by uniform approximation **after** a pathwise bound has been made simultaneous over the rational dense set. No conditioning on a random phase is used.

The same proof may be intersected over any countable family `(q_m,A_m)` of locally Lipschitz tracks and compact null packets.

## 7. T69 — countably many nonlinear null-packet tracks

Let `Z subset (0,infinity)` be deterministic measurable. Assume that for some `T>0`, `eta>0`, and `U_0<infinity`,

\[
\boxed{
|Z\cap[U-T,U]|\ge\eta
\qquad(U\ge U_0).
}
\tag{7.1}
\]

Let

\[
(q_m,A_m)_{m\ge1}
\]

be countably many deterministic pairs such that

- `q_m:(0,infinity)->R` is locally Lipschitz;
- `A_m subset R` is compact;
- `|A_m|=0`.

Let `K(u) subset R` be deterministic fibers satisfying, only at gate ages,

\[
\boxed{
K(u)\subset
\bigcup_{m\ge1}(q_m(u)+A_m),
\qquad u\in Z,
}
\tag{7.2}
\]

with **no restriction whatsoever** on `K(u)` for `u notin Z`.

### Theorem T69 — nonlinear null-packet curtain obstruction

For every forward Brownian motion `X`,

\[
\boxed{
\mathbb P\left(
\exists R<\infty:\ X_{-u}\in K(u)\ \forall u\ge R
\right)=0.
}
\tag{T69}
\]

### Proof

Assume instead that eventual confinement has positive probability. By countable decomposition in the tail radius, choose a deterministic `R` for which

\[
E_R:=\{X_{-u}\in K(u)\ \forall u\ge R\}
\tag{7.3}
\]

has positive probability.

Let `S_j -> -infinity` be the FBM witness sequence. Since `S_j -> -infinity` almost surely, there is a deterministic index `j` such that

\[
\mathbb P(E_R\cap\{-S_j\ge \max(U_0,R+T)\})>0.
\tag{7.4}
\]

Fix that index once and for all and write

\[
B_s=X_{S_j+s}-X_{S_j},\qquad 0\le s\le T,
\tag{7.5}
\]

so `B` is unconditional standard Brownian motion by the FBM definition. Put

\[
U=-S_j.
\]

On the event in (7.4), define the reflected gate-time set

\[
F:=\{s\in[0,T]:U-s\in Z\}.
\tag{7.6}
\]

Then by (7.1),

\[
|F|\ge\eta.
\tag{7.7}
\]

For each `m`, let

\[
F_m:=
\{s\in F:
X_{S_j+s}\in q_m(U-s)+A_m
\}.
\tag{7.8}
\]

Because confinement and (7.2) hold at every gate time,

\[
F=\bigcup_{m\ge1}F_m.
\tag{7.9}
\]

For `s in F_m`,

\[
X_{S_j}+B_s\in q_m(U-s)+A_m.
\]

Define

\[
g_{m,U}(s)=q_m(U-s)-q_m(U),
\qquad
c_m=q_m(U)-X_{S_j}.
\tag{7.10}
\]

Then

\[
B_s-g_{m,U}(s)\in c_m+A_m
\qquad(s\in F_m).
\tag{7.11}
\]

Apply Lemma 6.1 on the probability-one event intersected over all `m`. It is simultaneous in the phase `U` and translate `c_m`, even though both are random. Therefore

\[
|F_m|=0
\qquad\text{for every }m.
\tag{7.12}
\]

Countable subadditivity and (7.9) give `|F|=0`, contradicting (7.7). Thus (T69) holds. `QED`

### Dependence audit

The witness **index** `j` is deterministic before Brownian-path facts are invoked. No conditioning on `S_j`, `U`, or `X_{S_j}` occurs. The random phase enters only after Lemma 6.1 has already produced a pathwise statement valid for every phase and translate.

## 8. T70 — canonical nonlinear logarithmic null-packet curtain

I now build one explicit closed shape that is not covered by the affine/ballistic packet theorem from run 51.

### 8.1 Temporal gate set

Let `F_SV subset [0,1]` be the standard Smith–Volterra–Cantor set. It is compact, nowhere dense, and has Lebesgue measure `1/2`; its first removed interval is `(3/8,5/8)`.

Periodize it:

\[
E:= (F_{SV}+\mathbb Z)\cap[0,\infty).
\tag{8.1}
\]

By periodicity, every unit sliding window has exactly half gate-time mass:

\[
\boxed{|E\cap[U-1,U]|=1/2\qquad(U\ge1).}
\tag{8.2}
\]

### 8.2 A compact null packet of full Hausdorff dimension

Reuse the explicit packet from run 51,

\[
A_*:=
\left\{
\sum_{j\ge1}\omega_j2^{-j}:
\omega_j\in\{0,1\},\ \omega_{k^2}=0\ \forall k
\right\}.
\tag{8.3}
\]

It is compact and contains `0`. At binary depth `n`, exactly `floor(sqrt(n))` digits are forced, so it is covered by

\[
2^{n-\lfloor\sqrt n\rfloor}
\]

dyadic intervals of length `2^{-n}`. Their total length is

\[
2^{-\lfloor\sqrt n\rfloor}\to0,
\]

hence

\[
|A_*|=0.
\tag{8.4}
\]

For completeness, put fair product mass on the free digits. A depth-`n` admissible cylinder has mass `2^{-(n-floor(sqrt(n)))}`, and an interval of length comparable to `2^{-n}` meets only `O(1)` such cylinders. For every `s<1`, eventually

\[
2^{-(n-\lfloor\sqrt n\rfloor)}\le C_s2^{-ns},
\]

so the mass-distribution principle gives `dim_H A_*>=s`. Therefore

\[
\boxed{|A_*|=0,\qquad \dim_HA_*=1.}
\tag{8.5}
\]

### 8.3 Nonlinear center and wide off-gate chambers

Set

\[
q(u)=\frac18\log(1+u),
\tag{8.6}
\]

which is smooth, strictly increasing, unbounded, genuinely nonlinear, and globally Lipschitz because

\[
0<q'(u)=\frac1{8(1+u)}\le\frac18.
\tag{8.7}
\]

Let

\[
r(u)=u^3\operatorname{dist}(u,E),
\tag{8.8}
\]

and define

\[
K_*(u):=
\{x\in\mathbb R:\operatorname{dist}(x,q(u)+A_*)\le r(u)\},
\qquad u>0.
\tag{8.9}
\]

Finally let

\[
\mathcal Q_*:=
\{(-u,x):u>0,\ x\in K_*(u)\}
\cup (\{0\}\times A_*).
\tag{8.10}
\]

The shape is closed because

\[
(u,x)\mapsto
\operatorname{dist}(x-q(u),A_*)-r(u)
\]

is continuous for `u>=0`, with `q(0)=r(0)=0`, and `A_*` is compact.

At every gate age `u in E`,

\[
K_*(u)=q(u)+A_*,
\tag{8.11}
\]

a compact uncountable Lebesgue-null set of Hausdorff dimension one.

At the midpoint

\[
u_n=n+1/2
\]

of the periodized first Smith–Volterra gap `(n+3/8,n+5/8)`,

\[
\operatorname{dist}(u_n,E)=1/8,
\qquad
r(u_n)=u_n^3/8.
\tag{8.12}
\]

Since `0 in A_*`, the fiber contains the interval

\[
[q(u_n)-u_n^3/8,\ q(u_n)+u_n^3/8],
\tag{8.13}
\]

whose diameter is `u_n^3/4`. Thus the admissible chambers become **cubically wide** between nowhere-dense positive-time null-packet gates.

Apply T69 with one track `q`, one packet `A_*`, `T=1`, `eta=1/2`, and `Z=E`.

### Theorem T70 — logarithmically curved dimension-one null-packet curtain

For every forward Brownian motion `X`,

\[
\boxed{
\mathbb P\left(
\exists R<\infty:\ (-u,X_{-u})\in\mathcal Q_*
\quad\forall u\ge R
\right)=0.
}
\tag{T70}
\]

This is the family earning metric point **52**.

## 9. Frozen-equivalence audit — why point 52 is not run 44, 45, 49, 50, or 51 again

### Versus run 44 — fixed-null occupation curtains

Run 44 requires one fixed spatial null set `A` containing every restrictive gate fiber. Here a fixed null set cannot contain all `q(u)+A_*`, `u in E`.

Indeed `0 in A_*`, so any such set would contain `q(E)`. On each period `[n,n+1]`, `q` is bi-Lipschitz onto its image because

\[
\frac1{8(n+2)}\le q'(u)\le\frac1{8(n+1)}.
\tag{9.1}
\]

Since `|E cap [n,n+1]|=1/2`, its image `q(E cap[n,n+1])` has positive Lebesgue measure. Hence no fixed spatial null set contains the gate fibers. T53/T54 from run 44 are genuinely silent.

### Versus run 45 — fixed spatial fractal / strict image-dimension gap

Run 45 pins into one fixed spatial set of Hausdorff dimension `a<1` and needs the strict inequality `d>(1+a)/2`. Here the packet has `a=1`; with temporal gate dimension `d=1`, the inequality becomes `1>1`, false. Moreover the packet translates nonlinearly with age.

### Versus run 49 — countable finite-variation traces

Run 49 requires a gate fiber contained in countably many track values. Here each gate fiber `q(u)+A_*` is uncountable and has Hausdorff dimension one. It cannot be reduced to a countable trace family.

### Versus run 50 — traveling Cantor velocity fans

Run 50 requires packet dimension strictly below `2d-1`. At `d=1` our packet dimension is exactly one, the excluded endpoint. Its proof gives no information here.

### Versus run 51 — affine/ballistic null packets

Run 51 allows countably many affine tracks `v_m u+b_m+A_m`. The new center `q(u)=(1/8)log(1+u)` cannot be hidden inside any countable affine-null-packet representation on the positive-measure gate set.

To see this already from the point `q(u)` (because `0 in A_*`), suppose

\[
q(u)\in v_m u+b_m+A_m
\]

for `u` in a set `E_m`, with `A_m` null. Define

\[
h_m(u)=q(u)-v_m u-b_m.
\]

Then

\[
h_m'(u)=\frac1{8(1+u)}-v_m.
\tag{9.2}
\]

This derivative vanishes at at most one point. Away from that point the domain is a countable union of intervals on which `|h_m'|` is bounded below, so `h_m` has a locally Lipschitz inverse there. Therefore

\[
|h_m^{-1}(A_m)|=0.
\tag{9.3}
\]

Adding the possible single critical point still gives `|E_m|=0`. A countable union of such `E_m` cannot cover `E`, which has positive measure in every unit period. Thus no T67 affine packet representation can contain the new gate fibers.

The distinction is geometric and invariant under the frozen equivalences: a constant Brownian rescaling/reflection/translation sends a nonlinear logarithmic center to another nonlinear logarithmic center; it cannot turn its nonconstant slope into an affine ballistic track. The new shape is therefore not a parameter change inside run 51.

## 10. Exact-check policy

There is no nontrivial finite computational core in T69/T70. The argument is analytic. The finite identities used in the canonical example—Smith–Volterra measure `1/2`, first-gap midpoint distance `1/8`, and the binary-cylinder count `2^{n-floor(sqrt(n))}`—are exact symbolic facts proved on the page. In accordance with the owner's 90/10 rule, I did **not** manufacture a checker merely to create an artifact.

## 11. What moved and what remains

The tracked metric moved

\[
\boxed{51\longrightarrow52.}
\]

The substantive new ingredient is not another checker or another cage estimate. It is the simultaneous-phase lemma (6.2), which closes the random-witness-phase gap explicitly identified at the end of run 51.

T69/T70 are theorem-sized claims with a complete proof on this page. They currently have:

- source recovery: yes;
- current/later-author literature pass: yes;
- full proof on page: yes;
- finite core requiring exact checker: none;
- independent OTHER-track audits: **0/2**;
- publication novelty: **UNVERIFIED**.

Therefore exact Problem 7.8 remains **PARTIAL**, not closed. No `paper_<name>/` folder is created because the owner's closure rule is not met.

The next mathematically genuine frontier is the **critical rough-track boundary**. Bass–Burdzy's corrected theorem is uniform for Hölder exponent `alpha>1/2`, while their earlier work identifies `1/2` as the critical value for the curve-local-time supremum. A next route should decide whether a source-appropriate FBM obstruction survives for nonlinear track families at critical `1/2` regularity using a finer gauge/capacity, rather than merely taking another Lipschitz corollary. I do not claim such a theorem here.

## 12. Model / reasoning / scheduler-control escalation

The actual runtime exposed to this report is **GPT-5.6 Sol / reasoning UNVERIFIED**, not GPT-6 / maximum.

The task-control schema exposed in this environment still has prompt/title, schedule or start-offset, enabled state, and timing mode. It still exposes **no binding model-family selector, no reasoning-effort selector, no guaranteed-duration field, and no authenticated completed-run receipt of the applied model/reasoning level**. Therefore `GPT-6 / maximum` remains a prompt request only; it cannot honestly be claimed as enforced.

The current repository state also records that P26's historical `You cannot modify this task` error was authorization-context-specific: a later full P26 prompt update succeeded from an authorized context, while other contexts still denied some native IDs. The legitimate remedy for any task that still rejects modification is the owning/authorized account or workspace, an authorized ownership/admin correction, or platform support. It is not a duplicate schedule, permission bypass, or fabricated success.

No scheduler modification was attempted in this run, in accordance with the owner's instruction.

## 13. Structured ledger_delta

```yaml
ledger_delta:
  worker: R07
  allocation: CLOSABLE_OUTSIDE
  source_id: I0077
  source: "Burdzy--Scheutzow, Forward Brownian Motion, Problem 7.8"
  target: "generalize Theorem 4.3 beyond parabolic regions"
  metric: "number of genuinely distinct nonparabolic shape families with complete source-appropriate theorem"
  before: 51
  after: 52
  movement: true
  unchanged_count_after: 0
  methods: [3, 21, 27]
  new_claims:
    - T69: "countable locally-Lipschitz nonlinear null-packet curtain obstruction"
    - T70: "logarithmically curved dimension-one null-packet curtain"
  mechanism: "simultaneous-in-phase occupation zero via corrected uniform Brownian local times on Holder curves"
  source_status: PARTIAL
  canonical_claim_status: PENDING_ADMISSION_NOT_READY
  finite_core: none
  checker_created: false
  other_track_audits: "0/2"
  publication_novelty: UNVERIFIED
  next_frontier: "critical 1/2-Holder nonlinear track families / gauge or capacity replacement"
  scheduler_changes: none
  delivery: "private GitHub only"
```
