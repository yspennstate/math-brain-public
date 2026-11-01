# Growing-depth stopping overcomes the transitive remainder obstruction

Research continuation for Yitzchak Shmalo — 20 September 2026.

**Full FEI is not proved here.** The preceding report refuted every fixed-depth local induction on the arithmetic remainder. This report proves that its transitive obstruction family does admit a constant-paid, dimension-growing physical restriction tree. The maximum depth is logarithmic in the dimension, and the expected number of queries is smaller by a logarithmic factor. An exact binomial-carry formula explains the mechanism. This repairs the proposed stopping method on that family, not on arbitrary Boolean functions. FEI for disjoint tribes was already known; it is not re-announced as new.

The preceding package's checker had not completed: its `EXECUTION.json` records a large-integer serialization failure and `checker_status=NOT_CONFIRMED`. In this continuation the display routine was replaced by outward dyadic rounding, without changing any mathematical assertion. The repaired checker completed and generated the formerly missing certificates and verification output. Separate replay results and source hashes are recorded in the delivery files. A successful finite checker is not an independent proof audit or a formalization.

## 1. Notation and the precise question

For Boolean signs, entropy is in bits and Fourier coefficients are normalized. For each nonzero Fourier magnitude a, let A_a be its label set, V_a the inverse unnormalized Walsh transform of its sign mask, and r_a the minimum 2-adic valuation of a nonzero V_a value. Define

    p_a = |A_a| a^2,   R(f) = sum_a p_a r_a,
    D(f) = H(f)/2 - R(f).

The preceding spectral-lattice proof gives R>=0 and D>=0. The previous isolation report proves that the optimal universal constants satisfy

    sup_f H(f)/I(f) = 2 sup_f D(f)/I(f).

These are suprema over all Boolean functions and dimensions; the equality is not a pointwise entropy bound. It is not reproved or counted as a new contribution here.

For a finite physical restriction tree T, let

    Q_T = I(f) - E I(leaf)
        = sum_internal_nodes w_v Inf_{queried coordinate}(f_v).

The weights are the probabilities of reaching the nodes under uniform physical inputs. Restriction cannot increase Fourier entropy on average. One elementary proof writes each parent Fourier pair as (u,v), the two child coefficients as u+v,u-v, and decomposes the entropy decrement into a nonnegative binary conditional entropy plus a nonnegative Jensen–Shannon divergence. These inherited identities apply to arbitrary adaptive trees.

The family from the preceding obstruction is

\[
T_{k,m}(x)=2\prod_{j=1}^{m}(1-\mathbf1_{\{x^{(j)}=0^k\}})-1,
\qquad N=2^k,\quad q=1-1/N.
\tag{1}
\]

The main root is m=N-1. There are n=k(N-1) physical variables. All coordinates are relevant and equivalent. The preceding report proves R(T_{k,N-1})=0 and an unbounded remainder-decrement/influence ratio at every coordinate.

## 2. Exact valuation of every band

For 1<=m<N and a Fourier label meeting exactly b blocks, the nonempty-band magnitude, sign, multiplicity and mass are

\[
a_b=2N^{-b}q^{m-b},\qquad (-1)^b,
\quad {m\choose b}(N-1)^b,
\quad p_b=4{m\choose b}N^{-b}q^{2m-b}.
\tag{2}
\]

For N>=8 the head |2q^m-1| is distinct from every nonempty band. Indeed, multiplying a possible equality by N^m and reducing modulo N-1 gives a head residue +/-1, whereas a band has residue 0 or +/-2. Different b have different magnitudes. The head's mask is a single character and has valuation zero.

**Theorem 2.1.** Suppose N>=8 and 1<=m<N. For every nonempty band,

\[
\boxed{r_b(k,m)=\nu_2{m\choose b}.}
\tag{3}
\]

Thus, if B has the binomial distribution with parameters (m,1/N),

\[
\boxed{R(T_{k,m})=4q^m\,\mathbb E\nu_2{m\choose B}.}
\tag{4}
\]

