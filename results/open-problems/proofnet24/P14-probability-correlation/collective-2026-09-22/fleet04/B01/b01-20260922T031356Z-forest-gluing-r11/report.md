# FOREST / fleet04 B01 — weighted equivalence, simultaneous theta compilation, and exact 3-connected gluing

**Run:** `b01-20260922T031356Z-forest-gluing-r11`  
**Candidate version:** `FOREST-WEIGHTED-3CONN-EQUIVALENCE-v1`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent Grimmett–Winkler target:** **OPEN**  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact target, lead state, and peer results actually used

For a finite simple graph `G=(V,E)` and positive edge weights `y`, let

`P_G(y)=sum_{F acyclic} product_{h in F} y_h`.

For distinct edges `e,f`, write

`Delta_G(e,f;y)=P_e P_f-P_G P_ef`.

At unit weights this is exactly `Z_e Z_f-Z Z_ef`, so the source target is `Delta_G(e,f;1)>=0` for every finite simple `G` and every distinct pair. All forest sizes, disconnected forests and the empty forest remain present.

I read the latest complete team-lead candidate, fleet01/B01 `FOREST-KN-HERMITE-REDUCTION-v1`, report blob `e11be369a70e59449ea744da6f1e32040889c216`. Its self-contained Hermite calculation proves the **unit-weight** source inequality on every complete graph `K_n`. I also read the assigned partner fleet01/B02 switching audit, report blob `d424fe91d8889c03961de3e9de6a8a9c994f57e2`, which independently rederives the complete-graph marked-edge enumeration and Hermite positivity.

The global closure in the lead candidate is not treated as established. Fleet02/B02 correction blob `733d840093ca109d38f4e336d228ae1ddedf77c0` records a source-scope conflict: the accessible Cocks mechanism is class-level through parallel copies, while a final Semple–Welsh note has stronger fixed-graph wording. I therefore do not use the disputed implication `unit on one fixed G => all positive weights on the same G`.

The named **OTHER-account result consumed and applied** is fleet03/B03 `fleet03-b03-20260922T015800Z-forest-r11`, report blob `e76cd27787722e1b80e6e5edb657f45ebe50ec49`. It proves the exact two-terminal response `k/(2^ell-1)` for `k` internally disjoint length-`ell` paths, proves those responses are dense in `(0,infinity)`, and uses the earlier two-separator identity to compile one bad virtual-edge weight into a genuine finite simple unit-weight counterexample. I extend that one-edge compilation simultaneously to **every edge of a weighted graph** and then apply it to make the all-parameter separator induction legitimate.

## 2. Compact conditional end-to-end argument

This run proves the following equivalence theorem.

> **Theorem A (weighted/3-connected/complete equivalence).** The following statements are equivalent.
>
> 1. Every finite simple graph is pairwise negatively correlated under the **unit** uniform law on all forests.
> 2. Every finite simple graph is Rayleigh for its forest polynomial at **every positive edge-weight vector**.
> 3. Every finite simple **3-vertex-connected** graph is Rayleigh for its forest polynomial at every positive edge-weight vector, with the graphs on at most three vertices handled as base cases.
> 4. Every complete graph `K_n` is Rayleigh for its forest polynomial at every positive edge-weight vector.

Thus the lead's proved unit `K_n` theorem is a genuine strong piece, but the exact first unpaid implication is now clean:

> **Missing implication:** prove the forest Rayleigh inequality on `K_n` for **arbitrary positive edge weights**, not only at the all-ones point.

That statement is not merely a convenient strengthening: by Theorem A it is equivalent to the original all-simple-graphs source conjecture.

The proof of Theorem A occupies §§3–6.

## 3. Exact network substitution and simultaneous compilation of arbitrary positive weights

### 3.1 Two-terminal substitution identity

For each edge `h={u,v}` of a simple base graph `G`, replace `h` by a finite simple two-terminal network `N_h`; all internal vertices of different networks are disjoint, and different networks meet only at their original base endpoints. For `N_h`, let

- `D_h` be the forest polynomial sum over forests in which `u,v` are disconnected;
- `C_h` be the sum over forests in which `u,v` are connected;
- `r_h=C_h/D_h`.

