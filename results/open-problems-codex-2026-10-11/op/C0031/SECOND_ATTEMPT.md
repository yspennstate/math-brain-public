# C0031 — renewed attempt, 2026-10-11

## Two routes not previously pursued here

**Route A: spatially integrated hard-edge control.** Replace almost-sure invertibility at each fixed spectral parameter by control of the area-integrated clipping defect. The already-proved uniform fractional eigenvalue moment gives uniform local L2 bounds on the true logarithmic potentials. This may make the spatial area of exceptional hard-edge parameters sufficient, even if the fixed-parameter failure probabilities are nonsummable. The question is whether determinant-polynomial structure or subharmonic compactness supplies the missing almost-sure control of that exceptional area. A deterministic Jordan-block test must be used before trusting such a transfer.

**Route B: finite-mixture noise and general high-confidence invertibility.** For an entry law having two atoms, extract an independent fair bit on a positive-density random mask, condition on the rest, and seek a high-confidence invertibility theorem for the resulting bounded but non-identically distributed noise and arbitrary polynomial-size deterministic core. This differs from the independent additive convolution subclass: a generic mixture has no independent convolution factor. Before constructing a new proof, inspect the exact scope of the neighboring Tao–Vu/Cook/Jain invertibility hypotheses, especially controlled truncated moments and non-identically distributed entries. A theorem valid only for iid finite-variance noise is insufficient.

**Choice.** Route B is more promising initially: it attacks the precise atomic obstruction and may reveal an overlooked hypothesis-level reduction. Route A will receive a deterministic stress test in parallel; if its only input is potential compactness plus rarity in probability, it cannot be accepted as a full almost-sure upgrade.

## Brain query

Asked the math store, read-only, for `Cook Jain bounded amplitude Bernoulli profile arbitrary deterministic perturbation summable smallest singular value`. Returned hints will be checked against theorem statements, not treated as verdicts.

The returned cards were generic subgaussian smallest-singular-value bounds and eventwise Borel–Cantelli transfer results; none supplied the required arbitrary-core non-identical-noise theorem. In particular, a subgaussian noise theorem cannot be invoked on the unconditioned infinite-variance entry law.

## Route A: a complete unrestricted averaged theorem

Let mu_n be the empirical eigenvalue measure of A_n=n^{-1/alpha}X_n under the exact source hypotheses in ATTEMPT.md. No extra smoothness or convolution assumption is imposed. Let mu=mu_alpha. Then, almost surely,

1. the probability measures (1/N) sum_(n=1)^N mu_n converge weakly to mu;
2. for a bounded metric d inducing weak convergence on probability measures on C, (1/N) sum_(n=1)^N d(mu_n,mu) -> 0.

Thus convergence holds statistically almost surely: for every epsilon>0, the fraction of dimensions n<=N with d(mu_n,mu)>epsilon tends to zero almost surely. This is weaker than the requested full-sequence almost-sure convergence. No novelty is claimed.

### Step 1: quantitative exceptional-area bound from the source

Fix a disk K={|z|<=R}. Pick 0<kappa<alpha. Since E|X|^kappa<infinity, choose r>1/alpha with kappa(r-1)>4. For large n, uniformly for z in K,

P(||X_n-n^{1/alpha}zI||>n^r) <= C_R n^{2-kappa(r-1)} <= C_R n^{-2}.

Indeed the shift has norm at most R n^{1/alpha}<=n^r/2 eventually, and ||X_n||<=n max|X_ij|; the union and Markov bounds apply at threshold n^{r-1}/2.

The source's Lemma A.1 (printed page 54) gives, for the fixed nonconstant entry law, a constant c such that

P(s_min(X_n+M)<=t/sqrt(n), ||X_n+M||<=s) <= c sqrt(log(cs)) [t s^2+n^{-1/2}]

for deterministic M, n large, s>=1 and 0<t<=1. Its truncated nondegeneracy hypotheses hold for this fixed nonconstant law: a bounded truncation level can be chosen with positive retained probability and positive truncated variance. Take s=n^r, t=n^{-2r-1/2}, and M=-n^{1/alpha}zI. Set b=2r+1+1/alpha. Then

sup_(z in K) P(s_min(A_n-zI)<=n^{-b}) <= C_R sqrt(log n/n)+C_R n^{-2}=:q_n.

Define B_n={z in K:s_min(A_n-zI)<n^{-b}}. By Fubini, E area(B_n)<=area(K) q_n. This requires no independence between dimensions n.

### Step 2: clipped potentials converge almost surely without an almost-sure floor

