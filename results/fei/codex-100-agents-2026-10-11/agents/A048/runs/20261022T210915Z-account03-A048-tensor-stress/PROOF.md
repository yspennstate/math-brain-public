# Exact canonical payment, tensor copies, and sparse activation

All cubes are finite and uniform. Functions take values in {-1,1}; entropy, cross-entropy and KL use bits. This is a scoped fixed-reference payment result. Full FEI remains OPEN.

## 1. Independent reconstruction of A050 v1

The reviewed source is A050-NONPOINT-CANONICAL-GAP-REPAIR@1, statement hash 2eb7d96d75bfa2553f61bb8773d9b73f0232a8c0ae4c62edd7e5204831d72689, run 20261021T171109Z-account03-A050-repair-with-scope. The following reconstruction does not alter its hypotheses.

At a physical coordinate query let p(s),q(s) be source and reference probabilities. Erasing the coordinate gives p_e(w),q_e(w). The actual coherent channel is K(b|w), with fair fallback when p_e(w)=0. The branch source probability is 1/2. Reference branch probability is q_b=sum_w q_e(w)K(b|w), and the inherited reference is q_e(w)K(b|w)/q_b. For every source-positive atom and positive channel entry, the product of its conditional erasure likelihood, branch likelihood (1/2)/q_b, and inherited child likelihood is exactly p(s)/q(s). This proves the KL chain by summing logarithms. Source-zero/reference-positive rows stay in q_e,q_b and the inherited laws. Induction proves the chain for any finite adaptive fresh-coordinate tree. No reference is renewed.

Put A=KL(P_root||Q), H0=H(root), Hf=E H(leaf), R=I(root)-E I(leaf), D=H0-Hf, S=E(4I(leaf)-H(leaf)). The whole conservative liability is L=A+[D-4R]_+. It contains the complete source KL, including all its eventual erasure/outcome and terminal pieces; these pieces are not added to A again. The exact scalar identity is

    L=max(CE-H0, CE-Hf-4R).

Hence H0,Hf>=2 and CE<=M imply L<=M-2. If the actual certified terminal owner S is unused and L<=S, then

    4I(root)-CE = S-(A+D-4R) >= S-L >=0.

Already booked conservative overpayment omega must additionally be charged once. The theorem supplies no earlier ancestor funding.

For A050's root F_h, take x,a,b as 0/1 coordinate names:

    F_h=(-1)^a on x=0; h(z) on x=b=1; +1 otherwise.

Write t=Pr(h=-1), d_j=Inf_j(h), p0=(1-t)^2/4, v=1-p0. Its exact Fourier marginals are d=(1/2,1/2,t/2,d_j/4). Delete dummies. All r_i=d_i/v belong to (0,1), and sum r_i>1, since the xa coefficient has squared mass 1/4 at degree two. The polynomial

    phi(c)=[1-product_i(1-c r_i)]/c
          =sum_i r_i product_{j<i}(1-c r_j)

extends continuously at zero, is strictly decreasing on [0,1], has phi(0)>1 and phi(1)<1. Strict decrease follows already from the second positive summand; every other summand is nonincreasing and all factors are positive. Thus precisely one c in (0,1) satisfies phi(c)=1. No square-sum condition is needed.

The canonical complete law is Q(empty)=p0 and Q(s)=(v/c) product_i(c r_i)^{s_i}(1-c r_i)^{1-s_i} for s nonempty. Normalization and matched marginals follow from 1-product_i(1-c r_i)=c. On nonempty sets log Q is affine in the membership indicators, so CE(P,Q)=H(Q). Entropy subadditivity gives CE<=2+G(h), where G=h2(t/2)+sum_j h2(d_j/4).

After b first, allow arbitrary finite adaptive fresh data-only stopping in b=1; retain b=0, x and a. Each terminal with core g has H=2+H(g)/2 and I=1+I(g)/2. A supplied actual certificate H(g)<=4I(g) gives S>=2. Root coefficients all have absolute value <=1/2, so H0>=2, and all terminal entropies are >=2. This proves A050's conditional payment when G<2.

