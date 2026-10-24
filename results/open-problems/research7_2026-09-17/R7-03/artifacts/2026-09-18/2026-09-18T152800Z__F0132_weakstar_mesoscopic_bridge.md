Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime model/effort telemetry or binding selector is exposed.

# F0132 source-status reconciliation and a weak-* -> mesoscopic scaling bridge

Run date: 2026-09-18 UTC  
Slot: R7-03 Boundary-Case Research  
Native ID: `6aabe7be74008191b526b109ee4e9e80`  
Repository: `yspennstate/math-open-problems`, existing `master`  
Captured start-of-run master: `46f981d6d113f55ec1cc8a1be637bc88f77adef2`  
Fresh master before this artifact: `67e6a20272695b3e6f3a884fa055d2b150930e4b`

## 1. Exact outside source and canonical scope

Canonical candidate: `F0132`. Its case-sensitive checksum is

`sum(ord(c) for c in "F0132") = 268 = 2 (mod 7)`,

so it lies in R7-03's initial-selection shard. There is no `operations/claims/F0132.md` at the fresh master above, but absence of a claim is not by itself permission to admit it.

Original outside source:

- Alexander E. Holroyd, Lionel Levine, Karola Mészáros, Yuval Peres, James Propp, David B. Wilson;
- *Chip-Firing and Rotor-Routing on Directed Graphs*;
- 2008, arXiv:0801.3306;
- Conjecture 6.4, Section 6, PDF p. 31;
- source copy: https://lionellevine.github.io/sand.pdf .

Let `I_n` be the identity element of the sandpile group of the `n x n` square grid `G_n` with wired boundary. For integers `a_n` with `a_n -> infinity` and `a_n/n -> 0`, define

\[
f_n(x)=\frac1{a_n^2}\sum_{\substack{y\in G_n\\ \|y-nx\|\le a_n}} I_n(y),\qquad x\in[0,1]^2.
\]

The source asks whether there exist such a sequence `a_n` and a function `f:[0,1]^2 -> R_{>=0}`, locally constant almost everywhere, such that `f_n(x)->f(x)` at every continuity point of `f`.

This is an identity-element problem on the wired square grid. It is not the point-source sandpile convergence problem.

## 2. Dated current-status reconciliation: announced solution, but not a clean published closure

The current record is materially subtler than either `OPEN` or `KNOWN`.

### 2.1 Sportiello's 2015 announced solution

Andrea Sportiello's ICERM talk, *The limit shape of the Abelian Sandpile identity*, was given on 2015-04-14. The surviving ICERM abstract says that the determination of the recurrent identity's limit shape "was an open problem up to date, and is here solved." It further says that the shapes and contents of polygonal patches stabilize in the scaled-domain limit and gives explicit algebraic coordinates, including the central-square constant `0.58315637...`.

Public records:

- https://icerm.brown.edu/program/semester_program_workshop/sp-s15-w3
- https://icerm.brown.edu/video_archive/332
- abstract PDF indexed by ICERM under the title above.

Thus it is incorrect to describe F0132 in 2026 as having no claimed solution at all.

### 2.2 The 2019 published literature still treated the proof as announced

Lang and Shkolnikov, *Harmonic dynamics of the Abelian sandpile*, PNAS 116 (2019), explicitly distinguish the identity from sandpile configurations for which rigorous scaling limits were already available. They state that corresponding rigorous results for the sandpile identity were still missing, while noting that a proof of the identity scaling limit had recently been **announced**; their reference for the announcement is Sportiello's ICERM video. The same paper formulates as its Conjecture 1 weak-* convergence of the sandpile identities to a piecewise smooth function and says that existence of such a limit had not yet been shown in the published setting.

Published source:

- https://doi.org/10.1073/pnas.1812015116

This is affirmative evidence that the 2015 announcement was known, but not then available as a conventional written proof of the square-grid identity limit.

### 2.3 Related rigorous work does not by title/abstract alone close F0132

Pegden--Smart, *Stability of patterns in the Abelian sandpile* (Ann. Henri Poincaré 21 (2020), arXiv:1708.09432), proves pattern stability and upgrades weak-* convergence to pattern convergence for **certain classes of solutions**. Its abstract does not identify HLM+ Conjecture 6.4 or the square-grid sandpile identity as one of those classes.

