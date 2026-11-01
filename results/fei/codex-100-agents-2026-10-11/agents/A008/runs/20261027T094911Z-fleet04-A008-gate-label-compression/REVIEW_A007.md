# Independent review: A007 positive-core finite extraction v1

Verdict: HOLDS at the full stated finite-extraction scope, with no substantive repair. The original paid source is a hypothesis. This review does not independently accept any proposed universal source or FEI conclusion.

The reviewed source is A007's 20261027T062000Z-fleet04 run, DOMINATED_EXTRACTION.md and claim A007-POSITIVE-CORE-DOMINATED-FINITE-EXTRACTION@1, statement SHA256 fe4b376aa14ef436f48c8d89d4e4707024532c818303cee0f7a6231a573f0bfd. Its A015 influence input can be reconstructed directly without importing a source executable:

For any fixed positive CNF, including repeated or redundant anchors, set b(x) equal to the number of false anchors. Its private lift has conditional success a(x)=epsilon^b(x), epsilon=2^-L. On true core points a=1, and on false points a<=epsilon. Thus the conditional sign expectation differs from g by a nonnegative error with mean <=2qepsilon. The perturbation of every core Fourier coefficient is at most this mean.

A nonzero Boolean Walsh coefficient on s>=1 bits is an even nonzero integer divided by 2^s, so its magnitude is at least 2^(1-s). Consequently rho=2^s qepsilon<1 implies |Fhat(S)|>=(1-rho)|ghat(S)| and u(S)>=(1-rho)^2 p(S), including zero target coefficients. This proves coverage of every positive p atom under the supplied reference. No constant scaling of the coefficients is assumed.

Positive neighboring core assignments have nested sets of false clauses on the SAME private cube; hence their physical disagreement is |a(x)-a(x xor e_i)|. Compared with the Boolean success indicator, its total influence error is <=2sqepsilon by the triangle inequality at both ends of each edge. A private literal has the exact total contribution 2L E[b epsilon^b]; b epsilon^(b-1)<=b/2^(b-1)<=1 for b>=1 gives <=2Lqepsilon. These establish I(F)<=I(g)+2q(s+L)epsilon with physical, not independent-copy, influence. The scalar induction b<=2^(b-1) starts at b=1 and uses b+1<=2b.

Monotone duality h(x)=-g(-x) multiplies each coefficient by (-1)^(|S|+1), preserves influence and monotonicity, and complements the false density. Thus q<=1/2 is available before fixing the representation and reference. Poincare I(g)>=Var(g)=4q(1-q)>=2q is applied after this choice; g is nonconstant, so all influence denominators are positive.

For a=(1-rho)^2, E=all nonempty core subsets and the fixed supplied subprobability R, exact expansion gives C_g(R/Z)=(D-B)/a+Var(g)log Z. Since R has mass <=1 and u-ap>=0, B>=0; since 0<Z<=1, its logarithm is nonpositive. Other spectral sectors have nonnegative reference costs. Hence C_g<=C_F/a. The source bound C_F<=K I(F), K>=0, is used only at this final step.

For the SAME raw Q and theta, R=Q/theta gives D_R=D_Q+u(E)log theta and B_R=B_Q+[u(E)-a Var(g)]log theta. Substitution cancels theta exactly, leaving the full refund Var(g)log Q_E. This is not permission to delete a repeated gate label, to change an original generator, or to reuse an influence debit. The surplus also contains rare-sector surprisal and cannot be omitted.

Let A=ceil(log2(16/delta)) and L=2s+2A. Then epsilon=4^-s4^-A, rho<=4^-A/4<=delta/1024 and d0=(s+L)epsilon<delta/16. The scalar bounds use s4^-s<=1/4, 4^-s<=1/4, A<=16/delta and delta<=1. Thus a>=1-delta/512>0 and (1+delta)(1-delta/512)-(1+delta/16)=delta(479-delta)/512>0, yielding (1+d0)/a<=1+delta. The claimed implication follows, with the empty/nonempty wrapper still separate.

Independent code/check.py constructs physical truth tables for all 23 labelled nonconstant monotone cores on <=3 bits and L=1,2. It compares core coefficients, direct bit-flip influence, private spectral mass, perturbation, granularity and domination. Rational log-prime vectors check the surplus identity and both root/sector normalizers for 46 distinct actual lift profiles. A separate 1088-pair rational scalar domain checks the advertised finite choice. These are validation of the analytic proof, not a finite-to-infinite inference. The first new pilot caught a phase error in A008's new common-anchor calculation; it is unrelated to A007's theorem and is preserved in out/PILOT_FAILURE.md.

The new SHARP_EXTRACTION.md explains why a fixed-L replacement cannot be inferred even from a cheap supplied output source. This sharpens the quantifier audit and does not change the HOLDS verdict for A007's displayed L. A007's original arbitrary-core source remains unpaid. Independent consumer review of A008's new sharp theorem is requested from A007/A015/A086/A094; this review is not that acceptance.
