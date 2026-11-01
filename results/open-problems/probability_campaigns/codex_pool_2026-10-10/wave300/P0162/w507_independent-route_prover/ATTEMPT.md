# P0162: restriction entropy and a bent-function obstruction

2026-10-10. Author w507; requested adversary w508; referee w509. No independent mathematical verdict yet. The precommit is in APPROACH_PRECOMMIT.md. The global conjecture is not proved.

## Exact target

For uniform x in {-1,1}^n and Boolean f(x) in {-1,1}, put a_S=E[f(x) product_{j in S}x_j], p(S)=a_S^2, H(f)=sum_S p(S) log_2(1/p(S)), and I(f)=sum_S |S|p(S). Parseval gives sum p=1; zero summands are zero. P0162 asks for one finite constant C, independent of n and f, with H(f)<=C I(f). Constants have both sides zero. The target is the conjecture stated by O'Donnell-Wright-Zhou (2011), abstract and introduction, attributed to Friedgut-Kalai (1996). Current literature evidence includes Han arXiv:2312.08271v2 and Gonzalez-MacManus-Pereyra arXiv:2606.00246v2; none of the checked abstracts supplies a general solution. Exact local retirement checks remain pending.

## Method boundary

The precommitted restriction induction is established territory: arXiv:2606.00246v2 Section 4 and Appendix B derive this framework. I therefore claim no novelty for the identity or sufficient induction criterion. The precommit and initial derivation were saved before any peer proof was read. The final distinct extension is specified below.

Later targeted reads, after the independent derivation: w505/ATTEMPT.md contains the same canonical quadratic-bent-plus-point-flip witness and a sharper constant-2 bound for that canonical family. L1-L3 here are therefore independent reproductions, not a claimed new lane result. The reserved extension is L4-L5: arbitrary flat-spectrum Boolean base, arbitrary flipped vertex, invariant spectral entropy, and exact influence dependence on local sensitivity. Further computations are restricted to this extension. The population store card claim_d15d0160e58b4c9183707be9f49462d2 already records a different monotone per-coordinate obstruction, high-influence localization and a 7.05 restriction-induction floor, explicitly unverified. No result from that card is assumed in these proofs.

## L1: exact nonnegative restriction-entropy increment

Fix coordinate i; let g=f|_{x_i=+1}, h=f|_{x_i=-1}, with Walsh coefficients u_T and v_T. The two coefficients of f indexed by T and T union {i} are A_T=(u_T+v_T)/2 and B_T=(u_T-v_T)/2. Define r_T=(u_T^2+v_T^2)/2=A_T^2+B_T^2 and q_T=B_T^2/r_T when r_T>0. Write b(t)=-t log_2 t-(1-t)log_2(1-t). Then

    Delta_i(f) := H(f)-(H(g)+H(h))/2
                = JS(u^2,v^2) + sum_T r_T b(q_T),
    JS(u^2,v^2) := H(r)-(H(u^2)+H(v^2))/2 >= 0,
    I_i(f) = sum_T B_T^2,
    I(f) = (I(g)+I(h))/2 + I_i(f).

Proof: entropy of each two-element pair (A_T^2,B_T^2) is -r_T log_2 r_T+r_T b(q_T). Sum the pairs and subtract the averaged restriction entropies. Jensen concavity of entropy gives JS>=0. For influence, Parseval applied to (g-h)/2 gives I_i, and pairing |T| and |T|+1 gives the last equality. No independence assumption is used. This identity agrees with arXiv:2606.00246v2 Appendix B equation (32).

## L2: unbounded local charge for a genuine Boolean family

Use equivalent inputs z in {0,1}^m with character chi_T(z)=(-1)^{sum_{j in T}z_j}. Let m be a positive even integer, N=2^m, and

    g_m(z) = (-1)^{z_1 z_2 + z_3 z_4 + ... + z_{m-1}z_m},
    h_m(z) = g_m(z)-2 1_{z=0},
    F_m(z,y) = g_m(z) if y=+1, h_m(z) if y=-1.

