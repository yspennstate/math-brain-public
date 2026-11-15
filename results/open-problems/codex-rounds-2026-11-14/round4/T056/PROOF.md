# Transfer from a Bernoulli graphing to finite permutation models

This is a proof audit of Proposition `models:transfer` in OpenAI, *A group without fixed price* (5 October 2026), [finite-models.tex](https://github.com/openai/math/blob/main/preprints/A-group-without-fixed-price-October-5-2026/build/finite-models.tex). The group and action definitions are in [group-actions.tex](https://github.com/openai/math/blob/main/preprints/A-group-without-fixed-price-October-5-2026/build/group-actions.tex). The finite estimate (12) below makes the approximation errors explicit. No rank lower bound for the presented groups is assumed or proved here.

## Statement

Let

\[
A=F(a,b_1,\ldots,b_{99}),\qquad
u_0=1,\quad u_i=u_{i-1}ab_i,\quad w=u_{99}a,
\qquad J=\langle b_1,\ldots,b_{99},w\rangle.
\]

Let \(\Gamma\) be a countable group containing \(A\), and consider its Bernoulli right action on \([0,1]^\Gamma\),

\[
(xq)(g)=x(qg).
\]

For each \(q\ne1\), a fixed configuration satisfies \(x(q)=x(1)\), an event of measure zero because these are independent uniform coordinates. The free part is therefore Borel, invariant and conull, since \(\Gamma\) is countable. Let \((X,\mu)\) denote this part. For a subgroup \(L\leq A\), let \(R_L\) denote its orbit relation on \(X\). A graphing is a countable indexed family of measure-preserving Borel partial bijections; its cost is the sum of its domain measures. Define

\[
d_X=\inf\{C(\mathcal E):\mathcal E\subset R_A,
\quad R_J\vee\mathcal E=R_A\}.
\tag{1}
\]

Generation in (1) may hold on an invariant conull set. Removing the saturation of an exceptional null set makes the identity pointwise without changing costs. Saturations are null because the acting group is countable and preserves measure.

For a nonempty finite exact right \(A\)-set \(V\), define

\[
D_V=\left\langle x_v\ (v\in V)\ \middle|\
x_vx_{vu_1}\cdots x_{vu_{99}}=1\ (v\in V)\right\rangle.
\tag{2}
\]

Here exact means \((vg)h=v(gh)\) for every \(v,g,h\). The rank \(\operatorname{rk}(D_V)\) is the minimum number of group generators; \(D_V\) is not required to be finite.

**Proposition.** Suppose \(V_k\) are finite exact right \(A\)-sets, \(n_k=|V_k|\to\infty\), and

\[
\frac{|\operatorname{Fix}_{V_k}(g)|}{n_k}\longrightarrow0
\qquad(g\in A\setminus\{1\}).
\tag{3}
\]

Then

\[
d_X\geq\limsup_k\frac{\operatorname{rk}(D_{V_k})}{n_k}.
\tag{4}
\]

## 1. The restriction to A is a Bernoulli action

Choose one representative \(h_c\) of each coset \(Ah_c\) in \(\Gamma\). Every element of \(\Gamma\) has a unique expression \(gh_c\), with \(g\in A\). Put

\[
\Omega=[0,1]^{A\backslash\Gamma},\qquad
\nu=\operatorname{Leb}^{A\backslash\Gamma}.
\]

The coordinate bijection

\[
x\longmapsto \xi,\qquad \xi(g)=(x(gh_c))_c,
\]

sends product measure to \(\nu^A\). Indeed the coordinate blocks indexed by different \(g\) are disjoint, so they are independent and each has law \(\nu\). For \(q\in A\), the block at \(g\) after translating \(x\) by \(q\) is the old block at \(qg\). Thus the action becomes

\[
(\xi q)(g)=\xi(qg).
\tag{5}
\]

In particular \(((\xi q)r)(g)=\xi(qrg)\), which verifies the right-action convention. Work on the full space \(\Omega^A\) with measure \(\mu=\nu^A\), viewing domains originally in \(X\) as measurable subsets of this space. The complements discarded in passing to \(X\) are null. Cylinder approximations below are taken in the full product space.

## 2. A cocycle with values in D_V

For a finite exact \(A\)-set \(V\), prescribe

\[
\theta(v,a)=x_v,\qquad\theta(v,b_i)=1,
\qquad
\theta(v,s^{-1})=\theta(vs^{-1},s)^{-1}
\tag{6}
\]

for each positive free-basis letter \(s\). For a word \(s_1\cdots s_m\) in signed basis letters, multiply the prescribed values at the successive sources \(v,vs_1,\ldots,vs_1\cdots s_{m-1}\).

This value does not change under free reduction. If a pair \(ss^{-1}\) starts at \(y\), its two factors are

\[
\theta(y,s)\theta(ys,s^{-1})
=\theta(y,s)\theta(y,s)^{-1}=1.
\]

The pair returns to \(y\) by exactness, so the source for every later factor also remains unchanged. For a pair \(s^{-1}s\), the same calculation uses \(\theta(y,s^{-1})=\theta(ys^{-1},s)^{-1}\). Since \(A\) is free, this defines \(\theta(v,g)\) for every \(g\in A\), independently of its word expression. Concatenation gives

\[
\theta(v,gh)=\theta(v,g)\theta(vg,h),\qquad
\theta(v,g^{-1})=\theta(vg^{-1},g)^{-1}.
\tag{7}
\]

The occurrences of \(a\) in \(w=ab_1ab_2\cdots ab_{99}a\) start at \(v,vu_1,\ldots,vu_{99}\). Every \(b_i\)-factor contributes 1. Relation (2) therefore says \(\theta(v,w)=1\) for every \(v\). Together with \(\theta(v,b_i)=1\), (7) implies

\[
\theta(v,j)=1\qquad(v\in V,\ j\in J).
\tag{8}
\]

For completeness, the inverse of a generator of \(J\) has value 1 by the second identity in (7), at every source. A product of these signed generators has value 1 by the first identity, applied repeatedly. This proves (8) without requiring that \(J\) act freely on \(V\).

The value \(\theta(v,g)\) is attached to the group element \(g\). It need not be determined by the two vertices \(v,vg\).

## 3. Finitely many formal paths suffice up to small measure

Fix a finite-cost graphing \(\mathcal E\) admissible in (1). Finite cost suffices for the infimum, since the full \(a\)-translation has cost 1 and, together with \(R_J\), generates \(R_A\).

Split each partial map into its displacement pieces. On the conull free set, every pair in \(R_A\) has a unique displacement in \(A\); for a Borel map, its displacement pieces are Borel. The resulting indexed maps have the form

\[
\varphi_\ell:L_\ell\longrightarrow L_\ell g_\ell,
\qquad \varphi_\ell(\xi)=\xi g_\ell,
\qquad \sum_\ell\mu(L_\ell)=C(\mathcal E).
\]

A path type is a finite list of full \(J\)-translations and signed paid-map indices. Its formal label is the ordered product of the associated group elements, with \(g_\ell^{-1}\) for an inverse paid step. Its validity set is the intersection of its paid-domain tests at the successive prefixes. All these sets are measurable, and there are countably many types.

Almost every \(\xi\) admits a valid path to \(\xi a\). The formal label of such a path is exactly \(a\): if its label were \(g\), the equality \(\xi g=\xi a\) at a free point would force \(g=a\). Consequently the union of the validity sets of types with formal label \(a\) is conull. For any \(p>0\), countable continuity from below supplies a finite collection \(\mathcal T\) of these types whose validity union \(P\) satisfies

\[
\mu(P)\geq1-p.
\]

Write \(I\) for the finite set of paid indices appearing in \(\mathcal T\), \(r=|I|\), and \(m_\ell\) for the total number of occurrences of index \(\ell\) in all the selected types, counting both signs.

For every \(\ell\in I\), choose a finite-coordinate measurable set \(L'_\ell\), and put \(\Delta_\ell=\mu(L_\ell\triangle L'_\ell)\). These errors can be made arbitrarily small simultaneously. To justify this density, finite-coordinate measurable sets form an algebra generating the product sigma-algebra. The sets approximable by this algebra in symmetric-difference measure are closed under complements and finite unions. For a countable union, first approximate it by a finite subunion in measure using continuity from below, and then approximate that finite union. Thus the approximable sets form the whole sigma-algebra. The conclusion also holds for the measure completion by changing a set on a null set.