For n>=2 define h_n(s)=log(s) clamped to [-b log n,b log n], including h_n(0)=-b log n, and

S_n(z)=(1/n) sum_i h_n(s_i(A_n-zI)),
V_n(z)=(1/n) log|det(A_n-zI)|.

For Lebesgue-almost every fixed z, the probability that S_n(z) differs from V_n(z) tends to zero by Step 1 and the norm bound. The source already proves V_n(z)->ell(z) in probability, where ell is the positive-log potential of mu. Consequently S_n(z)->ell(z) in probability. The independent-row bounded-differences estimate from ATTEMPT.md gives

P(|S_n(z)-E S_n(z)|>=t)<=2 exp(-n t^2/(2b^2(log n)^2)).

It is summable for every fixed t>0. Therefore S_n(z)-E S_n(z)->0 almost surely. To check centering directly, if |E S_n(z)-ell(z)|>2t along a subsequence, the events |S_n(z)-E S_n(z)|<=t and |S_n(z)-ell(z)|<=t would be disjoint, although both probabilities tend to one. This contradiction for every t>0 proves E S_n(z)->ell(z). No interchange of limits and expectations is used. Fubini yields S_n(z)->ell(z) almost everywhere on K, simultaneously on one probability-one event.

The earlier fractional moment proof supplies a random finite bound M_p=sup_n (1/n) sum_i s_i(A_n)^p, for any fixed 0<p<alpha/4. Since p<1 and s_i(A_n-zI)<=s_i(A_n)+R,

S_n(z)<= (1/n) sum_i log_+(s_i(A_n-zI)) <= (M_p+R^p)/p=:C_R(omega).

Here h_n(s)<=log_+(s) for every s>=0, even at zero. Almost surely the upper clipping threshold is unused for all z in K and all sufficiently large n, by the uniform polynomial norm bound and the chosen b. Hence S_n(z)>=V_n(z) at those n, outside the finite eigenvalue set where V_n=-infinity. Thus the negative part of S_n is bounded by that of V_n, and its positive part is bounded by C_R(omega). The local L2 bound on V_n proved in ATTEMPT.md now implies a uniform local L2 bound on S_n. Fatou plus Egorov/Cauchy–Schwarz, exactly as in ATTEMPT.md, gives S_n->ell in L1(K) almost surely.

### Step 3: exceptional areas have almost-sure vanishing Cesaro average

Set a_n=area(B_n)>=0 and T_N=(1/N) sum_(n<=N) a_n. Step 1 implies

E T_N <= C_R sqrt(log N/N)+C_R/N

after absorbing finitely many initial n. For example sum_(n<=N)n^{-1/2}<=2 sqrt(N), so the logarithmic term has the displayed bound. At N=2^k, Markov gives for every epsilon>0

sum_k P(T_(2^k)>epsilon) <= (C_R/epsilon) sum_k [sqrt(k) 2^{-k/2}+2^{-k}] < infinity.

Borel–Cantelli at rational positive epsilon gives T_(2^k)->0 almost surely. If 2^k<=N<2^{k+1}, positivity gives T_N<=2 T_(2^{k+1}). Therefore T_N->0 almost surely along all N. No independence across n has been used.

### Step 4: control the integrated clipping defect

For sufficiently large n, D_n=S_n-V_n is nonnegative and vanishes outside B_n, up to a finite set of area zero. By the local L2 bounds on S_n and V_n,

||D_n||_(L1(K)) <= C'_R(omega) sqrt(a_n).

Consequently Cauchy–Schwarz gives

(1/N) sum_(n<=N) ||D_n||_(L1(K)) <= C'_R(omega) sqrt(T_N)+o(1) ->0

almost surely. The o(1) absorbs finitely many initial defects, each integrable because V_n is a finite-eigenvalue log potential and S_n is bounded. Combining with Step 2 and the ordinary Cesaro lemma yields

(1/N) sum_(n<=N) ||V_n-ell||_(L1(K)) ->0 almost surely.

### Step 5: spectral measures and a weak-convergence metric

For each smooth compactly supported phi with support in K, the distributional potential identity gives

|integral phi d(mu_n-mu)| <= (||Delta phi||_infinity/(2 pi)) ||V_n-ell||_(L1(K)).

Therefore the Cesaro average of the absolute error tends to zero almost surely. Use a countable family (phi_j) of smooth compactly supported functions with ||phi_j||_infinity<=1, dense in the unit ball of C_c(C) on each compact set (include enough rational smooth approximations to separate measures), and set

