# Source-bound whole-statement reviews

These reviews use fresh complete proofs, direct physical Fourier expansion, different independently written rational code, and the exact source statements. No source executable is imported. New A006 results in CORE_CLOSURE.md remain author proofs pending independent review, and are not required to repair either source.

## A008 common-anchor obstruction and fixed core repair @1

Source: A008/runs/20261023T121653Z-fleet03-A008-gate-label-compression, complete COMMON_ANCHOR.md, REPORT.md and selected CLAIMS.json entry. Statement SHA256 as recorded by the source: f6e2559e906465e54cfeeaeda85415530d987e63c28b73ea05a9774b802081a0. Verdict: HOLDS at the FULL stated scope; no repair supplied.

Reconstruction: direct pivots give I_z=1-a and private sum J=a sum w epsilon/p. Direct expansion f=1-2(1-z)(1-U) gives core coefficient (1-a), two equal private coefficient copies Uhat(B), total private pair mass 2a(1-a), and block occupation 2a epsilon. For private B the mask allocation is unique, while every nonempty choice of core inclusion among its L active blocks is a distinct actual tuple with unchanged anchor multiplicity. Hence the asserted Q(B) and Q(B+z)>=Q(B) hold without a cloned-coordinate Fourier model.

For width two, the weighted product derivative at the core singleton gives Q(z)=(1/7)(25/28)^(r-1). For r>=4, a<1/2 and I<2: r(3/4)^(r-1) is maximal at r=3,4, and then decreases. Since ln(28/25)>=3/28 and ln2<1, the single atom proves C/I>3(r-1)/224. The product private spectral law nu has local empty probability3/4 and each nonempty probability1/12; grouping core and private coefficients yields EXACT H=2aH(nu)+2(1-a)h2(a), and H<6I as stated. This entropy estimate is independent of the coding obstruction.

For R=(delta_z+Q)/2 normalization and the paid once-only label hold. Its private-output upper length is bounded by 1+log_+rho+sum_active(2w+2)+3rho. Average the exact moments above. The core cost is <=(1-a)^2; the four remaining payments are <=2J, (3/2)J, 3J and8J respectively, yielding (1-a)+(29/2)J<=(29/2)I. The standard wrapper adds<=2I. All arbitrary widths/counts and actual allocation ambiguity are covered. The new A006 17/2 bound is a separate strengthening/generalization, not a repair of the source's valid 29/2 statement. A006 authored the normalization premise of this source; A008 and A009 already reviewed that premise independently. This review independently reconstructs the new A008 extension and does not claim A006 can independently review its own prior premise.

## A009 all-activation uniform-mask obstruction @1

Source: A009/runs/20261023T124853Z-fleet03-A009-fractional-incidence-optimization, complete RETUNING_OBSTRUCTION.md, REPORT.md and selected CLAIMS.json entry. Source statement SHA256: 270cb5c13039d7be9638588190c3e5f056a6537218b3b887b9a026863e41920e. Verdict: HOLDS at the FULL stated scope; no repair supplied.

Conditional on the ENTIRE nonempty active support set K, independent uniform local subsets yield Q(z|K)=N^(-|K|)<=1/N, N=2^(w+1)-1. This step uses the conditional independence explicitly present in the hypotheses, rather than multiplying marginal bounds. Averaging over any dependent activation law, and then over any mixture, preserves the pointwise ceiling. Forced-anchor samplers satisfy the same conditional law. The optimal posterior cannot change Q(z).

For r=w2^w, the binomial inequality gives a=(1-2^-w)^r<2^-w. The physical identity is I=1-a+a w^2/(1-2^-w)<2 for w>=8, using w^2/2^w decreasing and its value64/256 at8. The actual singleton mass (1-a)^2>1/2 and log N>w yield C/I>w/4. The exact private-product entropy identity H=2ar h_w+2(1-a)h2(a), with h_w<2w epsilon+(3/2)epsilon/p, gives H<(4+3/w)J+2(1-a)<(35/8)I. Thus the witness is an actual bounded-FEI Boolean family, and the conclusion is only a reference obstruction. Boundary w=8 and every inequality's monotone extension were checked analytically; scalar rational checks cover w8..128, not giant truth tables.

## A009 dual read as context, not adopted as a third reviewed claim

DUAL.md was read completely. Its fixed-witness convex upper bound retains the negative allocation entropy and separately accounts for the negative nonempty normalizer; its KKT stationarity is rational. No claim is made here to have run a full independent reconstruction of its finite optimum certificates. The new stage does not use this dual as a proof premise.

## Checks and scope

FROZEN_SPEC.json precedes execution. code/check.py reconstructs spectra by integer Walsh transform and checks every influence against direct physical edges, then computes full physical-union probabilities with a fresh Fraction weighted convolution. Pilot conditional-anchor enumeration independently compares the actual run law. The core size-one rows reproduce A008's entire local probability/physical moment chain; the source asymptotic estimates are proved above rather than inferred from the finite checks. The final report records executed receipts. A006's old claim received separate full-version HOLDS reviews from A008 and A009; source files and old run remain unchanged. Shared registry adoption and remote persistence are unverified.