The value at B=0 contributes zero.

**Proof.** For a block set

    Z_j = sum_{S_j nonempty} chi_{S_j}
        = N 1_{x^(j)=0} - 1.

Up to a global sign, the b-band mask is e_b(Z_1,...,Z_m). Writing eta_j=1_{x^(j)=0}, its multilinear coefficient at any j-element set of eta variables is

    N^j (-1)^(b-j) binom(m-j,b-j).

Every eta assignment is physically realizable. The largest common power of two dividing all values of an integer multilinear polynomial is also the largest common power dividing all its coefficients: evaluations are integer sums of coefficients, and coefficients are integer linear combinations of evaluations. Therefore

\[
r_b=\min_{0\le j\le b}\left(kj+\nu_2{m-j\choose b-j}\right).
\tag{5}
\]

The j=0 term is less than k. To see this, the identity nu_2(t!)=t-s_2(t), where s_2 counts binary ones, follows by summing floor(t/2^h). Hence nu_2 binom(m,b) counts the binary carries in b+(m-b)=m. Because m<2^k, there is no outgoing carry from the top bit and at most k-1 carries. All j>=1 terms in (5) are at least k. This proves (3). Multiplying the binomial probabilities by 4q^m gives exactly (2), proving (4). No large truth table is needed for this identity. QED.

The carry identity and the formula for nu_2(t!) are standard arithmetic; their application to these Fourier magnitude masks is the step used here.

## 3. Removing a power-of-two number of blocks postpones the first costly band

Let L be a power of two with L<N-1, and put m=N-1-L. Then

\[
\boxed{r_b(k,N-1-L)=\nu_2\left(1+\left\lfloor b/L\right\rfloor\right).}
\tag{6}
\]

Indeed m is the k-bit complement of L. The digit-sum formula gives

    nu_2 binom(m,b) = s_2(b)+1-s_2(b+L).

The last expression counts the carries produced by adding the single power of two L to b, namely the number of trailing ones of floor(b/L). This is nu_2(1+floor(b/L)). There is no overflow because b+L<=N-1.

In particular all bands with b<L have valuation zero. Also

    nu_2(1+floor(b/L)) <= floor(b/L) <= binom(b,L)

when b>=L; both sides vanish in the needed inequality when b<L. Applying the binomial factorial-moment identity to (4) yields

\[
\boxed{
R(T_{k,N-1-L})
\le4q^{N-1-L}{N-1-L\choose L}N^{-L}
\le\frac{4q^{N-1-L}}{L!}.
}
\tag{7}
\]

This is the new useful payment: after removing L blocks, the arithmetic cost is supported on a binomial upper tail, rather than on the positive-mass first band created by removing one block.

There is an exact calibration. If L tends to infinity through powers of two and L^2/N tends to zero, then

\[
\boxed{
R(T_{k,N-1-L})
=\frac{4e^{-2}}{L!}
\left[1+O\left(\frac1L+\frac{L^2}{N}\right)\right].
}
\tag{8}
\]

For the proof, the leading b=L band has valuation one. Its mass is

    p_L=4 binom(N-1-L,L) N^-L q^(2(N-1-L)-L).

For b=L+s, the band-mass ratio is at most (L+1)^(-s), since (N-1-L)/(Nq)<=1. Its valuation is at most 1+s/L. The sum of all higher contributions is therefore O(p_L/L). Finally the binomial product equals (1/L!)[1+O(L^2/N)] and the q-power equals e^-2[1+O(L/N)]. These estimates prove (8). They are analytical, not inferred from the finite calibration table.

## 4. A dimension-growing tree with a constant remainder payment

**Theorem 4.1.** Let k>=6, N=2^k and f=T_{k,N-1}. Let L be the smallest power of two with L!>=N. There is an explicit adaptive physical restriction tree T satisfying

