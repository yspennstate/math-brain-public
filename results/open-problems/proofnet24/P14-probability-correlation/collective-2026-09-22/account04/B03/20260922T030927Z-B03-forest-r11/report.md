# FOREST / account04 B03 — all-graphs integration, independent check, and exact multigraph lift

**Run:** `20260922T030927Z-B03-forest-r11`  
**Outcome:** **FULL_PROOF_CANDIDATE**  
**Parent target:** Grimmett–Winkler uniform-all-forests pairwise negative correlation.  
**Promotion scope:** internal mathematical full-proof candidate only; not an external novelty, priority, or publication claim.  
**Brain context:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact target

For every finite simple graph \(G=(V,E)\), let \(F\) be uniform over **all** acyclic subsets of \(E\), including the empty forest, disconnected forests, and all forest sizes. For distinct \(e,f\in E\), prove

\[
\Pr(e,f\in F)\le \Pr(e\in F)\Pr(f\in F).
\]

Equivalently, with \(Z\) the number of forests, \(Z_e,Z_f\) the counts containing the marked edge, and \(Z_{ef}\) the count containing both,

\[
\Delta_G(e,f):=Z_eZ_f-ZZ_{ef}\ge0.
\]

This report integrates the latest complete lead proof with two independent end-to-end reviews and then derives a new weighted multigraph corollary from an OTHER-account parallel-class result.

## 2. Exact peer results consumed

### Lead: account01/B01

Consumed `FOREST-KN-COCKS-REDUCTION-v2`, run `20260922T010823Z-b01-forest-auto11`, canonical report blob
`74622a667589ec94a53fa3f4ed63fecb72cd6c23`.

The lead's chain is:

1. prove the unit uniform-forest Rayleigh inequality for every complete graph \(K_n\);
2. use the fixed-graph Cocks theorem, as explicitly recorded in the final Semple–Welsh paper, to upgrade each \(K_n\) from unit pNC to positive-weight independence correlation of \(M(K_n)\);
3. use Semple–Welsh Proposition 3.5, which closes independence correlation under matroid minors;
4. obtain an arbitrary simple graph \(G\) on \(n\) vertices by deleting nonedges from \(K_n\), then set all surviving weights to one.

### Independent review 1: account03/B02

Consumed handoff
blob `b0a0f97426634919131e37b5a7bad4c4b7f8bb1e`.

It independently rederived the complete-graph coefficient formulas, Hermite reduction and all-\(n\) sign proof, checked the final Semple–Welsh fixed-graph Cocks attribution, and checked minor closure. It records `INDEPENDENT_END_TO_END_REVIEW_PASS_1`.

### Independent review 2: account03/B01

Consumed
`proofnet24/P14-probability-correlation/collective-2026-09-22/account03/B01/20260922T023025Z-account03-B01-forest-r11/second_end_to_end_review.md`,
blob `ea161f8956619130775dd7b638d3f87408624941`.

It independently rederived the labelled-forest decomposition, Cauchy/Hermite identities, root bound, small cases, fixed-graph transfer and deletion-minor step. It records `INDEPENDENT_END_TO_END_REVIEW_PASS_2`.

These are two separate existing-worker reviews of the same lead chain, satisfying the campaign's internal two-review gate. This does not establish external novelty or replace ordinary expert/source scrutiny.

### Named OTHER-account construction applied here: account02/B03

Consumed account02/B03 run `20260922T022013Z-b03-forest-auto11`, which proves the exact parallel-class aggregation identity for a loopless multigraph \(M\):

\[
Z_M(\{y_h\})=Z_Q(\{Y_C\}),\qquad
Y_C=\sum_{h\in C}y_h,
\]

where \(Q\) is the simple quotient and \(C\) runs through parallel classes. It also shows by book graphs that forgetting multiplicity after contraction can reverse a load-bearing sign. I apply this exact aggregation in Section 7 to derive a weighted multigraph lift rather than using the false unit-simple contraction shortcut.

## 3. Complete-graph forest counts

Let \(R\) be the rooted labelled-tree EGF, so

\[
R=ze^R,
\]

let

\[
T=R-\frac{R^2}{2},
\qquad
F=e^T,
\qquad
A=T'=e^R.
\]

Thus \(F\) is the EGF for arbitrary labelled unrooted forests.