Melchionna, *The sandpile identity element on an ellipse* (DCDS 42 (2022)), proves that on certain elliptical square-lattice domains the recurrent identity is predominantly biperiodic and the noisy area fraction tends to zero. This is a different domain family, not the wired square-grid conjecture.

Kaiser--Sava-Huss (2023) and Kaiser--Sava-Huss--Überbacher (2026) prove scaling statements for identity elements on finite approximations of the **Sierpinski gasket**, again a different graph family.

A bounded 2026-09-18 search did not locate a conventional written theorem by Sportiello or another author that states the full wired-square-grid HLM+ Conjecture 6.4 with its mesoscopic-average quantifiers. This is negative evidence only and is not a novelty/openness certificate.

### 2.4 Honest disposition

For admission purposes the right label is therefore:

**ANNOUNCED_SOLUTION / WRITTEN SOURCE-MATCHING PROOF NOT VERIFIED IN THIS RUN.**

That status already makes F0132 unsafe to claim as a clean open target. Independently, the conjecture is asymptotic/fractal and is honestly HARD rather than the CLOSABLE endpoint/sharp-constant shape required for R7-03. Hence no canonical claim is created.

## 3. B18 — translate the source statement into a measure-theoretic shrinking-ball problem

The useful mathematical reduction is exact and does not use any unverified sandpile theorem.

Let `Q=[0,1]^2`. Extend the grid configuration by zero outside its actual vertex set and define the finite empirical measure

\[
\mu_n:=\frac1{n^2}\sum_{y\in G_n} I_n(y)\,\delta_{y/n}.
\]

Because a stable square-grid sandpile height belongs to `{0,1,2,3}`, the total masses are uniformly bounded and each lattice atom has mass at most `3/n^2`.

Put

\[
h_n:=\frac{a_n}{n}.
\]

Then the HLM+ block average is exactly

\[
\boxed{\quad f_n(x)=h_n^{-2}\mu_n(B(x,h_n)).\quad}
\]

For the Euclidean norm, the target local normalization is therefore `pi` times the density of any absolutely continuous weak-* limit. For another fixed norm it is the area of that norm's unit ball.

This translation isolates the only scale-selection issue: weak-* convergence controls fixed macroscopic test scales, while HLM+ requires a **single shrinking scale** `h_n -> 0` with `n h_n=a_n -> infinity`.

## 4. B12 — mesoscopic extraction theorem

### Theorem (weak-* convergence implies one source-valid mesoscopic sequence)

Let `q_n:G_n -> [0,M]` be any uniformly bounded lattice functions on the square grid and

\[
\mu_n=\frac1{n^2}\sum_{y\in G_n}q_n(y)\delta_{y/n}.
\]

Assume

\[
\mu_n \Rightarrow \mu=\rho(x)\,dx
\]

weakly as finite measures on `Q`, with `rho in L^infty(Q)`.

Then there exists a sequence of integers `a_n` satisfying

\[
a_n\to\infty,\qquad \frac{a_n}{n}\to0,
\]

such that, simultaneously at every **interior Lebesgue point** `x` of `rho`,

\[
\boxed{
\frac1{a_n^2}
\sum_{\substack{y\in G_n\\|y-nx|\le a_n}}q_n(y)
\longrightarrow \pi\rho(x).
}
\]

More generally `pi` is replaced by the area `kappa` of the unit ball of the norm used in the averaging condition.

Consequently, if the weak-* limit density has a representative `rho_tilde` that is locally constant almost everywhere, then HLM+ Conjecture 6.4 follows: set `f=pi rho_tilde` in the interior (and choose boundary values so that boundary points which are not covered by the tangent-cone limit are discontinuity points). Every interior continuity point of `f` is a Lebesgue point of `rho`, so the displayed convergence gives exactly the source conclusion.

### Proof

The only nonstandard point is obtaining **one shrinking sequence** from weak convergence. The bounded lattice heights provide enough uniform anti-concentration to diagonalize.

#### Step 1: a uniform lattice-annulus estimate

For any center `x`, radius `r>0`, thickness `eta>0`, let

\[
A(x;r,\eta)=B(x,r+\eta)\setminus B(x,(r-\eta)_+).
\]

Associate to each lattice point `z=y/n` its square cell of side `1/n` centered at `z`. These cells have disjoint interiors and every cell whose center lies in `A(x;r,eta)` is contained in the enlarged annulus with thickness

