# C0100 mathematical attempt

## Exact target
For the stabilization s_n of n delta_0 on Z^d, prove existence for every positive-radius Euclidean ball B and integer j of lim #{x in Z^d intersect n^(1/d)B: s_n(x)=j}/#{Z^d intersect n^(1/d)B}. Separately determine the wired-square identity scaling limit. No full answer has been proved.

## Source audit
Apollonian PDE solutions do not imply an a.e. patch cover for the actual point-source limit. The gap in the earlier attempt includes the global geometry, as well as control of discrete patterns.

## 1. Exact finite-dimensional reduction (proved)

For any finite set D of square-lattice sites let p_j=|{x in D:s(x)=j}|/|D|, j=0,1,2,3. Put m_0=1, m_1=average s, m_2=average binom(s,2), m_3=average binom(s,3). Direct evaluation at the four possible heights gives

m_1=p_1+2p_2+3p_3, m_2=p_2+3p_3, m_3=p_3.

Solving these triangular equations gives

p_3=m_3,
p_2=m_2-3m_3,
p_1=m_1-2m_2+3m_3,
p_0=1-m_1+m_2-m_3.

These identities prove that, given the Pegden–Smart mean convergence on B, convergence of all four frequencies is equivalent to convergence of the two factorial moments m_2 and m_3 on B. Necessity holds since each moment is a fixed linear combination of frequencies; sufficiency follows from the displayed inverse. This is a reduction, not a proof that the extra moments converge. MomentChecks.lean formalizes the inversion over the rationals, which contain every finite-site frequency.

## 2. Weak-* convergence plus recurrence still does not suffice (proved obstruction)

Here the objects are arbitrary recurrent configurations, NOT stabilization of n delta_0 and NOT identities. On lattice spacing 1/N, alternate the constant height-2 configuration with the checkerboard taking height 1 when x_1+x_2 is even and height 3 otherwise. Extend each value constantly over its half-open lattice square. Both kinds converge weak-* to constant 2, while the height-2 fraction on every fixed positive-radius ball alternates between 1 and 0.

Proof of convergence. In each 2-by-2 lattice-square block the checkerboard minus 2 has integral zero. For a compactly supported continuous test function, subtract its value at one point of each block; the remaining integral is bounded by the support area enlarged by O(1/N), times its modulus of continuity at 2 sqrt(2)/N. This tends to zero. Boundedness by 1 extends the conclusion to all L^1 tests by approximation by compactly supported continuous functions. Constant arrays already have the stated limit.

Both configurations are recurrent on every finite wired square domain (using the standard forbidden-subconfiguration characterization of recurrence). For constant height 2, a nonempty subset X has a vertex of maximal first coordinate and, among those, maximal second coordinate. It has at most two neighbors in X, so its height is at least its indegree. Thus X is not forbidden. For the checkerboard, consider a vertex of maximal first coordinate in X. If its height is 3 it has at most three neighbors in X, and again X is not forbidden. If its height is 1 and it has a vertical neighbor in X, that neighbor is height 3 and has the same maximal first coordinate, hence indegree at most 3. If it has no vertical neighbor in X, it has at most its left neighbor in X, hence indegree at most 1. Every case supplies a vertex with height at least indegree, excluding a forbidden subconfiguration. This proves recurrence.

This refutes a possible argument based only on mean convergence and recurrence. It is not a counterexample to C0100: the input configurations and toppling equivalence classes change.

## 3. Local translated-pattern convergence implies frequency convergence (proved)

Let P be an open set, p:Z^2->{0,1,2,3} be periodic under a full-rank sublattice, and f_j be its frequency over that sublattice. Choose an integer a>=1 with a Z^2 contained in the period lattice; such a exists by taking the index of the sublattice. For configurations t_N, suppose the following for every ball C with closure in P and every fixed sufficiently large r: all but o(N^2) centers in NC intersect Z^2 have t_N equal to some translation of p throughout their radius-r neighborhood. The translation can depend arbitrarily on the center and on N. Then for every bounded Jordan set D with closure in P,

N^(-2) #{x in ND intersect Z^2:t_N(x)=j} -> |D| f_j.