Replace every paid-domain test by the test using \(L'_\ell\), and let \(P'\) be the union of the resulting validity sets. The formal labels are unchanged.

For a forward step \(\ell\) after prefix \(h\), the test is \(\xi h\in L_\ell\). For an inverse step, its source \(\xi h\) must belong to the range \(L_\ell g_\ell\), so the test is

\[
\xi h g_\ell^{-1}\in L_\ell.
\tag{9}
\]

Translation invariance shows that changing either test changes its truth value on a set of measure \(\Delta_\ell\). The symmetric difference of two finite intersections is contained in the union of the symmetric differences of their individual predicates; the same holds for finite unions. It follows that

\[
\mu(P\triangle P')\leq\sum_{\ell\in I}m_\ell\Delta_\ell,
\qquad
\sum_{\ell\in I}\mu(L'_\ell)
\leq C(\mathcal E)+\sum_{\ell\in I}\Delta_\ell.
\]

In particular, with

\[
H=\sum_{\ell\in I}\mu(L'_\ell)+1-\mu(P'),
\]

we have

\[
0\leq H\leq C(\mathcal E)+p+
\sum_{\ell\in I}(1+m_\ell)\Delta_\ell.
\tag{10}
\]

There is a finite set \(F\subset A\) supporting all the sets \(L'_\ell\) and \(P'\). In detail, if \(L'_\ell\) uses coordinates \(F_\ell\), its forward test after \(h\) uses \(hF_\ell\) by (5); its inverse test uses \(hg_\ell^{-1}F_\ell\). Take the union of these finite sets over all occurrences and also include every \(F_\ell\). These choices are made before choosing \(k\).

## 4. The local law on a finite exact action

For a finite exact right \(A\)-set \(V\), choose independent labels \(z_v\) of law \(\nu\) and set

\[
\xi_v(g)=z_{vg}\qquad(v\in V,\ g\in A).
\]

For every labeling, exactness gives

\[
\xi_{vq}(g)=z_{v(qg)}=(\xi_vq)(g),
\qquad\text{hence }\xi_{vq}=\xi_vq.
\tag{11}
\]

Let \(B_V(F)\) be the sources \(v\) for which \(g\mapsto vg\) is not injective on \(F\), and put \(\beta_V(F)=|B_V(F)|/|V|\). If \(v\notin B_V(F)\), the labels \(z_{vg}\), \(g\in F\), are independent with law \(\nu\). Thus every measurable \(F\)-cylinder \(E\) satisfies \(\Pr(\xi_v\in E)=\mu(E)\) at this source. At a bad source the discrepancy is at most 1. Averaging yields

\[
\left|\frac1{|V|}\sum_v\Pr(\xi_v\in E)-\mu(E)\right|
\leq\beta_V(F).
\]

If \(vg=vh\), applying \(h^{-1}\) on the right gives \(vgh^{-1}=v\). Conversely that last equality implies \(vg=vh\). For distinct \(g,h\), the element \(gh^{-1}\) is nonidentity. A union bound therefore gives

\[
\beta_V(F)\leq
\sum_{\substack{g,h\in F\\g\ne h}}
\frac{|\operatorname{Fix}_V(gh^{-1})|}{|V|}.
\]

The ordered-pair sum may count a source more than once, which is harmless for this upper bound. Since \(F\) is fixed and finite, (3) implies \(\beta_{V_k}(F)\to0\).

## 5. A generating list for every labeling

For a fixed labeling, make a list \(\mathcal L\) containing \(\theta(y,g_\ell)\) for every \(\ell\in I\) and every \(y\in V\) such that \(\xi_y\in L'_\ell\). Repetitions and identity elements are allowed in this list.

Suppose \(\xi_v\in P'\). Choose a selected type valid at \(\xi_v\) under the modified tests, and follow its formal labels in \(V\). After a prefix \(h\), the current vertex is \(vh\). By (11) its configuration is \(\xi_vh\).

For a forward paid step \(\ell\), validity means \(\xi_{vh}\in L'_\ell\), so its factor \(\theta(vh,g_\ell)\) is in \(\mathcal L\). For an inverse paid step, (9) and (11) give \(\xi_{vhg_\ell^{-1}}\in L'_\ell\). Thus \(\theta(vhg_\ell^{-1},g_\ell)\) is in the list, and by (7) the required factor is its inverse:

\[
\theta(vh,g_\ell^{-1})
=\theta(vhg_\ell^{-1},g_\ell)^{-1}.
\]

Every full \(J\)-step has factor 1 by (8). Iterating (7) along the path, whose formal label is exactly \(a\), now expresses

\[
x_v=\theta(v,a)\in\langle\mathcal L\rangle.
\]

Add \(x_v\) to the list for each remaining source \(v\) with \(\xi_v\notin P'\). The enlarged list generates all of \(D_V\), since it generates every displayed generator in (2). For every labeling, therefore,

\[
\operatorname{rk}(D_V)\leq
\sum_{\ell\in I}\sum_{v\in V}\mathbf1_{L'_\ell}(\xi_v)
+\sum_{v\in V}\mathbf1_{(P')^c}(\xi_v).
\]

Taking expectations and using the local law for its \(r+1\) summands proves the finite estimate

\[
\boxed{\displaystyle
\frac{\operatorname{rk}(D_V)}{|V|}
\leq C(\mathcal E)+p+
\sum_{\ell\in I}(1+m_\ell)\Delta_\ell
+(r+1)\beta_V(F).}
\tag{12}
\]

Neither concentration nor independence between different sources is used. Only the independent base labels on distinct vertices at a single good source enter the local law.

## 6. The limit and the cost consequence

Given \(\varepsilon>0\), first choose the selected types with \(p=\varepsilon\), then their cylinder approximations with \(\sum_{\ell\in I}(1+m_\ell)\Delta_\ell<\varepsilon\). The numbers \(r,m_\ell\), the labels of all types, and the finite support \(F\) are fixed before \(k\) tends to infinity. Equations (3) and (12) give

\[
\limsup_k\frac{\operatorname{rk}(D_{V_k})}{n_k}
\leq C(\mathcal E)+2\varepsilon.
\]

Let \(\varepsilon\downarrow0\) for this fixed graphing, and then take the infimum over admissible graphings. This proves (4). The coefficient 2 here combines the path-coverage error and the weighted cylinder error; its value has no effect on (4).

For the manuscript's \(\Gamma=A*_J(J\times\mathbb Z)\), the earlier deployment estimate combines with (4) to yield

\[
\operatorname{Cost}(R_\Gamma)
\geq1+d_X
\geq1+\limsup_k\frac{\operatorname{rk}(D_{V_k})}{n_k}.
\]

This implication needs no positivity assumption. A positive normalized-rank bound and a suitable sequence satisfying (3) are further requirements for a positive cost gap.

## 7. Independent checks and boundary cases

The error in (10) can also be checked by comparing the functions

\[
W=\sum_{\ell\in I}\mathbf1_{L_\ell}+\mathbf1_{P^c},
\qquad
W'=\sum_{\ell\in I}\mathbf1_{L'_\ell}+\mathbf1_{(P')^c}.
\]

The first has integral at most \(C(\mathcal E)+p\). Pointwise, \(|W-W'|\) is bounded by the sum of the paid-domain disagreement indicators and the disagreement indicators for every occurrence in every selected path, with each such occurrence translated by its appropriate prefix. Integration gives at most \(\sum_\ell(1+m_\ell)\Delta_\ell\), recovering (10) directly.

The coefficient of \(\beta_V(F)\) can be checked without applying a separate discrepancy bound to each event. At a good source the expectation of \(W'(\xi_v)\) is exactly \(H\); at a bad source \(0\leq W'(\xi_v)\leq r+1\). Hence its average is at most \((1-\beta_V(F))H+\beta_V(F)(r+1)\leq H+(r+1)\beta_V(F)\), agreeing with (12).

An explicit inverse-path test checks the source in (9). Put \(g=b_1a^{-1}\). The type consisting of an inverse paid \(g\)-step followed by a full \(b_1\)-step has formal label \(g^{-1}b_1=a\). Its paid source is \(vg^{-1}\), not \(v\). Indeed \(\theta(y,g)=x_{yg}^{-1}\), so the list entry at \(y=vg^{-1}\) is \(x_v^{-1}\); its inverse generates \(x_v\), as required. Testing the inverse step at \(v\) would not justify that list entry.

For the one-point trivial action \(V=\{v\}\), (2) gives \(D_V=\langle x_v\mid x_v^{100}=1\rangle\), cyclic of order 100. There are 100 factors because the indices run from 0 to 99; independently, \(u_{99}\) contains 99 occurrences of \(a\), and the final \(a\) in \(w\) adds one. The cyclic group has order exactly 100: its order divides 100 by its relation, while the map \(x_v\mapsto1\) onto \(\mathbb Z/100\mathbb Z\) shows it is at least 100. The cocycle still has \(\theta(v,a)=x_v\) and \(\theta(v,w)=1\), even though every group element has the same endpoints in \(V\). Thus replacing formal labels by endpoint pairs would destroy the argument. Also every \(\xi_v\) is a constant configuration; its coordinates at two distinct elements agree with probability 1, whereas two independent \(\nu\)-labels agree with probability zero (\(\nu\) has a uniform coordinate and is nonatomic). The local product law therefore fails on any support with at least two distinct coordinates. Here \(\beta_V(F)=1\), exactly the case excluded asymptotically by (3).

Finite-model configurations may all lie outside the original free conull subset. This causes no domain problem: the cylinder predicates are measurable on all of \(\Omega^A\), and their local laws are evaluated there. Freeness was used only to obtain formal label \(a\) for the original selected paths. Subsequent generation uses those unchanged labels and (7), so it remains valid with stabilizers, repeated vertices, or repeated generator values in the finite model.

If \(F\) has at most one element, there are no coordinate collisions and \(\beta_V(F)=0\). If selected paths have no paid indices, the first list is empty; (8) then makes \(x_v=1\) at every source satisfying one of those formal paths, and the same proof applies. Empty selected validity sets, overlapping domains, and redundant list entries only weaken the upper bound on rank. No ergodicity or transitivity assumption is used.
