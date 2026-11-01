from pathlib import Path
p=Path('SECOND_ATTEMPT.md')
p.write_text(p.read_text(encoding='utf8')+r'''
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
''',encoding='utf8')
