# Rare activation does not repair a shallow product stopping rule

All cubes are uniform, signs are Boolean, and logarithms are base two. Physical product indecomposability means that a sign cannot be written as two nonconstant signs on a partition of its physical variables. No assertion of indecomposability under an invertible linear change of coordinates is made.

1. Let m>=2, d=2^(1-m), N=1/d, and let g be a product of N disjoint point signs p_m(x)=1-2 1[x=0]. For t>=1 controls let A_t be their all-zero indicator, delta=2^(-t), and F=1+A_t(g-1). Put mu=E g=(1-d)^N and a=1-mu, so 0<a<1. The exact influences are delta*d on each core coordinate and delta*a on each control. Thus I(F)=delta[m+t a]. The complete F is physically product indecomposable: fixing any one control to its inactive value makes F identically 1. In any proposed disjoint tensor split, place that control in the first factor. The second factor must then be constant, since the restricted first factor takes only signs and its product with the second factor is identically 1. Every coordinate is relevant by the positive influence formulas, so a split into two nonconstant factors is impossible.

2. The Fourier coefficients of g are all nonzero (the point empty coefficient 1-d is positive and all its other coefficients equal -d). For every nonempty core subset S and every control subset T, Fhat(S,T)=delta*ghat(S). For empty S and nonempty T it is -delta*a, while Fhat(empty,empty)=1-delta*a. The convention uses zero as the active control value, whose character is +1; other activation vertices only alter signs. Consequently F has FULL Fourier support. These are actual Boolean functions, with no relaxed probability spectrum involved.

3. Consider ANY finite adaptive fair physical tree of the following class. It reveals controls first until either an inactive bit is seen (constant terminal) or all t active bits are seen. On the active branch it queries arbitrary core coordinates, with decisions depending on all previously revealed outcomes, but reveals at most k distinct coordinates in each original point block, where 0<=k<=m-1. It then actually installs the coordinate-marginal product reference at every terminal and stops. Continuing to query irrelevant coordinates does not change the argument. Initial and inherited references may be ANY normalized supporting references. Inherited references need not tensor, and source-zero reference rows are not discarded. The lower bound uses only the actual final reference installed, so it does not assume any hereditary product-transport property.

4. Write r0=m-k. A live point block with r remaining bits has marginal entropy M_r=r h2(2^(1-r)); a killed block is constant and has M=0. Querying a live block gives one constant child and one live r-1 child, each with probability 1/2. Concavity of h2, h2(0)=0, gives h2(z)>=h2(2z)/2 for 0<=z<=1/2. Hence M_r>=M_(r-1)/2 for r>=2; M_1=0 handles the character boundary. Iterating yields

    M_r >= 2^(-(r-r0)) M_r0,  r>=r0.

The right side is harmonic under every legal live-block query above the r0 boundary: its constant child is zero and its live child has twice its value. Sum this harmonic potential over all blocks. Queries in any other block leave a given summand unchanged. Finite fair-tree induction, with BOTH children retained, now gives on the active branch

    E M_terminal >= N*2^(-k)*(m-k)*h2(2^k*d).

This is SHARP: expose exactly k bits in each live original block, stopping a block once it is killed, then install the product reference. No numerical limit, interchanged infinite sum, or unbounded optional stopping is used. Each tree is finite. A witness tree may depend on m,t,k; the lower bound holds for every tree of the stated class.

5. At an actual marginal-product terminal, its FULL H+KL is exactly M, including deterministic spectral coordinates by their usual zero-term convention. Thus any account paying both full terminals and all nonnegative actual outcome losses, without outside infusions, has ORIGINAL capital at least

    B_mtk = delta*N*2^(-k)*(m-k)*h2(2^k*d)
          >= delta*(m-k)*(m-k-1).

The last step retains the positive -z log2 z term in h2(z), with z=2^(1-(m-k)) in (0,1]. In particular

    Capital/I(F) >= (m-k)(m-k-1)/(m+t).

