Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime reasoning-effort telemetry or binding model/effort selector is exposed.

# G0008 — local-star deformation, finite-energy surgery, and an open homogeneous interval around criticality

Target: Campos--de Lima, canonical intake `G0008`, Bernoulli bond percolation on `Z^2`.  Write

\[
\tau_n(p)=\mathbb P_p(0\leftrightarrow n e_1).
\]

The full source question asks whether `tau_{n+1}(p) <= tau_n(p)` for every `0<p<1` and every `n>=1`.  The frozen R7-06 metric remains `M_axis=UNKNOWN/UNMEASURED`: this artifact strengthens the first-step analysis but does **not** prove `tau_1>=tau_2` for every parameter.

The preceding run proved the strict critical certificate

\[
\tau_1(1/2)-\tau_2(1/2)\ge {13\over4096}>0,
\tag{1}
\]

and the six-orbit punctured-star normal form.  This run uses the nonrepeating Section-B triple **B5 / B25 / B6**.

## 1. B5 — add independent central-edge parameters and differentiate exactly

Let `x=0`, `y=e_1`, `z=2e_1`.  Delete the two path edges `xy,yz` but leave every other edge at the bulk Bernoulli parameter `p`; call the resulting graph `H`.  Denote the five terminal-partition masses on `{x,y,z}` by

- `c`: `xyz` all connected;
- `a`: `xy|z`;
- `a'`: `yz|x`;
- `b`: `xz|y`;
- `s`: `x|y|z`.

No reflection assumption is needed for the next lemma.

### Lemma 1 (two-edge deformation identity)

Restore `xy` independently with probability `r` and `yz` independently with probability `t`.  Then

\[
\boxed{
D(r,t):=\mathbb P(x\leftrightarrow y)-\mathbb P(x\leftrightarrow z)
=(1-t)\,[a-(1-r)b+rs].
}
\tag{2}
\]

Equivalently, with

\[
\Delta_H=a-b,
\qquad
D_H=b+s,
\]

we have

\[
\boxed{D(r,t)=(1-t)(\Delta_H+rD_H).}
\tag{3}
\]

#### Proof

Condition on the terminal partition in `H`.

- On `xyz`, the two indicators agree.
- On `xy|z`, `x<->y` is certain and `x<->z` occurs iff `yz` is restored, giving `1-t`.
- On `yz|x`, both connections occur iff `xy` is restored, giving difference zero.
- On `xz|y`, `x<->z` is certain and `y` joins that cluster unless both restored edges fail, so the difference is `-(1-r)(1-t)`.
- On `x|y|z`, `x<->y` requires `xy`, while `x<->z` requires both edges, giving `r(1-t)`.

Summing gives (2), and regrouping gives (3). QED.

### Consequences

For every fixed defect law,

\[
\boxed{\partial_r D(r,t)=(1-t)D_H\ge0.}
\tag{4}
\]

Thus increasing the **near** path-edge probability can only improve the first comparison.  More strikingly, the **far** path-edge probability `t` affects the sign only through the positive factor `1-t`: the sign is completely determined by `Delta_H+rD_H`.

If `b>a`, the exact local horizontal threshold is

\[
r_*(H)={b-a\over b+s};
\tag{5}
\]

if `b<=a`, take `r_*(H)=0`.  For `t<1`, the first comparison holds exactly iff `r>=r_*(H)`.  In the homogeneous square lattice, `H` itself depends on the bulk parameter `p`, and the source first-step problem is precisely

\[
\boxed{p\ge r_*(H_p).}
\tag{6}
\]

Equation (6) is not a solution; it is an exact deformation threshold that isolates the remaining global quantity.

## 2. B5 continued — four-terminal punctured-star polynomial

Delete all four edges incident to `y`, obtaining the punctured lattice `K`.  Around the hole order the neighbors as `x,u,z,d`.  As in the preceding run, the 14 noncrossing partitions have six `D_4` orbit masses per specified partition:

`(sigma,alpha,beta,gamma,delta,epsilon)`

with orbit sizes `(1,4,2,2,4,1)`.

Keep the bulk law on `K` fixed.  Restore `yx` with probability `r`, `yz` with probability `t`, and the two vertical star edges `yu,yd` with probability `v`.  Exact conditioning on the 14 partitions gives

\[
\boxed{D(r,t,v)=(1-t)Q(r,v),}
\tag{7}
\]

where

\[
\begin{aligned}
Q(r,v)={}&r\sigma
+2(2r+v-2rv)\alpha
+(2r-1)\beta\\
&+2(1-v)(r+v-rv)\gamma\\
&+(2rv^2-6rv+4r-v^2+4v-2)\delta\\
&-(1-r)(1-v)^2\epsilon.
\end{aligned}
\tag{8}
\]

This polynomial has an exact positive derivative in the near-edge parameter:

