# G0008 — primal/dual detour conservation and an exact scalar-duality no-go certificate

Target: Campos--de Lima square-lattice axis-connectivity monotonicity, first milestone
\[
\tau_1(p)\ge \tau_2(p)\qquad(0<p<1).
\]
Status of this artifact: **PARTIAL**. It does not settle the source problem. It executes the STUCK1 recovery action by identifying the exact planar-dual scalar conservation law and then proving that this scalar law, even augmented by the previously established FKG and finite-energy constraints and the correct subcritical/supercritical detour signs, is still insufficient to force the first-step sign.

## 1. Setup retained from the cumulative R7-06 proof

Let
\[
x=(0,0),\qquad y=(1,0),\qquad z=(2,0),\qquad q=1-p.
\]
Let
\[
\tau_n(p)=\mathbb P_p(0\leftrightarrow ne_1).
\]
The previous R7-06 reductions proved
\[
\tau_1(p)-\tau_2(p)=qF(p),
\]
where, after deleting the whole four-edge star at `y`, the induced noncrossing partition of the neighbours
\[
x,u,z,d
\]
has six `D_4` orbit masses per specified partition
\[
\theta_p=(\sigma_p,\alpha_p,\beta_p,\gamma_p,\delta_p,\epsilon_p)
\]
with orbit sizes `(1,4,2,2,4,1)`, and
\[
\begin{aligned}
F(p)={}&p\sigma_p+2p(3-2p)\alpha_p+(2p-1)\beta_p\\
&+2p(1-p)(2-p)\gamma_p\\
&+(2p^3-7p^2+8p-2)\delta_p-(1-p)^3\epsilon_p.
\end{aligned}
\tag{1}
\]
The frozen source metric moves to `M_axis>=1` exactly when (1) is proved nonnegative for every `p`.

## 2. B18 — translate the missing information into the planar dual edge-detour law

### Idea

The STUCK1 diagnosis proposed a primal/dual boundary-partition lift. The first thing to check is what planar duality actually does to the punctured-star law. The correct dual object is not another copy of the same six-orbit law: **deletion in the primal becomes wiring/contraction in the dual**. This is the first gluing correction.

Let `e=xy` and let `e*` be its dual edge. Define the nearest-neighbour detour probability
\[
D(p):=\mathbb P_p\bigl(x\leftrightarrow y\text{ in }\mathbb Z^2\setminus\{e\}\bigr).
\tag{2}
\]
Equivalently, this is the source quantity
\[
\mathbb P_p(x\leftrightarrow y\mid e\text{ closed}).
\]

### Theorem 2.1 — exact edge-detour duality

For every `0<p<1`,
\[
\boxed{D(p)+D(1-p)=1.}
\tag{3}
\]

### Proof

Fix an edge configuration on all primal edges except `e`, and declare a dual edge open exactly when the crossed primal edge is closed. Standard planar edge-duality gives the following deterministic dichotomy: exactly one of

1. the endpoints `x,y` of `e` are joined by a primal-open path avoiding `e`;
2. the endpoints of `e*` are joined by a dual-open path avoiding `e*`.

This is the local cycle/cut form of planar duality: adding `e` creates a primal open cycle exactly when the complementary dual configuration has no `e*`-avoiding connection between the two faces adjacent to `e`. The two alternatives are mutually exclusive by planarity and exhaustive by the finite planar cycle-cut theorem; passage to `Z^2` follows by exhaustion (the event itself is a union of finite-path events).

Under Bernoulli(`p`) primal percolation, the dual-open edges are i.i.d. Bernoulli(`q`) with `q=1-p`. The square lattice is isomorphic to its dual, and the dual deleted-edge geometry `Z^2*\{e*}` is a translated/rotated copy of `Z^2\{e}`. Therefore the probability of alternative 2 is exactly `D(q)`. Taking probabilities in the deterministic dichotomy proves (3). QED.

This all-parameter identity is the natural extension of the source paper's critical observation `D(1/2)=1/2`.

### Why the naive four-terminal Kreweras identification fails

Let `K` be the graph obtained by deleting **all four** primal edges incident to `y`, as in the six-orbit reduction. In the dual configuration, those four deleted/fixed-closed primal edges correspond to four fixed-open dual edges. These four dual edges form the boundary cycle around the dual face corresponding to `y`; hence their four dual boundary vertices are wired into one cluster.

