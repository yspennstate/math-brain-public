# P0043 independent analysis — w433

Checkpoint 2026-10-10. Sections 1–4 were saved before reading any proof by paired prover w432. No proof of the full target is claimed. Independent referee: w434, pending.

## 1. Exact target and scope correction

Let G be an infinite, connected, locally finite graph whose automorphism group has finitely many vertex orbits. Under independent Bernoulli bond percolation, let p_c(G) be the threshold for an infinite open cluster. Assuming p_c(G)<1, the target is that G[p_c(G)] has no infinite cluster almost surely. This implies theta_v(p_c)=0 at every vertex v, and conversely, since V(G) is countable, that family of zero probabilities implies almost sure absence everywhere.

Primary statement: Hutchcroft, *Critical percolation on any quasi-transitive graph of exponential growth has no infinite clusters* (2016), Conjecture 1.1, with connectedness and local finiteness specified in the introduction; https://comptes-rendus.academie-sciences.fr/mathematique/item/10.1016/j.crma.2016.07.013.pdf . Its Theorem 1.2 settles the exponential-growth subclass. This is a historical scope source, not a present-openness certificate.

The ranking omits p_c<1. That hypothesis matters: on the two-sided line Z, p_c=1 and the cluster at p=1 is all of Z. For p<1, either ray from any fixed vertex is all open with probability lim_n p^n=0, so countable union gives no infinite cluster. Thus the unqualified ranking shorthand is false.

A fresh public scope note https://github.com/openai/math/blob/main/lean/docs/213.md claims the full graph theorem. Actual comparator, solution, trusted axioms, and kernel verification have not yet been checked. Current openness remains UNKNOWN; no novelty claim is made.

## 2. Proved reduction: any hypothetical critical infinite cluster is maximally fragile

Statement. For a countable connected locally finite graph G and critical bond probability p_c>0, almost surely every infinite component H of G[p_c] has its own bond threshold p_c(H)=1. This does not assume quasi-transitivity.

Proof. Generate independent X_e~Bernoulli(p_c) on all edges of G. Independently generate Y_e~Bernoulli(q), for a fixed rational q in (0,1). The retained configuration Z_e=X_e Y_e is independent Bernoulli(p_c q) across edges, because the independent pairs (X_e,Y_e) factor across e. Since p_c q<p_c, Z has no infinite cluster almost surely.

Condition on the complete X configuration. On every open component H of X, the Y variables restricted to E(H) are independent Bernoulli(q). For a fixed vertex v, let f_{v,q}(X) be the conditional probability that v has an infinite Y-open component inside its X-component. It is nonnegative, and E[f_{v,q}(X)]=0 by the preceding subcritical statement. Hence f_{v,q}(X)=0 almost surely.

Intersect these probability-one statements over the countable set of vertices v and rational q in (0,1). On the resulting full-measure set, every infinite X-component H fails to percolate at every rational q<1. By monotonicity it fails at every real q<1: choose a rational q' with q<q'<1. At q=1 it percolates since H is infinite and connected. Therefore p_c(H)=1 for every infinite H. QED.

Dependency check. Conditioning uses an independent thinning family, not independent cluster-membership events. The inference from zero annealed probability to zero conditional probability uses nonnegativity. The countable rational intersection is explicit. A graph with p_c=0 has no edges at p=0, so its critical configuration already has no infinite component.

Later source attribution: after the independent phase, the original Lyons--Peres cached primary text was located. Conjecture 8.15 is at text lines 17168-17169, printed p.285. The proof of Theorem 8.21 explicitly uses critical-cluster fragility at text line 17360. The thinning mechanism above is therefore a rederivation of a known mechanism, with no originality or solved-open-problem credit.

## 3. Concrete obstruction: positive density and ambient geometry do not ensure thinning robustness

Statement. Every infinite connected nearest-neighbor tree T embedded as a subgraph of Z^d has p_c(T)=1, regardless of the density of its vertex set in Z^d.

Proof. Fix a vertex o of T. There is at most one simple T-path from o to each vertex. A simple T-path of length n ends within the ambient lattice box o+[-n,n]^d. Consequently there are at most (2n+1)^d possible endpoints and hence at most that many length-n simple T-paths. Under independent q-bond percolation on T, each fixed path is open with probability q^n. The union bound gives

P_q(o reaches intrinsic distance n) <= (2n+1)^d q^n.

For each q<1 the right side tends to zero. An infinite component in a locally finite tree contains vertices at every intrinsic distance. Thus P_q(o belongs to an infinite component)=0. Take the countable union over o. At q=1 the infinite connected T percolates, proving p_c(T)=1. QED.

