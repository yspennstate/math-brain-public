# Exact tensorization and a faithful signed-bank counterexample standard

All functions are actual finite Boolean maps on uniform independent physical bits. Entropy H uses log base 2; I is total physical influence. K >= 0 is common to every factor. Write d_K=H-KI, b_K=max(0,d_K). R_K is the maximum expected b_K over finite adaptive stopping policies on the complete physical restriction DAG, equivalently the least nonnegative superharmonic majorant of b_K. Constants have H=I=R_K=0. All maxima exist because every query reduces dimension.

## 1. Hull bounds

Physical-query entropy is superharmonic. Pair Fourier coefficients a_L,b_L differing in the queried coordinate and put s_L=a_L^2+b_L^2. Shannon's chain rule gives H(parent)=H(s)+B, where B is the nonnegative conditional entropy of the erased membership bit given L. The child spectral laws are (a_L+b_L)^2 and (a_L-b_L)^2, each a probability law by Boolean Parseval, whose average is s. Concavity gives their Jensen-Shannon divergence J=H(s)-mean H(children)>=0. Therefore H(parent)-mean H(children)=B+J>=0. Thus H is a nonnegative superharmonic majorant of b_K for K>=0. Consequently 0 <= R_K <= H and R_K >= H-KI. Therefore D_K=H-R_K satisfies 0 <= D_K <= KI. For I>0, 0<=H/I-R_K/I<=K: at any fixed finite K, unbounded R_K/I is equivalent to unbounded ordinary H/I.

The entropy inequality is the usual unconditional physical-restriction entropy inequality, not an assumption about a coherent correction. It can alternatively be obtained from the previously recorded nonnegative erasure B+J identity in A074's independent proof of A072. No universal FEI estimate is used here.

## 2. Exact tensorization, including the lower bound

For disjoint factors f_1,...,f_m, Fourier probabilities form a product, so H and I add, also after every restriction. The sum U=sum_i R_K(f_i restricted) is nonnegative and superharmonic under every physical query, even when queries interleave adaptively. Since sum_i (d_i)_+ >= (sum_i d_i)_+, U majorizes the product obstacle. Minimality gives R_K(product_i f_i) <= sum_i R_K(f_i).

For the converse, take an optimal finite stopping policy for each factor. At every terminal state with d_i<0, its stopping payoff is zero; continue that state by revealing all its remaining bits. Every resulting terminal constant has d_i=0 and payoff zero. This replacement preserves the policy's expected payoff and makes every terminal d_i nonnegative. Run the modified factor policies successively on their disjoint bit blocks. Their marginal laws are unchanged. At the final product state, all terminal d_i>=0, hence (sum_i d_i)_+=sum_i (d_i)_+. Its expected payoff is sum_i R_K(f_i). This is an admissible physical stopping policy, proving equality:

    R_K(product_i f_i) = sum_i R_K(f_i), for all finite disjoint Boolean factors and K>=0.

The zero-credit completion is essential. The proof does not assume that an arbitrary optimal stopping policy has nonnegative signed deficit at its zero-payoff leaves. Dummy coordinates and constant factors are allowed. Literal parity factors have H=R_K=0, so parity padding leaves R_K unchanged.

## 3. Rate stability

If 0<=K<=L, each terminal payoff obeys 0<=b_K-b_L <= (L-K)I_terminal. Influence is superharmonic: a query removes its own nonnegative influence, while the other influences average exactly. For every policy E I_terminal <= I_root. Maximizing payoffs gives

    0 <= R_K(f)-R_L(f) <= (L-K)I(f).

For a fixed policy, its expected payoff is convex piecewise affine in K; the finite maximum over policies remains convex piecewise affine. Also R_0=H.

## 4. A bank whose normalized divergence is faithful

Provenance: the sandwich below was derived independently in this run and
overlaps A089-SHARPENED-SIGNED-COMPOSITION-RESERVE@1 (earlier immutable run
20261023T130925Z). SOURCE_REVIEW.md accepts that unchanged bank-price
substatement. No novelty is claimed for the sandwich; tensor lower bounds
and actual whole-or-core extraction are the distinct additions here.

For an actual disjoint-core composition F=B(g_1,...,g_m), let q_i be the outer pivotal probability under the actual independent output biases of the other cores. Then I(F)=sum_i q_i I(g_i), including constants and dummy cores. Define the signed correction C=H(F)-sum_i q_i H(g_i), and

    A_{K,kappa}=C+kappa I(F)+sum_i q_i R_K(g_i).

Substitute D_i=H(g_i)-R_K(g_i) to obtain the exact identity

    A_{K,kappa}=H(F)+kappa I(F)-sum_i q_i D_i.

The hull bounds prove the universal sharp-width sandwich

    H(F)+(kappa-K)I(F) <= A_{K,kappa} <= H(F)+kappa I(F).

In particular, for ANY two actual disjoint-core representations P,Q of the SAME function, at the same K,kappa, |A(P)-A(Q)|<=K I(F). Changing the representation cannot turn a bounded A/I sequence into an unbounded one at bounded K. If kappa>K, the lower bound and H>=0 also give A(Q)<=kappa/(kappa-K) A(P) (and symmetrically), including the constant-function zero case. This is a one-state comparison. It does NOT permit charging K I anew at every change of decomposition in a history: an original owner spent earlier still cannot be reused.