Thus the dual of the punctured-star law `theta_p` is a **wired** boundary law, not the free punctured-star law `theta_{1-p}`. In particular, there is no valid identity obtained by simply applying a Kreweras complement to `theta_p` and equating it with `theta_{1-p}`. Any recovery argument that does that silently confuses deletion with deletion rather than the correct deletion/contraction duality.

That is the exact structural reason the critical one-edge self-duality does not automatically upgrade to six orbit-by-orbit identities off criticality.

## 3. B12 — conserved scalar in the paired `p` / `1-p` orbit laws

### Idea

Although the whole punctured-star law does not self-dualize, the single-edge detour event does. Express `D(p)` exactly through `theta_p`; then (3) becomes a conserved scalar coupling the two six-orbit laws.

For a punctured-star configuration `K`, let
\[
m_x\in\{0,1,2,3\}
\]
be the number of vertices among `{u,z,d}` lying in the `K`-cluster of `x`.
After restoring the three remaining edges from `y` independently with probability `p` while keeping `xy` closed, `y` fails to connect to `x` iff all star edges from `y` to members of the `x`-cluster are closed. Therefore
\[
1-D(p)=\mathbb E_p[q^{m_x}].
\tag{4}
\]

Summing `q^{m_x}` over each `D_4` orbit yields the exact coefficients
\[
1,\quad 2(1+q),\quad 1+q,\quad 2q,\quad 1+3q^2,\quad q^3.
\]
Hence define
\[
\boxed{
L_p(q):=
\sigma_p+2(1+q)\alpha_p+(1+q)\beta_p+2q\gamma_p
 +(1+3q^2)\delta_p+q^3\epsilon_p.
}
\tag{5}
\]
Then
\[
\boxed{D(p)=1-L_p(q).}
\tag{6}
\]
Combining (3) and (6) gives the promised conserved paired functional:
\[
\boxed{L_p(1-p)+L_{1-p}(p)=1.}
\tag{7}
\]
At `p=1/2`, (7) specializes to
\[
L_{1/2}(1/2)=1/2,
\]
which is exactly the scalar identity used in the previous critical proof, written before eliminating orbit variables.

Equation (7) is therefore the strongest scalar conservation law supplied by the nearest-neighbour duality, and it is valid for every `p`.

## 4. B27 — swap the quantifiers and test whether the paired scalar law can force the first-step signs

### Idea

The STUCK1 recovery proposed proving the `p` and `q=1-p` statements simultaneously. Before seeking a proof, test whether the currently known necessary constraints plus (7) even logically imply `F(p)>=0`. If they do not, the scalar recovery route is exhausted and the missing dual input must be genuinely multi-terminal.

Besides nonnegativity and normalization, retain the two strongest necessary one-law constraints already proved in R7-06:

1. **opposite-connection FKG**
\[
\epsilon\ge T^2,
\qquad T:=\beta+2\delta+\epsilon;
\tag{8}
\]
2. **finite-energy leaf surgery**
\[
\delta_p\ge {q^3\over2}\epsilon_p.
\tag{9}
\]
For the reflected `q` law, (9) becomes
\[
\delta_q\ge {p^3\over2}\epsilon_q.
\tag{10}
\]
Also impose the source-valid detour-threshold direction: below `1/2`, `D(p)<p`, and above `1/2`, `D(q)>q`.

### Proposition 4.1 — exact paired relaxed no-go certificate

Take
\[
p={1\over3},\qquad q={2\over3}.
\]
Consider the following **formal** `D_4`-symmetric noncrossing orbit laws:
\[
\boxed{
\theta_p=\left({1\over4},0,{7\over40},0,{3\over80},{1\over4}\right),
}
\tag{11}
\]
and
\[
\boxed{
\theta_q=\left(0,0,0,{14989\over34560},{79\over34560},{79\over640}\right).
}
\tag{12}
\]
They satisfy all of the following exactly:

