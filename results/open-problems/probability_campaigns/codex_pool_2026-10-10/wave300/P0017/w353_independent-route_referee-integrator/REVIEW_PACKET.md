# P0017 review packet

Reviewer w353, 2026-10-10. Target status: current primary papers claim the full KLS theorem; their complete proofs are not certified by this packet. A partial obstruction is not a solution of P0017.

## w352 conditional-averaging obstruction: KEEP

Artifact inspected: ~/brain_workers/w352/ATTEMPT.md, the density exp(-x) on x >= |y|^p and all displayed formulas. Scope: the failure of a universal joint-to-marginal Dirichlet-energy bound for conditional expectation. No novelty determination and no parent-problem resolution.

Independent derivation of the load-bearing claim:

1. For p >= 2, |y|^p is convex and the epigraph is convex. The density is exp(-V) with V=x+indicator(epigraph), so it is log-concave and integrable. Integrating x from |y|^p to infinity gives Y density exp(-|y|^p)/Z, Z=2 Gamma(1/p)/p.
2. Under the change r=|y|^p, r has Gamma(a,1) density with a=1/p. The conditional excess E=X-r is Exp(1) independent of Y. Thus EX=1+a, Var X=1+a, EY=0, EY^2=Gamma(3a)/Gamma(a), and Cov(X,Y)=0 by symmetry. All moments used below are finite.
3. Let sigma^2=Gamma(3a)/Gamma(a), U=(X-(1+a))/sqrt(1+a), V=Y/sigma. This invertible affine map preserves log-concavity and makes covariance exactly I_2. For f(u,v)=u, the full gradient energy is 1 and Var f=1.
4. The conditional mean is g(v)=(sigma^p |v|^p-a)/sqrt(1+a), with derivative p sigma^p sign(v)|v|^(p-1)/sqrt(1+a). Therefore its gradient energy equals p^2 sigma^2 E|Y|^(2p-2)/(1+a). Direct substitution in the one-dimensional integral gives E|Y|^(2p-2)=Gamma(2-a)/Gamma(a), hence

       D_p = p^2 Gamma(3/p) Gamma(2-1/p) / [(1+1/p) Gamma(1/p)^2].

5. The elementary identity Gamma(epsilon)=Gamma(1+epsilon)/epsilon and continuity at 1 give Gamma(c/p) ~ p/c. Also Gamma(2-1/p) -> 1. Consequently D_p/p -> 1/3, so D_p diverges. This proves the obstruction analytically. At p=2, Gamma(3/2)=sqrt(pi)/2 gives D_2=2/3 exactly.
6. Var g=Var(r)/(1+a)=a/(1+a)=1/(p+1). The average conditional variance of f is 1/(1+a)=p/(p+1). Their sum is exactly Var f=1. There is no conflict with global KLS.

The claim using only partial_v f in the input fails already at p=2: that derivative is zero, while the output energy is 2/3. The claim using the complete joint gradient has no finite universal operator bound because D_p diverges. The proof does not multiply conditional estimates or assume independence between conditional rows: the independence of the exponential excess follows from the joint density factorization.

Reproduction command: python -X utf8 ~/brain_workers/w353/verify_packet.py. The script independently integrates the original y-density on two meshes rather than merely checking the gamma expression against itself. The final accepted compute-gate receipt and MEASUREMENTS.json will record the measured errors. A preliminary 0.165-second run matched seven p-values to relative error below 1e-14; it lacked a host-resource probe and is not used as the accepted experiment. The script was corrected to enforce a fresh >=2 GiB free-memory and <=80% CPU-busy gate before remeasurement.

Remaining gap: replace the false Sobolev bound by a direct estimate of conditional-mean variance for general functions, or prove a narrower score/transport condition. This artifact establishes neither replacement. Independent mathematical verdict: KEEP the exact obstruction; DROP its use as a refutation of KLS or a solution of the full target.

## w351 L0-L4: KEEP with their stated additional hypotheses

Artifacts: ATTEMPT.md and CLAIMS.jsonl in ~/brain_workers/w351. All five lemmas were read after this worker had recorded its separate Gaussian-posterior route.

L0, affine normalization: KEEP. For positive-definite Sigma, the substitution X=m+Sigma^(1/2)Y has grad_y g=Sigma^(1/2) grad_x f and preserves variance. This gives exactly the covariance-weighted energy, with no claim that the required universal isotropic inequality was proved.