Proof. Cover the compact closure of D by finitely many balls with closure in P. For fixed r the union bound shows that only o(N^2) centers in ND are bad. Choose m divisible by a, and fix r>2 sqrt(2)m large enough for the hypothesis. The window W={-m,...,m-1}^2 contains exactly equal numbers of every residue class modulo a in both coordinates. Therefore any translated pattern has exactly |W| f_j sites of height j in that window. For each center x define A_N(x)=|W|^(-1) sum_{z in W} 1_{t_N(x+z)=j}. At a good center A_N(x)=f_j; at a bad center its difference from f_j is at most 1. Hence

sum_{x in ND intersect Z^2} A_N(x)=f_j #(ND intersect Z^2)+o(N^2).

Interchanging the finite sums shows that the difference from sum_{x in ND intersect Z^2}1_{t_N(x)=j} is bounded by

|W|^(-1) sum_{z in W} #((ND intersect Z^2) symmetric_difference ((ND intersect Z^2)+z)).

For each fixed z this is o(N^2): after scaling by 1/N the symmetric difference lies in an O(1/N) neighborhood of the boundary of D. Since D is bounded Jordan measurable, its boundary is compact and null; covering it by finitely many boxes of arbitrarily small total area and using elementary box lattice counts proves the bound. Also #(ND intersect Z^2)/N^2 -> |D| by the same Jordan counting argument. Combining proves the conclusion. This window argument is necessary: equality to a different translated pattern at each single site would convey no frequency information.

The argument also applies with scale N any positive real tending to infinity; integer scale was not used in the lattice-counting proof. Thus N=sqrt(n) is allowed.

## 4. Countably many open patches: no uniform boundary-layer bound needed (proved conditional criterion)

Suppose disjoint open patches P_i cover a ball B up to a null set. On each P_i suppose the hypothesis of section 3 holds with periodic p_i, and let f_{i,j} be its frequency. Then

F_n(B,j) -> |B|^(-1) sum_i |B intersect P_i| f_{i,j}.

No Jordan condition on P_i and no dimension estimate on their combined boundary is required.

Proof. Given epsilon>0, choose finitely many patches whose intersections with B have total area greater than |B|-epsilon. Inside each of these open intersections choose finitely many closed axis-parallel boxes with pairwise disjoint interiors, lying a positive distance from its boundary, whose total area approximates that intersection within epsilon divided by the number of chosen patches. Such boxes exist by the inner regularity of Lebesgue measure, or by the increasing unions of dyadic boxes compactly contained in the open set. Treat box edges as omitted; they have zero area and o(N^2) lattice sites. We obtain a finite union K of Jordan boxes, closure inside the respective patches, with |B\K|<2epsilon. Apply section 3 to every box and sum. The omitted lattice sites contribute at most #(NB intersect Z^2)-#(NK intersect Z^2)=N^2|B\K|+o(N^2), since both sets are Jordan measurable and the boxes have disjoint interiors. The omitted target integral also has magnitude at most |B\K|, as 0<=f_{i,j}<=1. The normalized discrepancy has limsup at most 4epsilon. Let epsilon tend to zero and divide by |B|. Heights outside 0,...,3 have frequency zero throughout.

This improves the earlier conditional criterion by permitting different local phases, arbitrary open patches, and no prescribed transition-layer width. Its application to the actual point-source pile remains conditional on an almost-everywhere cover and the pattern hypotheses.

## 5. Quadratic limiting patches yield local frequencies (proved conditional application)

Conventions. Write Gamma_3 for attainable quadratic Hessians with discrete Laplacian at most 3, Gamma_2 for the bound 2 convention in Pegden–Smart 2020. Let E=diag(1,0). The integer polynomial q(x)=x_1(x_1+1)/2 has Delta q=1; hence Gamma_2=Gamma_3-E, and the isolated extremal classes Gamma_2^+ and Gamma_3^+ correspond by that translation. In this section, a maximal pattern means the pattern supplied for a matrix in Gamma^+, not an arbitrary matrix on the boundary of Gamma.

Claim. Let U be the locally uniform limit of u_n/n on R^2\{0}, with N=sqrt(n). Suppose P is an open subset of {U>0}\{0}, and U on P is a quadratic polynomial with Hessian A in Gamma_3^+. Then on every bounded Jordan set D with closure in P, the height frequencies of s_n converge to those of the canonical periodic pattern associated to A.

