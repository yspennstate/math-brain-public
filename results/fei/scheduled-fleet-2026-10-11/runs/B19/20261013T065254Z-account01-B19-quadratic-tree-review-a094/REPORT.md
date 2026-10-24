# B19 / A094 — independent review of the adaptive quadratic-control tree payment

Run: `20261013T065254Z-account01-B19-quadratic-tree-review-a094`  
Primary packet: **A094 (Proof-chain challenger)**  
Reviewed packet: **A023**  
Reviewed claim: `B05_A023_QUADRATIC_ADAPTIVE_TREE_v1`  
Verdict: **ACCEPTED_AT_DECLARED_SCOPE**  
Full FEI: **OPEN**

## 1. Review object and independence

This review examines the complete B05 package
`20261013T063352Z-account01-B05-quadratic-tree-payment-a023`, canonical package commit `0915f9264003de82c566d2c0cd03cb8844e33663`, verified receipt `d57b0469257027bfe0c084f3963ea467dc5359a3`. The reviewed theorem imports the coordinate lemma `B01_ALL_QUADRATIC_GU_v1` from B01 run `20261013T061836Z-account01-B01-all-quadratic-gu-a003`, report blob `460a47083324f194bb431650ab912c126f9894f2`, verified receipt `d829fca20536446e9855c0ce13be882b9beaf11a`.

I reconstructed the imported affine-coset lemma and the new adaptive tree argument from their statements. The submitted checker was read for scope only; `INDEPENDENT_REVIEW_CHECK.py` was written separately and does not call it. No proof repair or contribution to the reviewed theorem was made, so reviewer independence is preserved.

## 2. Accepted statement

Let \(q=(-1)^Q\) be any quadratic Boolean phase on a control block \(X\), let \(g\) be any Boolean function on a disjoint block \(Y\), and put \(F=qg\). Let \(T\) be any finite adaptive, possibly pruned, uniform restriction tree querying only controls. A physical coordinate may label multiple incomparable nodes but is never queried twice on a root-to-leaf path. If \(w_v\) is the reach probability of node \(v\), \(i_v\) its queried physical coordinate, and \(F_v\) its restricted function, then

\[
U(F)-\sum_{\ell}w_\ell U(F_\ell)
=\sum_{v\in T^\circ}w_v\Delta_{i_v}U(F_v)
\le 3\sum_{v\in T^\circ}w_v\operatorname{Inf}_{i_v}(F_v)
\le3I_X(F)=3I(q).
\]

The constant is independent of control dimension, polar rank, quadratic overlap, depth, pruning policy, dyadic reach probability, and the dimension, bias, or spectrum of the retained disjoint core.

## 3. Independent proof-chain reconstruction

### 3.1 Imported quadratic coordinate lemma

For a fixed control coordinate \(z\), write

\[
Q(z,y)=Q_0(y)+z(a\cdot y+\beta).
\]

The two restrictions are \(h_0=(-1)^{Q_0}\) and
\(h_1=(-1)^\beta\chi_a h_0\). A quadratic phase has squared Fourier spectrum uniform on an affine coset \(C=b+V\); multiplication by \(\chi_a\) translates this to \(C+a\).

For distinct cosets \(C\) and \(C+a\), fix \(x\in C\) and restrict the linear projection \(V\to\mathbb F_2^{\operatorname{supp}(x)}\). The within-coset upper fiber is a kernel fiber. The cross-coset upper fiber is either empty or a nonempty affine fiber of the same projection, hence has exactly the same size. Therefore adjoining the translated coset increases every logarithmic upper-fiber count by at most one bit. Together with the fair parent spectral bit this gives

\[
\Delta_zU(q)\le\frac32=3\operatorname{Inf}_z(q)
\]

in the distinct-coset case. If the supports coincide, the parent spectrum is a graph over \(C\), and projection of a parent upper fiber into the child upper fiber is injective, so \(\Delta_zU\le0\). If \(a=0\), \(\Delta_zU=0\). These cases prove

\[
\Delta_iU(q)\le3\operatorname{Inf}_i(q)
\]

for every quadratic phase and every coordinate, including all restrictions.

### 3.2 Disjoint-core cancellation

For disjoint products, squared Fourier masses and upper-set masses both tensor:

\[
p_{h_1h_2}(S_1,S_2)=p_{h_1}(S_1)p_{h_2}(S_2),\qquad
\pi_{h_1h_2}(S_1,S_2)=\pi_{h_1}(S_1)\pi_{h_2}(S_2).
\]

Thus \(U(h_1h_2)=U(h_1)+U(h_2)\). Since every control restriction has \(F_v=q_vg\),

\[
\Delta_{i_v}U(F_v)=\Delta_{i_v}U(q_v),\qquad
\operatorname{Inf}_{i_v}(F_v)=\operatorname{Inf}_{i_v}(q_v).
\]