- orbit-weighted normalization
\[
\sigma+4\alpha+2\beta+2\gamma+4\delta+\epsilon=1;
\tag{13}
\]
- the paired dual conservation law (7):
\[
L_p(q)={1519\over2160},
\qquad
L_q(p)={641\over2160},
\qquad
L_p(q)+L_q(p)=1;
\tag{14}
\]
- the correct detour-threshold directions:
\[
D(p)={641\over2160}<{1\over3},
\qquad
D(q)={1519\over2160}>{2\over3};
\tag{15}
\]
- opposite-connection FKG (8): for the `p` law,
\[
T_p={1\over2},\qquad \epsilon_p-T_p^2=0,
\tag{16}
\]
while for the `q` law,
\[
T_q={553\over4320},
\qquad
\epsilon_q-T_q^2={1997831\over18662400}>0;
\tag{17}
\]
- the finite-energy leaf bounds (9)--(10):
\[
\delta_p-{q^3\over2}\epsilon_p={1\over2160}>0,
\qquad
\delta_q-{p^3\over2}\epsilon_q=0.
\tag{18}
\]

Nevertheless the first-step brackets are
\[
\boxed{F(p)=-{109\over2160}<0,}
\tag{19}
\]
while
\[
F(q)={14831\over58320}>0.
\tag{20}
\]

### Consequence

The conjunction of

- noncrossing `D_4` orbit normalization,
- exact primal/dual nearest-neighbour detour conservation,
- correct subcritical/supercritical detour signs,
- the available opposite-pair FKG inequality, and
- the available finite-energy leaf-surgery inequality

**does not imply** the desired first-step sign at each parameter.

The laws (11)--(12) are not asserted to be realizable as actual punctured Bernoulli-percolation laws. Their role is sharper: they are an exact separation certificate proving that the STUCK1 scalar paired-duality relaxation is logically too weak. Therefore any successful primal/dual recovery must use additional **multi-terminal realizability information**, not merely the scalar edge-detour invariant.

## 5. Exact finite verification

The rational certificate (11)--(20) was checked with exact `fractions.Fraction` arithmetic in

`research7_2026-09-17/R7-06/artifacts/2026-09-18/2026-09-18T072700Z__G0008_dual_pair_no_go_checker.py`

with archived output

`research7_2026-09-17/R7-06/artifacts/2026-09-18/2026-09-18T072700Z__G0008_dual_pair_no_go_checker.out`.

The executed output terminates with

`ALL_EXACT_CHECKS_PASS`.

## 6. What was learned and exact remaining blocker

The STUCK1 recovery action has now been executed far enough to separate valid from invalid primal/dual information:

1. the valid all-parameter dual conservation is the one-dimensional identity (7);
2. deleting the whole primal star does **not** yield the same punctured dual law, because the dual boundary cycle is wired;
3. even after adding the strongest currently available one-law FKG and finite-energy inequalities plus the correct detour-threshold signs, the scalar paired relation does not force `F(p)>=0`.

So the missing ingredient can now be stated more narrowly:

> Find a genuinely multi-terminal deletion/contraction duality inequality for the actual punctured square-lattice partition law which excludes the exact relaxed pair (11)--(12) and, when combined with (1), forces `F(p)>=0`.

A future successful route must see more than the single random variable `m_x`; it must retain enough joint boundary information to distinguish actual Bernoulli realizability from the relaxed orbit cone.

## 7. Source / literature status checked 2026-09-18

Primary source: Alberto M. Campos and Bernardo N. B. de Lima, *The probability of connection between two vertices cannot be monotone with the distance for Bernoulli Percolation on transitive graphs*, arXiv:2601.00291. The current arXiv record still exposes v1 (submitted 2026-01-01) and still explicitly calls square-lattice distance monotonicity open.

Nearest external analogue retained: Philipp Koenig and Thomas Richthammer, *Monotonicity properties for Bernoulli percolation on layered graphs -- a Markov chain approach*, arXiv:2207.13173 / SPA 181 (2025), which proves eventual monotonicity for finite transverse layered graphs, not the `n=1` infinite-width square-lattice endpoint.

For the deterministic local duality dichotomy, a standard statement appears as Proposition 9.1.1 in lecture notes *An introduction to percolation*: for a planar edge and its dual, after deleting the two corresponding edges, either the primal endpoints are connected by an open path or the dual endpoints are connected by an open dual path. The argument above uses precisely this local cycle/cut duality.

A bounded fresh search on 2026-09-18 did not expose a later all-`p`, all-`n` square-lattice resolution. This remains negative evidence only; no novelty claim is made.
