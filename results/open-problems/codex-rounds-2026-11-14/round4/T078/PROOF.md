# A smaller boundary-coloring cost for exchange loops

The boundary-coloring estimate below holds for every finite transposition mesh. Its conversion into a magnetization tail assumes a bound on the probability that a slot's cycle avoids the boundary pins. That assumption is not proved here.

## 1. Finite mesh and its probability law

Let V be a finite nonempty set of slots, let m>=1, and index layers by j=0,...,m-1, cyclically. At layer j choose a transposition tau_j=(a_j b_j); a_j=b_j is allowed and means the identity. Let 0<=r_j<=1. A configuration c belongs to {0,1}^m and has product weight

    w(c) = product_j r_j^(c_j) (1-r_j)^(1-c_j).

The factors mean r_j if c_j=1 and 1-r_j if c_j=0, so no ambiguous power 0^0 is needed. Define the permutation of layer-slot pairs

    gamma_c(j,v) = (j+1 mod m, tau_j^(c_j)(v)).

Let k(c) be its number of cycles. Every cycle meets layer zero. Taking successive returns to that layer identifies these cycles with the cycles of the return permutation

    Pi_c = tau_(m-1)^(c_(m-1)) ... tau_0^(c_0)

on V. In particular k(c)<=|V|. Put

    Z = sum_c w(c) 2^(k(c)),
    nu(c) = w(c) 2^(k(c)) / Z.

The weights w sum to one and 2^k is positive, hence Z>0. Given c, color its cycles independently up or down with probabilities 1/2 each. This defines the joint mark-and-color law P.

Fix D subset V and let n_D(c) count the cycles meeting some (j,v) with v in D. Let G_D be the event that all these cycles are up. Define the set of crossing layers

    X = {j : exactly one of a_j,b_j belongs to D}.

## 2. Boundary-coloring theorem

For every such mesh,

    P(G_D) >= 2^(-|D|) product_(j in X) (1+r_j)^(-1).       (1)

There is no restriction on dimension, mesh size, or period in (1).

### Cycle counting

Separate the cycles meeting D into those meeting {0}xD and the rest. The former number at most |D| because the cycles are disjoint. Any remaining cycle meets D somewhere and meets layer zero only outside D. Along that directed cycle membership in D therefore changes from true to false at least once. Assign one such exit to the cycle. Distinct cycles receive distinct exits.

At an inactive layer there is no exit. At an active layer whose endpoints both belong to D or both lie outside D, there is no exit either. At an active crossing layer there is exactly one exit: the endpoint in D is mapped to the endpoint outside D. The other endpoint gives an entrance, not a second exit. Consequently

    n_D(c) <= |D| + sum_(j in X) c_j.                     (2)

This proof covers cycles visiting D several times: only one exit per cycle is assigned. A cycle staying in D necessarily meets {0}xD and belongs to the first class.

### A conditional coin bound

Fix all coins except c_j at a conditioning value of positive nu-probability. Write k_0,k_1 for the two possible cycle counts. If a_j!=b_j, changing c_j composes gamma_c with a transposition of the two output vertices (j+1,a_j),(j+1,b_j). Multiplication of a permutation by a transposition merges two cycles or splits one cycle into two. To see this, cut the two arrows whose images are transposed: different cycles become one circuit, whereas one cycle becomes the two arcs closed separately. Thus k_1-k_0 is -1 or 1. If a_j=b_j it is zero. In every case

    R := 2^(k_1-k_0) <= 2.

For 0<r_j<1, cancellation of the other product weights gives

    nu(c_j=1 | other coins) = r_j R / (1-r_j+r_j R)
                            <= 2r_j/(1+r_j).             (3)

The displayed rational function is increasing in R, as its derivative is r_j(1-r_j)/(1-r_j+r_j R)^2>=0. For r_j=0 or 1 the coin is deterministic and (3) still holds. Therefore

    E_nu[2^(-c_j) | other coins]
       = 1 - nu(c_j=1 | other coins)/2
       >= 1/(1+r_j).                                    (4)