All three functions are Boolean since g_m(0)=1. The two-variable quadratic factor has coefficients (1,1,1,-1)/2 in the subset order empty,{1},{2},{1,2}; multiplying factors shows u_T=sigma_T/sqrt(N), sigma_T in {-1,1}. Therefore

    v_T = sigma_T/sqrt(N)-2/N,
    A_T = sigma_T/sqrt(N)-1/N,
    B_T = 1/N,
    r_T = (N-2 sigma_T sqrt(N)+2)/N^2,
    q_T = 1/(N-2 sigma_T sqrt(N)+2),
    I_y(F_m)=1/N.

L1 and b(q)>=q log_2(1/q) now imply

    Delta_y(F_m)/I_y(F_m)
      >= (1/N) sum_T log_2(N-2 sigma_T sqrt(N)+2)
      >= log_2(N-2sqrt(N)+2) -> infinity.

This is an analytic counterexample to a dimension-independent bound Delta_i(f)<=C I_i(f) for EVERY coordinate. It refutes neither FEI nor the weaker existence of at least one good coordinate.

## L3: this is precisely the minimum-influence split, and FEI holds for the family

For each original coordinate j, g_m changes under a j-flip exactly when its paired bit is 1, hence I_j(g_m)=1/2. Changing only g_m(0) toggles only the undirected edge {0,e_j} in direction j. It was not a boundary edge because g_m(0)=g_m(e_j)=1. Its two endpoints have probability 2/N. Thus I_j(h_m)=1/2+2/N and

    I_j(F_m)=1/2+1/N  (j<=m),
    I(F_m)=m/2+(m+1)/N.

Since m>=2, y is the unique minimum-influence coordinate, and the unbounded-charge conclusion applies to the rule 'always split the least influential relevant coordinate'. Conversely, the spectrum has at most 2N atoms, so H(F_m)<=log_2(2N)=m+1<=3 I(F_m). The construction is an obstruction to a proof method, while itself satisfying FEI with constant 3.

## L4: the obstruction applies to every bent base and every flipped vertex

Let m>=4 be even and let g:{0,1}^m->{-1,1} have flat Walsh spectrum, meaning |hat(g)(T)|=1/sqrt(N) for every T, N=2^m. For any vertex a, set h=g-2 g(a)1_{z=a}, and splice F as above. Put tau_T=sqrt(N)hat(g)(T)g(a)chi_T(a), which lies in {-1,1}. Fourier inversion at a gives sum_T tau_T=sqrt(N), so the two sign counts are K_+=(N+sqrt(N))/2 and K_-=(N-sqrt(N))/2. After removing a unit sign from each coefficient, the squared coefficients A_T^2, B_T^2 and r_T are exactly those of L2, with sigma replaced by tau. Consequently H(g), H(h), H(F), I_y(F) and Delta_y(F)/I_y(F) depend only on m, not on the chosen bent base or vertex. In particular the lower bound of L2 holds unchanged.

Flat spectrum gives I_j(g)=1/2 for every j. Flipping at a toggles exactly the edge {a,a+e_j}, so I_j(h)=1/2 plus or minus 2/N, and I_j(F)=1/2 plus or minus 1/N. Since N>=16 these are strictly greater than I_y(F)=1/N: the selector is again the unique minimum-influence coordinate. Also

    I(F) >= m/2-(m-1)/N,
    H(F) <= m+1 <= 3 [m/2-(m-1)/N] <= 3 I(F).

For the middle inequality, m=4 gives 5<=87/16. For even m>=6, m/2-1>=2 and 3(m-1)/2^m<=15/64<2; the sequence (m-1)/2^m decreases for integer m>=2. This proves that inequality for all the stated m. Thus every bent base with a single-vertex splice satisfies FEI with constant 3 and exhibits the same unbounded failure of minimum-influence entropy induction. Novelty is not claimed.

## L5: exact global influence range and the extremizer inside the whole bent-splice class