\[
t=\eta+\sqrt2/n.
\]

Therefore, for an absolute constant `C`,

\[
\#\{y:y/n\in A(x;r,\eta)\}
\le Cn^2\big(r t+t^2\big).
\]

Since `0<=q_n<=M`, this gives uniformly in `x`

\[
\boxed{
\mu_n(A(x;r,\eta))
\le CM\left[r\left(\eta+\frac1n\right)
+\left(\eta+\frac1n\right)^2\right].
}
\tag{4.1}
\]

The absolutely continuous limit satisfies the analogous deterministic estimate

\[
\mu(A(x;r,\eta))\le C\|\rho\|_\infty(r\eta+\eta^2).
\tag{4.2}
\]

#### Step 2: weak convergence is uniform over centers at every fixed radius

Fix `r>0` and write

\[
F_{n,r}(x)=\mu_n(B(x,r)),\qquad F_r(x)=\mu(B(x,r)).
\]

Because `mu` has a density, every circle `partial B(x,r)` has `mu`-measure zero. Hence weak convergence gives

\[
F_{n,r}(x)\to F_r(x)
\]

for each fixed center `x`.

To upgrade this to uniform convergence, fix `eta>0` and take a finite `eta`-net `{x_1,...,x_N}` of `Q`. If `|x-x_j|<=eta`, then

\[
B(x,r)\triangle B(x_j,r)
\subset A(x_j;r,\eta).
\]

Equations (4.1)--(4.2) show that the variation of both `F_{n,r}` and `F_r` between `x` and `x_j` is `O(r eta+eta^2)+o_n(1)`, uniformly in the center. At the finite net points, pointwise convergence is uniform once `n` is large. First send `n->infinity` and then `eta->0`. Therefore

\[
\boxed{
\sup_{x\in Q}|\mu_n(B(x,r))-\mu(B(x,r))|\to0
}
\tag{4.3}
\]

for every fixed `r>0`.

#### Step 3: diagonalize fixed scales into one mesoscopic scale

Choose any deterministic sequence `r_m downarrow 0`, for example `r_m=2^{-m}`. By (4.3), choose strictly increasing integers `N_m` so large that whenever `n>=N_m`,

\[
\sup_x|\mu_n(B(x,r_m))-\mu(B(x,r_m))|
\le \frac{r_m^2}{m},
\tag{4.4}
\]

and also

\[
nr_m\ge m^2.
\tag{4.5}
\]

For `N_m<=n<N_{m+1}`, define

\[
a_n=\lfloor nr_m\rfloor,
\qquad h_n=\frac{a_n}{n}.
\]

Then `h_n->0`. Moreover (4.5) gives

\[
a_n\ge m^2-1\to\infty,
\]

so `a_n` is a source-valid mesoscopic averaging scale.

#### Step 4: replacing `r_m` by the lattice-compatible `h_n` costs `o(h_n^2)`

We have

\[
|h_n-r_m|\le 1/n,
\qquad \frac{|h_n-r_m|}{r_m}\le\frac1{nr_m}\le\frac1{m^2}.
\]

Applying the annulus estimate (4.1) with thickness `1/n`, and using `nr_m>=m^2`, yields

\[
\sup_x
\frac{|\mu_n(B(x,h_n))-\mu_n(B(x,r_m))|}{r_m^2}
=O(m^{-2}).
\tag{4.6}
\]

The same scale relation gives `h_n^{-2}/r_m^{-2}->1`. Since the normalized ball masses are uniformly bounded by the lattice-counting estimate, (4.4)--(4.6) imply

\[
\boxed{
\sup_x\left|
 h_n^{-2}\mu_n(B(x,h_n))
-r_m^{-2}\mu(B(x,r_m))
\right|\to0.
}
\tag{4.7}
\]

#### Step 5: differentiate the limiting density

Let `x` be an interior Lebesgue point of `rho`. For all sufficiently large `m`, `B(x,r_m) subset Q`, and the Lebesgue differentiation theorem gives

\[
\frac1{\pi r_m^2}\int_{B(x,r_m)}\rho(z)\,dz\to\rho(x).
\]

Equivalently,

\[
r_m^{-2}\mu(B(x,r_m))\to\pi\rho(x).
\tag{4.8}
\]