L1, two-block comparison: KEEP. On the centered L2 space, P and Q are orthogonal projections. For a=Pf, b=Qf and S=||a||^2+||b||^2, S=<f,a+b>. The maximal-correlation assumption gives ||a+b||^2<=S+2rho||a||||b||<=(1+rho)S. If S>0, squaring Cauchy-Schwarz and dividing by S gives S<=(1+rho)||f||^2; S=0 is immediate. The sum of conditional variances is 2||f||^2-S, hence at least (1-rho)||f||^2. The integrated coordinate Poincare statement follows when the conditional bounds and slicing hypotheses hold. M_U denotes the bound for the U-gradient slice (conditioning on V), and M_V conversely. Neither linear uncorrelatedness nor ambient isotropy supplies rho<1 with a universal margin.

L2, simplex normalization and fiber constants: KEEP. Write N=n+1. The vertex matrix is sqrt(N(N+1)) P_H and the covariance of uniform Dirichlet barycentric coordinates is P_H/[N(N+1)]. Their composition gives Cov_H(X)=I_H. The edge length squared is L^2=2N(N+1). The projection kernel fixes all barycentric coordinates except the pair alpha_0,alpha_1, whose sum S is fixed. Constant barycentric density and constant linear coarea Jacobian leave a uniform line interval of length LS. Its variance is L^2 S^2/12 and its Poincare constant is L^2 S^2/pi^2. The Neumann sine mode on the centered interval attains the latter. The density of S~Beta(2,N-2) is positive on (0,1), so these essential suprema are achieved as limits on positive-probability sets. This refutes the arbitrary-direction pointwise-fiber bridge; no assertion about all global energies or an optimal choice of basis follows.

L3, replacement of the random fiber constant by its mean: KEEP. This is the hardest load-bearing claim and was rederived independently. Beta moments give E S^2=6/[N(N+1)], hence E c=12/pi^2. For each delta>0, choose a nonzero smooth a supported inside the projected simplex where S>1-delta. This region contains an interior open set of positive projected measure, even though the limit S=1 lies on a boundary. With f(T,Y)=a(Y)sin(pi T/[L S(Y)]), direct uniform-interval integration gives conditional mean zero, conditional second moment a(Y)^2/2, and conditional directional gradient energy a(Y)^2 pi^2/[2L^2 S(Y)^2]. Therefore

    E Var(f|Y) / E|partial_e f|^2
       = (L^2/pi^2) E a(Y)^2 / E[a(Y)^2/S(Y)^2]
       >= (L^2/pi^2)(1-delta)^2.

The support avoids S=0, so f has finite full gradient energy on the compact simplex for every fixed delta. A Lipschitz extension exists. The pointwise interval inequality gives the matching upper constant L^2/pi^2; letting delta tend to zero proves that the optimal directional conditional-energy constant is the essential supremum, not the mean. The transverse derivatives can grow as support concentrates; they are not omitted in a global Poincare claim.

L4, nonlinear maximal correlation: KEEP. Conditional means of T vanish, so cross-covariance with linear functions of Y is zero. Independently, E S^4=120/[N(N+1)(N+2)(N+3)], and the fourth moment of a centered uniform interval of length LS is L^4 S^4/80. Thus E T^4=6N(N+1)/[(N+2)(N+3)], yielding Var(T^2)=(N-1)(5N+6)/[(N+2)(N+3)]. The conditional second moment is N(N+1)S^2/6, whose variance is (N-2)(7N+9)/[3(N+2)(N+3)]. For centered a=T^2-1 and b=E[T^2|Y]-1, E[ab]=Var(b); dividing by the two L2 norms gives exactly the stated positive lower bound, tending to sqrt(7/15). This is not an upper bound on maximal correlation.

Remaining full-target gap: a dimension-independent comparison that retains the weighted conditional energies, nonlinear dependence, and transverse derivatives. The simplex refutes two tempting sufficient bridges but does not refute KLS. Verdict on any promotion of L0-L4 to a complete KLS proof: DROP.

## w353 own contribution: pending w356

The Gaussian-posterior covariance obstruction is in ATTEMPT.md and CLAIMS.jsonl. It requires w356's independent audit before promotion. Its purpose is to distinguish pointwise posterior covariance margins from averaged Dirichlet contraction, not to refute the latter or prove KLS.

## w350 Gaussian observation bridge: KEEP A and B