The external ingredients are Pegden–Smart 2013, Theorem 4.2 and the fundamental-solution normalization (locally uniform odometer convergence away from 0), and Pegden–Smart 2020, Proposition 8, Lemma 13 and Theorem 10 (pattern witnesses, approximation of arbitrary slopes, and pattern stability). Theorem 10's proof is local: its uses of recurrence are inside B_R, via Lemma 14. Thus it applies to a function recurrent in B_R, with values on its neighboring boundary. We justify that local recurrence for u_n below rather than assume that u_n is globally recurrent (it is not globally recurrent).

Local recurrence lemma. On any finite Y in a region where u_n>=1, excluding 0, if w is integer-valued and Delta w<=3 in Y, then

max_Y(u_n-w) <= max_{partial Y}(u_n-w),

where partial Y is the outer nearest-neighbor boundary. Proof: let c=max_{partial Y}(u_n-w). If M=max_Y(u_n-w)>c, integrality gives M-1>=c. Define z=u_n outside Y and z=min(u_n,w+M-1) in Y. Everywhere z>=u_n-1>=0 in Y, and outside z>=0. At a site where z=u_n, all neighbor values weakly decreased, so Delta z<=Delta u_n. At a lowered site, z=w+M-1; for neighbors inside Y one has z<=w+M-1 by construction, and for neighbors outside Y one has z=u_n<=w+c<=w+M-1. Thus Delta z<=Delta w<=3 there. No lowered site is the origin, so n delta_0+Delta z<=3 throughout the lattice. At the origin or any other unchanged site the inequality follows from Delta z<=Delta u_n. This z is a nonnegative integer stabilizing comparison function, smaller than u_n at a maximizer of u_n-w. This contradicts the least-action principle. The local maximum principle follows. Subtracting q transforms this recurrence inequality to the bound-2 convention.

Proof of the claim. Fix a ball C whose closure and a slightly larger concentric ball are compactly contained in P. At scale N choose a nearby lattice center x_N and a lattice ball of radius R_N=cN whose rescaled closure lies in that larger ball, with c>0 fixed. For large n all sites in this ball and its outer boundary have u_n>=1, since U has a positive minimum there. Define, in centered coordinates z,

v_n(z)=u_n(x_N+z)-q(z).

This is integer-valued, recurrent locally with Delta v_n<=2. Let

Q_n(z)=N^2 U((x_N+z)/N)-q(z).

Its Hessian is H=A-E in Gamma_2^+, and it is a quadratic polynomial whose affine part depends on n. Locally uniform convergence gives

sup_{|z|<=R_N+1}|v_n(z)-Q_n(z)|=o(N^2).

By Proposition 8 choose the canonical integer recurrent witness o with Hessian H, and a quadratic q_H with o-q_H bounded. Lemma 13 says that for any real slope b there is a translation tilde_o (allowing integer affine additions) with

|tilde_o(z)-o(z)-b dot z|<=C_H(1+|z|).

Apply this to the difference of the affine parts of Q_n and q_H, and add a nearest integer constant to tilde_o to fit the constant term. The resulting translation o_n satisfies

sup_{|z|<=R_N+1}|Q_n(z)-o_n(z)|<=C_H(1+R_N).

In particular a_n:=sup|v_n-o_n|=o(N^2). Set h_n=max(C_H,N^(1/4),sqrt(a_n)). Then h_n/N->0. For any fixed sufficiently large r (depending on H), the hypotheses h_n>=C, r>=C|V|, h_n r>=C|V|^3, and R_N>=C h_n r of Theorem 10 hold eventually. That theorem gives, at all but an O(r h_n/R_N)=o(1) fraction of centers in B_{R_N-r}, equality v_n=some translation of o_n throughout B_r at that center. Taking Laplacians loses at most one unit of radius, so s_n=Delta v_n+1 equals a translation of p_A:=Delta o+1 in B_{r-1}. This last '+1' is essential to match the original bound-3 heights. The fixed-width annulus between R_N-r and R_N has o(N^2) sites. Cover any smaller compact set by finitely many such balls; the bad centers remain o(N^2). Section 3 now gives the claimed frequencies on D.

Consequences and limits. No rate of convergence of the odometer is required here: h_n=o(N) suffices with r fixed. No global phase of the pattern is required. If the point-source limiting odometer admitted an almost-everywhere cover by such maximal quadratic patches (with a separately controlled exterior), section 4 would give the desired height-frequency conclusion. We have NOT proved that cover. In particular, almost-everywhere twice differentiability or a.e. membership in the boundary of Gamma does not by itself imply membership in the isolated subset Gamma^+, let alone an open quadratic patch. The source's Apollonian theorem is not a proof of that missing assertion.

