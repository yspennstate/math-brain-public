# Independent reconstruction of A039 moving-anchor absorption

A039-MOVING-ANCHOR-ABSORPTION@1 holds at its stated scope. The reference transport and the supplied-source recovery are separate statements. Neither supplies the initial reference price for arbitrary Boolean functions. All logarithms are in bits.

## Reference, support and physical channel

Let f be Boolean on n finite uniform coordinates, p(S)=fhat(S)^2, alpha in (0,1), beta=1-alpha, ell=log2(1/beta). For a nonempty character J set

    q(0)=p(0), q(S)=beta p(S)+alpha(1-p(0)) 1[S=J], S nonempty.

For J empty set q=p. The nonempty formula is NOT extended to J empty. Each law sums to one. Since q>=beta p, all source-positive atoms are covered and every KL is finite. The possible atom q(J)>0=p(J) is retained. Direct separation gives 0<=K=D(p||q)<=ell(1-p(0)-p(J))<=ell a, where a=1-p(J); for J empty K=0.

On querying i erase its spectral coordinate: Pbar(T)=p(T)+p(T+i), with the corresponding Qbar. The actual Boolean children have normalized squared amplitudes (fhat(T)+/-fhat(T+i))^2, denoted p_y. Thus mean_y p_y=Pbar. Apply k_y(T)=p_y(T)/(2Pbar(T)) when Pbar(T)>0 and k_y(T)=1/2 otherwise. Reference-only rows therefore survive with an explicit fair kernel. Put r_y=sum Qbar k_y and q_inh,y=Qbar k_y/r_y. Because Qbar>=beta Pbar and each physical child is normalized, r_y>=beta/2>0. The source outcome law is fair even though r need not be fair.

The finite KL chain proves

    K=E+O+mean K_inh,
    E=K-D(Pbar||Qbar)>=0, O=D(fair||r)>=0.

Reset both children to the same construction with projected J'=J minus i, and define the ACTUAL signed reset sigma=mean K_fresh-mean K_inh. No term is clipped; hence sigma<=mean K_fresh. If J'=empty, K_fresh=0 and sigma<=0. If J was already empty, both inherited and fresh references are exact spectra, r is fair and E=O=sigma=0.

## The bank and all adaptive histories

Let B=(n-1)a when J is nonempty and B=0 when empty. If J remains nonempty after querying i, write b=fhat(J symmetric_difference {i}). Physical restriction gives mean a_child=a-b^2, including queries inside J (the child amplitudes interchange sign order). Since n>=2 in this case,

    B-mean B_child=a+(n-2)b^2,
    (B-mean B_child)-mean a_child=(n-1)b^2>=0.

Thus sigma<=ell(B-mean B_child). For the last anchor query, sigma<=0 while B-mean B_child=B>=0. Subsequent queries are exact and cost zero. All cases include constants, vanishing anchor coefficients, ghosts, and n=1.

Multiply by actual physical reach probabilities in ANY finite adaptive restriction tree and sum. The tree has depth at most n; every internal contribution cancels its child contribution. Early stopping and branch-dependent queries require no independence assumption. Therefore

    Sigma<=ell(B_root-E B_leaf),
    K_root+Sigma<=ell(n a_root-E B_leaf)<=ell n a_root,
    K_root+Sigma=sum reach E+sum reach O+E K_leaf.

This directly retains the query KL challenged elsewhere on the board: sum reach E is explicitly present. The proof does not substitute an endpoint functional for a transaction cost. Resetting both children is a hypothesis; resetting only selected nodes without repricing the inherited reference is not covered.

For a singleton anchor, B_root=(n-1)a_root equals A036's old protected bank. For larger J, it exceeds that old (n-|J|)a_root by (|J|-1)a_root. The larger-anchor result does not claim that extra reserve is free.

## Terminal entropy and the SAME original owner

