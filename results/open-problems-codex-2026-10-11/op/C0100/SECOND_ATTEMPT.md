# C0100: second serious attempt (2026-10-12)

## Gap reread and two untried approaches

The first attempt's main point-source gap is isolated-maximal Hessian membership almost everywhere at intermediate limiting density. It also leaves the standard wired-square identity limit unidentified. The previous periodic-patch and two-scale arguments do not settle either gap.

**Approach A: the identity as an integer Dirichlet problem.** Prove the exact finite identity equals the Laplacian of the pointwise least integer function v with Delta v<=3 inside and v=0 outside. Then use the general integer-superharmonic continuum comparison mechanism (or its viscosity Dirichlet problem) at cutoff 3, without shifting to the all-ones recurrent class. This may establish a weak-* identity limit or a precise reduction to an existing Dirichlet convergence theorem without proving any patch geometry. The first attempt inspected the ellipse special case but did not pursue this general boundary-value route.

**Approach B: fixed-Hessian microstructure rigidity or counterexamples.** Seek two integer quadratic-plus-periodic locally recurrent functions with the SAME Hessian and different height histograms. The old recurrent checkerboard obstruction had only the same mean, not the same Hessian. A fixed-Hessian counterexample would refute a broad replacement for the isolated-maximal-Hessian hypothesis; conversely a rigidity theorem might identify frequencies on non-maximal Hessians and remove that gap. A concrete bounded search can enumerate periodic corrections and test forbidden subconfigurations, rather than simulating further point-source sizes.

I pursue A first because it addresses an actual requested family and exposes a precise distinction between the zero-class and all-ones-class boundary problems. B remains a secondary explicit construction search if A stalls.

## Brain query

Read-only math_recall.py on "sandpile isolated maximal Hessian Gamma positive density Pegden Smart pattern stability" returned the same older conditional patch argument, plus the LPS structure references. It did not provide a result establishing the gap. A second query targets "sandpile identity least integer Dirichlet recurrent representative Melchionna Pegden Smart". Brain suggestions are not treated as proofs.

## A1. Finite Dirichlet representation of the actual identity (proved)

Let D be a finite subset of Z^2, all exterior edges wired to one sink, with lattice degree 4 retained. Let Delta use zero extension to the exterior. Define

F_D={v:Z^2->Z : v=0 on D^c, Delta v<=3 on D}.

This family has a pointwise least member v_D, and the recurrent identity is e_D=Delta v_D restricted to D.

Proof of existence. The zero function belongs to F_D. Let w be the real solution Delta w=3 in D, w=0 on the outer boundary. It exists because the reduced graph Laplacian is invertible: its negative has quadratic form sum over interior edges (f(x)-f(y))^2 plus sum over sink edges f(x)^2, strictly positive for nonzero f since each component connects to the exterior. If v belongs to F_D, Delta(v-w)<=0 and v-w=0 on the boundary, so the discrete minimum principle gives v>=w. Hence all admissible integer values at each site are bounded below. Their infimum is an attained integer. A finite minimum of members of F_D remains admissible: at a point where the minimum selects v, all neighbor values are at most those of v, so its Laplacian is at most Delta v. Select one admissible member attaining the minimum at each of the finitely many sites and take their finite minimum. This gives the pointwise least member, and zero admissibility implies v_D<=0.

Proof of stable heights and recurrence. By definition Delta v_D<=3. If Delta v_D(x)<=-1, lowering v_D by 1 just at x changes its Laplacian by +4 there and by -1 at each neighbor. It still has Laplacian at most 3 throughout D and zero exterior, contradicting leastness. Thus 0<=e_D<=3. If X is a forbidden subconfiguration, e_D(x)<indeg_X(x) for every x in X. Lower v_D by 1 on X. At each x in X the new Laplacian is e_D(x)+4-indeg_X(x)<=3 by integrality. At every point of D\X it decreases. This is another admissible function, contradicting leastness. Therefore e_D has no forbidden subconfiguration and is recurrent by Dhar's finite undirected burning characterization. It is in the zero toppling-equivalence class because it is a reduced integer Laplacian. The uniqueness of the recurrent representative in every class proves that it is exactly the identity.