## 6. Full one-dimensional special case (proved)

On Z with threshold 2, for k>=0 the stabilization of 2k+1 grains is height 1 on [-k,k] and 0 elsewhere; for k>=1 the stabilization of 2k grains is height 1 on [-k,k]\{0} and 0 elsewhere. Thus on any interval B of positive length under spatial scale n,

F_n(B,1) -> |B intersect [-1/2,1/2]|/|B|,
F_n(B,0) -> 1-|B intersect [-1/2,1/2]|/|B|,

and all other height fractions are zero.

Proof of the exact configurations by induction using legal topplings. Begin with n=1. From the even configuration 2k, adding one grain fills its empty origin and gives the stated odd configuration 2k+1 without toppling. From the odd configuration, add one grain at 0. Its height is now 2. Perform stages t=k,k-1,...,0, in each stage toppling 0, then 1,2,...,t, then -1,-2,...,-t (the side lists are empty when t=0). Before the first stage all sites 1<=|x|<=k have height 1 and the center has height 2. After the first center toppling each side sweep is legal: the next site has received one grain, going from 1 to 2; its toppling sends one grain forward and one backward. At the end of a stage t>=1 the center has received one grain from each side and has height 2; sites 1<=|x|<t have height 1, the two sites |x|=t have height 0, and the previous holes at |x|=t+1 (or the unoccupied exterior at the first stage) are filled with height 1. Thus the next stage t-1 satisfies the same conditions. In the final stage t=0 the center becomes 0 and fills the two holes at +/-1. The result is height 1 on [-k-1,k+1]\{0}. All moves were legal and the result stable, so Abelian uniqueness proves the formula for 2k+2. The induction is complete.

For completeness, with k=floor(n/2), the odometer in both cases is

u_n(x)=((k-|x|)(k-|x|+1))/2 for |x|<=k, and 0 otherwise.

The sweep counts prove this: passage from 2k+1 to 2k+2 adds k+1-|x| topplings for |x|<=k and none beyond; this is exactly the difference of the displayed formulas at k+1 and k. Passage from even to odd adds no topplings. The base k=0 is zero. Counting integer points in the interval intersection gives the frequency limits, with at most O(1) error from the origin and interval endpoints; floor(n/2)/n->1/2.

This settles d=1, not the intended planar question. It supplies an exact small/boundary case rather than a claim of planar resolution.

## 7. Frequencies on extreme-mean balls (proved special case in all dimensions)

Let H=2d-1. On a fixed ball B let the mean heights tend to mu_B, as supplied by weak-* convergence. Since heights are nonnegative integers, 1_{s_n!=0}<=s_n, so if mu_B=0 then F_n(B,0)->1 and every other frequency tends to 0. Likewise 1_{s_n!=H}<=H-s_n, so if mu_B=H then F_n(B,H)->1 and all other frequencies tend to 0. This uses neither geometry nor periodicity and applies to the actual point-source model. It says nothing about balls with intermediate mean.

## 8. A sharper a.e.-Hessian criterion (proved conditional reduction)

This replaces the need for an open quadratic-patch cover. Let S be the set of points x!=0 where U(x)>0, U is twice differentiable in the pointwise Taylor-expansion sense, and D^2U(x) belongs to Gamma_3^+. Suppose almost every point of R^2 is either in S or has limiting mean height s(x) equal to 0 or 3. Then all four height-frequency fields converge weak-*; consequently the requested fractions converge on every ball. At x in S their limiting frequencies are f_j(D^2U(x)), the canonical-pattern frequencies; at mean-0 or mean-3 points they are respectively the unit vectors at 0 or at 3.

All membership and coverage assumptions in this statement are hypotheses, NOT established facts about the point-source limit. The relevant matrices in Gamma_3^+ are the countable isolated maximal matrices with canonical patterns from LPS/Pegden–Smart, so the frequency function on S is measurable. Equivalently the conclusion's measurability follows from the weak-* subsequential limit identified below.

