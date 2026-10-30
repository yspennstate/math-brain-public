# Product banks and the sparse ghost charge

The moving-anchor bank transfers linearly across independent factors. A canonical sparse reset has an additional outcome-KL charge when the reference contains atoms outside the actual spectral support. That charge is at most one unit of guard influence over all controller queries. Full FEI remains open.

All functions below are actual Boolean functions on finite uniform cubes. Entropy and KL use bits. Every tree is finite, uses physical coordinate queries and retains both outcomes. References are complete normalized laws. Signed reset costs include negative refunds; they are never clipped individually.

## 1. The moving-anchor input, reconstructed

For a factor f on d coordinates with p(S)=fhat(S)^2, nonempty J and 0<alpha<1, put beta=1-alpha, ell=log2(1/beta), u=p(empty),

    q(empty)=u,
    q(S)=beta*p(S)+alpha*(1-u)*1[S=J], S nonempty.

For projected J=empty define q=p. Normalization holds, q>=beta*p, and K=D(p||q)<=ell*(1-p(J)) when J is nonempty. At J the KL term is nonpositive; all other nonempty terms equal ell*p(S). Constants and zero source rows are included.

For physical query i erase i first, giving Pbar,Qbar; then use the actual amplitude channel

    k_y(T)=p_y(T)/(2Pbar(T)), or 1/2 when Pbar(T)=0,
    r_y=sum Qbar(T)k_y(T),
    q_inh,y(T)=Qbar(T)k_y(T)/r_y.

Here p_y(T)=(fhat(T)+y*fhat(T+i))^2, and r_y>=beta/2>0. The finite KL chain reads K=E+O+mean K_inh, where E is erasure KL release and O=D(fair||r). The signed reset is sigma=mean K_fresh-mean K_inh.

Put a=1-p(J), J'=J\{i}, b=fhat(J symmetric_difference {i}). The coefficient-square identity gives mean a_child=a-b^2. Set B=(d-1)a while J is nonempty, and B=0 after absorption. When J' is nonempty,

    B-mean B_child=a+(d-2)b^2 >= a-b^2.

The side conditions are d>=2 and b^2>=0. Thus sigma<=ell*(B-mean B_child). When J' is empty, fresh KL is zero and sigma=-mean K_inh<=0, so the same inequality holds. Future exact resets have zero cost. Finite-tree summation gives

    Sigma <= ell*(B_root-E B_terminal),
    K_root+Sigma <= ell*(d*a_root-E B_terminal).

This reconstructs A039-MOVING-ANCHOR-ABSORPTION@1's universal bank, not its separate supplied mod3 application. Zero terminal KL after absorption does not erase terminal entropy.

## 2. Tensor products: ghost rows give a refund

Let f=product_j f_j on disjoint blocks, with P=product_j p_j and fresh Q=product_j q_j. Allow arbitrary adaptive interleaving of the physical factor queries, using projected anchors in each factor. Reset to the complete product reference after each query. H, I and root KL add exactly.

Query factor j. Write r^loc for its own outcome law and

    z=Q_other({s: P_other(s)=0}).

On rows with P_other>0 the physical kernel is the local kernel. On source-zero rows it is the stipulated fair fallback. Hence

    r^glob=(1-z)*r^loc+z*fair.

Erasure release is exactly the local release, because Pbar and Qbar remain product laws. Fresh expected KL changes only in factor j. Comparing the two exact KL chains therefore gives

    sigma_global=sigma_local+O_global-O_local <= sigma_local.

The inequality is convexity of D(fair||r) in its second argument. It remains valid for z=0 or1, reference-only anchors and an absorbed local anchor. All outcome probabilities are positive: each factor reference dominates its actual spectrum by a positive constant, and so does their finite product. No factorwise inherited-reference assertion is needed (it would be false on ghost rows).

Consequently the ONE supplied product bank

    V=sum_j ell_j*(d_j-1)*a_j

pays every signed reset, with

    K_root+Sigma <= sum_j ell_j*d_j*a_j - E V_terminal.

All original bookings subtract from this same account. Full terminal entropy and influence remain sums of the factor terminal quantities. The theorem prices conversion, not the initial complete cross-entropy H(P)+K_root. There is no T log T term for T identical independently referenced factors. A common unqueried parity has H=0 and does not change these bills; it retains its own terminal influence. A genuinely arbitrary common factor retains its full entropy and cannot be discarded.

## 3. Sparse activation: explicit normalized source

Take g=product_j f_j, an independent fair guard x, k>=1 fair controls, rho=2^-k and A_k the point indicator that all controls are +1. Put

    F=1+A_k*(x*g-1).

On the spectrum, selector-only empty mass is (1-rho)^2, every other selector-only frequency has mass rho^2, and for each data frequency S and each controller frequency R the guard-bearing row has mass rho^2*p_g(S). Define Q_F by keeping all selector-only masses and replacing p_g by the supplied product Q_g on guard-bearing rows. These sectors are disjoint because the guard is present in every data row. Their total masses are1-rho and rho, respectively. Thus Q_F is complete and normalized, and

    D(P_F||Q_F)=rho*sum_j D(p_j||q_j),
    CE(P_F,Q_F)=H_quotient+rho*sum_j CE(p_j,q_j),
    H(F)=H_quotient+rho*sum_j H(f_j),
    I(F)=rho*(k+1+sum_j I(f_j)).