This is not a claim of novelty; Melchionna's paper gives the same representation for its ellipses. The proof here explicitly checks it for arbitrary finite wired domains and is used below for squares.

## A2. Square barriers and compactness (proved)

Set D_L={1,...,L}^2, N=L+1, h=1/N, Omega=(0,1)^2, v_L=v_{D_L}, e_L=Delta v_L. Rescale V_L(x)=N^(-2)v_L(round(Nx)), using nearest-neighbor interpolation and zero outside. For a lattice point (i,j) in D_L,

-(3/2) min{i(N-i),j(N-j)} <= v_L(i,j) <=0.                (A.1)

Proof. The polynomial w_x(i,j)=(3/2)i(i-N), on the whole lattice, has Delta w_x=3. On the outer boundary of D_L its value is zero at i=0,N and nonpositive on j=0,N. Since v_L=0 there and Delta(v_L-w_x)<=0 inside, the minimum principle gives v_L>=w_x. Apply the same argument to w_y. The larger of these two lower bounds is the left side of (A.1). In rescaled coordinates this gives |V_L|<=3/8 and |V_L(x)|<=(3/2)dist(x,partial Omega)+O(h). This is a uniform boundary modulus.

Every sequence L->infinity has a subsequence on which V_L converges uniformly on the closed square to a continuous V with V=0 on the boundary. Indeed, Delta_h V_L=e_L belongs to [0,3] at interior lattice sites. Pegden–Smart 2013 Proposition 2.3 (local discrete Poisson compactness), applied to finitely many balls in each compact interior subset and followed by a diagonal argument, gives locally uniform subsequential convergence. The boundary modulus extends convergence to the closed square: choose a thin strip where all V_L and V are uniformly small, and use interior uniform convergence on the complement.

Along a further subsequence the bounded fields E_L, obtained by extending e_L over the nearest-neighbor cells and setting them to zero outside Omega, converge weak-* to g in L^infinity(Omega), with 0<=g<=3. Discrete summation by parts against any smooth test supported strictly inside Omega gives Delta V=g distributionally there. More explicitly, h^2 sum_x E_L(x) phi(x)=h^2 sum_x V_L(x) Delta_h phi(x), with support away from the boundary for small h. Riemann-sum and cell-extension errors vanish; Delta_h phi->Delta phi uniformly, and V_L->V uniformly on the support. This proves the distributional identity.

Standard interior Poisson regularity, also used in Pegden–Smart Proposition 2.4, gives V in W^{2,p}_loc for finite p and twice differentiability almost everywhere; its gradient is locally bounded. The latter follows, for example, by cutting off the bounded Poisson right-hand side and convolving with the fundamental solution, whose gradient is locally integrable in dimension 2, leaving a smooth harmonic remainder.

Important boundary correction: the zero extension of v_L has Delta v_L<=0 at exterior sites, but may have magnitude O(N) there. Therefore global absolute-Laplacian bounds must NOT be assumed. Compactness and Delta V=g are asserted inside Omega. The global one-sided bound Delta v_L<=3 nevertheless holds, because exterior neighbors have v_L<=0; that is exactly the hypothesis needed by Lemma 4.1.

## A3. A contact lemma on the square from the published ball lemma (proved application)

Let F be continuous on the closed square, zero on its boundary, and Delta F bounded in the interior. If max F>0, there is a positive-measure set of interior points a with F(a)>0, F twice differentiable, and D^2F(a) negative definite.

We cannot simply assume an inscribed ball contains the whole positive maximum set. To obtain the result from Pegden–Smart Proposition 2.5, choose c=(max F)/4 and a smooth convex nondecreasing function theta:R->R with theta=0 on (-infinity,c], theta'>0 on (c,infinity), and bounded first two derivatives on the range of F. Such a function is obtained by integrating a smooth increasing derivative that is zero up to c, positive thereafter, and equals 1 past 2c. The function H=theta(F) is identically zero in a neighborhood of the square boundary, since F=0 there and continuity makes F<c on a boundary strip. Extend H by zero to a ball containing the square. Its Laplacian is

