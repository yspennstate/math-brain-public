# account02/B04 early checkpoint — fractional third-volume support gate

Programme: QFORM-DENSITY-3EIG-20260922
Run: account02-B04-20260923T105109Z-auto11
Status: substantive partial calculation; full target remains OPEN.

## First unpaid implication attacked

Previous B04 left `QFORM-SUPPORT-DEFICIENT-DOUBLE-HUB-QUANTITATIVE-PAYMENT-v1`: after the q=1 two-disjoint-bases criterion, determine which support defects genuinely survive the full fractional three-volume window h<3/4 before routing to hubs/ridge/grouped endpoints.

## Fractional base-packing calculation

Let M be an original-coordinate cross block of rank at least three. Delete zero rows and let N be the rank-three truncation of its physical row matroid on active row set E. A row triple S supports some nonzero physical 3x3 minor iff S is a basis of N. For h in (0,1], a probability law on supported physical 3x3 minors with every row inclusion marginal <=h exists iff a probability law on bases of N has vertex loads <=h.

Scale such a probability law by 1/h. This is a fractional packing of bases with vertex capacities one and total weight 1/h. Edmonds' fractional base-packing theorem gives

    nu*(N)=min_{A subset E, r(A)<3} |E\A|/(3-r(A)).

Therefore the exact minimum feasible row cap is

    h_*(N)=max_{A subset E, r(A)<3} (3-r(A))/|E\A|,

and the sharp fractional Fourier parameter forced by support alone is q_*=2h_* (subject to the analytic window 1<=q<3/2).

Consequently support is infeasible for every h<3/4 iff h_*>=3/4. In rank three this has the exact structural alternatives:

1. r(A)=2 and |E\A|=1: one physical row is a coloop;
2. r(A)=1 and |E\A|=2: all but two active rows lie in a rank-one flat;
3. r(A)=0 and |E\A|<=4: there are at most four active rows.

Thus the five-active-row branch in the previous q=1 classification is not intrinsically support-hard for D': the only five-row obstruction is a stronger rank-flat/coloop defect.

## Same-matrix stress family to finish

Take the 5x3 harmonic tight frame before a fixed coefficient rotation,

    u_k=(1/sqrt(5), sqrt(2/5) cos(2 pi k/5), sqrt(2/5) sin(2 pi k/5)), k=0,...,4,

and right-multiply by the rational orthogonal matrix

    V=(1/7) [[6,-2,-3],[-2,3,-6],[-3,-6,-2]].

Let U have rows u_k V and M=2U. Then U^T U=I_3 and every row has squared norm 3/5, so M has singular values 2,2,2, E3(M^T M)=64, and the natural squared-minor law has every physical row marginal exactly 3/5. Numerical symbolic-form checks show all 15 physical entries and all ten row-triple determinants are nonzero; the exact nonvanishing proof and constants will be recorded in the final report.

Thus h_*=3/5 by the average lower bound sum alpha_i=3 and the natural law attains it. The sharp fractional-volume theorem at q=6/5 gives the candidate explicit bound

    ||p_Q||inf <= [3e/((3-12/5)sqrt(6/5))] 64^(-1/6)
                = (5e/2) sqrt(5/6)
                = 6.203601146... .

The completed account03/B04 r31 arbitrary-weight D' theorem gives on the same law

    ||p_Q||inf <= 6 sqrt(e)(6/5)^(-1/2)(3/5)^(-1)64^(-1/6)
                = 5 sqrt(e) sqrt(5/6)
                = 7.525348592... .

Next: prove entry/minor nonvanishing cleanly, optimize the ridge theorem on this identical physical M, embed A=[[0,M],[M^T,0]] (spectrum +/-2, multiplicity three, plus two zeros), and compare the exact certificates.