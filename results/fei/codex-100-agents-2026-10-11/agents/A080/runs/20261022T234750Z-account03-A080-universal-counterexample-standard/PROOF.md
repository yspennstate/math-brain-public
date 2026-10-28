# A uniform activation bound, including seeds that vary with the selector

All cubes are finite and uniform, outputs are signs, and entropy is in bits. A nonconstant seed G has mean m, negative-output probability p=(1-m)/2 in (0,1), entropy h=H(G), and influence J=I(G)>0. Its negative output need not be its minority. On k>=1 fresh bits let A indicate one vertex, let a=2^-k, and put F=1+A(G-1). Define c=2akp, the TOTAL selector influence. Thus I(F)=aJ+c. No bound on p away from zero or one is assumed, and G, its dimension, its orientation and its tensor count may depend on k.

## 1. Uniform, finite-width statement

The new quantitative bound is

    H(F) <= a H(G) + (4+5/k)c.                        (U)

Consequently, for every actual nonconstant seed,

    H(F)/I(F) <= max{H(G)/I(G), 4+5/k}.              (V)

For every real C>=4+5/k it also gives the signed slack transport inequality

    C I(F)-H(F) >= a[C I(G)-H(G)]
                       +(C-4-5/k)c.                 (W)

These are finite inequalities uniform in ALL seed parameters, not fixed-seed asymptotic statements. In particular a bounded-ratio seed family cannot become an unbounded-ratio actual Boolean counterfamily through point activation, even when seed bias and influence vanish arbitrarily fast. All k>=1 are covered, with an absolute selector ceiling9. As k->infinity, the ceiling improves uniformly to4. If H(F)/I(F)>L and L>=4+5/k, then H(G)/I(G)>L: a claimed large ratio must already occur in the complete seed.

This strengthens the preceding stage's fixed-seed bounds. Its additive entropy error32 became useless after normalization when p could approach zero with k. The bias-proportional error below removes that diagonal-limit problem. The constants5/k and32 concern different bounds; no earlier limiting constants4/8/2 are changed.

## 2. Complete spectrum and the bias-proportional error

With data set S and selector set T the coefficients are 1-2ap when both are empty, -2ap when S is empty and T nonempty, and a*Ghat(S) when S is nonempty. Selector-point character signs are immaterial. Direct physical edges give q=Pr[F=-1]=ap and I(F)=aJ+2akp. Both data and selector costs are retained.

Write ell(z)=z log2(1/z), ell(0)=0. The exact full entropy identity is

    H(F)/a = h+8kp(1-ap)-ell((1-2p)^2)
             -8(1-a)p^2 log2(2p)
             +ell((1-2ap)^2)/a.                     (1)

This includes the constant atom and every control-only atom. It follows by summing their squared coefficients, without assuming spectral-coordinate independence.

For 0<=z<=1, ell(z)<=1 and ell(z)<=h2(z). Also

    -(1-z)log2(1-z)<=z/ln2,
    ln2>2/3.

The first logarithmic inequality follows by integrating 1/(1-t)<=1/(1-z) from0 to z; the second follows from the first two positive atanh terms at1/3. They hold at endpoints by continuity.

If p<=1/2, the possibly positive logarithmic correction in (1) is

    -8(1-a)p^2 log2(2p)=4(1-a)p ell(2p)<=4p.

If p>1/2 that term is nonpositive. The constant-atom term is nonnegative and bounded by

    ell((1-2ap)^2)/a
       <= [1-(1-2ap)^2]/(a ln2)
       <= 4p/ln2 <6p.

The discarded term -ell((1-2p)^2) is nonpositive, as is the difference 8kp(1-ap)-8kp. Hence

    H(F)/a <= h+8kp+10p.                             (2)

Multiplying by a proves (U), because (4+5/k)c=8akp+10ap. Convex weighting proves (V) since aJ>0, c>0 and their sum is I(F)>0. Subtracting (U) from C times the exact influence identity proves (W). No limit, domination assumption, unproved FEI estimate or small-bias hypothesis is used.

The finite correction cannot simply be deleted. Activating a dictator with k=2 gives H(F)>4c, although its seed entropy is zero. The exact checker requires this strict failure as a negative control. Thus (U) is not an assertion that an uncorrected finite constant4 works.

## 3. Other normalizations and actual counterfamilies

Let v=Var(F)>0 and rho be the squared Fourier law conditioned on a nonempty set. Exactly

    H(rho)/(I(F)/v)=[H(F)-h2(v)]/I(F)<=H(F)/I(F).    (3)

Thus consistently conditioned normalization cannot create divergence absent in the ordinary ratio. Dividing H(rho) by the unconditioned I(F) changes the target and is not a FEI counterexample.

For the output-gap denominator, use the indicator entropy tensorization inequality I(F)>=2q log2(1/q). This follows by tensorizing functional entropy of the negative-output indicator: a crossing two-point fiber contributes1/2, and the sign influence counts exactly twice this contribution. Since q=ap<=2^-k,

    h2(q)/I(F) <= 1/2 + 1/(2k ln2)
                 < 1/2+3/(4k).

Therefore for k>=2,

    I(F)-h2(q) >= [(2k-3)/(4k)] I(F)>0,
    H(F)/(I(F)-h2(q))
       <= [4k/(2k-3)] max{H(G)/I(G),4+5/k}.          (4)

This is uniform in G. In the campaign's rare sector k>=4 the multiplicative normalization factor is at most16/5, matching the earlier bound at k4 and improving with k. The factor tends to2, not1, uniformly over arbitrary varying seeds. Only the previous special tensor-dominated schedule makes the normalization correction vanish. No uniform output-gap assertion is made here at k1.

