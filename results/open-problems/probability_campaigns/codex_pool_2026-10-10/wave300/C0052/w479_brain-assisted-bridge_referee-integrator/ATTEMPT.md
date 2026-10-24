# C0052: finite-volume weighted-current bridge

## Source target and hardest missing step

Duminil-Copin, *Lectures on the Ising and Potts models on the hypercubic lattice* (arXiv:1707.00520), printed p. 94, defines the near-critical renormalized coupling g(beta) from the spatial sum of U4 divided by chi(beta)^2 xi(beta)^3. Its C0052 part asks that g(beta) not tend to zero as beta increases to beta_c in d=3. The source's Exercise 61, part 1, gives a finite-graph random-current identity for U4. The hardest open piece here is a lower bound on the relevant weighted current connectivity at diverging correlation length, with enough localization and thermodynamic control to imply a lower bound on -g(beta). None is established below.

## Exact finite-graph lemma (own derivation; independent review pending)

Let G be a finite graph with zero-field ferromagnetic Ising couplings J_e>=0 and free boundary conditions at finite beta. Let f:V(G)->[0,infinity) be nonzero. Put S_f=sum_x f(x)sigma_x and V_f=E[S_f^2]>0. Sample two ordered endpoint pairs (X,Y) and (U,V) independently, each with law p_f(x,y)=f(x)f(y)E[sigma_x sigma_y]/V_f. Given the pairs, sample two independent random currents n1 and n2 with source sets {X} symmetric-difference {Y} and {U} symmetric-difference {V}. Let A be the event that X,Y,U,V lie in one connected component of the union n1+n2 (repeated endpoints allowed). Then

  (3 V_f^2-E[S_f^4])/V_f^2 = 2 P(A).

The left side lies in [0,2]. In particular a uniform fourth-cumulant deficit epsilon>0 is equivalent, at the same finite scale, to P(A)>=epsilon/2. This is an exact *weighted* probability, with endpoints sampled according to their correlations; it is not the unweighted intersection probability claimed in the 2026-09-07 attempt record.

Proof. Zero field gives E S_f=0. Expand E S_f^4-3(E S_f^2)^2 as the sum over ordered x,y,u,v of f(x)f(y)f(u)f(v) U4(x,y,u,v). Exercise 61(1) gives U4=-2 E[sigma_x sigma_y]E[sigma_u sigma_v] q(x,y,u,v), where q is the conditional random-current probability of A. All p_f weights are nonnegative and sum to one by the definition of V_f. Divide the expanded identity by V_f^2. Since 0<=q<=1, the range follows. This uses no independence of overlap events across endpoint choices; independence is only the explicit sampling of the two endpoint pairs and then of the two currents.

The source identity is for finite G. Passing to an infinite-volume near-critical sum, comparing a box of size xi(beta) to the global U4 sum, and producing P(A)>=c uniformly at that scale are **not proved**. A critical finite-volume fourth-moment bound alone does not establish the source's near-critical g(beta) criterion.

## Two-spin exact control

Take G to be one edge, f=1 at both vertices, and t=tanh(beta J)=1/3. Then S=sigma_0+sigma_1, V=2(1+t)=8/3 and E S^4=8(1+t)=32/3. Thus (3V^2-E S^4)/V^2=3/2. For the current side, p(0,0)=p(1,1)=1/V and p(0,1)=p(1,0)=t/V. A current with distinct sources uses the edge; an even-source current uses it with probability 1-sech(beta J). If two diagonal pair choices are at opposite vertices, their union connects with probability 1-sech(beta J)^2=t^2. Enumerating the four pair categories gives P(A)=(1+3t)/(2(1+t))=3/4. Hence 2P(A)=3/2. This checks signs, normalization, repeated endpoints and source parity in a nonzero-coupling example.

## Why the earlier route cannot close C0052

The C0052-A001 record treats nontriviality as equivalent to a uniform probability that two arbitrary independent currents at scale L intersect. Exercise 61 instead has endpoint-dependent current source laws and two correlation weights. Its global g(beta) numerator also sums all triples of endpoints. Without an endpoint distribution, a precise scale window, and a comparison from that window to the full numerator, that equivalence is unsupported. The second-moment argument in the record explicitly leaves its six-point variance estimate open. The heuristic current-cluster dimension formula is not an established hypothesis or proof.

NEXT: Audit whether a source-backed near-critical localization inequality converts a box of side comparable to xi(beta), with p_f-weighted current connectivity, into a quantitative lower bound on -g(beta); if unavailable, retain this as a finite-graph bridge only.