For a k-bit point defect with epsilon=2^-k, I=2k epsilon, nonempty spectral entropy=8(k-1)epsilon(1-epsilon), and empty contribution <=4epsilon(1-epsilon)/ln 2. The last inequality follows from -u ln u<=1-u applied at u=(1-2epsilon)^2. Since ln 2>1/2, H<=4I for k>=2; k=0,1 are constant or character. Disjoint products add H and I and every restriction remains such a product up to sign. For m width-r factors, t=[1-(1-2^(1-r))^m]/2 and d_j=2^(1-r). When r>=8 and 2<=m<=r, monotonicity of h2 below 1/2 and h2(u)<=u log2(e/u), log2(e)<3/2, give

    G < m(r+1)(r+5/2)/2^(r+1) <=189/128.

The envelope decreases for r>=8 because its successive ratio is (r+2)(r+7/2)/(2r(r+5/2))<1, equivalent to r^2-r/2-7>0. Thus the same unused terminal owner >=2 pays the source's stated liability and leaves >67/128. First-data children are both nonconstant for m,r>=2. This independently reconstructs the reviewed theorem. Its arbitrary-core, mixed-query and fresh-reset exclusions remain essential.

## 2. Sharper eligibility without renewing the reference

Keep exactly the same root, reference, tree and terminal certificates. The first b query removes influence t/2, so R>=t/2 on every allowed continuation. The exact identity above now gives

    L <= max(CE-H0, CE-2-2t)
       = CE-min(H0,2+2t).                              (1)

Therefore CE-min(H0,2+2t)+omega<2 suffices to pay from the same owner >=2, after the old conservative overpayment omega. This uses an already executed edge, not a second influence allowance. No data-query energy is separately credited in (1). All actual data descendants and their full inherited references remain included. A simpler sufficient condition is CE<4 when omega=0; the exact floor in (1) can be stronger.

All terms are computable without enumerating the full cube. Let h be the product of m width-r point defects, mu=(1-2^(1-r))^m, t=(1-mu)/2 and Hh=m H(defect_r). With e(u)=-u log2 u, e(0)=0, put g_b=1 on b=0 and h on b=1. Its nonempty data coefficients are hhat(S)/2 at both b labels, while its empty and b coefficients are 1-t and -t. Thus

    H(g)=e((1-t)^2)+e(t^2)+(Hh-e(mu^2))/2+1-mu^2,
    H0=2+H(g)/2.

The exact canonical entropy is

    CE=h2(p0)+v[log2 c
       -sum_i {r_i log2(c r_i)+(1-r_i)log2(1-c r_i)}]. (2)

The sum counts actual coordinate multiplicities. Every logarithm has a positive argument because c,r_i are in (0,1). Rational polynomial signs bracket c; monotone logarithm intervals enclose (2). The selected (m,r)=(3,5) core has 15 data coordinates and 18 total coordinates. Its certified G>2 is outside A050's G<2 test. Its certified bound in (1) is <2. The exact rational interval receipts, rather than a floating value, determine these signs. It follows that the SAME canonical source, including all terminal KL, is paid through every allowed data-only adaptive stopping continuation. This is a narrow extension of the existing criterion, not a new universal potential.

The hereditary leaf certificates hold in all dimensions by the restriction argument in section 1. The 343-state finite replay checks the small and boundary states of the selected three width-five blocks, including a killed block, a constant negative block, and characters. It is not the proof for arbitrary histories. No conclusion about querying x/a, other mixed histories, fresh references, or pre-spent terminal capacity follows.

## 3. Tensor and sparse-activation stress of the funded account

For independent identical copies with product reference, H, I, CE and KL add exactly. Under identical factorwise stopping partitions, D and R also add, so L_T=T L and S_T=T S. For different independent partitions, [sum e_j]_+<=sum[e_j]_+ gives L_total<=sum L_j. There is no T log T term, and no spectator entropy is silently removed. The assertion concerns product references and stated physical partitions, not a fresh whole-product canonical projection.

