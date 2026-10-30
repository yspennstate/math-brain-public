# B16 FEI signed transport: a T-join normal form on the actual disagreement cut

**Status:** full Fourier Entropy--Influence remains **OPEN / NOT PROVED**.  
**Run scope:** fleet03 / B16, `FEI signed transport proof`.  
**Brain status:** **WITHOUT_VERIFIED_BRAIN**. No genuine mathematical/cognitive-brain retrieval was used in this derivation.  
**Research snapshot recovered:** `yspennstate/math-open-problems` master `95fd9990ddf7a86743471394706c724fa092678a` for the complete pre-fleet P03 state, followed by the live 21 September continuation and concurrent fleet head.  
**No novelty claim:** the lemmas below are new derivation/proof-state progress in this repository; publication novelty has not been established.

## 0. Exact entering state and what is not being repeated

The recovered P03 chain still has the exact half-band compiler identity

\[
H_{\rm nat}(f)=\kappa_2J(f)-\mathcal B_d+\mathcal Q_{d,<2}+R_d(f),
\qquad \mathcal B_d\ge0,
\]

with the R16 alternating high-resolvent bank retaining odd collision-order refunds, and the R32 truth-table identity

\[
H_{\rm nat}(f)-R_d(f)
=\frac8N\sum_{\substack{A\in C_0\setminus D_d\\f_A=-1}}
(-1)^{|A|/2}I_{|A|,N}. \tag{0.1}
\]

Here `C_0=RM(1,n)^perp`, so every relation `A` has even cardinality and `xor_{x in A} x=0`; `D_d` is retained exactly; the `0 mod 4` terms are debits and the `2 mod 4` terms are genuine negative credits. The terminal theorem is only a **net signed endpoint** theorem. The current Borel form is likewise retained:

\[
\mathfrak G_d(s)=2N\sum_{\substack{A\in C_0\setminus D_d\\f_A=-1}}
(-1)^{|A|/2}\sin^{|A|}(s/N)\cos^{N-|A|}(s/N),
\qquad
H_{\rm nat}(f)-R_d(f)=4\int_0^\infty \mathfrak G_d(s)\frac{ds}{s^3}. \tag{0.2}
\]

The newer exact first-moment occupation theorem proves total positive leakage at most `J`, but the bent-phase counterexample kills a gatewise lift from instantaneous leakage to nonlinear entropy. The square-root/Fourier-l1 comparator route is also killed; the valid scalar min-log bound has the right support-birth scale but does not by itself control old-support signed response. Earlier adjacent-shell physical q-flip transports pay fixed shells but have a growing-shell/premode obstruction and cannot be promoted to a universal proof.

The 21 September owner continuation was also recovered before finalizing this note: the read-once theorem `H<=6.4573 I`, the numerical sharp read-once value near Hod's `beta(1/2)=6.4547837`, and the fourteen current route suggestions. This run does **not** audit or re-run that certificate. It takes a different route aimed directly at (0.1).

The new route is:

> **Route 15 -- signed T-join disintegration on the monochromatic quotient.** Express every frustrated affine relation by an exact physical edge chain, contract all zero-cost monochromatic geometry, symmetrize the multiplicative telescoping identity so relation mass is routed with no path-length loss, and leave the R32 signs untouched. The remaining universal obligation becomes a signed congestion problem on the *actual influence cut graph*.

This is not the killed physical downward-edge/q-flip route: it uses arbitrary global T-joins, all relation weights simultaneously, and never positive-parts the signed shell sum.

---

## 1. Physical notation

Work after the one legitimate minimizing-character gauge and rename the gauged function `f`. Let

\[
Q_n=(V,E),\qquad V=\mathbb F_2^n,\qquad N=2^n,
\]

and let

\[
\mathcal D_f=\{\{x,x+e_i\}\in E:f(x)f(x+e_i)=-1\}
\]

be the undirected physical disagreement edges. Then

\[
J(f)=I(f)=\frac{2|\mathcal D_f|}{N}. \tag{1.1}
\]

For an even vertex set `A`, an **A-join** is an edge set `T subset E` whose odd-degree boundary is exactly `A`:

\[
\partial T=A.
\]

Such a join exists in the connected cube whenever `|A|` is even.

---

## 2. `P03-B16-DIRECTION-EVEN-TJOIN` -- PROVED

### Theorem 2.1

If `A in C_0` and `T` is any A-join in the physical cube, then every original coordinate direction occurs an even number of times in `T`.

### Proof

For an edge `e={x,x+e_i}`, write `dir(e)=e_i`. Over `F_2^n`,

\[
\bigoplus_{v\in\partial T}v
=
\bigoplus_{\{x,y\}\in T}(x\oplus y)
=
\bigoplus_{e\in T}\operatorname{dir}(e). \tag{2.1}
\]

