# Two-direction quadratic ownership of the mixed sector

All logs are natural; actual physical biases are interior. F=2*1{w N_A+N_B>=t}-1, with disjoint groups, real w>0,t. P(U,T)=Fhat(U,T)^2, v_i=4p_i(1-p_i), M=sum_{U,T nonempty}P, D=sum_mixed(|U|+|T|-1)P. The root deficit Delta also includes pure higher-degree packets. Empty mixed sector has zero obligation and no conditional reference is formed.

## 1. Source quadratic reference and independent reconstruction

For nonempty T in B the physical count profile h_T(k)=Fhat_B(T;N_A=k)/sqrt(v_T) has canonical representation constant+sum_j alpha_Tj g_j(A), with symmetric tails g_j=2*1{N_A>=j}-1. Different tails' physical derivatives have disjoint count supports, so

    I_A(h_T)=sum_j alpha_Tj^2 I_A(g_j).

Define K_A(U,T)=v_T sum_j alpha_Tj^2 ghat_j(U)^2. Parseval gives

    sum_mixed |U|K_A=sum_mixed |U|P=:J_A,
    Z_A=sum_mixed K_A<=J_A<=D.

Coherent nonzero actual amplitude entails at least one nonzero summand in K_A, so K_A>0 wherever P>0. The coefficient bound |ghat_j(U)|<=sqrt(v_U) and sum|alpha|<=1 give K_A<=v_Uv_T. No Boolean law is presumed for K_A/Z_A. These are the independently reconstructed A045-QUADRATIC-TAIL-ENERGY-NORMALIZED-REFERENCE@1 facts.

Reverse A,B to construct K_B. The light-group tails remain symmetric: conditioning on a B-count gives a threshold in N_A. Real w causes no difficulty. Its corresponding energy and mass satisfy

    sum_mixed |T|K_B=J_B=sum_mixed |T|P,
    Z_B<=J_B<=D,
    J_A+J_B=D+M.                                           (1)

The sum of orientation energies is D+M, not two independent copies of D. This exact ledger governs the reference below.

## 2. Complete pointwise-best reference

On the full mixed label space, including zero-actual-mass labels, put

    K_*(U,T)=max(K_A(U,T),K_B(U,T)),
    Z_*=sum K_*, Q_*=K_*/Z_*, R=P/M,
    C_*=sum_mixed P ln(v_Uv_T/K_*).

When M>0, Z_*>0; Q_* is normalized and positive on the support of R. Also K_*<=v_Uv_T, so C_*>=0. Crucially

    Z_*<=Z_A+Z_B<=J_A+J_B=D+M<=2D.                        (2)

The choice of direction can depend on the entire Fourier set; its cost is paid by this full normalizer, including off-support labels. It is not a free postselected reference. Logarithmic expansion proves exactly

    E_mixed=C_*+M ln(Z_*/M)-M KL(R||Q_*).                   (3)

The positive mass tax costs at most Z_*/e, hence

    [M ln(Z_*/M)]_+ <=(D+M)/e <=2D/e <3D/4,
    E_mixed<=C_*+2D/e-M KL(R||Q_*).                        (4)

Here e>8/3. The negative term is an ordinary KL under R. If degree tilt Rd=(|U|+|T|-1)P/D is used, preserve it as

    M KL(R||Q_*)=D E_Rd[ln(R/Q_*)/(|U|+|T|-1)].

It is not generally D times the unweighted degree KL. This retains A045's harmonic correction. Physical conditional-input TC, any reference-conversion spectral TC, and coordinate erasure are distinct. No Boolean estimate is applied to R or Q_*.

For comparison, using the uniform mixture (K_A+K_B)/2 would own at most D mass but add a pointwise ln2 direction charge. The max reference avoids that separate charge; equation (2) accounts for its normalizer in one conserved mixed ledger.

## 3. One orientation alone cannot pay even the actual entropy

Use the actual fair two-heavy family already defined in A041's prior stage: n=4r+1 light inputs, two heavy inputs of weight n+1, threshold n+1+(n+1)/2, r>=1. Branches at heavy count0,1,2 are -1, odd majority g, +1. Then

    M=1/4, D=(I(g)+1)/4, J_A=1/2, J_B=I(g)/4,
    E_mixed=[E(g)+ln4]/4,
    C_A=[E(g)+ln8]/4.                                     (5)

C_A is the source reference's corrected cross-entropy in the A direction. Both C_A/J_A and E_mixed/J_A diverge. Thus not even retaining the source's constant KL rebate can pay the full mixed logarithm from J_A alone. This refutes an unregistered strengthening C_A<=KJ_A, and the stronger direct E_mixed<=KJ_A, not A045's valid reference statement or a root-Delta payment.

Here is an elementary all-r lower bound. Let c_m=binom(2m,m)/4^m. Induction gives for m>=1

    c_m^2>=1/(4m),    c_m^2<=1/(m+1).

