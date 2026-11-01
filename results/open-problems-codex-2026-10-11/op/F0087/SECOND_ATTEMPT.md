# F0087 — second attempt, 2026-10-11

## Two approaches not used in the first attempt

**A. Compactification / charge-fusion counterexample search.** Put all positive insertions in one lattice cell and all negative insertions in another macroscopic cell. The product becomes a two-point electric correlator at the fused charge n*s. Exact height aliases then reduce this charge modulo integers. Compare its decay with the proposed matching bound (MB). This tests whether the missing bound is even true, before trying to prove it. If it fails, seek a weaker nearest-neighbor Onsager majorant that allows same-sign microscopic collisions but still permits moment integration.

**B. Mixed regular/singular observables and L2 projection.** Fix the height's additive constant by subtracting a smooth macroscopic average. Try to prove asymptotics for one electric insertion together with arbitrary smooth linear height observables, using a Kasteleyn operator with both a singular twist and a smooth potential. If mixed expectations determine the conditional expectation of any electric-field subsequential limit, and its second moments converge, an L2 projection argument can identify the limit without uniform high moments. The new analytic obligation is the mixed singular/smooth determinant asymptotic; GFF convergence alone does not provide it.

Chosen first: A, because the charge-period test can give a definitive algebraic answer to the exact gap (MB). B is reserved as an alternative if the collision target fails. No result claimed yet.

## Brain queries
Read-only math_recall.py calls on the gap were made with:
- dimer electric correlators collision bound Dubedat Onsager inequality
- double dimer loop switching bosonization Ising correlations
- imaginary chaos universality non Gaussian approximation smoothing
The returns contained mainly generic or different-model cards. The Ising switching card (claim_0e56f800a1dcbb9ca09e3847fa493b7687771d01283cedfde6336337a247e371) applies to ferromagnetic Ising spins with nonnegative weights; no representation transferring it to this dimer observable has been established. It is not a verdict or a usable dimer bound. A further recall on compactification and fusion follows.

## A1. The proposed matching bound (MB) is false for every nonzero principal charge

This is a counterexample to our proposed sufficient hypothesis, **not** a counterexample to existence of the electric-field scaling limit. It invalidates the first attempt's suggestion that (MB) was a plausible target.

Recall W_epsilon(z)=exp(iTheta) a_s epsilon^(-s^2) exp(2pi i s h(f_epsilon(z))), with a_s>0 fixed and 0<|s|<1/2. For n positive insertions all lying in Q_epsilon(f), and n negative insertions all lying in Q_epsilon(g), the balanced product has expectation of modulus exactly

    a_s^(2n) epsilon^(-2n s^2) |E exp(2pi i n s (h(f)-h(g)))|.       (A.1)

Proof: the phase exp(iTheta) cancels, all n copies of the same cell value multiply, and their exponents add. No independence or approximation is used.

Fix epsilon=1/N, f=(0,0), g=(N,0). Their embedded cells are near 0 and (1,0). For N>=4 every cross distance |x_i-y_j| is at least 1/2. Thus the matching sum on the right of (MB) is at most

    n! 2^(2n s^2),                                               (A.2)

independently of N. The set of these insertion configurations has positive Lebesgue measure epsilon^(4n), and contains tuples of pairwise distinct continuum points. Therefore an almost-everywhere bound cannot exclude it.

### Rational charge: an exact contradiction, with no asymptotic theorem
If s=a/b in lowest terms, take n=b. Then ns=a is an integer. Since h(f)-h(g) is deterministic modulo Z,

    exp(2pi i a(h(f)-h(g)))

is deterministic of modulus 1. The left side of (MB) is exactly a_s^(2b) N^(2b s^2), which diverges. No fixed C_b,K can multiply the bounded expression (A.2) to dominate it. This works for any dimer measure with the pinned height convention, provided the two cells are present.

For the concrete charge s=1/4 (alpha=pi/2), n=4: the eight-point correlator on these open cell products has modulus a_s^8 N^(1/2). The proposed cross-pairing majorant remains at most 24 sqrt(2). This is the simplest exact example.

