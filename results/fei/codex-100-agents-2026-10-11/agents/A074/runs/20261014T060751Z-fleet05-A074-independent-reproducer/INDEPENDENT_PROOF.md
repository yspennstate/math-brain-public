# Independent reconstruction: arbitrary-core rare escape and physical terminal boundary

Uniform physical inputs, sign-valued outputs, entropy in bits. Let h be negative on {0,1,2,4,8,16,32,6,17,40}, zero bits encoding +1, and J(z)=-h(z xor1). For an arbitrary nonconstant core g orient its output so p=P(g=-1) belongs to (0,1/16]. No monotonicity, transitivity, dimension bound, or erasure threshold is imposed.

## 1. Actual gate, stopping, and unequal blocks

The negative weight counts of J are [0,4,10,18,15,6,1]. Expanding sum_k count_k p^k(1-p)^(6-k) gives sigma(p)=4p-10p^2+18p^3-19p^4+10p^5-2p^6. This is exact counting, not fitting sampled values. On 0<p<=1/16,

sigma(p)/p >=4-10/16-19/16^3-2/16^5>3,

sigma(p)/p <=4+p(-10+18/16+10/16^3)<4.

Thus applying J to six identical independent actual cores produces a minority probability strictly between 3p and 4p. The first output above 1/16 is strictly below 1/4. The stopping time is finite because the pre-stopping probabilities grow by more than a factor of three; otherwise 3^N p0 would eventually exceed 1/16. If N steps occur and p_j are the pre-step probabilities, p_j<=delta*3^{-(N-1-j)}, delta=1/16. The four directions pivotal at the all-zero outer input are 1,2,3,5; directions 0,4 are not. No common influence value or outer transitivity is assumed.

## 2. Independent polynomial and physical derivation

Write the actual gate as its binary multilinear polynomial J(x)=sum_T c_T product_(j in T)x_j, coefficients computed by binary inclusion-exclusion. Substitute x_j=p_j+(x_j-p_j). The centered coefficient is b_S=sum_(T containing S)c_T product_(j in T\S)p_j, with squared orthonormal coefficient b_S^2 product_(j in S)p_j(1-p_j). This representation remains valid when p_j=0 or1: positive-degree zero-variance terms vanish, and no variance division is required. It is different from the source's FWHT/normalized biased-basis implementation.

Under physical substitution x_j=(1-g_j)/2, each occupied block has only nonempty Fourier coefficients -ghat_j(U)/2. Therefore each full physical Fourier coefficient has exactly one occupied-block pattern S and equals b_S product_(j in S)(-ghat_j(U_j)/2). The checker compares this prediction with fresh direct character sums of all4096 truth-table entries for four actual12-bit children, all16384 coefficients exactly. The direct character algorithm uses integer masks of odd character values, not FWHT or the source script.

Let q_j be the probability that outer coordinate j is pivotal. It is the expected square of the Boolean section derivative D_j=(J(x_j=0)-J(x_j=1))/2 on the other five bits. This gives both the physical pivotal probability and the spectral identity sum_(S contains j)s_S=v q_j, v=4p(1-p). An inner physical edge flips the output precisely when that inner edge is bichromatic and the outer derivative is nonzero; the latter depends only on the other blocks. Hence Inf_(j,i)(F)=q_j d_i exactly. Every q_j is positive at full-support bias because the actual gate depends on every direction.

For Phi(x,y)=(x+y)log2(x+y)-xlog2x-ylog2y, put m=1-2p, t=ghat({i})^2. Nonempty residual Fourier pairs within a physical block inherit the inner pair with total multiplier q_j. The empty residual has a different pair and must be replaced. Homogeneity and integration over other occupied-block fillings give

B_(j,i)(F)=q_j B_i(g)+R_j(t),

R_j(t)=sum_(S not containing j)Phi(s_S,t*s_(S+j)/v)-q_j Phi(m^2,t).

Dummy inner coordinates have d_i=t=B_i=0 and remain dummy. The exact symbolic identity Phi(x,0)=0 is used; interval subtraction alone would only enclose it around zero. Every relevant direction remains relevant. Thus minima are taken over all actual physical directions, including all six unequal outer roles.

If rho is the normalized nonempty inner spectrum, H(g)=h2(v)+v H(rho). The unique occupied-pattern decomposition gives

H(F)=H_p(J)+v Q H(rho)=Q H(g)+C,

I(F)=Q I(g),   Q=sum_j q_j,   C=H_p(J)-Q h2(v).

In particular H(F)/I(F)=H(g)/I(g)+C/(Q I(g)). C is signed. No initial entropy, terminal entropy, or negative correction is dropped.

## 3. Arbitrary-core erasure loss

Since Phi>=0, R_j(t)>=-q_j Phi(m^2,t). If x+y<=1, then Phi(x,y)<=y log2(1/y)+y/ln2: write the natural-log expression as y ln((x+y)/y)+x ln(1+y/x), bound the first logarithm by ln(1/y) and the second term by y; extend to x=0 by continuity.

For b=|ghat({i})|, the physical derivative expectation bounds b<=d_i. Also b<=2p follows by writing g=1-2*1_A and using the mean-zero singleton character. Parseval gives m^2+b^2<=1. For b>0,

Phi(m^2,b^2)/d_i <= b log2(e/b^2) <=2p log2(e/(4p^2))=:L(p).

