# FOREST / fleet02 B02 — complete-log-concavity gives a spectral Rayleigh budget, and minimal bad clusters must satisfy a quantitative Gram obstruction

Status: **ESSENTIAL_STEP_APPLIED. Parent target remains OPEN. FULL_PROOF_CANDIDATE=false.**

Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`.

Assignment: derive a source-valid polynomial or probabilistic comparison for the uniform law on all unrooted forests, and prove exactly what log-concavity/Rayleigh input applies at unit weights.

Named partner: `fleet03/B03`. Campaign lead: `fleet01/B01`. At the fresh observation point neither had a complete current collective FOREST report in the scientific tree. Per the collective order I did not wait. I consumed the closest exact compatible OTHER-account result instead: `fleet03/B02/20260921T235733Z-b02-forest-r11/report.md`, report commit `e5ada175cb0383d4b87fc8243e76790dbc9abb8c`, report blob `c492ca3b040b5d185e0c825ef1c63d3759a3d8f8`. I also checked the independent overlap/reconnection identity in the shared handoff `fleet01-B03-20260921T234923Z.md`, blob `b49c6b896238cd62508b98549526dd12a469ceb3`.

Brain status: **WITHOUT_VERIFIED_BRAIN**. No authenticated brain retrieval/context runtime was used.

## 1. Exact target and notation

Let `G=(V,E)` be a finite simple graph, `m=|E|`, and let

\[
P_G(\mathbf z)=\sum_{F\subseteq E:\,F\text{ acyclic}}\prod_{h\in F}z_h.
\]

This is the independence polynomial of the graphic matroid. In particular its monomials are **all** acyclic edge subsets: disconnected forests and every cardinality, including the empty set. No root, component weight, fixed-size condition, or spanning-tree condition is present.

At unit weights write

\[
Z=P_G(\mathbf1),\qquad Z_e=\partial_eP_G(\mathbf1),\qquad Z_{ef}=\partial_e\partial_fP_G(\mathbf1).
\]

For distinct edges define the Rayleigh difference

\[
\Delta_G(e,f)=Z_eZ_f-ZZ_{ef}.
\]

If `F` is uniform over all forests and `X_e=1_{e\in F}`, then

\[
\Pr(e\in F)=\frac{Z_e}{Z},\qquad
\Pr(e,f\in F)=\frac{Z_{ef}}{Z},
\]

and hence

\[
\operatorname{Cov}(X_e,X_f)=-\frac{\Delta_G(e,f)}{Z^2}.
\]

The source target is therefore exactly `Delta_G(e,f)>=0` for every finite simple `G` and every distinct pair `e,f`.

## 2. Source-valid log-concavity input really does apply to the unrooted all-forest law

The key source is:

- N. Anari, K. Liu, S. Oveis Gharan, C. Vinzant, **Log-Concave Polynomials III: Mason's Ultra-Log-Concavity Conjecture for Independent Sets of Matroids**, arXiv:1811.01600.

Their main matroid theorem proves complete log-concavity of the homogenized independent-set generating polynomial. For a matroid on `m` elements this polynomial is

\[
H_M(y,\mathbf z)
=\sum_{I\in\mathcal I(M)}y^{m-|I|}\prod_{i\in I}z_i.
\tag{2.1}
\]

For the graphic matroid `M(G)`, the independent sets `I` are precisely the acyclic edge subsets. Thus (2.1) is

\[
H_G(y,\mathbf z)
=\sum_{F\text{ forest}}y^{m-|F|}\mathbf z^F.
\]

Set `y=1`. Then

\[
H_G(1,\mathbf z)=P_G(\mathbf z).
\tag{2.2}
\]

This specialization is not a heuristic limiting operation. Anari--Liu--Oveis Gharan--Vinzant, Lemma 2.2, states that complete log-concavity is preserved by an affine map taking the nonnegative orthant into the nonnegative orthant. The map

\[
T(\mathbf z)=(1,\mathbf z)
\]

has exactly that property. Consequently:

### Theorem 2.1 — exact unrooted forest complete log-concavity

For every finite graph `G`, the all-forest polynomial `P_G` is completely log-concave on the nonnegative orthant, and in particular `log P_G` is concave on the positive orthant.

This is the requested source-valid applicability statement. It applies to the **unrooted, all-cardinalities, possibly disconnected** forest measure itself. It does not pass through rooted forests, determinants, spanning trees, or a fixed component count.

## 3. The spectral Rayleigh matrix and a universal factor-two theorem

For any positive evaluation `z`, define the matrix

\[
R_{ij}(\mathbf z)
=P_i(\mathbf z)P_j(\mathbf z)-P(\mathbf z)P_{ij}(\mathbf z).
\tag{3.1}
\]

A direct differentiation gives

\[
\nabla^2\log P
=\frac{P\nabla^2P-(\nabla P)(\nabla P)^T}{P^2},
\]

so

\[
\boxed{R(\mathbf z)=-P(\mathbf z)^2\nabla^2\log P(\mathbf z).}
\tag{3.2}
\]

By Theorem 2.1 the Hessian of `log P` is negative semidefinite. Therefore:

### Theorem 3.1 — spectral Rayleigh positivity

For every finite graph and every positive edge-weight vector,

\[
\boxed{R(\mathbf z)\succeq0.}
\tag{3.3}
\]

This is weaker than entrywise Rayleigh positivity, but it is an exact all-graph theorem.

Because `P` is multiaffine, `P_{ii}=0`. Hence

\[
R_{ii}=P_i^2.
\]

Every `2x2` principal minor of the positive-semidefinite matrix `R` is nonnegative, so for distinct `i,j`,

\[
\boxed{|R_{ij}|\le P_iP_j.}
\tag{3.4}
\]

At unit weights this becomes

\[
|\Delta_G(e,f)|\le Z_eZ_f.
\tag{3.5}
\]

If `Delta>=0`, the desired target already holds. If `Delta<0`, (3.5) gives

\[
ZZ_{ef}-Z_eZ_f\le Z_eZ_f,
\]

or equivalently

\[
\boxed{ZZ_{ef}\le2Z_eZ_f.}
\tag{3.6}
\]

Thus for a uniformly sampled unrooted forest,

\[
\boxed{\Pr(e,f\in F)\le2\Pr(e\in F)\Pr(f\in F).}
\tag{3.7}
\]

This factor-two approximate negative-correlation inequality is a universal consequence of complete log-concavity. The argument actually works for the weighted independent-set law of every matroid after specialization.

## 4. Why complete log-concavity is not itself the missing Rayleigh theorem

One must not replace the target by spectral negative dependence. The same Anari--Liu--Oveis Gharan--Vinzant paper explicitly explains the distinction: pairwise negative correlation is an **entrywise sign condition** on the off-diagonal Hessian of `log p`, whereas complete log-concavity only forces all eigenvalues of that Hessian to be nonpositive. They explicitly note that a completely log-concave matroid polynomial can have positive Hessian entries.

Since

\[
\Delta_{ef}=-P^2(\nabla^2\log P)_{ef},
\]

the source conjecture requires each off-diagonal entry of `-Hess(log P)` to be nonnegative. Positive semidefiniteness of the whole matrix does not imply that entrywise sign.

This also matches the stronger special-class literature: A. Erickson, **Sums of squares and negative correlation for spanning forests of series parallel graphs**, arXiv:1008.3660, proves a positive sum-of-squares representation of Rayleigh differences for series-parallel graphs. That stronger entrywise Rayleigh property is therefore additional structure, not a consequence one may silently read off from general matroid log-concavity.

So the correct source use is:

1. **valid:** complete log-concavity applies exactly to the target all-forest polynomial;
2. **valid:** it yields the positive-semidefinite Rayleigh matrix and consequences such as (3.5)--(3.7);
3. **invalid shortcut:** it does **not** yield `Delta_ef>=0` entrywise.

## 5. OTHER-account input: minimal-counterexample sign clusters

The consumed `fleet03/B02` result proves the following exact deletion/contraction identity. Fix distinct `e,f,g` and split

\[
P_G=A+y_gB,
\]

where at the remaining unit weights `A` is the deletion stratum and `B` the contraction stratum. Put

\[
D_0=A_eA_f-AA_{ef},\qquad
D_1=B_eB_f-BB_{ef}.
\]

Then the peer proves

\[
\boxed{
AB\Delta_G(e,f)
=BZ D_0+AZ D_1-\Delta_G(g,e)\Delta_G(g,f).
}
\tag{5.1}
\]

In a lexicographically minimal simple counterexample, the deletion and contraction gaps are nonnegative after the source-valid minor/parallel-class reductions. Hence if `Delta_G(e,f)<0`, then for every third edge `g`,

\[
\boxed{
\Delta_G(g,e)\Delta_G(g,f)
>Z(BD_0+AD_1)\ge0.
}
\tag{5.2}
\]

The peer therefore derives that the violating pairs `Delta<0` form equivalence classes. Inside a nontrivial class every pair has positive covariance; from such a class to any external edge all Rayleigh gaps are strictly positive.

Their exact checker evaluated 1,098 labelled simple graphs through five vertices and 46,563 marked triples, with zero identity or implication failures. Those finite checks support the algebra only; they are not a proof of the parent conjecture.

## 6. New combination: every minimal bad class is an obtuse Gram cluster with a sharp total budget

This section is the main new mathematical step of the run.

At unit weights write `p_e=Z_e/Z`. Normalize the positive-semidefinite Rayleigh matrix by the positive diagonal derivatives:

\[
Q_{ef}=\frac{\Delta_G(e,f)}{Z_eZ_f}\quad(e\ne f),
\qquad Q_{ee}=1.
\tag{6.1}
\]

Equivalently,

\[
Q=D^{-1}R D^{-1},\qquad D=\operatorname{diag}(Z_e).
\]

Hence

\[
\boxed{Q\succeq0.}
\tag{6.2}
\]

For a violating pair define its normalized positive-covariance strength

\[
\rho_{ef}
=\frac{\operatorname{Cov}(X_e,X_f)}{p_ep_f}
=-\frac{\Delta_G(e,f)}{Z_eZ_f}.
\tag{6.3}
\]

Thus on a bad class `C`, `rho_ef>0` and `Q_ef=-rho_ef` for distinct `e,f in C`.

Let `s=|C|`. Testing the principal matrix `Q_C` on the all-ones vector gives

\[
0\le \mathbf1^TQ_C\mathbf1
=s-2\sum_{\{e,f\}\subset C}\rho_{ef}.
\]

Therefore:

### Theorem 6.1 — minimal bad-cluster spectral budget

Every nontrivial violation class `C` in a lexicographically minimal counterexample must satisfy

\[
\boxed{
\sum_{\{e,f\}\subset C}\rho_{ef}\le\frac{s}{2}.
}
\tag{6.4}
\]

In particular the average normalized violation in the class is at most

\[
\boxed{
\frac{1}{s-1}.
}
\tag{6.5}
\]

So at least one violating pair in every bad class satisfies `rho_ef<=1/(s-1)`.

In unnormalized probability units, the same argument with `R_C` gives

\[
\boxed{
\sum_{\{e,f\}\subset C}\operatorname{Cov}(X_e,X_f)
\le\frac12\sum_{e\in C}p_e^2.
}
\tag{6.6}
\]

A further local constraint comes from every three-edge principal minor. For distinct `a,b,c in C`, positive semidefiniteness of

\[
\begin{pmatrix}
1&-\rho_{ab}&-\rho_{ac}\\
-\rho_{ab}&1&-\rho_{bc}\\
-\rho_{ac}&-\rho_{bc}&1
\end{pmatrix}
\]

gives

\[
\boxed{
\rho_{ab}^2+\rho_{ac}^2+\rho_{bc}^2
+2\rho_{ab}\rho_{ac}\rho_{bc}\le1.
}
\tag{6.7}
\]

For an equal-strength bad triple this forces `rho<=1/2`.

Geometrically, `Q_C` is a Gram matrix of unit vectors whose pairwise inner products are all negative. Thus the peer's bad equivalence class is not an arbitrary clique of positive covariances: it must be realizable as a finite obtuse Gram cluster satisfying (6.4) and every principal-minor constraint such as (6.7).

## 7. First quantitative bridge back to the peer deletion/contraction inequality

The preceding budget can be coupled directly to the peer's strict lower bounds, rather than left as an unrelated auxiliary fact.

Let `C` be a nontrivial bad class, `s=|C|`, and let `h notin C`. By the peer sign-cluster theorem,

\[
\alpha_{h,e}:=Q_{he}
=\frac{\Delta_G(h,e)}{Z_hZ_e}>0
\quad(e\in C).
\tag{7.1}
\]

Write

\[
R_C^{\rho}=\sum_{\{e,f\}\subset C}\rho_{ef},
\qquad
A_h=\sum_{e\in C}\alpha_{h,e}.
\]

Use positive semidefiniteness of the principal matrix on `{h} union C`. Test it on the vector having coordinate `-t` at `h` and coordinate `1` on every edge of `C`. For all real `t`,

\[
t^2-2A_ht+s-2R_C^{\rho}\ge0.
\]

Minimizing at `t=A_h` gives the new external/internal budget

\[
\boxed{
\left(\sum_{e\in C}\alpha_{h,e}\right)^2
\le s-2\sum_{\{e,f\}\subset C}\rho_{ef}.
}
\tag{7.2}
\]

Thus stronger internal positive-covariance violations force the total normalized negative-covariance response to **every** external edge to be small.

Now specialize the peer identity (5.2) with `g=h`. In its decomposition `P=A+y_hB`, one has `Z_h=B`. For every bad pair `{e,f} subset C`, define

\[
L_{h;ef}
:=\frac{Z(BD_0^{ef}+AD_1^{ef})}{B^2Z_eZ_f}\ge0,
\tag{7.3}
\]

where `D_0^{ef},D_1^{ef}` are the deletion/contraction Rayleigh gaps for that pair. Dividing (5.2) by `B^2 Z_eZ_f` gives

\[
\alpha_{h,e}\alpha_{h,f}>L_{h;ef}.
\tag{7.4}
\]

Since all `alpha_{h,e}>0`,

\[
A_h^2
>2\sum_{\{e,f\}\subset C}L_{h;ef}.
\]

Combining with (7.2) yields the following necessary condition for every external edge:

### Theorem 7.1 — deletion/contraction versus spectral-budget obstruction

In any lexicographically minimal counterexample, every nontrivial bad class `C` and every external edge `h` must obey

\[
\boxed{
2\sum_{\{e,f\}\subset C}L_{h;ef}
< s-2\sum_{\{e,f\}\subset C}\rho_{ef}.
}
\tag{7.5}
\]

This is a direct source-valid join between the OTHER-account minimal-counterexample theorem and general matroid complete log-concavity. A violation of (7.5) for even one external edge rules out the proposed bad class.

This is the **first essential missing implication derived in this run**. The next targeted step is no longer “prove log-concavity implies Rayleigh,” which is false in that form. It is:

> Show that in every surviving 3-connected minimal-counterexample configuration, the peer deletion/contraction lower bounds force the left side of (7.5) to meet or exceed the right side for some external edge; or else construct a genuine 3-connected forest response satisfying all these inequalities.

That is a quantitatively falsifiable obstruction.

## 8. Exact size-mixture decomposition: why fixed-size negative correlation or Mason ULC does not finish the target

Let

\[
K=|F|,
\qquad \pi_k=\Pr(K=k),
\qquad p_e(k)=\Pr(e\in F\mid K=k),
\]

and

\[
c_{ef}(k)=\operatorname{Cov}(X_e,X_f\mid K=k).
\]

The law of total covariance gives the exact identity

\[
\boxed{
\operatorname{Cov}(X_e,X_f)
=\mathbb E[c_{ef}(K)]
+\operatorname{Cov}(p_e(K),p_f(K)).
}
\tag{8.1}
\]

Therefore the source target is exactly equivalent to

\[
\boxed{
\mathbb E[-c_{ef}(K)]
\ge \operatorname{Cov}(p_e(K),p_f(K)).
}
\tag{8.2}
\]

Mason ultra-log-concavity controls the size sequence `pi_k`, and complete log-concavity gives much more spectral information, but neither fact by itself establishes the two-term dominance (8.2).

There is an exact elementary warning already on a tree with `m` edges. Every subset is a forest, so under the uniform law `K~Bin(m,1/2)`. Conditioned on `K=k`, the selected set is a uniform `k`-subset of the `m` edges, giving for distinct `e,f`

\[
\operatorname{Cov}(X_e,X_f\mid K=k)
=-\frac{k(m-k)}{m^2(m-1)}.
\]

Averaging over the binomial law yields

\[
\mathbb E[c_{ef}(K)]= -\frac{1}{4m}.
\]

But `p_e(k)=k/m`, so

\[
\operatorname{Cov}(p_e(K),p_f(K))
=\frac{\operatorname{Var}(K)}{m^2}
=\frac{1}{4m}.
\]

The two terms cancel exactly and the unconditional covariance is zero.

Thus even perfect fixed-size negative correlation does not pass to the all-sizes mixture without a quantitative comparison of the two terms. This is precisely why a theorem about fixed-component forests, fixed-size independent sets, or the ULC rank sequence cannot simply be substituted for the Grimmett--Winkler target.

## 9. Refuted candidate: a one-variable Schur-complement sufficient condition is not close to necessary

I also tested a stronger-looking route using the homogenizing variable `y` together with two edge coordinates. The positive-semidefinite Rayleigh matrix of the homogenized polynomial yields a Schur-complement **sufficient** condition of the rough form

\[
\frac{\operatorname{Cov}(K,X_e)^2}{p_e^2}
+\frac{\operatorname{Cov}(K,X_f)^2}{p_f^2}
\ge m-\mathbb E K-\operatorname{Var}(K)
\quad\Longrightarrow\quad \Delta(e,f)\ge0
\]

when the relevant size-edge covariances have the compatible sign.

This is **CANDIDATE_REFUTED as a useful necessary mechanism**. On `K_3`, exact counts give

\[
Z=7,\quad Z_e=Z_f=3,\quad Z_{ef}=1,\quad \Delta=2>0,
\]

while

\[
\mathbb E K=\frac97,
\quad \operatorname{Var}(K)=\frac{24}{49},
\quad \operatorname{Cov}(K,X_e)=\frac8{49}.
\]

The proposed sufficient inequality has left side `128/441` and right side `60/49`, so it fails badly although the target Rayleigh gap is positive. I therefore do not promote this as the next route.

## 10. Exact computation used only as a sanity check

The archived checker `spectral_forest_checker.py` independently enumerates every labelled simple graph on `2,3,4,5` vertices, every forest of each graph, and every present unordered edge pair.

Exact output:

```text
TOTAL_GRAPHS=1098
TOTAL_EDGE_PAIRS=11766
FACTOR2_FAILURES=0
SIZE_VARIANCE_FAILURES=0
TARGET_NEGATIVE_GAPS=0
K3_Z=7 K3_ZE=3 K3_ZEF=1 K3_DELTA=2
K3_EK=9/7 K3_VARK=24/49 K3_COV_K_XE=8/49 K3_YDIAG=60/49
K3_SCHUR_SUFFICIENT_LHS=128/441 K3_SCHUR_SUFFICIENT_RHS=60/49 HOLDS=False
TREE_M4_EXPECTED_CONDITIONAL_COV=-1/16
TREE_M4_SIZE_MIXING_COV=1/16
TREE_M4_TOTAL_COV=0
```

The `FACTOR2_FAILURES=0` line checks (3.6) on 11,766 finite pair instances. The tree and triangle lines check the exact algebra in Sections 8--9. These are sanity checks only. They do not replace the source proof from complete log-concavity and do not extend the known complete-order census.

## 11. Conditional end-to-end argument and exact remaining gap

A compact conditional route now reads as follows.

1. Suppose a finite simple counterexample exists and choose one lexicographically minimal in `(number of vertices, number of edges)`.
2. Use the inherited P14 block/two-separator reductions to work in the surviving 3-connected obstruction.
3. By the consumed `fleet03/B02` theorem, every violating pair lies in a nontrivial bad equivalence class `C`, and every external edge has strict positive Rayleigh gap to every member of `C`; moreover the deletion/contraction products satisfy (5.2).
4. By the source-valid Anari--Liu--Oveis Gharan--Vinzant theorem specialized at `y=1`, the exact all-unrooted-forest Rayleigh matrix is positive semidefinite.
5. Therefore `C` must obey the internal Gram budgets (6.4), (6.7), the external response budget (7.2), and the combined deletion/contraction inequality (7.5) for **every** external edge.
6. A proof that some external edge necessarily violates (7.5) would contradict the existence of the minimal counterexample and finish the parent conjecture.

Step 6 is not proved here. It is the exact first remaining implication after the new join.

## 12. Source and provenance ledger

Primary mathematical sources used:

- G. R. Grimmett and S. N. Winkler, **Negative association in uniform forests and connected graphs**, arXiv:math/0302185. This is the source uniform-all-forests conjecture and distinguishes it from the already-settled uniform spanning-tree case.
- N. Anari, K. Liu, S. Oveis Gharan, C. Vinzant, **Log-Concave Polynomials III: Mason's Ultra-Log-Concavity Conjecture for Independent Sets of Matroids**, arXiv:1811.01600. Used specifically for complete log-concavity of the homogenized independent-set polynomial and affine specialization closure; also for the explicit distinction between entrywise negative correlation and spectral negative dependence.
- A. Erickson, **Sums of squares and negative correlation for spanning forests of series parallel graphs**, arXiv:1008.3660. Used only to delimit the stronger independent-set-Rayleigh property on a special graph class.

OTHER-account artifact consumed and mathematically applied:

- `fleet03/B02`, run `20260921T235733Z-b02-forest-r11`, report commit `e5ada175cb0383d4b87fc8243e76790dbc9abb8c`, report blob `c492ca3b040b5d185e0c825ef1c63d3759a3d8f8`. Applied in Sections 5 and 7, not merely cited.

Independent compatible handoff checked:

- `fleet01/B03-20260921T234923Z.md`, blob `b49c6b896238cd62508b98549526dd12a469ceb3`, exact overlap/reconnection identity `Delta=N^2(P(Q)-Cov(X,Y))`. It was not needed in the final spectral proof, so I do not count it as closure.

No novelty or priority claim is made from a search miss. No benchmark answer or sealed material was read. No paid/remote model was used.

## 13. Honest status

- `ESSENTIAL_STEP_APPLIED`: **yes** — exact source-valid complete-log-concavity input was specialized to the true unrooted all-forest polynomial, and then combined with the OTHER-account minimal-counterexample sign-cluster theorem to yield the new quantitative obstruction (7.5).
- `CANDIDATE_REFUTED`: **yes, subroute only** — the homogenizing-variable Schur sufficient condition is far too strong and is rejected as the main route by the exact `K_3` calculation.
- `AUXILIARY_ONLY`: **no** for the run as a whole; the spectral/deletion-contraction join directly constrains the essential surviving minimal counterexample.
- `NO_CHANGE`: **no**.
- `FULL_PROOF_CANDIDATE`: **no**. The parent Grimmett--Winkler conjecture remains open here.

Model self-report: **GPT-5.6 Sol**. Requested reasoning effort: **maximum supported**. Configured/known effort: **UNKNOWN_NOT_EXPOSED**. Exposed provider token/reasoning usage: **null / NOT_EXPOSED**. Elapsed execution is recorded in the scoped finish status and is wall work, not pure thinking.