Proof. Extend the indicator 1_{s_n=j} constantly over lattice squares of side 1/N, N=sqrt(n). These functions take values in [0,1]. From any subsequence, extract a further subsequence for which the four indicators converge weak-* locally to g_j, using Banach–Alaoglu, separability of L^1 on bounded sets, and a diagonal exhaustion by balls. Then g_j>=0, sum_j g_j=1, and sum_j j g_j=s almost everywhere. The last equality follows from the supplied weak-* convergence of s_n and the exact pointwise linear identity. At points where s=0 or 3, nonnegativity and these two equations force the asserted unit vectors.

It remains to identify g_j almost everywhere in S. Fix x in S which is a Lebesgue point of each of the four g_j; this excludes only a null set. Write A=D^2U(x). For any sufficiently small rho, the closed ball B_{2rho}(x) lies away from 0 and in {U>0}. Twice differentiability gives a quadratic Taylor polynomial Q_x with Hessian A and

sup_{|y-x|<=2rho}|U(y)-Q_x(y)| <= e(rho) rho^2,

where e(rho)->0. At scale N, compare u_n on the lattice ball of radius R=N rho centered at a nearest lattice point to Nx to the polynomial N^2 Q_x(y/N). Uniform odometer convergence gives an error e(rho) R^2+o_rho(N^2); the subscript emphasizes that rho is fixed while n tends to infinity. Center rounding introduces O_rho(N) errors, absorbed in o_rho(N^2). After subtracting the integer q with Delta q=1, the Taylor Hessian is A-E in Gamma_2^+. Lemma 13 and Proposition 8 fit its affine part by a translated canonical witness with additional O_A(R+1) error, exactly as in section 5. Local recurrence follows from the least-action lemma, since the ball is inside a positive-U region.

Fix r_A large enough for Theorem 10 and to contain an a-period square window for this pattern together with its nearest neighbors. Choose h so that

h>=C_A, h^2>=e(rho)R^2+o_rho(N^2)+O_A(R+1),

and h/R has limsup at most sqrt(e(rho)); one may add N^(1/4) to h to satisfy the lower-bound hypotheses. For rho sufficiently small, C_10 r_A sqrt(e(rho))<1/2. The hypotheses R>=C_10 h r_A and h r_A>=C_10|V_A|^3 then hold for large n, increasing the negligible N^(1/4) term if necessary. Theorem 10 bounds the bad fraction by C_A r_A h/R. The fixed outer annulus and the window-boundary error are O_A(r_A/R), which tends to zero. The translated-period window argument of section 3 therefore implies

limsup_{n->infinity} | average_{B_rho(x)} 1_{s_n=j} - f_j(A) |
 <= C_A sqrt(e(rho)).

Here average over lattice points and average over lattice-square extensions differ by o(1) for each fixed rho: only cells meeting the sphere contribute, their total area is O(rho/N+N^(-2)), and the fields are bounded. Along the extracted subsequence the average converges to the average of g_j on the ball because its indicator is an L^1 test. Thus

| average_{B_rho(x)} g_j - f_j(A) | <= C_A sqrt(e(rho)).

Let rho tend to zero. The Lebesgue differentiation theorem and e(rho)->0 give g_j(x)=f_j(A). This identifies every subsequential limit with the same four densities almost everywhere under the stated coverage assumption. If the original sequence failed weak-* convergence against some compactly supported L^1 test, a subsequence with discrepancy bounded below would have a convergent further subsequence, contradicting this uniqueness. Exhaustion and boundedness extend the conclusion to arbitrary L^1 tests. Taking indicators of balls and dividing by their area proves all ball-frequency limits. The sphere-cell comparison above converts these integral averages back to site fractions.

Precise new bottleneck. It suffices to prove that, at almost every point with intermediate mean height 0<s(x)<3, U(x)>0 and its second-order Taylor Hessian belongs to Gamma_3^+. The known viscosity constraint D^2U in partial Gamma_3 is weaker. This reduction is not a proof of that missing isolated-maximal-Hessian assertion. The square identity question still requires a separate analysis of the zero equivalence class with its own boundary problem; this theorem does not identify that limit.

## 9. Consequence of the ellipse theorem (proved special case, using literature)

For a positive-definite A in Gamma_3^+ lying in the fundamental domain corresponding to (x,y) in [0,2]^2, as required in section 4 of Melchionna's paper (in particular 0<lambda_1<=1<lambda_2), covered by Theorem 4.3, let E_A={x: x^T A x/2<1} and let e_{A,k} be the recurrent identity on sqrt(k) E_A intersect Z^2 with the exterior wired to a sink. For every ball B, the fractions among the sites in sqrt(k)(B intersect E_A) tend to the periodic frequencies f_{A,j}, provided |B intersect E_A|>0. Extending the identity by zero outside the ellipse instead gives the ball fraction