Past paid bills remain spent and only strengthen the necessary original capital. Negative SIGNED erasure/reference-difference terms are NOT being added as nonnegative losses; they cannot invalidate this lower bound on an account explicitly required to pay the full terminal H+KL and actual nonnegative outcome bills. A different accounting specification must say which terminal obligation it removes or pays elsewhere. This is a bound on TOTAL required original funding, not automatically the additional positive reserve over an already booked inherited KL.

6. For even m, t=m, k=m/2, the activation has probability 2^(-m) and every rule in the class satisfies Capital/I(F)>=(m-2)/8. This diverges even though the source has full Fourier support and is physically tensor prime, and even though rules may adapt freely after activation within the per-block exposure cap. More generally, k<=alpha*m and t<=beta*m, for fixed alpha<1 and beta finite, give linear growth. Thus a policy that hopes to reset EVERY such shallow cut cannot escape the original obstruction merely by excluding physically decomposable roots or by inserting rare controls. This still does not rule out a selected deeper rule or a nonproduct terminal class.

7. These sources do not disprove FEI. An explicit bound is H(F)<=(4+6/m) I(F)<=7 I(F). For a point block,

    H(p_m)=A(d)+2(m-1)(2d-d^2),
    A(x)=-2(1-x)^2 log2(1-x)<=2x/ln2<3x.

Therefore H(g)<4m. The exact activated entropy is

    H(F)=A(delta*a)+delta H(g)-delta*phi(mu^2)
          +2t delta(1-mu^2)+(2^t-1)phi(delta^2*a^2),
    phi(x)=-x log2 x.

Using 1-mu^2+a^2=2a, dropping the nonpositive -delta*phi(mu^2), and keeping the signs of every remaining term gives

    H(F)<=delta H(g)+4t delta a
              +2delta*a^2 log2(1/a)+A(delta*a)
          <=4I(F)+4delta*a/ln2
          <4I(F)+6delta*a <=(4+6/m) I(F).

Here -a ln a<=1, A(x)<=2x/ln2, ln2>2/3, and I(F)>=delta*m are used on their full declared domains. The coefficient (1-delta) in the control-only log term is at most 1, and the omitted -2t delta^2 a^2 term is nonpositive. Thus no small-activation logarithm is lost. Cases k=m-1 (zero lower bound) and m=2 are included; k=m is intentionally excluded from the displayed h2(2^k d) expression because its argument would exceed 1. The rule revealing every bit resolves F at zero terminal entropy and is outside the shallow class.

8. Source-bound audit: A087 PROOF section 4 correctly identifies each full product terminal as M(g), independently of the incoming reference; this mathematical step is reconstructed without repair. Its hereditary GU conclusion is not being extended to the activated roots here. The source's all-reference immediate-cut corollary is accepted at this stated scope; new adaptive/activation statements await A087/A094 independent review. Physical tensor primeness is weaker than affine primeness. No affine-prime claim or universal original-owner supplier follows.

9. Expected unpaid cost can grow in absolute units, not only relative to influence. Replace N by L/d for any positive integer L, retaining ONE shared activation gate over all blocks. The root stays physically tensor prime with full support. The same proof gives I(F)=delta[Lm+t a_L], a_L=1-(1-d)^(L/d), and terminal bill at least delta*L*(m-k)*(m-k-1). Given any fixed C>=0, choose even m>8C+2, t=m, k=m/2 and let L grow. With r=m/2 the unpaid terminal bill after allocating C I(F) is at least

    delta*[L*(r(r-1)-C*m)-C*m] -> infinity.

The positive linear coefficient follows from m>8C+2 (in fact m>4C+2 suffices). This is a family of the prescribed adaptive paths inside physically tensor-prime sources, not disjoint copies of already accounted histories with a silently tensorized inherited reference. Its actual entropy still obeys H(F)<=(4+6/(Lm))I(F)<=7I(F), by section 7 with H(g)<4Lm. No arbitrary incoming reference assumption can eliminate an explicitly required full marginal-product terminal bill.

First unpaid universal line: choose a sufficient nonproduct or sufficiently deep physical terminal/reference rule for an arbitrary Boolean core and fund its FULL initial and terminal costs from actual unused original O(I) capital. This stage supplies a quantitative adversarial admission test for a proposed rule, not that supplier. Full FEI remains OPEN.
