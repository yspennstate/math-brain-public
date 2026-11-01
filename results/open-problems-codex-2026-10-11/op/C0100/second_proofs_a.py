from pathlib import Path
p=Path('SECOND_ATTEMPT.md')
p.write_text(p.read_text(encoding='utf8')+r'''
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
''',encoding='utf8')
