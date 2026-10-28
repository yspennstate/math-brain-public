# Exact Booleanity cannot be replaced by uniform approximate Booleanity

All logarithms are base two. The new family below is REAL, not Boolean. Its energy is J(g)=sum |S| ghat(S)^2, not change-indicator influence. It is a guard against a proposed relaxation of the original-source problem, not a counterexample to FEI. No novelty priority is claimed.

## 1. Independent reconstruction of A070's boundary

For real g and a supplied probability reference R dominating its squared Fourier support, use HOMOGENEOUS squared spectra at physical children. Write B(g,R)=sum ghat(S)^2 log(1/R(S)). Under a physical query i both child references are R'(T)=R(T)+R(T+i), and the mean child squared mass at T is ghat(T)^2+ghat(T+i)^2. Thus

 D_i=B(g,R)-mean B(g_+,R')=
 sum_T [ghat(T)^2 log(R'(T)/R(T))+ghat(T+i)^2 log(R'(T)/R(T+i))]>=0.

Zero actual mass terms are omitted. Support domination is hereditary, since positive child mass implies some positive parent coefficient in that fiber. At full physical exposure the only reference atom is one, so terminal B is zero even when g at that input is not plus or minus one. Energy satisfies J=j_i+mean J(children). Hence for every complete adaptive tree with original physical reach weights w,

 sum wD=B, sum wj=J, V=sum w(D-4j)_+=B-sum w min(D,4j)>=B-4J.

Independently chosen initial seeds are allowed by conditioning on the seed and averaging its original law. Every physical child and constant-output continuation remains. Root norm one permits Gibbs B>=H(ghat^2). It does NOT permit separately normalizing children. For g=(2+x+2y)/3 the root spectrum is (4,1,4,0)/9. After x the child spectra are (1,4/9) and (1/9,4/9). Their separate normalized mean is (29/65,36/65), different from the root erasure (5/9,4/9). This checks A070's exact failure line. For g_n=sum x_i/sqrt(n), H=log n and J=1, so V>=log n-4 for all sources and trees. These reconstruct A070-HOMOGENEOUS-SOURCE-BOOLEAN-BOUNDARY@1 unchanged; no repair is supplied.

For completeness, take q=1/4096 and R=(4(1-q)/5,(1-q)/5,q/2,q/2) in mask order empty,x,y,xy. The homogeneous decrement is D_hom=(5/9)h2(1/5)+4/9, in (0,1]. Separate child normalization changes the first erased mass by 5/9-29/65=64/585 and the other by its negative. Therefore D_norm=D_hom-(64/585)log2(4095)<0: log2(4095)>11 and 64*11>585. The entropy upper bound h2<=1 follows by Gibbs against a fair bit. This reconstructs the strict sign without floating logarithms.

## 2. Bounded rational product family

Let m>=2 be even, n=m^2, p=1/(n+1), r=1-2p, and use n fresh sign coordinates y_j. Set

 U_n(y)=product_j (m+i*y_j)/(sqrt(m^2+1)), h_n(y)=Im U_n(y).

Every factor has modulus one, so |h_n(y)|<=1 at EVERY input. Expansion gives, for odd s=|S|,

 hhat_n(S)=(-1)^((s-1)/2) m^(n-s)/(n+1)^(n/2),

and zero for even s. All coefficients are rational because n is even. Squared mass at each odd S is w_s=p^s(1-p)^(n-s). Consequently

 A_n=E h_n^2=(1-r^n)/2,
 J(h_n)=sum_s odd s binom(n,s)w_s=np(1+r^(n-1))/2<=1.

The second identity follows by differentiating [(1-p+p*z)^n-(1-p-p*z)^n]/2 at z=1. It is a finite polynomial identity, so no convergence interchange is involved. Also A_n>1/3: r^(-n)=(1+2/(n-1))^n>=1+2n/(n-1)>3 by the binomial theorem. Each occupied w_s<=p for s>=1, since p<=1 and (1-p)<=1. Therefore the homogeneous spectral entropy satisfies

 sum_S hhat_n(S)^2 log(1/hhat_n(S)^2)>=A_n log(n+1).

## 3. Uniformly near a Boolean dictator

Add a fresh x0 and choose 0<epsilon<1. Put Z=1+epsilon^2 A_n and

 g_n,epsilon(x0,y)=(x0+epsilon*h_n(y))/sqrt(Z).

The two summands have disjoint Fourier supports: {x0} and nonempty odd y sets. Thus g has squared norm exactly one. Its squared spectral law has mass 1/Z at {x0}, and epsilon^2 w_s/Z at every odd y-set S. In particular

 J(g)=(1+epsilon^2 J(h_n))/Z<=1+epsilon^2,
 H(g)>=epsilon^2 A_n log(n+1)/Z,
 H(g)/J(g)>epsilon^2 log(n+1)/(3(1+epsilon^2)).             (1)

For the entropy lower bound, every odd-cell mass is at most p, since epsilon^2/Z<1. Its logarithm is at least log(n+1); the distinguished atom contributes nonnegative entropy. No logarithm of a zero mass is used.

At each physical input |h|<=1 gives

 sign(g)=x0,
 |g-x0|<epsilon+epsilon^2/2,
 |g^2-1|<=2epsilon+epsilon^2.                            (2)

Indeed 1-1/sqrt(Z)<= (Z-1)/2 and epsilon/sqrt(Z)<=epsilon. For the last bound, (1-epsilon)^2/Z<=g^2<=(1+epsilon)^2/Z, and subtracting one gives the claimed two-sided estimate. The sign is exact because epsilon<1. Every actual physical restriction g_alpha therefore satisfies the SAME uniform squared-norm bound

 |E g_alpha^2-1|<=2epsilon+epsilon^2.                    (3)

This includes all adaptive prefixes, full singleton restrictions, and both outcomes; there is no change of measure or renormalization. Pointwise bound (2) also implies that every signed Fourier convolution residual is at most 2epsilon+epsilon^2 in absolute value, and their sum of squares is at most (2epsilon+epsilon^2)^2, by Fourier inversion and Parseval applied to g^2-1. The empty residual is exactly zero at the root.

Take k>=2, epsilon=1/k, n=2^(2*k^4), m=2^(k^4). These satisfy all parity and nonzero-denominator hypotheses. By (1),

 H(g)/J(g)> 2*k^2/[3(1+1/k^2)] -> infinity,

while the uniform deviations in (2)-(3) go to zero. For ANY fixed tolerance tau>0, first take k sufficiently large so 2/k+1/k^2<tau; arbitrarily larger k preserve the tolerance and yield unbounded H/J. The sign-rounded ACTUAL Boolean functions are exactly x0 with H=0 and I=1. Thus these are not Boolean FEI counterexamples, and the energy J must never be called their change-indicator influence.

## 4. Consequence for original-source encoding

By Section 1, for EVERY normalized support-dominating original reference and EVERY complete adaptive physical tree, homogeneous positive invoice V/J>=H/J-4. The family of Section 3 makes this diverge even under any fixed positive tolerance in (2) or (3). Therefore no finite source-payment constant depending only on such a positive tolerance exists. Equivalently no complete reference with CE<=K(tau)J can cover this relaxed family. This is stronger than the normalized degree-one guard: these real functions are uniformly bounded, uniformly approach a Boolean dictator, have uniformly nearly unit norms at EVERY physical restriction, and satisfy uniformly small full convolution residuals.

The result does NOT rule out bounds with an explicit dimension/error penalty, exact Booleanity, or a Boolean-specific original source. Percolation Lemma 2.1 is a valid complete encoding for arbitrary random sets; what it lacks universally is an influence-priced expected occupancy bill. Approximate normalization and approximate signed cancellation do not supply that bill, even in the stronger uniform sense above. Exact Boolean relations or another hypothesis that excludes this family must enter an original-source construction.

## 5. What remains unpaid

The first unsupported Boolean line is still an ORIGINAL influence-priced support-dominating reference or a selected complete-tree supersolution for arbitrary indecomposable Boolean cores. Existing unused owners, old debits, and both full terminals must remain. This stage closes a relaxation of that line, not the line itself. The shortest next mathematical action is to use the exact pointwise relation f^2=1 to price a necessary local source update; a norm-tolerance or residual-tolerance substitute cannot be uniform.
