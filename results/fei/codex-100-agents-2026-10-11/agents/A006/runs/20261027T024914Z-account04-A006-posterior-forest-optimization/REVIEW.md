# Independent reconstruction of the unequal-replication source

A010-UNEQUAL-CORE-RETUNING-AND-UNIFORM-WEIGHT-OBSTRUCTION version1 HOLDS at its stated scope, with unchanged statement identity 8d8797db2b40e832e14d578d77b4f98179f5a2bdb3d929dded4b75ce705828fa. The reviewer supplies no repair. The source is A010/runs/20261026T235529Z-account04-A010-universal-residual-falsifier/REVIEW_AND_EXTENSION.md, including its adversarial-control section. This review concerns that entire statement; it does not independently accept every older dependency mentioned in the source report.

For r,s>=4, the physical event is z1 OR [(z0 OR A_X)(z2 OR A_Y)] where A_X and A_Y are products of r and s disjoint width-two OR clauses. With a=(3/4)^r, b=(3/4)^s, u=(1+a)/2, v=(1+b)/2, the middle bit contributes 1-uv to influence, and the two sides contribute v[1-a+(2r/3)a]/2 and u[1-b+(2s/3)b]/2. Therefore

    I=5/4-(a+b)/4-3ab/4+[ra(1+b)+sb(1+a)]/6.

Conditioning on physical outside variables (without cloning shared bits) gives private Fourier occupation M_X=va(1-a) and M_Y=ub(1-b). These identities use conditional variance, not an independence assertion about the Fourier occupations. The exact target atom {z0,z2} has mass (1-a)^2(1-b)^2/16.

Give the r-side clauses activation1/(2r), the s-side clauses1/(2s). The activities sum to one and all physical incidence sums are at most one. For an actual mask tuple, sum over all its actual possible anchor draws: Q(A)=sum_(union=A) K mu, hence sum Q=E_mu K=1. Every anchor and every allocation is retained. For side length t, empty mass p=1-1/(2t), each nonempty local mask c=1/(30t), and p^t>=1/2. A nonempty pure-core subset has side probability at least t c p^(t-1)>=1/60. For a subset with private bits, select any compatible tuple; its probability is at least (30t)^(-t). For any output A allocate z1 to X, outer bits to their own side, and private bits to their own side. On nonempty union K>=1, so Q(A)>=mu_r(B_X)mu_s(B_Y). This step is a lower bound by a subset of actual tuples, not a replacement of the full law by one tuple.

Thus the cost is less than 12+r(r+5)M_X+s(s+5)M_Y. For t>=4, (3/4)^t<1/3, t(3/4)^t<=81/64, and t^2(3/4)^t<7; the third follows from checking4..7 and a nonincreasing successive ratio afterwards. Also u,v<2/3. The full cost is consequently below1429/48. The displayed influence gives I>5/4, proving C/I<1429/60<24. Both private occupations are charged when both occur; the two bills correspond to two side factors, so no false independence or missing double-occupation correction is involved.

For equal activation1/(r+s), set N=r+s, p=1-1/N, c=1/(15N), d=p+c. The FULL mass at {z0,z2} is

    r c d^(r-1)(d^s-p^s)+s c d^(s-1)(d^r-p^r)
       <=2rs/[225N^2].

Indeed the only allowed active masks are the respective outer singleton on each side; marking each allowed anchor yields the two terms. The inequality uses d<=1 and d^t-p^t<=tc. For r,s>=4 the physical target mass exceeds1/81 and I<2, giving C_equal/I>(1/162)log2[225N^2/(2rs)]. Fixing s=4 and sending r to infinity proves divergence. Any added branch supported inside one of the individual cores omits {z0,z2}, so no fixed mixture with those branches increases this atom above the original equal-weight mass. This argument does NOT exclude a new feasible weight vector; the side-balanced vector has just paid the same family.

Independent code/review.py imports no peer executable. It uses truth-table Walsh coefficients and physical bit flips, and reconstructs the complete source by a union/occupation DP. Four physical pairs r,s=1,2 verify the identities outside the theorem's r,s>=4 estimate range; they are identity checks, not assertions that the source proof assumes those smaller parameters. All3721 scalar pairs r,s4..64 check the proof's numerical inequalities, with analytic ratio reasoning covering the unbounded range. out/REVIEW.json records11673 exact assertions. The source is an author proof now independently reconstructed at the complete stated scope; no shared registry adoption, remote mirror, or full-FEI acceptance follows.

This consumes the current retuning objection to A006's earlier fixed-law NEXT. The next all-weight certificate must keep the physical feasible parameter set. An obstruction to fixed equal weights alone is insufficient.
