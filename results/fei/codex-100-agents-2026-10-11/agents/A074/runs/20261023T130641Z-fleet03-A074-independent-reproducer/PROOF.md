# Independent review: signed composition drift and the unpaid initial bank

Full uniform-cube FEI remains OPEN. This review concerns A072-SIGNED-COMPOSITION-DRIFT-COHERENT-ENVELOPE@1, unchanged, not a new FEI theorem. Entropy is in bits. Constants, zero influences, both complete physical children, and original dummy coordinates are retained throughout.

## Independent reconstruction of the entropy identity

For a sign-valued u, split the physical Fourier index according to its queried bit i. Write coefficients a_L=uhat(L), b_L=uhat(L union {i}), where i is absent from L. The probability law of the full Fourier index has masses a_L^2 and b_L^2. Projecting away i produces law s_L=a_L^2+b_L^2. Its conditional entropy is B=sum Phi(a_L^2,b_L^2), with Phi(A,B)=(A+B)log2(A+B)-Alog2 A-Blog2 B. Thus H(u)=H(s)+B. Independently the two complete child spectra are (a_L+b_L)^2 and (a_L-b_L)^2. Their average is s. Defining J=H(s)-mean H(children) gives H(u)-mean H(children)=B+J. Concavity gives J>=0. In particular, the sign of J is positive.

Here is an all-dimensional bound, reconstructed rather than inferred from cases. For t>=0, t-ln(1+t^2) has derivative (t-1)^2/(1+t^2)>=0 and value zero at zero. Applying ln(1+t^2)<=t twice gives Phi(x^2,y^2)<=2|xy|/ln2, including zero arguments by continuity. One row's Jensen-Shannon contribution is s G(2ab/s)/ln2, where G(t)=((1+t)ln(1+t)+(1-t)ln(1-t))/2. Both G and 1-sqrt(1-t^2) are even and vanish at zero. On [0,1), G'=atanh(t)<=t/sqrt(1-t^2): differentiate the latter comparison to obtain (1-t^2)^(-1)<=(1-t^2)^(-3/2). Thus the row is at most (s-|a^2-b^2|)/ln2=2min(a^2,b^2)/ln2. Summation proves J<=2 Inf_i(u)/ln2. Endpoint and zero-mass rows follow by continuity, without division by zero.

## Composition, the empty-row exception, and exact drift

Fix a finite gate h and disjoint sign-valued cores g_j. Let q_j be the pivotal probability of input j under the other independent core outputs. Define F=h(g) and C=H(F)-sum q_j H(g_j). For a query i in core j put mu=E g_j, tau=ghat_j({i}), d=Inf_i(g_j). Direct physical edge conditioning gives Inf_i(F)=q_j d and I(F)=sum q_j I(g_j).

Write h(z)=A(z_-j)+z_j D(z_-j). Substitution into the other physical blocks gives F=A(g_-j)+g_j D(g_-j). Orthogonality yields E D(g_-j)^2=q_j. At a nonempty frequency within the queried block, the full coefficient is the inner coefficient times the outside coefficient of D. Every erasure pair whose remaining inner frequency is nonempty therefore factors. The remaining pairs have coefficients Ahat+mu Dhat and tau Dhat. Their erasure entropy sum, denoted B_special, is nonnegative. Homogeneity of Phi and Parseval give exactly

    B_i(F)=q_j[B_i(g_j)-Phi(mu^2,tau^2)]+B_special.

No variances are divided out; constant other cores are included. Under the query q_j is unchanged. For k!=j, q_k is an expectation over g_j's sign, hence affine in its negative probability; the two child negative probabilities average to the original one. Thus mean q_k(child)=q_k(parent), while H(g_k) is unchanged. Subtracting the two entropy decrements therefore gives

    mean C_child-C_parent
      =q_j[Phi(mu^2,tau^2)+J_i(g_j)]-B_special-J_i(F).

The physical Boolean derivative has values -1,0,1. Its signed mean is tau, and its absolute mean equals d, so |tau|<=d. Since |mu|<=1, the preceding bounds prove drift <=(4/ln2)q_j d. Finally ln2=2sum_(k>=0)(1/3)^(2k+1)/(2k+1)>2/3, giving 4/ln2<6. If physical influence is zero the same inequality gives drift<=0, without a special support assumption. This establishes A072's full dimension-independent drift statement.

