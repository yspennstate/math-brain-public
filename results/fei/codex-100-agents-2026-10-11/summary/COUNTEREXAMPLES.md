# FEI campaign counterexamples and mandatory scope tests

**Full FEI remains OPEN.** These examples refute specified intermediate assertions, or show that a proposed restriction retains full FEI. None is a counterexample to full FEI. Use the F01–F20 roster in `TEAMS.json`. Source aliases and log conventions are defined in `CLAIMS.md`; explicit natural-log exceptions are noted below.

Every proposing team must record which tests apply, why an excluded test fails its hypotheses, and whether its new conclusion is an identity, a proper-class result, a conditional reduction, or a universal claim. Historical finite checks are source-reported unless the new run actually replays them.

## X001 — Parity lift hides all entropy from local erasure

**Owners:** F05–F07,F15,F17. **Related:** C015,C027. **Source:** ES §3.

For any Boolean g on n sign coordinates, let f(x,z)=g(x₁z,…,x_nz). A Fourier set S becomes S if |S| is even and S∪{z} otherwise. Therefore H(f)=H(g), every occupied set has even size, B(f)=0, and I(f)=I(g)+P(|S_g| odd)≤2I(g). Restricting the physical input z=+1 recovers arbitrary g.

**Defeats:** treating B=0, absence of spectral edges, or even spectral support as a certified easy leaf. The class is not closed under physical restriction. A universal bound for its entropy is full-FEI strength up to a factor two. A bound for aggregate erasure on *all restrictions* is not refuted.

## X002 — One physical selector creates unbounded erasure synergy

**Owners:** F05–F07,F17. **Related:** C027. **Source:** ES §§1–2.

For odd m≥3 put b(t)=(-1)^(t₁t₂+…+t_(m−2)t_(m−1)) on m−1 binary bits. Set g₀(y)=b(y₁+y_m,…,y_(m−1)+y_m), g₁(y)=(-1)^y_m g₀(y), with addition mod 2. Their squared spectra are uniform on even and odd subsets respectively: H(g_j)=m−1, B(g_j)=0, I(g_j)=m/2.

The actual Boolean splice F(0,y)=g₀(y), F(1,y)=g₁(y) has uniform spectrum on m+1 bits: H(F)=B(F)=m+1 and I(F)=(m+1)/2. Its selector influence is 1/2. The mixture of child spectra has B=m although its selector-label mutual information is only one bit.

**Defeats:** B(mixture)≤average B+C·Inf_selector for fixed C. Also defeats restriction stability of P_λ=B+λ(H−B) for every fixed 0≤λ<1: it would require C≥2[(1−λ)m+1+λ]. Does not refute nonlinear potentials or the true entropy restriction identity.

## X003 — Sparse activation leaves a necessary local logarithm

**Owners:** F03,F05,F15,F17. **Related:** C028. **Source:** LA §4.

Take even k≥4, δ=2^−k, r=2k, p=2^−r, b(x)=(-1)^(x₁x₂+…+x_(k−1)x_k), b'=b−2·1_{x=0}, and A(z)=1_{z=0} on r fresh bits. Boolean children G=1+A(b−1), H=1+A(b'−1) are spliced at a physical selector y.

The exact minority influence is j_y=pδ. Both child influences are at most 5k·2^−2k→0, while B_y/j_y≥(1−δ)(k−2)→∞. In this family log₂(1+κ_min/(2j_y))=k+o(1), where κ(u)=1−max_S uhat(S)².

**Defeats:** B_y≤j_y[C+K·min(I(G),I(H))], and the same with max or sum, for any fixed C,K. More generally any multiplier bounded near zero child influences fails. Does not refute global non-reusing amortization that retains the logarithm or the exact mismatch/KL rebate.

## X004 — Overlapping leaf supports invalidate the mixture identities

**Owners:** F11,F14,F16,F19. **Related:** C029. **Source:** direct two-bit substitution in P, `prop:selector-identities`.

Use cells a_±(z)=(1±z)/2 and balanced leaves g_+=y, g_−=−y. They share the same nonempty Fourier support {y}. The actual selector is F(z,y)=zy, so H(F)=0 and I(F)=2. If one wrongly applies the disjoint-support formula, p_±=1/2, q_± are uniform on the two control subsets, d_±=1/2, and it predicts H=2 and I=3/2.

**Defeats:** the *identities* C010 after removing spectral-support disjointness. Physical selector cells remain disjoint; leaf-variable overlap alone is not the issue. Correct Fourier coefficients must retain cross terms and their signs. This is not a counterexample to an unspecified upper bound with an explicit interference penalty.

## X005 — Arbitrary signed leaves encode full FEI

**Owners:** F11,F14,F15,F20. **Related:** C014. **Kind:** exact scope reduction, not a numerical counterexample.