\[
\boxed{
\max\operatorname{depth}(T)\le4L+8k\le16k,
\qquad \mathbb E\operatorname{depth}(T)\le2L,
}
\tag{9}
\]

and

\[
\boxed{0<Q_T,\qquad D(f)-\mathbb E D(leaf)\le5Q_T.}
\tag{10}
\]

Thus the maximum depth is O(log n), and the expected query count is O(log n/log log n), for n=k(N-1). The coefficient five applies to this family and this procedure only. It is not a universal theorem for arbitrary Boolean f, and must not be converted into a general FEI coefficient ten.

### 4.1 The uncapped block procedure

Choose L distinct blocks. Inspect each chosen block, querying its bits until the first one appears. A one disables that block's zero test, so move to the next chosen block. If all k bits of a block are zero, stop: the function is the constant -1. Stop after L blocks have been disabled.

Every nonconstant leaf is T_{k,N-1-L}, up to irrelevant variables. The probability of this outcome is q^L. The other leaves are constant. The expected number of queries is at most 2L, because a block inspection is dominated by a geometric(1/2) variable of mean two.

Set m=N-1 and M=m-L. Since

    I(T_{k,m}) = (2km/N) q^(m-1),

the full procedure consumes exactly

\[
\boxed{Q=I(T_{k,m})-q^L I(T_{k,M})
=\frac{2kL}{N}q^{m-1}.}
\tag{11}
\]

The choice of L gives 8<=L<=N/8 and L<=2k. The first lower bound follows from 4!<64. For L<=N/8, the available dyadic number N/8 is at least eight and its factorial is at least 8(N/8)=N. For L<=2k use k!>=2^k and take a dyadic number between k and 2k.

### 4.2 Entropy decrement of the full procedure

Write h(t)=-t log_2 t and

\[
A_k=-2q^2\log_2 q+(2q/N)k,
\qquad c(z)=h((2z-1)^2)-4h(z^2)-8(z-z^2).
\]

Direct expansion of the product spectrum gives

\[
H(T_{k,m})=4m q^{m-1}A_k+c(q^m).
\tag{12}
\]

This is the preceding report's homogeneous-entropy identity, retained with the same normalization. To derive it, each factor u=1-1_{0^k} has squared norm q and homogeneous Fourier entropy A_k. Their product has homogeneous entropy m q^(m-1) A_k. Multiplication by two scales nonempty masses by four, contributing an extra -8 times their original total mass. Correcting the head coefficient gives (12).

Both z=q^m and y=q^M lie in [1/3,1/2]. The lower endpoint follows from q^(N-1)>e^-1>1/3. For the upper endpoint, M>=7N/8-1, so q^M<=exp(-M/N)<1/2 for N>=64.

On this interval,

\[
|c(z)|\le6,\qquad |c'(z)|\le12.
\tag{13}
\]

Here are explicit bounds, to avoid relying on a numerical plot. The entropy summand has maximum 1/(e ln2)<1, and four times that maximum is less than three; also 8z(1-z)<=2. This proves the first inequality. For the derivative put x=1-2z in [0,1/3]. The three absolute derivative terms are bounded respectively by

    8/(e^(3/2) ln2) < 3,
    [8/(3 ln2)](2 ln3-1) < 5,
    8/3 < 3.

These follow by differentiating x(-2 ln x-1), and z(-2 ln z-1), respectively. The elementary inequalities ln2>2/3, ln3<9/8 and e^(3/2)>4 suffice for the displayed strict bounds. Thus twelve is conservative.

Since z=q^L y and y<=1/2,

    |c(z)-q^L c(y)| <=12(1-q^L)<=12L/N.

The other part of the entropy decrement, divided by Q in (11), is

    2N A_k/k <=4+4/(k ln2),

using -ln q<=1/(Nq). Also Q>=2kL/(3N). It follows that

\[
\frac{H(T_{k,m})-q^L H(T_{k,M})}{Q}
\le4+\frac{4/\ln2+18}{k}<8.
\tag{14}
\]