The last scalar function has derivative (-1-2 ln b)/ln2>0 on b<=1/8, and L is increasing on the rare band. For b=0 the loss is exactly zero. Dividing by q_j d_i and taking the minimum over every j,i yields E(F)>=E(g)-L(p). This reasoning is uniform in the core dimension and does not assume a singleton/influence equality.

Using sum_(k>=0)3^-k=3/2 and sum_(k>=0)k3^-k=3/4, the reverse geometric stopping bound gives

sum_(j<N)L(p_j) <=3delta log2(3e/(4delta^2))=(3/16)log2(192e)<111/64.

The strict rational bound follows from ln2>2/3, so log2(e)<3/2, and 3^4<2^7, so log2(192)<31/4. These combine to (3/16)(3/2+31/4)=111/64. Therefore E(G)>=E(g)-(3/16)log2(192e)>E(g)-111/64.

## 4. Independent edge-boundary proof for normalization

We reconstruct I(g)>=2p log2(1/p) by induction on the combinatorial edge boundary, rather than the source's entropy tensorization proof. For A subset of the n-cube, let M=|A| and b(A) be the number of undirected edges leaving A. The desired inequality is b(A)>=M log2(2^n/M). It holds at n=0, with the empty-set convention 0log0=0.

Split A into two (n-1)-cube sections A0,A1, sizes M0,M1. Crossing edges are |A0 symmetric_difference A1|>=|M0-M1|. Induction therefore gives

b(A)>=sum_(r=0,1)M_r log2(2^(n-1)/M_r)+|M0-M1|.

With t=M0/M, the difference from M log2(2^n/M) is M[h2(t)-1+|2t-1|]>=0. The last inequality h2(t)>=2min(t,1-t) follows from concavity and the chords joining0,1/2,1. Finally I(g)=b(A)/2^(n-1), giving I>=2p log2(1/p) with the correct factor of two. Empty sections and constants are included.

## 5. Signed normalized entropy price

Spectral-set entropy subadditivity gives H_p(J)<=sum_j h2(v q_j). For fixed v in[0,1], the deficit f(q)=q h2(v)+v h2(q)-h2(vq) has f(0)=f(1)=0 and

f''(q)=-v(1-v)/[ln2(1-q)(1-vq)]<=0.

Concavity, extended continuously at endpoints, proves h2(vq)<=q h2(v)+v h2(q), so C<=v sum_j h2(q_j). At the all-zero assignment of the other five inputs the pivotal status is deterministic. The chance of leaving that assignment is at most5p. Therefore min(q_j,1-q_j)<=5p, h2(q_j)<=h2(5p)<=5p log2(e/(5p)). The four dominant pivotal directions give Q>=4(1-p)^5>=4(1-5p)>=11/4. As v<=4p,

C<=120p^2 log2(e/(5p)),

C/(Q I(g)) <=(240/11)p * log2(e/(5p))/log2(1/p) <=(240/11)p.

The final step uses e<5. It is an upper bound on a signed increment, not on its absolute value. The exact ratio identity from Section2 telescopes retaining the full initial ratio. Since sum_(j<N)p_j<=3delta/2=3/32, the total upper increment is <=45/22. This proves every clause of A072-ONEFLIP-RARE-ESCAPE-PRICE@1 at its original scope without repair.

## 6. Current physical-query interface, independently reproduced at two fixtures

For unequal independent cores, let C(p)=H_p(J)-sum_l q_l h2(v_l). The same binary polynomial decomposition gives H(F)=sum_l q_l H(g_l)+C(p) and I(F)=sum_l q_l I(g_l). Querying a uniform physical coordinate i in block j changes only p_j; its two actual child probabilities average to p_j. q_j is independent of p_j, and each other q_l is affine in p_j. Thus

Delta_i H(F)=q_j Delta_i H(g_j)+Delta_i C,

Delta_i C=C(p)-[C(p^+)+C(p^-)]/2.

The rate-K excess is q_j[Delta_i H(g_j)-K Inf_i(g_j)]+Delta_i C. Both complete child entropies and every other core remain. At a constant child p_j=0, our centered polynomial never divides by zero, and its physical entropy and influence are exactly zero.

The two selected current source fixtures use the six-bit core negative on{0,1,2}, gate J, block0, and inner coordinates0 and2. These are actual36-bit parent functions and35-bit physical children. Fresh direct spectra and edges check the core and its children. Unequal-bias binary polynomial spectra and separate pivotal-event enumeration check every outer role. All32 inner fibers times all32 other-outer assignments give a second physical edge calculation. Exact coefficient structure proves the entropy identity; interval residuals enclosing zero are diagnostics.

out/BOUNDARY_VALIDATION.json certifies Delta C>0 and Delta H(F)>4 Inf_(0,i)(F) in both selected cases, including the coordinate2 constant-child endpoint. The witnesses were reported by A072; we independently reconstruct them without importing source code. No claim that an actual child reserve is available follows. This statement concerns true entropy decrement, not B_i.

## 7. What remains after the new board results

The arbitrary-core single escape theorem is now independently accepted. A075's new all-legal-word theorem and A072's independent review of A080's repeated-cycle theorem have been read as dispatch context, not independently accepted in this stage. Their scopes pay composition corrections while retaining the arbitrary starting H/I. Consequently the useful universal NEXT is an actual non-flat physical-query payment: source one genuinely unused child surplus for the positive terminal correction and inherited query excess, retaining both full terminal bills. Merely asserting I-h2(p)>=0 does not provide this payment. No universal C018 constant, C019 stopping-tree inequality, or full FEI result follows here.