For nonconstant F this implies A/I-kappa <= H/I <= A/I-kappa+K. For fixed kappa, any sequence of ACTUAL Boolean compositions with A/I tending to infinity is an actual FEI counterexample, even if K varies. Conversely, H/I tending to infinity forces A/I to infinity whenever K stays bounded. If kappa varies, subtract kappa I before claiming divergence; an increasing added capital is not a counterexample. Z=A-kappa I satisfies H-KI<=Z<=H, so Z_+/I is also a faithful unbounded-ratio witness for bounded K. This algebra does not assert that Z or Z_+ is coherent. A072's separately reviewed coherence theorem applies to A with kappa>=4/ln(2), for example kappa=6; it does not pay for A's initial value.

Products of entire disjoint outer representations have additive C and A, because every outer pivotal probability for a given block is unchanged by multiplication by other Boolean output factors. Thus A/I and R/I for heterogeneous products are influence-weighted averages (zero-influence constants contribute zero); repeated tensor products cannot amplify a finite ratio. This holds for arbitrary factors, not only positive-root-deficit factors.

## 5. Actual Boolean normalization controls and sharpness

Let a be the two-bit function negative only at 00. Its four Fourier masses are all 1/4: H(a)=2, I(a)=1, E a=1/2. Every proper restriction has zero spectral entropy, hence R_K(a)=(2-K)_+. Let F_t be the product of t independent copies, for any integer t>=1. Then H(F_t)=2t, I(F_t)=t, Var(F_t)=1-4^{-t}, R_K(F_t)=t(2-K)_+. These identities are exact for the full sequence of actual Boolean functions.

Using a single core gives A_coarse=t[kappa+(2-K)_+]; using individual physical bits as cores gives A_fine=(kappa+2)t. At K in [0,2], these attain both endpoints of the sandwich, so the partition bandwidth K I is real. For K>=2, their ratios to I are kappa and kappa+2, while H/I=2. Their ratios to variance diverge linearly; even Z_fine/Var=2t/(1-4^{-t}) diverges. Such variance-normalized divergence is therefore not an FEI disproof. Conversion from bits to nats scales entropy by ln 2 and never changes bounded versus unbounded. Conditioning away the empty spectral set requires converting both numerator and denominator: if v=Var(F)>0, H=h_2(v)+v H_cond and I=v E[|S| | S nonempty], so H_cond/(I/v)<=H/I.

More explicitly H_nats=lambda H_bits, lambda=ln 2, gives R^{nats}_K=lambda R^{bits}_{K/lambda}; one must scale K and kappa too when comparing the same bank in different units. Fixed positive conversion factors in H or I preserve bounded versus unbounded. Dividing total influence by dimension is NOT a fixed conversion: for the very same F_t, H/(I/(2t))=4t although H/I=2. Adding arbitrarily many dummy physical variables leaves H,I,R_K unchanged, yet can arbitrarily inflate a ratio using average influence per variable. These are failed counterexample normalizations. A claimed family must return to squared normalized Fourier coefficients of an actual {-1,1}-valued function and to total uniform physical influence.

## 6. Actual-family extraction even from the clipped candidate

The earlier clipped candidate fails coherence, but a high ROOT ratio for that candidate is still a valid counterexample detector. Define A_plus=(C)_+ + kappa I(F)+sum_i q_i R_K(g_i), with kappa fixed and K>=0 arbitrary. Put W=sum_i q_i H(g_i). Since each R_K(g_i)<=H(g_i),

    A_plus <= kappa I(F)+(H(F)-W)_+ + W
           = kappa I(F)+max(H(F),W).

For I(F)>0, the identity I(F)=sum_i q_i I(g_i) writes W/I(F) as an influence-weighted average of H(g_i)/I(g_i) over q_i I(g_i)>0. Terms of zero influence have zero entropy and contribute zero. Therefore

    A_plus/I(F)-kappa
      <= max( H(F)/I(F), max_{i:q_i I(g_i)>0} H(g_i)/I(g_i) ).

This is a constructive actual-function extraction: given a sequence of literal Boolean circuits with A_plus/I unbounded, choose at each index the member with maximal ordinary ratio among the whole circuit and its finitely many active cores. The selected members are actual Boolean functions on uniform cubes and have unbounded H/I. No coherence of A_plus is asserted or needed; no upper bound on K is needed in this direction. An unbounded algebraic parameter without actual Boolean core realizations does not meet the hypothesis. A single finite high ratio supplies only a finite lower bound on the universal constant.

For clarity, this argument does not accept an arbitrary admission capital or a reported envelope value. It uses the specific bank above and the checked bound R_K<=H for its TRUE full physical stopping hulls. Replacing R_K by an unbounded overestimate would invalidate the extraction.

## Scope and first unsupported line

The proofs above are universal finite-dimensional lemmas and a normalization standard. The first unsupported line for full FEI remains a universal initial price A<=L I (equivalently an appropriate universal entropy bound). Neither exact tensorization nor bank coherence supplies that price. Any proposed disproof still needs a concrete actual Boolean family and unbounded A/I with fixed kappa, or unbounded ordinary H/I directly. No such family is asserted here.