For singleton address cells A_u={z=u}, choosing constant leaves s_u=g(u) represents any Boolean table: F(z)=sum_u1_{A_u}(z)s_u=g(z). Each leaf has zero entropy and zero influence; cheap individual leaves do not control interference in the resulting address function.

Even if leaves must be balanced, take g_u(y)=g(u)y. Then F(z,y)=g(z)y, H(F)=H(g), I(F)=I(g)+1. All leaves have the same Fourier support. Apply this to the t-fold disjoint tensor power of g and divide by t: a uniform C on this selector class implies H(g)≤CI(g), with the same constant.

For a proposed *strong* bound H(F)≤C(I(F)−1), no limiting argument is needed: I(F)−1=I(g) exactly. See also [REPORT.md](REPORT.md), “Shared leaves can hide the full problem”; this is distinct from the two-cell arbitrary-selector reduction C012.

**Defeats:** declaring “affine/singleton cells and arbitrary signed leaves” an easier general FEI class, or extending the distinct-character/orthogonal-leaf theorem without paying its lost hypothesis. Source: elementary coefficient identity in the setup of P, `sec:selectors`; preserve the explicit distinction between this reduction and C010.

## X006 — Real coherent amplitudes are not Boolean restrictions

**Owners:** F09,F11,F14,F16. **Related:** C033. **Source:** ER §6; Shalev §1.1, https://arxiv.org/html/1806.03646v2 .

The real unit-norm function ψ_n(x)=n^−1/2 sum_i x_i has n Fourier atoms of mass 1/n, H=log₂n and I=1. For growing n it is not Boolean. It cannot be admitted merely because it is a normalized signed superposition of Boolean characters.

**Defeats:** universal entropy/influence bounds that use only normalization and allow arbitrary coherent mixtures. For a true Boolean physical splice the coefficients are (ghat±hhat)/2 on two selector-frequency sectors; neither sector may be independently substituted for a Boolean function. Full signed XOR identities must be checked, not assumed after normalization.

## X007 — Shared-variable product entropy is not subadditive

**Owners:** F14,F17,F19. **Related:** C030. **Sources:** OP; RM §9.2; corrected primary package linked from OP.

The recovered seven-variable Boolean pair has H(fg)−H(f)−H(g)>0.1630852002095 bits, with a one-point-defect multiplier. The corrected outward interval is [0.16308520020956166,0.16308520020956171]; use the corrected package, not the historical nearest-rounded exports.

The explicit rare-clause family also has product-entropy excess 4p²log₂(1/p)+(6/ln2−24)p²+O(p³log(1/p)), while I(f)+I(g)−I(fg)=2p². Thus no fixed multiple of this common-pivotal-overlap deficit repairs subadditivity universally.

**Defeats:** uncharged coherent product composition and fixed linear overlap corrections. Disjoint tensor additivity and averages over physical translations remain valid. The seven-variable table and integer histograms must be loaded from the pinned source before replay; this ledger does not replace that certificate.

## X008 — Two spectral addresses already need more than constant two

**Owners:** F12,F16,F17. **Related:** C016,C022,C031. **Source:** RM §9.4 and [sources/ONE_BIT_ENDPOINT.md](sources/ONE_BIT_ENDPOINT.md), with original proof and endpoint verification pinned at commit `2591d8acb920ca59230530761efa3113bea2167a`.

The genuine six-variable Boolean witness has two spectral address bits with masses (5/8,1/8,1/8,1/8), and all four conditional retained spectra are product. Its full spectrum has eight atoms of mass 1/16 and thirty-two of mass 1/64; H=5 and influence vector (1/4,1/4,1/2,1/2,1/2,1/8), giving I=17/8 and H/I=40/17>2.

**Defeats:** extending the solved one-address constant two unchanged. It does not refute a larger finite C₂ or a collective address-entropy payment. Hypothesis checks require the actual signed witness, not just a distribution with this histogram.

## X009 — Tiny dependence does not pay rare local erasure

**Owners:** F07,F09,F12,F17. **Related:** C032. **Source:** RIG §§2–3.

Let b be quadratic bent on even m bits, δ=2^−m, and splice b with b−2·1_{y=0} using a physical bit t. Then Inf_t=δ. The spectral law P satisfies χ²(P∥P_t⊗P_y)=4δ²/(1+4δ²), yet B_t/δ=log₂(1/δ)+1/ln2+O(δ)→∞. Other coordinates retain large influence.

**Defeats:** a universal coordinatewise erasure/influence estimate justified only by closeness to a product law. Does not refute aggregate FEI or a source-sensitive integrated bound. Exact product rigidity is not a uniform approximate-product theorem.

## X010 — Paid noise correlation is not paid source restoration

