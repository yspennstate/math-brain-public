# Independent reconstruction of the A096 active-reset payment

Verdict: the active-reset implication in A096 run20261021T210221Z HOLDS conditional on its explicitly supplied A097 complete-floor cost bound. This review does not independently accept the general A097 source-reference construction, arbitrary interleaved queries or a free-reset strengthening.

The producer's literal checker is read for scope, but is not imported into either A003 checker. The reconstruction uses the stated floor formula and the physical Fourier amplitudes. All source costs and all empty/reference-only fibers remain present.

For a>=2, s=2^-a, t=2^-(a+b), e=2pt with p=2^-r, the actual active erasure is the vacuum binary packet plus (2^a-2)(2s-e)^2+2^a(2^(b+r)-1)e^2. Subtracting the source's nonvacuum erasure gives -2e(1-4s+e)<=0. The vacuum packet decreases because mu=1-2s>=2s and moving (mu,2s) to (mu+e,2s-e) makes the squared pair more uneven. Its derivative reduces to L(z)=ln(1+z^2)-z ln(1+z^-2)>=0 for z>=1. L(1)=0; the lower derivative bound has numerator 2z^3+z^2-1>=2. The segment has positive second entry because e<=s<2s. Thus B_j(F)<=B_j(g). The assumption a>=2 is used, and the producer's a=1 failure is respected.

The complementary child is constant, but its inherited CE k=-log2 q* is not zero. With vj=R({j}), kappa=(2s-e)^2/(4s^2-4se+2et), its q* equals (mu+e)^2+kappa[(1-e/s)vj+2et]. The source marginal vacuum is V0=mu^2+vj. The ratio V0/q* increases with vj: its derivative has numerator A-Bmu^2>=0 after writing q*=A+Bvj. The maximum is at vj=1-mu^2; this algebraic endpoint need not itself be a finite-cost source reference. The producer's inequalities e<=t<=s, 1-kappa<=e/s and qj>=2s^2 have positive denominators. At that endpoint, keeping the positive vacuum shift gives 1-qmax<=6e. Completing the square gives qmax>=27/52>1/2. Hence k-c_const<=-log2 qmax<18e by ln2>2/3. A signed complementary debt can indeed be positive; no monotonicity of CE under an arbitrary reference reset is assumed.

Let W=c+10e(a+b+r). Source marginalization and empty calibration give B_j(g)+(c_child+c_const)/2<=c. The new child envelope contributes 10e(a+b+r-1) after weighting by its half reach, and the complementary excess is below 9e. Therefore B_j(F)+(W_child+k)/2<=W-e. This is an envelope inequality with two full terminals, not a local B/Inf bound. At the last active bit the on-child is an explicit point law; resetting to that known law costs minus its incoming KL and is nonpositive. The false a=1 erasure comparison is not needed. Induction pays all prescribed active histories without creating another ancestor quota.

For K=2C0+10, C0>=0 and c<=C0 I(g), set C=eb,E=ea,J=er. Then I(F)=I(g)+C-E+J and E<=I(g)/2. The gap between K I(F) and c+10(C+E+J) is at least

    (K-C0)I(g)-(K+10)E+(K-10)(C+J)>=0.

The last sign uses K-C0=C0+10, K+10=2C0+20 and K-10=2C0. This proves the supplied-source pricing implication at the original rate. Our exact positive-reset witnesses still satisfy its whole local inequality, so they challenge only the producer's explicitly open stronger sign question. No repair to the paid-reset theorem is required.

Rung: analytic reconstruction of the conditional implication, with exact checks on two adversarial source references. The complete A097 floor theorem is an unpaid dependency of this review. External acceptance, registry adoption and remote persistence are unverified.