The projected anchor can be empty. Nevertheless mean a_child=a-b^2 remains valid: after absorption this is the conditional-mean square identity at the empty frequency. Therefore A=E a_leaf<=a_root for arbitrary stopped trees. With d remaining coordinates, partitioning the spectrum at its distinguished atom yields H_leaf<=h2(a_leaf)+d a_leaf. Finite Jensen gives E H_leaf<=h2(A)+D A, D the original dimension. When a_root<1/2, monotonicity of h2(t)+Dt on [0,a_root] permits A<=a_root. There is no surviving nonempty-atom influence lower bound after absorption.

The application uses A036 stage21 PROOF sections3-5: even N>=10, D=2N, delta=2^-N, singleton J={z1}, alpha=1/6, delta<=a_root<=12delta, physical active reach 1/4, complementary surplus 2, and root surplus R=4I(F)-H(F)>=741/256. The old full-spike conversion c is retained exactly once with A0+c/4=K_J(h)/4. No new supplier or anchor is introduced. Hence the inclusive source/conversion/reset bill L obeys

    L=A0+c/4+Sigma_core/4<=6N 2^-N ell<1/64.

The strict certificate is 6^15<16*5^15, giving ell<4/15. At N=10 the RATIONAL ENVELOPE (6N2^-N)*(4/15) equals 1/64; strictness comes from ell, not from that envelope. N2^-N decreases for N>=10.

Since a>=delta and log2(e)<2, h2(a)<=a(N+2); thus E H_core<=12delta(3N+2)<=3/8. In fact the entropy bound is strict here, so the complete terminal surplus S=2+(4E I_core-E H_core)/4>61/32, using only I_core>=0. The previous protected bound 741/256 used I_core>=1-a and cannot be carried past absorption.

Let e=H(F)-E H_terminal-4(I(F)-E I_terminal)=S-R. Retaining all signs gives the exact recovery identity

    S-[A0+e+c/4+Sigma_core/4]_+=min(S,R-L).

R-L>737/256>61/32. After the SAME old debit 0<=omega<=1/4, recovery exceeds 61/32-1/4=53/32. This is a proof of the specified supplied-source recovery; it does not price an arbitrary initial source.

## The majority guard and the remaining unpaid line

For odd majority on n=2m+1, every influence equals c_m=binom(2m,m)/4^m and I=n c_m. For any nonempty J choose i in J. Monotonicity gives D_i f in {0,1}, so |fhat(J)|=|E D_i f chi_(J-i)|<=c_m. Also c_m=product_(k=1)^m(2k-1)/(2k), and ((2k-1)/(2k))^2<=k/(k+1) follows from 1<=3k. Thus c_m^2<=1/(m+1), and

    n(1-p(J))/I >= 1/c_m-c_m
                      >=sqrt(m+1)-1/sqrt(m+1) -> infinity.

All coordinates are essential. This rules out influence-pricing this particular initial upper bank even after optimizing J and deleting dummies. It does not lower-bound the actual selected-policy cost. In particular, immediately querying a singleton anchor gives nonpositive reset cost but leaves arbitrary child entropy. Zero terminal KL supplies no entropy payment.

The first unsupported universal line is an ORIGINAL useful arbitrary-core source/decomposition with complete cross-entropy and full terminal bills bounded by O(I), or a necessary selected policy paid from the SAME unused original capacity. Full FEI remains OPEN. The collision candidate remains T=L_collision/Z=H(v/Z)-log2 Z; ell here is a different scalar. No raw collision-L payment is revived.

## Verification scope

The independent code uses literal Walsh sums, exact rational normalizers, exact prime-exponent log cancellation, and outward rational atanh intervals. It imports only A036's prior interval arithmetic, never A039 producer code. Frozen finite checks cover all Boolean functions through n3, all anchors including empty, all coordinates, alpha=1/6 and1/2, and three adaptive complete/stopped rules. These finite checks audit the formulas; the finite-tree argument above supplies the all-dimensional proof. A separate scalar Lean attempt is recorded with its actual outcome and cannot certify the entropy argument.
