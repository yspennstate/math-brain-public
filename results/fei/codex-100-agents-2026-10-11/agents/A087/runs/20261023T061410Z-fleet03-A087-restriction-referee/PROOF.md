# Protected pivot: independent affine audit and explicit non-affine liability

All entropies and KL divergences are in bits. All children are physical Boolean restrictions with fair probabilities, not conditional spectral samples. Full FEI remains OPEN.

## 1. Independent reconstruction of the claimed affine theorem

Source: A061-AFFINE-PHASE-PIVOT-RESET-OLD-CAP@1, PROOF sections 1--5, run 20261023T051706Z. Let F(v,z,y)=(-1)^(v A(z,y))g(y), with A affine, v protected, and Q any normalized reference supporting the actual squared spectrum. At every physical query erase the queried spectral coordinate, then use the actual coherent restriction kernel, extended by 1/2 on every zero-source row. Normalize each resulting reference child by its OWN prediction r_b. Physical outcomes remain fair. The two finite KL chain rules give

    K = E + O + (K_0+K_1)/2,
    E = KL(p||Q)-KL(p_erase||Q_erase) >= 0,
    O = KL((1/2,1/2)||(r_0,r_1)) >= 0.

The fair extension on reference-only rows is essential. Positive source support implies both r_b are positive, including deterministic physical child spectra. None of these equations requires O=0, E=0 or a lifted reference.

For any Boolean b on remaining coordinates define M(b)=sum_j h2(Inf_j(b)). Restricting a physical coordinate i satisfies

    M(b) - mean M(b_child)
      = h2(Inf_i(b))
        + sum_(j!=i) [h2(Inf_j(b))-mean h2(Inf_j(b_child))] >= 0.

This follows by edge partition, Inf_j(b)=mean Inf_j(b_child), then binary entropy concavity. Endpoint influences are allowed. For the affine representation, queries in z leave the core unchanged and queries in y physically restrict it. Thus K+2M(g) has conditional drift E+O+2 Delta M >= O before v, regardless of the order of z/y queries or the loss of reference symmetry.

At v, the children are g and a character times g, with deterministic Fourier indicators on surviving z. Each full child marginal entropy is M(g), and each full child Fourier entropy is H(g). Hence the conditional mean of K_child+2M(g) is exactly K+2M(g)-E_v-O_v. For each child, keeping the reference and continuing costs at most K_child+M(g). Alternatively, ACTUALLY changing to its product marginal reference makes its KL equal TC=M(g)-H(g); continuation from that changed reference costs at most TC+M(g)=2M(g)-H(g). The pre-reset potential drop is K_child+H(g)>=0. A final product conversion-and-stop is included in continuation; another intermediate reset is not.

This proves the source's generic policy class without repair. Stops before v must retain their inherited references; permitting a product stop there is an additional policy class, not a consequence of this proof. All terminal KL values stay actual. Adding the actual expected terminal H to both sides retains the full H+KL; it does not pay H from the reserve.

For the original field selector fixture, the expected initial allocation is M_h because the two branches receive 0 and 2M_h. Previously reconstructed exact field influences give M_h=2l h2(2/q-2/q^2)+l h2(2/q), q=2^l, l>=2. At l=2, M_h<=6<8. At l>=3, M_h<39l/16<3l+2 by h2(1/4)<13/16, equivalently 3^12>2^19. Consequently the SAME already booked expected cap W=3l+2 pays this enlarged class. It is not a per-child cap. With Sbar=6l+2-H(h)/2 and H(h)<=3l, 5Sbar/7-W>=(3l-8)/14>0 for l>=3. For l=2, H(h)=5 and the exact gap is 3/14. Thus Sbar-omega-W>Sbar/28 when the SAME original unrelated consumed omega<=Sbar/4. A nested pending theta is included once by W-theta; already spent debits are not refunded. No union with incomparable pre-v product-stop policies is asserted.

## 2. Arbitrary phase: a source-specific reserve that actually pays

Here affinity is unnecessary. Let F be ANY Boolean function on a finite uniform cube, v any protected coordinate, and Q any normalized source-supporting reference. At each history before v define the two actual counterfactual physical children

    g_0 = F_history restricted to v=0,
    g_1 = F_history restricted to v=1,
    W_v(F_history)=M(g_0)+M(g_1).

These children are functions, not independently exposed random outcomes. No extra fair average belongs in W_v. The original allowance is allocated before the pivot, once.

For a query i!=v, physical restrictions commute. Applying marginal-entropy concavity separately to g_0 and g_1 gives W_v(parent)>=mean_i W_v(child). Combining with the ACTUAL KL chain rule shows K+W_v has drift at least O. At the protected pivot,

    mean_b [K_b+2M(g_b)] = K-E_v-O_v+W_v(parent).

Each child independently keeps its inherited reference or makes one immediate actual product reset. Exactly the reconstruction above shows that K_b+2M(g_b) pays either option followed by arbitrary adaptive physical continuation with inherited stops or one final product-conversion-and-stop. The continuation potential is K_current+M_full(current), and all actual reference changes are included. Therefore every bounded admitted policy satisfies

    E K_terminal + E sum O <= K_entry + W_v(F_entry),
    E[H_terminal+K_terminal] + E sum O
       <= K_entry + W_v(F_entry) + E H_terminal.

The finite supermartingale proof covers branch-dependent query orders and modes. An inherited-reference stop before the pivot is dominated by K+W_v. No pre-v reset or second intermediate reset is admitted. This is a reference-payment theorem, not an entropy-influence theorem.