d(rho,mu)=sum_(j>=1) 2^{-j} min(1,|integral phi_j d(rho-mu)|).

This is a bounded metric on probability measures whose convergent sequences with probability-measure limits are precisely the weakly convergent sequences. To check the latter, convergence of d implies convergence on every phi_j, then on every compactly supported continuous test by uniform approximation. This is vague convergence; when the limit has mass one it implies tightness and hence weak convergence. Conversely weak convergence implies convergence of every summand, and the geometric tail makes d tend to zero. For metric separation use the same density of C_c tests. The triangle inequality follows from min(1,a+b)<=min(1,a)+min(1,b).

Intersect the probability-one events for this countable family and integer disks. For each j the Cesaro absolute error tends to zero. Truncate the metric sum at J: the first J average summands tend to zero, and the tail is at most 2^{-J}. This proves (1/N) sum_n d(mu_n,mu)->0 almost surely. Markov's deterministic counting inequality gives the statistical-convergence assertion. The averaged measures themselves converge on each test; their uniform pth moment bound gives tightness, and the same test approximation argument proves their weak convergence to mu. This completes the unrestricted averaged theorem.

## Why this does not close C0031: a sharp reduction counterexample

Let J_n be the nilpotent shift with ones immediately above the diagonal, and let C_n=J_n+e_n e_1^T be the cyclic permutation matrix. Let E_n be independent Bernoulli variables with P(E_n=1)=n^{-1/2}, and set M_n=J_n on E_n=1, otherwise M_n=C_n. The rows within each M_n are independent: the first n-1 rows are deterministic and only the last row is random. Entries are not iid, so this is not a counterexample to C0031.

Both matrices have operator norm at most one and all eigenvalue-modulus pth moments at most one. The eigenvalue measure of C_n is uniform on the nth roots of unity and tends to circle-uniform measure, whereas that of J_n is delta_0. Thus the empirical spectral measures converge in probability to circle-uniform measure, but fail almost-sure convergence, since independent events E_n=1 occur infinitely often by the second Borel–Cantelli lemma. For example a bounded continuous test equal to |z|^2 on the unit disk has integral one for C_n and zero for J_n.

For |z|<=r<1, the approximate null vector v=(1,z,...,z^{n-1}) obeys (J_n-zI)v=(0,...,0,-z^n). Since ||v||>=1, s_min(J_n-zI)<=|z|^n. In contrast, C_n is unitary and s_min(C_n-zI)>=1-r. Therefore the bad-parameter area is eventually exactly area(K) E_n on each centered disk K of radius r<1, apart from threshold boundaries; the probability of the bad area is n^{-1/2}, not summable.

On K the true potential of J_n is log|z| and that of C_n is (1/n) log|z^n-1|, which tends uniformly to zero. Yet the clipped singular potentials of these two matrices differ by at most 2b log n/n by their rank-one difference. Consequently both clipped potentials tend uniformly to zero on K, regardless of the events E_n. This example has independent rows, summable clipped-potential concentration, uniform local L2 true potentials, the same polynomial bad-probability rate, and almost-sure Cesaro convergence, but still fails full almost-sure convergence. It rules out obtaining the full result from precisely these general inputs alone. To finish C0031 one must use additional iid-entry structure, beyond the averaged theorem.


## Route B: exact atomic-mixture reduction, and where the transfer fails

Suppose the fixed entry law P has two distinct atoms a,b with probabilities p_a,p_b>0. Put q=2 min(p_a,p_b) and c=(b-a)/2. In the heavy-tailed setting q<1: q=1 would force the entire law to be the equal two-point distribution. Define the residual probability law

P_res = [P-(q/2) delta_a-(q/2) delta_b]/(1-q).

Its masses are nonnegative and its total mass is one. Draw a Bernoulli(q) mask delta, a fair sign epsilon, and a residual sample Y independently. Set D=(a+b)/2 when delta=1 and D=Y otherwise. Then X=D+c delta epsilon has precisely law P: conditioning on delta gives atoms a,b with masses q/2 and the remaining law with weight 1-q. This proves the decomposition for complex as well as real atoms. If E|X|^kappa is finite, so is E|D|^kappa, since the residual law is dominated by P/(1-q) plus a finite deterministic contribution.

Take independent copies entrywise. Conditional on all delta_ij and D_ij, the signs remain independent fair signs, so

c^{-1}(X_n-n^{1/alpha}zI)=delta_n circ epsilon_n+B_n,
B_n=c^{-1}(D_n-n^{1/alpha}zI).

