# Spectator influence is not a second entropy liability

Uniform physical cube, Boolean signs, base-two spectral entropy. Put K=4+2/ln(2). Author proof and exact validation, independent review pending; full FEI remains OPEN.

## 1. Exact subtraction for disjoint physical cores

Let b and c be arbitrary Boolean functions on disjoint original physical coordinate sets. For i in b, write p=Inf_i(b), D=(b|i=0-b|i=1)/2, e=I(D), and Delta_i(b)=H(b)-average_s H(b|i=s). Spectra tensor exactly, so

 H(bc)=H(b)+H(c), I(bc)=I(b)+I(c),
 Inf_i(bc)=p, B_i(bc)=B_i(b), Delta_i(bc)=Delta_i(b),
 I(D_i(bc))=e+p I(c).                            (1)

Here I on a real function is its full Fourier energy sum_S |S| fhat(S)^2, and ||D||_2^2=p. The last equality follows by expanding the degree in the tensor spectrum of D*c; c has norm one. It is also the original physical-edge Dirichlet identity. The extra 2p I(c) in the usual boundary charge 2I(D_i(bc)) is a spectator term: it has NO effect on the actual entropy debit, influence or erasure at i. Subtracting it is an equality, not a new source of influence.

In particular the established one-query bound Delta_i(b)<=3p/ln(2)+2e applies inside any such disjoint Boolean context with exactly the same right-hand side. This is an application/refinement of the existing boundary estimate; it does not claim that generic dependent context can be subtracted.

## 2. The same spectator subtraction survives ONE shared data gate

For ANY Boolean h, define A_h(p0,z,x)=1 when p0=0, and (-1)^z h(x) when p0=1. The physical coordinates p0,z are fresh and unqueried, and shared across all the following queries. The z tag separates every h frequency from the vacuum. Direct Fourier expansion gives

 H(A_h)=2+H(h)/2, I(A_h)=1+I(h)/2.

Take h=bc as above and query an ORIGINAL core coordinate i of b. Both full children are A_(b_s c), using the SAME p0,z. Hence

 Inf_i(A_(bc))=p/2, B_i(A_(bc))=B_i(b)/2,
 Delta_i(A_(bc))=Delta_i(b)/2,
 2I(D_i(A_(bc)))=e+p I(c)+3p/2.                  (2)

Indeed D_i(A_(bc))=1_(p0=1)*(-1)^z*D*c. Its norm is p/2. Physical p0 and z derivatives contribute p/4 and p/2 to its influence, while core derivatives contribute (e+p I(c))/2. Multiplication by two gives (2). Thus the spectator-free boundary is e+3p/2 after removing p I(c). Every full child entropy is retained; the guard's original influence ONE is retained once, never recreated at each query or branch.

The formulas apply after every core-only history as long as the actual cores have disjoint physical supports, so the reached state remains a product of conditional Boolean factors inside the SAME gate. No branch normalization, influence bank, gate label or terminal is reset.

## 3. Actual bad-query fixture and an all-width test of the surrogate

Use the saved actual six-bit b from stage17. Exact checks give H(b)=21/4, I(b)=9/4, selected p=1/8 and e=5/16. Its selected erasure is

 B_i(b)=(136 log2(17)+120 log2(5)-704)/256>1/2=4p;

the strict sign is the positive integer comparison 17^136*5^120>2^832. Thus it is genuinely classified bad by the stream's B_i>4Inf_i test. All other coefficients and both full conditional truth tables are retained in the certificate. The exact actual entropy debit is

 delta:=Delta_i(b)=-11/4+(25/32)log2(5)+(9/8)log2(3)<K/8.   (4)

The strict upper bound is independently certified by integers. Its natural-log margin times32 equals104 ln(2)+8-25 ln(5)-36 ln(3). Since exp(8)>sum_(k=0)^16 8^k/k! and that rational sum is strictly larger than5^25*3^36/2^104, the margin is positive. code/scalar_certificate.py checks the final integer cross multiplication. The primary implementation obtains (4) from actual truth-table spectra and rational logarithm intervals; its base spectra are also recomputed by direct character sums.

For an arbitrary positive integer t, form h_t=product_(a=1)^t b(x_a) on t disjoint physical six-bit blocks and G_t=A_(h_t). Query the selected coordinate in each factor exactly once; choose the order by ANY adaptive permutation based on previously revealed selected bits. Do not query other core coordinates or the shared physical p0,z. Every reached selected query remains bad: B_i/Inf_i equals the original fixture ratio, by (1)-(2).

The entropy and influence ledgers are exact for ALL t:

 H(h_t)=21t/4, I(h_t)=9t/4,
 H(G_t)=2+21t/8, I(G_t)=1+9t/8,
 queried influence in h_t=t/8, in G_t=t/16,
 actual entropy debit in h_t=t Delta_i(b), in G_t=t Delta_i(b)/2.

Both full children are kept at every step. Averaged full terminal influence is 17t/8 for h_t, and 1+17t/16 for G_t. Averaged full terminal entropy is t(H(b)-Delta_i(b)) for h_t, and 2+t(H(b)-Delta_i(b))/2 for G_t. Thus every original physical influence is either spent or still present, exactly once.

