# Coordinate erasure: signed phase boundary and the two missing credits

All entropies and logarithms are in bits. Let f be a Boolean sign on a finite uniform cube, fix coordinate i, and write its actual children as g=f_(i=+1), h=f_(i=-1). On the remaining m coordinates set A=(g+h)/2, V=(g-h)/2, and F=A+imaginary_unit*V. Write u_T=Ahat(T), v_T=Vhat(T), q_T=u_T^2+v_T^2, and d=sum_T v_T^2=Inf_i(f). Zero entropy terms are zero.

## 1. Full signed constraints, rather than a generic probability bound

Booleanity is equivalent to A^2+V^2=1 and AV=0 pointwise, hence to F taking values in {1,-1,imaginary_unit,-imaginary_unit}, equivalently F^4=1. In Fourier coordinates these are ALL-shift equations

    sum_T [u_T u_(T xor U)+v_T v_(T xor U)] = delta_(U,0),
    sum_T u_T v_(T xor U) = 0.

Consequently G=F^2=A^2-V^2=g*h is a genuine real Boolean sign. Crucially, the imaginary Fourier part of F^2 cancels by the SECOND full signed identity BEFORE any square or absolute value. Set

    s_U=sum_T v_T v_(T xor U),
    W_i=2 sum_(U nonempty) |U| s_U^2 = I(G)/2.

The equality follows from Ghat(U)=delta_(U,0)-2s_U. The v signs remain inside the convolution. Since V^2=1_D, D={g!=h} has physical density d, and W_i is the normalized edge boundary of D. This step fails for a general unit-norm real vector.

## 2. Entropy identity with both credits explicit

Define the spectral-sector mutual information

    M_i=sum_T u_T^2 log2[u_T^2/((1-d)q_T)]
               +v_T^2 log2[v_T^2/(d q_T)],

with the deterministic-sector cases interpreted as M_i=0. It is the relative entropy of the genuine probability law (T,sector) with masses u_T^2 and v_T^2, against q_T times the sector marginal. Thus M_i>=0. Exactly,

    B_i=sum_T q_T h2(v_T^2/q_T)=h2(d)-M_i.             (1)

Define the physical isoperimetric deficit and the elementary scalar slack

    R_i=W_i-d log2(1/d),
    sigma(d)=log2(e)*d-(1-d)log2(1/(1-d)).

Both are nonnegative. The exact paid decomposition is

    B_i = W_i+log2(e)*d - R_i - M_i - sigma(d).       (2)

In particular the Booleanity-specific signed convolution bound is

    B_i+M_i <= 2 sum_(U nonempty)|U|(sum_T v_T v_(T xor U))^2
                     +log2(e)*d.                    (3)

The B05 lead already derived the uncredited bound B_i<=I(g*h)/2+log2(e)d. We do NOT claim that as a new theorem. This stage supplies the signed fourth-root interface, retains both exact credits, proves sharpness of its boundary coefficient, and refutes aggregate payment after retaining only spectral credit.

For completeness, edge-isoperimetry needs no external premise. If a subset of an m-cube has k vertices, its number of internal edges is at most k log2(k)/2. Induct on m, splitting into sizes a,b. Cross edges number at most min(a,b). The induction closes because (a+b)h2(a/(a+b))>=2min(a,b), by concavity of binary entropy on either half interval. Since boundary=mk-2*internal_edges, boundary/2^m>=d log2(1/d). This is R_i>=0. The inequality -(1-d)ln(1-d)<=d gives sigma(d)>=0; for example integrate ln(1-t)+1<=1 to bound -(1-d)ln(1-d). All endpoints follow by continuity. All Fourier sums are finite.

## 3. An explicit normalized non-Boolean violation

On a one-bit cube take real coefficients a_empty=4/5, a_i=3/5. The vector has norm one; the real inverse Walsh function has values 7/5 and 1/5. Here A=4/5, V=3/5, d=9/25, M_i=0, B_i=h2(9/25), and W_i=0 since every convolution is constant. But

    h2(9/25)> (9/25)log2(25/9) > (9/25)log2(e).

The last inequality follows from e<11/4<25/9 (the exponential series gives e<=8/3+5/96=261/96<11/4). Thus (3) fails. AV=12/25 is nonzero, F^2 is complex, and F^4!=1. This meets the lead's discriminator: (3) is not a generic probability consequence. The real linear control psi_n by itself has B_i=0 and therefore cannot discriminate THIS proposed coordinate inequality; we use the explicit normalized vector above instead.

## 4. Sharpness: the coefficient 1/2 on I(F^2) cannot decrease

For every even m>=2, on y in F_2^m take the quadratic bent sign b(y)=(-1)^(y1*y2+...+y_(m-1)*ym), d=2^(-m), and Boolean children g=b, h=b-2*1_(y=0). Then V=1_(y=0), A=b-1_(y=0), and F is b off the origin and imaginary_unit at the origin. The full fourth-root condition is exact. The bent Fourier coefficients are epsilon_T sqrt(d), and

    u_T=epsilon_T sqrt(d)-d, v_T=d,
    q_T=d[1+2d-2epsilon_T sqrt(d)],
    I(F^2)=2m d, W_i=m d, R_i=0.

The positive Fourier sign proportion is (1+sqrt(d))/2 because sum_T bhat(T)=b(0)=1. The imaginary-sector conditional spectrum is uniform U_T=d. A direct binary-mixture calculation yields

    chi2(P_(T,sector)||q tensor Bernoulli(d))
      =d/(1-d)[sum_T U_T^2/q_T-1],
    sum_T U_T^2/q_T=(1+4d)/(1+4d^2),
    chi2=4d^2/(1+4d^2).

