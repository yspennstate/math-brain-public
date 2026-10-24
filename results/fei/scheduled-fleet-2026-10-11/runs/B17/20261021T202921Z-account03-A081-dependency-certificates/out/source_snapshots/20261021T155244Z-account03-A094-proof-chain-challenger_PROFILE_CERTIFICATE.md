# Same-rate weak-history payment with no padding requirement

Let h_L=1-2·1_zero on L uniform bits and g=h₃h₂ on five disjoint bits. Pad by any m≥0 dummy bits, n=m+5, δ=2^-n. Select g and the flip of its all-zero full point by a fresh fair selector. Use exactly A095's support-completed reference with source R=P_g. Retain this incoming reference under either (i) the first width-three core query, or (ii) that query followed by a second width-three core query only on the zero first branch. Padding and selector are never queried. All quantities below are ideal bits and physical influences.

**Claim (author proof, independent review pending).** For every m≥0, the entire incoming root cross entropy is at most 301/64, whereas the average remaining physical influence after either history is at least 19/16. Consequently

4 E I_leaf-E CE_leaf≥3/64,

with the same normalized incoming reference, both complete terminal costs retained, no reference reset, and no bank renewal. In fact the original root cost itself fits inside 4 E I_leaf; no lower bound on the nonnegative history release Γ is required. An arbitrary independent prescribed terminal retains its full additive CE and divergence outside this core account.

## Signed profile, rather than the granularity envelope

At the edited point g(0)=1 and all Walsh point phases equal one. Its 32 coefficients consist of one +3/8, three -3/8, seven -1/8 and twenty-one +1/8. Thus the four high-magnitude atoms have squared mass 9/64 each and the others 1/64. Set L=log₂3. The source cost is c=6-(9/8)L. With ℓ_T=log₂(1/P_g(T)), direct summation gives

Σ a_T ℓ_T=6+(3/2)L,

Σ ℓ_T=192-8L.

The old-sector cost of the actual edited root is therefore exactly

c-δ(12+3L)+δ²(192-8L).

The full reference adds -(1-w)log₂(1-w)+2nw, where w=2δ-32δ². For n≥5, 0<w<1; there is no zero denominator or absent sector. The scalar inequality -(1-w)ln(1-w)≤w holds for 0≤w<1 by integration or log concavity. The atanh series gives ln2>2/3, so log₂e<3/2. Also log₂3>3/2 because 3²>2³. Hence c<69/16, the vacuum term is at most 3δ, and the quadratic term is at most 192δ²≤6δ because δ≤1/32. The complete cost satisfies

CE_root≤c+δ(4n-15/2).

For n=m+5 the remaining correction is (8m+25)/2^(m+6). It is at most 25/64 for every integer m≥0: the integer inequality 8m+25≤25·2^m holds at m=0, and its induction step follows from 8≤8m+25. Thus CE_root<69/16+25/64=301/64.

## Physical account and all terminals

All five original incident edges at the edit point are pivotal. Original I(g)=7/4. In history (i), Π_g=1/4, t_a=j_a=1 and j_rem=4, giving

E I_leaf=3/2+δ(m-3)≥45/32>19/16.

For m=0 the correction is -3/32; for m=1,2 it is respectively -2/64 and -1/128, and for m≥3 it is nonnegative. In history (ii), Π_g=1/2, t_a=j_a=2, j_rem=3, giving

E I_leaf=5/4+δ(m-2)≥19/16.

The minimum is m=0; m=1 gives -1/64 and m≥2 gives a nonnegative correction. These boundary cases are explicitly separated instead of extrapolating a large-m estimate. Both first children and every final core are nonconstant since the independent width-two factor remains. The old full-vertex edit is still present only on its unique path; its erased original edges remain debited.

Inherited reference transport has Γ≥0, so E CE_leaf≤CE_root. Combining with 4·19/16=304/64 leaves at least 3/64 of original surplus. Tensoring any independent terminal with product-compatible zero-fiber posteriors gives E CE_total=c_q+E CE_core and E I_total=I(q)+E I_core, with D_q retained as well. No part of c_q pays the core calculation.

## Scope and remaining universal line

This removes padding and the K>K₀ rate increase for the named two histories of this unequal-amplitude fixture. It does not remove them from the arbitrary-core theorem. The source reference is P_g for this explicit fixed five-bit core; an arbitrary core spectrum is not assumed to have a known influence price. The useful lesson for the universal bridge is quantitative: the exact signed old-sector term has a negative linear contribution, which the absolute-value granularity envelope discards. A universal proof still needs an influence-controlled signed profile or a selected history paying its positive part from one unused original bank, with complete inherited terminals.
