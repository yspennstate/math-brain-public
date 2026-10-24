# FEI: punctured-cube Shannon peeling and the failure of maximum-influence selection

21 September 2026. Owner-requested interactive account02 continuation, coordinated with ALL four accounts. Run: `20260921T192650Z-joint-fei-subcube-peeling`. Not a scheduled B-slot.

**Full uniform-cube FEI remains OPEN / NOT PROVED.** No finite universal constant for every Boolean function has been established. This continuation proves an unconditional one-step entropy theorem under an exact signed-subcube derivative hypothesis, and a genuinely Boolean obstruction to a universal local payment for the unique maximum-influence pivot. The new theorem is not just the previous all-row equality classification: one row, together with a quantitative surplus condition on its transverse controls, is enough for a paid peeling step. The proof uses a finite pure-state ensemble/Holevo bound to avoid any entropy penalty proportional to the number of residual variables.

All new arguments and executed checks are self-checked. No independent end-to-end review or publication-priority clearance has occurred. Model self-report: GPT-6 Astra Pro. Configured reasoning level and provider thinking counters: UNKNOWN / NOT_EXPOSED. Execution: WITHOUT_VERIFIED_BRAIN. Authenticated GitHub source retrieval occurred; native database ingestion, cognitive activation, later worker uptake and complete brain readiness are not inferred from repository delivery.

## 1. Exact target, current dependencies, and method change

For Boolean f:F_2^n->{-1,1}, write a_S=E_x f(x)(-1)^{S.x}, p_S=a_S^2,

    H(f)=sum_S p_S log_2(1/p_S),
    I_i(f)=sum_{S containing i}p_S,    I(f)=sum_i I_i(f),
    J(f)=sum_i min(I_i(f),1-I_i(f)).

Zero entropy terms are zero. Character multiplication preserves H and J and can make I=J. A uniform H<=C J statement is equivalent to full FEI with the same constant. Arbitrary affine changes preserve entropy but not this coordinate cost.

Fresh scientific source on entry was master `b54022151205145a398bd3da0818a8a8220ed571`. Complete relevant results were recovered from each account, not only account02:

* account01/B18, `20260921T1856Z-curvature-refunded-crossing/REPORT.md`, blob `ef9f471c019a7d81e9864fd457a0e4bae9da890d`: the potential P=sum_i j(I_i), j(t)=1-h_2(1/2+sqrt(t(1-t))), pays the JS recombination term and refunds surviving posterior crossings. The actual uniformly paid selective strategy is still missing.
* account02/B18, `20260921T190755Z-affine-subspace-plaquette-payment/REPORT.md`, blob `425212419d5db8dcc03b097ab789e1dac944c915`: exact arbitrary-pair affine-mask payment; the authentic signed compiler-to-physical-pair contraction is still missing.
* account03/B18, `20260921T185340Z-signed-flag-curvature/REPORT.md`: signed derivative curvature is support disagreement plus four times opposite-sign overlap; the ordered physical flag pays the full signed bank by J, but the authentic compiler map is still missing.
* account04/B18, `20260921T191147Z-mixed-curvature-global-rigidity/REPORT.md`, blob `0e8c2cc28da81af8843b565cb47285684b164480`: mixed derivatives give exact column conservation, and ALL folded derivative rows attaining their depth equality case force a one-point defect. Positive-defect joint stability and the depth-to-influence payment are still missing.
* account03/B16, `20260921T185632Z-integrated-phase-switch-logarithmic-bridge/REPORT.md`, blob `f7284256dac907940aea63f8d3458da4772ee774`: signed full-time Borel integration is an exact entropy increment; the finite live window is not paid by that endpoint identity alone.

These paths are relative to `proofnet24/P03-fei/fleet-2026-09-21/`. The preceding own `account02/interactive/20260921T174421Z-centered-critical-budget/REPORT.md` supplies the exact centered restriction budget and minimum-dimensional primitive-core reduction. The inherited genuine Boolean addressing family is in `proofnet24/P03-fei/solo-2026-09-17/ADDRESSING_BARRIER_2026-09-18.md`, blob `c1e52dff50095854d85c20e8b13a5385d91efaca`.