Here H_quotient is the entropy of the law with masses (1-rho)^2 and rho^2 on the other 2^(k+1)-1 frequencies. There is no assumption that g is balanced; the independent guard makes x*g balanced. The terminal active core entropy is rho*H(g), which remains owed.

## 4. The controller ghost correction

Let z=Q_g({S:p_g(S)=0}) in [0,1). Query a controller and then reset to the canonical sparse reference on both children. The source-supported data rows deterministically select the passing outcome, but reference-only data rows use the fair fallback. Direct summation gives

    r_pass=(1-rho*z)/2, r_fail=(1+rho*z)/2,
    E=0,
    O=-(1/2)log2(1-rho^2*z^2).

All denominators are positive since rho<=1/2. The fresh child references are the canonical lift at2rho on the passing child and the exact constant spectrum on failure. Their mean KL equals the root KL, so the signed reset costs sigma=O, not zero. Inherited failure ghosts must not be replaced for free.

An actual all-essential witness is g=x1*x2 with anchor J={x1}, alpha1/6, plus guard x and one selector. Then z=1/6, rho=1/2 and sigma=O=(1/2)log2(144/143)>0. All four coordinates are essential. This refutes the source-zero-fallback extension of a zero-controller-cost statement. It does not refute the positive-reserve transfer below or the source-complete telescopes in earlier A048 stages.

At the j-controls-remaining node rho_j=2^-j and physical reach rho/rho_j. The exact cumulative controller bill is

    C_ctrl=rho*sum_(j=1)^k O(rho_j*z)/rho_j.

For t in [0,1/2], -ln(1-t^2)<=t^2/(1-t^2), by integrating 1/(1-s). Also ln2>2/3, from the positive atanh series. Therefore O(t)<=t^2, strictly for t>0. The finite geometric sum yields

    0<=C_ctrl<=rho*z^2*(1-rho)<=rho.

The whole sparse protocol (controls first, then ANY adaptive factor tree; guard retained) satisfies

    K_root+Sigma_total
      <=rho*[sum_j ell_j*d_j*a_j + z^2*(1-rho) - E V_terminal].

The guard's original influence is rho. A supplied unused guard reserve of rho therefore pays the extra charge once; no root or descendant reserve is renewed. This is a bound independent of k and T, not a k-logarithmic charge. A previously spent guard reserve is not available. The physical control influence is k*rho and stays separately booked. The construction does not prove that the original core cross-entropy source is O(I).

## 5. Why globally re-spiking gives misleading upper budgets

Consider the single-anchor initial upper envelope U(f,J)=n*(1-p_f(J)). This is an upper envelope, not the exact realized cost.

For the all-essential near-character factor h_d=chi_{1}*(1-2*1_point) on d>=2 coordinates, p_h({1})=(1-2^(1-d))^2=1-a_d, where a_d=2^(2-d)*(1-2^-d). With r independent copies and their union anchor, the global envelope is rd*[1-(1-a_d)^r], while the sum of factor envelopes is rd*a_d. Their ratio is [1-(1-a_d)^r]/a_d. When r*a_d<=1 it is at least r/2: for0<=a<1, (1-a)^(-r)>=(1+a)^r>=1+ra, so1-(1-a)^r>=ra/(1+ra). This exhibits a quadratic-in-r global envelope in the small-ra regime, while the product bank is linear in r. It is an artifact of replacing factor references by one new global spike, not an actual quadratic bill lower bound.

For the all-essential sparse point defect F=1+A_k*(x-1), every nonempty coefficient has squared magnitude rho^2, n=k+1 and I=n*rho. Hence EVERY nonempty global anchor obeys

    U(F,J)/I(F)=(1-rho^2)/rho -> infinity.

This obstruction uses essential coordinates only. It shows exponential failure of influence-pricing this particular global envelope under sparse activation. The exact normalized factor/sector account above scales by rho with an additional guard charge at most rho. Neither result disproves FEI.

## 6. Checks that could fail and the remaining line

Critical checks are the projected-anchor square identity, last-anchor absorption, nonzero actual reference outcomes, product ghost fallback, sparse ghost normalization, sign of the reset, and complete terminal costs. code/check.py uses literal Walsh transforms, exact Fraction laws and exact prime-log KL identities on every Boolean function through n3, all anchors and physical edges. It separately checks all ordered pairs of two-bit truth tables and k1,2 sparse activations. code/audit.py uses integer FWHT and literal pivotal edges without importing the producer, and verifies the explicit all-essential counterfamilies and constant/character boundaries. These finite checks support the unrestricted finite-tree derivation; they do not prove FEI. The initial false zero-controller assertion is preserved in out/FAILED_ZERO_CONTROLLER_CLAIM.txt.

First unsupported universal line: construct a useful arbitrary-core ORIGINAL complete reference with cross-entropy and required adaptive terminal liability paid by one O(I) account, including any already spent guard reserve. A globally re-spiked n*(1-p(J)) envelope cannot provide that line. External review of the new ghost-corrected transfer remains pending. No full Lean entropy/KL proof is claimed.
