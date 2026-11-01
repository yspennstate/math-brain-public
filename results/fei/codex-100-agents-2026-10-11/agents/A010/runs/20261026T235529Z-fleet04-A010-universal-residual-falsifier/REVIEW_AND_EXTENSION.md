# Retuning survives unequal replication

A009's complete retuned-reference certificate HOLDS at its stated scope, unchanged statement SHA256 `8d194c974e094b199889fd4d8879d89072158d9996ea93e594826d75eea53836`. The following independent reconstruction strengthens its estimate and allows unequal replication. It does not repair or invalidate A010's earlier fixed-activation obstruction. It changes the activation hypothesis.

Let r,s>=4 be integers. On independent physical bits z0,z1,z2 and r+s disjoint private pairs, put

    f=2 product_(j<=r) OR(z0,z1,X_j1,X_j2)
        product_(j<=s) OR(z1,z2,Y_j1,Y_j2)-1.

All costs are bits. Give each X clause activation 1/(2r), each Y clause activation 1/(2s). Sample an anchor with probability equal to its activation (their sum is one), force its mask uniform on its 15 nonempty subsets, and sample other masks independently: empty with mass 1-alpha and each nonempty mask with mass alpha/15. Output the physical UNION. This source is fixed before observing the Fourier set.

The z1 incidence sum is one, z0 and z2 sums are one half, private rows are at most one. For a mask tuple u let K(u) count nonempty masks and mu(u) be its product-law probability. Each possible anchor contributes mu(u), hence

    Q(A)=sum_(union u=A) K(u)mu(u).

This counts distinct anchor draws, not descriptions of a draw. Sum_A Q(A)=E_mu K=1; Q(empty)=0. Thus the complete optimized posterior cost is -log2 Q(A), including anchor and allocation. There is no conditioned root normalizer missing. The nonempty cost is C_Q=sum_(A!=empty) fhat(A)^2 log2(1/Q(A)).

For a side of length t, write p=1-1/(2t), c=1/(30t), and mu_t(B) for that side's product-mask physical union law. Bernoulli's inequality gives p^t>=1/2, including t=1. Consequently every nonempty subset B of its two core coordinates satisfies

    mu_t(B)>=t c p^(t-1)>=1/60,

by summing the t distinct exactly-one-active tuples; mu_t(empty)=p^t>=1/2. If B contains private coordinates, assign each coordinate to one containing support, obtaining one compatible tuple. Every local probability is >=c (p>=c for t>=1), so mu_t(B)>=(30t)^(-t).

For any nonempty physical output A, assign its private coordinates and z0 to the X side, z2 to Y, and z1 to X if present. The two resulting side sets B_X,B_Y have union A. Independence and K>=1 on every tuple producing nonempty A imply

    Q(A)>=mu_r(B_X)mu_s(B_Y).

Therefore, with E_X indicating that A contains some X-private coordinate, and E_Y defined similarly,

    -log2 Q(A) <= 2 log2 60
        + E_X r log2(30r) + E_Y s log2(30s)
      < 12 + E_X r(5+r) + E_Y s(5+s).

The additional constant on a private side is harmless: it only weakens this bound. All seven pure-core outputs are covered, as are mixed outputs and simultaneous private outputs. This is an analysis witness for a lower bound on fixed Q, not an adaptive change to the source. This sidewise bound is the improvement over A009's global bound.

Set a=(3/4)^r, b=(3/4)^s, u=(1+a)/2, v=(1+b)/2. The actual event is z1 OR [(z0 OR A_X)(z2 OR A_Y)], where A_X and A_Y are products of the private OR pairs. Direct physical pivot conditioning gives

    I = 5/4 -(a+b)/4 -3ab/4
          + [r a(1+b)+s b(1+a)]/6.

Indeed the middle bit contributes 1-uv; the two sides contribute respectively v/2[1-a+(2r/3)a] and u/2[1-b+(2s/3)b]. Thus

    I-5/4 = a(r/6-1/4)+b(s/6-1/4)
                         +ab((r+s)/6-3/4)>0.