**Owners:** F08,F09,F18,F19. **Related:** C023,C024,C032. **Source:** RM §§11.15,11.19–11.20, including `POINT_FLIP_SURPLUS.md` and `ADDRESS_HISTORY_GUARD.md`.

Actual late no-click histories of a four-bit one-point defect have TC→0, yet the cited inverse-product truncations round to the wrong constant, with squared source error 1/4; the late branch probability is at least 49/64. The unweighted reconstruction-error time integral diverges.

The separate actual-address-history family has a degree-one ancestor with H=a ln2, J=1, TC≤1. At s=a^−1/(β+1), it defeats every fixed-coefficient pointwise payment by (1+t)J, sk, and s^−β[sqrt(J·TC)+TC], for each fixed finite β≥0. These assertions use natural-log entropy and the source's precise policy and grid definitions.

**Defeats:** the stated pointwise restoration shortcuts, including on genuine histories. Does not defeat C023, an integrated original-source influence payment, or an additionally proved high-ratio-critical hypothesis. In particular one-hot lifetime Θ(log n) is compatible with C023 because DTC₀=log n.

## X011 — Rarity and small influence preserve the optimal full constant

**Owners:** F03,F15,F17,F20. **Related:** C013. **Kind:** exact scope reduction. **Source:** P, `prop:activation`, `cor:activation-equivalence`.

For arbitrary nonconstant Boolean f, set g_t=z∏_(j=1)^t f(x^(j)), r_t=ceil(2log₂(t+1)), p_t=2^−r_t, and F_t=1+A_(r_t)(g_t−1). Then I(F_t)→0, P(F_t=−1)→0, and H(F_t)/I(F_t)→H(f)/I(f). The exact formulas are C013.

**Defeats:** claiming that arbitrarily sparse balanced-core activation has a smaller optimal universal FEI constant. A structural restriction on the core may still help; rarity alone does not. Credit the earlier low-influence reductions of Wan–Wright–Wu and Shalev, not just this exact calculation.

## X012 — Addressing calibrates joint label costs

**Owners:** F01–F03,F11,F17,F18. **Related:** C008,C009. **Kind:** exact benchmark, not a counterexample to FEI. **Source:** P, addressing benchmark and `cor:affine-selectors`.

With a control bits and N=2^a data bits, each nonzero Fourier set is T∪{y_u}, and under the spectral law |S|=1+Bin(a,1/2). Thus H=2a and I=1+a/2. The gate label u is paid once per whole set; every set can use one gate, one root, and zero allocation-congestion loss in the recovered queue witness.

**Defeats:** calling an extra |S|log₂N coordinatewise label charge necessary. Such a charge has expected size a(1+a/2), producing a spurious growing factor. A successful addressing calibration does not prove the witness-cost bound for arbitrary Boolean selectors.

## X013 — Orthogonal coherent vectors can exceed mixture entropy

**Owners:** F11,F14,F19. **Related:** C034. **Kind:** real-vector obstruction, not a Boolean counterexample. **Source:** direct exact construction checked with the joint-coding team; compare the interference obligation in [REPORT.md](REPORT.md).

In dimension 65 let v_+=(1/√2,1/√128,…,1/√128) and v_−=(−1/√2,1/√128,…,1/√128), with 64 equal tail entries. Both have norm one and their inner product is zero. Each squared-amplitude law has entropy 4 bits. Yet w=(v_++v_−)/√2 is uniform in squared magnitude on the 64 tail coordinates and has entropy 6 bits. Label entropy plus average component entropy is only 1+(4+4)/2=5 bits.

**Defeats:** an unqualified coherent-superposition entropy upper bound, even when component vectors are orthogonal. No claim is made that these vectors are realizable as the proposed Boolean pivotal pieces. A candidate Boolean/affine-selector inequality remains OPEN until a witness satisfying that extra structure is exhibited or a proof is accepted.

## Additional guards before universal acceptance

Read RM §3 for dyadic non-Boolean sources that satisfy every preselected fixed cancellation order and have near-Boolean norm data but divergent target ratios. Read [sources/ADDENDUM_11_26_CRITICAL_RARE_MOMENT.md](sources/ADDENDUM_11_26_CRITICAL_RARE_MOMENT.md) before charging full-degree rare-row logarithmic moments, even under the stated criticality. Read [sources/ADDENDUM_11_44_COMPONENT_ENTROPY_COUNTEREXAMPLE.md](sources/ADDENDUM_11_44_COMPONENT_ENTROPY_COUNTEREXAMPLE.md) before using entropy subadditivity across physical connected components; that counterexample does not refute a maximum-component *ratio* statement.

Searches and certificates must retain exact Boolean output, physical influence, all asserted structural hypotheses, and log conventions. A finite violation of an intermediate inequality is not an unbounded Boolean H/I family. Replaying a witness proves neither search optimality nor the universal conjecture.