### Irrational charge: contradiction using only the verified two-point theorem
Choose an integer n>1/(4s^2). Write ns=k+t with k integer and -1/2<t<1/2. Because s is irrational, t is neither zero nor a half-integer. The exact charge-alias identity from ATTEMPT.md P1 shows that the modulus in (A.1) equals

    |E exp(2pi i t(h(f)-h(g)))|.

Dubedat Proposition 23, with complex conjugation if t<0, makes this asymptotic to A_t N^(-2t^2), with A_t>0. Hence (A.1) is asymptotic to

    a_s^(2n) A_t N^(2n s^2-2t^2).

Its exponent is positive: n s^2>1/4>t^2. It diverges while (A.2) stays bounded. Again no C_n,K exists. This irrational case uses the canonical zero-slope infinite-volume measure to which Proposition 23 applies.

These cases exhaust all nonzero s in (-1/2,1/2). QED.

### Referee checks
- n is fixed once s is fixed, before epsilon tends to zero. The constants allowed in (MB) may depend on n but not epsilon; divergence defeats any such constant.
- The bad set is not an equality diagonal. The distinct real insertion points can all occupy the same constant lattice cell; this is an open, positive-measure set for each epsilon.
- The cells remain macroscopically separated, so every *cross* distance is uniformly bounded below. Same-sign distances shrink; these are absent from the original matching bound.
- The arbitrary fixed normalization a_s does not change divergence. The additional random phase cancels exactly for balanced moments.
- Aliasing is applied to a fused charge, not incorrectly to an individual Gaussian vertex operator. The rational case is exact; the irrational case uses an already verified two-point asymptotic with a fixed reduced charge t.
- The exact contradiction does not say that integrated high moments diverge. The bad configuration set has vanishing volume; this is examined below.

## A2. Why this counterexample does not prevent moment convergence

Fix n>=2 and a compact K contained in a fixed bounded square. Let E_epsilon be the set where all n positive insertions occupy one lattice cell and all n negative insertions occupy one other lattice cell (allowing the cells to be anywhere in K). There are O_K(epsilon^(-2)) choices for each cell. For any pair of cells the insertion volume is at most epsilon^(4n). Thus

    volume(E_epsilon) <= C_K epsilon^(4n-4).

The modulus of a balanced product of normalized fields is at most a_s^(2n) epsilon^(-2n s^2), because each raw electric field has modulus 1. For bounded test functions the absolute contribution of E_epsilon to the 2n-point integrated moment is therefore at most

    C_n,K,phi epsilon^[4(n-1)-2n s^2].                          (A.3)

The exponent is strictly positive: n>=2 and s^2<1/4 give 4(n-1)-2n s^2 > (7/2)n-4 >=3. Hence these explicitly bad fusion configurations have vanishing integrated contribution. This proof uses only amplitude and volume, so includes the same-cell choices and needs no dimer decorrelation theorem. It does not control arbitrary partial or mesoscopic collisions.

## A3. A weaker collision hypothesis that suffices

Replace the false cross-matching target by a nearest-neighbor Onsager target. Put m=2n, z=(x_1,...,x_n,y_1,...,y_n), q=s^2, and

    d_a(z)=min_{b!=a}|z_a-z_b|.

(OB) For every n and compact K there is C_n,K independent of epsilon and positions such that

    |E product_i W_epsilon(x_i) conjugate(W_epsilon(y_i))|
       <= C_n,K product_{a=1}^{2n}(d_a(z)+epsilon)^(-q).       (A.4)

**OB is unproved.** It includes nearest neighbors of either sign, so is not contradicted by A1. In A1's bad configurations every insertion has another same-sign insertion in the same epsilon cell, so d_a<=sqrt(2)epsilon; the right side can grow at least as epsilon^(-2nq), matching the crude maximal amplitude of the left side. For n=1, OB is established by the two-point bound in the first attempt: both nearest-neighbor distances equal |x-y|, and their combined power is 2q.

### A3a. Full proof that the proposed majorant is integrable

For any integer m>=2, any bounded planar set K, and 0<q<1,

    G_m,q(z)=product_{a=1}^m d_a(z)^(-q)

