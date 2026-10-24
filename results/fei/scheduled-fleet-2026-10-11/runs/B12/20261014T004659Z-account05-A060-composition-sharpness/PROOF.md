# Sharp signed data drift for the exclusive-controller reserve

All logarithms in entropy are base two. Let r>=4 be even, q=2^-r, s=sqrt(q), z in {0,1}^r, and y in {-1,+1}. Define the actual Boolean quadratic bent sign

    b(z)=(-1)^(z1*z2+z3*z4+...+z_(r-1)*z_r),
    C(z)=1[z=0],
    F(z,y)=b(z)+(y-1)C(z).

Only the point z=0 is replaced by the independent dictator y. The exclusive controller has three states: select y on C, output +1 on {b=+1}\C, and output -1 on {b=-1}. Constants are allowed selector states in A057/A038/A059. There is one independent nonconstant core, so their physical disjointness hypothesis holds.

## Exact spectrum and actual physical costs

The unnormalized two-bit quadratic Walsh vector is (2,2,2,-2). Tensoring gives bhat(T)=sigma_T*s, sigma_T in {-1,+1}; evaluation b(0)=1 implies sum sigma_T=1/s. Thus there are N_sigma=(q^-1+sigma*s^-1)/2 frequencies of each sign. Point C has every coefficient q. The two sectors of F are

    ahat(T)=sigma_T*s-q,   y-sector bhat(T)=q.

The actual y children are b and b-2C, with coefficients sigma*s and sigma*s-2q. Influence of y is q. Every control coordinate has influence 1/2+q: the bent derivative has baseline influence 1/2, and only the edge joining 0 to its coordinate neighbor changes, from no mismatch to mismatch probability 1/2. Each such edge occupies probability 2q. Therefore

    I(F)=r(1/2+q)+q,
    E I(F|y)=r(1/2+q).

No terminal influence is discarded.

## Exact terminal-inclusive drift

Put h(x)=(1-x)^2 ln((1-x)^2), and

    T(c)=sum_(sigma=+/-1) (1+sigma*s)/2 * h(c*sigma*s).

Direct summation of the squared coefficients, including zeros by continuity, gives

    H(b)=r,
    H(b-2C)=r-T(2)/ln2,
    H(F)=r+q*r-T(1)/ln2,
    D_y=H(F)-[H(b)+H(b-2C)]/2
       =q*r+[T(2)/2-T(1)]/ln2.

In the A059 ledger U=sum_j q_j[H(u_j)-eta((E u_j)^2)] is zero both before and after this query: the dictator and every constant have Fourier entropy zero, and eta(0)=eta(1)=0. Only the dictator has nonzero variance. Hence R_root=q*log2(1/q)=q*r and R_children=0. The exact signed DATA residual is

    E_r = D_y - (U_root-E U_child) - (R_root-E R_child)
        = [T(2)/2-T(1)]/ln2.

The controller has not been queried, so there is no controller-release or controller-reset term at this frontier. The terminal obligation is the actual average entropy of b and b-2C, not selected-core entropy and not output entropy.

## Convergent exact series and proved error

For |x|<1, multiply the absolutely convergent series for ln(1-x) by 2(1-x)^2:

    h(x)=-2x+3x^2-sum_(k>=3) 4*x^k/[k(k-1)(k-2)].

Since E sigma=s and E sigma^k is 1 for even k and s for odd k,

    T(c)=(3c^2-2c)*q
         -sum_(k>=3) 4*c^k*s^(k+(k mod 2))/[k(k-1)(k-2)].

Here |2s|<=1/2, justifying each rearrangement. It follows EXACTLY that

    E_r/q = 3/ln2 - sum_(k>=3)
      4*(2^(k-1)-1)*s^(k+(k mod 2))/(q*k(k-1)(k-2)*ln2).

All deficit terms are strictly positive. The k=3 and k=4 terms together give (19/6)*q/ln2. For an upper bound use k(k-1)(k-2)>=6 and 2^(k-1)-1<2^(k-1). Separate odd k>=3 and even k>=4 into geometric series. Their sum is at most 8*q^2/(1-4q). Therefore

    0 < 3/ln2 - E_r/q <= 8*q/[(1-4q)*ln2],
    3/ln2 - E_r/q >= (19/6)*q/ln2.

Consequently E_r/Inf_y(F) tends to 3/ln2 as even r tends to infinity. The coefficient 3/ln2 in A059's full signed DATA drift is optimal for exactly that U,R ledger and its allowed exclusive-controller class. It cannot be decreased by using beta^2<=Inf: here beta=1 and beta^2=Inf(y)=1 in the core. The finite bounds and convergence are analytic certificates, not extrapolation of a numerical search.

## Tensorization and scope

For k disjoint copies F^(1),...,F^(k), expose all k y coordinates while retaining all controllers. Fourier entropy, influence, entropy decrement and terminal entropy are additive for the product sign. The sum of the per-copy U,R ledgers used by the closure rule is also additive: U=0 and R=k*q*r before, R=0 after. Thus the aggregate signed residual is k*E_r and spent data influence k*q. A proposed uniform improvement E_total<=K*Pi_data+D with fixed D, on tensor products equipped with these additive per-factor ledgers, would imply E_r/q<=K by letting k grow. Choosing r so that E_r/q>K contradicts every K<3/ln2.

This tensor conclusion uses the ADDITIVE ledger explicitly. A product is not automatically a single-core instance of the original selector theorem with the same canonical U,R. It does not refute an improvement restricted to that different representation, an overhead charged once per factor, or a theorem with a stronger debit. It certifies that a fixed additive slack cannot repair the smaller coefficient in a tensor-closed additive payment rule.

Full FEI is open. H(F)/I(F) tends to 2, and the large terminal entropy r-T(2)/(2ln2) remains. The obstruction concerns the sharp local DATA residual after the existing reserve debit, not an unbounded H/I ratio or a paid controller residual. The first unsupported universal line remains a nonreused physical payment of the controller residual and the retained terminal H-U-R ledger; this stage supplies no such payment.