Here circ denotes entrywise multiplication. The core and mask are dependent on each other, but are both independent of the signs. Unconditionally each entry of the bounded noise delta epsilon is independent and identically distributed; it is NOT independent of the core D. After conditioning the mask, the noise has zero entries on its complement, so it is no longer iid. Thus an iid additive-noise theorem cannot be applied by either conditioning choice. This is the precise obstruction to treating a general mixture as an independent convolution.

### The mask itself is not the obstruction: complete super-regularity proof

Fix a sufficiently small constant epsilon_0>0 and delta_0=q/2. With probability at least 1-exp(-c_q n), the zero-one mask is (delta_0,epsilon_0)-super-regular in Cook's Definition 1.23: every row and column has at least delta_0 n ones, and every cut I by J with |I|,|J|>=epsilon_0 n contains at least delta_0 |I||J| ones.

For completeness, if S is the sum of m independent Bernoulli(q) variables, then

P(S<=qm/2)<=exp(-qm/8).

Indeed, exponential Markov at lambda=log 2 gives
P(S<=qm/2)<= exp(lambda qm/2)(1-q+q exp(-lambda))^m
<=exp[-qm(1-log 2)/2]<=exp(-qm/8).
The last inequality uses log 2<3/4; for example integrate 1/t on [1,2], whose strict convexity places its integral below the trapezoidal value 3/4. Apply this to each row and column and union bound to obtain 2n exp(-qn/8). For any fixed large cut use m=|I||J|>=epsilon_0^2 n^2. There are at most 4^n cuts, giving at most exp(2n log 2-q epsilon_0^2 n^2/8). The sum of these two errors is at most exp(-c_q n) for large n (constants may also depend on epsilon_0). This proves the assertion without assuming independence between different cuts.

Choose sigma_0=1/2. Cook's thresholded profile delta_n(sigma_0) is the same zero-one mask. Choosing epsilon_0 small enough to satisfy epsilon_0<c_1 delta_0 sigma_0^2 meets Theorem 1.24's super-regularity hypotheses. The Rademacher sign law is centered, variance one, bounded, and has a fixed controlled second moment as required in Definition 1.3. Also ||epsilon_n||<=n deterministically, hence ||delta_n circ epsilon_n||<=n, by the Frobenius bound. The residual moment bound and the same maximum-entry argument as Step 1 give a summable probability that ||B_n|| exceeds some fixed polynomial, uniformly for z in a fixed disk.

Cook's Theorem 1.24 (current fetched PDF, printed page 15) therefore applies uniformly after conditioning on good masks and polynomial-size cores. It supplies

P(s_min(delta_n circ epsilon_n+B_n)<=n^{-beta}, ||delta_n circ epsilon_n+B_n||<=n^gamma)
<=C sqrt(log n/n),

with beta depending on gamma and constants depending on fixed q and the sign law. Adding the summable core-norm and mask failures gives the same nonsummable rate, not the needed summable one. The reduction is valid; it does not improve the hard-edge error.

### Audit of the neighboring high-confidence theorems

Tao--Vu, arXiv:0805.3167v3, Definition 5.1, printed page 10, explicitly includes an upper bound on E|x|^2. Thus its controlled-second-moment terminology does not cover the unconditioned infinite-variance X. Remark 5.3 says a non-identically distributed extension is 'quite likely' and then states that the paper focuses on iid entries: that is not a theorem with the required quantifiers. Its fixed-vector Theorem 6.4 does allow independent controlled laws, but a global minimum over all directions is an additional step. Moreover the conditioned mask has deterministic zero entries outside the mask, which fail individual controlled nondegeneracy. Theorem 3.2 has an o(1) error as well as the norm-tail term; it is not a summable bound merely by choosing its polynomial parameter large.

Vishesh Jain, arXiv:1908.11255v3, Theorem 1.1, printed pages 4--5, supplies high-confidence bounds for arbitrary large deterministic cores with iid centered variance-one noise. It does not state the same bound for a nonseparable zero-one amplitude mask. Applying it before conditioning would wrongly assume independence of the core and noise; applying it after conditioning would wrongly assume iid noise. No such transfer has been proved here.

Thus Route B reduces a broad atomic benchmark to a concrete structured-noise invertibility question, but the papers inspected do not close it. An improvement of Cook's conditional profile theorem to, for example, n^{-2} error at some polynomial threshold for each fixed polynomial-size core would finish this two-atom subclass by the already-proved concentration argument. This improvement is a remaining question, not an asserted theorem. Entry laws with fewer than two atoms would also require a more general decomposition to obtain a full solution by this route.