For an arbitrary phase representation F(v,y)=g(y) h(y)^v, h Boolean (additional mask coordinates can be included in y), the exact additional signed liability relative to the affine bank is

    W_v - 2M(g) = M(hg)-M(g).

If only nonnegative top-ups are allowed, [M(hg)-M(g)]_+ suffices. Negative differences are retained algebraically and do not authorize refunds of consumed owner debits. Moreover

    M(hg) <= M(g)+M(h),
    W_v <= 2M(g)+M(h).

Proof: for each j, the derivative sign of hg is the product of the derivative signs of h and g, on the SAME uniform input. Entropy of their product is at most their joint entropy, at most the sum of their entropies. No independence is assumed. Summing proves the inequality. Affine h is a character up to sign, so M(h)=0 and M(hg)=M(g), recovering A061 exactly.

## 3. Boundary controls and the first unsupported universal payment

Non-lifted positive-outcome-cost guard: take g=1 on y0,y1, A=u+y0 and Q(s)=(s+1)/136 on all 16 spectral atoms, bit order u,v,y0,y1. After either physical u outcome, the subsequent v prediction is (15/34,19/34). Thus O_v=-(1/2)log2(285/289)>0. Direct characters and normalized reference transport reproduce this. Setting O_v=0 would invalidate the enlarged affine scope.

Actual non-affine failure of the OLD zero core bank: F(v,y)=(-1)^(v y0 y1 y2), g=1, Q=p_F. Initially K=2M(g)=0. After v both inherited KL values remain zero. The nonconstant child is the three-bit point sign, with TC=2-(9/8)log2(3). Resetting and stopping costs in fair expectation 1-(9/16)log2(3)>0; the strict sign follows independently from 2^16>3^9. The new W_v includes M of this child and pays the cost. This is not an FEI counterexample.

For any source the concavity identity also gives

    W_v <= 2 [M(F)-h2(Inf_v(F))].

This does NOT make the reserve influence scale. For the n-bit point sign, n>=3, every coordinate has d=2^(1-n). For ANY pivot, one child is constant and the other is the (n-1)-bit point sign, so W_v=(n-1)h2(2d). Since h2(2d)>=2d(n-2),

    W_v / I(F) >= 2(n-1)(n-2)/n -> infinity.

Thus even optimizing the pivot cannot yield a dimension-free bound for this raw sufficient reserve. The first unsupported universal line is a bound for the MINIMAL signed reference-payment reserve (retaining inherited K/E credits), or a different owner-based phase payment, from unused original influence-scale slack. Neither the sufficient W_v nor its upper bound supplies that line. The new theorem identifies and pays an exact source-dependent non-affine liability; it does not close the universal bridge.

There is a stronger guard against making the missing reference eligibility implicit. Even the MINIMAL reset payment cannot be bounded by C I for EVERY inherited reference. Take the same n-bit point source and Q=p_F, so K_entry=0 and the actual pivot children still have inherited KL zero. Set m=n-1 and a=2^(1-m)=2d. The nonconstant child's nonzero-frequency spectral mass is epsilon=2a-a^2, spread uniformly across 2^m-1 atoms. Thus

    H(point_m)=h2(epsilon)+epsilon log2(2^m-1).

For m>=2, a<=epsilon<=2a, log2(1/epsilon)<=m-1, and -(1-epsilon)log2(1-epsilon)<=epsilon log2(e)<2epsilon. Consequently H(point_m)<=2a(2m+1), whereas M(point_m)>=m a(m-1). The admitted policy that queries v and immediately resets both children to products therefore has actual expected terminal KL at least

    (a/2)(m^2-5m-2).

Dividing by I(point_n)=n d=n a/2 yields the lower bound n-7+4/n, which diverges. There is no outcome KL in this Q=p experiment. This disproves the unregistered extension 'for every F,Q, one intermediate product reset is payable by K_entry+C I(F)' for a dimension-free C. It is an actual Boolean family of reference-payment obstructions, NOT a Boolean FEI counterexample. If a post-reset physical query is required, append an unused dummy bit and query it after the reset: its actual influence, outcome KL and erasure credit are zero, and both full terminal laws are unchanged. The original field theorem and any fixed-root-reference eligibility condition remain untouched. An influence-scale minimal-reserve theorem MUST retain a substantive reference/owner eligibility hypothesis.

## 4. Exact verification scope

code/pivot.py enumerates all 128 three-bit truth tables with F[0]=1, for three references each: uniform, (1,...,8)/36, and p_F. Global output sign leaves squared spectra, physical coherent kernels and influences unchanged, so these are all 256 sources modulo an exact symmetry. For each fixture the recursion enumerates all ordinary query orders and fair outcomes before protected v, including adaptive stopping. It optimizes each child policy BEFORE averaging, and maximizes retention versus actual product reset separately in each pivot child. The post-pivot recursion includes all remaining physical queries and terminal product conversions. Every candidate policy retains full terminal H alongside its K+sum O value. Direct character sums and direct edge counts cross-check each spectrum and influence; exact prime-log algebra checks the KL chain rule, with rational interval signs only where required. No source author's helper is imported.

The all-dimensional proof above, rather than finite enumeration, establishes the quantifiers. The enumeration tests normalization, fair probabilities, averaging order, product support, endpoint influences and all source-zero/reference-only rows. It does not certify any unimplemented larger policy union.