Parseval in the private coordinates gives the two physical spectral occupation probabilities

    M_X=P(S intersects X-private) = v a(1-a),
    M_Y=P(S intersects Y-private) = u b(1-b).

For example, condition on all other physical coordinates for M_X. Nonzero variance requires z1=0, the Y event true, and z0=0, with probabilities 1/2,v,1/2; the remaining sign variance is 4a(1-a). This proves M_X. Double occupation is intentionally charged twice because its code bound has two distinct additive side bills; no independence between E_X and E_Y is assumed.

For every integer t>=4, c_t=(3/4)^t<1/3, t c_t<=81/64, and t^2 c_t<7. The first two follow from the successive ratio 3(t+1)/(4t)<=15/16. Check t=4,5,6,7 for the third; thereafter its ratio is 3(t+1)^2/(4t^2)<=1 because t^2-6t-3>=0 for t>=7. Also log2(30t)<5+t, using 30<32 and t<=2^t. Since u,v<2/3,

    C_Q < 12 + r(5+r)M_X + s(5+s)M_Y
        < 12 + (2/3)[5ra+r^2a+5sb+s^2b]
        < 12 + (4/3)(405/64+7)
        = 1429/48.

As I>5/4, C_Q/I<1429/60<24. This proves the unequal-replication feasible certificate analytically. Specializing r=s verifies A009's claim C_Q/I<8083/240<34 by a stronger bound on the identical source. The source statement and contributors are unchanged in that independent review; the strengthening is a separate A010 contribution awaiting review.

Potential failure checks are: actual rather than cloned shared-coordinate influences; normalization when side activations differ; collisions between masks counted by UNION; missing private sectors; the inequality Q>=product side masses; the nonempty-output exception K>=1; boundary t=4; and double occupation. The exact checker uses integer Walsh, independent physical flips, and full integer union/occupation dynamic programming, without importing A009 code. Finite checks supplement rather than replace the all-parameter derivation above. Formal status is recorded separately; no Lean certification of this full theorem is claimed.

The first unsupported universal line is an influence-priced ORIGINAL source for arbitrary Boolean cores, including growing-width and nonfactorable overlap. This proof uses a two-sector factorization with private width two and a bounded three-bit core. It cannot be generalized by treating arbitrary overlap sectors as independent. Its useful effect is to remove unequal replication as a plausible escape from retuning on this existing stress test; it does not settle FEI or the unrestricted representation infimum.

## Adversarial control: globally uniform retuning still fails under imbalance

The distinction between an arbitrary feasible global vector and equal weights matters even here. Instead give ALL N=r+s clauses activation 1/N (still incidence feasible), and keep the same actual anchor/mask sampler. Put p=1-1/N, c=1/(15N), d=p+c. For E={z0,z2}, the exact full-law probability is

    Q_equal(E)=r c d^(r-1)(d^s-p^s)
                    +s c d^(s-1)(d^r-p^r)
              <=2rs c^2=2rs/[225(r+s)^2].

The equality counts all compatible masks and anchor choices: an allowed active mask in each group must be its outer singleton. The inequality uses d<=1 and d^t-p^t<=t c. It is an UPPER bound on the FULL output mass, as required for a lower cost bound, not a selected-tuple estimate.

The physical Fourier coefficient on E has squared mass (1-a)^2(1-b)^2/16>1/81. Also the same physical influence is <29/16<2: drop the negative terms in I and use (r a+s b)<=162/64 and (1+a),(1+b)<4/3. Consequently

    C_equal/I > (1/162) log2[225(r+s)^2/(2rs)].

For fixed s=4 and r tending to infinity this diverges. All references whose nonempty individual-core dictionary branches omit E have the SAME lower bound if their remaining branch is Q_equal: mixing cannot increase the mass of E. Optimal anchor/allocation posteriors are already included. This is a failure of the equal-weight source (and that explicitly fixed-source mixture class), whereas the feasible side-balanced vector just proved has C/I<24 on the SAME functions for every r,s>=4. Thus imbalance is not a counterexample to the activation-weight variational infimum. The all-r proof is analytic; IMBALANCE.json supplies exact finite checks of its generating function signs and boundary inputs.