### Iteration

Condition on all other coins in a product over X. Its other factors are nonnegative and measurable under that conditioning. Equation (4) removes one factor with a lower bound 1/(1+r_j). Repeating this for each j in X gives

    E_nu[product_(j in X) 2^(-c_j)]
       >= product_(j in X) (1+r_j)^(-1).                 (5)

This uses the conditional bound in the original law at every step; it assumes no independence under nu. Given c, the probability of G_D is 2^(-n_D(c)). Equations (2) and (5) now prove (1).

## 3. Conditional magnetization tail

Let n=|V| and define M at layer zero by giving each up slot spin +1/2 and each down slot spin -1/2, then summing. Conditioned on G_D the uncolored law is

    nu_D(c) = w(c) 2^(k(c)-n_D(c)) / Z_D,
    Z_D = sum_c w(c) 2^(k(c)-n_D(c)).

Indeed P(G_D | c)=2^(-n_D(c)); conditioning multiplies nu by this factor. Cycles meeting D are up; all other cycles retain independent fair colors.

Assume, for some 0<=p<1/2, that every slot v at layer zero satisfies

    nu_D(the cycle of (0,v) avoids all layers of D) <= p.  (6)

Slots in D satisfy this automatically with probability zero. The conditional mean spin of v is one half times the probability its cycle meets D. Hence

    E[M | G_D] >= (n/2)(1-p).

Write q=P(M>=n/4 | G_D). Since M<=n/2 on the tail and M<=n/4 on its complement,

    (n/2)(1-p) <= E[M | G_D]
                <= (n/2)q+(n/4)(1-q).

As n>0, this yields q>=1-2p. Combining with (1),

    P(M>=n/4)
       >= (1-2p) 2^(-|D|) product_(j in X) (1+r_j)^(-1). (7)

Hypothesis (6) is the spatial input. Equation (7) alone does not supply it.

The coefficient 2p has a second derivation. The number of down slots is n/2-M, whose conditional expectation is at most np/2. On M<n/4 this number exceeds n/4. Markov's inequality therefore bounds that event's conditional probability by 2p, reproducing q>=1-2p without the mean decomposition above.

For a matrix formulation, let U_j be the permutation matrix induced by tau_j on the colorings V->{up,down}, let C_j=(1-r_j)I+r_j U_j, and let T=C_(m-1)...C_0. Expanding this product over c shows

    trace(T) = Z.

For fixed c, a coloring contributes to the trace exactly when it is constant on each return cycle, giving 2^k choices. Those choices correspond bijectively to the cycle colorings above. If Q is the diagonal projection onto M>=n/4, the same expansion with Q gives

    trace(TQ)/trace(T) = P(M>=n/4).

Thus (7) is also a trace inequality, with no limit or operator comparison required.

## 4. Repeated meshes and the continuous-time boundary factor

Suppose each of N sweeps contains the same q spatial transpositions, all at rate r=delta/2, and J_cross of these cross D. Any other transpositions preserve D and may have arbitrary rates in [0,1]. They contribute no factor to (1). Then |X|=N J_cross and

    P(G_D) >= 2^(-|D|)(1+delta/2)^(-N J_cross).           (8)

For fixed t>=0 take delta=t/N, restricting to N large enough that delta/2<=1. Since log(1+x)/x tends to one as x tends to zero,

    (1+t/(2N))^(-N J_cross) -> exp(-t J_cross/2).          (9)

If (6) holds with a common p along the mesh sequence and its normalized magnetization tails converge, (7) passes to that limit and gives

    P_limit(M>=n/4)
       >= (1-2p) exp(-|D| log 2 - t J_cross/2).           (10)

