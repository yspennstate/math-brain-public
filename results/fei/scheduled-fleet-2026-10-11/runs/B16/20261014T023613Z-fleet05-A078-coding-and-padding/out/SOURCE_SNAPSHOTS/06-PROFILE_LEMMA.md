# A078 paired-profile payment

All physical inputs are independent fair bits. At an actual Boolean split write f(z,x)=u(x)+(-1)^z v(x), u=(g+h)/2 and v=(g-h)/2. Then u,v take values in {-1,0,1}, uv=0 pointwise, and alpha=E v^2 is the physical queried influence. Put a_T=uhat(T)^2, b_T=vhat(T)^2, q_T=a_T+b_T, m_T=min(a_T,b_T). Entropy and Q are in bits and zero masses contribute zero.

## 1. Two universal paired-spectrum majorants

The exact retained profile is Q=sum_T m_T log2(q_T/m_T). For every Boolean split define

    L_half=(3/2) sum_T |uhat(T)vhat(T)|,
    L_quarter=6 sum_T |uhat(T)|^(1/2)|vhat(T)|^(3/2).

Both majorize Q. First ln(1+y)<=sqrt(y) for y>=0: its difference from sqrt(y) is zero at zero and has derivative (sqrt(y)-1)^2/[2sqrt(y)(1+y)]>=0. Taking y=max(a,b)/min(a,b) gives m log2(1+y)<=sqrt(ab)/ln2<=(3/2)sqrt(ab), since ln2>=2/3 follows from the first positive term of 2atanh(1/3).

For the second, 1/(1+y)<=y^(-3/4) for y>0, because y^(3/4)<=1+y. Integrating from zero gives ln(1+y)<=4y^(1/4). Thus the summand is at most (4/ln2) m^(3/4) max(a,b)^(1/4)<=6 a^(1/4)b^(3/4). If a>=b this last power equals the preceding min/max power; if a<=b, their ratio is sqrt(b/a)>=1. Zero cases follow by continuity. These bounds use the actual signed pair amplitudes, beyond scalar (j,kappa_min).

No universal sum_v w_v L_half<=C I is claimed. The half-power pilot is preserved as a separate attempted majorant; finite ratios cannot establish its all-dimensional boundedness. The quarter-power has the paid structural theorem below.

## 2. Physical antichain gives a negative-quarter spectral moment

Assume the support of v on its r physical residual bits is an antichain in the ordinary coordinatewise Boolean partial order. This is a hypothesis on actual physical derivative values, not on a formal spectral law. Signs of v on this support are arbitrary. Let D_k=sum_{|T|=k} vhat(T)^2 and R_k=D_k/alpha, for alpha>0. The R_k form a probability law.

Independently refresh each residual input bit with probability p. Its Fourier noise parameter is 1-p. Conditioning on v(X)!=0, on which coordinates refresh, and on the others, the support condition on the refreshed coordinates is still an antichain. A uniform K-dimensional cube gives any antichain mass at most c_K=2^-K binom(K,floor(K/2)). Here is the needed combinatorial proof: in a uniformly random maximal chain, each set of size j appears with probability 1/binom(K,j); an antichain contributes at most one set to the chain. Hence sum_{A in antichain}1/binom(K,|A|)<=1 and its size is at most the largest binomial coefficient.

Moreover c_K<=1/sqrt(K+1). For even K=2l, its ratio on increasing l is (2l+1)/(2l+2); the squared bound is preserved by (2l+1)(2l+3)<=(2l+2)^2. The base K=0 is equality. Odd K has c_(2l+1)=c_(2l+2), completing the proof.

For K~Bin(r,p), the absolute-value bound on the signed physical correlation yields

    sum_k R_k(1-p)^k
      <= E c_K <= E (K+1)^(-1/2)
      <= sqrt(E (K+1)^(-1))
      <= min(1, 1/sqrt((r+1)p)).

The inverse moment is exactly [1-(1-p)^(r+1)]/[(r+1)p], by binomial summation, with endpoint continuity. For integer l>=1 choose p=1/(l+1). Since (1+1/l)^l<=sum_{j>=0}1/j!<=3 (bound j!>=2^(j-1) for j>=2), (1-p)^l>=1/3. Therefore

    P_R(k<=l)<=3 sqrt((l+1)/(r+1)).

For l=0 take p=1 and obtain the stronger 1/sqrt(r+1) bound, hence the same stated bound. This also covers r=0.

Apply the tail-integral identity to X=((r+1)/(k+1))^(1/4)>=1. For x>=1 the preceding inequality gives P(X>x)<=3/x^2. Consequently

    E_R[((r+1)/(k+1))^(1/4)] <= 1+integral_1^infinity 3/x^2 dx =4.

All inequalities are proved for actual derivative support, without invoking threshold FEI or any unproved antichain reference-law payment.

## 3. Explicit degree-energy transport pays the quarter profile

Let A_k=sum_{|T|=k} uhat(T)^2. In addition to the derivative-antichain condition, assume the exact node inequalities

    k A_k <= (r-k+1) D_(k-1),  1<=k<=r.                 (DT)