## Nonnegativity, stopping hulls and historical owners

For kappa=4/ln2 or 6, W=C+kappa I is superharmonic because I(parent)-mean I(children)=Inf_i(F). At complete physical revelation, all functions are constant and W=0. Revealing all remaining original bits and applying finite backward induction proves W>=0 at every state. This argument needs neither a finite census nor an assumed FEI bound.

At fixed K>=0 let rho_j be the true finite stopping hull of (H(g_j)-K I(g_j))_+. These hulls are nonnegative and superharmonic. Under a query in core j, q_j is unchanged and rho_j is superharmonic; every other rho_k is unchanged and q_k has conserved conditional mean. Hence sum q_j rho_j is superharmonic. Consequently A_K=W+sum q_j rho_j is nonnegative and superharmonic. Since rho_j>=H(g_j)-K I(g_j), C+sum q_j rho_j>=H(F)-K I(F). Adding kappa I and using A_K>=0 proves A_K>=(H(F)-K I(F))_+.

If a>=A_K(parent) is supplied, write m=mean A_K(children) and a_b=A_K(child_b)+a-m. Then a-m>=0, both credits are nonnegative and their mean is a. For a>0 the kernel a_b/a propagates each original nonnegative credit-owner label with conserved conditional mean. If a=0, both children and credits vanish, so kernel 1 suffices. Put S=KI-H and d_b=S(child_b)+a_b>=0. Their mean T equals S(parent)+a+e, where e=mean S(children)-S(parent). For T>0, kernel d_b/T transports the old signed debit labels plus the signed query charge e, preserving their separate conditional means and summing to the required child debit. If T=0 then both d_b vanish; kernel 1 retains the signed labels whose total is zero. Both full children and stopped siblings remain present.

This is conditional allocation of already supplied stock. It does not draw from a spent outside owner. The fixed original partition is present from the start, so admissions do not change A_K. A changed partition is outside the claim. The reserve releases kappa Inf_i(F) in mean as potential headroom; the transported labels need not separately equal potential components.

## What remains unsupported

No dimension-independent initial estimate A_K<=L I has been proved. With singleton physical-bit cores, inner entropies and their complete stopping hulls vanish, q_j=Inf_j(F), and C=H(F). Therefore A_K=H(F)+kappa I(F), independently of K. Bounding this bank by a universal multiple of I is precisely an FEI bound. Universal coherence is established, universal initial influence payment remains the first unsupported line. A donor already charged by an earlier history cannot be reused merely because this coherent potential exists.

## Independence and arithmetic of the finite calculation

The fresh reviewer imports no producer script and no previous A074 numerical helper. It constructs literal full physical truth tables and computes each Fourier coefficient by its defining character sum. Inverse characters, Parseval and direct edge disagreements check every spectrum before entropy is used. It constructs outside A and D truth tables independently and compares the exceptional erasure identity as an exact prime-log expression. Stopping hulls use finite backwards recursion on complete restricted inner truth tables. Constants and both terminal outcomes are kept.

Entropy expressions are rational linear combinations of log2(primes), with log2(2)=1. Rational factorization proves exact identities. For strict inequalities, p=2^k y with 1<=y<2 and z=(y-1)/(y+1)<1/3. The 64-term expansion ln y=2sum_(j=0)^63 z^(2j+1)/(2j+1)+tail has 0<=tail<=2z^129/[129(1-z^2)]. The same expansion for ln2, with z=1/3, gives directed rational bounds on log2 p by division. Signed rational coefficients select outward endpoints. There is no floating-point mathematical verdict; elapsed timing alone uses floating point. The witness drift additionally has the integer certificate 7^3087>2^4736*3^2268*5^50.

The frozen finite domain is validation of the implementation and source row, not an exhaustive verification of the universal theorem. The analytic reconstruction above supplies the all-dimensional argument. No substantive repair to the source statement was required; independent acceptance preserves its version, hypotheses and digest. No full FEI claim is made.