Jensen applied under P to its likelihood ratio gives M_i<=log2(1+chi2)<=4d^2/ln2. Hence

    h2(d)-4d^2/ln2 <= B_i <= h2(d),
    B_i/(m d) -> 1.

Indeed (1-d)log2(1/(1-d))/d ->log2(e), while d log2(1/d)=m d. Therefore any universal bound B_i<=alpha I(F^2)+C d with fixed finite C forces alpha>=1/2. More generally no fixed C and nonnegative sublinear function psi(t)=o(t) can satisfy B_i<=d psi(I(F^2)/d)+C d for every Boolean split. This is an all-dimensional actual Boolean obstruction, not a conjecture disproof.

## 5. Dense bent phases: spectral KL credit alone does not pay boundary

For every EVEN r>=2 let M=I_r+J_r over F_2 (zero diagonal, one off diagonal). Since J_r^2=r J_r=0 and 2J_r=0, M^2=I_r, so M is invertible. On 2r physical bits define

    f_r(x,y)=(-1)^(x^T M y).

Summing over x proves every Fourier coefficient has magnitude 2^(-r); explicitly the sum forces My equal the x-frequency. Thus p is uniform on all 2^(2r) subsets, H=2r, I=r, d_i=1/2, B_i=1, and M_i=0 for EVERY coordinate. The square phase G_i is the sign product of children. For an x_j split it is the character of the r-1 y-variables in row j of M, and for a y_j split the corresponding column character. Therefore

    I(G_i)=r-1,
    W_i=(r-1)/2,
    R_i=(r-2)/2,
    sigma(1/2)=[log2(e)-1]/2.

For every coordinate (2) reduces exactly to B_i=1. But

    Q_sum=sum_i W_i=r(r-1),
    sum_i M_i=0,
    [Q_sum-sum_i M_i]/I=r-1 -> infinity.

This REFUTES a proposed uniform aggregate bound Q_sum-sum_i M_i<=K I even after spectral KL credit. It also refutes that bound with any fixed nonnegative multiplier on M_i. The missing isoperimetric deficit is decisive: sum_i R_i=r(r-2), and Q_sum-sum_i(M_i+R_i)=r=I. A low-physical-influence restriction cannot be inferred from arbitrary small spectral KL, and flat spectral entropy does not mean small phase boundary.

## 6. Tensor guard and the honest universal frontier

If f is multiplied by an arbitrary Boolean core h on disjoint variables, for a coordinate of f its phase becomes F*h. Its square is unchanged because h^2=1; W_i,d_i,R_i and B_i are unchanged, and the spectral sector law tensors with the core law, so M_i is unchanged as well. Thus the scalar phase quantities are correctly tensor additive after summing coordinates, even though the anchor cost in stage 1 was not. This does NOT pay the core's coordinate entropies.

Summing (2) gives the EXACT universal identity

    B(f)=log2(e) I(f)+Q_sum(f)-sum_i[R_i+M_i+sigma(d_i)].   (4)

No bound for the residual on the right is proved; claiming Q_sum-sum M=O(I) is now false. The first unsupported line for this route is an influence-paid bound for Q_sum-sum(R+M+sigma), or a physical stopping-tree version with terminal entropy and single-use credits. This is precisely C018 (or C019 after telescoping), not a solved weaker problem.

## 7. Refined C019 interface; do not confuse the two boundary totals

The B05 lead's odd-face quantity is Q_odd(f)=2^(1-n) times the number of odd 2-faces. It satisfies Q_odd=Q_sum/2, because the aggregate over coordinates counts each face twice. At a physical split its telescope is

    Q_odd(f)=W_i+[Q_odd(g)+Q_odd(h)]/2.

Proof: faces using direction i correspond exactly to edges cut by gh; the other faces lie in either child. This reconstructs the B05 lead's Lemma 2. Thus in a physical stopping tree T, w_v is the reach probability and

    sum_v w_v W_v=Q_odd(f)-E_leaf Q_odd(f_leaf).

Combine this with the EXACT entropy-drop identity Delta_v H=B_v+JS_v and influence telescope, to obtain

    H(f)=E_leaf H(f_leaf)+log2(e)[I(f)-E_leaf I(f_leaf)]
        +Q_odd(f)-E_leaf Q_odd(f_leaf)
        -sum_v w_v[R_v+M_v+sigma(d_v)]+sum_v w_v JS_v.       (5)

Nothing from the terminal leaf is discarded. With JS_v<=c_JS d_v, c_JS=2/ln2, (5) gives a proved conditional upper bound retaining ALL phase credits and the terminal odd-face balance. The local phase identities above are self-contained; this explicit C019 interface uses the previously proved C005 entropy-drop/JS theorem, whose proof was read in ERASURE_REDUCTION sections 1-2 in stage 1. No independent acceptance of the new credit interface is yet claimed.

For fixed K>=log2(e), the exact positive excess currency at a node is

    D_K(v)=[W_v-R_v-M_v-sigma(d_v)-(K-log2(e))d_v]_+
          =[B_v-Kd_v]_+.

Consequently a complete tree gives H(f)<=(K+c_JS)I(f)+sum_v w_v D_K(v); with nonconstant leaves the corresponding terminal H and I terms must remain. Unlike the uncredited bad-node bill W_v, D_K(v) subtracts both credits BEFORE taking a positive part. This is an exact interface, not an assertion that its expectation is linearly paid. Proving existence of a tree with this bill O(I) is sufficient for full FEI; the weaker-looking reparametrization is not called an easier theorem merely because it uses phases.

The shortest next mathematical action is to evaluate this joint-credit positive excess on the nested rare-flip tower already selected by B05, retaining both R and M and already paid terminal leaves, then seek an ownership or selection proof for the full joint-credit bill. This consumes an existing universal-route stress test rather than starting another isolated flat-class calculation.