(|B intersect E_A| f_{A,j} + |B\E_A| 1_{j=0})/|B|.

Proof. Take r fixed large enough to exceed both 3|V_A|^3 and a full-period square-window radius plus one. Theorem 4.3, printed/PDF p. 13, states that the fraction of non-r-good sites in the radius-r inner ellipse is O_A(r k^(-1/4)). Equality of odometers in Br implies equality of height patterns in B_{r-1}, since computing a Laplacian uses one extra nearest-neighbor layer. The ellipse boundary layer has O_A(r sqrt(k)+r^2)=o(k) sites, using its smooth perimeter and elementary lattice-square covering. Hence the bad centers in the whole ellipse are o(k). Restricting to any fixed B intersect E_A retains that bound. This intersection is Jordan measurable, since its boundary is contained in a circle and an ellipse, both null curves. Apply the window averaging proof of section 3 at scale N=sqrt(k), first on inner compact Jordan sets and then exclude a small boundary strip, or directly bound fixed-window shifts by the smooth boundaries. The outside-zero contribution follows by Jordan lattice counting. No claim is made for arbitrary ellipses or square identities.

## 10. Computations and hostile-referee audit

Exact implementation: experiments.py uses legal bulk topplings with a deque and a per-site queued flag. A bulk toppling at height h performs floor(h/4) ordinary legal topplings. Four-neighbor boundary edges go to the sink. For point-source experiments the box half-width is ceil(sqrt(n))+3; this choice is NOT used as a theoretical radius estimate. In each run, total final mass equals n and no boundary site toppled, verifying that this finite computation also represents the infinite lattice. Experiments were saved line by line to experiments.jsonl.

Point-source n=256,1024,4096,16384 were counted in the scaled balls (center,radius) ((0,0),.2), ((0,0),.5), and ((.25,.25),.1). For the first ball the four frequencies at n=16384 were approximately (.0820,.1747,.2969,.4464). Across these sizes the frequencies fluctuate; this is no evidence of either convergence or nonconvergence at infinity.

For wired squares with L=9,18,36,72 nonsink vertices per side, the candidate identity was computed as stabilize(6-stabilize(6)), with sitewise constants. It was then checked independently to be idempotent under addition/stabilization and to pass Dhar's burning test with every nonsink site toppling once. The latter proves recurrence, and a recurrent idempotent is the group identity. Thus these finite identities were validated; no continuum limit follows from finitely many values. At L=72 the whole-square frequencies were approximately (.0980,.0324,.3711,.4985). The run took about 19 seconds, with small arrays far below 1 GB.

finite_checks.py verifies the exact one-dimensional configuration and odometer formulas for n=1,...,200, enumerates all 511 nonempty subsets of a 3-by-3 wired square for each of the two recurrent obstruction patterns, and checks the factorial-moment inversion on all 624 nonzero four-tuples of weights in {0,...,4} using Fraction arithmetic. independent_checks.py compares the deque implementation with a synchronous parallel toppling implementation at n=16,64,256,1024, and checks the full discrete Laplacian/odometer identity.

MomentChecks.lean imports only Mathlib.Data.Rat.Defs and Mathlib.Tactic.Ring. It formalizes the factorial-moment inversion, a mass/mean-preserving direction over Q, and the exhaustive factorial-moment table for the four heights via decide +kernel. Final command: lake env lean ~/brain_workers/TRIO_1011/op/C0100/MomentChecks.lean, from ~/lean_verify, timeout 3600 seconds; exit 0. The first run failed because PowerShell had inserted a UTF-8 BOM; Python rewrote the file without it, and the final run succeeded. There is no sorry, axiom declaration, native_decide, or unverified placeholder in the checked file. The algebraic check is kernel-checked; the analytic reductions are handwritten proofs using the cited external theorems, not formalized analytic theorems.

Potential failure points and resolutions:

1. Confusing mean convergence with nonlinear indicator convergence: explicitly blocked by the recurrent checkerboard example and the two missing factorial moments.
2. Counting a separately translated pattern at each site: invalid. A full-period window and double counting are used, so arbitrary phase changes cannot bias the limiting histogram away from the periodic histogram.
3. Summing infinitely many boundary layers: avoided. Section 4 first retains finitely many compact boxes and uses the Jordan remainder; no uniform control of the entire gasket is asserted.
4. Using the wrong toppling cutoff: tracked by the integer polynomial q, with Delta q=1. Pattern-stability witnesses have bound 2; original heights are Delta v+1 and take values 0,...,3.
5. Assuming recurrence of the source odometer globally: false. A finite-domain recurrence comparison is proved from least action only inside a strictly positive odometer region away from the source; Theorem 10's proof uses that local property via its local Lemma 14.
6. Obtaining height equality from odometer equality without neighboring sites: corrected by losing one unit of matching radius before taking Laplacians.
7. Applying pattern stability with a large arbitrary linear slope: Lemma 13 fits the slope by a translated witness with O(R) error, which is negligible compared with N^2.
8. Needing an odometer convergence rate: not necessary for section 5; fixed pattern-radius r and h_n=o(N) suffice. In section 8 the order of limits is n->infinity for fixed rho, then rho->0; no interchange of limits is made.
9. Treating a.e. viscosity Hessians as isolated maximal Hessians: NOT justified; this is the remaining substantive assumption in section 8, rather than a step claimed as proved.
10. Mistaking the bound-2 square-domain theorem for the standard identity: the paper explicitly says Delta u_n+1 is equivalent to all ones, while the identity is equivalent to all zeros. A threshold shift changes the boundary data and does not identify the two equivalence classes.
11. Treating ellipse or Sierpinski results as wired-square results: neither has the requested objects. Section 9 retains the ellipse paper's fundamental-domain and positive-definiteness hypotheses.
12. Treating successful finite stabilization as infinite-lattice stabilization: conservation and zero boundary topplings certify that no sink effect reached the computed point-source pile. Independent legal schedules are checked on small sizes.
13. Claiming numerical trends solve the problem: expressly not done.

## 11. Remaining gaps and final assessment

No complete proof or counterexample for the planar point-source height-fraction question was obtained, and no exact solution in print was located. The most useful reduction is section 8: prove the isolated-maximal-Hessian condition almost everywhere at intermediate limiting densities, or supply some different mechanism that identifies the two missing factorial moments. The existing Apollonian structure theorem and viscosity constraint do not prove this assumption. A positive-measure set of non-maximal Hessians could require a different approach; its existence or absence has not been proved here.

At the end of the first pass, the standard wired-square identity weak limit had not been established here. This is superseded by the second attempt below: weak-* convergence and an implicit Dirichlet characterization are now proved in SECOND_ATTEMPT.md A1-A5. The 2020 paper's explicitly patterned cutoff-2 square model remains a different recurrent class. Explicit identity patch geometry and exact-height frequencies are still not identified.

Literature coverage is bounded rather than exhaustive: arXiv and Crossref queries succeeded, and GitHub repositories were screened. OpenAlex source resolution and citation-list retrieval could not be completed because the unauthenticated shared-IP daily quota was exhausted; Semantic Scholar search requests returned 429, but its final direct source-citations request succeeded with 32 records; these were screened and selected leads were fetched. These failures are saved in LITERATURE.md and search_log.json. Thus the correct verdict is PARTIAL, not SOLVED or SOLVED_IN_LITERATURE. This attempt is complete with the above gaps stated for a future continuation.


## 12. Second serious attempt (2026-10-12)

Two new approaches were written before pursuing one: (A) derive the standard zero-class identity directly from an integer cutoff-3 Dirichlet problem and adapt the general comparison machinery; (B) seek fixed-Hessian periodic recurrent microstructure counterexamples or rigidity, improving on the old same-mean obstruction. The gap-specific brain queries supplied no theorem closing the gap.

Approach A was pursued to a proof of weak-* convergence of the actual wired-square identity, uniform convergence of its least integer Dirichlet potential, and a unique implicit a.e.-Hessian boundary-value characterization. Its limiting mean density lies in [2,3] almost everywhere. Full proofs, a hostile-referee audit, exact numerical potential certificates, and the remaining gaps are in SECOND_ATTEMPT.md. This corrects the first pass's absence of an identity weak-limit existence result. It does not solve the point-source height-fraction refinement or calculate the identity's individual-height frequencies or explicit patch geometry. Overall verdict: PARTIAL.