The first equality holds because each vertex of even degree appears an even number of times and cancels. Since `A in C_0`,

\[
\bigoplus_{v\in A}v=0.
\]

Thus the direction-parity vector on the right of (2.1) is zero. Equivalently, the number of used edges in each physical coordinate is even. `□`

This keeps the dual-code relation constraint in original-cube geometry; it is not a shell surrogate.

---

## 3. `P03-B16-FRUSTRATION-CROSSING-PARITY` -- PROVED

### Theorem 3.1

For any even `A`, any A-join `T`, and any Boolean `f`,

\[
\boxed{\prod_{e=\{u,v\}\in T}f(u)f(v)=f_A:=\prod_{x\in A}f(x).} \tag{3.1}
\]

Consequently, if `f_A=-1`, then

\[
d_f(T):=|T\cap\mathcal D_f|
\]

is a positive odd integer.

### Proof

In the product over edges, a vertex `v` occurs `deg_T(v)` times. Even degrees disappear because `f(v)^2=1`; precisely the odd-degree boundary remains, giving (3.1). Every disagreement edge contributes `-1` and every agreement edge `+1`, so `f_A=(-1)^{d_f(T)}`. `□`

Thus every frustrated relation is forced to touch the actual influence cut, and it does so an odd number of times. No union bound has been used.

---

## 4. `P03-B16-SYMMETRIZED-SIGNED-TELESCOPE` -- PROVED

The next point removes a path-length loss that appears if one simply union-bounds all physical edges of a relation chain.

Let `T={e_1,...,e_L}` be an A-join and put `tau_e=f(u)f(v)`. For any ordering `sigma` of `T`, the exact multiplicative telescope is

\[
\frac{1-\prod_{e\in T}\tau_e}{2}
=
\sum_{r=1}^L
\frac{1-\tau_{\sigma(r)}}2
\prod_{q<r}\tau_{\sigma(q)}. \tag{4.1}
\]

If `f_A=-1`, the left side is one and `d=d_f(T)` is odd. Average (4.1) over all edge orderings. Agreement edges contribute zero. For a fixed disagreement edge, its relative rank among the `d` disagreement edges is uniform on `1,...,d`, hence its expected prefix sign is

\[
\frac1d\sum_{r=1}^d(-1)^{r-1}=\frac1d \qquad(d\ \text{odd}). \tag{4.2}
\]

Therefore

\[
\boxed{
1_{\{f_A=-1\}}
=
\sum_{e\in T\cap\mathcal D_f}\frac1{d_f(T)}.
} \tag{4.3}
\]

Equation (4.3) is the symmetrized form of the **signed** telescope, not an independent positive-part estimate. The alternating internal cancellations in (4.1) are exactly what remove the total path length: a relation crossing the cut `d=1,3,5,...` times still routes total mass one, not mass `d` and not mass `|T|`.

This is the first useful point of the new route: arbitrary long agreement geometry costs zero, and repeated disagreement crossings do not create a multiplicative congestion factor inside one relation.

---

## 5. `P03-B16-MONOCHROMATIC-QUOTIENT-TJOIN` -- PROVED

Delete the disagreement edges from the cube and contract each connected component. Call the resulting multigraph `G_f`. Its vertices are the monochromatic connected components of `f`; its edges are the *actual physical disagreement edges*. It is bipartite, with the `f=+1` and `f=-1` components as its two sides.

For a relation `A`, define a terminal parity on quotient components by

\[
t_A(C)=|A\cap C|\pmod2. \tag{5.1}
\]

Let `d_A` be the minimum number of physical disagreement edges among all A-joins in the cube.

### Theorem 5.1

`d_A` equals the minimum cardinality of a `t_A`-join in the quotient multigraph `G_f`.

### Proof

Project any cube A-join to its disagreement edges. Inside any monochromatic component, agreement edges contribute zero to the quotient. Parity of the projected degree at a component is exactly `|A cap C| mod 2`; hence the projection is a `t_A`-join. This gives one inequality.

Conversely, take any quotient `t_A`-join `J`, remembering the actual physical disagreement edge represented by every multiedge. In a monochromatic component `C`, the parity-defect set that remains after inserting the endpoints of `J` is

\[
(A\cap C)\triangle(\text{endpoints of }J\text{ in }C).
\]

Its cardinality is even because `deg_J(C)=t_A(C)` mod two. The component is connected using agreement edges, so this even defect set has an internal join made entirely of agreement edges. Do this independently in every component and unite those internal joins with `J`. The result is a cube A-join using exactly `|J|` disagreement edges. `□`

### Corollary 5.2 -- odd minimum

If `f_A=-1`, every quotient `t_A`-join, hence every minimum one, has odd cardinality. Indeed the parity of its number of edges is the sum of its degrees on the negative side of the bipartition,

