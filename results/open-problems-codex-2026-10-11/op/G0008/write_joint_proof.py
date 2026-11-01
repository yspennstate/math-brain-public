from pathlib import Path
import json
r=json.loads(Path('joint_signed_integer_certificate.json').read_text());coeff=r['counts'];body=r'''

## Proved: the first axial comparison for every parameter

**Computer-assisted theorem.** In iid nearest-neighbour bond percolation on the infinite square lattice,

    tau_1(p)-tau_2(p) >= p(1-p)^6 > 0  for every 0<p<1.       (NEW)

This settles the first comparison uniformly in p, but is still PARTIAL for G0008, which asks every n. The proof is finite and uses symmetry and planarity; it does not use critical self-duality, the no-infinite-cluster theorem, or an infinite-volume approximation limit. Publication novelty remains unverified.

### 1. Exact averaged signed observable

As before, center the middle vertex y at (0,0), and write its cyclically ordered neighbours as x=(-1,0), u=(0,1), z=(1,0), v=(0,-1). Delete the four star edges at y; call the remaining graph K. Let Pi be the partition of these four terminals by K-open connectivity. For a specified partition pi, define Phi_p(pi) to be the conditional probability difference P(x connected to y)-P(x connected to z) after independently restoring the four star edges with parameter p. Then

    tau_1(p)-tau_2(p)=E[Phi_p(Pi)].

Let G=D4 act on the four terminal labels. The law of Pi is G-invariant because K and the iid edge law are invariant under all these rotations/reflections. Define

    barPhi_p(pi)=(1/8) sum_{g in G} Phi_p(g pi).

For each fixed g, invariance gives E[Phi_p(g Pi)]=E[Phi_p(Pi)]. Averaging proves

    tau_1(p)-tau_2(p)=E[barPhi_p(Pi)].                       (S)

This is an expectation identity. It does NOT assert Phi_p(pi)=barPhi_p(pi) for each pi, and no conditional symmetry after revealing the interior is assumed.

The only impossible terminal partition is the crossing pair xz|uv, by the planar face/Jordan argument already proved above. Thus pi belongs to the same 14 noncrossing partitions and six D4 orbits. Directly restoring all 16 subsets of star edges and averaging all 8 dihedral permutations yields

    4 barPhi_p(pi) = sum_{j=0}^4 C_{o(pi),j} p^j(1-p)^{4-j},

with the following complete INTEGER table:

|Orbit|C_0|C_1|C_2|C_3|C_4|
|---|---:|---:|---:|---:|---:|
|s (four singletons)|0|4|8|4|0|
|a (one adjacent pair)|0|6|8|2|0|
|b (one opposite pair)|-2|-2|2|2|0|
|g (two adjacent pairs)|0|8|4|0|0|
|d (triple plus singleton)|-2|2|3|1|0|
|e (all four together)|-4|0|0|0|0|

These are UNNORMALIZED Bernstein coefficients; no binomial factors are implicit in the displayed expansion. The table also follows from the earlier orbit formulas by dividing each orbit coefficient by its orbit size and multiplying by 4. An independent verifier reconstructs it from scratch using 8*16 DSU calculations for each of the 14 partitions.

### 2. Reveal one common finite interior

Let B=[-2,2]^2 and let E_B be its lattice edges, except the four removed star edges. There are 40-4=36 such edges. Expose their states once. Write pi_f for the resulting free partition of the terminals, and mark each block by whether its interior open component meets the vertex boundary of B. This complete visible state is h=(pi_f,hit).

Define A(h) to contain every noncrossing terminal partition r with the following two properties:

1. r coarsens pi_f: vertices in the same interior block remain connected;
2. whenever r merges two distinct pi_f blocks, BOTH blocks are boundary-reaching.

The actual full-K terminal partition Pi belongs to A(h). Indeed, an interior connection cannot be destroyed by adding exterior edges. Conversely an interior terminal cluster that never reaches the boundary cannot use an exterior edge: any path from it to outside B would first reach a boundary vertex, contradicting its definition. Thus such a block cannot merge with any other block. Connections among boundary-reaching blocks may use intermediate exterior or interior components not containing terminals; A(h) allows all such coarsenings, even if some are not realizable. That enlargement only weakens a lower bound. A(h) is nonempty because it contains pi_f. The true Pi is noncrossing by the global planarity argument.

For each h and j, put

    l_{h,j}=min_{r in A(h)} C_{o(r),j}.

Since p^j(1-p)^{4-j} is nonnegative,

    4 barPhi_p(Pi) >= sum_{j=0}^4 l_{h,j} p^j(1-p)^{4-j}.  (L)

The minimum is taken COEFFICIENTWISE, not by selecting a partition that depends on p. This makes (L) valid simultaneously for every p. It is deliberately conservative, and remains valid even if different coefficients attain their minima at different partitions. There is no independence assumption between Pi and h in (L).

### 3. Exact counting of the visible states

Let c_{h,k} count configurations of E_B with k open edges and visible state h. Since these 36 edges are iid,

    P_p(h)=sum_{k=0}^{36} c_{h,k}p^k(1-p)^{36-k}.

There are exactly 80 visible states with nonzero counts. All 80 coefficient arrays appear in joint_R2.json. The finite transfer recurrence that calculates them has the following invariant: at every step, active vertices carry their exact processed-edge connectivity partition and each component carries an OR flag recording whether it has touched a boundary vertex. Keep all four terminal marks forever, introducing every other vertex at its first incident edge and removing it immediately after its last incident edge. A vertex on the boundary begins with hit flag 1; other introduced vertices begin with flag 0. In the open branch, merge the two endpoint components and OR their hit flags. In the closed branch, do not merge. Then restrict the partition to the retained vertices and canonically relabel its components, retaining their flags. A component forgotten completely can never reconnect later, so discarding it is safe. This proves the invariant by induction over the edges. Counting closed branches in degree k and open branches in degree k+1 proves the recurrence counts each configuration exactly once with its correct state and open-edge count.

Explicit edge ordering: scan x=-2,...,2 and y=-2,...,2, skip y's central vertex (0,0), and append the horizontal edge from (x-1,y) when present and the vertical edge from (x,y-1) when present, omitting all four central-star edges. The code independently checks sum_h c_{h,k}=binomial(36,k) for every k. Reversing the entire edge ordering yields the SAME 80 arrays, coefficient for coefficient. Exhaustive enumeration of all 256 rim-edge configurations in the analogous radius-one punctured square checks both partition and hit flags against the transfer implementation.

Taking expectations in (L), using (S), and convolving the two finite expansions gives

    4[tau_1(p)-tau_2(p)] >= sum_{t=0}^{40} d_t p^t(1-p)^{40-t},
    d_t=sum_{h} sum_{k+j=t} c_{h,k} l_{h,j}.                (C)

Every quantity on the right is a finite integer. This is where the independence/product-measure realizability information missing from earlier abstract partition inequalities enters: the 80-state law is the law of an actual 36-edge patch, not an arbitrary associated terminal-partition distribution.

### 4. The exact integer certificate and conclusion

The full coefficient vector d_0,...,d_40 is:

    COEFFICIENT_VECTOR

Here d_0=0 and d_35=...=d_40=0. For every j=0,...,33, exact integer comparison gives

    d_{j+1} >= 4 binomial(33,j).                            (I)

The minimal normalized reduced coefficient is exactly 4, attained at both ends. To see directly how this concludes the proof, substitute (I) into (C):

    4[tau_1-tau_2] >= 4 sum_{j=0}^{33} binomial(33,j)
                           p^{j+1}(1-p)^{39-j}
                    =4p(1-p)^6 [p+(1-p)]^{33}
                    =4p(1-p)^6.

Dividing by 4 proves (NEW), and strictness follows from 0<p<1.

### 5. Independent and formal checks of this proof

- verify_joint.py independently enumerates the 14 partitions, all 8 D4 actions and all 16 restored-star subsets. It rebuilds the integer orbit table and computes each coefficientwise minimum over A(h).
- The same verifier directly convolves each of the 80 visible-state count arrays with those integer minima. This result agrees with the independent normalized-Bernstein/grouped implementation in certify_joint.py.
- The 36-edge visible-state arrays agree under forward and reverse edge order; an exhaustive 8-edge radius-one calculation agrees with all partition/flag arrays. The radius-one lower bound is actually negative (-1/16), a useful check that the method has not assumed positivity.
- JointCertificate.lean checks the 34 integer dominance inequalities in (I) with `decide +kernel`; the theorem has NO axioms. It also checks list lengths and the sign lemma used in Approach B. No sorry and no native_decide are used. The explicit baseline integers are checked against Python math.comb; the binomial sum identity is proved above. Lean does NOT formalize the graph enumeration, symmetry argument or boundary coupling.
- All files and proof calculations remain inside the problem folder. This is a computer-assisted proof with transparent, small finite inputs, rather than a claim that the full probabilistic argument has been formalized in Lean.

### 6. What does not follow

The theorem covers exactly n=1 in d=2. The D4 orbit average works particularly well because the source is itself a neighbour of the deleted middle vertex. For a source at distance n>=2, rotations move the source to further axial vertices, and the observable involves more terminals; the same six-orbit table does not apply. Thus replacing 1 and 2 by arbitrary consecutive n is unjustified. Higher-dimensional stars also have extra neighbours and lose the single-face noncrossing restriction. No all-n or all-d result is claimed.

## Approach B: a finite obstruction, not a percolation counterexample

Let the five partitions of three boundary terminals be

    1|2|3, 12|3, 13|2, 23|1, 123.

The random-cluster boundary joining matrix M(q) has entry q^{number of blocks of pi join rho}. Directly joining these partitions gives

    M(q) = [[q^3,q^2,q^2,q^2,q],
            [q^2,q^2,q,q,q],
            [q^2,q,q^2,q,q],
            [q^2,q,q,q^2,q],
            [q,q,q,q,q]].

For v=(1,-1,-1,-1,2), multiplication yields

    v^T M(q) v = q^3-3q^2+2q = q(q-1)(q-2).

This is negative for every 1<q<2, because q>0, q-1>0 and q-2<0. At q=3/2 its exact value is -3/8. Therefore this boundary joining matrix is not positive semidefinite anywhere in (1,2). The generic reflection-positivity route cannot be justified by analytically continuing the integer-q boundary Gram matrix toward q=1. Moreover v^T M(q)v/(q-1) tends to -1 as q decreases to 1, so taking the first nontrivial derivative of the rank-one q=1 matrix does not repair that particular positivity argument. This is an obstruction to the proposed proof method, not a refutation of axial monotonicity. Symbolic matrix arithmetic is in reflection_join_obstruction.json; the real sign implication is checked in JointCertificate.lean.

This check also rejects the brain card's loose phrase suggesting the Potts representation automatically supplies reflection positivity for all real q>=1. Only the directly verified finite obstruction is used here; no broader reflection-positivity classification is asserted.
'''
body=body.replace('COEFFICIENT_VECTOR',str(coeff));
with Path('ATTEMPT.md').open('a',encoding='utf8') as f:f.write(body)
with Path('CLAIMS.jsonl').open('a',encoding='utf8') as f:
 for c in [
 {'claim':'On Z^2 with iid nearest-neighbour bond parameter 0<p<1, tau_1(p)-tau_2(p) >= p(1-p)^6 >0 for every p.','status':'proved_special_case','proof_location':'ATTEMPT.md, Proved: the first axial comparison for every parameter; joint_signed_integer_certificate.json','remaining_gap':'Comparisons tau_n-tau_{n+1} for n>=2 and the all-d statement remain unresolved.','checks':['Complete D4 averaged observable and common-boundary coupling proof.','80 visible-state arrays agree in reversed-edge transfer.','Independent exhaustive radius-one partition/flag enumeration.','Independent D4 8x16 star enumeration and integer convolution.','34 coefficient dominance inequalities passed decide +kernel in Lean; the graph enumeration is not formalized.']},
 {'claim':'The five-state boundary joining matrix q^{blocks(pi join rho)} is not positive semidefinite for 1<q<2; v=(1,-1,-1,-1,2) has quadratic form q(q-1)(q-2)<0.','status':'counterexample','proof_location':'ATTEMPT.md, Approach B: a finite obstruction; reflection_join_obstruction.json','remaining_gap':'This is a counterexample to the proposed matrix positivity, not to G0008.','checks':['Exact symbolic matrix calculation.','Sign implication checked in Lean.']}
 ]:f.write(json.dumps({'problem_id':'G0008',**c})+'\n')
p=Path('STATUS.md');s=p.read_text();s+='\n2026-10-11 continuation: Proved the full-parameter first axial comparison tau_1-tau_2 >= p(1-p)^6 by a common-boundary 36-edge finite certificate. Independent counting and kernel integer checks passed. Testing extension to n=2; original problem still PARTIAL.\n';s=s.replace(s.splitlines()[1],'NEXT: Finish the n=2 extension diagnostic and audit the written all-parameter first-step proof.');p.write_text(s,encoding='utf8')
