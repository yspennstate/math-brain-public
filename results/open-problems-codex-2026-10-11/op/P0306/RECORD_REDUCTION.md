# A model-specific record reduction and its obstruction

11 October 2026. This is a continuation of SECOND_ATTEMPT.md, not a solution of P0306.

## 1. The direction of the cactus map

For a rooted geodesic space (X,D,rho), the continuous cactus pseudodistance is

K(a,b)=D(rho,a)+D(rho,b)-2 sup_gamma min_t D(rho,gamma(t)),

where gamma ranges over continuous paths from a to b. Proposition 2.4, PDF page 8 of Curien--Le Gall--Miermont, arXiv:1102.4177, proves K(a,b)<=D(a,b). Thus the quotient map X -> cactus is 1-Lipschitz. This bounds dimensions in the cactus by dimensions in X; it does not bound dimensions in X by dimensions in the cactus. A section with an upper distance bound would be additional input.

There is also an obstruction to placing all surface two-stars in the nonleaf skeleton of this tree. Take the Euclidean closed unit disk with its ordinary distance and root its center. If |a|=r<=s=|b|, a circular arc at radius r followed by a radial segment reaches b without going below radius r. Endpoint a forces every path's minimum radius to be at most r. Consequently K(a,b)=s-r, and the cactus is the interval [0,1]. Every boundary point maps to its leaf 1. Every boundary point is nevertheless a two-star: choose two distinct inward directions and short straight segments starting there. These segments lie in the disk, are minimizing, and intersect only at their common starting point. This is a counterexample to a proposed deterministic inclusion, not a counterexample for LQG. The disk lacks LQG geodesic coalescence.

## 2. A complete contour-record lemma

Suppose a compact coded space is obtained from a continuous cyclic contour label function L:[0,T]->[0,infinity), with L(0)=L(T)=0. Let pi denote its quotient map. Assume the constructed metric satisfies

|L(s)-L(t)| <= D(pi(s),pi(t)) <= Dcirc(s,t),

Dcirc(s,t)=L(s)+L(t)-2 max(min_[s,t] L, min_[t,T]union[0,s] L), for s<=t.

These inequalities hold in the labeled-forest construction of the Brownian disk viewed from a boundary point; the contour traverses the grafted trees as well as the boundary. The lower bound and the infimum-over-chains construction are essential here. No equality D=Dcirc is assumed.

Fix an anchor u in [0,T]. Let R_u be the times t in [u,T] such that L(t)=min_[u,t] L. For r<=s in R_u, every label in [r,s] is at least L(s), while the endpoint has label L(s). Hence min_[r,s] L=L(s). The complementary arc contains the zero-label root, so its minimum is zero. Therefore Dcirc(r,s)=L(r)-L(s), and both metric inequalities imply

D(pi(r),pi(s))=L(r)-L(s).

Continuity and L(T)=0 imply that for each a in [0,L(u)] the first time after u with label a is a record time. Thus pi(R_u), with its inherited metric, is isometric to the interval [0,L(u)]: equal labels have distance zero, and all intermediate labels occur. It has Hausdorff dimension at most one, and exactly one if L(u)>0. Every subset of this image, including its intersection with the boundary, has dimension at most one. For any countable collection of anchors, the union of their record images and its boundary intersection still have dimension at most one, by countable stability of Hausdorff dimension.

This proves a genuine special-case bound within the Brownian disk coding. It does not prove that arbitrary boundary two-stars lie in these record images. Being the start of two disjoint outgoing geodesics is not the same as lying on a geodesic from one of countably many anchors to a fixed root. Neither existence of geodesics nor the two-star definition supplies that inclusion. General gamma also has no Brownian-snake representation in these sources.

## 3. Why boundary records alone cannot replace full contour records

In Le Gall, arXiv:2006.11050, PDF page 23, the boundary labels are lambda(t)=sqrt(3)b(t), where b is a five-dimensional Bessel bridge. Conditional on b, grafted Brownian-snake excursions have Poisson intensity

2 dt N_0(domega) 1{W_*(omega)>=-lambda(t)}.

Their shifted minimum is lambda(t)+W_*(omega). The excursion law has

N_0(W_*<=-a)=3/(2a^2), a>0

(equation (2), PDF page 4). This tail is continuous, so the excursion minimum has no atom at any negative threshold.

Let J be a compact interval of positive length inside (0,1), and let 0<m<min_J lambda. Conditional on lambda, the number of retained excursions attached in J whose shifted minimum is at most m is Poisson with mean

mu_m(J)=3 integral_J [(lambda(t)-m)^(-2)-lambda(t)^(-2)] dt.

Proof: a retained excursion counted here has -lambda(t)<=W_*<=-(lambda(t)-m). Subtract the two excursion-law tails and multiply by the intensity factor 2. Integrating in t gives the displayed mean. The integrand is positive and bounded on J, so 0<mu_m(J)<infinity. The defining count property of a Poisson random measure therefore gives conditional probability 1-exp(-mu_m(J)) of at least one such graft.

All boundary labels on J exceed m, yet with strictly positive conditional probability a grafted contour segment attached in J reaches a label at most m. Thus a lower bound on boundary labels does not imply the corresponding lower bound on the full forest contour. This invalidates substituting boundary-only running minima into the distance formula. It does not establish a lower bound for D from Dcirc, or an upper dimension bound for two-stars. The chain infimum can further lower D.

## 4. Hostile-referee audit and exact remaining gap

* Cactus quotient: the verified inequality has the wrong direction for the intended upper bound. No inverse estimate was inferred.
* Cactus skeleton: even a planar compact geodesic disk has boundary two-stars mapping to a cactus leaf. Coalescence-specific input would be necessary to avoid this example.
* Record lemma: both distance inequalities, continuity, nonnegative labels, and a zero on the complementary contour arc were used explicitly. Record times are full-contour records. A boundary-only version is not proved.
* The Poisson computation is conditional on the entire Bessel bridge. Its thresholds stay strictly away from zero on J, ensuring finite intensity. It is a calculation for the Brownian disk coding, not a simulation of an LQG star event.
* The Brownian disk record subset is not identified with the Neumann-GFF boundary two-star set. Even a Brownian-disk all-stars covering theorem would require the appropriate local-law transfer before answering the original half-plane question.

The most promising remaining reduction is to prove that the relevant boundary two-stars admit a countable cover by full-contour record geodesics, or by other tree subsets with Lipschitz maps into the surface. The sources checked do not provide this inclusion, and no proof of it is given here. For arbitrary gamma, the earlier missing mixed arm/diameter estimate under Gaussian tilt remains unresolved. The original equality is still unproved in this attempt.