For \(K_n\), by edge transitivity let \(E_n\) count forests containing one fixed edge, \(J_n^{\rm adj}\) forests containing two fixed adjacent edges, and \(J_n^{\rm dis}\) forests containing two fixed disjoint edges. Removing the marked edges from their tree components gives

\[
Z_n=n![z^n]F,
\]

\[
E_n=(n-2)![z^{n-2}]FA^2,
\]

\[
J_n^{\rm adj}=(n-3)![z^{n-3}]FA^3.
\]

For two disjoint marked edges there are two cases. If the two marked edges lie in different tree components, their contribution is \(FA^4\). If they lie in the same tree, deleting both marked edges leaves three components; exactly one of the four choices of an endpoint from each marked edge lies in the middle component. The two-rooted-tree EGF is

\[
T''=A'=\frac{A^2}{1-R}.
\]

Hence

\[
J_n^{\rm dis}
=(n-4)![z^{n-4}]FA^4\left(1+\frac4{1-R}\right).
\tag{3.1}
\]

### Independent combinatorial check of the factor \(4/(1-R)\)

There is a second direct derivation of the delicate same-component term. Put \(m=n-4\). Fix the two disjoint marked edges and regard the remaining \(m\) vertices as isolated components before completing to a tree. The prescribed forest has component sizes

\[
2,2,1,\ldots,1
\]

and \(m+2\) components. The generalized Cayley/Prufer formula says that a specified forest with component sizes \(s_1,\ldots,s_c\) is contained in exactly

\[
n^{c-2}\prod_i s_i
\]

labelled trees on those \(n\) vertices. Here this equals

\[
4n^m=4(m+4)^m.
\]

Equivalently,

\[
m![z^m]\frac{A^4}{1-R}=(m+4)^m,
\]

so the same-component contribution is exactly \(4A^4/(1-R)\). This independently confirms (3.1), rather than merely reusing the lead's species argument.

## 4. Cauchy/Hermite reduction

For probabilists' Hermite polynomials \(He_m\), Cauchy's formula with the substitution \(z=ue^{-u}\) gives

\[
m![z^m]e^{aR-R^2/2}
=
He_m(m+a)-mHe_{m-1}(m+a),
\tag{4.1}
\]

and the Jacobian cancellation gives

\[
m![z^m]\frac{e^{aR-R^2/2}}{1-R}
=
He_m(m+a).
\tag{4.2}
\]

Put \(k=n-4\), \(H_j=He_j(n+1)\), and

\[
s=\frac{kH_{k-1}}{H_k}.
\]

Repeated use of the Hermite recurrence yields

\[
\frac{J_n^{\rm dis}}{H_k}=5-s,\qquad
\frac{J_n^{\rm adj}}{H_k}=4-s,
\]

\[
\frac{E_n}{H_k}=2n+6-3s,
\]

\[
\frac{Z_n}{H_k}=n^2+3n+10-(n+4)s.
\]

Therefore the harder disjoint-pair Rayleigh gap has the sign of

\[
G_n(s)
=
(5-n)s^2+(n^2-4n-6)s-n^2+9n-14.
\tag{4.3}
\]

Also \(J_n^{\rm dis}-J_n^{\rm adj}=H_k>0\), so positivity for the disjoint orbit implies positivity for the adjacent orbit.

## 5. All-\(n\) sign proof

Let \(x=n+1=k+5\). The zeros \(\lambda_i\) of \(He_k\) are real and symmetric. Since \(x\) lies to the right of all of them,