Delta H=theta'(F)Delta F+theta''(F)|DF|^2,

which is bounded because the support of theta' is compactly contained in the square and DF is locally bounded. This weak chain rule follows from W^{2,p}_loc regularity, by smooth approximation on that compact support. H has positive maximum and zero ball-boundary values. Published Proposition 2.5 gives a positive-measure set where H>0 and D^2H<0. Intersect it with the full-measure sets of twice differentiability of F and any other finitely many Poisson solutions under consideration. At these points theta'(F)>0 and

D^2H=theta'(F)D^2F+theta''(F)DF tensor DF.

The second term is positive semidefinite. Thus D^2H<0 forces D^2F<0, while H>0 implies F>c>0. This proves the claim with all domain changes justified.

## A4. Weak-* convergence of the wired-square identity (proved)

**Theorem.** On D_L={1,...,L}^2 with wired exterior, the standard recurrent identity e_L, under spatial rescaling by N=L+1 and zero extension outside the unit square, converges weak-* in L^infinity(R^2) to a unique bounded density e. Its least integer Dirichlet potential V_L converges uniformly to a continuous potential V on the closed square, V=0 on its boundary, and e=Delta V in the interior. This asserts weak-limit existence and the characterization below, not height-indicator convergence or explicit patch geometry.

Proof of uniqueness of the potential. Suppose two subsequences give distinct limits V and W. Swap them if necessary so max(V-W)>0. Both have bounded interior Laplacian by A2. Apply A3 to F=V-W and intersect the positive-measure contact set with the full-measure sets where V and W are twice differentiable. We obtain a in Omega, V(a)>W(a), and

D^2V(a)<=D^2W(a)-2 epsilon I

for some epsilon>0.

Apply Pegden–Smart 2013 Lemma 4.1, with K=3, to the integer functions in the subsequence converging to W. They have Delta v_L<=3 on the WHOLE lattice: inside by definition, outside because their zero extension has nonpositive neighboring values. Their scaled functions converge uniformly near a; their lattice spacing is h=1/N, which is precisely the paper's d=2 scale with n=N^2. The lemma supplies an integer function o:Z^2->Z with

Delta o<=3,
o(z)>= (1/2)z^T(D^2W(a)-epsilon I)z
      >= (1/2)z^T(D^2V(a)+epsilon I)z                    (A.2)

for all z in Z^2.

We use this witness to contradict leastness along the subsequence converging to V. Let a_N be a nearest lattice point to Na, and l_N be coordinatewise rounding of N DV(a). Choose r>0 so B_{2r}(a) is contained in Omega and the Taylor remainder of V at a is at most (epsilon/64)r^2 throughout B_{2r}(a); shrinking r guarantees this by twice differentiability. Uniform convergence and a_N/N=a+O(1/N) imply, for all sufficiently large N and |z|<=rN,

v_L(a_N+z) <= v_L(a_N)+N DV(a) dot z
              +(1/2)z^T D^2V(a)z +(epsilon/32)r^2 N^2.     (A.3)

Here the Taylor-remainder error at each of the two compared points is at most a fixed fraction of epsilon r^2 N^2, the convergence errors are o(N^2) for fixed r, and center rounding contributes O_r(N), absorbed by choosing N large. The numerical constants can be enforced by first choosing the Taylor remainder less than epsilon r^2/256 and then bounding each error separately; the displayed /32 is a deliberately larger allowance.

Inside the lattice ball |z|<rN define

T_N(a_N+z)=o(z)+l_N dot z-o(0)+v_L(a_N)-1.

Outside that ball set T_N=1. For rN/2<=|z|<rN, (A.2), (A.3), and |l_N-N DV(a)|<=sqrt(2)/2 give