For finite matrix limits the required convergence follows whenever T_N converges to T with trace(T)>0: the numerator and denominator are finite sums of entries, so their ratio converges. Positivity of the limiting trace follows, for example, for T=U exp(tG) with U a slot-permutation color matrix and G=sum_j(U_j-I)/2. In the finite sum defining G, the all-up coloring is fixed by every U_j and by U. Accordingly T has diagonal entry one there. The matrices exp(tG) have nonnegative entries: write exp(tG)=exp(-tq/2)exp((t/2)sum_j U_j) and expand the latter exponential in its nonnegative power series. Multiplying by U preserves entrywise nonnegativity. Thus trace(T)>=1.

Every permutation preserving D can be expressed as transpositions within D and within its complement, by decomposing its cycles. Such deterministic seam permutations can therefore be included among the other layers at rate one. This includes within-site seam permutations when D is a union of complete sites.

There is a separate continuous-time check on the coefficient 1/2 in (9). Give each spatial transposition an independent rate-1/2 Poisson clock for time t, and permit fixed seam permutations preserving D. Let J count the crossing marks and put Lambda=t J_cross/2, its mean under the unweighted Poisson law. Weight the picture by 2^k as before. The deterministic count (2), applied to the finite random sequence of marks, still holds.

For a Poisson process of intensity measure alpha and any bounded nonnegative functional H, expansion of the Poisson probabilities and reindexing l/l! as 1/(l-1)! gives

    E[sum_(x in process) H(process)]
       = integral E[H(process with x inserted)] alpha(dx).

Apply this to crossing marks and H=2^k. Inserting one mark composes the return permutation with a transposition, conjugated by the later part of the picture, so it increases 2^k by at most a factor two. The mean crossing count under the weighted law is consequently at most 2 Lambda. The same argument holds when all crossing intensities are multiplied by exp(-u): its weighted mean count is at most 2 Lambda exp(-u).

Let F(u)=E_nu[exp(-u J)] for u>=0. The law obtained by this tilt is precisely the loop-weighted law with crossing intensities multiplied by exp(-u); the extra Poisson normalization is independent of the picture and cancels. Differentiation gives

    d/du log F(u) = -E_(nu,u)[J] >= -2 Lambda exp(-u).

These differentiations are justified by k<=n and the finite exponential moments of a Poisson variable. Integrating from 0 to log 2 gives log F(log 2)>=-Lambda. Thus P(G_D)>=2^(-|D|)E_nu[2^(-J)]>=2^(-|D|)exp(-t J_cross/2), independently reproducing (9)'s constant. The spatial assumption (6) is still needed for a magnetization tail.

## 5. Comparison with the inspected mesh estimate

In the notation of MeshSurface.lean, take D to be the slots outside F. Its set K includes all spatial layers with at least one endpoint in D, so X is a subset of K; edges with both endpoints in D are removed by X. The source bounds the boundary-cycle mean by |D|+4 sum_(j in K) r_j and uses a Jensen bound for the coloring probability. At r_j=delta/2 its coloring factor is

    exp[-log(2)(|D|+2 delta |K|)].

For N repeated sweeps and J_K such spatial layers per sweep this tends to

    exp[-|D| log 2 - 2 log(2) t J_K].

Equations (8)–(9) replace its time-dependent exponent by t J_cross/2. This is a smaller cost: J_cross<=J_K and 1/2<2 log 2. Already on the finite mesh, log(1+delta/2)<=delta/2<2 log(2)delta for delta>0, giving the comparison directly. No optimality of (1) is asserted.

The source supplies (6) through Bootstrap.mesh_pin_bound. If that input is accepted, its p<1/4 allows 1-2p>1/2 in (7) and (10). The coloring-cost argument and its improvement do not verify that bootstrap or the physical-spin projection.

## 6. Independent checks and edge cases

An algebraic derivation checks the conditional constant without differentiating a probability. Fix j and sum the weights of the other coins, possibly with any fixed nonnegative factor depending only on those coins. Let A be the resulting weight when c_j=0, before its factor 1-r_j, and B the corresponding weight when c_j=1, before r_j. The transposition argument gives B<=2A term by term. Writing r=r_j,

    [(1-r)A+(r/2)B] - [(1-r)A+rB]/(1+r)
       = r(1-r)(A-B/2)/(1+r) >= 0.