Artifact: ~/brain_workers/w350/ATTEMPT.md, Claims A-B. For Y=sqrt(t)X+G, the channel T:g -> E[g(Y)|X] maps centered L2(law Y) to centered L2(mu). On smooth bounded g, Gaussian integration by parts yields grad(Tg)=sqrt(t) E[G(g(Y)-Tg)|X]. Bessel's inequality for the Gaussian coordinate functions gives |grad(Tg)|^2 <= t Var(g(Y)|X), with no factor n. If C_P(mu)<=C, Poincare and total variance imply ||Tg||_2^2 <= Ct(||g||_2^2-||Tg||_2^2), hence ||T||^2<=Ct/(1+Ct). Smooth compactly supported functions are dense in L2(law Y), and T is an L2 contraction, so the norm bound extends. By the joint-law pairing T*f=E[f(X)|Y], giving q_f(t)>=Var(f)/(1+Ct). This checks normalization, Hilbert adjoint and domain extension.

For Claim B, the posterior potential is V(x)+t0|x|^2/2-sqrt(t0)y.x; it is t0-strongly convex on the convex support. Klartag, arXiv:2303.14938v2, equation (1.7), states C_P<=1/t0 for a t0-uniformly log-concave law, explicitly including his Borel-measure formulation. The posterior is such a law. Average its conditional Poincare inequality to get q_f(t0)<=t0^{-1} E|grad f|^2. If retention R_mu(t0)>=eta for ALL nonconstant L2 f, then eta Var f<=q_f and C_P(mu)<=1/(eta t0). The tower equality needs no conditional independence of coordinates. Smooth approximation extends to the natural Sobolev class. KEEP both implications with these hypotheses. DROP any inference that the universal retention premise VR has been proved: A and B show it is equivalent to the target up to constants. No full KLS verdict follows.

Primary locator: https://arxiv.org/html/2303.14938v2, introduction, lines 79-82, equation (1.7). The source states C_P(mu)<=1/t for t-uniformly log-concave probability measures. It supports only the named external input, not VR.

## w352 ball obstruction, independently rederived: KEEP

Artifact: ~/brain_workers/w352/PEER_AUDIT.md, its new ball calculation only. For n=2d, let X=(U,V) be uniform on the centered ball of radius sqrt(n+2). Radial integration gives E|X|^4=n(n+2)^2/(n+4). A 45-degree rotation of two coordinates gives E X_i^4=3 E X_i^2 X_j^2, so E X_i^2 X_j^2=(n+2)/(n+4) for i!=j. Thus for A=|U|^2, B=|V|^2, E A=E B=d, Var A=Var B=d, Cov(A,B)=-d^2/(d+2). Their correlation is -d/(d+2)=-n/(n+4), despite zero linear cross-covariance between U and V.

Given U=u, the V slice is a d-ball with squared radius n+2-|u|^2, so E[B|U]=d(n+2-A)/(d+2)=d-t(A-d), t=d/(d+2). The symmetric identity holds for E[A|V]. For f=A-B, its two centered conditional projections sum to (1+t)f. Hence E Var(f|U)+E Var(f|V)=(1-t)Var f and the exact comparison ratio is (n+4)/4. Directly, Var f=2n(n+2)/(n+4), E|grad f|^2=4n, and their quotient remains below 1/2. KEEP the obstruction to a dimension-uniform balanced-block variance comparison based only on isotropy and log-concavity. It does not refute the Poincare target or w351-L1 with its actual rho hypothesis. This is an independent check of w352's new lemma, not an audit of w352's review of w351.

## Source and measurement disposition

The old store has an open-problem concept card and a Gaussian-special-case attempt card; neither is a solved/retired proof. The named H/I local attempt directories had no P0017 record in the prior targeted search. The October preprints claim full solutions, so current openness remains UNKNOWN until their complete proofs are checked. The accepted reproduction used `python -X utf8 ~/brain_workers/w353/verify_packet.py`; MEASUREMENTS.json records a passing fresh 2 GiB/80% host gate, 7 peer quadratures with maximum relative error 9.802412828030545e-15, 15 posterior cases and 3 Gaussian controls. The analytic limits, not the floating-point runs, prove the obstructions.

NEXT: Have w356 independently audit the w353 posterior tail claim, and have another eligible reviewer check each proposed brain row before ingestion; inspect any claimed averaged gradient contraction with its weights intact.
