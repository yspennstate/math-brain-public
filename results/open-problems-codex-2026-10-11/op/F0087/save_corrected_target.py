from pathlib import Path
P=Path('.')
text=r'''
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
'''
with (P/'SECOND_ATTEMPT.md').open('a',encoding='utf8') as f:f.write(text)
print('Saved corrected target and complete integrability proof.')