\[
s=\frac{H_k'(x)}{H_k(x)}
=\sum_i\frac1{x-\lambda_i}.
\]

Pairing roots \(\lambda,-\lambda\),

\[
\frac1{x-\lambda}+\frac1{x+\lambda}
=
\frac{2x}{x^2-\lambda^2}
\ge
\frac2x+\frac{2\lambda^2}{x^3}.
\]

Using

\[
\sum_i\lambda_i^2=k(k-1)
\]

gives

\[
s\ge
\frac{k}{x}+\frac{k(k-1)}{x^3}
=
\frac{(n-4)(n-1)(n+4)}{(n+1)^3}
=:L_n.
\tag{5.1}
\]

Moreover

\[
H_k-kH_{k-1}
=
k![z^k]FA^4>0,
\]

so \(0\le s<1\).

For \(n\ge6\),

\[
G_n'(s)=2(5-n)s+n^2-4n-6
\]

is positive throughout \([0,1]\), because its minimum there is

\[
G_n'(1)=n^2-6n+4>0.
\]

Thus \(G_n(s)\ge G_n(L_n)\). Exact simplification gives

\[
(n+1)^6G_n(L_n)
=
2n^6+70n^5-33n^4+185n^3+1369n^2-3147n+1170.
\]

Writing \(n=t+6\) turns the numerator into

\[
2t^6+142t^5+3147t^4+33233t^3
+187651t^2+551661t+666396,
\]

which is strictly positive for all \(t\ge0\). Hence both edge-pair orbits in \(K_n\) have positive Rayleigh gap for every \(n\ge6\).

The exact small cases are:

- \(K_2\): no distinct edge pair;
- \(K_3\): \((Z,E,J_{\rm adj})=(7,3,1)\), gap \(2\);
- \(K_4\): \((Z,E,J_{\rm adj},J_{\rm dis})=(38,14,4,5)\), gaps \(44,6\);
- \(K_5\): \((291,93,23,29)\), gaps \(1956,210\).

Thus the unit uniform-all-forests pairwise negative-correlation inequality holds for every complete graph \(K_n\).

## 6. All-simple-graphs deduction

The source-sensitive step is the fixed-graph upgrade. The final published Semple–Welsh paper, in its note after the open questions, explicitly records that Cocks proved:

> if Conjecture 1.1 holds for a graph \(G\), then \(M(G)\) is independence correlated.

The same paper's Proposition 3.5 proves that independence-correlated matroids are closed under minors. Its independence-correlation definition quantifies over all positive real weights.

Now let \(G\) be an arbitrary finite simple graph on \(n\) vertices. Section 5 proves Conjecture 1.1 for \(K_n\). Therefore the Cocks fixed-graph result upgrades \(M(K_n)\) to positive-weight independence correlation. Since

\[
M(G)
=
M(K_n)\setminus(E(K_n)\setminus E(G)),
\]

\(M(G)\) is a deletion minor of \(M(K_n)\) and is also independence correlated. Specializing every surviving edge weight to \(1\) gives exactly the uniform law on all unrooted acyclic edge subsets of \(G\). Isolated vertices do not change the edge-set forest counts. Graphs with fewer than two edges have no pair to check.

Therefore the target inequality holds for every finite simple graph, conditional only on the cited published Cocks theorem exactly as recorded by Semple–Welsh.

### Source limitation kept explicit

The body of Cocks's 2008 paper was not directly available in this runtime. The exact fixed-graph statement is, however, explicitly printed in the final peer-reviewed Semple–Welsh paper, and both independent reviews above checked this final-versus-working-paper distinction. The older 2005 working-paper parallel-copy argument is only class-level and is **not** used as a substitute proof of the fixed-graph theorem.

## 7. New exact weighted multigraph lift from account02/B03

The account02/B03 aggregation result allows a clean strengthening and simultaneously resolves the induced-parallel-edge issue.

Let \(M\) be a finite loopless multigraph with positive individual edge weights \(y_h\). Let \(C\) range over its parallel classes, let \(Q\) be the simple quotient, and set

\[
Y_C=\sum_{h\in C}y_h.
\]

Because a forest contains at most one member of any parallel class,

\[
Z_M(\{y_h\})=Z_Q(\{Y_C\}).
\tag{7.1}
\]

For a marked edge \(e\in C\),

\[
\partial_e Z_M=\partial_C Z_Q.
\]

For marked edges \(e\in C\), \(f\in D\) with \(C\ne D\),

\[
\partial_e\partial_f Z_M
=
\partial_C\partial_D Z_Q.
\]

By Section 6 plus the fixed-graph Cocks upgrade, every simple quotient \(Q\) is independence correlated for **all positive class weights** \(Y_C\). Hence

\[
(\partial_e Z_M)(\partial_f Z_M)
-
Z_M\partial_e\partial_f Z_M
=
(\partial_C Z_Q)(\partial_D Z_Q)
-
Z_Q\partial_C\partial_D Z_Q
\ge0.
\]

Multiplying by \(y_ey_f/Z_M^2>0\) gives pairwise negative correlation of the two inclusion indicators.

If \(e,f\) are distinct members of the same parallel class, no forest contains both, so their joint probability is zero and the inequality is immediate. Loops, if allowed, are never present and are likewise trivial.

Thus the integrated candidate yields the stronger corollary:

> **Weighted multigraph corollary.** Every finite multigraph, with arbitrary positive edge weights and the forest measure proportional to the product of selected edge weights, has pairwise negatively correlated edge indicators.

This corollary is not needed for the original simple/unit target, but it is a genuine use of the named OTHER-account result and eliminates the false “contract then forget parallel multiplicity” mechanism exposed by its book-graph adversary.

## 8. Independent exact regression

A fresh standard-library checker was run in this invocation. It independently enumerates all forests of \(K_3,\ldots,K_6\) by union-find, checks the exact marked-edge gaps, and checks the Hermite inequalities in exact rational arithmetic for \(6\le n\le500\). Output:

```text
K3 adjacent=(7, 3, 3, 1, 2)
K4 adjacent=(38, 14, 14, 4, 44) disjoint=(38, 14, 14, 5, 6)
K5 adjacent=(291, 93, 93, 23, 1956) disjoint=(291, 93, 93, 29, 210)
K6 adjacent=(2932, 822, 822, 178, 153788) disjoint=(2932, 822, 822, 226, 13052)
HERMITE_EXACT_REVIEW_PASS n=6..500
GENERALIZED_CAYLEY_DISJOINT_COMPONENT_CHECK m=0..12 PASS
```

Checker SHA-256:
`92662cf55711e8a95a9940e7cdff156b1b6c4abf9db4fce73cf132781d4f6d14`.

Output SHA-256:
`e594686d249a71c94542c81dddfd19dfa19b642d8c63f3a8ff58151dca24074b`.

The finite checker is regression evidence only. Sections 3–6 are the all-\(n\), all-simple-graphs argument.

## 9. Fresh external-status check

A bounded fresh literature check on 22 September 2026 found contemporary sources still describing the general uniform-forest negative-correlation conjecture as open. In particular, the September 2026 wheel-graph result presents wheels as a new covered family and explicitly says the general conjecture remains open; Tang–Zhang's March 2026 complete-graph work covers different fixed-component/excess families for sufficiently large \(n\), not the exact all-forest theorem used here.

This search result is **not** a novelty certificate. The present artifact makes no priority claim.

## 10. Verdict and handoff

**Status: `FULL_PROOF_CANDIDATE`.**

Reason for the upgraded internal status:

1. the lead's complete candidate covers every finite simple graph and every distinct edge pair under the exact uniform-all-forests measure;
2. the delicate complete-graph factor and Hermite sign mechanism were independently checked again here;
3. the final published Semple–Welsh source states the fixed-graph Cocks implication and the required minor closure;
4. two independent existing workers have now supplied end-to-end passes of the same candidate;
5. the account02/B03 exact parallel-class result has been integrated, yielding the weighted multigraph corollary and excluding the known false contraction simplification.

No automatic truth/publication promotion is made. Before any external claim, the strongest remaining diligence item is ordinary expert verification of the Cocks theorem from its own full text if obtainable, plus independent line-by-line checking of this integrated write-up. A later source contradiction must retract the chain immediately.

### Sources

- G. Grimmett and S. Winkler, *Negative association in uniform forests and connected graphs*, Random Structures & Algorithms 24 (2004), 444–460; arXiv:math/0302185.
- C. Semple and D. Welsh, *Negative Correlation in Graphs and Matroids*, Combinatorics, Probability and Computing 17 (2008), 423–435; Proposition 3.5 and the Section 5 note.
- C. C. Cocks, *Correlated Matroids*, Combinatorics, Probability and Computing 17 (2008), 511–518, DOI 10.1017/S0963548308009152.
- P. Tang and Z. Zhang, *Pairwise Negative Correlation for Uniform Spanning Subgraphs of the Complete Graph*, arXiv:2603.10738 (11 March 2026).
- I. O. Bado, *Negative edge correlation for uniform random forests on wheel graphs*, Statistics & Probability Letters, DOI 10.1016/j.spl.2026.110960 (online September 2026).