Explicit density-one example. On vertex set Z^2 retain all vertical nearest-neighbor edges, and retain horizontal nearest-neighbor edges only along the row y=0. This comb is connected, acyclic, has maximum degree 4, and has every ambient vertex (density exactly one). Its threshold is nevertheless 1. This is not itself quasi-transitive and is not an iid percolation cluster on Z^2. It refutes only the proposed deduction from connectedness, positive vertex density, bounded degree, and polynomial ambient growth to survival of thinning. It is not a counterexample to P0043.

## 4. Hardest missing input in this route

An argument by downward thinning would need a separate theorem ruling out maximally fragile infinite critical components specifically under the iid Bernoulli law on the quasi-transitive ambient graph. One precise sufficient input is:

(R) If an infinite connected locally finite quasi-transitive G has p_c(G)<1 and critical percolation has an infinite component with positive probability, then with positive probability at least one such component H has p_c(H)<1.

Section 2 proves that (R) would contradict the assumed infinite critical component. Thus (R) implies P0043. Conversely, P0043 makes (R) vacuously true. In this form (R) has the strength of the full target; calling it a routine robustness lemma would hide the entire missing theorem. Density alone cannot supply it by Section 3.

Next concrete proof step: inspect the paired proof's actual mechanism and locate the smallest inference that supplies (R), or an alternative critical-continuity input; check its filtration and limit quantifiers rather than assuming robustness.

## 5. Independent quantifier obstruction for block arguments

This construction was also derived before reading w432's proof. It refutes a uniform inference from very high one-site probabilities and finite dependence when the dependence range is allowed to increase.

Fix d>=1 and integer R>=1. Give sites z in Z^d independent continuous labels U_z. For each x, let c(x) be the site with least label in B_infinity(x,R). Almost surely all labels are distinct. Declare x open exactly when c(x)=c(y) for every nearest neighbor y of x.

The resulting site field is translation invariant. Its values on sets at sup-norm distance greater than 2R+2 are jointly independent, since each value only reads labels in B_infinity(x,R+1). In the usual nearest-neighbor graph-distance convention a conservative dependence range is k=2d(R+1).

Every adjacent open pair has the same c value. Hence every connected open component has a single c value, say z, and all its sites lie in B_infinity(z,R). Every component has at most (2R+1)^d sites; in particular percolation is impossible for every realization with distinct labels.

The exact one-site open probability is

a_R = (2R-1)^d / ((2R+1)^d + 2d(2R+1)^(d-1)).

Indeed, all the local minima agree if and only if the minimum label in the union of B_infinity(y,R), for y=x and the 2d neighbors of x, lies in their intersection. The intersection is B_infinity(x,R-1), with (2R-1)^d sites. The union consists of B_infinity(x,R) and 2d disjoint extra faces of (2R+1)^(d-1) sites. Exchangeability of the continuous iid labels makes the minimum's location uniform in that union. This proves the formula.

Alternatively, each neighboring pair has different c values with probability 1/(R+1), by counting the symmetric difference and union of the two boxes. Thus a_R>=1-2d/(R+1), which tends to one. At d=2,R=399, a_R=635209/641597>0.99, yet all components have at most 638401 sites; sup-norm dependence range 800 suffices.

Audit implication. A sequence of block events whose probabilities tend to one is not enough if their dependency ranges simultaneously diverge. A valid domination argument must choose and control both quantities: for a fixed finite k obtain an error below the relevant k-dependent domination threshold, or derive another explicit joint law. The construction is not iid Bernoulli percolation and no FKG, insertion-tolerance, or monotonicity property is claimed. It attacks only a proof step that assumes high marginals plus unspecified finite dependence suffice.

## 6. Attempt at the missing robustness input

On Z^d, suppose hypothetically that critical iid percolation has a unique infinite cluster with positive density. Large fixed boxes then meet it with probability approaching one, by ergodicity. For any finite family of boxes that meet that cluster, their chosen cluster vertices eventually connect inside a sufficiently large finite surrounding box, by uniqueness and continuity from below. This suggests a local block argument followed by finite-event continuity to a parameter below p_c.

