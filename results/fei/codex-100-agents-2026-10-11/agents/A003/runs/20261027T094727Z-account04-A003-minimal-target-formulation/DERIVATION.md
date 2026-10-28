# Tensor overhead can be removed; an unpaid source cannot

All logarithms are base two. This is an author proof of an interface lemma, pending independent review. It does not prove FEI. Fix a nonconstant Boolean function f on d relevant variables. Put p(S)=fhat(S)^2, alpha_i=P(i in S), I=sum_i alpha_i, H=H(p), B_i=H(S_i|S_-i), and B=sum_i B_i. Thus I>0. Let c0=2/ln(2).

For u,v>=0 put Phi(u,v)=(u+v)h2(v/(u+v)), with Phi(0,0)=0, and Psi(u,v)=v log2(1+u/v), with Psi(u,0)=0. Then B_i=sum_{T not containing i} Phi(p(T),p(T+i)); write L_i for the same sum with Psi. Both kernels are positively homogeneous, including zero arguments. The baseline inequalities are L_i<=B_i<=L_i+alpha_i/ln(2), and entropy restriction drift Delta_i=B_i+JS_i, where JS_i<=c0 alpha_i. These baseline inequalities are inherited, not newly proved here.

## Exact tensor identities

On m disjoint copies put F_m=product_{b=1}^m f(x_b). Its Fourier amplitude is product_b fhat(S_b); hence p_m=p^tensor m. In particular

H(F_m)=mH, I(F_m)=mI, B(F_m)=mB,

alpha_(b,i)(F_m)=alpha_i, B_(b,i)(F_m)=B_i, L_(b,i)(F_m)=L_i.

The first equality follows by expanding log(product p(S_b)) on positive atoms and summing the other independent factors to one. Zero atoms contribute zero. For B_i and L_i, fix the other blocks; their probability t multiplies both members of the coordinate pair. Homogeneity gives t times the seed value, and sum t=1. Influence follows from the marginal. F_m remains Boolean. No conditioning on the nonempty spectrum is used.

For 0<c<1 define G_c(f)={i:alpha_i>=cI/d}. It is nonempty: otherwise sum_i alpha_i<cI. Under tensor replication it becomes precisely {(b,i):i in G_c(f)}, because I(F_m)/(md)=I/d. The maximum coordinate influence is unchanged, so the class max_i alpha_i<tau is closed under these tensors. Ambient dummy variables may instead be retained consistently: n_m=mn also preserves eligibility, but d is the less ambiguous convention.

## 1. Total erasure: sublinear total defect is enough

Fix lambda<1 and K independent of f,m. Suppose that for every Boolean seed f there is an unbounded sequence of positive integers m and real errors r_f(m) with r_f(m)/m ->0 along that sequence, such that

B(F_m)<=lambda H(F_m)+K I(F_m)+r_f(m).

Division by m gives B<=lambda H+KI+r_f(m)/m. If the asserted exact inequality were false by a fixed positive margin delta, taking an m with r_f(m)/m<delta gives a contradiction. Thus B<=lambda H+KI for every f. The inherited erasure-fraction bridge gives FEI with constant (K+c0)/(1-lambda). No uniform convergence rate across seeds is required. Constants f have H=I=B=0 and need no division by I.

The quantifier 'every seed' is essential: a bound only for a chosen tensor family settles only its seed. The same lambda<1 and K must apply to all seeds. Lambda=1 cannot be divided out and supplies no FEI constant.

## 2. A chosen coordinate: the local defect must vanish

Fix tau>0, 0<c<1, lambda<1 and K. Suppose for every nonconstant seed f with max alpha_i<tau, and along an unbounded sequence m, some i_m in G_c(F_m) obeys

B_i_m(F_m)<=(lambda H(F_m)/I(F_m)+K)alpha_i_m(F_m)+eta_f(m),

where eta_f(m)->0. The finite set of seed margins

D_i=B_i-(lambda H/I+K)alpha_i, i in G_c(f),

has a minimum D. By tensor invariance D<=eta_f(m) for every allowed m; hence D<=0. A seed coordinate realizing the minimum supplies the exact target with no defect. The inherited weak-influence localization therefore gives FEI with

C=max(log2(e/tau)+c0, (K+c0)/(1-lambda)).

Eligibility is a stronger structural demand than the existential baseline; the implication uses only its nonemptiness and invariance. For the fixed target c=1/2,tau=1/4,lambda=0,K=4, the resulting constant is 4+c0 (the high-influence price log2(4e) is below 4).

Replacing B_i with L_i gives the identical defect-removal statement. The inherited L_i<=B_i<=L_i+alpha_i/ln(2) then yields

C=max(log2(e/tau)+c0, (K+3/ln(2))/(1-lambda)).

If the L-target applies without a low-influence cutoff, its constant is simply (K+3/ln(2))/(1-lambda). A total error r_f(m)=o(m) on a ONE-coordinate inequality is insufficient. Its correct local counterpart is eta_f(m)=r_f(m)/m. For example A log2(1+md)/(md) tends to zero; A log2(1+md) does not. A constant local tolerance also cannot be dropped by replication: all seed margins repeat unchanged. This is a statement about inference, not a Boolean counterexample to an unknown universal K.

## 3. Signed Booleanity: keep every convolution equation

Let a be a real vector indexed by subsets of [d]. The conditions

sum_S a_S^2=1; sum_S a_S a_(S symmetric-difference U)=0 for every nonempty U

