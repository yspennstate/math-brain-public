# Denominator caps and joint root-packing constraints

Fix one positive width-two prime table E of an actual Boolean positive edge DNF, both endpoint orders, and the FULL partition event family. Weights are global, positive, and satisfy sum_(e incident v) lambda_e<=1. Write D=product_e(1+lambda_e/4)-1 and p_lambda(T)=product_(e in T)(lambda_e/4)/D for every nonempty T. These root-index coordinates reindex used-gate monomials; T is not asserted to be the actual initial-root set of every forest. This distinction is essential. All cost comparisons refer to the same table, orders, and full family, optimized over its actual run posterior.

## A sharper cap with an exact equality criterion

Let k=|T|>=1 and let L>0 be any proved upper bound on sum_(e in T)lambda_e. For example nonnegative vertex prices y_u+y_v>=1 for every edge uv in T give L=sum_v y_v. Then

    p_lambda(T) <= c(k,L)
    c(k,L) = 1 / [(1+4k/L)^k - (4k/L)^k].

Proof. Since all factors are positive, D>=D_T=product_(e in T)(1+lambda_e/4)-1>0. Divide D_T by product_T(lambda_e/4). With z_e=1/lambda_e the result is

    sum_(j=0)^(k-1) 4^j e_j(z).

There are binom(k,j) products in e_j. Their geometric mean is (product_T z)^(j/k), because each z occurs binom(k-1,j-1) times. AM-GM therefore gives e_j(z)>=binom(k,j)(product_T z)^(j/k)>=binom(k,j)(k/L)^j. The last step uses product_T lambda<=(L/k)^k. The j=0 case is the identity1, and k=1 gives cap1 directly. Sum the inequalities and use the binomial theorem. No limit or expectation is exchanged.

For k>=2 this strictly improves A006's cap min(1,4^(1-k)L^(k-1)/k^k), because that bound retained only j=k-1 in the positive denominator. Equal lambda=L/k gives equality for a table consisting only of T whenever these equal weights are packing-feasible. For a larger table this is a sharp SUPREMUM if equal weights on T are feasible: scale them by 1-epsilon and take sufficiently small positive outside weights, then let epsilon decrease to0. This supplies an admissible sequence even at saturated vertices. A sufficient criterion is (L/k) max_v deg_T(v)<=1. All star subsets satisfy it with L=1; regular graph subsets with an equal-weight fractional-matching optimum satisfy it as well. Arbitrary irregular subsets need not satisfy it; no claim of their sharpness is made.

The cap depends only on physical packing and conditioning. It applies unchanged after the full partition coefficients are recomputed and does not transfer a selected-family lower certificate to a larger event family. Replacing old caps by c in the tangent LP gives a subset of the old feasible polytope. Its exact primal-dual gap is therefore no larger. This is a lower certificate for the physical infimum; it does not pay either complete cost or entropy by influence.

## Sharp individual caps still lose joint packing

Take any two distinct incident gates i,j in any table. Let p_i=p({i}), p_j=p({j}), r=p({i,j}). All are positive under the stipulated weights. The denominator cancels exactly:

    lambda_i=4r/p_j, lambda_j=4r/p_i.

Their common vertex implies lambda_i+lambda_j<=1, hence

    p_i p_j >= 4r(p_i+p_j).

Equivalently the symmetric matrix

    [[p_i-4r, 4r], [4r, p_j-4r]]

is positive semidefinite. The determinant is p_i p_j-4r(p_i+p_j). Positivity and the displayed inequality also force both diagonal entries nonnegative, since 4r<=p_i p_j/(p_i+p_j)<min(p_i,p_j). This is a necessary constraint on every pair of incident gates in the full table.

For a table with exactly two incident gates this condition, positivity and p_i+p_j+r=1 are also sufficient. Set the two lambdas by the ratios above. Their sum is<=1, and direct expansion gives D=r/(p_i p_j). Substitution recovers precisely the three probabilities. Thus the positive feasible root laws of this actual two-prime Boolean table are described exactly by this cone. This is not a characterization for three or more gates; higher multiplicative compatibilities remain.

Every such matrix gives rational linear cuts, for every rational t>=0:

    t^2 p_i+p_j-4(t+1)^2 r >=0.

This is its quadratic form on (t,-1). The t=1 cut gives p_i+p_j>=16r, and normalization gives the sharp r<=1/17 for two gates. Asymmetric cuts retain information the scalar cap loses.

The rational point (p_i,p_j,r)=(2/3,5/18,1/18) has total mass1, all coordinates positive, r<1/17, and both individual conditional bounds p_i>4r, p_j>4r. It obeys every sharp individual root-subset cap of this two-gate table. Nevertheless its recovered weights are (4/5,1/3), with sum17/15>1. The determinant is -2/81, and the t=1/2 cut has value -1/18. This is an exact falsifier of the sufficiency of separate caps, including those strengthened by individual lambda<=1 bounds. It is NOT a Boolean spectral law or an FEI counterexample: it is an inadmissible root law for an actual Boolean prime table.

## First unsupported line

The unpaid universal step is still an influence-paid complete same-reference partition cost for arbitrary Boolean prime tables. Even on arbitrary positive edge DNFs no such all-dimensional payment or growing variational lower bound is established here. Pair cuts can tighten a root-law relaxation, but cannot establish higher-gate realizability. The next action is an exact rational LP with these transferable asymmetric pair cuts on the SAME full shared/leafless coefficients, then price the complete cost separately. No full-FEI constant changes.
