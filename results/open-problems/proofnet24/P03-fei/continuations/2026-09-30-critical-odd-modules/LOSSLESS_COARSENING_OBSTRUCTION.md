# Lossless odd-module decrement coarsening is false

Date: 2026-09-30. Full FEI remains open. This rejects one attempted strengthening of the audited odd-module theorem; it does not affect that theorem.

## Failed implication

For balanced odd g substituted at outer coordinate j, the inequality

    Delta_i H(G(...,g,...))/Inf_i(G(...,g,...))
      <= Delta_j H(G)/Inf_j(G)

is false, even when `Inf_j(G)<=1/2`. Consequently one cannot use this lossless step to repeatedly coarsen a high-decrement core while keeping exactly the same threshold. The proved additive erasure bound in REPORT.md remains valid.

## Exact six-variable Boolean counterexample

Use binary input labels with coordinate 0 the least significant bit. Let G on four bits be -1 at labels

    {0,2,4,6,8,9}

and +1 elsewhere. Its normalized Walsh coefficients multiplied by eight, in integer-label order, are

    [2,-4,-2,0,-2,0,-2,0,-2,-4,2,0,2,0,2,0].

Thus its squared spectrum has two masses 1/4 and eight masses 1/16. Hence H(G)=3 and `Inf_0(G)=1/2`.

The two coordinate-0 children each have one squared Fourier mass 9/16 and seven masses 1/16. Each therefore has entropy

    H_child=4-(9/8)log2 3.

It follows that

    Delta_0 H(G)/Inf_0(G)
       =(9/4)log2 3-2
       =1.5661656266226016... .

Now replace input 0 by ternary majority M on a fresh three-bit block, leaving the other three inputs as disjoint balanced dictators. M is balanced and odd, with H(M)=2 and each coordinate influence and singleton Fourier coefficient equal to 1/2. Call the resulting six-variable function F.

Balanced composition gives H(F)=H(G)+Inf_0(G)H(M)=4 and every physical majority leaf has influence 1/4. At any such leaf, both restriction spectra have one mass 1/4 and twelve masses 1/16, with all other masses zero. Their entropy is 7/2. Therefore

    Delta_i H(F)=1/2,
    Delta_i H(F)/Inf_i(F)=2.

This is strictly larger than the outer ratio. The erasure and Jensen–Shannon terms are both exactly 1/4 after substitution. No non-Boolean function, approximation, or asymptotic limit is used.

## Verification and scope

The displayed Walsh coefficient lists and mass multiplicities were obtained by integer Walsh transforms and then checked analytically as above. The searching script exhausts all outer Boolean functions through dimension four at eight t values; this finite search is not used as the proof of the displayed counterexample. The counterexample has small decrement ratios and is not a C=100 critical core. It rules out the universal lossless contraction lemma, not a statement that assumes extra high-criticality hypotheses.

The broader unresolved implication is still a source-realizable affordable coordinate/block for arbitrary composition-prime critical cores. The exact mismatch/packet accounting has not supplied such a universal selector.