For any actual sequence G_j, k_j>=1, if the ordinary activated ratios tend to infinity then the ordinary seed ratios tend to infinity by (V), because 4+5/k_j<=9. The same implication holds if the consistently conditioned ratios tend to infinity, by (3). In the rare sector k_j>=4 it also holds for output-gap divergence, by (4), whose factor is bounded. Conversely, actual unbounded seeds can be tensored before activation using the previous explicit schedule to preserve divergence. This does not supply such seeds.

## 4. Independent reconstruction of the signed-terminal obstruction

Let h on six binary coordinates be negative precisely at {0,1,2,4,8,16,32,6,17,40}, let J(x)=-h(x xor1), and let g be negative at {0,1,2}. A089's two negative full terminals are

    E_b = J(-1, g restricted at original bit0=b, g,g,g,g),
    b in {0,1}.

Each is an actual Boolean function on29 ambient coordinates; adding A089's irrelevant residual coordinate gives its stated30-coordinate representation and changes neither entropy nor influence. The other16 states let the two residual block0 coordinates4,5 be free or fixed to0/1. No peer executable is used.

For a direct reconstruction, compute the outer64 Walsh coefficients A_T. If B is the occupied set of nonconstant blocks and m_i their means, the exact coefficient multiplying the product of their nonempty Fourier coefficients is

    L_B = sum_(T containing B) A_T product_(i in T\B) m_i.

Thus every actual full Fourier atom has squared mass L_B^2 times the product of its selected nonempty core squared coefficients. The checker groups only equal masses, retaining their exact multiplicities. Their total is1 by an exact rational check. Physical pivotal probabilities of the outer truth table independently give I(E)=sum_i q_i I(core_i). The occupied-block masses L_B^2 product_(i in B) Var(core_i) give a second entropy and influence calculation. All coefficients and core edge counts are exact.

The certificate must establish exactly two negative S4=4I-H states, with the source intervals (-56/1000,-55/1000) and (-46/1000,-45/1000). These are finite rate4 failures. They are not unbounded-H/I families and do not refute full FEI.

For completeness, independently reconstruct A089's finite scalar theorem. For weights w>=0 summing to1, work on their positive-weight support, and put P=E(s)_+, N=E(-s)_+ for supplied signed full capacities s. For a required NONNEGATIVE net debit T, feasible nonnegative debits d and zero-mean signed transfers f with s+f-d>=0 exist iff T<=P-N. Every negative s must receive f>=-s, so E(f)_+>=N. If P>0, k=(s)_+/P, d=T k and f=(-s)_+-N k attain that minimum and leave residual (P-N-T)k>=0. If P=0, feasibility forces N=T=0 on the positive-weight support; use d=f=0 and k=1. Every signed old label L transfers as Lk, preserving its mean even at T=0.

This proof derives no capacity from nothing. Allowing negative net debits would invalidate the minimum-transfer claim: s=(-1,1), equal weights, T=0 admits d=s,f=0, so the nonnegative-d hypothesis is essential. Zero-weight states must also be excluded from pointwise requirements. These boundaries are included in the exact rational grid.

This review accepts the scalar allocation and18 actual terminal-spectrum substatements at the source's unchanged statement/hash. It does not independently verify the entire root-to-terminal ancestry booking, the four complete source policies or parked donor reaches. Those source facts are not prerequisites of (U)-(W), and are not promoted to independent full-scope acceptance.

## 5. Explicit rare lifts retain the finite obstruction, not an unbounded ratio

For each certified negative E_b, let R_lower>4 and R_upper be outward rational bounds for H(E_b)/I(E_b). Define one deterministic integer

    k0=ceil((8 R_lower+16)/(R_lower-4))+8,
    t0=ceil(k0^2/I(E_b)).

The checker verifies, without dimension search, that

    R_lower/(1+2/k0)-1/k0^2>4.

The actual finite function formed by t0 disjoint copies of E_b followed by point activation has minority<=2^-k0 and influence<=2^-k0(k0^2+3k0), while its ordinary ratio exceeds4. The checker also verifies k0>=I(E_b), which justifies the stated influence envelope. The lower inequality follows directly from the full-spectrum sum before expansion: every term is nonnegative except -a ell(m^2)>=-a, so H(F)>=a(tH(E_b)-1), with every control influence retained. Its upper ratio is at most max(R_upper,4+5/k0) by the new uniform theorem. The output is specified as a finite Boolean formula, not enumerated on its immense cube.

For a sequence take k_j=k0+j and t_j=ceil(k_j^2/I(E_b)). These actual finite functions have bias and influence tending to zero and ordinary ratio tending exactly to the finite seed ratio: the lower estimate approaches R(E_b) and the new upper estimate approaches max(R(E_b),4)=R(E_b). The finite S4 failure therefore survives arbitrarily rare/small-influence normalization but does not become an FEI disproof. Disjoint spectator multiplication gives the weighted ratio [H(E_b)+H(spectator)]/[I(E_b)+I(spectator)]; tensoring a higher-ratio spectator makes that larger ratio dominate. These endpoints are not universal extremizers, and no new universal constant is inferred from a finite ratio above4.

## 6. The remaining universal bill

The signed-transfer theorem pays only capacities supplied in advance; the activation theorem cannot create an unbounded seed ratio. What remains is either an actual Boolean seed sequence with unbounded ordinary H/I or a dimension-independent bound for arbitrary seed entropy that makes the inherited signed capacity feasible after the next physical query. In particular the A089 subsidy already sent to a negative terminal must remain spent, and both that terminal and its donor's full entropy remain in the ledger. Neither rarity, a changed denominator, nor generic allocation establishes this unpaid premise.