are equivalent to Booleanity of f(x)=sum_S a_S chi_S(x). Indeed they are exactly all Fourier coefficients of f^2=1; Fourier inversion gives the pointwise assertion. Conversely a Boolean f has f^2=1. Tensor amplitudes retain all these equations since the shifted autocorrelation factors by block. The signed route in section 2 is restricted to these exact vectors, and not all normalized real vectors.

The hypothesis cannot be omitted. For integer k>=2, take a0=(k^2-1)/(k^2+1), a1=2k/(k^2+1). Its squared masses are (1-epsilon,epsilon), epsilon=4k^2/(k^2+1)^2. Norm is exactly one, but the nonzero-shift autocorrelation is 4k(k^2-1)/(k^2+1)^2>0. Here I=epsilon and B=H=h2(epsilon), so B/I>=log2(1/epsilon)->infinity. Also L/I=log2(1/epsilon). Tensoring preserves these coordinate ratios. Thus normalization, nonnegativity and independence cannot supply any fixed K, nor the erasure-fraction inequality with lambda<1. These real vectors are not a FEI counterfamily.

## 4. Witness/source payment: sublinear full-source overhead is enough

For every Boolean seed f suppose that along an unbounded sequence m there is a normalized complete reference Q_f,m on the full spectrum of F_m, positive on supp(p_m), with

CE(p_m,Q_f,m)<=C mI+r_f(m), r_f(m)/m->0.

Then mH<=CE by nonnegativity of relative entropy. Divide by m and take the same fixed-margin contradiction to obtain FEI(C). The references need not tensorize and may depend on f,m. A noncircular construction of those references is still required. Existentially Q=p_m shows this target is FEI-equivalent; the interface lemma claims no stronger structural theorem.

For the FIXED whole-set witness mechanism retain its original gate/selector/normalizer. The sharper inherited identity is

h2(v_g)+Kref I(g)+R*(g)=H(g)+v_g D(P_g^+||U_g),

where Kref=3+2log2(3)+log2(6e), v_g=1-p_g(empty), U_g is the admitted SUBprobability on nonempty frequencies and the divergence includes missing mass. More explicitly t_A is the sum of 2^(-B_run) over distinct actual runs, c_ref=Lambda+log2 Z, U_g(A)=2^(-c_ref-Kref|A|)t_A, and R*=v_g c_ref+sum_(A nonempty) p_g(A)[-log2 t_A]. Choices remain in the original fixed admissible family; no new family or omitted normalizer is permitted. If U_g misses a positive actual atom the bill is infinite and cannot satisfy the target. For v_g=0, g is constant and FEI is immediate.

Because U_g is a subprobability, D(P_g^+||U_g)>=0: normalize its mass q<=1 and use D(P||U)=D(P||U/q)-log2 q. Thus H(g)<=h2(v_g)+Kref I(g)+R*(g). For F_m, h2(v_F_m)<=1. Consequently witnesses with R*(F_m)<=K mI+r_f(m), r_f(m)=o(m), give

mH<=(Kref+K)mI+1+r_f(m),

and hence FEI(Kref+K). This SAVES TWO in the earlier conservative constant 2+Kref+K, which first bounded h2(v_g)<=2I(g) one function at a time. Here it is a bounded total tensor overhead and vanishes after division by m. The witness choices need not factor by block. The strengthened conclusion uses the original exact interface, not a new witness construction. A universal R*<=KI hypothesis is a special case, by applying it to every F_m. The arbitrary-core residual payment itself remains OPEN.

In particular A log2(1+md)+D_f is admissible total overhead for fixed f, finite A,D_f; an error m delta_f with delta_f>0 is not. A product of a fixed imperfect reference Q has D(p_m||Q^tensor m)=mD(p||Q), by the same product expansion. Its mismatch is linear and survives amortization. Complete terminals, old debits and physical-query KL must already be included in the alleged CE/source bill; amortization never authorizes discarding them.

## Implication diagram and unpaid inputs

Tensor total-erasure target with o(m) defect -> exact B<=lambda H+KI -> FEI((K+c0)/(1-lambda)).

Tensor eligible weak-coordinate B-target with o(1) local defect -> exact eligible target -> FEI(max(log2(e/tau)+c0,(K+c0)/(1-lambda))).

Exact signed Booleanity + tensor L-target with o(1) local defect -> exact L-target -> FEI((K+3/ln(2))/(1-lambda)) (or the cutoff maximum above).

Constructed complete tensor sources with CE<=C mI+o(m) -> FEI(C).

Fixed whole-set tensor witnesses with R*<=K mI+o(m) -> FEI(Kref+K), improving the earlier conservative constant by 2.

Each implication quantifies over every seed. FEI(C) conversely implies the total-erasure target with lambda=0,K=C and zero error; it implies eligible B-selection with price C/(1-c), since G_c carries more than (1-c)I and sum_G B_i<=H. It implies the unrestricted L-selection with K=C. It implies the unrestricted reference-existence target via Q=p_m. It need not supply the prescribed fixed witnesses or fixed numerical eligible price. There is no canonical smallest stronger lemma among those structural choices.

The new permissible supplier is a constructive tensor source with only logarithmic TOTAL overhead, rather than a dimension-free additive overhead. No such arbitrary-core source is produced here. The first unsupported line is its construction from exact Boolean cancellation with CE at most C mI+o(m), for one absolute C and every seed. That line is the next universal target; repeating an optional matched reset does not establish it.