T_N(a_N+z)-v_L(a_N+z)
 >= (epsilon/2)|z|^2 -(epsilon/32)r^2 N^2
    -(sqrt(2)/2)|z|-|o(0)|-1
 >= (3epsilon/32)r^2 N^2 -O_r(N)-|o(0)|-1>0.            (A.4)

Now set b_N=min(v_L,T_N). Since v_L<=0, b_N=v_L outside the ball, and (A.4) shows that every lowered site lies in |z|<rN/2. For N large the whole neighbor stencil at a lowered site lies inside |z|<rN, where T_N is an affine adjustment of o and has Laplacian at most 3. Since b_N<=T_N there, Delta b_N<=Delta T_N<=3 at a lowered site. At an unlowered site b_N=v_L and all neighbors weakly decreased, so Delta b_N<=Delta v_L<=3. The ball is strictly inside D_L, hence b_N remains zero outside D_L and belongs to F_{D_L}. But at its center

b_N(a_N)=v_L(a_N)-1,

contradicting the pointwise leastness of v_L. No nonnegativity requirement occurs in this Dirichlet family, so the fact that the potentials are negative presents no obstruction. Therefore V=W.

Every subsequence has a convergent further subsequence by A2, and all such limits coincide, so the entire potential sequence converges uniformly. Every weak-* subsequential limit of the identity has distributional Laplacian Delta V inside Omega, hence is the same L^infinity function there. The identities are uniformly bounded by 3. Exhaustion by compact interior sets and a boundary-strip estimate prove weak-* convergence on Omega for every L^1 test: approximate the test by one supported away from the boundary and bound the remaining integral by 3 times its L^1 norm. The fields are zero outside the square and differ from the ideal cell extension only on a strip of area O(h), so this gives weak-* convergence on R^2. This completes the proof.

This is an adaptation of a published comparison argument, not a theorem quoted as a full solution in print. It is a stronger partial result than the first attempt's ellipse-only identity statement.

## A5. An implicit characterization of the identity limit (proved)

Let C_3 be the closure of the set of symmetric matrices A for which some integer o on Z^2 satisfies Delta o<=3 and o(z)>=(1/2)z^T A z for every z. This is the closed integer-superharmonic matrix set in the cutoff-3 convention. It is downward closed in the matrix order.

The potential V from A4 is the unique function satisfying:

(i) V is continuous on the closed square and zero on its boundary;
(ii) Delta V is an L^infinity function with 0<=Delta V<=3 in the square;
(iii) V is twice differentiable almost everywhere and D^2V belongs to the topological boundary partial C_3 almost everywhere.

Existence of (i) and (ii) is A2–A4. At a point of twice differentiability, Lemma 4.1 gives D^2V-epsilon I in the defining (unclosed) attainable set for every epsilon>0, so D^2V belongs to C_3. If D^2V were an interior point of C_3, choose epsilon>0 with D^2V+2epsilon I in C_3. Approximate that matrix in operator norm within epsilon/2 by an actually attainable matrix B. Then B>=D^2V+epsilon I. Its integer witness dominates the quadratic with Hessian D^2V+epsilon I, and the one-subsequence lowering construction (A.3)–(A.4) contradicts leastness. Hence D^2V is on the boundary.

For uniqueness within this class, suppose V_1,V_2 satisfy (i)–(iii) and differ. The contact lemma A3 and twice differentiability give a point a where V_1(a)>V_2(a), both Hessians belong to partial C_3, and D^2V_1(a)<=D^2V_2(a)-2epsilon I. But downward closure implies that every symmetric matrix within operator distance epsilon of D^2V_1(a) belongs to C_3: each is strictly below D^2V_2(a) in matrix order. Thus D^2V_1(a) is an interior point of C_3, contradiction. This proves the characterization.

We state this as an a.e. Hessian Dirichlet characterization within the bounded-Poisson class, not as an unproved assertion of equivalence with all viscosity notions. It does determine the weak limit implicitly, but does not calculate its patch geometry or the four height-frequency densities. No novelty claim is made; the cutoff-3 Dirichlet conclusion may be implicit in the existing general convergence methods.