Every local forest configuration records a base edge `h` exactly when its terminals are connected. The union of the local forests is acyclic **iff** the recorded base-edge set is acyclic: a cycle in the union contracts to a cycle of recorded base edges, and a recorded base cycle lifts through the unique terminal paths inside the local forest components. Therefore

`P_H = (product_h D_h) P_G(r)`.

This is an exact identity, not an independence approximation.

Now let `a` be an edge inside `N_e` and `b` an edge inside `N_f`, where `e != f`. Define local marked-edge responses

`S_e(a)=D_e C_{e,a}-C_e D_{e,a}`,

`S_f(b)=D_f C_{f,b}-C_f D_{f,b}`.

Differentiating the factorization above with respect to `a` and `b`, all derivative terms coming from the prefactor cancel in the Rayleigh difference. One obtains the exact sign-transfer formula

`Delta_H(a,b) = K^2 [S_e(a)/D_e^2] [S_f(b)/D_f^2] Delta_G(e,f;r)`,

where `K=product_h D_h`.

### 3.2 Positive marked response of the theta gadgets

Take `N=N(k,ell)` to be `k>=1` internally vertex-disjoint `u-v` paths of common length `ell>=2`. Put `d=2^ell-1`. Fleet03/B03 gives

`D=d^k`, `C=k d^(k-1)`, hence `r=k/d`.

For completeness, the sign needed in the new simultaneous substitution is explicit. Mark one edge `a` on one path and give that edge variable weight `x`, all other local edges weight one. For the marked path,

`D_path(x)=2^(ell-1)+(2^(ell-1)-1)x`, `C_path(x)=x`.

Parallel composition of the `k` paths gives

`D(x)=D_path(x)d^(k-1)`,

`C(x)=x d^(k-1)+(k-1)D_path(x)d^(k-2)`.

At `x=1`, direct cancellation yields

`S(a)=D C_a-C D_a = 2^(ell-1) d^(2k-2) > 0`.

So the substitution preserves the sign of the base Rayleigh difference.

### 3.3 Simultaneous theta compilation theorem

Suppose a finite simple weighted graph `G` has a bad positive weight vector `w` and marked edges `e,f` with

`Delta_G(e,f;w)<0`.

Because the forest polynomial is a finite polynomial, `Delta_G(e,f;y)` is continuous in all edge weights. Hence it remains negative in some open neighbourhood of `w`.

For every edge `h`, independently choose a theta response

`r_h=k_h/(2^(ell_h)-1)`

inside that neighbourhood; the density of these responses is the fleet03/B03 theorem cited above. Replace **every** base edge by its chosen theta network, using fresh internal vertices. The resulting graph `H` is finite and simple because every path has length at least two and the base graph itself is simple. Choose one marked internal edge in the theta network replacing `e` and one in the network replacing `f`.

The factorization and positive-response formula imply

`Delta_H(a,b)<0`.

All edges of `H` have unit weight, so `H` is a genuine source-model counterexample: finite, simple, unrooted, all forest sizes included.

Therefore

`unit pNC for every finite simple graph  <=>  positive-weight Rayleigh for every finite simple graph`.

The reverse implication is simply specialization to weight one. This establishes `(1) <=> (2)` in Theorem A without any Cocks fixed-graph upgrade.

## 4. Exact all-parameter gluing across a 2-vertex separator

I now work entirely in the equivalent positive-weight problem, so virtual separator weights are legitimate induction parameters rather than an unpaid strengthening.

Let a 2-connected simple graph `G` have a 2-vertex cut `{u,v}`. Its `uv`-bridges are the edge-disjoint subgraphs induced by the components of `G-{u,v}` together with their incident edges; if the edge `uv` itself is present, treat it as an additional singleton bridge. For bridge `B_i`, define positive-weight forest sums `D_i,C_i` according as `u,v` are disconnected or connected, and put `r_i=C_i/D_i`.

A global forest can have **at most one** bridge connecting `u` to `v`, because two such connecting bridge paths would form a cycle. Conversely, choosing disconnected local forests in every bridge, or choosing exactly one connected local forest, is always globally acyclic iff each local choice is. Hence

`P_G = product_i D_i + sum_i C_i product_{j!=i}D_j`

or equivalently

`P_G=(product_i D_i)(1+sum_i r_i)`.

This includes any singleton original `uv` edge exactly; no parallel virtual edge is introduced into that singleton bridge.

### 4.1 Both marked edges in one bridge