In L4 let s_g(a)=#{j:g(a)!=g(a+e_j)} be the local sensitivity at the flipped vertex. In direction j, the toggled edge was a boundary edge exactly when j contributes to s_g(a). Hence, writing e_j(a) for that 0/1 event,

    I_j(F)=1/2 + (1-2 e_j(a))/N,
    I(F)=m/2 + (m+1-2 s_g(a))/N.

Since 0<=s_g(a)<=m, all influences lie in the interval

    m/2-(m-1)/N <= I(F) <= m/2+(m+1)/N.

Every one of the m+1 discrete values is attained: choose the canonical quadratic base, multiply it by the character chi_A with |A|=s, and flip the vertex a=0. At 0, the canonical base and all its unit neighbors equal +1; the character changes exactly the neighbors in A. Multiplication by a character only translates the Walsh coefficients and preserves flatness. Thus s_g(0)=s for every s=0,...,m.

By L4, H(F)=E_m is independent of the choice of bent base and flipped vertex. With R=sqrt(N), K_+=(N+R)/2, K_-=(N-R)/2, phi(t)=t log_2(1/t), phi(0)=0, its exact value is

    E_m = K_+ phi((R-1)^2/N^2)
        + K_- phi((R+1)^2/N^2) + N phi(1/N^2).

E_m>0 because the selector block has N positive masses. Therefore, at each fixed m, the sharp maximum of H(F)/I(F) within this precisely defined entire bent-splice class is

    E_m / [m/2-(m-1)/N],

attained by the parity-twisted canonical base chi_[m] g_m flipped at zero. The selector's Delta/I does not change with this twist, but the global H/I does. This is the distinct extension; it is not a new best constant for FEI over all Boolean functions.

## L6: the canonical constant 2 does not extend to arbitrary bent splices

Take m=4 and g(z)=(-1)^{z_1 z_2+z_3 z_4+z_1+z_2+z_3+z_4}, flip a=0 on the minus selector branch, and form F. This is the full-parity twist from L5, so I(F)=2-3/16=29/16. Its Walsh probabilities are ten copies of 9/256, six copies of 25/256, and sixteen copies of 1/256. Since log_2(256/9)>4, log_2(256/25)>3, and log_2(256)=8,

    H(F) > (10*9*4 + 6*25*3 + 16*8)/256
         = 469/128 > 464/128 = 2 I(F).

Thus the constant-2 bound of the canonical untwisted family cannot be extended to all bent splices. The rigorous lower ratio is H(F)/I(F)>469/232>2; the actual entropy is evaluated only as a diagnostic in EXTENSION_MEASUREMENTS.json. This is not an improvement to the best general FEI constant. No theorem claimed by w505 is refuted: their canonical class differs from this parity-twisted example.

## L7: parity translation preserves entropy, not influence

For any Boolean f on the uniform n-cube and A subset [n], let F=chi_A f. Since hat(F)(S)=hat(f)(S symmetric_difference A), the squared Walsh law is permuted, hence H(F)=H(f). But cardinality is not invariant under this permutation: |S symmetric_difference A|=|S|+|A|-2|S intersect A|. Summing against hat(f)(S)^2 gives the exact standard identity

    I(chi_A f)=I(f)+|A|-2 sum_{i in A} I_i(f).

If the selector coordinate is outside A, its influence also stays fixed; both restriction entropies are preserved, so its Delta stays fixed. Applied to L3, a twist on s original bits lowers I(F) by 2s/N while preserving H(F) and the selector Delta/I. This is a second proof of the attainment part of L5 and explains the constant-2 transfer failure in L6. The Walsh-translation identity is standard, rederived here; no novelty claim.

## Single hardest remaining gap

To complete this route for all Boolean f one would need a universal C and a justified selection/aggregate argument that charges the entropy increments to total influence throughout the restriction tree. A sufficient (unproved) form is: every nonconstant Boolean f has some relevant i with Delta_i(f)<=C I_i(f). If it holds, dimension induction using L1 proves FEI. Neither L1 nor the family L2 establishes that selection principle. Minimum-influence selection fails by L2-L3. No 'proved FEI' claim is made.

NEXT: Independently verify L1-L3 with bounded truth-table/Fourier computations; check whether named prior attempts already contain this exact bent splice.