## A6. A nontrivial bound on the identity weak limit (proved)

The density e from A4 satisfies 2<=e<=3 almost everywhere in the unit square.

The upper bound has already been proved. For the lower bound, fix a ball B whose closure lies inside the square and let X_N=NB intersect Z^2 for large N. Recurrence of e_L means every nonempty subset of X_N contains a vertex x with e_L(x)>=indeg_remaining(x). Remove such a vertex and continue. In the resulting removal ordering, sum_x e_L(x) is at least the sum of those inside-degrees at removal time. Each edge of the induced lattice graph on X_N is counted exactly once, at the removal of its first endpoint. Hence

sum_{x in X_N}e_L(x)>=#edges(X_N)
 =2#X_N -(1/2)#edges(X_N,X_N^c).

For a ball of radius N r the number of outgoing edges is O(N): each such edge has an endpoint within a fixed-width annulus of its circular boundary, which contains O(N) lattice sites by covering with unit squares. Jordan counting gives #X_N=N^2|B|+O(N). Divide by N^2 and use the weak limit from A4 to obtain integral_B e>=2|B|. The Lebesgue differentiation theorem gives e>=2 almost everywhere. The edge-counting identity also works on inner boxes; no symmetry or periodicity of the identity was assumed.

This lower bound constrains the mean density only. It does not imply vanishing height-0 or height-1 frequency: mixtures containing heights 0 and 1 can still have average between 2 and 3.

## What approach A resolves, and what it does not

It proves weak-* convergence and an intrinsic Dirichlet characterization for the actual standard wired-square identity; this replaces the first attempt's statement that even weak-limit existence was unproved here. It gives neither an explicit patch description nor convergence of exact-height frequencies for that identity. Those would follow from isolated-maximal-Hessian membership almost everywhere by the earlier window/stability argument, adapted to the unrestricted local leastness of v_L (there is no positivity obstacle for this Dirichlet potential).

The main C0100 point-source frequency refinement remains open in this attempt. Its two missing factorial moments and its isolated-maximal-Hessian hypothesis have not been established. Approach B was recorded as a genuinely different fixed-Hessian counterexample/rigidity route, but is not needed to support any of the proved results above and is not claimed to have succeeded.

## Numerical certificates and hostile-referee audit

identity_dirichlet_checks.py computes the standard identity by the earlier stabilization formula, tests recurrence by burning, solves Delta v=e by a discrete sine transform, rounds to integers, and then checks EVERY integer residual exactly. The transform's floating output is used only to propose integers: the zero integer residual plus invertibility is the certificate. It checks v<=0 and all four strip barriers. For L=1,2,3,4,5,6,8,10 it separately constructs v by repeated lowering of a forbidden subset, starting from zero, and compares the entire functions and height fields. These independent constructions agree. For L=12,24,48,72 it additionally computes the recurrent all-ones class as stabilization of e+1, and certifies its integer potential from Delta u=r-1. In each case that configuration and potential differ from the zero-class identity and cutoff-3 potential.

The samples in identity_dirichlet_checks.jsonl are saved as each run finishes. At L=72, min v/(L+1)^2=-0.1649465190 and mean identity height is 2.2700617284; the exact Laplacian, recurrence, and barrier tests pass. All twelve grids together ran in about 12.5 seconds. No asymptotic convergence claim rests on these numbers. Finite-grid averages can be BELOW 2: L=3 has mean 4/3, exactly consistent with the boundary deficit in the induced-edge lower bound. This explicitly tests an easy way to overstate A6.

DirichletChecks.lean checks the forbidden-set lowering inequality over integers, the single-site nonnegativity argument, and the strip barrier's discrete Laplacian over rationals. It also kernel-evaluates the five possible inside-degrees with decide +kernel. The initial import Mathlib.Tactic.Omega was unavailable in the installed build; it was corrected to the core Lean.Elab.Tactic.Omega import. The final rerun exited 0 in about 91 seconds; its results are recorded in dirichlet_lean_check.log and are considered kernel-checked. No analytic compactness or uniqueness theorem is claimed to be formalized.

