# Independent review of singleton and pair reserve interfaces

Reviewer A052; original versions unchanged, no substantive repair supplied. The new signed-merging correction is a subsequent A052 application, not a contributor repair to these sources. Shared registry adoption is not asserted.

## A055-SINGLETON-CRITICAL-RESERVE@1

Source: A055/runs/20261014T004129Z-fleet05-A055-extremal-obstruction-referee/PROOF.md and CLAIMS.json. Statement hash bfc2c09293d9446e7301b5c562668288de096d6758459530ec93bf1db80c09bf. Verdict HOLDS at the full analytic scope.

Reconstruction: For a singleton real coefficient pair a,b, the physical squared row density has two values 1 plus/minus 2ab/(a^2+b^2). The conditional spectral entropy is h2(e), e=min(a^2,b^2)/(a^2+b^2), and its squared density variance is c=4e(1-e). Direct expansion of (1+z)ln(1+z)+(1-z)ln(1-z) produces the stated nonnegative series for j(c). Since coefficients sum to ln2 at c=1, j(c)<=c. The binomial-series coefficient bound proves j(c)<=2e/ln2; its induction is valid at every integer k>=1. Entropy concavity then gives L<=h2(C/2)+C. The Fourier point mass of either singleton Boolean phase lies at a dominant coefficient, including ties; its TV distance is e.

Retain the EXACT identity D+S=L-K Inf and O=Inf-beta. Hence D+S+K O=L-K beta. Apply the preceding row entropy/recentring estimates and maximize h2(x)-(K-2/ln2)x. Differentiating the binary entropy gives precisely log2(1+2^(2/ln2-K)). The log bound by its argument yields the weaker exponential estimate. Nonnegative S requires the explicitly stated essential-dimension minimality; the algebraic identity and scalar upper bound themselves do not. No positive lower bound on D is supplied.

## A051-TWO-BIT-CRITICAL-PHASE-RESERVE@1

Source: A051/runs/20261014T012634Z-fleet05-A051-near-extremizer-definition/TWO_BIT_RESERVE.md and CLAIMS.json. Statement hash 25d00942803b7fd8918a198dc313101701674dc04a88f5919f6624bf28288e09. Verdict HOLDS at the full analytic scope.

Reconstruction: The fourteen nonconstant two-bit Boolean phases have influence at least1, by counting square boundary edges; H<=2 for every four-atom law. The unit-vector norm-to-squared-law TV argument is Cauchy--Schwarz and Walsh orthogonality. For c<=1/16 it changes influence by at most2sqrt(c)<=1/2, yielding the good phase deficit at most2-K/2. Constant phases have nonempty mass e=1-(E|u|)^2<=||u-sign(u)||_2^2<=c; grouping the three nonempty atoms gives h2(e)+e log2(3)-Ke, whose maximum is log2(1+3*2^-K). Bad phases contribute at most2 and their mass is at most16C. Weighting all three cases with actual q and retaining S_A proves the bank. Concavity of the capped four-atom entropy function proves the pure collision modulus, including the cap above3/4. The quartic Cauchy--Schwarz proof of C<=6I is valid; it supplies no selected-block contradiction.

The parity sign (-1)^((x_i xor x_j)y) has nonzero amplitudes at empty,y,ij,ijy. Its singleton minority/collision masses vanish but each orientation energy is1/2; pair collision1 remains. This defeats only the source's explicitly unconditional comparison. The new A052 orientation-corrected inequality passes this guard and cannot omit its correction.

## Executed validation and scope

The frozen direct-character checker independently reconstructs all labelled singleton and pair cuts through three Boolean variables, plus fixed NAND6 and parity controls. It verifies the A055 complete singleton bank with actual signed child reserves at K=2,4,8, using the rigorously weaker rational exponent floor 2/ln2<3. It verifies the A051 row-class bank at K=4,8 using exact log2(1+3*2^-K), W0,Wg,Wb and actual L-KI, without assuming arbitrary roots are critical. The saved CHECK.json gives final counts and runtime. The new signed quartic/refund identity is separately checked on 625 arbitrary rational real quartets; those are algebra tests, not Boolean FEI witnesses. No source finite census total is adopted from its report.

The source-bound A055 independent acceptance of A052's prior phase-exclusion theorem is consumed, with the analytic-versus-finite-census scope intact. It is not rewritten into the old run. Both reviewed results leave the universal pair-selection and terminal-payment gap open, as do the new corrections.
