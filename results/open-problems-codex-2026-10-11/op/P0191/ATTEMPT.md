# P0191: partial results (2026-10-11)

## Target and normalization

The source is Yi Han, *Brown measure convergence for the spectrum of polynomials in Ginibre matrices*, arXiv:2606.01664v1, 1 June 2026. Theorem 1.3 is on printed/PDF page 3; Question 1.6 is on page 6. The target is: for each fixed nonconstant p in C<x_1,...,x_n>, find positive constants C,c,c_1 and an exponent c_0, and N_0, depending on p, such that for every N>=N_0 and every epsilon>0,

    P(s_min(p(X)-p(0)I)<=epsilon)
       <= C (N^(c_0) epsilon^c + exp(-c_1 N)).

This is the constant-term extension of Theorem 1.3, not merely a high-probability invertibility assertion. Equivalently one can subtract the constant and ask this for nonzero p with p(0)=0, exactly the substantive class highlighted in Question 1.6. Literal inclusion of nonzero constant polynomials would be false; it is not the intended research problem. In the published theorem away from p(0), c_0,c,c_1 depend only on p, while C and N_0 may also depend on z. At the one fixed shift z=p(0), dependence is on p only. No adjoints occur. Definition 1.1 uses entries with independent real and imaginary parts N(0,1/(2N)); throughout these proofs the entry density is (N/pi) exp(-N|z|^2), so E|X_ab|^2=1/N. These arguments do not solve the general noncommutative problem.

## Lemma 1: a uniform deterministic-mean Gaussian bound

For every deterministic complex N by N matrix D, scalar a != 0, and t >= 0,

    P(s_min(aX+D) <= t) <= min(1, N^3 t^2 / |a|^2).

Proof. Write M=aX+D with columns C_1,...,C_N, and let H_j be the span of all columns other than C_j. If s_min(M)<=t, compactness of the unit sphere gives a unit vector v with ||Mv||<=t. Some j has |v_j|>=1/sqrt(N), because sum |v_j|^2=1. Projecting Mv onto H_j perpendicular gives |v_j| dist(C_j,H_j)<=t. Thus dist(C_j,H_j)<=sqrt(N)t for some j.

Condition on all other columns. Their span has dimension at most N-1, so choose a unit u in H_j perpendicular. A measurable choice exists: use the orthogonal projection onto H_j perpendicular, select its first nonzero projected coordinate vector, and normalize it; the projections are Borel functions, obtained separately on the finitely many rank strata. Then |u* C_j|<=dist(C_j,H_j). The conditional variable u* C_j is circular complex Gaussian with variance |a|^2/N and a deterministic mean. Its planar density is everywhere at most N/(pi |a|^2). Consequently the probability it lies in a disk of radius sqrt(N)t is at most N^2 t^2/|a|^2. Sum over the N columns. This also holds for t=0 (a point has planar Lebesgue measure zero). The probability bound by 1 is automatic. QED.

The lemma requires no norm bound on D, and D may be random provided it is independent of X: condition on D and integrate the same uniform inequality.

## Proposition 2: a generator appearing only as an additive linear term

Suppose p(x_1,...,x_k)=a x_j+q(x_1,...,x_(j-1),x_(j+1),...,x_k), where a != 0 and q is any fixed holomorphic polynomial. Then

    P(s_min(p(X)-p(0)I) <= t) <= min(1, N^3 t^2/|a|^2).

Proof. Condition on all generators except X_j. The matrix D=q(X_others)-q(0)I is independent of X_j. Apply Lemma 1 and integrate. QED. For each A>0, choosing B>(A+3)/2 gives probability O(N^(-A)) at t=N^(-B). This proves a genuine special case including arbitrary nonlinear q, e.g. x_1+[x_2,x_3]. It is a sufficient hypothesis, not a claim about all polynomials with a nonzero linear coefficient: additional appearances of x_j destroy the independence used here.

## Lemma 3: product propagation without independence

For deterministic square matrices A,B,

    s_min(AB) >= s_min(A) s_min(B).

