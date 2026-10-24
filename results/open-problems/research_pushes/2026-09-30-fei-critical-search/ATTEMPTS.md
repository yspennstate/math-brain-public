# FEI continuation: global attempts and bounded critical-core search

Started 2026-09-30 03:01 UTC. Full FEI remains OPEN. This is an ongoing attempt record, not a proof certificate.

## Live target

For actual Boolean coefficients a_S, p_S=a_S^2, prove sum_i B_i<=K I for one finite K. Each B_i is exact conditional spectral entropy. All signed identities sum_S a_S a_(S xor U)=0, U nonzero, are retained. A scalar surrogate or a proof for real amplitudes is not automatically sufficient.

## Already completed positive output

The companion package research_pushes/2026-09-30-fei-log-allocation proves the logarithmic child-defect bound, the variance-relative local bound, hereditary short-certificate closure, arbitrary decision-tree log-log leaf bound, and the conditional normalized-collision admission implication. They have independent mathematical review and finite self-checks. They do not bound the universal aggregate residual.

## Explicit attempts and stopping reasons

### A. Raw minor-child amortization

The old additive min-child-influence cost charges independent spectator factors and even parity where actual allocation is zero. Replacing it by variance or largest-atom defect was already done September20. No novelty claimed for recovering those repairs. The new logarithmic child-defect aggregation is materially smaller at rare splits, but the full tree sum remains unpaid.

### B. Mismatch-weighted small-child repair

The genuine sparse activated bent-flip family in the companion REPORT rigorously rejects B_i<=j_i Phi(child influences) for any Phi bounded near the origin. Both child influences tend to zero while B_i/j_i grows linearly with bent dimension. This rejects a previously tentative specific repair, not FEI or an existential good-coordinate selector.

### C. Singleton/finite-order signed cancellation

A simple test vector with independent Bernoulli squared amplitudes and sign+ at the empty coefficient, sign- elsewhere can make every singleton autocorrelation zero at theta=1-2^(-1/(n-1)), but has B/I=h2(theta)/theta tending to infinity. It is not Boolean: weight-two autocorrelations do not vanish. This observation was NOT archived as new because the September20 BOOLEANITY_ORDER report proves a much stronger all-fixed-order, dyadic, bounded-fourth-moment obstruction, including uniformly almost-Boolean variants. Finite-order truncation is retired as a full proof strategy unless an additional all-Boolean consequence is genuinely used.

### D. Exact low-influence idempotence

For a_0 nonzero, all-shift Booleanity gives exactly

    a_U=-(1/(2a_0)) sum_(S not 0,U) a_S a_(S xor U),  U nonzero.

This is retained. Absolute convolution or Cauchy-Schwarz destroys the signed hierarchy and supplies no entropy-weighted O(I) bound. Small total influence does not remove the hard source: tensor many copies of a balanced Boolean seed and activate behind r=o(m), r->infinity controls. The data erasure scales by the activation probability, while the controls add asymptotically negligible influence per seed copy; the original erasure ratio survives with total influence tending to zero. A density-only perturbative estimate cannot be substituted for the missing signed transport.

### E. Relative-influence critical cores

The new variance bound implies that any FEI violation at coefficient C can descend, preserving excess H-CI, to a core with Inf_i/Var<2^(C_var-C) at every relevant coordinate. But this remains full-scope hard even on balanced functions. Character-center any noncharacter seed f so all influences are <=1/2, preserving H and replacing I by J<=I. Let G_m=Maj3 times the disjoint tensor product of m centered seeds. It is balanced, max influence<=1/2, I=mJ+3/2, H=mH+2. Balanced depth-k selfcomposition gives

    max influence<=2^-k, Var=1,
    H/I=[(mH+2)/(mJ+1/2)] [1-(mJ+3/2)^(-k)].

First taking m large then k large preserves any bad seed ratio. This is an application of established exact composition identities, not a newly easier class.

### F. Translation derivatives and entropy integral

For f_z(x)=f(x)f(x+z), the exact discrepancy 2H(f)-E_z H(f_z) is a sum of spectral XOR collision entropy and a nonnegative translation information term. Walsh uncertainty bounds the latter by the former. These identities, the sharp marginal payment <5.394754 times affine-minimum influence, and the signed truth-table integral expansion were already established in September20 sharp-derivative/REPORT.md (blob a0bc9c65e3cc0332bfe9ed996209df9268267a5c).