The present approach changes the category of the local problem: instead of charging all mixed derivative energy at unit price, it controls the Shannon entropy of a small ensemble of residual Boolean functions. The other new move is to attack the tempting maximum-influence choice before assuming it provides the required selector. Earlier variance-refund results were found in account01/B14 and are not claimed again. The global phase/rank/l1 optimizer and scalar sign-free profile relaxations remain refuted as full-proof routes.

## 2. Exact signed-subcube derivative and transverse surplus

Let x be one pivot bit, let z consist of r>=1 control bits, and let w be any number m>=0 of residual bits. Assume exactly

    D_x f(z,w):=[f(0,z,w)-f(1,z,w)]/2
               =sigma * 1{z=a},                       (2.1)

where sigma is a constant sign and a in F_2^r. In particular the support is a coordinate subcube, and the derivative sign is constant on it. Neither merely small L2 distance to (2.1), nor a statement about support alone, is this hypothesis.

Write

    N=2^r,    q=1/N,    q0=1-q.

On z=a, Booleanity forces f(x,a,w)=sigma(-1)^x, independent of w. On every z!=a, the derivative vanishes, so f(x,z,w)=h_z(w) for a Boolean h_z independent of x. Thus (2.1) has the exact normal form

    f(x,z,w)=sigma(-1)^x 1{z=a}+h_z(w)1{z!=a}.          (2.2)

The values h_z can be arbitrary Boolean functions and may depend on the same residual variables.

### Lemma 2.1 — the exact surplus identity

Define

    B=sum_{k=1}^r [I_{z_k}(f)-q].                       (2.3)

Every summand is nonnegative. If E_w denotes the set of unordered edges in the punctured r-cube F_2^r minus {a} on which h_z(w) changes sign, then

    B=(2/N) E_w |E_w|.                                 (2.4)

Moreover,

    I(f)=q(r+1)+B+q0 E_{z!=a} I(h_z).                  (2.5)

Proof. In control direction k, the two directed z-edges incident to a occur with probability 2/N. Since one endpoint is sigma(-1)^x and the other is independent of x, their average disagreement probability is 1/2. This contributes q. Every other edge contributes exactly its h_z disagreement, proving nonnegativity and (2.4). The pivot has influence q. Residual-variable influences vanish at z=a and average the corresponding h_z influences elsewhere, proving (2.5). QED.

This is ordinary influence in the stated gauge. When applying it to a centered function, I(f)=J(f); residual functions can be recentered separately, and J(h_z)<=I(h_z). No influence-preservation claim is made for general linear changes.

## 3. One exact maximal row can be peeled, with sharp constant four

### Theorem 3.1 — zero-surplus normal form and entropy identity

Under (2.1), if B=0, all h_z equal one Boolean function h. In that case

    H(f)=q0 H(h)+K_r,
    I(f)=q(r+1)+q0 I(h),                               (3.1)

where, writing phi(t)=t log_2(1/t),

    K_r=phi(q0^2)+2qr(2-q)<4q(r+1).                    (3.2)

Proof. The punctured r-cube is connected for r>=2, and for r=1 it has a single vertex. Equation (2.4) implies that for every w, all h_z(w) coincide along its edges, hence everywhere. A nonnegative quantity with average zero is zero at every point of the finite residual cube.

Fourier labels including x come solely from sigma(-1)^x 1{z=a}: there are N coefficients of magnitude q, with no residual frequency. Their entropy contribution is 2qr. Labels excluding x have the tensor-product Fourier coefficients of (1-1{z=a})h(w). The control factor has coefficient q0 at zero and magnitude q at every nonzero frequency, total squared mass q0. Expanding entropy for this subnormalized product gives q0 H(h)+phi(q0^2)+(N-1)q^2*2r. Adding the two sectors yields (3.1)-(3.2).

Finally -ln(1-q)<=q/(1-q) implies

    phi(q0^2)<= (2/ln2)q q0 <4q.

Also 2qr(2-q)<=4qr. This proves the strict inequality. QED.

The coefficient four cannot be reduced uniformly for this one-step class: taking h constant gives a one-point defect on r+1 bits, and K_r/[q(r+1)] tends to four as r tends to infinity.

### Corollary 3.2 — maximum-influence exact-row exclusion

If (2.1) holds and the pivot x has maximum ordinary influence, then B=0. Therefore a centered physical-restriction-critical Boolean function with H/J>4 cannot have a maximum-influence pivot whose derivative is a constant-sign coordinate-subcube indicator.