Proof. For every vector v, ||ABv||>=s_min(A)||Bv||>=s_min(A)s_min(B)||v||; take the minimum over unit v. Iterate for r factors. If every factor has least singular value greater than u, the product has least singular value greater than u^r. Therefore, for arbitrarily dependent random factors F_1,...,F_r,

    P(s_min(c F_1 ... F_r)<=t)
       <= sum_l P(s_min(F_l)<=(t/|c|)^(1/r)),

for c != 0 and t >=0. The contrapositive uses strict inequalities and so handles the closed lower-tail event correctly. QED.

If each factor has the form a_l X_(j_l)+q_l(X_other generators), with a_l != 0 and no X_(j_l) in q_l, Lemma 1 gives

    P(s_min(c product F_l)<=t)
       <= min(1, N^3 (t/|c|)^(2/r) sum_l |a_l|^(-2)).

Factors may share generators and may repeat. This proves the target for polynomials whose constant-subtracted polynomial has this factorization; a product factorization of p alone does not automatically give one for p-p(0).

## Proposition 4: every nonconstant polynomial in one generator

Let f in C[z] be nonconstant of degree d with leading coefficient c. By the fundamental theorem of algebra, f(z)-f(0)=c product_(l=1)^d (z-rho_l), counting multiplicities. Substituting a matrix for z is an algebra homomorphism, hence

    f(X)-f(0)I = c product_l (X-rho_l I).

Lemma 1 with a=1 and D=-rho_l I and Lemma 3 imply

    P(s_min(f(X)-f(0)I)<=t) <= min(1, d N^3 (t/|c|)^(2/d)).

The same proof works for any scalar shift f(X)-zI. Repeated roots and repeated factors cause no difficulty because the union bound needs no independence. For each A>0, choosing B>d(A+3)/2 gives O(N^(-A)). QED.

## Proposition 5: a Gaussian generator between random invertible factors

Let A,B,C be matrices measurable with respect to generators other than X_j. Suppose for 0<u<=1,

    P(s_min(A)<=u) <= K_A N^(a_A) u^(alpha_A) + E_A(N),
    P(s_min(B)<=u) <= K_B N^(a_B) u^(alpha_B) + E_B(N),

with positive alpha_A,alpha_B. Put beta=(1/alpha_A+1/alpha_B+1/2)^(-1) and a=max(a_A,a_B,3). For 0<t<=1,

    P(s_min(A X_j B+C)<=t)
      <= (K_A+K_B+1) N^a t^beta + E_A(N)+E_B(N).

Proof. Set u_A=t^(beta/alpha_A), u_B=t^(beta/alpha_B), and v=t^(beta/2). Their product is t by the definition of beta, and they belong to (0,1]. Outside the two exceptional events s_min(A)<=u_A and s_min(B)<=u_B, both matrices are invertible. Condition on all other generators there. Then

    A X_j B+C = A (X_j+A^(-1) C B^(-1)) B.

If the middle factor has least singular value greater than v, Lemma 3 makes the product least singular value greater than u_A v u_B=t. Lemma 1 bounds the conditional exceptional probability by N^3 v^2=N^3 t^beta, regardless of the potentially enormous norm of A^(-1) C B^(-1). Integrating over the good event and adding the two marginal exceptional probabilities gives the result; use N>=1 to replace each N exponent by a. No independence between A,B,C is required. QED.

For t>1 one can increase the fixed constant so the right side is at least 1 (a>=3). If E_A and E_B are exponential in N, so is their sum. Thus this proves a closure principle for the exact source-type estimate, rather than just qualitative invertibility.

In particular, p=x_2 x_1 x_3+q(x_2,x_3), with arbitrary q, satisfies at its constant term

    P(s_min(p(X)-p(0)I)<=t) <= min(1,3 N^3 t^(2/3)),

by taking A=X_2, B=X_3, C=q(X_2,X_3)-q(0)I and applying Lemma 1 to A,B. The bound holds for all t>=0: the case t=0 follows by letting t decrease to zero in the positive-t estimate. This includes higher-degree sums such as x_2 x_1 x_3+x_3 x_2 x_3 x_2, not merely a monomial or a univariate polynomial.

The same construction applies recursively when the two exterior polynomials already have such bounds and the selected generator appears nowhere else. It does not apply to x_1 x_2 x_1+x_2 x_1 x_2, because neither generator can be isolated as one sandwiched occurrence with an independent remainder.