\[
|J|\equiv\sum_{C:f|_C=-1}t_A(C)
\equiv |A\cap\{f=-1\}|\equiv1\pmod2. \tag{5.2}
\]

Thus `d_A` is a well-defined positive odd integer depending only on the genuine disagreement quotient, not on arbitrary cube path length.

---

## 6. `P03-B16-R32-EDGE-DISINTEGRATION` -- PROVED

For every frustrated relation

\[
A\in\mathcal R_d(f):=\{A\in C_0\setminus D_d:f_A=-1\},
\]

choose a minimum quotient `t_A`-join `J_A`. If several exist, any convex combination of them is allowed. For one chosen join define the probability distribution on physical disagreement edges

\[
\pi_A(e)=\frac{1_{\{e\in J_A\}}}{d_A},
\qquad e\in\mathcal D_f. \tag{6.1}
\]

By Sections 3--5,

\[
\pi_A(e)\ge0,\qquad \sum_{e\in\mathcal D_f}\pi_A(e)=1. \tag{6.2}
\]

Define the **integrated signed edge load**

\[
c_A=(-1)^{|A|/2}I_{|A|,N},
\qquad
W_e=\sum_{A\in\mathcal R_d(f)}c_A\pi_A(e). \tag{6.3}
\]

Then the exact R32 relation sum disintegrates as

\[
\boxed{
H_{\rm nat}(f)-R_d(f)
=\frac8N\sum_{e\in\mathcal D_f}W_e.
} \tag{6.4}
\]

The proof is just finite Fubini plus (6.2), but the structure is important: every original relation is retained with its exact multiplicity, exact terminal-code exclusion and exact sign. In particular, a `2 mod 4` relation contributes a **negative** edge load; it is not discarded or replaced by its magnitude.

Combining (6.4) with the exact compiler identity gives the equivalent small-resolvent statement

\[
\boxed{
\mathcal Q_{d,<2}-\mathcal B_d
=
\frac8N\sum_{e\in\mathcal D_f}W_e-\kappa_2J(f).
} \tag{6.5}
\]

Thus the R16 high-resolvent bank has not been spent twice or thrown away: it is still present in the equality relating the compiler ledger to the routed R32 sum.

### Borel version -- same physical routing at every scale

Using the same `pi_A`, independent of Borel time, define

\[
W_e(s)=2N\sum_{A\in\mathcal R_d(f)}
(-1)^{|A|/2}\pi_A(e)
\sin^{|A|}(s/N)\cos^{N-|A|}(s/N). \tag{6.6}
\]

Then for every `s`,

\[
\boxed{\mathfrak G_d(s)=\sum_{e\in\mathcal D_f}W_e(s).} \tag{6.7}
\]

Hence one geometric routing simultaneously disintegrates the whole Borel corridor. When the global sum is expanded in collision order, the inherited R16 odd-order refunds remain the same global negative coefficients. No claim is made that an individual edge carries a separately nonnegative R16 bank; only the exact global identity is asserted.

The terminal response `R_d` also remains separate. Nothing in this section infers cumulative variation from its bounded endpoint.

---

## 7. A precise conditional FEI closure criterion

Assume the inherited one-sided terminal payment at the chosen prefix is

\[
R_d(f)\le C_{\rm term}J(f). \tag{7.1}
\]

If the minimum-join choices can be made so that, for a universal finite `L`,

\[
\boxed{W_e\le L\quad\text{for every }e\in\mathcal D_f,} \tag{7.2}
\]

then, by (1.1) and (6.4),

\[
H_{\rm nat}(f)-R_d(f)
\le\frac8N L|\mathcal D_f|
=4LJ(f),
\]

and therefore

\[
\boxed{H_{\rm nat}(f)\le(4L+C_{\rm term})J(f).} \tag{7.3}
\]

After undoing the entropy-unit conversion and the character gauge this is FEI with a dimension-independent constant.

**Status of (7.2): OPEN.** This run does not prove a universal `L`. It isolates an exact, sign-preserving congestion theorem whose proof would suffice. The remaining obstacle is now *cross-relation signed congestion on the actual disagreement quotient*, not path length inside one relation.

---

## 8. `P03-B16-SIGNED-CONGESTION-LP-DUAL` -- PROVED

The routing freedom has an exact finite linear-program dual which makes the negative credits visible instead of hiding them in an absolute value.

For each frustrated `A`, let `J_A` be the finite set of minimum `t_A`-joins in `G_f`; every member has cardinality `d_A`. Let `x_{A,J}` be a probability distribution on `J_A`. The resulting load is

\[
W_e(x)=\sum_A c_A\sum_{J\in\mathcal J_A}x_{A,J}\frac{1_{\{e\in J\}}}{d_A}. \tag{8.1}
\]