\[
\boxed{
\begin{aligned}
\partial_rQ={}&\sigma+4(1-v)\alpha+2\beta
+2(1-v)^2\gamma\\
&+2(1-v)(2-v)\delta+(1-v)^2\epsilon\ge0.
\end{aligned}}
\tag{9}
\]

At `r=t=v=p`, (8) reduces exactly to the previous homogeneous bracket

\[
\begin{aligned}
B_H={}&p\sigma+2p(1+2q)\alpha+(p-q)\beta\\
&+2pq(1+q)\gamma+(1-q^2-2q^3)\delta-q^3\epsilon,
\end{aligned}
\tag{10}
\]

with `q=1-p` and `tau_1-tau_2=qB_H`.

The finite 14-partition identity, factorization, derivative, and homogeneous specialization were executed exactly in

`research7_2026-09-17/R7-06/artifacts/2026-09-18/2026-09-18T050500Z__G0008_star_deformation_checker.py`

creation commit `75815bfcf25275443227f014723c06173be97e84`, with archived output

`research7_2026-09-17/R7-06/artifacts/2026-09-18/2026-09-18T050500Z__G0008_star_deformation_checker.out`

creation commit `bbd7c305f5ce21bcc3d8d080cd81f8833fc678fd` ending

`ALL_EXACT_CHECKS_PASS`.

## 3. B25 — double-count terminal leaves to get a new finite-energy orbit inequality

The only negative orbit at the solved critical point was `epsilon`, the event that all four puncture terminals are connected.  A natural strategy is therefore to convert all-four-connected configurations into favorable triple-plus-singleton configurations by a local surgery.  There is a rigorous universal inequality, but it also reveals the exact deficit of this strategy.

### Proposition 2 (leaf-surgery inequality)

For Bernoulli(`p`) percolation on the punctured square lattice `K`, with `q=1-p`,

\[
\boxed{\delta\ge {q^3\over2}\,\epsilon.}
\tag{11}
\]

Here `delta` is the probability of one specified triple-plus-singleton partition and `epsilon` is the all-four-connected probability.

#### Proof

For each terminal `w in {x,u,z,d}`, let `E_w` be the event that the **other three** terminals are connected after deleting the three remaining `K`-edges incident to `w` (the central edge `wy` was already removed in `K`).

On any configuration in the `epsilon` event, choose a finite tree contained in the open cluster and minimal under edge deletion while still spanning all four terminals.  Every leaf of such a minimal Steiner tree is a terminal, and every finite tree has at least two leaves.  If `w` is a leaf, deleting `w` from the tree leaves the other three terminals connected without using any edge incident to `w`; hence `E_w` holds.  Pointwise,

\[
\sum_{w\in\{x,u,z,d\}}\mathbf1_{E_w}\ge2\mathbf1_{\epsilon}.
\tag{12}
\]

By `D_4` symmetry, the four probabilities `P(E_w)` are equal, so

\[
\mathbb P(E_d)\ge\epsilon/2.
\tag{13}
\]

The event `E_d` is measurable with respect to all edges except the three deleted incident edges of `d`; hence it is independent of their states.  If `E_d` occurs and all three such edges are closed, `d` is isolated in `K` while `x,u,z` are connected.  This is exactly the specified `delta` partition. Therefore

\[
\delta\ge q^3\mathbb P(E_d)\ge(q^3/2)\epsilon.
\]

QED.

This is a genuine finite-energy constraint absent from the abstract orbit polytope.  It is nevertheless not enough by itself to settle (10): for `p>=1/2`, the guaranteed `delta` contribution only pays a fraction of the adverse `-q^3 epsilon` term.  Thus the missing injection must also create or control `alpha`, `beta`, `gamma`, or `sigma`, or use a genuinely global planar constraint.

### Exact no-go for an FKG-only orbit proof

The formal orbit law `epsilon=1` and all other orbit masses zero is noncrossing, `D_4`-symmetric, and satisfies every FKG inequality among terminal-connectivity events with equality.  After restoring the star, its detour probability with `xy` forced closed is

\[
F=1-q^3>p,
\]

so it even has the correct supercritical side of the source detour-threshold sign.  Yet its first-step difference is

\[
\tau_1-\tau_2=-q^4<0.
\]

This is **not** a percolation counterexample: `epsilon=1` violates finite energy for the actual punctured lattice law.  It proves only that noncrossing + dihedral symmetry + terminal FKG + the sign `F>p` cannot, by themselves, force the desired inequality.  Proposition 2 identifies one precise finite-energy ingredient that any successful orbit proof must exploit.

## 4. B6 — deform the solved homogeneous critical point

The strict certificate (1) implies more than a single parameter value because fixed-vertex connectivities are continuous at criticality on `Z^2`.

### Lemma 3 (continuity at a parameter with no infinite cluster)

Let `G` be locally finite and suppose `P_{p0}(x<->infinity)=0`.  For every fixed vertex `w`, the function

\[
p\mapsto\mathbb P_p(x\leftrightarrow w)
\]

is continuous at `p0`.

#### Proof