Combining (4.7) and (4.8) proves the theorem. The construction of `a_n` is independent of `x`, so the same sequence works simultaneously at every interior Lebesgue point. `QED`.

## 5. B29 — boundary/end-point bookkeeping

The source defines `f_n` on the closed square. At a smooth boundary point of `Q`, a shrinking Euclidean ball sees asymptotically half a disk, while at a corner it sees one quarter. Thus if `rho` has a continuous representative up to the boundary, the corresponding geometric limits are

\[
\frac\pi2\rho(x)\quad\text{on an edge},
\qquad
\frac\pi4\rho(x)\quad\text{at a corner}.
\]

This does not obstruct the source conjecture. Boundary points have two-dimensional measure zero, so boundary values of `f` do not affect the requirement that `f` be locally constant almost everywhere. One may either use the tangent-cone values above when their continuity is desired, or define the boundary representative so that boundary points are discontinuities. The convergence obligation in Conjecture 6.4 applies only at continuity points of the chosen `f`.

Thus the substantive content of the mesoscopic bridge is the interior weak-* density.

## 6. What the bridge does and does not prove

The theorem proves a clean implication that was not explicit in the repository's previous F0132 attempt:

\[
\boxed{
\text{weak-* convergence of the square-grid identities to a bounded}
\atop
\text{locally-constant-a.e. density}
\quad\Longrightarrow\quad
\text{HLM+ Conjecture 6.4.}
}
\]

It also explains the exact relationship between later formulations and the 2008 source:

1. Merely proving weak-* convergence to an arbitrary **piecewise smooth** function, as conjectured in the 2019 PNAS paper, is not logically sufficient for the source's `locally constant almost everywhere` clause.
2. A theorem proving the stronger patch-content stabilization described in Sportiello's 2015 abstract would be source-relevant if it supplies a bounded locally-constant-a.e. weak-* density. The diagonal theorem above would then manufacture the required single sequence `a_n` automatically.
3. Pegden--Smart pattern stability is exactly the kind of theorem that could supply the second ingredient once its hypotheses are verified for the square-grid identity, but its published abstract only claims this for certain classes of solutions. No source-level hypothesis match is assumed here.

Accordingly this artifact is **not** a proof of F0132. It is a complete reduction of the mesoscopic-scale selection issue to a macroscopic weak-* / patch-density theorem.

## 7. Admission conclusion and gaps

`F0132` remains **NOT ADMITTED** by R7-03 for two independent reasons:

- the source has a concrete 2015 announced solution whose full written proof/status has not been reconciled, so it is not safe open inventory;
- even if the announcement were disregarded, the full square-grid fractal scaling theorem is honestly HARD, not a CLOSABLE endpoint/boundary/sharp-constant source.

Exact remaining mathematical/source-status gaps:

1. Recover a citable written proof, if one exists, corresponding to Sportiello's 2015 solution announcement, and check it theorem-by-theorem against HLM+ Conjecture 6.4.
2. If no such proof exists, establish for the wired-square-grid identities either (a) weak-* convergence to a locally-constant-a.e. density, or (b) a stronger pattern-stabilization theorem implying that statement.
3. Verify whether Pegden--Smart's `certain classes of solutions` include the two-stabilization/identity boundary-value problem; no such inclusion is assumed here.

No novelty claim is made for the literature-status observations or for the theorem beyond this repository's cumulative research record.

## 8. Method accounting

Immediately preceding R7-03 methods were `B2 / B21 / B30`. This run used a nonrepeating triple:

- **B18 — translate the statement:** exact identity `f_n(x)=h_n^{-2}mu_n(B(x,h_n))`.
- **B12 — transform to normal form:** uniform fixed-radius ball convergence plus diagonal extraction proves the mesoscopic extraction theorem.
- **B29 — endpoint/degenerate analysis:** boundary tangent-cone constants and the continuity-point convention remove a false boundary obstruction.

Because no target is admitted, these are admission-side mathematical methods and do not start or advance a target stagnation counter.

## 9. Metric

Successor metric remains intentionally unfrozen:

- before: `UNKNOWN/UNMEASURED`;
- after: `UNKNOWN/UNMEASURED`;
- target-specific stagnation count: `NOT_STARTED`.

This is not a reset of any predecessor metric. Retired/handoff histories remain attached to their own targets.