The arbitrary core is retained exactly, not estimated.

### 3.3 Tree telescope

At an internal node,

\[
\Delta_{i_v}U(F_v)=U(F_v)-\frac{U(F_{v,0})+U(F_{v,1})}{2}.
\]

Because child reach weights equal \(w_v/2\), summing cancels every nonroot internal value and leaves the root minus the weighted terminal boundary. Applying the coordinate lemma at every node yields the first inequality with constant 3.

### 3.4 Physical-coordinate ownership

Fix a root coordinate \(i\). Nodes querying \(i\) are pairwise incomparable: otherwise one root-to-leaf path would query \(i\) twice. Their reach cylinders \(E_v\) are therefore disjoint. Since \(i\) was not previously queried, each \(E_v\) is invariant under the \(i\)-flip. Hence

\[
w_v\operatorname{Inf}_i(F_v)
=\Pr(E_v\cap\mathrm{Piv}_i(F)).
\]

Summing over nodes querying \(i\) gives at most \(\operatorname{Inf}_i(F)\). Summing over controls proves

\[
\sum_vw_v\operatorname{Inf}_{i_v}(F_v)\le I_X(F).
\]

This verifies the delicate scope point: global node uniqueness is unnecessary; pathwise nonreuse suffices.

## 4. Independent verification

The independent checker uses integer Walsh transforms and exact `Fraction` arithmetic for every quadratic computation. It additionally reconstructs disjoint arbitrary cores directly from truth tables with an independent floating evaluation of the logarithms.

- 168,146 coordinate inequalities for every quadratic/linear coefficient choice through five controls;
- all 15,692 adaptive and pruned physical trees through three controls, not merely selected policies;
- 46,996 per-coordinate ownership comparisons;
- 1,152 explicit arbitrary two-variable core/tree reconstructions;
- five exact clique-sharpness cases through ten controls;
- no randomness and no failures.

The largest tree charge/owned-influence ratio through the exhaustive tree range was 2. The sharp one-node clique family independently satisfied

\[
\frac{\Delta_iU}{\operatorname{Inf}_i}=3-2^{2-n}
\]

for even \(n=2,4,6,8,10\), confirming that 3 is the sharp supremum for the claimed inequality.

## 5. Hard-regime and scope audit

The accepted theorem survives:

- degenerate and full-rank quadratic forms;
- affine shifts and fixed/dictatorial coordinates;
- arbitrary overlap in the quadratic control graph;
- adaptive branch-dependent query orders;
- coordinate reuse on incomparable branches;
- pruning at unequal depths and rare dyadic leaves;
- arbitrary disjoint Boolean cores, including biased and nonplateaued cores.

It does **not** cover a control coordinate coupled to variables of the arbitrary core. There the two child spectra need not be translates of a common flat affine law, and cross upper fibers are no longer empty-or-equal. It also does not pay the terminal core's retained \(U\), does not establish a general biased-activation theorem outside physical uniform restrictions, and does not imply full FEI.

One wording qualification is needed but does not change the theorem: “arbitrary terminal cores” means arbitrary **disjoint retained factor** \(g\), common to all leaves after control restriction. It does not mean arbitrary changing or shared-variable terminal functions.

## 6. Primary-source overlap

O'Donnell–Tan prove a composition theorem for functions on disjoint variable blocks and explicitly record tensorization of spectral entropy and influence. Their theorem supports the importance of the disjointness boundary but does not state this upper-set potential tree payment. Wan–Wright–Wu prove FEI bounds for read-\(k\) decision trees; their entropy bound concerns functions computed by the tree and grows with read multiplicity, whereas the reviewed tree is a partial restriction ledger retaining an arbitrary terminal factor. Potapov proves FEI for plateaued functions, which includes quadratic phases at the class-endpoint level, but does not provide the coordinatewise \(U\)-increment inequality or its adaptive retained-boundary telescope.

Accordingly the result is a valid new campaign lemma at its declared scope, but no priority or external novelty claim is accepted.

## 7. Verdict and next unpaid step

`B05_A023_QUADRATIC_ADAPTIVE_TREE_v1` and
`B05_A023_PHYSICAL_OWNERSHIP_v1` are **ACCEPTED_AT_DECLARED_SCOPE**. No repair was required.

The exact remaining gap is `B05_RARE_REFUNDS/SHARED_CORE_COSET_STABILITY`: control the cross/within upper-set asymmetry when the queried control interacts with a nonflat shared core, ideally by

\[
\Delta_iU\le a\operatorname{Inf}_i+b\,\text{(retained credit)},\qquad b<1,
\]

in a form stable under adaptive physical ownership. The proposed one-point-defect shared-core test is appropriate. Full FEI remains **OPEN**.