## Proposition 6: qualitative invertibility with nonzero abelianization

Write r=p-p(0), and suppose its abelianization r_ab, obtained by replacing the generators by commuting scalars, is not the zero polynomial. Then for every N>=1, r(X) is invertible almost surely.

Proof. A nonzero polynomial over the infinite field C takes a nonzero value at some scalar tuple lambda. To verify this assertion without any genericity assumption, induct on the number of variables: regard the polynomial as a polynomial in the last variable; choose the other variables so a nonzero coefficient remains nonzero by induction, then avoid the finitely many roots of that univariate polynomial. At the deterministic matrix tuple X_i=lambda_i I_N, the polynomial r evaluates to r_ab(lambda)I_N. Its determinant is r_ab(lambda)^N !=0. Thus det(r(X)) is a nonzero ordinary holomorphic polynomial in the n N^2 complex entry variables.

The zero set of a nonzero complex polynomial has Lebesgue measure zero. Indeed, the one-variable assertion follows from finiteness of roots. In more variables expand in the last variable and select a nonzero coefficient polynomial. Outside its zero set (null by induction), each last-variable fiber has finitely many roots, a null set in C. The exceptional base set is null and its product with C is null, by restricting to bounded boxes and applying Fubini, then taking a countable union. Fubini on the remaining fibers establishes the claim. The joint Ginibre law has a density on C^(n N^2), so it assigns zero probability to that zero set. QED.

In particular the representative cubic r=x_1 x_2 x_1+x_2 x_1 x_2 is invertible almost surely at every N (take lambda_1=lambda_2=1, giving r_ab=2). This does not establish a polynomial lower tail for it. For each fixed N, continuity of probability for the decreasing events {s_min<=t} gives a limit zero as t decreases to zero, but supplies neither an exponent nor constants uniform in N. Polynomials with zero abelianization are outside this qualitative proof; they are not thereby shown singular.

## Proposition 7: a dominated linear Gaussian channel with a repeated generator

For any holomorphic q in x_2,x_3 and any |lambda|<=1/128, let

    p=x_1+lambda x_2 x_1 x_3+q(x_2,x_3).

Then with gamma=16-4 log(9)>0, every N>=1 and t>=0 satisfy

    P(s_min(p(X)-p(0)I)<=t) <= 4 N^3 t^2+2 exp(-gamma N).

This has exactly the source's required form and permits the distinguished generator to appear twice, unlike Proposition 2.

Proof of the norm cutoff used below. The complex unit sphere has a 1/4-net of cardinality at most 9^(2N): take a maximal 1/4-separated set; disjoint real 2N-dimensional balls of radius 1/8 around its centers are contained in the radius 9/8 ball, so volume comparison bounds their number by 9^(2N); maximality gives the net. Compactness ensures a finite maximal set, or the same volume bound terminates greedy selection. For any matrix X choose unit u,v attaining its operator norm in |u*Xv| and approximate both by the net. The approximation error is at most (1/4+1/4)||X||. Thus ||X||>8 forces some net pair to have |u_0*Xv_0|>4. For each fixed pair this variable is circular complex Gaussian of variance 1/N (expand its linear combination of independent entries), with tail P(|g|>4)=exp(-16N), obtained by integrating the density in polar coordinates. A union bound over at most 9^(4N) pairs gives P(||X||>8)<=exp(-gamma N).

Now condition on X_2,X_3. On the good event ||X_2||,||X_3||<=8, the complex-linear operator on matrices equipped with Frobenius norm

    T(H)=H+lambda X_2 H X_3

satisfies ||T(H)||_F>=(1-|lambda| ||X_2|| ||X_3||)||H||_F>=(1/2)||H||_F. Here ||A H B||_F<=||A|| ||B|| ||H||_F follows by applying the operator-norm inequality to columns for left multiplication and to rows for right multiplication. In vectorized coordinates the covariance of T(X_1) is TT*/N, hence is at least I/(4N). The equivalence with the lower singular-value bound follows from the singular value decomposition (T*T and TT* have identical singular values, since T is square).