The last inequality uses k>=6 and ln2>2/3.

### 4.3 Remainder payment before capping

At the root R=0. Equation (7) and L!>=N give

\[
\frac{q^L R(T_{k,M})}{Q}
\le\frac{2Nq}{kL L!}\le\frac2{kL}\le\frac1{24}.
\tag{15}
\]

Therefore

\[
D(f)-\mathbb E D(leaf)
=\frac12\bigl[H(f)-\mathbb E H(leaf)\bigr]+\mathbb E R(leaf)
\le\frac{17}{4}Q.
\tag{16}
\]

The proof actually gives a slightly smaller numerical coefficient, but no sharpness claim is needed.

### 4.4 Cap the maximum depth

Cap the procedure after d=4L+8k queries. Its uncapped query count is dominated by a sum of L independent geometric(1/2) variables G_j. Since

    E 2^(G_j/2)=1+sqrt(2)<3,

Markov's inequality gives

\[
\Pr(\text{unfinished at the cap})\le3^L2^{-d/2}\le N^{-4}.
\tag{17}
\]

Let epsilon=n/N^4=k(N-1)/N^4. At a prematurely stopped leaf both I and R are at most n. The additional full-procedure influence expenditure is therefore at most epsilon, so

    Q_T >= Q-epsilon.

Entropy cannot increase on average under further restrictions, and R is nonnegative. Hence the capped remainder drop is at most the full remainder drop plus epsilon:

    D(f)-E D(capped leaf) <= (17/4)Q+epsilon.

But epsilon/Q <=3/(2 L N^2)<1/16. Dividing shows

    [(17/4)Q+epsilon]/[Q-epsilon] <5.

This proves (10). Capping preserves the expected-depth bound. The estimate L<=2k proves the maximum-depth bound in (9). Q_T>0 because the root query is relevant. QED.

For the growth rate, the elementary integral bounds for log(L!) show that the least integer meeting L!>=N is of order ln N/ln ln N. Rounding to a power of two costs less than a factor two. Since ln n=ln N+O(ln ln N), the claimed expected-query asymptotic follows. This is an upper bound on expected depth, not a lower bound for all possible procedures.

## 5. The preceding obstruction also rules out some growing depths

The earlier lower bound was stated for fixed d, but its proof gives the explicit inequality for every pair (N,d) with N>=16(d+1):

\[
\frac{D(T_{k,N-1})-\mathbb E D(leaf)}{Q_T}
\ge\frac{N}{4d\,d!\,8^d}
\tag{18}
\]

for every nontrivial physical restriction tree of maximum depth at most d.

Consequently, fix any eta in (0,1). If

\[
d\le(1-\eta)\frac{\ln N}{\ln\ln N},
\]

then for all sufficiently large N the right side of (18) is at least N^(eta/2), and diverges. Indeed log(4d d! 8^d)<=d log d+d log8+O(log d)<=(1-eta+o(1))log N. This is a direct quantitative corollary of the inherited bound, not an independent new obstruction construction.

Thus for this family constant-paid stopping cannot have uniformly bounded maximum depth, or maximum depth below this slowly growing scale. The new construction succeeds with maximum depth O(log N) and expected depth O(log N/log log N). There remains a logarithmic-factor gap between the lower and upper bounds on **maximum** depth; no matching lower bound on expected depth is claimed.

## 6. A different full-scope attempt: normalized spectral information

I also examined a continuous, information-theoretic quantity rather than a minimum divisibility order. For a coordinate i, each parent pair (u_T,v_T) gives

    w_T=u_T^2+v_T^2,   m_T=min(u_T^2,v_T^2),   M=sum_T m_T.

For 0<M<=1/2, define probability laws rho_T=m_T/M and sigma_T=(w_T-m_T)/(1-M). Their mixture is w. The inherited erasure entropy has the exact identity

\[
\boxed{
B_i(f)=h_2(M)-M D_{KL}(\rho\|w)-(1-M)D_{KL}(\sigma\|w).
}
\tag{19}
\]

