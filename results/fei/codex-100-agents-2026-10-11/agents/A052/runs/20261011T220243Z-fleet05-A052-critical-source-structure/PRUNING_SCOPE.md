# Exact pruning replay and criticality scope

All component comparisons in the historical records use raw indicator Fourier entropy with natural logarithms, not the entropy of a probability law. Write E(g)=sum |S| ghat(S)^2 and Hraw(g)=sum ghat(S)^2 ln(1/ghat(S)^2), including the empty coefficient. For an indicator of density p its coefficient squares sum to p. For the sign f=1-2g, nonempty squared coefficients multiply by four and the empty coefficient changes to (1-2p)^2; therefore raw Hraw/E and sign H/I cannot be interchanged.

## Nine-bit entropy obstruction: exact replay

Use five data bits y and four controls x. Let A={wt(y)<=1} times the full control cube, and B={(11111,0000)}. These are exactly the two Hamming-connected components, of sizes 96 and 1; their minimum separation is four. Independent direct Walsh and FWHT transforms, plus physical edge enumeration, give E(A)=5/16, E(B)=9/1024 and E(A union B)=329/1024. The helper certifies

    Hraw(A union B)-Hraw(A)-Hraw(B)>1/5000

by rational logarithm enclosures. It also checks R(A union B)<R(B). This is the original Addendum 11.44 obstruction, reproduced from its truth table and not inferred from its navigation status.

Fix three data coordinates to zero. The inherited indicator is {00,01,10} on the remaining two data bits, with irrelevant controls. Its raw ratio is 12 ln2-(9/2)ln3. Our exact certificate verifies that this ratio exceeds R(A union B). Thus the nine-bit source is not all-descendant raw-ratio critical.

## Seven-bit maximum-component-ratio obstruction: exact replay

Use four data bits and three controls, with the analogous star A and opposite singleton B. Component sizes are 40 and 1; minimum separation is three. Energies are 3/8, 7/256, 103/256. The numerator histograms, derived independently from the truth table, give

    Hraw(A)=[40960 ln2-5760 ln3-3200 ln5]/16384,
    Hraw(B)=1792 ln2/16384,
    Hraw(A union B)=[73472 ln2-3240 ln3-5290 ln23-3362 ln41]/16384.

Two exact integer comparisons certify R(A)<R(B)<R(A union B):

    3^45 * 5^25 > 2^128,
    2^23552 > 3^1620 * 23^2645 * 41^1681.

Fix two data bits to zero. The same inherited two-bit indicator has strictly larger ratio than the union. Rational intervals certify this too. This source therefore refutes unrestricted component-ratio pruning while failing the criticality hypothesis. The source report was retrieved read-only at commit 31c201a0a8caef323c65abe964ff8ed4b702fc81, blob 978c180155e1a25d4d8f34988b5216269c7b83c3, and its text is saved in out/COMPONENT_RATIO_SOURCE.md.

## Actual Boolean sign lifts also fail physical ratio criticality

This is an additional check, not a transfer of the raw conclusions. For f=1-2 indicator(A union B), fix the first two data bits to one. The entire star disappears, and B becomes one negative point on n-2 free coordinates. The exact influence pairs (source,child) are (103/64,5/16) at n=7 and (329/256,7/64) at n=9. Independently computed sign entropies and rational logarithm certificates show

    R(child)-R(source)>1/2 bit per unit influence

for both examples. The point-defect child has essential dimension n-2, so this is an actual proper physical descendant. Details and exact interval endpoints are in out/SIGN_REPLAY_OUTPUT.json. Nothing is assumed about raw-to-sign ratio preservation.

## The specified use of criticality

For a Boolean sign source let L_A=H(f)-average H(f_x). The exact identity I(f)=I_A+average I(f_x) implies

    L_A-R(f) I_A = -average [H(f_x)-R(f)I(f_x)].

Only after imposing the all-proper-physical-descendant bound is the right side nonnegative. Our structural theorem uses that sign at this exact line, then applies the separately proved upper bound L_A<=H(VS|S_C)+(2/ln2)b. A dimension-critical K-witness instead gives L_A-KI_A>=D_K(f)>0. None of the component counterexamples satisfies the needed sign/indicator condition; their checked higher-ratio restrictions explain the failure directly.

Criticality changes this comparison of actual children. It supplies no comparison with indicator components, which are generally not physical descendants. We do not claim criticality restores component subadditivity or maximum-component-ratio pruning, nor that it forces connected support. Those stronger targets remain open.

## Arbitrary-core embeddings and descendant inheritance

The standard construction F=1+A_r(g-1), g=z times f^tensor k, has a proper physical restriction to g and then to f^tensor k. Its exact formulas are H(F)=pH(g)+2rp(2-p)+h((1-p)^2), I(F)=p(I(g)+r), where p=2^-r and h(t)=t log2(1/t). For k=m^2 and r=m the ratio tends to R(f), while influence and minority probability tend to zero. If f violates K, then k D_K(f)-K>0 for large m, so g is already a smaller violating physical restriction. Hence this FEI-hardness embedding fails dimension-criticality explicitly. For ratio criticality itself, fixing the balancing bit in g preserves entropy and removes one unit of influence, giving a strict improvement when H(f)>0. Activation may sometimes have larger ratio than that child; no blanket ratio-criticality verdict for every activation is made.

Six fixed activations of the balanced tensor powers of the two-bit point defect are validated exactly in check_structure.py. These verify the formulas and descendants, not a universal activation-criticality classification. The independently reviewed Addendum 11.26 shows that raw-indicator descendant maximality alone allows AND powers with a divergent full-degree logarithmic moment. The present theorem does not pay that moment or supersede that obstruction: its metric is sign entropy and its stronger dimension-critical form excludes the displayed violating-core enlargements.

A child of a critical source need not be critical at its own ratio. No such inheritance is used. The full spectral law is never replaced by an incoherent mixture of physical components, and fiberwise character demodulation in the analytic channel proof is never labelled a Boolean descendant.
