# Maximal-matching star completion for arbitrary simple graph prime tables

Let G be any nonempty finite simple graph on its covered physical coordinates. Let f_G be +1 exactly when some edge has both endpoint bits +1. Every edge conjunction is a prime implicant, and these are all primes: any true partial assignment must contain a complete positive edge, since otherwise setting every unspecified coordinate negative gives a false completion. Fix both endpoint orders in every width-two gate, pi_e=1/4, and ANY strictly positive feasible weights lambda_e, sum_(e incident v)lambda_e<=1. The reference is fixed globally before A is sampled. Put D=product_e(1+lambda_e/4)-1. All costs are bits.

With both orders, theta_1 is identically one on the two endpoints. The original size-and-subset draw probabilities are t({v})=1/4 and t({v,w})=1/6. These are actual probabilities, not surrogate weights. In particular the width-two singleton probability is not 1/2.

## Exact completed mass

Fix any covered nonempty set A. Let M be a MAXIMAL matching in G[A] (inclusion-maximal, not necessarily maximum-cardinality), let V(M) be its matched coordinates and U=A\V(M). Maximality implies U is independent in G. For every u in U choose a neighbor nu(u) in G. It lies in V(M) or outside A. For every matched edge e={v,w}, use gate e with owned subset {v,w}. For each u in U use the distinct gate {u,nu(u)} with owned singleton {u}. If nu(u) is matched, attach this singleton gate as a child of the unique matching gate owning nu(u), at that coordinate. Otherwise make it an isolated root. No two chosen singleton gates coincide: such a collision would require an edge within U, impossible. None equals a matching gate.

The full ownership-incidence graph of these used gates is exactly a disjoint union of outgoing stars and isolated roots. Singleton owners have no outgoing edges, because U is independent and no other chosen gate contains their u. Matching roots own both endpoints and have precisely their prescribed singleton children. Hence these are actual source-SCC partition forests, not arbitrary covers requiring extra roots. All selected subsets are disjoint and the queue terminates.

For e={v,w} in M let h_v,h_w be the numbers of children attached at its endpoints, and c_e=h_v+h_w. Let b(nu) be the number of choices with nu(u) outside A. Summing every chronological ordering within the repeated attachment slots gives the following EXACT conditioned mass for this matching:

    Q_M(A) = (1/D) product_(e in M)(lambda_e/24)
                 * sum_neighbor_choices_nu [ product_(u in U)(lambda_{u,nu(u)}/8)
                       *4^(-b(nu))
                       *product_(e={v,w} in M) h_v! h_w! / [(c_e+1)^2(c_e+2)] ].       (1)

Ledger: matched roots pay lambda_e*pi_e*t_e=lambda_e/24; their child count pays 1/[(c+1)(c+2)] and uniform attachment multiset pays 1/(c+1), since they own two coordinates. Exactly h_v!h_w! chronological child-label sequences occur. Every singleton child pays lambda*t_singleton*Pr(c=0)=lambda/8. An external singleton ROOT additionally pays pi=1/4, producing lambda/32. D includes all absent-root probabilities and nonempty-root conditioning. Root order and order between distinct attachment coordinates remain fixed; there is no permutation credit for either.

Different matchings and neighbor choices give disjoint actual events. The size-two owned subsets uniquely recover M. Each singleton selected subset together with its visited gate ID uniquely recovers nu; parent and attachment are recoverable from actual appended-child draws. Thus

    Q_MS(A)=sum_(maximal matchings M in G[A]) Q_M(A)                         (2)

is a genuine subprobability output lower mass, Q_MS(A)<=Q_part(A)<=Q_*(A). It is strictly POSITIVE for every covered nonempty A, including every positive Fourier-mass set. The empty matching is included precisely when G[A] has no edges. This closes the matching-sector coverage defect identified by A009; it does not yet pay universal expected cost.

## Explicit computable lower bound

For integer c>=0, (c+1)(c+2)<=2*3^c and c+1<=2^c (induction). Therefore [(c+1)^2(c+2)]^-1 >= (1/2)*6^-c. Discarding h!>=1, each matching gate contributes at least lambda_e/48 and each internal singleton child at least lambda/48. An external singleton root contributes lambda/32>=lambda/48. If r_u=sum_(v neighbor u)lambda_uv, independent summation over neighbor choices yields

    Q_M(A) >= (1/D) 48^(-( |M|+|U| )) product_(e in M)lambda_e product_(u in U)r_u.      (3)

Summing (3) over maximal matchings is another computable positive lower mass L_MS(A). Hence -log2 Q_MS(A)<=-log2 L_MS(A). For one chosen M, the upper cost is

    log2 D + (|M|+|U|)log2 48
            +sum_(e in M)log2(1/lambda_e)+sum_(u in U)log2(1/r_u).           (4)

This is a FULL queue cost with no omitted overhead or free table choice. Conditional on A, posterior eta(r)=q(r)/Q_MS(A) retains the final output ambiguity and gives E[-log q]-H(eta)=-log Q_MS(A). Root identity, both orders, all original subset/count/multiset factors and failure/infinite-run exclusions remain explicit. Computing every maximal matching may be exponential; no polynomial-time claim is made.

If A is independent, the empty matching is unique and all singleton choices are external roots. Formula (1) specializes to Q_MS(A)=D^-1 product_(u in A)(r_u/32), agreeing with the already-derived independent sector. This specialization is a consistency check, not a new claim about that closed sector.

## Exact first unpaid line

Coverage is resolved for every graph prime table, including the 104 positive-spectrum failures reported by A009 at n=4. But the label/row term and matching multiplicity still need spectral payment. A sufficient unproved inequality is

    E_(A!=empty) P_f(A) [-log2 sum_M 48^(-( |M|+|U| ))
                              product_(e in M)lambda_e product_(u in U)r_u]
        + Var(f)log2 D <= K I(f_G)                                    (5)

for one globally fixed feasible positive lambda and dimension-independent K. Equation (5) is not inferred from pointwise positivity, density, or small cubes. No universal FEI bound, arbitrary hypergraph extension, or divergence obstruction is claimed. A sharper route should use the exact factorial credit in (1) rather than discard it as in (3), and local incidence cancellation from A010 to weight the non-independent Fourier sectors. This is a general missing-component interface, not another isolated complete-graph FEI calibration.
