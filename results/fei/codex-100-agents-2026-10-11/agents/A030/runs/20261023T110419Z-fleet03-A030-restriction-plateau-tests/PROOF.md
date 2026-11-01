# Repeated incoherent-profile resets: one global potential

Author proof; independent external review pending. Uniform physical cubes, normalized Walsh coefficients, bits. Full FEI remains OPEN.

## 1. Universal finite-label bounded potential

For F(y,x)=g_{L(y)}(x), with a finite number ell of Boolean sources and an independent control cube, write C_j=1_{L=j}, c_j=hat C_j and b_j=hat g_j. Sources may share all data. At EVERY actual physical restriction v rebuild the explicitly prescribed reference

 Q_v(U,t)=sum_j c_{j,v}(U)^2 b_{j,v}(t)^2.

Retain all reference mass on zero-true rows. Partition orthogonality normalizes Q_v, and its data marginal equals that of the true squared spectrum P_v. Cauchy gives P_v<=ell Q_v pointwise. Therefore the exact potential

 c_v=D(P_v||Q_v) satisfies 0<=c_v<=log2 ell.                (1)

Every physical restriction preserves this selector representation: controller queries restrict the label map, data queries restrict every source on the same physical bit. Zero-probability labels and constant source children are retained. Thus(1) holds at arbitrary mixed histories, without a restriction-class FEI assumption. This reconstructs A030@4's conversion interface and now uses it as a CURRENT-reference potential, not as a new allowance per reset.

## 2. Actual reset liability, actual refunds, no renewal

At v transport the CURRENT Q_v through the full Boolean function's actual-phase pair channel. If a,b are the real Fourier amplitudes of a queried pair, the outcome kernel is (a+(-1)^s b)^2/[2(a^2+b^2)]; choose1/2 for a=b=0. Normalize each inherited reference child R_s by its OWN branch mass rho_s. Physical outcomes remain fair. Let d_s=D(P_s||R_s). KL disintegration gives

 c_v=E_s d_s+E_v+O_v,                                    (2)

where E_v>=0 is the actual pair-erasure KL refund and O_v=D((1/2,1/2)||rho)>=0 is the reference-outcome normalization refund. These are actual refunds from the CURRENT reference, not fresh source banks.

Replacing each inherited child R_s by the prescribed Q_s has the signed raw reset charge

 kappa_v=E_s(c_s-d_s).

After retaining BOTH refunds, its signed net charge is

 sigma_v=kappa_v-E_v-O_v=E_s c_s-c_v.                      (3)

Neither kappa nor sigma is replaced by a positive part. For EVERY finite adaptive mixed physical stopping tree with actual physical reaches w_v,

 sum_v w_v sigma_v=E_leaf c_leaf-c_root.                   (4)

Equivalently c_root+sum_v w_v sigma_v=E_leaf c_leaf. This equality, (2) and the nonnegative entropy-decrement telescope give the complete cost at EVERY prefix frontier:

 old entropy path + E_leaf CE(P_leaf,Q_leaf)
   =H_root+E_leaf c_leaf <= H_root+log2 ell.                (5)

All terminal H+KL costs are retained. Internal raw reset differences and refunds are the alternative exact expansion(2)--(4); they are not added AGAIN to(5). A supplied ONE original quota U with old debit b and U-b>=H_root+log2 ell funds all repeated prescribed resets at every frontier, without a new child quota. If the initial target Q_root differs from a prior true reference, its genuine initial cost c_root is included by the same bound. Queries can stop at any depth. No claim is made for arbitrary external references replacing Q_v.

## 3. All-history payment on the previous tagged bent obstruction

Use exactly A030@4's root: even r>=4, epsilon=2^-r, t=2^(-r/2), canonical quadratic bent g on r controller bits; one extra controller bit s relabels z=0 from label1 to0 in its child1, otherwise labels1/2 follow g. The three independent private sources are a*PD2, Maj3, b*PD2. Here a,b are real fair DATA tags; all source entropies equal2 and means equal0. The actual root I is

 I_root=r/4+(r+1)epsilon/2+2-pi1/2 >=r/4+27/16.            (6)

The source spectra are disjoint nonempty private sectors at this root, so Q_root=P_root and c_root=0. Keeping the exact label-entropy constant rather than rounding it to2 improves the admission estimate from the previous stage:

 H_root=H(pi)+sum_j pi_j H(c_j^2/pi_j)+2
        <=r+3+log2 3.                                    (7)

This uses the r+1 physical controller coordinates and retains all source costs. Set the SAME original U=4I_root and old unrelated debit b=1/4. Combining(5)--(7) with ell=3 yields at EVERY finite adaptive mixed frontier, rebuilding Q_v after EVERY query,

 U-b-[old entropy path+E full terminal CE]
 >=7/2-2log2 3 >1/4.                                     (8)

The strict rational check is3^8=6561<8192=2^13, hence log2 3<13/8. This pays the next conversion, arbitrary subsequent DATA/controller profile changes, all tag orders/interleavings, and both full children throughout. The previous selected conversion and its debit are included in the raw history, not discarded or renewed. At an intermediate frontier the available amount is U-b-H_root-E c_frontier; future signed sigma changes that amount exactly by the change in E c. Thus refunds can release a previous liability without losing its audit trail.