is integrable on K^m. Our q=s^2<1/4 is well inside this range.

Proof. On the complement of the equality diagonals,

    d_a^(-q)=max_{b!=a}|z_a-z_b|^(-q)
              <= sum_{b!=a}|z_a-z_b|^(-q).

Multiply these finite sums. The result is a sum over functions T:{1,...,m}->{1,...,m}, T(a)!=a, of products

    product_a |z_a-z_{T(a)}|^(-q).                             (A.5)

It suffices to integrate each of the (m-1)^m products. The directed graph of T has one outgoing edge at every vertex. Each connected component has a unique directed cycle, of length at least 2, and directed trees feeding that cycle: following successors must eventually repeat; two different cycles cannot belong to one component since following the single successor from any vertex ends in only one cycle. Equivalently, each component has equally many edges and vertices (parallel opposite directed edges are counted twice), so it is a cycle with attached trees.

Choose a disk of radius R containing K, and write

    B_a = 2pi(2R)^(2-a)/(2-a), 0<a<2.

For every v in K, integral_{K}|u-v|^(-a)d²u<=B_a, since K-v is contained in the radius-2R disk. Remove a tree leaf, meaning a vertex with indegree zero. Its variable occurs in only its one outgoing edge. Integrating that variable costs at most B_q, uniformly in the parent position, and removes the leaf factor. Repeat until only the directed cycle remains.

For a cycle of length 2, the two directed edges are the same distance and contribute |u-v|^(-2q). Integrating one vertex costs at most B_(2q); integrating the remaining unfactored variable costs |K|.

For a cycle of length k>=3, integrate any one cycle vertex u with its two incident factors. Cauchy-Schwarz gives

    integral_K |u-v|^(-q)|u-w|^(-q) d²u
       <= [integral_K |u-v|^(-2q)]^(1/2)
          [integral_K |u-w|^(-2q)]^(1/2)
       <= B_(2q).

This is uniform even if v=w because 2q<2. The remaining cycle edges form a path; integrate its endpoint leaves one at a time using B_q, then the last vertex using |K|. If a component has v vertices, its integral is at most |K| B_(2q) B_q^(v-2). Components factor, so every term (A.5) has a finite integral. Summing finitely many terms proves integrability. Equality diagonals have Lebesgue measure zero. QED.

A uniform quantitative collision-tail estimate also follows. Choose delta>0 with q(1+delta)<1, for example delta=(1/q-1)/2. The same proof with exponent q(1+delta) shows G_m,q is in L^(1+delta)(K^m). If B_eta is the set where any pair of positions has distance <eta, then its volume is at most binom(m,2)|K|^(m-1)pi eta^2 (each pair fixes one point and restricts the other to an eta disk; remaining variables range in K). Holder therefore gives

    integral_{B_eta}G_m,q <= ||G_m,q||_(1+delta)
                              volume(B_eta)^[delta/(1+delta)]
                           <= C_m,q,K eta^[2delta/(1+delta)].   (A.6)

This is explicit uniform integrability near all collision diagonals, not only the full fusion examples.

### A3b. Conditional scaling-limit theorem with corrected hypothesis

For 0<|s|<1/2, the first attempt's random-phase convergence conclusion is valid with OB replacing MB. Proof: off equality diagonals, Dubedat Theorem 24 supplies the balanced correlation limit F_(2s^2). The right side of OB is at most C_n,K G_(2n,s^2), independent of epsilon, because d_a+epsilon>=d_a. A3a proves that majorant integrable. Dominated convergence now gives convergence of all integrated balanced moments. Uniform bounds for higher balanced moments give uniform integrability of moment polynomials of test pairings. Unbalanced moments vanish by the independent uniform phase. The candidate exists and its moments determine its law by the construction and Cauchy bound in ATTEMPT.md P5-P6. The unconditional tightness proof P2a is unchanged. Every subsequential limit has the candidate's finite-dimensional test-pairing moments and therefore its distribution-valued law. Thus convergence in law in local H^(-t), t>1, follows **if OB is established**. All uses of dominated convergence now have an explicit integrable and collision-uniform majorant. QED, conditional on OB.

