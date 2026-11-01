> UPDATE: The owner has retired the Cayley/cutoff line in favor of Downloads/Shmalo_Overleaf_Revised.zip (Sparse unweighted Cayley realizations and instability of cutoff). Its stated near-logarithmic theorem covers the sparse-degree question below. Those sections are historical, not active open targets. The separate HDX source questions are not the cutoff question. Active work has moved to P0174 free-Brownian unimodality.

# Harder probability fronts, 10 September 2026

This is disjoint author work supporting the existing probability campaign. It does not change the master solved count. The companion manuscript is in Downloads/Shmalo_Cayley_Product_Condition.pdf; its independently reviewed mathematical merit is YES. The public Lean repository contains components only.

## A completed strengthening to hand over

P0276 now has an existence corollary with degree n^{o(1)}, preserving the full non-cutoff profile and the spectral product condition. The full proof is copied in P0276_subpolynomial_degree_extension.tex. It uses a degree-matched rapidly mixing Abelian factor. It is a strengthening of the same result, not an additional historical open problem solved. The auxiliary generators are selected by an existence argument, not a closed-form construction. The original graph remains explicit. A separate referee independently rederived the corollary, including all constants, and found no mathematical defect.

## Historical sparse-degree question: retired by the owner

RETIRED: the owner's Shmalo_Overleaf_Revised.zip states a near-logarithmic realization theorem that covers this follow-up. The question below is retained only as research history and must not be served as an active open target. Previously we asked whether an unweighted Abelian Cayley counterexample could have degree at most (log n)^C for a fixed C. The barrier below applies only to our particular fast-factor padding method; it does not contradict the owner's more general construction.

The existing construction does not attain this regime. Nor can arbitrary fast-factor padding of that construction do so, as the following elementary obstruction shows.

### Fast-padding volume bound: complete proof

Let A be a finite D-regular graph, D>=2, with M vertices. Start its rate-one continuous-time simple random walk at a vertex x, and suppose its distance to uniform at time u is at most1/4. Let R=ceil(4u+4). The number N of jumps by time u is Poisson with mean u. Markov gives P(N>R)<=u/R<=1/4. Therefore the graph ball B(x,R) has walk probability at least3/4. Total variation at most1/4 implies |B(x,R)|/M>=1/2. There are at most 1+D+...+D^R<=D^(R+1) vertices in the ball. Consequently

    log M <= log2 + (4u+6) log D.

Apply this with D=D_d from the original P0276 graph and an auxiliary mixing time u_d=o(T_d). Here log D_d~d log2 and T_d~d log d/4, so log M_d=o(d^2 log d). The original group has logarithmic order O(d), hence the enlarged group still satisfies log n_d=o(d^2 log d). For every fixed C,

    log((log n_d)^C)=O_C(log d), whereas log(2D_d)~d log2.

It follows that 2D_d/(log n_d)^C tends to infinity. Thus a same-degree auxiliary factor mixing in o(T_d) cannot make this family polylogarithmic in total volume. This is a barrier for this padding method, not a no-go theorem for every counterexample construction.

### Independent entropy check of the bound's order

At time u, entropy of the endpoint is at most H(N)+u log D: conditional on N=j, at most D^j paths are possible. The maximum-entropy bound for an integer-valued variable of mean u gives H(N)<=log(u+1)+1 (compare with the geometric distribution). A maximal coupling with uniform U and error delta<=1/4 gives H(U)<=H(X)+h(delta)+delta log M. Thus (3/4)log M<=H(X)+log2. This independently yields log M=O((u+1)log D), agreeing with the support argument. The support proof above does not depend on any entropy theorem.

## A fresh primary-source intake

Songtao Mao, Abelian Cayley High-Dimensional Expanders with Polylogarithmic Degree, arXiv:2609.08937v1, submitted8 September2026. Section6 has three open-question families. These concern high-dimensional link random walks; they must not be conflated with the total-variation cutoff theorem in our paper.

The first two have precise source formulations ready for the campaign's duplicate and scope checks. The third needs the cited stronger-expansion definitions fixed before a precise master-ledger statement can be admitted. All three remain UNSOLVED by this work. Source-reported openness is not a certification of absence of a newer solution.

## Brownian-sheet caution

Khoshnevisan's slice-finiteness Open Problem1, especially its remaining planar case, is a separate hard front. The d=3 finite-fiber result is only a partial resolution of the source's two-dimensional/three-dimensional question. Do not replace that question with the projection problem. Chen and Woessner's Zeros of the Brownian Sheet (2025), Theorem1.2, resolves Khoshnevisan's Open Problem4 on simultaneous projection dimensions; it does not state a solution to Open Problem1. The published source is https://doi.org/10.1007/s10959-024-01399-1 . This literature separation should be carried into intake deduplication.

## References and ownership

- Salez, Problem2.4: https://arxiv.org/abs/2508.21055
- Hermon and Olesker-Taylor, displayed Conjecture1: https://doi.org/10.4171/JEMS/1743
- Mao, Section6: https://arxiv.org/html/2609.08937v1#S6
- Khoshnevisan, Section8: https://arxiv.org/abs/math/0510518
- Chen and Woessner, Theorem1.2: https://doi.org/10.1007/s10959-024-01399-1

Owner has authorized collaboration. Requests were sent to the current probability worker and its parent; integration into their master ledger remains their responsibility until the handoff is accepted. No existing candidate proof or ledger was edited here.

