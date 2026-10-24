# Rank-two star L² receiver with arbitrary light-only terms

**Status:** proved scoped analytic theorem and independent-block convolution corollary. The unrestricted QFORM theorem remains open. A hub self-square is outside the theorem.

Let H be a real random variable with probability density f_H bounded by K. Let Y be an arbitrary independent random vector. Assume L=L(Y) has a probability density bounded by M, and let R=R(Y) be **any** measurable real function, finite almost surely. For c≠0 and any deterministic u, put

Z=cH L+uH+R(Y)=cH(L+u/c)+R(Y).

Then Z has an L² density satisfying

||p_Z||_2² <= 4KM/|c|.                                      (1)

There is no assumption that L and R are independent. In particular R may contain arbitrary light-only quadratic interactions and original-coordinate affine terms, of any size or sign. The result also allows arbitrary dependence among the coordinates of Y, as long as the displayed marginal L density cap is established. It does **not** allow a hub self-square aH² or an additional interaction H·T(Y) unless that interaction is absorbed into the single coefficient c(L+u/c).

## Proof

Translate L by u/c, which preserves its density cap, and write the translated variable again as L. Since L has a density, L=0 has probability zero. Conditioning on Y gives the output density

p_Z(s)=E_Y [ f_H((s−R(Y))/(cL(Y))) / (|cL(Y)|) ].

For independent copies Y,Y', square this expression and integrate in s. For fixed values l,l',r,r', the overlap of the two rescaled and shifted hub densities is bounded by

int_R f_H((s−r)/(cl)) f_H((s−r')/(cl')) ds
 <= K min(|cl|,|cl'|).

Indeed either factor is at most K, while integrating the other factor gives |cl| or |cl'| because f_H is a probability density. The shifts r,r' do not enter the bound. Tonelli therefore gives

||p_Z||_2²
 <= (K/|c|) E[1/max(|L|,|L'|)].                            (2)

Since p_L<=M, P(|L|<=x)<=min(1,2Mx). By layer cake,

E[1/max(|L|,|L'|)]
 =int_0^infinity P(|L|<1/t)^2 dt
 <=int_0^{2M}1 dt+int_{2M}^infinity(2M/t)^2dt
 =4M.

This proves (1), without moment or support assumptions.

## Two independent stars

Suppose Z_1,Z_2 are independent variables of this form, with parameters K_j,M_j,c_j and arbitrary light-only R_j. By Cauchy–Schwarz for convolution,

||p_(Z_1+Z_2)||_infinity
 <=||p_(Z_1)||_2 ||p_(Z_2)||_2
 <=4 sqrt(K_1M_1K_2M_2/(|c_1c_2|)).                         (3)

An additional independent summand can be convolved afterward and cannot increase the density cap.

For the previously studied two-star structural family with cross coefficients c_1=4,c_2=2, independent cap-one hubs K_1=K_2=1, and light projection caps M_1=M_2=sqrt(2), equation (3) gives exactly 2. Unlike the earlier pure homogeneous calculation, (3) permits arbitrary within-star light-only quadratic tails and arbitrary light affine terms. Independent original-coordinate affine terms on the hubs are included through u_jH_j.

## Boundary

A hub self-square aH² changes the conditional hub map from linear to quadratic, so the overlap argument above no longer applies. Arbitrary cross terms between the two star blocks also destroy their convolution independence. Neither issue is resolved by (1)–(3). The result pays a broad decomposable arbitrary-rank branch, not the full s3(A)>=1 theorem.