Suppose `e,f` both lie in `B_i`. Set

`D_out=product_{j!=i}D_j`,

`lambda_i=sum_{j!=i} C_j/D_j > 0`.

Let `H_i=B_i+g_i`, where `g_i` is a new virtual `uv` edge of weight `lambda_i`. Because an original `uv` edge, if present, is its own singleton bridge, `H_i` is simple. Its forest polynomial is

`P_{H_i}=D_i+C_i+lambda_i D_i`.

The global polynomial is `P_G=D_out P_{H_i}`, so

`Delta_G(e,f)=D_out^2 Delta_{H_i}(e,f)`.

This is the requested all-parameter same-bridge transfer.

### 4.2 Marked edges in different bridges

Suppose `e in B_i` and `f in B_j`, `i!=j`. Put

`D_rest=product_{k notin {i,j}}D_k`

and define

`R_i(e)=D_i C_{i,e}-C_i D_{i,e}`,

`R_j(f)=D_j C_{j,f}-C_j D_{j,f}`.

Differentiating the global bridge formula gives a complete cancellation of every other bridge response:

`Delta_G(e,f)=D_rest^2 R_i(e)R_j(f)`.

For a non-singleton bridge `B_i`, add a virtual edge `g_i=uv` of any positive weight. Then

`Delta_{B_i+g_i}(e,g_i)=R_i(e)`;

the right side is independent of the chosen positive weight of `g_i`. For a singleton original `uv` bridge with marked edge `e`, one has `D_i=1`, `C_i=y_e`, `D_{i,e}=0`, `C_{i,e}=1`, so

`R_i(e)=1`.

Thus the singleton separator-edge case is completely explicit rather than hidden behind a parallel-edge intermediate.

## 5. Induction to the 3-connected core

Assume the positive-weight forest Rayleigh inequality is known for all smaller simple graphs. I use edge count as the induction measure, with trivial small graphs as bases.

- If `G` is disconnected, its forest polynomial factors over connected components. A marked pair in different components has Rayleigh difference zero; a pair in one component reduces to that component.
- If `G` has a cut vertex, its forest polynomial factors over the 1-sum pieces for the same reason: cycles cannot cross a one-vertex join. Again cross-piece pairs have difference zero, and same-piece pairs reduce to a smaller graph.
- Trees have a product forest polynomial and zero pairwise Rayleigh differences. For the triangle with positive edge weights `a,b,c`,
  `P=1+a+b+c+ab+ac+bc`, and `Delta(a,b)=c(1+c)>0`, cyclically; these cover the only small 2-connected base that matters.

Now suppose `G` is 2-connected but not 3-vertex-connected, and choose a 2-cut `{u,v}`. Since it is a genuine vertex cut, `G-{u,v}` has at least two components, hence at least two non-singleton `uv`-bridges. Each such bridge attaches to both terminals in a 2-connected graph, so it contains a `u-v` path and at least two edges. Therefore, for every non-singleton bridge `B_i`, the augmented simple graph `B_i+g_i` has strictly fewer edges than `G`.

For same-bridge marked pairs, §4.1 reduces the sign to the smaller weighted simple graph `B_i+g_i`. For cross-bridge pairs, §4.2 reduces the sign to the product of two response factors, each either `1` for a singleton separator edge or the Rayleigh difference of a smaller augmented simple graph. Every factor is nonnegative by induction.

Hence every weighted simple counterexample has a smaller weighted simple counterexample unless it is 3-vertex-connected. This proves `(3) => (2)`; the converse is immediate.

**Important scope correction:** this does **not** say that a lexicographically minimal *unit-weight* counterexample itself must be 3-connected. The old argument needed an unjustified fixed-graph unit-to-weight upgrade at its virtual edge. What is proved is the correct equivalent statement: if the original unit conjecture fails anywhere, then by §3 there exists a positive-weight counterexample, and by the weighted separator induction there exists a positive-weight 3-connected counterexample.

## 6. Complete graphs are an equivalent all-parameter target

`(2) => (4)` is immediate. Conversely, assume every `K_n` is Rayleigh at every positive edge-weight vector. Let `G` be any finite simple graph on `n` vertices with arbitrary positive weights on its present edges. Regard it as `K_n` by assigning every missing edge a common weight `epsilon>0`, while retaining the desired weights on present edges. The assumed complete-graph theorem gives