Define

\[
L_*(f,d)=\min_x\max_{e\in\mathcal D_f}W_e(x). \tag{8.2}
\]

For a nonconstant gauged function `D_f` is nonempty. Finite-dimensional strong LP duality gives

\[
\boxed{
L_*(f,d)=
\max_{\substack{y_e\ge0\\\sum_e y_e=1}}
\left[
\sum_{A:c_A>0} c_A\min_{J\in\mathcal J_A}\frac1{d_A}\sum_{e\in J}y_e
+
\sum_{A:c_A<0} c_A\max_{J\in\mathcal J_A}\frac1{d_A}\sum_{e\in J}y_e
\right].
} \tag{8.3}
\]

### Proof

Use the primal constraints `W_e(x)<=L`, multipliers `y_e>=0`, and simplex constraints `sum_J x_{A,J}=1`. Minimizing the Lagrangian over unrestricted `L` forces `sum_e y_e=1`. For each relation independently, minimizing over its route simplex picks the minimum `y`-average when `c_A>0`; when `c_A<0`, multiplication by a negative coefficient reverses the choice and picks the maximum `y`-average. The feasible routing product is compact and the finite LP is feasible, so strong duality applies. `□`

This sign reversal is exactly what is wanted: in the dual, positive debit relations seek a cheap minimum T-join, while negative `2 mod 4` credits seek an expensive one and cancel load on the heavily taxed physical edges. Taking `|c_A|` would destroy this mechanism.

Equation (8.3) suggests the next mathematical target more sharply than a shellwise positive bound:

> For every probability tax `y` on the actual disagreement edges, compare the weighted cheapest debit T-joins with the weighted most expensive negative-credit T-joins, using the exact R32 radial weights and the R16/global moment refunds. Prove that the resulting signed functional is `O(1)` uniformly in `n,f,d` at the paid prefix.

A counterexample in which this dual value grows without bound would decisively kill this route.

---

## 9. Finite falsification check

A small exact checker was written separately at

`proofnet24/P03-fei/fleet-2026-09-21/fleet03/B16/2026-09-21__signed_tjoin_transport_check.py`.

It exhausts all 256 Boolean phases on `Q_3` and all 16 words of `C_0`, independently compares minimum disagreement-edge cube T-joins with minimum quotient T-joins, checks odd crossing parity and direction-evenness, and verifies exact conservation of arbitrary rational signed relation weights under the normalized edge routing. Current-run native evaluation covered **1,920 frustrated relation instances** and passed every assertion; the largest minimum disagreement T-join seen was three. The saved output is

`proofnet24/P03-fei/fleet-2026-09-21/fleet03/B16/2026-09-21__signed_tjoin_transport_check_output.json`.

This finite check is only a falsification/sanity test for the proved identities. It is not evidence for the open uniform congestion bound (7.2).

---

## 10. Why this is not a killed shortcut

This route deliberately avoids the failures already in the P03 ledger:

- no positive-part replacement of the R32 sum;
- no absolute-value replacement of the odd R16 collision refunds;
- no inference from a bounded terminal endpoint to bounded intermediate turnover;
- no adjacent-shell-only q-flip requirement;
- no downward-edge-only payment;
- no instantaneous-leakage-to-Shannon lift;
- no Fourier-l1/square-root comparator surrogate;
- no dimension factor from physical path length.

The exact relation-code support, original physical coordinates, relation multiplicity, shell sign, Borel radial weight, compiler bank, and terminal residual are all retained.

---

## 11. Precise residual obligation and next attack

**PROVED in this run:** the direction-even T-join geometry; the frustration/odd-crossing identity; the symmetrized no-path-length telescope; exact contraction to the monochromatic quotient; exact integrated and Borel R32 edge disintegration; and the finite signed-congestion LP dual.

**OPEN:** a universal bound on `L_*(f,d)` at a prefix with the inherited terminal payment, or a bank-assisted equivalent that keeps the R16 moment refunds global and avoids double spending.

The next B16 run on this route should attack the dual (8.3), not re-run the Q3 checker. The most concrete first target is a cut-tax reduction: characterize an extreme or near-extreme `y` on `G_f` and prove that whenever a positive relation is forced through a heavily taxed quotient cut, either an exact `2 mod 4` relation family supplies comparable negative routed mass on the same cut or the corresponding first-separator/collision deposit is already present in the R16 bank. That is where dual-code multiplicity and moment refunds can interact without taking absolute values.

Current primary literature checked during the run still describes the unrestricted FEI assertion as a conjecture; in particular González--MacManus--Pereyra, arXiv:2606.00246 (29 May 2026), proves additional classes/stopping-tree results rather than a universal resolution. This is only an open-status/prior-art check, not a novelty certificate for the T-join formulation.