This is a genuine repair of the sufficient target; it is not a proof of OB or of the nontrivial dimer limit.

## A4. Stronger counterexample: eight distinct lattice faces

The matching bound fails even if one insists that all insertions occupy distinct lattice faces. We prove this for s=1/4 using a local determinantal computation and mixing of the infinite-volume square-grid measure. This removes any concern that A1 was only an artifact of repeated evaluation within one cell.

### A4a. The needed canonical inverse-kernel facts

Use primal vertices Z^2 (the half-cell shift from the dual-corner convention is immaterial), black vertices with even coordinate sum, and the bipartite Kasteleyn matrix K(b,w)=1 on horizontal edges and i on vertical edges. Its Fourier symbol for the full off-diagonal adjacency operator is

    P(k_x,k_y)=2cos(k_x)+2i cos(k_y).

The canonical zero-slope inverse kernel is the restriction of

    G(d)= (2pi)^(-2) integral_[0,2pi]^2
                    exp(i k.d)/P(k) dk.                       (A.7)

The integrand is L1: its only singularities occur at the four points where both cosines vanish, and its modulus is O(1/|k-k0|) there; this is integrable in dimension 2. Multiplication by P gives 1 almost everywhere, so Fourier multiplication verifies that the full adjacency operator times G is the identity. A simultaneous shift of both Fourier coordinates by pi shows G vanishes on even-parity displacements; hence this inverse restricts to the bipartite K inverse. The Riemann-Lebesgue lemma gives G(d)->0 as |d|->infinity. The canonical inverse-kernel construction and dimer occupation determinant formula are the standard existing Kasteleyn/Kenyon results (also Dubedat Theorem 1 and its dimer discussion); this paragraph verifies the Fourier realization and the decay needed here, not a new construction of the Gibbs measure.

Because P is even separately in k_x and k_y, G is even separately in d_x and d_y. Taking conjugates and shifting k_y by pi gives

    conjugate(G(d_x,d_y)) = (-1)^(d_y) G(d_x,d_y).

Thus G(1,0) is real and G(2,1) is purely imaginary. Swapping the Fourier coordinates gives G(0,1)=-i G(1,0): the swapped symbol is i conjugate(P), and evenness and the preceding reality relation finish this calculation. The inverse identity at d=0 then gives 2G(1,0)+2iG(0,1)=1, so

    G(1,0)=1/4,  G(0,1)=-i/4.                                (A.8)

Set c=iG(2,1), which is real; evenness handles all signs of these displacements.

### A4b. Local fusion product and nonzero mean

Take four consecutive dual faces f_j=(j,0), j=0,1,2,3. Let N_j, j=0,1,2, be the indicators of the three vertical primal edges crossed by the horizontal dual path. The signed quarter-height increments are alternating, so summing the four face heights gives exactly

    sum_{j=0}^3 h(f_j)=4h(f_0)+1/2-3N_0+2N_1-N_2.

For s=1/4, define the four-point raw product A_f=product_{j=0}^3 exp(i(pi/2)h(f+(j,0))). When f is an even horizontal translate of 0, the residue table gives exp(2pi i h(f))=1. Therefore

    A_f = exp(i pi/4) i^(N_0) (-1)^(N_1) (-i)^(N_2).           (A.9)

This is a local function of just three dimer indicators; no unbounded height variable remains.

For those vertical edges, the occupation kernel L_{jk}=K(b_j,w_j) K^{-1}(w_j,b_k) is, by (A.7)-(A.8),

    L = [[1/4, i/4, c],
         [i/4, 1/4, i/4],
         [c,   i/4, 1/4]].

The two nonadjacent crossed edges give a joint occupation probability det L_{0,2}=1/16-c^2>=0. Hence |c|<=1/4. Joint occupation moments are principal minors of L. Expanding product_j[1+(u_j-1)N_j] consequently gives

    E product_j u_j^(N_j) = det(I+diag(u_j-1)L).