Hostile-referee checklist and resolution:

1. **Is e_D actually the zero-class identity?** Yes: stability follows from one-site lowering, recurrence from forbidden-set lowering, and e_D is an integer reduced Laplacian. All three conditions are necessary and were proved separately.
2. **Does the least element exist rather than merely a pointwise infimum?** Yes: a real Poisson lower bound makes each integer infimum attainable; finitely many attaining functions can be minimized simultaneously, preserving the cutoff inequality.
3. **Can we use global absolute-Laplacian compactness?** No. Exterior Laplacians can grow with L. The proof uses interior compactness and an explicit boundary modulus. Only the global UPPER bound is used in the lifting lemma.
4. **Does the source's Lemma 4.1 permit negative functions and a general upper bound?** Yes, its statement is for any integer functions with Delta<=K; the paper explicitly says translated functions may be negative. Here K=3, and the whole-lattice upper bound was verified.
5. **Does Proposition 2.5 on a ball automatically apply to a square?** Not without an argument. A3 supplies the convex-composition construction. Its Hessian correction is positive semidefinite, so strict negativity transfers to the original difference. The support stays away from the square boundary.
6. **Are both limit functions twice differentiable at the selected contact point?** Yes: both Poisson solutions have a full-measure differentiability set, while the contact set has positive measure. The intersection is nonempty; the same reasoning imposes their a.e. matrix constraints in A5.
7. **Can the affine rounding and center shift destroy the annular inequality?** Their contributions are O(N) for fixed r; the positive curvature gap is order epsilon r^2 N^2. The order of choices is: fix a and epsilon, shrink r, then let N grow. Equation (A.4) retains a positive quadratic coefficient after all remainder allowances.
8. **Can patching T_N to a constant violate the stencil inequality?** Lowered sites lie in the inner half-ball, so their full stencil uses the unpatched witness. Unlowered sites use the original v_L and weakly decreased neighbors. The outer annulus protects the join.
9. **Does the old nonnegative odometer obstacle survive here?** It is absent. The Dirichlet admissible family permits negative interior functions. The competitor retains zero exterior, so every constraint in that family is satisfied.
10. **Is the matrix set closed/downward?** It is defined as a closure. Downward closure survives closure: if A_n->A are attainable and B<=A, then B_n=B+(A_n-A)<=A_n are attainable and converge to B. This justifies the strict-order interior argument in A5.
11. **Does the a.e. Hessian description alone identify individual heights?** No. It identifies the weak mean density through the unique potential. The old window/stability mechanism still needs isolated maximal Hessians for local height histograms.
12. **Does the scale match wired [0,n]^2?** With its outer vertices wired, the nonsink set is {1,...,n-1}^2, exactly our L=n-1 and N=L+1=n. Other conventions differing by one vertex give the same weak limit by a dilation tending to one and boundedness against L^1 tests.
13. **Can boundary mass invalidate weak-* convergence?** The identity fields themselves are bounded by 3; boundary strips have vanishing area. The unbounded exterior Laplacian is excluded from the identity field and is never equated with its global continuum zero extension.
14. **Is this a solution in print or a novel theorem?** Neither is asserted. It is a complete adaptation of cited methods for a requested family. Targeted literature searches did not supply an exact full C0100 theorem; general Dirichlet convergence may already be implicit in existing work.

## Final remaining gap

The main point-source height-fraction question is not proved or disproved. The old a.e.-isolated-maximal-Hessian condition remains a sufficient hypothesis, not a theorem about that limit. The two untried approaches were recorded before pursuing A; A now yields a rigorously derived weak wired-identity limit and implicit matrix-Dirichlet characterization, while its explicit geometry and individual-height frequencies remain undetermined. The honest overall verdict remains PARTIAL.
