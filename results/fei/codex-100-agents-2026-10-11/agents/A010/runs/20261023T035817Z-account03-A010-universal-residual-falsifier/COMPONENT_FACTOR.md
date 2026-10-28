# Exact component factorization of the original full queue

All costs are in bits. The result concerns the original queue with one fixed feasible vector of positive gate weights and its original nonempty-root conditioning. It does not choose a different reference after the Fourier set is known. For the finite cost identities assume every positive local spectral mass has positive local reference mass; otherwise the mass identity still holds with the usual extended-real cost convention.

## 1. Exact mass and posterior theorem

Let f_j be nonconstant Boolean functions on disjoint nonempty physical coordinate blocks, q_j=Pr(f_j=-1), and f=OR_j f_j (true is +1). Use the union of their finite gate tables, local orders and subset/count/attachment rules, with global gate ordering whose restrictions are the local gate orderings. Supports of different tables are disjoint. Let D_j=product_(e in j)(1+lambda_e pi_e)-1, D=product_j(1+D_j)-1. For A_j nonempty let W_j(A_j)=D_j Q_j(A_j) be the FULL local queue numerator, summing distinct actual partition runs. Set W_j(empty)=1, the empty history numerator, not a local conditioned probability. Then for every nonempty A,

    Q_f(A)=product_j W_j(A_j)/D.                         (1)

There are no cross-component ownership arcs, so a global admissible owned partition is precisely a tuple of local owned partitions; source SCCs, roots, parent attachments and per-slot child orders split into their local versions. A tuple of local actual FIFO runs has exactly ONE global run: start the globally sorted roots and execute the prescribed queue. The local subsequence of this global FIFO word equals its local FIFO word. This follows inductively because new children append at the queue tail; other components only delay a pop and never reorder that component's pending entries. Conversely deleting other components from a global word recovers the local words. There is no arbitrary shuffle credit or multiplicity. Every node subset/count/composition/child-label factor is local. The root Bernoulli denominators and all absent-gate factors reduce to ONE D; the root numerator factors by component. These facts prove a probability-preserving bijection and (1).

The conditional actual-run posterior given A factors as the product of the local actual-run posteriors on active blocks; empty blocks have the unique empty history. Thus the full ambiguity refund is retained and additive. This is an exact FULL-family statement, not a selected-family lower certificate transferred to a larger family. Infinite zero-probability boundary weights are not needed: all weights are positive.

If the tables are all prime implicants, their union is exactly the prime table of f. Indeed if no block projection of a cube implies f_j, choose a false extension in each block, producing a false extension of f. Hence some projected cube must imply f_j; a prime global cube must be that local prime and fix no coordinates in other blocks. This proves the union assertion also for signed, nonmonotone f_j.

## 2. Exact complete-cost identity and an admissible transfer

Put v_j=4q_j(1-q_j), q=product q_j, v_f=4q(1-q). For any nonempty local Fourier set S,

    sum_(A:A_j=S) fhat(A)^2 = (product_(h!=j)q_h) f_jhat(S)^2.   (2)

To prove (2), write g_j=(1-f_j)/2, so f=1-2 product g_j. At nonempty global sets its coefficient is -2 product g_jhat(A_j); Parseval gives sum g_hhat^2=E g_h^2=q_h, and f_jhat(S)=-2 g_jhat(S) for nonempty S. In particular I(f)=sum_j q_-j I(f_j), q_-j=product_(h!=j)q_h.

Define the UNNORMALIZED occupation bill

    N_j=-sum_(S nonempty) f_jhat(S)^2 log W_j(S)
       =C_j-v_j log D_j.

Combining (1) and (2) gives the exact identity

    C_f=v_f log D+sum_j q_-j [C_j-v_j log D_j].        (3)

Therefore if the same local references satisfy N_j<=K I(f_j), their global union satisfies C_f<=v_f log D+K I(f). The universal signed-implicant root payment then gives C_f< [K+2a_k/ln2]I(f), for widths at least k and a_k=(1-2^-k)/k. For width two, C_f<(K+9/8)I. This last bound uses only actual packing and the same original D.

A complete local bound C_j<=K I_j alone does NOT supply the premise N_j<=K I_j: negative log D_j leaves the additional bill -v_j log D_j. Dropping it is the first unsupported line in an automatic same-reference composition argument. Equation (3), not a renewed local normalizer, is the transferable ledger.

## 3. Pay A009's crossed obstruction with its SAME weights

For the source family let the surviving graph be two disjoint K_(m,m), m>=2, using its existing lambda=1/(2m), pi=1/4, both endpoint orders. Do not change these weights. Within either component, actual one-sided singleton-root labels sum to numerator (m lambda/32)^s=64^-s. For a mixed local output of degree d use A010's generic width-two event, with numerator >=(lambda/72)^d=(1/(144m))^d. Both choices are subfamilies of the FULL original queue.