With u=(i,-1,-i), direct expansion of this 3x3 determinant yields

    D := E i^(N_0)(-1)^(N_1)(-i)^(N_2)
       = 7/16+c/2-c^2.                                      (A.10)

For explicit algebra checking, the three pair-minor contributions sum to 5/8-2c^2, the singleton plus constant contributions cancel, det L=3/64-c/8-c^2/4, and the triple coefficient (i-1)(-2)(-i-1) is -4. This gives (A.10). Since c>=-1/4 and c^2<=1/16,

    D >= 7/16-1/8-1/16 = 1/4.

Thus |E A_f|=D>=1/4. No numerical evaluation of c or pi is needed for this lower bound.

### A4c. Dimer mixing supplies the separated-cluster limit

For two fixed finite edge sets separated by an even translation T, a joint occupation probability is a determinant of a block matrix whose off-diagonal blocks consist of G entries at displacements tending to infinity. By the Riemann-Lebesgue decay just proved these blocks tend to zero. The determinant tends to the product of the two diagonal-block determinants, giving asymptotic independence of all occupation monomials. Any function of finitely many binary occupations has a finite multilinear expansion: write it as the sum over configurations v of its value at v times product_j[N_j if v_j=1 else (1-N_j)], then expand. Thus all bounded local functions also factor in expectation in the limit. Applying this to (A.9),

    E A_0 conjugate(A_{(2N,0)}) -> D^2 >=1/16.                (A.11)

This mixing argument is proved for the canonical translation-invariant measure; it does not assume uniform independence under arbitrary boundary conditioning.

Finally take epsilon=1/(2N), put four positive insertions in the four different cells at epsilon f_j near 0, and four negative insertions in the four different cells at epsilon((2N,0)+f_j) near (1,0). Cross distances are uniformly bounded below, while all eight lattice faces are distinct. Their normalized balanced correlation is

    a_s^8 epsilon^(-8s^2) E A_0 conjugate(A_{(2N,0)}),

whose modulus is asymptotic to a_s^8 D^2 epsilon^(-1/2), diverging by (A.11). The matching sum remains bounded. Each product of eight prescribed cell interiors has positive measure, so the almost-everywhere issue is again resolved. QED.

### Independent checks of A4

`distinct_fusion_checks.py` scanned 455 four-face clusters using the Fourier inverse (A.7) and finite-rank Kasteleyn perturbation determinants. For the horizontal consecutive cluster, quadrature grids 64,128,256,512 gave mean moduli 0.3986795039, 0.3986788592, 0.3986788190, 0.3986788165. This suggests c=1/4-1/pi but that evaluation is **not** assumed or claimed proved. The analytical proof only uses c^2<=1/16. The nearest inverse entries were checked against (A.8). `local_fusion_symbolic.py` independently expanded the determinant exactly with SymPy; the initial u vector there is reflected, (-i,-1,i), which has the same determinant since L is invariant under swapping indices 0 and 2. The explicit proof uses the actual vector (i,-1,-i). These quadrature computations are numerical evidence, not an error-certified inverse-kernel construction. A3x3 algebra and the positivity bound, not quadrature, establish nonvanishing.

## A5. Attempt to bridge OB to existing theorems; exact stopping point

The first attempt's Gaussian Cauchy determinant bound does not transfer to the discrete field. A1/A4 prove that such a transfer at the cross-pairing level would actually be false. The brain's Ising switching/moment-domination card likewise has incompatible objects: zero-field ferromagnetic spins and nonnegative test weights, not complex dimer height exponentials. No representation putting this observable under that theorem was found or assumed.

Dubedat's Theorem 24 supplies the correct powers on configurations with all pairwise distances comparable. It does not state constants uniform when a subset of insertions becomes microscopic while another subset remains macroscopic. His p.75 warning about fusing charges already notes compactification and says the naive confluent limit is incorrect. A4 identifies a concrete surviving lattice fusion channel, rather than taking that confluent limit.

To prove OB by extending the determinant method one would need estimates on twisted inverse kernels and determinants for a hierarchy of collision scales, with the fused charge reduced modulo integers each time a cluster is contracted. Merely substituting nearest-neighbor distances into the separated-point theorem is not justified: the error constants there may depend on ratios of distances, and the fusion sector can change. The local Fourier/determinant calculation proves one resonant fusion channel and ordinary mixing, not a uniform bound for arbitrary numbers and geometries of charge clusters.