On an auxiliary finite-dimensional Gaussian probability space, form an independent normalized Ginibre Y and a centered circular Gaussian vector Z of covariance (TT*-I/4)/N, reshaped as a matrix. This covariance is positive semidefinite: diagonalize it unitarily and multiply independent standard circular Gaussians by the square roots of its nonnegative eigenvalues. Then Y/2+Z has covariance TT*/N, the same as T(X_1), and has the same distribution. To check this last statement, both vectors have zero mean and zero complex pseudocovariance E[gg^T]. If Sigma=E[gg*] and this pseudocovariance vanishes, expand g=x+iy to obtain the real covariance of (x,y): Sigma_real=(1/2) [[Re Sigma,-Im Sigma],[Im Sigma,Re Sigma]]. The real characteristic function at a real vector w is exp(-w^T Sigma_real w/2). This formula follows for independent standard real Gaussians by multiplying their one-dimensional characteristic functions, and for linear transforms by substitution. The two real covariance matrices agree, so the characteristic functions agree. This uses only finite-dimensional Gaussian linear algebra.

Set D=q(X_2,X_3)-q(0)I. Conditional on Z and the other generators, Lemma 1 with a=1/2 bounds the lower tail of Y/2+Z+D by 4 N^3 t^2, uniformly in Z+D. Thus the same conditional bound applies to T(X_1)+D on the good event. The probability of its complement is at most 2 exp(-gamma N), by the cutoff estimate for the two matrices. Integrating proves the stated result. No norm bound is needed on q. QED.

The small coefficient hypothesis is essential to this proof: without it the conditional covariance can degenerate. We do not claim the result for arbitrary lambda by this argument, nor does this supply a small-parameter reduction of an arbitrary polynomial.

## Hostile-referee checks and unsuccessful reductions

1. A nonzero *constant* p makes p(X)-p(0)I identically zero. A positive extension must exclude constant polynomials. This boundary observation is not a counterexample to an intended nonconstant formulation until the exact source wording is checked.
2. At N=1 a commutator is identically zero. Thus an estimate with no dimension exception cannot hold for every nonzero free polynomial. This does not refute a large-N statement.
3. A lower bound for each monomial does not bound their sum: A+(-A)=0 even when A is invertible. Our product argument never applies to an arbitrary sum.
4. Knowing almost-sure invertibility for each N supplies no polynomial dependence on N. Even a deterministic invertible matrix e^(-N)I illustrates the missing rate. Determinant polynomial anti-concentration has degree proportional to N and typically an exponent of order 1/N; that estimate alone does not give a fixed power tail in t.
5. Bounds at fixed nonzero shifts cannot simply be passed to zero if their constants depend on that shift. Lipschitz continuity |s_min(M-zI)-s_min(M)|<=|z| would require a bound uniform at a shift of order t.
6. The row/column argument requires independent Gaussian columns conditional on the deformation. In a general p(X) they are correlated and are not conditionally Gaussian. For [X,Y], conditioning on Y gives a structured linear Gaussian matrix; its noise need not have full independent-column covariance. Proposition 2 does not apply.

## Numerical verification

`experiments.py` (NumPy, seed 191) uses 160 samples at each N=1,2,4,8,16, and normalized complex Gaussian entries. It samples X+[Y,Z], X^3-X, [X,Y], and XYX+YXY; the full quantiles and empirical lower tails are in `numerics.json`. It checks s_min(XY)>=s_min(X)s_min(Y) and min_j dist(C_j,span(other columns))<=sqrt(N)s_min(M) on 800 instances each. The largest product-inequality violation is 4.44e-16 (roundoff); all column-distance assertions passed at absolute tolerance 1e-9. All 160 scalar commutators vanish exactly, confirming the N_0 caveat. Runtime reported by the script was 395.3 seconds and arrays were at most 16 by 16; memory is far below 1 GB. These observations are diagnostics, not evidence of a uniform exponent for arbitrary p. No numerical result is promoted to a proof.

