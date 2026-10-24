# Independent mathematical audit

Date: 2026-09-30. Reviewer worked from the theorem statements and independently reconstructed the proofs, rather than relying on the finite checker. This is an independent analytic review, not proof-assistant certification.

## Odd-module and coarsening results

Verdict: both claims are correct under balanced, disjoint composition, with the designated child odd under simultaneous input negation. No missing cross terms were found.

For every nonempty residual subset in the designated child block, the two paired Fourier coefficients have opposite support parity; one is zero. Both binary erasure and Jensen–Shannon terms vanish. At the empty residual subset, the pair is exactly `(Ghat(T), c Ghat(T+j))` multiplied by the other children’s Fourier factors. Summing those squared factors gives one. This yields both exact packet formulas and `Inf_i(F)=qd`.

The reviewer independently proved `J(a,b)<=(2/ln 2)min(a²,b²)` by writing the natural-log pair entropy in terms of `r=2|ab|/(a²+b²)` and integrating `atanh(r)<=r/sqrt(1-r²)`. This establishes the stronger `JS_i(F)<=(2/ln 2)c²q`, not merely a bound by `qd`.

The reviewer checked homogeneous concavity, `|c|<=d`, and the increasing scalar function used to replace c² by d², confirming the logarithmic critical-core exclusion. The strict bound on q follows with the report's `Delta_i>C Inf_i` convention; the reviewer also noted that the logarithmic upper bound is strictly loose at positive q,d.

The scalar inequality `E(a,t²b)<=tE(a,b)+(t/2)b` was independently checked. At fixed product, homogeneous binary entropy decreases with imbalance. The remaining range follows from `E(x/t,t)<=2sqrt(x)`, `E(x,1)>=2x` for x<=1, and `2sqrt(x)-2x<=1/2`. This confirms the coarsening bound.

Important scope caveat retained: arbitrary physical restrictions need not preserve the balance and oddness hypotheses.

## Activation and joint-smallness results

Separate verdict: all activation identities and asymptotics are correct; no correction is needed.

The reviewer reconstructed the raw spectrum entropy of A as `pr[2+H(g)/2]`, accounted separately for pure-control and h-containing Fourier labels, and checked removal of the empty coefficient p² and insertion of `(1-p)²`.

Pivotal-edge counting gives p times each data or control influence, hence the mean, variance, total-influence and maximum-influence formulas exactly.

The character-centering step preserves entropy and gives `J=sum_i min(Inf_i,1-Inf_i)>0` when H>0. The balanced seed, tensor and self-composition formulas were checked independently. For `r=k²`, all three smallness parameters tend to zero. The ratio limit follows particularly cleanly from

    rH(g_k)+4r=4r(3/2)^k,
    [-phi(p²)+phi((1-p)²)]/p -> 2/ln 2,
    k²(3/2)^k/(kJ+3/2)^k ->0.

Every control coordinate has outer q=p and inner d=2^-k, giving exactly the affordable-coordinate certificate in the report.

The reviewer explicitly confirmed that these controls prevent the constructed sequence from being all-coordinate C-critical for any fixed C>0. The construction is not a full FEI proof and not a criticality-preserving reduction.

## Finite checks

The author executed the final checker, which passed 8,640 odd-module coordinate cases, 1,248 activation cases and 57,491 scalar cases. The independent reviewer did not rerun those bytes. The finite checks are regression evidence, separate from the analytic audit above.