Thus Approach A reaches a definitive refutation of MB, an explicit distinct-site fusion theorem, and a repaired sufficient bound OB with a complete integrability and moment-convergence argument. OB itself remains open in this attempt. Approach B remains a distinct alternative; it would require mixed one-singular-insertion/smooth-potential asymptotics after a macroscopic height gauge is fixed. The present calculation does not prove these asymptotics, and balanced moments cannot identify the original pinned phase by themselves.

## Final hostile-referee checklist, second attempt

1. **Wrong target:** MB is now explicitly refuted, and its former conjecture record in CLAIMS.jsonl is replaced by the counterexample. The earlier implication MB -> convergence is retained only as a formal conditional statement, never used as an available route.
2. **Almost everywhere:** A1 and A4 give positive-volume products of cell interiors. Distinct continuum insertion coordinates and, in A4, distinct lattice faces are permitted. Neither proof relies on a measure-zero equality diagonal.
3. **Wrong normalization:** q=s^2, raw exponent alpha=2pi s, and 2n normalized fields contribute epsilon^(-2nq). For s=1/4, eight fields contribute epsilon^(-1/2), as checked algebraically.
4. **Unjustified nonzero limit:** A4's lower bound comes from a nonnegative two-edge occupation probability, not from numerical extrapolation. All mixing needed is proved using decaying canonical inverse kernels and finite determinants.
5. **Uncontrolled Fourier singularity:** The kernel is L1 around each of its four isolated zeros; multiplying its symbol is valid almost everywhere. Riemann-Lebesgue decay is therefore applicable. This is not a pointwise inversion at a zero of the symbol.
6. **Probability versus non-Hermitian kernel:** L is not claimed positive semidefinite. The single fact 1/16-c^2>=0 comes from an actual dimer two-edge probability via the known occupation determinant formula. No Hermitian eigenvalue bound is imposed on L.
7. **Numerical scope:** 455 cluster scans, rational finite fusion checks, and the SymPy expansion are checks. Fourier quadrature is not used as a rigorous lower bound. No evaluation c=1/4-1/pi has been claimed proved.
8. **Same-sign collision majorant:** OB intentionally permits singularities between either sign. A3a's functional-graph expansion proves its full local integrability and quantitative collision-tail control, so replacing MB by OB repairs the dominated-convergence step without hiding another integrability gap.
9. **Full problem still open here:** No estimate OB for general n is proved, no nontrivial original pinned field law is identified, and alpha congruent to pi modulo 2pi remains outside the proved two-point range. This counterexample is to our estimate, not to Kenyon's scaling-limit question.

Final second-attempt verdict: **PARTIAL**, with a corrected and narrower next step. The new unconditional results are MB's failure (including a distinct-lattice-site example), the local nonzero fusion channel, the negligible total volume contribution of the fully fused bad regions, and the nearest-neighbor-majorant integrability theorem. The corrected convergence theorem is conditional on OB.


## Final check records

`FusionExponents.lean` passes Lean 4 kernel checking (exit 0): fusion-divergence exponent, vanishing-volume exponent, admissible Holder exponent algebra, and the local mean lower bound. Imports are only Mathlib.Data.Real.Basic and Mathlib.Tactic.Linarith. No sorry, native_decide, or full Mathlib import; printed axioms are propext, Classical.choice, Quot.sound. The final transcript is `fusion_lean_check.log`.

`verify_local_fusion_actual.py` checked the actual u=(i,-1,-i) determinant and det L as exact symbolic polynomial identities; `local_fusion_exact_check.log` records both. `nearest_neighbor_graph_checks.py` exhaustively checked leaf peeling and remaining cycles for 16,739 nonself successor maps on 2 through 6 vertices. This checks small finite cases of A3a's general graph proof; the proof for arbitrary m is the written argument, not an extrapolation from enumeration. Results are in `nearest_neighbor_graph_checks.json`.