After k of the selected bits have been exposed, expected total influence of the OTHER factors is

 k*(17/8)+(t-k-1)*(9/4).

Each newly selected factor is fresh and independent of the observed history. Its average postquery influence is I(b)-p=17/8. Adaptive choice of its label does not change this conditional law; taking conditional expectation proves the displayed formula without assuming independence between all past decisions.

The weighted usual boundary charge of the next bad query is consequently

 (9t+1)/16-k/32 for h_t,
 (9t+1)/32-k/64+3/16 for G_t.

Summing k=0,...,t-1 gives

 BILL(h_t)=(35t^2+5t)/64,
 BILL(G_t)=(35t^2+29t)/128.                       (3)

In particular BILL(G_t)/I(G_t)=t(35t+29)/(16(9t+8)), unbounded with t, for EVERY adaptive permutation of this prescribed selected-bit policy. All these charged nodes satisfy the EXACT bad-erasure test, so filtering out good nodes does not remove the overcharge. The full functions themselves have bounded H/I and are not FEI counterexamples. A policy querying other physical coordinates can escape this obstruction; no existential adaptive-tree claim is refuted.

After the exact spectator subtraction in (2), the bill for G_t is instead

 t*(e+3p/2)=t/2,

and for h_t it is 2te=5t/8. Those intrinsic bills scale linearly. They are not taken from a terminal's full FEI budget; they explain which repeatedly charged spectator influence the crude proxy was counting. Actual entropy payment uses the separately certified Delta_i(b), so it retains every full terminal and needs no hypothetical terminal FEI estimate.

In fact EVERY adaptive stopped prefix that queries only these still-unqueried selected factor coordinates has an exact SAME-K payment. If N_T is its number of queried factors on a uniform input, then for h_t its actual debit is delta*E N_T and its spent influence is (1/8)*E N_T. For G_t these are halved. Equation (4) therefore pays the prefix from actual queried original influence, with ALL full terminal entropies and influences retained. Previously spent block influence or the guard's one physical influence is never borrowed. This resolves the stated residual-query payment for this actual tensor-core mechanism, though not for arbitrary cores.

This also suggests a precise, universally valid refinement of the payment predicate. For any physical stopping tree and any kappa>=3/ln(2), charge the generic boundary estimate only at nodes with ACTUAL Delta_v>kappa*p_v. The exact telescope and the established generic estimate give

 H(f)<=kappa*A+E H(full leaves)
       +sum_(Delta_v>kappa*p_v) w_v[2I(D_v)-(kappa-3/ln(2))*p_v].

Each charged bracket is positive by that node's strict bad predicate. This is an elementary reformulation of the established generic estimate, not a claimed universal selection theorem. At kappa=K every node of the tensor-core policy above has ZERO charge under this valid refined predicate, even though the B_v>4p_v filter incurs the quadratic bill (3). The actual coupled B+JS slack must therefore be tested before assigning the full boundary liability.

## 4. Overlapping physical supports need a real correction

The disjoint-support condition cannot be dropped even when the context c is just an unqueried character. On two ORIGINAL coordinates i,x, take b=(-1)^(i*x), c=(-1)^x, f=bc. Their actual truth tables in little-endian order are b=(1,1,1,-1), c=(1,1,-1,-1), f=(1,1,-1,1). For the selected i, p=1/2, e_f=I(D_i f)=1/4, I(c)=1, and Delta_i(f)=2. Treating p I(c) as removable spectator influence would assert

 Delta_i(f)<=3p/ln(2)+2(e_f-p I(c))=3/(2ln(2))-1/2<7/4<2,

which is false. The strict scalar bound uses ln(2)>2/3 from the first positive atanh-series term. In fact I(D_i b*c)=1/4, not I(D_i b)+p I(c)=3/4. This refutes precisely the proposed overlap extension, not (1)-(2), the existing boundary theorem, or FEI.

For a real D and any Boolean c independent of i but possibly sharing OTHER physical coordinates with D, the correct identity is

 I(D*c)-I(D)=sum_j E[1_(c(x)!=c(x^j))*D(x)*D(x^j)].

It follows by subtracting the two squared physical-edge differences: on a c-flip edge (D+D')^2-(D-D')^2=4DD', and on other edges the difference is zero. The summands are signed conditional correlations. They equal p Inf_j(c) only in the disjoint case; they may cancel or be negative under overlap. A universal spectator refund cannot replace them by the unconditional product without proof.

## 5. Precise universal frontier

Stage19 left a rank-two quadratic reference with no eligible tangent and arbitrary full tagged-half core. This stage exposes actual residual-core queries through the SAME shared data gate and identifies the exact collateral term that must be removed before charging the boundary. The subtraction is proved for actual disjoint physical product factors, not general Fourier cancellation patterns. The first unsupported universal line would be removing p I(c) after the remaining core shares original physical coordinates with the queried factor: then D*c is no longer a disjoint tensor, (1) fails, and the cross-derivative liability must be priced from UNUSED original influence with all previous debits and both full children retained. A certified overlap version or a selection rule yielding such a factorization is still required. No universal terminal payment, universal useful selection or full FEI theorem is proved here.