Thus the component occupation bill is at most (log144)I_B+M_B log m. With u=2^-m, the exact balanced-component moments are I_B=4m u(1-u) and M_B=4m u^2(1-u), so M_B/I_B=u. Since log144<29/4 (equivalent to72^4<2^25) and u log m<=m2^-m<=1/2,

    N_B<(31/4)I_B.

Sections1-2 with the actual two-component spectrum give N_f<(31/4)I_f and the SAME global root term<9I_f/8. Therefore

    C_f<(71/8)I_f<9I_f.                               (4)

This pays the exact inherited crossed-biclique obstruction while J log b/I diverges. No entropy of f is borrowed, no completion replaces f, and there is no reference reset. The source remains a counterexample to paying its coarse J log b bill, but it is not a cost or variational-infimum obstruction. This is a correction to a coding ledger, not a claim of a new FEI class.

## 4. A true complete-posterior representation failure, with bounded infimum

Let r>=2 and m>=2, and let f be the OR of r disjoint K_(m,m) edge DNFs. Compare two globally fixed, packing-feasible vectors on the SAME complete prime table: uniform lambda_U=1/(rm), and componentwise lambda_R=1/m. The latter is not conditioned on A. All local queue rules remain unchanged.

Every distinct width-two run producing A uses at least |A|/2 gates. Rescaling all weights by1/r therefore gives, term by term in the FULL nonnegative numerator polynomial,

    W_U(A)<=r^(-|A|/2) W_R(A).

Consequently C_U-C_R >=(I/2)log r+v_f log(D_U/D_R). This compares complete sums and hence includes the optimal posterior over every actual run, not just chosen witnesses. Let u=2^-m, q_B=2u-u^2. Then I=r q_B^(r-1)4m u(1-u), v_f=4q_B^r(1-q_B^r), and

    v_f/I <=7/(3rm),
    D_U=(1+1/(4rm))^(rm^2)-1 >=m/4>=1/2,
    log D_R<=rm/(4 ln2).

The first inequality follows from (2-u)/(1-u)<=7/3 for0<u<=1/4. The second is the binomial first term. The third follows from log(1+x)<=x, retaining the original normalizer. Since C_R>=0 (the full queue is a subprobability), rm>=4 and ln2>2/3,

    C_U/I > (1/2)log r-35/24.                         (5)

Taking r=2^t and fixed m=2 proves unbounded complete cost for this ONE uniform reference, despite optimizing over ALL actual-run posteriors.

For lambda_R=1/m each component's singleton numerator is32^-s and mixed numerator >=(1/(72m))^d. Hence N_B< (25/4+1/2)I_B=(27/4)I_B. Equations(2)-(3) with the SAME retuned global reference then yield

    C_R<(63/8)I<8I.                                  (6)

The variational infimum over positive feasible global weights and all actual-run posteriors is therefore <=C_R<8I for every r,m. The failed uniform reference does not falsify that infimum or FEI. For r=2 the stronger relevance is (4): even the source's unchanged uniform reference is paid. No all-representation LOWER claim is made.

## 5. Exact adversarial controls and finite symmetry

Dropping the correction in (3) already fails for two disjoint AND2 gates at lambda=1. The exact difference between global complete cost and the influence-scaled sum of local complete costs is (63/32)log2(3)-27/16>81/64 bits. For two edges sharing a coordinate at feasible lambda=1/2, the center-singleton actual numerator is1/32, while multiplying the two local singleton numerators gives1/4096, an exact factor128 error. These are actual queue calculations, not hypothetical spectral laws. They expose respectively the normalizer and shared-coordinate hypotheses before any universal extrapolation.

The crossed K22 finite check uses twenty nonempty output orbits. Its FULL numerator polynomial, not only its spectrum, is invariant under the stated graph automorphisms, with gate variables relabelled. A relabelled owned partition, parent attachment map and per-slot child orders determine one new FIFO run using the newly fixed root order; each probability factor is unchanged. Root order changes its interleaving only and earns no shuffle multiplicity. Thus the monomial coefficients transform by the induced gate permutation. With equal global weights the total output mass is invariant under independent within-side vertex permutations, side exchange in either component and exchange of the equal components. Local counts reduce to the six states(0,0),(0,1),(0,2),(1,1),(1,2),(2,2); unordered pairs give21 states, minus empty-empty. The checker reconstructs every monomial on these20 representatives with two independent enumerators and computes physical Fourier masses for all255 nonempty outputs. It does not infer mass invariance from spectral invariance.

## 6. Precise universal frontier

The factorization and identity(3) hold for arbitrary disjoint physical prime components, including signed functions and arbitrary gate widths, with their original finite tables. They do not split connected overlapping prime incidence. A full universal PI-J proof still needs compatible occupation mass for connected, nonsymmetric overlap, with global weights fixed and all non-root labels, ranks and ambiguity paid. Extending (1) across a shared coordinate is unsupported: both the FIFO product bijection and the physical Fourier projection (2) then fail. The shortest next test is two dense components joined by a genuine shared incidence, keeping the current original table and pricing the resulting compatibility correction rather than charging all perturbation energy a maximum label logarithm.
