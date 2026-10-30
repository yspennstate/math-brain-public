# Independent review: A090-ARBITRARY-GATE-SIGNED-REFUND-PARTITION@1

Verdict: HOLDS at the entire original statement and hypotheses, without repair. A081 supplies no substantive change and is an independent reviewer. All information below is in bits. The proof is analytic for every even d>=4 and every finite arbitrary Boolean gate; the finite checks corroborate identities, not the universal quantifiers. This is not an FEI proof or a universal non-flat-core payment.

## 1. Physical signs, normalization and signed partition

Use 0/1 labels for the uniform cube. A two-bit quadratic sign has character coefficients (+,+,+,-)/2. Multiplication on disjoint pairs gives coefficients sigma_R t for the d-bit core, t=2^(-d/2), sigma_R in {-1,1}. Parseval counts 2^d coefficients, and evaluation at zero gives t sum_R sigma_R=1. Therefore N_sigma=(2^d+sigma 2^(d/2))/2 exactly.

The indicator of zero has every character coefficient delta=2^-d. For the physical sign F=b+1[y=0](g-1), expansion gives

    Fhat(R,V)=sigma_R t 1[V=empty]+delta(a_V-1[V=empty]).

Only y=0 exposes a gate query i. Its physical influence is e_i=delta E_i, E_i=Inf_i(g). For E_i>0, the complete derivative/reference laws are

    mu_i(R,V)=delta a_(V+i)^2/E_i,
    r_i(R,V)=Fhat(R,V)^2+delta^2 a_(V+i)^2,

where V excludes i. Summing over all R,V normalizes each to one; this uses the full squared spectrum, not a conditioning on derivative support. The reference can have mass where the derivative has none, and this mass remains in all pushforwards. The likelihood ratio depends only on (V,sigma_R). The conditional law on each positive-derivative cell then agrees, so the KL chain rule proves exact equality between full KL and the signed-partition KL. Reference-only cells contribute zero to KL but are not removed from the reference. The alphabet bound 2^r reflects at most 2^(r-1) residual gate masks and two signs, not a paid complexity bound.

For nonempty V, r_i is independent of R; derivative and reference conditional laws are both uniform. The only possible lost refund upon deleting sigma_R occurs at V=empty. Its reference mass is

    rho_i=1-delta+delta(a_empty^2+a_i^2),

and its derivative mass is a_i^2/E_i. Put c_sigma=(sigma+t(a_empty-1))^2+delta a_i^2. The conditional derivative/reference probabilities on R are delta and delta c_sigma/rho_i. Their normalization follows from sum_R delta c_sigma=rho_i, using sum_R sigma_R=1/t. Thus

    D0_i=sum_sigma N_sigma delta log2(rho_i/c_sigma),
    D_full-D_mask=(a_i^2/E_i)D0_i,
    L_i=e_i(D_full-D_mask)=delta a_i^2 D0_i.

When a_i=0 the derivative cell has zero mass and the loss is zero. No exceptional support renormalization is needed. This derives exactly the source's statement, rather than a weaker product-law special case.

## 2. One aggregate dedicated reserve for every gate

Because |a_empty-1|<=2 and t<=1/4, c_sigma>=(1-2t)^2>=1/4. Parseval gives a_empty^2+a_i^2<=1, hence rho_i<=1. The conditional likelihood ratio is therefore at most four; averaging its logarithm gives D0_i<=2. Nonnegativity is ordinary KL nonnegativity between normalized laws. Consequently

    0<=sum_i L_i<=2delta sum_i a_i^2<=2delta.

The last inequality is first-level Parseval on a single gate. Bounding each row separately and multiplying by r would miss the actual aggregate estimate.

Each core bit initially has influence 1/2. Both endpoints 0 and e_j have b=1, so editing zero to -1 toggles precisely one formerly nonpivotal undirected edge. Its directed uniform measure is 2delta. The gate is negative with probability (1-a_empty)/2, giving

    Inf_(y_j)(F)=1/2+delta(1-a_empty).

