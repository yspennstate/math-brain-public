# Terminal-inclusive phase-comb repair

Author reconstruction, pending independent review. Bits throughout. This is a narrow extension of A011's existing comb interface, not universal FEI.

Let a>=1. Uniform physical selectors x_1,...,x_a stop at the first +1; stopping leaf j has probability w_j=2^-j, and terminal leaf a+1 has w_(a+1)=2^-a. All actual Boolean leaves g_j use the SAME uniform data cube, with arbitrary repetitions. Assume their squared Fourier coefficients agree at EVERY data set T:

    g_jhat(T)^2 = P(T), for every j,T.

There is no disjointness assumption between leaf data supports. Translates and sign changes of an arbitrary fixed Boolean core h satisfy this admission. The admission also allows any other actual Boolean functions with the same Fourier magnitudes, without needing a translation representation.

Fix one full subprobability reference R on data subsets, positive on true P-support. Write c=CE(P,R), and let F be the physical comb of the g_j. There is a complete fixed root reference Q with

    CE(P_F,Q) = c + sum_T P(T) H(sigma_T)
              <= c + C_* I_sel(F),
    C_*=4+2/(e ln 2)<41/8,
    I_data(F)=I(g_1),
    CE(P_F,Q)-H(F)=c-H(g_1).

Here sigma_T is the Boolean SIGN comb whose leaf labels are g_jhat(T)/sqrt(P(T)). No arbitrary core cost is removed: a supplied c<=K I(g_1) gives ideal full cost <=max(K,C_*) I(F). A single ordinary Shannon output word has expected length <CE+1; the additive one is retained. If the core is balanced, I(g_1)>=1 pays that rounding, yielding (max(K,C_*)+1)I(F). No dimension-independent influence payment for that integer rounding is asserted for arbitrary biased cores.

## 1. Scalar Boolean sign-comb lemma, proved here

Fix labels sigma_1,...,sigma_(a+1) in {-1,1}. Let m_(a+1)=sigma_(a+1), m_j=(sigma_j+m_(j+1))/2, r_j=(1-sigma_j m_(j+1))/2. Thus 0<=r_j<=1. The scalar comb b has mean m_1. For nonempty selector U with max U=j,

    bhat(U)=2^(1-j) sigma_j r_j (-1)^(|U|-1).

This follows by expanding the first-positive indicators, or by recursion b=(sigma_1+h)/2+x_1(sigma_1-h)/2. There are 2^(j-1) predecessor subsets. Their total mass is v_j=2^(1-j)r_j^2. Hence

    V=sum_j v_j=1-m_1^2,
    I(b)=sum_j 2^(1-j)r_j = (1/2)sum_j (j+1)v_j.

The physical identity conditions on reaching coordinate j, probability 2^(1-j); the branch-label disagreement is exactly r_j. The spectral identity averages |U| over the uniform predecessor subsets, giving (j+1)/2. In particular no independence between different leaf labels is used.

Put L(t)=t log2(1/t), with L(0)=0. Full entropy, including the empty selector atom, is

    H(b)=L(m_1^2)+sum_j v_j[2(j-1)+2log2(1/r_j)].

Zero r_j terms are omitted. Since L(1-V)<=V/ln2<2V,

    H(b) <= 4 I(b)-2V + 2 sum_j 2^(1-j)r_j^2 log2(1/r_j)
         <= [4+2/(e ln2)] I(b)-2V
         <= C_* I(b).

The first equality used in this bound is sum 2(j-1)v_j=4I(b)-4V. The scalar bound r log2(1/r)<=1/(e ln2) follows by differentiating -r ln r on [0,1]. The elementary estimates e>8/3 and ln2>2/3 give C_*<41/8: the former follows from the first five exponential series terms, the latter from ln2=2 sum_(k>=0)(1/3)^(2k+1)/(2k+1)>2/3. The L estimate is -t ln t<=1-t for t in [0,1], including its continuous endpoint. This proves all lengths and all label strings; finite computation is a check, not extrapolation.

## 2. Exact common-magnitude conditional rows

For P(T)>0 define beta_T=sqrt(P(T)) and labels sigma_j(T)=g_jhat(T)/beta_T in {-1,1}. The data Fourier coefficient of F at a physical selector input x is beta_T sigma_T(x). Taking the selector transform gives

    Fhat(U,T)=beta_T sigma_That(U),
    P_F(U,T)=P(T) K_T(U),   K_T(U)=sigma_That(U)^2.