Proof. Each control influence is at least q by Lemma 2.1 and at most I_x=q by maximality, hence equals q. Apply Theorem 3.1. The function h occurs as a proper physical restriction. If the parent ratio R=H(f)/I(f)>4 and every proper noncharacter restriction has H/J<=R, then H(h)<=R J(h)<=R I(h). Equations (3.1)-(3.2) imply H(f)<R I(f), a contradiction. Character h has H=0 and satisfies the same comparison. QED.

This uses ONE exact row, not the hypothesis that all derivative rows are extremizers. It does not assert that every maximum-influence row has that structure. Section 6 proves that the latter choice alone is insufficient.

## 4. A dimension-free Shannon bound for small positive surplus

The residual functions need not be equal when B>0. Direct continuity estimates on their full Fourier spectra can incur a factor m, the number of residual variables. The argument below instead pays the information carried by an ensemble of N-1 vectors, so no m appears.

### Lemma 4.1 — punctured-cube variance

Put

    hbar(w)=E_{z!=a}h_z(w),
    v=E_w[1-hbar(w)^2].                                (4.1)

For r>=2,

    0<=v<=2B/q0.                                       (4.2)

For r=1, B=v=0.

Proof. Let L be the unnormalized graph Laplacian of the full r-cube. Its second-smallest eigenvalue is two: Walsh characters diagonalize it with eigenvalue twice their Hamming weight. Delete the row and column indexed by a to obtain the principal matrix M. Eigenvalue interlacing gives lambda_2(M)>=2. The induced punctured-cube Laplacian is M-D, where D is the diagonal indicator of the neighbors of a, so 0<=D<=Id. The variational principle gives lambda_2(M-D)>=1. Its zero eigenvector is constant, and the punctured cube is connected. Thus for any real function u on its N-1 vertices,

    Var_uniform(u)<= [1/(N-1)]sum_edges (u(z)-u(z'))^2.

Apply this to u(z)=h_z(w). A changing sign contributes four. Average over w and use (2.4): v<=4 E|E_w|/(N-1)=2B/q0. QED.

The interlacing step is valid for r>=2, when N-1>=3; the one-vertex case is handled separately.

### Lemma 4.2 — finite-ensemble entropy bound

Let phi_1,...,phi_K be real or complex unit vectors, rho=K^{-1}sum_z |phi_z><phi_z|, and suppose the average vector has squared norm 1-v. For any orthonormal-basis measurement, let P_z be the squared-coordinate distribution of phi_z and let Pbar be its average. Then

    H(Pbar)<=K^{-1}sum_z H(P_z)+S(rho).                 (4.3)

If K>=2 and 0<=v<=1/2, then

    S(rho)<=h_2(v)+v log_2(K-1).                        (4.4)

Proof. Equation (4.3) is the pure-state case of Holevo's theorem: the measurement mutual information is H(Pbar)-average H(P_z), and the ensemble's Holevo quantity is S(rho) because each state has zero von Neumann entropy. This is a standard imported information inequality, not a new theorem or a physical quantum computation. Its precise finite-dimensional hypotheses and proof via strong subadditivity were checked in John Watrous, Theory of Quantum Information lecture notes, Lecture 12, Theorem 12.1, PDF pages 3-4 (2011), available on the author's University of Waterloo site.

For (4.4), the covariance identity shows rho>=|phibar><phibar|, hence its largest eigenvalue is at least 1-v. Its rank is at most K. If t=1-lambda_max<=v, concavity of scalar entropy bounds S(rho)<=h_2(t)+t log_2(K-1). This expression increases for t<=1-1/K; v<=1/2 lies in that interval. QED.

This statement can equivalently be written using only a positive semidefinite Gram matrix. No quantum computer, remote model or specialized experimental assumption is used.

### Theorem 4.3 — explicit Shannon peeling with arbitrary residual dimension

Under (2.1), with r>=2 and v<=1/2, define

    Phi_N(s)=h_2(s)+s log_2(N-1).

Then

    H(f)<=q0 E_{z!=a} H(h_z)+h_2(q)+qr
          +q0[h_2(v)+v log_2(N-2)+Phi_N(q+q0 v)].       (4.5)

Proof. Let phi_z be the normalized Walsh coefficient vector of h_z. The Walsh transform is an isometry for normalized L2, so every phi_z is a unit vector and ||E_z phi_z||^2=E_w hbar(w)^2=1-v. Their average density matrix has rank at most N-1. Apply Lemma 4.2 to measurement in the residual Fourier basis.

For clarity, partition the actual Fourier spectral sample of f according to membership of pivot x. The x-containing sector has probability q, uniform control frequency on N labels, and residual frequency zero. Conditional entropy there is r. In the x-absent sector, denote control and residual frequencies by T,W. Its residual marginal is exactly

    Pr(W=s | x absent)=E_{z!=a} |hhat_z(s)|^2,

by Parseval in the control variables. Lemma 4.2 gives

    H(W | x absent)<=E_z H(h_z)+h_2(v)+v log_2(N-2).

The coefficient vector at control frequency T=0 is q0*E_z phi_z before normalization of the x-absent sector. That sector has mass q0, so

    Pr(T=0 | x absent)=q0(1-v).

Thus Pr(T!=0 | x absent)=q+q0v, and the entropy of T is at most Phi_N(q+q0v), maximizing over its N-1 nonzero values. Subadditivity gives H(T,W)<=H(W)+H(T). Finally add the binary sector entropy h_2(q), the q r term, and the q0-weighted conditional bound. QED.

At v=0, the expression outside q0 E H(h_z) is exactly K_r of (3.2). The proof uses common residual variables and arbitrary residual Boolean functions; it does not assume that the h_z are balanced, disjoint or independent.

### Corollary 4.4 — low-surplus coefficient 4+8 epsilon

For every r>=1, if

    B<=epsilon q,    0<=epsilon<=1/8,                  (4.6)

then

    H(f)<=q0 E_{z!=a}H(h_z)+(4+8epsilon)q(r+1).         (4.7)

In particular B<=q/16 gives coefficient 9/2 in the last term. There is no dependence on the residual dimension m.

Proof. For r=1 the exact formula already applies. For r>=2, (4.2) and (4.6) ensure v<=2epsilon q/q0<=1/12<1/2. Concavity of Phi_N and

    Phi'_N(q)=2log_2(N-1)<=2r

give

    Phi_N(q+q0v)-Phi_N(q)<=2r q0v.

Consequently the excess of (4.5) over q0 E H(h_z)+K_r is at most

    q0 h_2(v)+3q0 r v
    <=2B log_2(e q0/(2B))+6rB,                         (4.8)

with the continuous zero value at B=0. Here h_2(v)<=v log_2(e/v) and the function v log(e/v) increases on [0,1]. The right side increases in B over the present range. Since q=2^-r and q0<=1, it is at most

    8epsilon qr+2epsilon q log_2(e/(2epsilon)).          (4.9)

Also K_r<=4qr+(2/ln2)q. On 0<=epsilon<=1/8,

    2epsilon log_2(e/(2epsilon))
       <=(1/4)log_2(4e)=1/2+1/(4ln2).

Thus the q-only coefficient is at most 1/2+9/(4ln2)<4; for example ln2>2/3 proves it is below 31/8. Combining with (4.9) gives (4.7). QED.

The natural constant e in (4.8)-(4.9) is Euler's number; all displayed logarithms there are base two. The proof of the simple entropy envelopes is analytic, not a floating-point certificate.

### Corollary 4.5 — a new primitive-core exclusion and an honest conditional class theorem

A centered H/J-critical Boolean core with ratio strictly greater than 4+8epsilon cannot contain an exact signed-subcube derivative row satisfying (4.6). This includes a maximum-influence exact row at epsilon=0.

Indeed, every h_z is a proper restriction. If the parent's critical ratio is R, then H(h_z)<=R J(h_z)<=R I(h_z). Equations (2.5) and (4.7) would give

    H(f)<=R q0 E I(h_z)+(4+8epsilon)q(r+1)<R I(f),

a contradiction when R>4+8epsilon.

Likewise, a restriction-closed class in which every noncharacter member, after character centering, has such a row satisfies H<= (4+8epsilon)J by induction. This last statement is a CONDITIONAL compiler: no assertion is made that arbitrary Boolean functions or arbitrary critical cores satisfy its row hypothesis.

The exact derivative condition has not been extended here to a near-subcube row with sign/support errors. A small global L2 error could carry high-dimensional residual spectral entropy; dropping that issue would be an unsupported extension. The useful improvement is that transverse variation among arbitrary exact-row residual functions is now paid without an ambient residual-dimension factor.

## 5. Why this is not a renamed all-row equality theorem

The account04 endpoint requires every derivative row to attain its isoperimetric depth equality. Here only one row must have the exact form (2.1); the other rows and all residual functions can be arbitrary. At B=0 it has an exact removable-gadget form, and at small positive B it has a quantitative Shannon transfer. In particular the 9/2 step is compatible with completely unclassified h_z. They enter as true physical descendants with their own entropy, not as invented spectra.

The next full-scope obligation is to deal with primitive cores having no such row, or to prove an influence-relative extension to approximate signed-subcube rows and show that a realizable selection strategy finds enough of them. The present theorem is one completed transfer in interface B-to-A of the all-account programme; it does not prove that the interface covers all functions.

## 6. Maximum influence is not a universally valid entropy selector

The previous theorem might suggest always choosing the largest influence. The following construction rules out that shortcut, even when the largest folded and ordinary influence is UNIQUE.

### Lemma 6.1 — balanced substitution preserves the pivot decrement

Let f have a designated pivot x of influence p>0. Replace each OTHER variable j by a balanced Boolean g_j on a disjoint fresh block. Leave x unchanged and call the result F. Then

    I_x(F)=I_x(f),
    I_(j,l)(F)=I_j(f) I_l(g_j),                         (6.1)
    H(F)=H(f)+sum_(j!=x) I_j(f) H(g_j),                (6.2)
    Delta_x H(F)=Delta_x H(f).                          (6.3)

Proof. A balanced child has zero empty Fourier coefficient. In the outer expansion of f, each selected child contributes a nonempty spectrum on its own block. Thus the selected block set uniquely identifies the outer spectral label and there are no Fourier collisions. The spectral experiment first samples the outer label and then, independently on each selected block, the child's squared spectrum. Its entropy chain rule proves (6.2), and counting coordinate memberships gives (6.1). The same expansion holds for both x restrictions. Average their (6.2) formulas and use E_b I_j(f_(x=b))=I_j(f). The child contributions cancel, proving (6.3). QED.

This is established balanced-disjoint composition methodology, rederived here for its exact pivot-invariance use. No claim of inventing composition is made.

Take every g_j to be recursive ternary majority of depth d. Starting with one sign bit and composing disjoint copies using (u+v+w-uvw)/2 gives

    every leaf influence =2^-d,
    A_d:=I(g_j)=(3/2)^d,
    H(g_j)=4(A_d-1).                                   (6.4)

These follow from the gate influences 1/2 and entropy two by Lemma 6.1's composition identities.

### Theorem 6.2 — arbitrary influence dilution without changing a bad local ratio

Suppose 0<p=I_x(f)<=1/2. Choose d with 2^-d<p and make the substitutions above. Then x is the unique maximum ordinary and folded influence of F, all its surviving restricted leaf influences are below 1/2, and

    D_x(F):=J(F)-E_b J(F_(x=b))=p,
    Delta_x H(F)/D_x(F)=Delta_x H(f)/I_x(f).             (6.5)

Proof. Every other leaf influence is at most 2^-d<p. After either x restriction, its outer-coordinate factor remains at most one, so the leaf influence is still at most 2^-d<1/2. Thus J=I for the parent and both children (with the pivot absent in children). The ordinary influence identity gives D_x=p. Apply (6.3). QED.

### Corollary 6.3 — an explicit Boolean unbounded greedy-pivot family

For even m>=2, N=2^m, use the actual bent/addressing Boolean function

    f_m(z,a,y)=[(1+z)/2]b(a)+[(1-z)/2]y_a,
    b(a)=(-1)^(a_1a_2+...+a_(m-1)a_m).

Fix one designated data bit y_c. Its influence is p=1/(2N). Its nonzero Fourier pairs across that bit have squared magnitudes 1/(4N) and 1/(4N^2), with 2N pairs. Therefore

    B_(y_c)(f_m)/p
      =(N+1)log_2(N+1)-Nlog_2 N
      >log_2 N=m.                                     (6.6)

The exact restriction identity Delta_i=B_i+JS_i and JS_i>=0 imply the same strict lower bound for Delta_(y_c)/p. The pair list follows directly by expanding 1{a=c}=N^-1 sum_S chi_S(a)chi_S(c) and the bent transform of b, whose magnitudes are N^-1/2. Thus realizability comes from the displayed Boolean function, not a squared-spectrum guess.

Replace every coordinate except y_c by recursive majority of depth d=m+2. Theorem 6.2 gives a genuine Boolean F_m with a UNIQUE maximum-influence pivot and

    Delta_(y_c) H(F_m)/D_(y_c)(F_m)>m -> infinity.       (6.7)

Nevertheless this family obeys H(F_m)<4I(F_m). Indeed the inherited exact formulas are H(f_m)=2+3m/2 and I(f_m)=(m+2)/2, while (6.4) makes

    H(F_m)-4I(F_m)=H(f_m)-4I(f_m)=-2-m/2<0.            (6.8)

Consequently (6.7) refutes only a universal local payment for the greedy largest-influence pivot. It is NOT a counterexample to FEI, to an existential selector, to a valid adaptive strategy, or to the theorem restricted to primitive high-ratio cores. Nor does it contradict Corollary 3.2: the diluted bad pivot does not have the signed-subcube row structure required there.

## 7. Attempts that did not close the full problem

Before the punctured-cube argument, I tested the candidate H<=4J+2D where D=I_2-(1/2)sum_i q_i log_2(1/q_i) is the total derivative-depth defect in the median-character gauge. Exhaustive four-bit data, seeded higher-dimensional truth tables and threshold examples found no numerical violation. There is NO proof, and the second factorial spectral moment I_2 is not universally O(J). This is retained as exploratory output, not as a theorem or an improved universal FEI bound. Older second-moment results in the primary literature were checked to avoid claiming that an entropy/second-moment comparison is new methodology.

I also read the complete account03 signed integrated-phase-switch result and compared it with the account02 affine-mask sink. The missing finite-window/PSD contraction was not derived; the two existing results cannot simply be concatenated into a proof. No compiler closure or new constant is claimed from that inspection. The punctured-cube/Holevo mechanism was then executed as a different actual transfer, rather than producing another source-kernel dictionary.

Finally, a generic block bound based only on a large diagonal mass or a rank cap throws away too much Shannon information. The present proof uses the actual branch-vector Gram spectrum and control-frequency zero mass before relaxing them. It does not establish that the same low-surplus configuration is available in every function.

## 8. Executed checks and reproducibility

New script: `check_peeling.py`. This is different mathematical code from the previously denied centered-critical-budget verification upload; that denied script was not renamed, encoded, rerouted or retried.

Actual commands included the three `--part exhaustive`, `--part seeded`, and `--part substitution` runs, followed by an executed `--part all --output verification.json` run. The final JSON preserves the resulting values; its 145 per-family records use an explicit column-name/row-array representation, and whitespace was compacted for delivery. This is ordinary JSON, not an encoding of code. Separate-process replay is reproducibility evidence, not independent review.

Coverage:

* All 65,812 Boolean functions in dimensions one through four. The checker finds 15,428 constant-sign subcube rows, including 15,408 of positive codimension; verifies nonnegative surplus and zero-surplus factorization; and checks that all 1,248 maximum-influence qualifying rows have B=0. There are 1,440 zero/low-surplus rows in this exhaustive range. Walsh, influence and combinatorial tests are integer/Fraction exact. Entropy identities are labeled floating diagnostics, with maximum observed identity discrepancy zero.
* 145 generated exact-row families. Fourteen have positive B and satisfy B/q<=1/8; 47 in total satisfy the low-surplus hypothesis. All 47 peeling inequalities are certified by rational logarithm intervals, not merely floating tolerances. The minimum recorded rigorous margin lower bound is 5881959909/274877906944. Integer/Fraction checks verify the punctured boundary, variance, Fourier sector masses and Gram identities. The eigenvalue/Holevo intermediate comparisons are floating diagnostics; the analytic proof supplies their universal validity.
* All 256 three-bit outer Boolean functions and each of three designated pivots, with both other variables replaced by disjoint ternary majorities: 768 directly materialized seven-bit composition cases. Leaf influences are checked exactly; entropy/decrement diagnostics have maximum discrepancy 4.440892098500626e-16.
* Exact compact-formula checks of the genuine dilated addressing family for m=2,4,6,10,20. Large formal dimensions are formula evaluations, NOT enumerated truth tables. The smallest reported formal dimension is 487 and the largest is 32,906,053,581,758,965; neither is represented as a full-table computation.

The rational log enclosure reduces an integer to 2^k y with 1<=y<2, uses z=(y-1)/(y+1), sums 40 terms of ln y=2sum_(j>=0)z^(2j+1)/(2j+1), and bounds the remainder by 2z^81/[81(1-z^2)]. It similarly encloses ln2, then bounds entropy from the exact integer Walsh histogram. These finite certificates supplement, not replace, the analytic theorem and its standard Holevo dependency.

The speculative depth exploration and its exact sampling metadata are retained in `explore_depth.py` and `depth_exploration.json`; entropy comparisons there are explicitly floating and unproved. No independent worker or external model was used for the new derivations or checks.

## 9. Primary-source comparison and novelty limitations

Primary mathematical resources checked include:

* John Watrous, Theory of Quantum Information lecture notes, Lecture 12, Theorem 12.1, PDF pp. 3-4, author-hosted at cs.uwaterloo.ca/~watrous/TQI-notes/TQI-notes.12.pdf. This is the exact imported finite-ensemble measurement information bound in Lemma 4.2. Its proof uses strong subadditivity. The current author page recommends the later book; no new theorem is attributed to these notes.
* O'Donnell and Tan, A composition theorem for the Fourier Entropy-Influence conjecture, arXiv:1304.1347. Balanced-disjoint entropy composition is prior methodology, not invented here.
* Chakraborty, Kulkarni, Lokam and Saurabh, Upper Bounds on Fourier Entropy, ECCC TR13-052, revision 2 dated 13 September 2018. Its first/second-moment and decision-tree results were checked at the revision-summary level. The revision explicitly removes inaccuracies in older statements; this work does not rely on those removed assertions.
* González, MacManus and Pereyra, Further evidence towards the Fourier Entropy-Influence conjecture, arXiv:2606.00246; and Potapov, On the Fourier Entropy Influence Conjecture for Boolean Plateaued Functions, arXiv:2609.21563 (18 September 2026). They are current restriction/structured-class context, not imported unconditional full proofs.

Repository searches included `Holevo`, `max-influence`, and combinations of maximum/influence/selector; public searches included Fourier entropy, quantum ensembles, and moment bounds. These are bounded checks, not exhaustive priority clearance. No publication priority is claimed for the peeling theorem, its constants, the dilution use of composition, or the underlying linear algebra.

## 10. All-account delivery and exact remaining task

This invocation did not confine coordination to account02. It created a shared order and source-exact research index under `scheduled_tasks/work/shared/fei-joint-proof-2026-09-21/` in the brain repository, and inserted an additive pointer in the common `scheduled_tasks/README.md` read by all four accounts. The root change is exactly eight inserted lines, with prior controls intact, at commit d2c57e60881050d3cae1176d9804a1a538831378. The order is 4ba19644d6c44499692c5e16c29c3c02515f66de, and the research-state index is 5b02cab94d0ea3563adc86da6831f25ad62ffcf5. They route the 28 existing FEI slots into complementary cross-account interfaces and preserve the other existing brain/benchmark roles and safeguards.

Publication, local keeper prompt incorporation, and a subsequent worker actually consuming a peer result are separate states. The completed 18Z login snapshot had 20/17/17/20 files across accounts01-04, respectively: 74 canonical check-ins, not 74 completed proofs. Mathematical reports from every account were actually read. Neither the activity snapshot nor the shared instruction proves that every scheduled worker has already adopted the new order.

The new mathematical handoff is intended for account04/B18 and all A/B-interface workers: use the paid exact-row low-surplus peeling step; do not substitute an unsigned near-subcube condition for its hypothesis; and do not use unique-largest-influence selection without additional structure, because Section 6 rules that out.

FULL-PROBLEM CHANGE: none; full FEI remains open in this work.
MECHANISM CHANGE: a complete one-row, residual-dimension-free Shannon transfer with coefficient 4+8epsilon, plus an exact obstruction to a tempting greedy selector.
REMAINING IMPLICATION: establish that every primitive high-ratio core admits a paid realizable elimination, including rows with support/sign errors or large transverse surplus, or derive the separate authentic signed compiler contraction with all live-window and terminal terms accounted for.

The report contains proof arguments, not a promise that these remaining universal implications have been proved. Preserve the failed routes and continue actual derivation; a conditional class theorem or an updated collaboration order is not full FEI closure.