For the first inequality the ratio c_{m+1}/c_m=(2m+1)/(2m+2) is at least sqrt(m/(m+1)); for the second, its square is at most (m+1)/(m+2), since the difference after clearing denominators is3m+2>=0. The majority singleton coefficient is q=c_{2r}. Its total singleton mass satisfies (4r+1)q^2>=1/2, while ln(1/q^2)>=ln(2r+1). Corrected entropy is nonnegative term by term, so

    E(g)>= (1/2)ln(2r+1),
    E_mixed/J_A>= (1/4)ln(2r+1)+(1/2)ln4 -> infinity.     (6)

This is an actual two-weight Boolean family, not an arbitrary spectral profile. No new growing truth-table search is needed for the infinite quantifier. It shows why the other group's terminal entropy cannot be discarded from a quadratic energy account.

## 4. The two-direction reference repairs this control exactly

For this family K_A(U,T)=P_g(T)/8 at each of the three nonempty A labels U. Actual mixed P is P_g(T)/4 only at U=A. In the reverse direction the A-full coefficient profile on the B count is -g(B)/2, which has just one tail jump. Thus K_B=P on the mixed label space, with zero entries at the two singleton A labels. Consequently

    K_*=P on actual support; Z_*=1/2,
    C_*=E_mixed, KL(R||Q_*)=ln2,
    M ln(Z_*/M)=ln2/4.                                   (7)

The normalizer and the complete-reference KL cancel exactly. Off-support A singleton labels remain in Q_* and are not discarded. For the symmetric baseline E(g)<=c[I(g)-1], c=460+80ln2, this gives C_*<=cD. This is a diagnostic of the new reference on the old obstruction, not a new isolated class target and not an all-two-weight payment theorem.

## Exact first unsupported line

No absolute bound C_*<=KD has been proved for all actual two-weight gates at all product biases. Nor is the weaker signed remainder C_*-M KL(R||Q_*) proved paid. Equations (1)-(4) now supply a complete per-set direction choice with its finite normalizer cost; (6) excludes funding the whole charge from one derivative direction. Next must bound the selected complete cross-entropy or its signed remainder using the exact physical coefficient profiles, keeping the already paid pure sectors and all normalization rebates. Summing A044/A045's local mean-only pair bills would reintroduce their proved congestion failure and is not this reference construction. The recovered pivotal-credit failure retains its coefficient-one scope.

## Recovered weighted guards are preserved

When A is one physical bit, its single tail literal gives K_A=P on every mixed label, without any Booleanity assumption on the B coefficient process. Therefore K_*>=P and C_*<=E_mixed. In particular the recovered guards F=2*1{mX0+sum_jXj>=m}-1 with q0=(1-eta)q^m/[eta+(1-eta)q^m] are the disjoint composition OR(X0,AND(X1,...,Xm)). Both gates are symmetric thresholds at their actual induced product biases, so exact corrected entropy/deficit composition and the accepted symmetric baseline give E(F)<=cDelta(F). This holds for every m,q,eta in their declared ranges, including q=m^-2,eta=1/m and eta=1/2,q->0. Thus C_*<=cDelta on all three recovered weighted normalization/TC guards. Their failure of conditional-input TC and coefficient-one pivotal payment is not imported into the spectral reference. Finite certificates check the new reference on explicitly frozen rational members; the all-parameter conclusion is the composition argument, not grid extrapolation.

## 5. One complete owner on A045's congestion fixture

A045's latest obstruction is a different actual Boolean class: a single fair selector C chooses parity chi on n=16r^2 fair data bits or a symmetric band sign g. It is not a two-weight threshold, so the full two-direction threshold theorem is not silently applied to it. Its one-bit selector direction does have an exact universal cofactor identity, valid for any Boolean branches and any interior selector bias:

    K_C({C},T)=P({C},T) for every nonempty data set T.

Indeed the sole canonical tail is the selector literal. Its coefficient profile jump alpha_T=(f1hat(T)-f0hat(T))/(2sqrt(v_T)) gives K_C=v_C(f1hat-f0hat)^2/4=P({C},T). Thus Z_C=M, Q_C=R and the reference charges every occupied mixed label exactly once, with no repeated pair owners, normalization tax or KL mismatch. This does not prove a general entropy payment: the remaining cost is precisely E_mixed, including the actual terminal spectra of both branches.

On the specified congestion control, all n+1 physical coordinates are fair, H(F)<=n+1 bits by spectral support, and I(F)>=n/2 from the parity branch. Thus Delta(F)>=n/2-1 and E_mixed<=E(F)<= (n+1)ln2 <=3ln2 Delta(F) for n>=16. This is a concrete complete-owner diagnostic on A045's already paid family, not a new universal selector or threshold theorem. It resolves the repeated-pair ownership there by retaining the whole terminal mixed cost and paying it from the root, rather than reusing the selector's much smaller derivative energy. Any extension beyond this family still needs the complete signed terminal reference charge.