`Delta_{K_n}(e,f;y(epsilon))>=0`

for every `epsilon>0`. Since `Delta` is a polynomial in the edge weights, letting `epsilon -> 0` gives exactly

`Delta_G(e,f;y)>=0`.

Thus `(4) => (2)`.

Combining §§3–6 establishes all equivalences in Theorem A.

## 7. What this does to the current lead candidate

The complete-graph Hermite theorem in `FOREST-KN-HERMITE-REDUCTION-v1` remains intact: it proves the all-ones point of `K_n` for every `n`, and fleet01/B02 independently rederived that calculation.

The global fixed-graph Cocks step is no longer needed for this run's structural theorem, and the source disagreement about that citation cannot be used to promote the parent conjecture. Theorem A instead identifies the exact mathematical debt:

`unit K_n theorem (proved by lead)`

`--> MISSING: arbitrary positive weights on K_n`

`<=> full source conjecture on all simple graphs`.

Equivalently, the search for a source counterexample may be redirected to either a positive-weight complete graph or a positive-weight 3-connected simple graph; any such weighted failure can then be compiled by §3 into a genuine simple unit-weight source counterexample.

This is a materially stronger use of fleet03/B03's response-realization theorem than the previous one-virtual-edge argument and supplies the all-parameter gluing/three-connected step requested for this slot.

## 8. Exact computational regression

The proof above is symbolic. I ran a bounded exact-arithmetic checker only as regression evidence. It uses Python standard-library `Fraction` arithmetic and exhaustive forest enumeration for the finite fixtures.

Checker: `weighted_gluing_checker.py`  
SHA-256: `9440b5352095752d26b93440dc75e68934961b349f408b5c8f196df6f8f1e2a2`

Captured output: `weighted_gluing_checker.out`  
SHA-256: `5b878a6e180e88e57c50d0298596b6511d29f1a38531d4466e4809a46936f6b6`

Exact output:

```text
PASS theta_response_formula cases=4
PASS simultaneous_substitution_factorization delta=63504 base_delta=18/49
PASS two_cut_same_bridge lambda=5/2 delta=6300
PASS two_cut_cross_bridge R1=12 R2=1400/9 delta=5600/3
ALL_EXACT_CHECKS_PASS
```

The simultaneous-substitution fixture uses a weighted base triangle with theta responses `(2/3,1/7,2/7)` and checks the full derivative prefactor identity exactly. The separator fixture includes two nontrivial `uv` bridges and an original singleton `uv` edge, testing both the same-bridge virtual weight and the cross-bridge response factorization.

## 9. Status, failure retained, and next mathematical step

**Outcome:** `ESSENTIAL_STEP_APPLIED`.  
**FULL_PROOF_CANDIDATE:** false.  
**Parent target:** OPEN.  
**Source-valid counterexample found:** no.  
**Brain assistance:** none; `WITHOUT_VERIFIED_BRAIN`.

The failed/superseded route is preserved: I do not erase the earlier fixed-graph Cocks ambiguity or claim that unit minimality alone pays the virtual-weight separator gate. The new mechanism avoids that debt by proving the global unit/weighted equivalence first and then inducting within the weighted class.

The decisive next step for the team lead and partner is **not another separator lemma**. It is to attack arbitrary positive edge weights on `K_n` (equivalently, the positive-weight 3-connected obstruction). A successful extension of the Hermite argument must genuinely retain nonuniform weights; a proof only along the uniform radial line repeats the already-solved slice.

## 10. Source references

- Grimmett and Winkler, *Negative association in uniform forests and connected graphs*, source target (forest half, uniform all forests).
- Team lead fleet01/B01, `FOREST-KN-HERMITE-REDUCTION-v1`, report blob `e11be369a70e59449ea744da6f1e32040889c216`.
- Assigned partner fleet01/B02, switching/Hermite audit, report blob `d424fe91d8889c03961de3e9de6a8a9c994f57e2`.
- OTHER-account fleet03/B03, dense theta response and one-edge weighted-gate theorem, report blob `e76cd27787722e1b80e6e5edb657f45ebe50ec49`.
- Fleet02/B02 scope correction on the disputed Cocks fixed-graph inference, blob `733d840093ca109d38f4e336d228ae1ddedf77c0`.

No novelty claim is made from repository search, and no target-level truth promotion is requested by this report.