Choose finite boxes `Lambda_R` increasing to `G`, containing `x,w`.  Let `A_R` be the event that `x` connects to `w` using a path entirely in `Lambda_R`, and let `B_R` be the event that `x` connects inside `Lambda_R` to its boundary.  Both are cylinder events, so their probabilities are polynomials in `p` and hence continuous.

If `A={x<->w}`, then

\[
A_R\subseteq A,
\qquad
A\setminus A_R\subseteq B_R.
\tag{14}
\]

At `p0`, `P_{p0}(B_R)` decreases to `P_{p0}(x<->infinity)=0`.  Given `eta>0`, choose `R` with `P_{p0}(B_R)<eta`.  For `p` sufficiently close to `p0`, cylinder-event continuity gives

\[
|P_p(A_R)-P_{p0}(A_R)|<\eta,
\qquad
P_p(B_R)<2\eta.
\]

Using (14) and also `P_{p0}(A)-P_{p0}(A_R)<=P_{p0}(B_R)`, we get two-sided bounds tending to zero with `eta`.  Hence `P_p(A)->P_{p0}(A)`. QED.

Critical bond percolation on the square lattice has no infinite open cluster at `p_c=1/2`. Applying Lemma 3 to `w=e_1,2e_1`, the difference

\[
D(p)=\tau_1(p)-\tau_2(p)
\]

is continuous at `1/2`.  Combining this with (1) yields:

### Corollary 4 (nontrivial homogeneous interval around criticality)

There exists `eta_*>0` such that

\[
\boxed{\tau_1(p)>\tau_2(p)\quad\text{whenever}\quad |p-1/2|<\eta_*.}
\tag{15}
\]

The argument is qualitative: it does not currently give a useful explicit `eta_*`.  Nevertheless it removes the possibility that any first-step counterexample accumulates at the self-dual point.  Combined with the prior explicit low/high-density certificates, a hypothetical first-step counterexample is confined away from `p=0`, away from `p=1`, and a positive distance away from `p=1/2`.

## 5. What moved mathematically and what did not

The frozen metric is unchanged:

`M_axis: UNKNOWN/UNMEASURED -> UNKNOWN/UNMEASURED` (**NO MOVEMENT**).

This is ordinary unchanged research run 3 on G0008.  Therefore the **next** R7-06 run is forced by the owner protocol to be a thinking-only STUCK1 diagnosis, not a fourth ordinary lemma run.

What did move in the proof architecture:

1. The central two-edge problem now has an exact deformation threshold `r_*(H)` and monotonicity in the near-edge probability.
2. The full four-terminal star polynomial factorizes by `1-t` and is coefficientwise nondecreasing in `r`; this was exactly executed.
3. A new finite-energy inequality `2 delta >= q^3 epsilon` is proved by terminal-leaf double counting.
4. An FKG-only orbit proof is rigorously ruled out by an abstract orbit law, identifying finite energy/local surgery as essential.
5. The exact critical inequality extends to a genuine, though nonquantified, homogeneous parameter interval.

## 6. Exact remaining blocker for the mandated next diagnosis

At the first source milestone, the sharp obstruction can now be written in three equivalent ways:

\[
\boxed{\Delta_{H_p}+pD_{H_p}\ge0,}
\tag{16}
\]

\[
\boxed{p\ge r_*(H_p),}
\tag{17}
\]

or the six-orbit inequality `Q(p,p)>=0` from (8).

The solved critical point and Corollary 4 show that the blocker is not local instability at `p=1/2`; Proposition 2 shows that a single all-connected-to-triple surgery is quantitatively insufficient; and the formal `epsilon=1` law shows that FKG/noncrossing/detour sign are not enough without finite-energy geometry.

The next report must therefore diagnose, rather than immediately attack, which additional realizability inequality for the punctured-lattice orbit law could force (16), identify the simplest unresolved parameter subinterval/case, and select exactly one recovery action plus three new Section-B methods.

## 7. Source/current-literature status, 2026-09-18

Primary source retained: Alberto M. Campos and Bernardo N. B. de Lima, *The probability of connection between two vertices cannot be monotone with the distance for Bernoulli Percolation on transitive graphs*, arXiv:2601.00291v1 (submitted 2026-01-01).  The current arXiv record still has only v1 and its abstract/introduction still states the square-lattice monotonicity question as open.

Relevant earlier partials retained:

- de Lima--Procacci--Sanchis, arXiv:1504.06549: ordinary two-point monotonicity for sufficiently small `p`, high-density monotonicity only for the truncated connectivity function;
- Koenig--Richthammer, arXiv:2207.13173 / SPA 181 (2025): eventual layer monotonicity for finite transverse `G x Z`, not the `n=1` square-lattice endpoint and not a width-uniform theorem.

A bounded fresh title/question/author search on 2026-09-18 did not surface a later exact all-`p`, all-`n` square-lattice solution.  This is negative evidence only, not a novelty or openness certificate.  Publication novelty of the new identities and inequalities above remains **UNVERIFIED**.