## Hostile-referee checks for this renewed attempt

1. Lemma A.1 was reread in the actual survey: it assumes independent nonconstant complex entries and positive fixed truncated variance, not finite variance. Its exact error is c sqrt(log(cs))(t s^2+n^{-1/2}). The norm and scaling substitutions above include the additional n^{-1/alpha} factor.
2. The source's in-probability logarithmic potential input is needed only for Lebesgue-almost every fixed z. Fubini is applied to this full-area set, not to an uncountable intersection of probability-one events.
3. Concentration identifies the deterministic mean without an expectation-uniform-integrability assumption: if |E S_n-ell|>2t along a subsequence, the events |S_n-E S_n|<=t and |S_n-ell|<=t cannot both occur, although their probabilities tend to one. This contradiction proves E S_n->ell.
4. All upper clips are eventually inactive uniformly on each disk by a summable polynomial norm bound. Consequently the lower clipping defect is nonnegative and supported on the hard-edge exceptional set. Without this eventual inactivity the support argument would be invalid.
5. Uniform local L2 bounds concern the TRUE eigenvalue potentials, obtained from fractional eigenvalue moments; they do not claim uniform negative-log integrability of all singular values. Finite eigenvalue singularities have area zero and locally integrable logarithms.
6. The dyadic argument uses nonnegativity of exceptional areas. It establishes vanishing average area, not eventual absence of bad dimensions. The Jordan example checks this exact limitation.
7. The chosen metric is sufficient, and the result holds for any other bounded metric d' inducing weak convergence: continuity at mu gives, for each epsilon>0, a delta>0 such that d(rho,mu)<delta implies d'(rho,mu)<epsilon. If d'<=L, its average is at most epsilon+(L/delta) times the average of d. Let N tend to infinity and then epsilon decrease to zero.
8. The Jordan/cyclic example fails the iid-entry hypothesis and also is not given as principal minors of an iid infinite array. It only disproves a proposed implication from the general potential/concentration inputs. It is not a counterexample to the question.
9. The numerical script second_checks.py checks 15 small Jordan/cyclic cases, the null-vector residual, cyclic singular-value lower bound, and clipped rank-one inequality, plus an exact rational atomic-mixture identity. All checks passed; SECOND_CHECKS.json retains the values. The largest dense matrix is 64 by 64. These finite tests supplement, not replace, the proofs above.
10. CesaroCore.lean is a deliberately limited formalization of the algebraic inequality used to interpolate between dyadic partial averages. The probability, random-matrix and potential arguments are not formally verified. The Lean result will be recorded separately when the single running check finishes.

## Final mathematical gap

The unrestricted source law now has an almost-sure averaged/statistical convergence theorem, in addition to the earlier smoothness and independent-convolution subclasses. To get full-sequence almost-sure convergence, it remains to eliminate sparse exceptional dimensions: for example prove ||S_n-V_n||_{L1(K)}->0 almost surely for every bounded disk K, or obtain a summable fixed-z lower-singular-value tail sufficient for that conclusion. No argument here shows area(B_n)->0 almost surely; only its Cesaro average tends to zero. No counterexample respecting iid entries and the exact source tail/angular hypotheses has been constructed. Verdict remains PARTIAL.


### Additional details of the deterministic stress test

The cyclic spectra converge to the uniform circle law because their test integrals are the Riemann sums (1/n) sum_{k=0}^{n-1} f(exp(2 pi i k/n)) of a continuous periodic function. Both types of event occur infinitely often almost surely: the independent bad-event probabilities sum to infinity, and so do their complementary probabilities. Thus the bounded continuous test min(1,|z|^2) takes spectral integral zero infinitely often and one infinitely often. There is no weak almost-sure limit in this non-iid model. For |z|<=r<1 the cyclic singular values lie in [1-r,1+r], so eventually its clipped and true potentials coincide uniformly. Also |log|1-z^n||<=max(-log(1-r^n),log(1+r^n)), which tends to zero, proving the uniform potential convergence used above. The rank-one clipped bound then proves uniform convergence for the nilpotent matrix too. At n=1 any finite clipped definition, for example S_1=0, may be used; finite initial terms have no effect on the averaged theorem.


### Lean check outcome

CesaroCore.lean passed with exit code 0 and no sorry or native_decide. The only formally checked claim is the algebraic dyadic-interpolation inequality; the random-matrix theorem is checked by the written proof, not formalized.