Every K_T is a normalized probability law, including all empty selector atoms. At zero P(T), set K_T to the point mass on the empty selector set. Define

    Q(U,T)=R(T) K_T(U).

All masses and kernels are determined from the finite physical tree and fixed terminal reference before sampling. Sum Q=sum R<=1, including reference mass on zero true fibers; any deficient mass is a failure atom. True support positivity holds. The generator first uses R to choose a data set or failure, then uses its fixed phase-comb spectrum to choose U. Its joint description cost includes the conditional max-index labels, predecessor subset choices, zero-selector atoms, and the full c.

Chain rule gives the displayed exact CE and entropy identities, with c-H(g_1) retained as the complete reference deficit. Spectral influence gives I_sel=sum_T P(T)I(sigma_T) and I_data=sum_T |T|P(T)=I(g_1); direct physical conditioning gives the same data identity. The scalar lemma now pays the entire extra selector cost without charging core influence. No free physical-leaf posterior entropy is subtracted from a transmitted leaf word.

This is exactly the same Boolean-phase row admission used by A019's product/star translation interfaces. The distinct addition is a stopped decision-list phase law, with arbitrary repeated labels, arbitrary same-magnitude leaves, and a prescribed complete core reference. It is not a new proof of A019's product/star theorem or A097's general compatible-reference telescope.

## 3. The general shared-data comb and the exact missing line

For arbitrary Boolean leaves, define suffix means h_(a+1)=g_(a+1), h_j=(g_j+h_(j+1))/2, pointwise on the data cube. Let Delta_j=g_j-h_(j+1). For nonempty selector U with max U=j,

    Fhat(U,T)=2^-j (-1)^(|U|-1) Delta_jhat(T),
    Fhat(empty,T)=h_1hat(T).

Thus the max-index group has mass 2^(-j-1)||Delta_j||_2^2. These residuals are real functions, generally not Boolean. The data marginal is exactly

    q(T)=sum_j w_j g_jhat(T)^2.

It follows by Parseval on selector inputs, not by an unsigned approximation to F. For arbitrary complete leaf references R_j define r(T)=sum_j w_j R_j(T), the actual conditional selector kernel K(U|T)=P_F(U,T)/q(T), and Q(U,T)=r(T)K(U|T), choosing a normalized kernel at zero true q. This is complete, and

    CE(P_F,Q)=H(U|T)+sum_j w_j c_j+JS- kappa,
    JS=H(q)-sum_j w_j H(P_j),
    kappa=sum_T q(T) KL(k_P(j|T)||k_R(j|T)),
    k_P(j|T)=w_j P_j(T)/q(T),
    k_R(j|T)=w_j R_j(T)/r(T).

The exact terminal deficit identity is sum_j w_j KL(P_j||R_j)=KL(q||r)+kappa. It conserves all subprobability normalizers. This is the whole-comb specialization of A097's already established general transfer, not a new universal bridge claim. Choosing exact terminal spectra sets kappa=0; that choice does not pay H(U|T).

The common-magnitude hypothesis makes q=P, JS=0 and, with the same R at every leaf, kappa=0. It also makes every normalized coefficient row Boolean, so section 1 gives the missing conditional entropy payment. Without admission, rows g_jhat(T)/sqrt(q(T)) are real with varying magnitudes. The FIRST unsupported line is that one can select a universal cover or allocate one nonreused magnitude-change reserve that restores this Boolean-phase payment with all terminal costs. Applying the scalar lemma to those real rows is invalid. Merely asserting this payment for arbitrary selectors is FEI strength: take g_j to be +/- a dictator, and replace the comb by an arbitrary Boolean label selector b, obtaining F=b(x)y and H(F)=H(b).

## 4. Guards and scope

A prescribed arbitrary Boolean core h is still arbitrary: repeated copies/tensor powers retain c_h or t c_h and I(h) or t I(h). The transfer does not supply c_h<=K I(h). Constant cores are allowed; when all leaves are constants the theorem reduces to the proved scalar comb bound. Arbitrary nonempty Fourier supports and the empty data set are included. Core translations can share every physical coordinate. Selector coordinates are fresh and tested once in the same fixed order. Reusing a selector inside a leaf is outside the stated admission and requires actual restriction first.

The shortest next step is to vary the magnitudes in just one stopping leaf, compute the exact JS/kappa and full conditional core bill, and seek a one-use correction paid from a source-compatible reserve. Adding more identical-magnitude translations would preserve the same unpaid universal admission.