The previous >765/512 bound was for ONE selected reset followed by NO resets, with its reach1/4 rare-event bound. The new >1/4 guarantee is for ALL repeated resets on ALL branches of EVERY physical tree. The weaker numerical reserve covers this stronger scope, not a correction to the old theorem. The local cut/rarity residual E/Inf_s from A030@3 still diverges; no cut slack is invented to pay it.

## 4. Actual Boolean oscillations: bounded potential, unbounded positive variation

Let v(x,y)=(1,1,1,-1) in binary table order and w(x,y)=v(x xor1,y)=(1,1,-1,1). For k>=1 use one fair selector bit s and shared source data pairs(x_l,y_l):

 g0=product_l v(x_l,y_l), g1=product_l w(x_l,y_l),
 F_k=g_s.

Each two-bit source is flat, so both products have equal-magnitude Fourier coefficients2^-k on all4^k data sets, with potentially different signs. For a single fair selector the two control rows have amplitudes(a+b)/2 and(a-b)/2. If |a|=|b| on their common full support, one control row is zero and the other carries the entire row mass, while Q gives each half. Hence c=1 exactly. At the root H(F_k)=2k and I(F_k)=k+1/2; this is not an FEI counterfamily.

Query x1,y1,x2,y2,...,xk,yk, then s, retaining every outcome. After each x_l query, one source has a remaining y_l character and the other a constant at that pair, irrespective of the actual x_l outcome. Thus their remaining Fourier supports are disjoint and c=0. After y_l, both pair factors become signs, and the remaining products are isospectral: c=1. This holds on EVERY history, not a chosen branch. Consequently the signed net transactions alternate

 -1,+1,-1,+1,...,-1,+1, then -1 at the final selector.

Their total is -1, consistent with c_root=1 and terminal c=0. Their weighted positive-part sum is k, unbounded for fixed ell=2, although c_v is always0 or1 and a ONE-bit conversion envelope suffices for all frontiers. Including the initial target cost1, the signed final calibration cost is0 but positive clipping demands1+k. In particular no constant multiple of log2 ell bounds the positive-part net reset total. Actual phase-channel raw charges and refunds must be retained; this is not a statement that raw kappa equals sigma.

## 5. External source references: a likelihood martingale

The bounded-potential argument also permits genuinely supplied source references, including off-true mass. Supply normalized R_j and finite constants lambda_j with P_j(t)<=lambda_j R_j(t) pointwise. At each DATA query transport each CURRENT R_j through its OWN source's actual-phase channel. If its reference outcome mass is rho_(j,s), the inherited likelihood constant is

 lambda_(j,s)=2 rho_(j,s) lambda_j.

The factor2 is the actual fair physical branch normalizer. Positivity makes all rho positive. Channel domination proves the child likelihood inequality. At CONTROL queries keep R_j and lambda_j unchanged. Thus M_v=sum_j lambda_(j,v) is positive and exactly harmonic under every physical query, including arbitrary adaptive choices. It is an inherited likelihood account, not a renewed maximum-likelihood estimate at the child.

Rebuild the output target Q^R_v(U,t)=sum_j c_j(U)^2 R_j(t). It is normalized by partition Parseval. Weighted Cauchy gives

 P_v(U,t)<=M_v Q^R_v(U,t), and D(P_v||Q^R_v)<=log2 M_v.

Indeed apply Cauchy to c_j sqrt(R_j) and b_j/sqrt(R_j), omitting zero R_j rows whose true b_j also vanish. For EVERY finite adaptive frontier, harmonicity and concavity imply

 E D(P_leaf||Q^R_leaf)<=E log2 M_leaf<=log2 M_root.

The full cost is therefore at most H_root+log2 M_root. Actual CURRENT output-target raw resets and refunds obey precisely(2)--(4), so repeated external-source-profile reconstructions do not add another log M at each descendant. This also changes the output DATA-row marginal when the supplied source references differ from P_j; it is not confined to a true-profile empty/nonempty shape change. No external controller reference or arbitrary freshly chosen terminal target is asserted. The initial source likelihood constants and the full H_root allowance are explicit hypotheses. With R_j=P_j and lambda_j=1 this reduces exactly to(1)--(8).

## 6. Exact open frontier

The universal statement proved is a conditional all-history reference-transfer theorem with a bounded signed profile liability or a supplied likelihood martingale. The explicit rate4 supplier is proved for the tagged bent family, not for every Boolean input. The first unsupported universal line remains an influence-priced initial full source/structural admission U-b>=H_root+log2 ell (or H_root+log2 M_root in the external-source variant). For ell=1 its H_root term already contains arbitrary source FEI. Reducing reference calibration to a bounded potential does not supply that theorem. Next test whether a particular genuinely influence-priced external controller/source target has a pointwise or signed-KL conversion supplier from the SAME diminished original bank; arbitrary target positivity alone is insufficient.