An independent common unqueried spectator s gives D'=D, R'=R, A'=A+KL(P_s||Q_s), hence exactly L'=L+KL(P_s||Q_s). Its retained owner changes by 4I(s)-H(s), and its entire terminal entropy/reference bill remains. If Q_s=P_s then L is invariant. Any claimed extra credit must be an actual unused certificate for that spectator; a new full-product canonical projection is a reference reset requiring a separate price. This is the precise irrelevant-factor test for the complete signed account.

There is also an arbitrarily sparse physical lift. For a funded seed f=F_h and its original Q, take T independent copies, a fresh balanced retained sign z, and k fair point-activation controls C. Put alpha=2^-k and

    W=1+AND_k(C)(z product_{j=1}^T f_j-1).

The quotient W0=1+AND_k(C)(z-1) is a (k+1)-bit point defect up to bit complements. The normalized reference lift uses the ACTUAL quotient spectrum and Q^tensor T on the active spectral sector; on the inactive sector it uses the forced empty seed label. Direct Fourier expansion, as in the prior A048 activation audit, gives

    H(W)=H(W0)+alpha T H(f),
    I(W)=alpha(k+1+T I(f)),
    CE(W,Q_W)=H(W0)+alpha T CE(f,Q),
    KL(W||Q_W)=alpha T KL(f||Q).

After all controls, the inactive branch is constant and the active branch has the retained z-character and the factorwise physical cores. The inherited reference is the complete law produced by the stated actual channel; it need not remain a product on source-zero/reference-positive rows. The total initial KL is alpha*T*A and its full erasure/outcome/terminal decomposition is retained. For identical factorwise stopping partitions the total signed edge is H(W0)-4alpha*k+alpha*T*(D-4R). The final actual owner is 4alpha+alpha*T*S. Because H(W0)<=4alpha*(k+1), positive-part subadditivity gives the whole outer liability at most 4alpha+alpha*T*L. Pay the controller portion only from the guard's 4alpha owner and the factor portions only from their alpha-scaled original owners. This pays the single complete source account without assuming zero controller KL release, product terminal references, or any renewed bank; all inactive/active terminals remain.

In particular, a certified seed CE<=4I-margin gives

    CE(W,Q_W)<=4I(W)-alpha T margin.

Independent-copy bills scale linearly before sparse reach weighting, and exactly by alpha afterward. Choosing k=ceil(2 log2(T+1)) sends total influence and minority probability to zero for the fixed supplied seed. This is a paid scoped family, not a universal FEI conclusion; the earlier arbitrary-seed version remains FEI-complete because it lacks the seed payment.

## 4. Verification boundary and universal gap

The independent checker uses integer Walsh transforms and direct pivotal edges on small actual Boolean cubes, rational normalized perturbation references for physical transport replay, and atomwise likelihood product identities. A rational perturbation is never called the algebraic canonical law. The canonical signs use separate exact root brackets and logarithm bounds. Logs use 40 terms of the positive atanh series after range reduction, with the explicit tail 2 z^81/[81(1-z^2)], z in [0,1/3]; division by a positive rational enclosure of ln 2 and every interval operation round outward to multiples of 2^-96. No floating sign decides a claim. Lean checks, if available, certify only the scalar statement recorded in their own receipt.

FIRST UNPAID UNIVERSAL STEP: supply, for an arbitrary core and a useful selected mixed physical query or prescribed reset, genuinely unused certified terminal surplus dominating the complete inherited CE/source liability after old bookings. Exact canonical pricing does not prove such a surplus exists; canonical full-source prices are themselves obstructed on other Boolean families. C018 and full FEI have no improved universal constant here. The useful advance is independent acceptance of an existing repair plus exact eligibility and transparent tensor/sparse transport of one newly admitted complete account.
