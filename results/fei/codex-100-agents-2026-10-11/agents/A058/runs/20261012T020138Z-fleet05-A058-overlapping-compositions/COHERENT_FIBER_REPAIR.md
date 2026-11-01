# One shared anchor: exact signed correction and two distinct failed prices

Units: bits; all functions are Boolean signs on a uniform cube. This repairs the scope of A058's existing overlap ledger, rather than opening a new broad FEI candidate.

Start from the previous anchored function f_0 with outer Fourier coefficients a_T and shared factors h_T=product_j b_j^(A1_T)_j. Identify x_2=x_1 (the alternative x_2=-x_1 is equivalent to a sign change in the outer coefficients). Write phi(T) for the private frequency that replaces the two first membership bits by their XOR and retains all other private bits. Every fiber has two labels, paired by T'=T symmetric-difference {1,2}. Let v_T(S)=a_T hhat_T(S), where S is a complete shared support. Then the actual merged coefficient is

c_(phi(T),S)=v_T(S)+v_T'(S).

Signs of constant shared factors are included. Fourier coefficients of h_T are obtained only after Boolean parity cancellation of reused b_j; no independent-copy convolution is used.

Define a normalized latent law ell(T,S)=v_T(S)^2 and its pushforward

Q(Y)=v_T(S)^2+v_T'(S)^2,
P(Y)=(v_T(S)+v_T'(S))^2,
delta(Y)=2 v_T(S) v_T'(S),

where Y=(phi(T),S). Both P and Q have mass one. Q is normalized by the original anchored spectrum. P is the spectrum of the actual Boolean diagonal restriction, so Parseval normalizes it. Directly, sum delta=E[h_1 h_2] sum_T a_T a_T'=0 by the outer Boolean XOR identity. Thus the global norm cancellation is a Boolean identity, not normalization imposed on an arbitrary real coherent vector.

P<=2Q pointwise; if Q=0 then P=0. The latent posterior debt is

B_lat=H(ell)-H(Q)=sum_Y Q(Y) h2(v_T(S)^2/Q(Y)).

Put K=D_KL(P||Q) and R=-sum_Y delta(Y) log2 Q(Y), with zero-Q terms omitted. The exact coherent ledger is

H(P)=H(f_0)-B_lat-K+R.

Proof: expand H(P)-H(Q)=-sum(P-Q)log2 Q-sum P log2(P/Q). This is precisely R-K; apply the latent probability chain rule. Further, 0<=K<=1, 0<=B_lat<=1. The correction R is signed and may be positive or negative. Neither posterior loss nor normalization credit may be relabeled as an unsigned influence payment.

The shared physical anchor influence is

I_x(f)=sum_{Y:private frequency contains x}P(Y).

It is not the old sum Inf_1(F)+Inf_2(F). For any other private coordinate, use its membership indicator in P. For shared coordinates use their membership in S. These weighted sums give every physical influence once, but there is no general equality with the old activated d_j budget after identification.

## Exact counterfamily: positive coherent entropy increment is not paid by this anchor

Let b_k be the quadratic bent sign on 2k bits,

b_k(z)=(-1)^(z_1 z_2+...+z_(2k-1) z_(2k))

in binary coordinates. Each two-bit factor has four Fourier squares 1/4. Hence H(b_k)=2k and I(b_k)=k. Take the two-input gate F to be -1 only at (y_1,y_2)=(+1,-1). Its coefficients are

(a_empty,a_1,a_2,a_12)=(1/2,-1/2,1/2,1/2).

Use the two children g_1=x b_k, g_2=-x b_k; the constant sign is an allowed constant shared gate, or equivalently a negated outer input. The actual Boolean merged function is f=-x b_k. Prior to identifying its two private bits,

H(f_0)=2+k,
H(f)=2k,
I_x(f)=1,
I_data(f)=k,
H(f)-H(f_0)=k-2.

The pushed incoherent Q has mass 1/2 at the empty support and mass (1/2) bhat_k(S)^2 on anchor-odd supports. Thus

H(Q)=1+k, B_lat=1, K=1, R=k.

Every equality is exact for all k>=1. In particular no finite C gives either R<=C I_x or H(f)-H(f_0)<=C I_x uniformly over this shared-anchor class. The counterfamily keeps the whole function Boolean and normalized; it is not the real-vector obstruction X013. Data influence pays R on this family: R=I_data. Its FEI ratio is 2k/(k+1)<2, so it is not an FEI counterexample.

## Exact zero-influence control: posterior debt itself is not paid by the anchor

With the same off-diagonal exceptional F and g_1=g_2=x (all shared factors constant), f=1. Its anchor influence is zero. The latent law is uniform on four outer labels, Q is uniform on the two private frequency fibers, and P is concentrated at the empty frequency. Consequently H(f_0)=2, B_lat=1, K=1, R=0, H(f)=0. Thus B_lat<=C I_x is also false for every C. This posterior is a subtractive entropy credit in the exact ledger, not a positive debt that must independently be paid to bound H(P).

## X004 and the bent-splice control

The canonical X004 Boolean selector has children +y and -y, and actual function xy: H=0, I=2. Reconstructing the physical coefficients gives this exact answer; an incoherent selector mixture predicts entropy 2 and influence 3/2. It is retained as a separate supplied collision control. No assertion here extends the disjoint-support selector identity.

For the supplied sparse bent splice (X009), with even core dimension m, delta=2^-m and actual children b and b-2*1_{0}, the selector influence is delta. Its actual spectral selector erasure has the exact law derived from coefficients: at zero core frequency the selector-odd mass is delta^2 and selector-even mass (sqrt(delta)-delta)^2; at every nonzero core frequency the odd mass is delta^2 and even mass (sign*sqrt(delta)-delta)^2. This is a distinct physical splice, not automatically a member of the one-anchor algebraic family. It tests why a selector-only entropy/erasure increment helper cannot be imported. Its stated B_x/delta asymptotic grows as log2(1/delta). The existing source theorem is a control, not newly claimed here; finite exact replay of its actual coefficient and influence law is included.

## Surviving universal gap

The previous anchored theorem is still true at its hypotheses; its posterior identity never controlled the signed R created by identification. The first unsupported line is a nonreusing physical payment of R-B_lat-K together with retained terminal data entropy. Charging the shared anchor alone is now refuted. The next repair must compare the increase with the CHANGE in physical data influence or with a reserved terminal deficit, rather than spend the data influence that already paid H(f_0) again.

Here is the exact deficit interface, including the loss of a physical anchor. Let l(Y)=|phi(T)|+|S| and L=2 Pr_ell(1,2 both belong to T)=2 sum_{T includes {1,2}}a_T^2. Counting membership on both sides gives

I(merged)-I(old)=sum_Y delta(Y) l(Y)-L.

The negative L is essential: an even private pair loses two original coordinates on identification. For any fixed C, the deficit D_C=CI-H therefore satisfies

D_C(merged)-D_C(old)=C[sum delta l-L]+B_lat+K-R.

Equivalently the unpaid signed increment is

G_C=R-B_lat-K-C[sum delta l-L].

Proving G_C<=0 under a structural hypothesis preserves the old certified deficit without reusing its data influence. More general tree transport needs a separately conserved reserve to pay positive G_C and must retain terminal H. For the bent counterfamily, Delta I_data=k/2, Delta I_anchor=0, and G_2=-2 exactly. For the constant zero-anchor control Delta I=-1 and G_2=0. Thus both anchor-only prices fail but these controls do not refute a correctly retained deficit payment. The bent counterfamily is mandatory: a reserve must cover exactly k-2 additional entropy bits and recognize that the physical data price changes from k/2 to k, rather than charge the entire k anew. A universal G_C sign bound, or a universally paid positive-part sum, is OPEN; this identity is not such a theorem.