Since delta<=1/16, 2delta<=1/8<=Inf_(y_1)(F)/4. This quarter of the one physical influence is dedicated to the combined quotient losses once. The theorem does not establish that it remains available after activation, terminal reference or other history charges. Retaining the sign makes these losses zero while retaining the gate mask and its unpaid complexity.

## 3. A precise capacity distinction using an actual Boolean tree

The proposed implication "CE(P_l,Q_l)<=C I(f_l) for each child, therefore some fixed quarter-core capacity is available from child slack for an additional positive quotient loss" is false for the permitted complete subprobability references. This is an insufficiency of the implication; it is not attributed to A090, A097 or any accepted theorem, and does not refute an existential choice of better references.

Take d=4 and g positive on gate truth-table labels 0,1,2 and negative only on 3. This actual six-bit sign is split on y_1. Its two actual five-bit children have influences 21/16 and 2, checked directly from all physical edges. Any five-bit squared spectrum has H<=log2(32)=5. For each child define its complete subprobability reference before spectral sampling by

    Q_l(S)=P_l(S) 2^(H_l-12 I_l).

Since 12 I_l>=5>=H_l, this has total mass at most one and is positive everywhere the true law is positive; it is a complete reference on the entire subset space with zero probabilities only off true support. Its cross entropy is exactly

    CE(P_l,Q_l)=H_l-(H_l-12 I_l)=12 I_l.

Both unused child surpluses 12 I_l-CE_l are therefore zero, as is their reach-weighted average. These references satisfy the allowed leaf-reference hypotheses of the already accepted A097-COMPATIBLE-LEAF-REFERENCE-TRANSFER@1. No interior reference reset is being asserted or needed for this logical witness.

Nevertheless each gate-row quotient loss is strictly positive. Here a_empty=a_i=1/2, rho=31/32, and c_-=41/32,c_+=25/32. The conditional derivative and reference laws differ on both sign classes, whose multiplicities are N_-=6 and N_+=10, so strict KL nonnegativity applies. For the first row the exact weighted loss is

    L_i=(1/64)log2(31)-(5/256)log2(5)-(3/512)log2(41)>0.

The coefficient identity is rationally checked; its positive sign follows from unequal normalized conditional laws, not a floating-point evaluation. The core influence is 17/32 and A090's dedicated bound still holds. Thus a local size bound cannot be converted into an assertion about unused slack in arbitrary already-certified terminal references. A downstream proof must state a separate available-capacity receipt, prove joint payment, or choose and certify different references. It may also retain the sign and avoid the quotient loss; that still leaves the terminal mask cost.

This distinction is not a new universal candidate. It is a source-compatible negative ledger test. A097's terminal KL correction remains intact and may be used only through its existing explicit conservation identity; the test does not refute it or assert that the quotient loss exceeds that correction.

## 4. Exact validation and unresolved bridge

FROZEN_SPEC was saved before either job. Direct integer character sums independently reconstruct the actual spectra, rather than reusing the source helper. Domain: d in {4,6}; every one- and two-bit gate (4+16 truth tables), and four explicitly named three-bit gates. There are 48 actual functions, no symmetry quotient or dimension extrapolation. The 76 relevant gate rows are normalized as complete laws. Exact rational prime-log coefficient identities verify full/signed KL equality and the gate-mask loss formula; 56 row losses are algebraically nonzero. Rational checks verify pointwise likelihood bounds, aggregate Parseval reserve and physical influences. The child fixture has a separate physical-edge influence calculation. Pilot: 171 assertions; full run: 15,566 assertions, 0.388 seconds, estimated memory 64 MB. No floating-point sign decides an entropy inequality.

The exact first unsupported universal line remains

    sum_i e_i D(mu_i||r_i)>=sum_i e_i log2(1/e_i)-K I(f)

for one finite K and every actual Boolean sign with complete normalized reference laws. It is equivalent to paying L<=KI, hence would yield the existing C018 route. The new theorem pays only specified quotient losses for a quadratic bent point-edit. An arbitrary residual gate remains. A general non-flat core, residual terminal CE and a globally nonoverlapping available influence ledger remain unproved. The next shortest route is a source-complete payment construction that names its complete terminal reference and proves available child slack or an explicit joint debit, not another numerical census.