The first bracket is the weighted sum after inserting 2^(-c_j). Applying this identity successively reproduces (5), including r=0 and r=1.

For a second check on (2), follow each cycle from an occurrence at layer zero. A cycle meeting D without a layer-zero point in D must enter and then leave D between successive returns to that cut. Active crossing layers supply one entrance and one exit apiece. Distinct cycles use disjoint exit vertices. Internal transpositions supply neither. This again gives |D|+J_cross, with coefficient one, not two.

For two slots a,b with D={a}, consider two layers, both swapping a,b, with rates r,s. The four configurations have weights 4(1-r)(1-s), 2r(1-s), 2(1-r)s, 4rs under the unnormalized loop law. Their numbers of boundary-touching cycles are 1,1,1,2. Therefore

    Z = 4-2r-2s+4rs,
    Z_D = 2-r-s+rs,
    P(G_D) = (2-r-s+rs)/(4-2r-2s+4rs).

Equation (1) gives 1/[2(1+r)(1+s)]. To check the inequality for the entire square 0<=r,s<=1, multiply by its positive denominators. The difference is

    2(1+r)(1+s)Z_D-Z
      = 2[2r+2s-r^2-s^2-rs+r^2 s^2] >= 0,

because 2r-r^2>=r, 2s-s^2>=s, and r+s-rs>=0. In particular r=s=1 gives P(G_D)=1/4. Counting only layer-zero boundary cycles would incorrectly give 1/2 in this case; the exit term in (2) is necessary.

With one crossing layer the same enumeration gives Z=4-2r, Z_D=2-r, and P(G_D)=1/2. The bound 1/[2(1+r)] is valid but usually strict. Hence the improvement is not presented as sharp.

The conditional coin bound itself can be attained. In the two-layer example set s=1. The two allowed configurations have unnormalized weights 2(1-r) and 4r, so the first coin is active with probability 2r/(1+r). Its expectation of 2^(-coin) is exactly 1/(1+r), independently checking (3)–(4).

If D is empty, (1) is the equality 1>=1. If D=V, X is empty and k<=|V| gives P(G_D)=E_nu[2^(-k)]>=2^(-|V|), as claimed. If X is empty but D is proper, all histories preserve D and every cycle meeting D has a layer-zero representative there, so the same argument gives P(G_D)>=2^(-|D|). Repeated endpoints cause identity maps and do not affect any bound. Rates zero and one were included above. No assumption about independence of colors on distinct slots was used: colors are independent on cycles.

## Sources inspected

OpenAI, *Spontaneous magnetization in the quantum Heisenberg ferromagnet*, September 24, 2026, [manuscript](https://mathcommunity.github.io/oai-math-revised/papers/Spontaneous-magnetization-in-the-quantum-Heisenberg-ferromagnet-September-24-2026/paper.pdf), Lemma 8.1. The precise mesh estimates used for comparison are [BoundaryMesh.lean](https://raw.githubusercontent.com/openai/math/main/lean/OAI/MathematicalPhysics/Heisenberg/BoundaryMesh.lean), `mesh_boundary_count` and `mean_boundary_cycles`; [MeshSurface.lean](https://raw.githubusercontent.com/openai/math/main/lean/OAI/MathematicalPhysics/Heisenberg/MeshSurface.lean), `mesh_surface_tail`; and [MeshMatrixSurface.lean](https://raw.githubusercontent.com/openai/math/main/lean/OAI/MathematicalPhysics/Heisenberg/MeshMatrixSurface.lean), `mesh_matrix_surface`. The remaining spatial hypothesis is in [MeshPin.lean](https://raw.githubusercontent.com/openai/math/main/lean/OAI/MathematicalPhysics/Heisenberg/MeshPin.lean), `mesh_pin_bound`. No claim of novelty is made for the finite permutation and conditional-weight arguments.