`ProductThreshold.lean` formalizes only the two-factor real threshold implication a*b<=u*u => a<=u or b<=u for u>=0. It contains no sorry or native_decide. `lake env lean ~/brain_workers/TRIO_1011/op/P0191/ProductThreshold.lean`, run from ~/lean_verify with a 3600-second subprocess timeout, exited 0 after 928.6 seconds. `#print axioms` returned only propext, Classical.choice, Quot.sound. Output is saved in `lean_check.txt`. The analytic/probabilistic results above are written proofs, not Lean-verified theorems.

`covariance_checks.py` (seed 7191) tests Proposition 7's column-major vectorization T=I+lambda(B^T tensor A), its deterministic lower singular-value bound, and positive semidefiniteness of TT*-I/4, on five instances each at N=2,4. All ten checks passed with tolerance 1e-12; results are in `covariance_checks.json`. Reported computation time was 0.016 seconds. These check the potentially fragile transpose/covariance bookkeeping; the proof itself uses a norm inequality valid for all sizes.

## Remaining gap

Second attempt (2026-10-11): two genuinely different approaches are recorded in RETRY.md. The pursued approach combines conditioning on a Gaussian generator, exact Ginibre eigenvalue correlations, and expected pseudospectral area. Complete proofs are in [RETRY_PROOF.md](RETRY_PROOF.md). It proves, for every k>=1,

    P(s_min(X^kY+YX^k+Q(X,Z)-Q(0)I)<=epsilon)
       <=(64k+83)N^4 epsilon^(2/(k+3))+exp(-(16-4log9)N),

where Q does not use Y. More generally it proves a source-type bound with exponent 2/(D+3) for sum a_(r,s)X^rYX^s+Q(X,Z), where h(u,v)=sum a_(r,s)u^rv^s has total degree D>=1 and h(z,z) is not identically zero. This is a stronger special case without a small-coefficient restriction. The proof explicitly includes diagonal eigenvalue pairs, controls the whole eigenvector diagonalizer through spectral projections, handles variable leading coefficients in h, and restores an independent Gaussian channel by covariance decomposition. It does not prove arbitrary-polynomial bounds.

The further masked-Gaussian argument in RETRY_PROOF.md, Lemma F and Theorem G, removes the requirement h(z,z) not identically zero. For any nonzero h of total degree D>=1, every N>=2, and epsilon>0, it proves

    P(s_min(sum a_(r,s)X^rYX^s+Q(X,Z)-Q(0)I)<=epsilon)
       <=C_poly N^4 epsilon^(2/(2D+7))+C_exp exp(-cN),

with explicit coefficient-dependent constants, c=min(16-4log9,2-log2)>0, and Q excluding Y. This includes the cubic [X,[X,Y]] and other zero-abelianization channels. The previously identified commutator-channel kernel obstructs the full-covariance proof, but is now covered by an independent off-diagonal Gaussian baseline with a norm-controlled deformation. The general polynomial gap below remains.

For a general nonconstant free polynomial p of degree at least three, obtain the exact uniform-in-epsilon estimate stated above. No such general proof or asymptotic counterexample is established here. Degree two is already covered by Cook--Guionnet--Husson as explicitly stated by Han; [x_1,x_2] is outside our elementary special-case proofs but is not an unresolved instance. A representative instance outside both the degree-two result and our elementary proofs is x_1 x_2 x_1+x_2 x_1 x_2.

Final proof audit: all quantitative special cases have fixed, dimension-independent positive epsilon exponents. Lemmas 1--4 give bounds without an exponential error, which is stronger than the required form in their classes. Proposition 5 retains existing exponential errors; Proposition 7 has an explicitly derived exponential error. All constants are attached to a fixed polynomial, with N_0=1 in the direct special cases. The mean/deformation is independent of the exposed Gaussian generator each time it is used. Proposition 7 instead proves a new independent-Gaussian decomposition after conditioning, and does not treat the original correlated entries as independent. Product-factor dependence is handled by marginal bounds and a union bound only. The scalar-evaluation proof of Proposition 6 is deliberately kept qualitative. None of these steps yields the bound for the representative cubic or for arbitrary singular-constant-term linearizations. The natural next research step is a quantitative least-singular-value theorem for full noncommutative-rank Gaussian pencils with singular deterministic coefficient; Han's identity-coefficient theorem alone does not provide it.