Even granting a correct deterministic gluing condition, the quantifier needed for domination is stronger than those facts provide. What one obtains is: for each error epsilon>0 there exist block scale L and inspection radius R with probability of a good local event at least 1-epsilon. The field of translated events has a dependence range k that depends on R/L. To obtain a percolating coarse field one needs one choice satisfying epsilon<eta(k), where eta(k)>0 is the quantitative tolerance at that particular dependence range. The existence of L and R for each epsilon gives no bound on k and does not imply this joint inequality. Section 5 gives an exact counterexample to the abstract implication even when finite dependence and translation invariance hold.

Outcome: this route does not establish the missing iid robustness theorem. A repair must provide a scale-compatible local uniqueness or a joint exploration bound, with constants and dependence controlled together. The construction in Section 5 does not refute a proposed repair with additional FKG or uniform conditional hypotheses.

## 7. Source-card mechanism correction

The existing author-unreviewed attempt card at math-brain-build/export/population/nodes.jsonl line 260 describes the exponential-growth proof as a comparison yielding critical susceptibility finiteness. The published Hutchcroft argument uses susceptibility finiteness only for p<p_c. Supermultiplicativity of the infimum two-point function, Fekete's lemma, and left continuity of its exponential rate yield kappa_{p_c}(n)<=gr(G)^(-n). For subexponential growth gr(G)=1, that estimate is just kappa<=1. The published argument by itself does not yield a decaying bound in that regime.

Critical susceptibility need not be finite even for exponential-growth graphs. For a Delta-regular tree, Delta>=3, p_c=1/(Delta-1), a sphere of radius n>=1 has Delta(Delta-1)^(n-1) vertices, and each is connected to the root with probability p_c^n. The expected number of connected vertices in that sphere is Delta/(Delta-1) for every n. Therefore susceptibility at criticality is infinite. This refutes the stronger interpretation of the old card; it does not refute Hutchcroft's theorem.

## 8. Paired-proof audit and separately derived constant improvement

Read w432/ATTEMPT.md only after Sections 1-5 of this file had been saved. Verdict: keep the pivotal-measure reduction and the stated special cases, with the unproved quasi-transitive input G01 retained. No full-target proof is present.

L02: the finite Russo measures on [0,p_c] have masses f_n(p_c) and their mass on each [0,t], t<p_c, tends to zero. The continuous-test-function split proves the claimed weak limit, with n and then delta in the stated order. L03: the stated critical-window uniform condition is equivalent to theta(p_c)=0; the finite initial set of polynomials in the necessity proof is essential and is included. The L^r sufficient condition is honestly unproved on the full class.

L04: the nonsymmetric tree has k_n=floor(log_2((n+1)^2)), level sizes 2^(n+k_n), unique degree-8 root, and maximum degree 8. Its branching second-moment increments are (1-p)/M_n, giving E(W_n^2)<=pi^2/6 at p=1/2. The survival lower bound 6/pi^2 follows from Cauchy--Schwarz and decreasing events. It is not quasi-transitive, as the proof correctly states. L05: the open-pivotal identity and the at-most-n witness-path bound give pointwise derivative decay below criticality without losing the critical atom. These are valid concrete obstructions to replacing uniform integrability by pointwise limits.

L06: the regular-tree derivative bound is valid. Here is a separate tightening. Let D>=3, b=D-1 and

c_b=(b-1)/(2b)*(1-1/b)^(b-2).

For the forward b-ary tree, let s_m(p) be level-m survival, with s_0=1. Child independence gives s_{m+1}=1-(1-p s_m)^b. At p=1/b, the second derivative of g(s)=1-(1-s/b)^b is at most -2c_b on [0,1]. Taylor's formula gives s_{m+1}<=s_m-c_b s_m^2, hence 1/s_{m+1}>=1/s_m+c_b and s_m(1/b)<=1/(1+c_b m). By monotonicity this also holds for 0<=p<=1/b.

For p>0, Russo's formula and an open witness path give p*s_m'(p)<=m*s_m(p). In the D-regular tree, with m=n-1,

f_n'(p)=D*(1-p*s_m)^(D-1)*(s_m+p*s_m')
         <=D*(m+1)*s_m
         <=D*(m+1)/(1+c_b*m)
         <=D/c_b.

The last inequality uses 0<c_b<1. At p=0 the same bound follows from polynomial continuity. Therefore the bound D/c_b holds uniformly in n>=1 and p in [0,1/b]. This directly gives every critical-window integral <=(D/c_b)*delta.

At D=3, c_b=1/4 and the bound is 12, versus w432's valid bound 27 on [1/4,1/2]. The new bound holds on [0,1/2]. This is a tightening of a known special-case control, with no novelty claim and no implication for cyclic subexponential graphs. w434 must independently check it before theorem promotion.