A derivative has translation symmetry z and can be quotiented by an actual coordinate restriction after choosing a nonzero component of z, preserving entropy and not increasing remaining-coordinate influence. However averaging derivative influences gives 2I-2 sum_i Inf_i^2. The entropy discrepancy is not generally paid by this small quadratic loss. The already proved one-point family makes the discounted derivative influence load grow as dimension/2. The exact signed integral has exponentially large positive fourth-order terms canceled by higher negative terms even on bent phases. These routes cannot be closed by discarding signs, using a fixed potential coefficient, or summing the affine-minimum upper envelope.

## Mandatory actual-Boolean stress baseline

The September22-23 F4 report, proofnet24/P03-fei/continuations/2026-09-22-opus-team/F4-proof-attempt/REPORT.md (blob b8ee8759677c6c115691918aada049d6dd5120e7), supersedes the old 6.003746 tribes-only benchmark. On the 104,976-variable Numaro selfcomposition its source certificate reports approximately

    B/I=4.5388346767,
    min_i B_i/Inf_i=4.5048788574,
    min_i Delta_i H/Inf_i=7.0518528350.

The source's certificate log assumes numpy log2/log1p accuracy within8ulp; this continuation has read the report and exact composition recursions but has not replayed that certificate. Conservative floors are4.5388,4.5048,7.0518. Numerical limiting values are not rigorous bounds. These numbers refute K=4 erasure and small potential-free induction constants, not FEI.

## New bounded computation

One CPU only, fixed seed20260930, exact integer Walsh updates. Functions are invariant under permutations of equal-size blocks and permutations of bits within each block. A function is specified by an arbitrary +/- assignment to the histogram of block Hamming weights. The action is transitive on physical coordinates, so evaluating the true entropy decrement/influence ratio at one coordinate evaluates the existential minimum exactly up to entropy arithmetic.

Runs, sequentially:
- width2,8blocks,n16: at most500,000 proposals or1200seconds
- width3,5blocks,n15: at most500,000 proposals or1200seconds
- width4,4blocks,n16: at most350,000 proposals or900seconds

The total hard wall-time cap is55minutes. No paid compute is used. Annealing/restarts explore arbitrary orbit assignments, beyond the older restriction to toggling <=3 pair-profile orbits. Seeds include tribes, threshold-of-clauses and global symmetric thresholds. Candidate Walsh arrays, exact influence numerator/denominator, Boolean orbit definitions, actual elapsed time and proposal count are saved. Ranking uses double precision and is exploratory; selected candidates must receive a separate integer and high-precision check. No numerical search is a universal proof.

The initial test reproduced width-two eight-tribes rho0=6.003746056559..., as expected. This is a regression check, not a record. The campaign is complete: 9,350,000 objective evaluations and 2,130,944 small orbit assignments yielded no improvement over existing benchmarks. See REPORT.md and RESULTS.json for exact outcomes and six certified candidates.

### G. Exact all-shift cubic entropy identity (new derivation, no payment theorem)

For a_0>0, let the sum below range over ordered (U,T) with U,T,U xor T all nonzero, and let c_(U,T)=a_U a_T a_(U xor T). Multiplying the exact idempotence recursion by a_U log|a_U| and symmetrizing its three nonzero labels gives

    H_nonempty(f)=(1/(3a_0)) sum_(U,T) c_(U,T) log2|c_(U,T)|,
    I(f)=-(1/(3a_0)) sum_(U,T) c_(U,T) |U union T|.

Zero products contribute zero by continuity. The second identity uses |U|+|T|+|U xor T|=2|U union T|. The nonempty entropy formula follows because the ordered triple sum is symmetric in its three labels and because 2a_0 a_U+sum_(T not0,U)a_T a_(T xor U)=0. These identities retain every shift and all signs. They are identities, not an upper bound, and are not claimed to be an easier reformulation than FEI.

The constant Fourier atom has entropy -a_0^2 log2(a_0^2)<=Var(f)/ln2<=I(f)/ln2. A proof would therefore need a signed triangle-log comparison to the signed union-degree sum. Taking absolute values is not justified. On flat bent backgrounds there are exponentially many positive and negative triangles with large cancellation; sparse activation does not remove that issue. No dimension-independent signed triangle comparison was obtained in this pass.

This attempt does not use a continuous flow through Boolean spectra, a finite-order truncation, quantum anticommutation, or a false overlapping-product entropy triangle inequality. The latter restrictions were checked against Section8 of the verified shared route map at brain commit0bdd6c7177d0b756b4b16be317caed29f0cf75e4.