All KL divergences are in bits. This is the ordinary mutual-information identity for the binary mixture with posterior probability m_T/w_T. At M=0 the entropy is zero.

Using the existing JS bound for the restriction remainder and h_2(M)<=M log_2(1/M)+M/ln2 gives

\[
\Delta_iH(f)
\le M\left[\log_2(1/M)+3/\ln2-D_{KL}(\rho\|w)\right].
\tag{20}
\]

This retains the logarithmic information that the earlier scalar affinity cap discards. In a one-point defect, the minority law spreads over fibres whose original probabilities are tiny; the KL term cancels the spurious large marginal-entropy charge. In a bent-background rare split the same cancellation need not occur. No universal lower bound on the KL term sufficient for a paid selector was proved. Equation (19) is a standard identity written in the project notation, not a newly discovered entropy theorem.

The exact finite checker tests (19). Those tests are not evidence of a missing universal inequality. This route remains an attempted alternative, not an additional completed solution.

## 7. Why this is not full FEI

If every nonconstant Boolean function admitted a nontrivial physical restriction tree with

    D(f)-E D(leaf) <= K [I(f)-E I(leaf)]

for one universal K, then induction on dimension would give D<=K I. The preceding isolation theorem would then give FEI with constant 2K. That universal existence statement is unproved.

The theorem here constructs such a tree with K=5 only for T_{k,N-1}. It establishes that the previously refuted bounded-depth version cannot be used to dismiss all dimension-growing procedures. It does not prove that every surviving dependent high-degree function can be treated in the same way, nor that a universal logarithmic-depth selector exists. The original full erasure bound also remains unpaid.

FEI for disjoint tribes, and restriction/stopping-tree methods more generally, already appear in the literature. The new-to-this-project result is the exact magnitude-mask valuation, factorial suppression, and the constant-paid logarithmic-depth procedure for the arithmetic remainder that defeats its own previous fixed-depth obstruction. Publication priority has not been established.

## 8. Reproducibility, sources and scope

The new `verify_growing_stopping.py` uses integer Walsh transforms and outward rational logarithm enclosures. It checks the exact mask valuations against all physically possible zero-block counts in finite cases, direct truth tables, the entropy and query-budget formulae, exact finite-state query laws including capping, the factorial remainder bounds, and the normalized spectral information identity. Actual counts are in `verification.json`; no huge Boolean cube is enumerated merely because an exact parameter formula is evaluated.

The primary mathematical predecessor is the actual conversation file `FEI_Remainder_Isolation_2026-09-20.md`, read in full, together with the code and the failed execution record in its actual ZIP. The source spectral-lattice report is `proofnet24/P03-fei/continuations/2026-09-20-spectral-lattices/REPORT.md`, blob `9f981c30a0c8a80b3cbad92eb531d17c64688e03`. The repository entrypoint was read at blob `ab4f7102c5bb2c629a1e88d296dcf8c8fac3e1f5`.

The companion `scheduled-continuation/runs/2026-09-20/2026-09-20T14-08-00Z__report.md`, blob `d32dc70753dafd22b53f03253e3485da5a703d47`, was consulted in its dependency-bank and projected-entropy sections. No uninspected later portions are used as premises. Its projection payment does not settle the inside-block allocation cost.

Primary literature checked on 20 September 2026: Gonzalez–MacManus–Pereyra, *Further evidence towards the Fourier Entropy-Influence conjecture*, arXiv:2606.00246v2, revised 9 June 2026; and O'Donnell–Tan, *A composition theorem for the Fourier Entropy-Influence conjecture*, arXiv:1304.1347. Their abstract pages were read for status and attribution; no uninspected result from them is used as a premise of the new arithmetic argument. The former explicitly records tribes as already known examples and treats unrestricted FEI as a conjecture.

No schedules, ownership, permissions, visibility, or native atlas metrics are changed. Delivery status is recorded separately and will not be inferred from merely creating local files.
