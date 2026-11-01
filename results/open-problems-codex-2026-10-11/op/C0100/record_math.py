from pathlib import Path
p=Path('ATTEMPT.md')
p.write_text(p.read_text(encoding='utf8')+r'''
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
''',encoding='utf8')