Holder inside each degree gives sum_{|T|=k}|uhat|^(1/2)|vhat|^(3/2)<=A_k^(1/4)D_k^(3/4). Under DT this is at most

    alpha [(r-k+1)/k]^(1/4) R_(k-1)^(1/4)R_k^(3/4).

Young's inequality bounds the last two factors by R_(k-1)/4+3R_k/4. Replace the degree factor by [(r+1)/k]^(1/4). The first sum is bounded by one-quarter times the negative-quarter moment, hence by one. The second sum is bounded by three-quarters times (5/4) times that moment, hence by 15/4, because k>=1 implies ((k+1)/k)^(1/4)<=2^(1/4)<=5/4. The nonempty degrees together cost at most (19/4)alpha.

The empty contribution is |E u|^(1/2)|E v|^(3/2)<=alpha^(3/2)<=alpha: |u|<=1 and |E v|<=E|v|=alpha. Thus

    sum_T |uhat|^(1/2)|vhat|^(3/2) <= (23/4)alpha,
    Q <= L_quarter <= (69/2)alpha.                       (1)

The exact node erasure has B=Q+sum_T(q_T-m_T)log2(q_T/(q_T-m_T))<=Q+M/ln2, M=sum m_T. Standard actual-child recombination gives JS<=2M/ln2: for two masses s(1+t),s(1-t), its natural-log contribution is at most s(1-sqrt(1-t^2)), by comparing derivatives atanh(t) and t/sqrt(1-t^2); summing gives the Hellinger mass 2M. Hence the actual entropy decrement obeys

    Delta H=B+JS<=L_quarter+(3/ln2)M<=39 alpha,          (2)

using M<=alpha and ln2>=2/3. Constants are intentionally loose; the theorem targets a paid hereditary mechanism rather than improving known threshold constants.

## 4. Hereditary threshold admission and spectator accounting

For f_(m,t)=1-2*1{|x|>=t}, 1<=t<=m, its queried derivative is the indicator of the physical layer |x|=t-1 on r=m-1 bits. It is an antichain. Let v_k be a derivative Fourier coefficient at degree k, u_k the u coefficient. Symmetry and Fourier differentiation give u_k=v_(k-1) for k>=1. To see this without a presumed formula, a parent coefficient on a k-set containing any one of its coordinates equals that coordinate's derivative coefficient on the remaining (k-1)-set; all coordinates are symmetric. Therefore

    k A_k=k binom(r,k)v_(k-1)^2
          =(r-k+1)binom(r,k-1)v_(k-1)^2
          =(r-k+1)D_(k-1).

Every actual physical descendant is another such threshold or a constant. Thus this admission is hereditary and (1)-(2) pay any complete fresh-coordinate tree. In particular L_quarter,T<=69 I/2 for every shifted threshold and every adaptive coordinate order. For odd majority, all adaptive orders have the same weighted state law: after d fresh queries the observed bits are independent fair bits even when their labels are adaptively chosen, and the state threshold depends only on their number of ones. The compressed exact tree calculations use binom(d,j)/2^d with residual m=n-d, t=(n+1)/2-j. Constant branches cost zero and the query influence budget telescopes exactly to I.

If f(z,x,y)=h(y)[u(x)+(-1)^z v(x)] is an exact Boolean tensor spectator, the L_quarter value at the z query is unchanged. Its paired coefficients each acquire hhat(S), so the fractional term acquires |hhat(S)|^2 and sums to one. Q, alpha, and the pair level rate on the core are also unchanged. The theorem may therefore be applied after an explicitly verified physical tensor factorization; it does not require the full derivative support including arbitrary spectator bits to be an antichain. Terminal spectator entropy remains H(h), never a zero-cost leaf certificate.

More generally, any genuine stopping tree all of whose queried nodes satisfy the two structural conditions (after such a verified tensor factorization when used), and whose leaves satisfy H<=C_leaf I, has H(root)<=max(39,C_leaf)I(root). The proof is the exact entropy/influence telescope with leaf costs included. An external threshold theorem is not used to pay any of these node costs.

## 5. Exact gap to arbitrary cores

The local inequality Q<=L_quarter is universal. Its dimension-independent payment is conditional on an actual derivative-antichain and DT certificate at each selected physical state. Neither condition is assumed for arbitrary Boolean f. Exact first-child fixtures of A076's shifted majority/arbitrary-core family test both separately and preserve any failed level and actual descendant table. A core can fail DT or antichain after a physical query; a root-only certificate is not a stopping theorem.

The first unsupported universal line is: every arbitrary-core descendant admits a physical coordinate with a paid quarter-profile certificate (or a proved replacement for DT) using a nonreused influence budget, and all terminal spectra are paid. The universal retained-KL sandwich makes merely reporting bounded Q/I on a known FEI class uninformative. This stage instead provides an explicit local, rationally testable structural majorant and identifies failures of its sufficient structural tests. The raw mixed-fixture failure counts do not rule out free zero-overlap queries or verified spectator factorization. CORE_TRANSPORT_PROOF.md adds free-query admission, arbitrary-core mixed-majority transport, and the exact activation empty-sector correction, with every terminal control cost included. Full FEI remains open.
