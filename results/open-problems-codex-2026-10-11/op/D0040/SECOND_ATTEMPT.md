# D0040 — additional serious attempt, 2026-10-12

## Remaining gap read from ATTEMPT.md

The previous attempt proves a fixed-rectangularity beta-Laguerre construction and failure of the canonical Dirichlet-weight quartic model. It leaves existence/classification of arbitrary tridiagonal leading-minor couplings for other Dyson potentials unresolved. An arbitrary coupling can choose spectral weights depending on the eigenvalues; the canonical quartic failure does not rule that out.

## Two approaches not previously pursued

1. **Compact-support construction via canonical moments / the CS decomposition.** The finite beta-Jacobi bidiagonal model has two sets of independent beta-distributed angles. Reverse and transpose its factor, rather than reverse the Gram matrix, and test whether all coefficients become independent of size when both rectangularities remain fixed. If so, prove one infinite contraction Jacobi matrix produces fixed-weight beta-Jacobi laws. This would be a stronger proved special case and avoids assuming canonical Dirichlet weights for the chosen endpoint.

2. **Inverse-spectral transport on the Jacobi recurrence locus.** Instead of using ordinary corners kernels, seek a coupling of the polynomial roots supported on p_{n+1}=(x−a_{n+1})p_n−b_n²p_{n−1}. At three levels the law must be supported on a codimension-one constraint. One can formulate a constrained transport feasibility problem with the three ensemble marginals, or seek a separating functional proving infeasibility for a quartic potential. Interlacing alone is too weak. A numerical failure of a discretized transport problem would require a rigorous dual certificate before becoming a counterexample.

I pursue approach 1 first: it has an explicit finite-size theorem to verify and a plausible exact coefficient identity. Approach 2 is a distinct route to the unresolved arbitrary-weight problem, but finding a valid separating inequality appears substantially harder.

## Verified construction — fixed-weight beta-Jacobi

Fix β>0 and r,s>−1. Let independently

    p_i ~ Beta(β(r+i)/2, β(s+i)/2), i≥1,
    q_i ~ Beta(β i/2, β(r+s+1+i)/2), i≥1,
    q_0=0.

Define a lower bidiagonal array by

    d_i=sqrt(p_i(1−q_{i−1})),
    e_i=sqrt((1−p_i)q_i),
    B_{ii}=d_i, B_{i+1,i}=e_i,
    J=B B^T entrywise.

The beta shapes are all positive: r+i,s+i>0, and the smallest r+s+1+i is r+s+2>0. The proposed level-n eigenvalue density is

    Z_n^{-1} ∏_{i<j}(λ_j−λ_i)^β
      ∏_i λ_i^{β(r+1)/2−1}(1−λ_i)^{β(s+1)/2−1},
      0<λ_1<⋯<λ_n<1.

The angle laws and factor orientation have now been checked against Edelman–Sutton, Definition 1.6 (PDF p. 7), Definition 1.8 (pp. 7–8), and Theorem 4.1 (p. 17). The full all-size proof is below. The key factor is the lower-right CS block B_22, not the usual B_11. A matching trace mean alone is not used as a distributional proof.

## Checks already derived algebraically

For n=1, J_1=p_1 has precisely the proposed one-point beta distribution. At n=2,

    tr J_2=p_1+p_2(1−q_1)+(1−p_1)q_1,
    det J_2=p_1 p_2(1−q_1).

With r=1,s=0 their expected values are 6/5 and 3/10 for every β, matching the Selberg/Jacobi formulas. This is a consistency check only, not a proof of the joint law.

For each finite vector x with x_{n+1}=0,

    ||B_n^T x||²
      = Σ_{i=1}^n [sqrt(p_i) sqrt(1−q_{i−1}) x_i
                    +sqrt(1−p_i) sqrt(q_i) x_{i+1}]²
      ≤ Σ_{i=1}^n [(1−q_{i−1})x_i²+q_i x_{i+1}²]
      = Σ_{i=1}^n x_i².

This is Cauchy–Schwarz with the unit vector (sqrt(p_i),sqrt(1−p_i)); the last equality telescopes and uses q_0=0. Thus every J_n is a contraction. Equality is impossible for a nonzero vector: the i=n inequality, with x_{n+1}=0 and 0<p_n<1, forces x_n=0, and then backward induction forces every x_i=0. Positive definiteness follows from the positive diagonal of B_n. Therefore all eigenvalues lie strictly inside (0,1). The contraction proof is valid for every sequence p_i,q_i in (0,1), independently of the proposed probability theorem.

The following sections supply the complete probability proof and the independent referee checks.

## A second exact Gram factor and mixed determinant moments

Define a lower bidiagonal C_n with diagonal f_i=sqrt((1−p_i)(1−q_{i−1})) and subdiagonal −g_i=−sqrt(p_i q_i). Direct entry multiplication gives

    I_n−J_n=C_n C_n^T.

Indeed diagonal i of the sum B_n B_n^T+C_n C_n^T equals

    p_i(1−q_{i−1})+(1−p_{i−1})q_{i−1}
      +(1−p_i)(1−q_{i−1})+p_{i−1}q_{i−1}=1

with the q_0 terms zero; the offdiagonal entries cancel because d_i e_i=f_i g_i. This gives an exact alternative proof that every eigenvalue lies in (0,1), since both triangular factors have strictly positive diagonals. It also gives

The displayed diagonal formula is for i≥2; at i=1 the calculation is simply p_1+(1−p_1)=1, with no p_0 variable needed.

    D_n=det J_n=∏_{i=1}^n p_i ∏_{i=1}^{n−1}(1−q_i),
    E_n=det(I_n−J_n)=∏_{i=1}^n (1−p_i) ∏_{i=1}^{n−1}(1−q_i).

Let γ=β/2, t=r+s, and (z)_k=z(z+1)⋯(z+k−1), (z)_0=1. Independence and elementary beta integrals give, for all nonnegative integers k,l,

    E[D_n^k E_n^l]
      =∏_{i=1}^n (γ(r+i))_k (γ(s+i))_l / (γ(t+2i))_{k+l}
         ×∏_{i=1}^{n−1} (γ(t+1+i))_{k+l}/(γ(t+1+2i))_{k+l}
      =∏_{i=1}^n (γ(r+i))_k (γ(s+i))_l / (γ(t+n+i))_{k+l}.

For the cancellation, the two denominator products together range over t+j for j=2,…,2n; the extra numerator ranges over j=2,…,n, leaving precisely j=n+1,…,2n. These are exactly the mixed determinant moments computed by the Selberg integral for the proposed beta-Jacobi density with exponents γ(r+1)−1 and γ(s+1)−1.

Here is the integral input explicitly. If X has Beta(A,B) law, then E[X^k(1−X)^l]=B(A+k,B+l)/B(A,B)=(A)_k(B)_l/(A+B)_{k+l}, by integrating its density. For q_i only the complement power k+l occurs, giving (D_i)_{k+l}/(C_i+D_i)_{k+l}. The Selberg integral, with A,B>0 and γ>0, is

    S_n(A,B,γ)=∫_{[0,1]^n} ∏λ_i^{A−1}(1−λ_i)^{B−1}
                            ∏_{i<j}|λ_i−λ_j|^{2γ} dλ
      =∏_{j=0}^{n−1} Γ(A+jγ)Γ(B+jγ)Γ(1+(j+1)γ)
                    /[Γ(A+B+(n+j−1)γ)Γ(1+γ)].

Its ratio S_n(A+k,B+l,γ)/S_n(A,B,γ), with A=γ(r+1),B=γ(s+1), is exactly the final product above. Restricting to ordered eigenvalues divides both integrals by n!, which cancels. All hypotheses hold in the full parameter range considered here.

This already proves the full eigenvalue law at n=2, assuming the standard Selberg integral formula: polynomials are dense in continuous functions on [0,1]^2, so equality of every mixed moment determines the joint law of (D_2,E_2). The ordered two eigenvalues are determined by their product D_2 and their sum 1+D_2−E_2, as the ordered roots of x²−(1+D_2−E_2)x+D_2. This does NOT establish the n≥3 law: two determinants cease to determine all eigenvalues. The primary model theorem supplies that identification in the next section.

## Full proof of the all-size Jacobi construction

**Theorem.** For every β>0 and every α,δ>−1, there is one random bounded self-adjoint Jacobi operator J with positive offdiagonals and 0≤J≤I such that for every n its leading n-by-n minor has density

    Z_n^{-1} ∏_{i<j}(λ_j−λ_i)^β ∏_i λ_i^α(1−λ_i)^δ,
    0<λ_1<⋯<λ_n<1.

Equivalently there is one random probability measure μ on [0,1] with infinite support whose degree-n orthogonal polynomial zeros have that n-point law for every n. In particular the levels strictly interlace. This is a proved special case of D0040, derived from a pre-existing finite-size model theorem; no novelty or general classification claim is made.

**Proof.** Put γ=β/2, r=(α+1)/γ−1 and s=(δ+1)/γ−1. Then r,s>−1. Sample all p_i,q_i independently with the laws above, on their countable product probability space. Their parameters are positive: r+i,s+i>0, i>0, and r+s+1+i≥r+s+2>0. Hence almost surely all p_i,q_i lie strictly between zero and one simultaneously. Work on that probability-one event.

Define B and J as above. Explicitly,

    J_{11}=p_1,
    J_{ii}=p_i(1−q_{i−1})+(1−p_{i−1})q_{i−1}, i≥2,
    J_{i,i+1}=sqrt[p_i(1−q_{i−1})(1−p_i)q_i]>0.

Every row of B has support only in columns i−1,i, so the leading block J_n equals B_n B_n^T with no boundary correction. The complementary factor proof above gives I_n−J_n=C_n C_n^T. Both B_n and C_n are invertible since their diagonals are positive. Thus every eigenvalue of J_n lies strictly between zero and one.

For the eigenvalue law, set cos θ_i=sqrt(p_i), sin θ_i=sqrt(1−p_i), cos φ_i=sqrt(q_i), sin φ_i=sqrt(1−q_i), and define sin φ_0=1. These independent angles have exactly the distributions in Edelman–Sutton Definition 1.8 with parameters a=r,b=s. Their Definition 1.6 gives the lower-right block T_n=B_22(Θ,Φ), with

    (T_n)_{ii}=cos θ_{n+1−i} sin φ_{n−i}=d_{n+1−i},
    (T_n)_{i+1,i}=−sin θ_{n−i} cos φ_{n−i}=−e_{n−i}.

All other offdiagonal entries vanish. The final diagonal is cos θ_1=d_1. The source specifically clarifies that the penultimate diagonal of B_22 is cos θ_2 sin φ_1, consistent with this formula; the boundary sin φ_0=1 is therefore verified rather than guessed.

Let R_n be reversal and S_n=diag(1,−1,1,−1,…). Then

    T_n=S_n R_n B_n^T R_n S_n.

This identity follows entry by entry: reversal sends the diagonal to d_n,…,d_1 and the lower subdiagonal to e_{n−1},…,e_1; S_n changes each subdiagonal sign. These operations preserve singular values, so T_n and B_n have the same singular values.

In the CS decomposition used by Edelman–Sutton, the entire 2n-by-2n orthogonal model is

    diag(U_1,U_2) [[C,S],[-S,C]] diag(V_1,V_2)^T,

where C,S are nonnegative diagonal matrices with C²+S²=I. The lower-right block is U_2 C V_2^T, hence its singular values are the diagonal entries of C, just as for the upper-left block U_1 C V_1^T. Edelman–Sutton Theorem 4.1 applies for all β>0 and r,s>−1 and says these entries squared have the beta-Jacobi law with exponents γ(r+1)−1=α and γ(s+1)−1=δ. Because the eigenvalues of B_n B_n^T are its squared singular values, this is exactly the eigenvalue law of J_n. The same sampled sequences furnish every n, and no angle law depends on n. This proves strict leading-minor nesting, not just interlacing of separately sampled spectra.

To construct the common measure, first consider B^T on finitely supported vectors. The Cauchy–Schwarz/telescoping calculation above proves ||B^T x||≤||x||, uniformly in the support size. Thus B^T extends to a contraction K on ℓ²(N). Define J=K^*K. On finitely supported vectors its entries are exactly the tridiagonal array already constructed. It is a bounded self-adjoint positive contraction; its spectrum lies in [0,1]. Let μ be its spectral measure at e_1. The spectral theorem makes this a probability measure on [0,1], with all moments finite.

Write t_i=J_{i,i+1}>0, h_i=J_{ii}, and p_n(x)=det(xI−J_n), p_0=1. Last-row determinant expansion gives

    p_1=x−h_1,
    p_{n+1}=(x−h_{n+1})p_n−t_n²p_{n−1}.

Set P_0=1 and P_n=p_n/(t_1⋯t_n). Induction in this recurrence and the tridiagonal action gives P_n(J)e_1=e_{n+1}. Therefore ∫P_n P_m dμ=⟨e_{n+1},e_{m+1}⟩, so these are orthonormal polynomials, with positive leading coefficients, and their zeros are the eigenvalues of J_n. All polynomial vectors are linearly independent; consequently μ cannot have finite support. The strict-interlacing proof by this recurrence is written in full in ATTEMPT.md and applies unchanged because every t_i>0.

For measurability, every moment ∫x^k dμ=⟨e_1,J^k e_1⟩ is a polynomial in finitely many measurable matrix entries. For any continuous f on [0,1], uniform polynomial approximation makes ∫f dμ a limit of measurable random variables. The weak Borel structure of probability measures on [0,1] is generated by a countable dense collection of these continuous test functions. Hence μ is a random measure. This proves the source's common-measure formulation as well. ∎

The infinite measure is only asserted to be supported on the closed interval; strict exclusion of endpoints is proved for every finite minor, not asserted for μ itself.

### Corollary: the uniform hard-wall Dyson ensemble

Set α=δ=0, equivalently r=s=2/β−1. Then

    p_i ~ Beta(1+β(i−1)/2, 1+β(i−1)/2),
    q_i ~ Beta(βi/2, 2+β(i−1)/2),

and the n-point spectrum has density proportional simply to ∏_{i<j}(λ_j−λ_i)^β on (0,1)^n. This supplies a non-Gaussian fixed-potential example if hard-wall confinement is allowed: V=0 inside [0,1] and V=+∞ outside. It is not a smooth confining potential on the whole real line.

A fixed affine transformation L I+(U−L)J, U>L, similarly yields the fixed-weight family ∏(λ_i−L)^α(U−λ_i)^δ ∏_{i<j}(λ_j−λ_i)^β on any fixed interval (L,U). The affine map is independent of n, so literal leading-minor nesting is preserved.

## Exact scope of progress and remaining gap

### A concrete escape from canonical inconsistency

The new construction gives a useful counterexample to the inference “the canonical matrix laws fail to nest, therefore the eigenvalue laws admit no nesting.” This is an exact statement, not just a logical possibility.

**Proposition.** If r≠s (equivalently α≠δ), the beta-Jacobi tridiagonal representatives with independent Dirichlet(β/2,…,β/2) first-coordinate spectral weights fail leading-minor consistency already between sizes 2 and 1, despite the alternative nesting constructed above.

**Proof.** The one-point law is Beta(γ(r+1),γ(s+1)), so its mean is (r+1)/(r+s+2). At size two the mixed determinant formulas give, with t=r+s,

    E det J_2=(r+1)(r+2)/[(t+3)(t+4)],
    E det(I−J_2)=(s+1)(s+2)/[(t+3)(t+4)].

For every two-by-two matrix, tr J_2=1+det J_2−det(I−J_2). Hence

    E tr J_2=1+(r−s)/(t+4)=2(r+2)/(t+4).

For any spectral representation with independent Dirichlet(γ,γ) weights W_1,W_2 at e_1, E W_i=1/2. Thus its first diagonal has mean (r+2)/(t+4). Equality of its leading one-by-one law with the one-point ensemble would require equality with (r+1)/(t+2). But

    (r+1)/(t+2)−(r+2)/(t+4)
       =(r−s)/[(t+2)(t+4)] ≠0.

All denominators are strictly positive since r,s>−1. Therefore the canonical laws are inconsistent. The all-size theorem above supplies a different consistent Jacobi law with the same eigenvalue marginal at every size. ∎

For example β=2,r=1,s=0 means endpoint powers α=1,δ=0: the one-point mean is 2/3, whereas the canonical size-two first-diagonal mean is 3/5. The new coupling keeps mean 2/3 at its first diagonal in every size. The mean test alone makes no conclusion at r=s. The following variance calculation resolves that boundary of the argument. Neither calculation constructs a quartic coupling.

**Stronger corollary.** The canonical independent-Dirichlet-weight matrix family is inconsistent between sizes 2 and 1 for EVERY β>0 and EVERY r,s>−1, including r=s. Every one of these spectral families nevertheless has the alternative all-size nesting proved above.

**Proof of the remaining symmetric case.** Write r=s=u>−1 and γ=β/2>0. Let D=λ_1λ_2, E=(1−λ_1)(1−λ_2), T=λ_1+λ_2=1+D−E under the size-two Jacobi law. Symmetry under λ↦1−λ gives E[D]=E[E] and E[D²]=E[E²]. From the mixed determinant formula,

    E[D]=(u+1)/[2(2u+3)],
    E[D²]−E[DE]
      =(u+1)/[2(2u+3)(2γ(u+2)+1)].

For the second identity, the common denominator before cancellation is

    γ²(2u+3)(2u+4)[γ(2u+3)+1][γ(2u+4)+1].

The numerator of the difference is

    γ²(u+1)(u+2)
      [(γ(u+1)+1)(γ(u+2)+1)−γ²(u+1)(u+2)]
      =γ²(u+1)(u+2)[γ(2u+3)+1],

which gives the displayed identity after cancellation. All canceled factors are positive. Expanding T² therefore gives

    E[T²]=1+2(E[D²]−E[DE])
           =1+(u+1)/[(2u+3)(2γ(u+2)+1)].

The canonical first diagonal is Y=Wλ_1+(1−W)λ_2, with W~Beta(γ,γ) independent of the eigenvalues. Its conditional mean is T/2. The beta integral gives E[W²]=(γ+1)/[2(2γ+1)] and E[W(1−W)]=γ/[2(2γ+1)]. Hence

    E[Y²]=[(γ+1)/(2(2γ+1))] E[T²]−E[D]/(2γ+1)
          =1/4+1/[4(2γ(u+2)+1)].

E[Y]=1/2, so Var(Y)=1/[4(2γ(u+2)+1)]. In contrast the one-point law is Beta(γ(u+1),γ(u+1)) and has variance 1/[4(2γ(u+1)+1)]. These are strictly different because γ>0. Thus the canonical size-two first diagonal cannot have the one-point law. Together with the asymmetric mean argument this proves the corollary for all parameters. ∎

As a symmetric check, β=2,u=0 gives the uniform one-point variance 1/12, versus canonical size-two first-diagonal variance 1/20. This exact escape from canonical inconsistency demonstrates why the earlier canonical quartic obstruction cannot be promoted to arbitrary-coupling impossibility.

The additional attempt establishes the entire integrable beta-Jacobi weight family for every β, with one common random orthogonality measure. Together with the earlier Hermite and Laguerre models this covers all three classical real-line beta families under the stated fixed-weight conventions. It does not classify all Dyson potentials.

The unresolved central gap is still: for a fixed nonclassical confining potential, such as the full-real-line quartic weight exp(−βx⁴), does ANY random Jacobi/Favard recurrence have the required level laws? No independent-Dirichlet-weight condition is imposed. The compact hard-wall example does not settle that full-real-line question. The inverse-spectral transport approach remains a possible route to existence or a genuine separating certificate, but is not a proved criterion or counterexample here.

VERDICT remains PARTIAL for the broad D0040 question. There is no verified paper explicitly proving the question with matching broad objects and quantifiers; the new nesting implication is derived from a finite-size theorem, so SOLVED_IN_LITERATURE is not claimed.

## Hostile-referee audit

1. **Which block?** The usual B_11 block has different terminal coefficients. The proof uses B_22 from Definition 1.6 and explicitly identifies its penultimate and final diagonals. The source CS decomposition proves its singular values are the same as B_11's. All four source blocks were separately implemented in check_cs_orientation.py, rather than only testing a reversal of our own factor.
2. **Which Gram orientation?** Nesting uses the row Gram B_n B_n^T of a lower bidiagonal factor. The column Gram B_n^T B_n would acquire e_n² in its final diagonal on extension, so it is not the matrix whose leading blocks are claimed consistent. Column-Gram spectra enter only in the finite singular-value comparison.
3. **All parameters?** Theorem 4.1 explicitly allows every β>0 and r,s>−1. The shape of q_1's second beta parameter is γ(r+s+2)>0, even when r,s are both negative. No integer or nonnegative rectangularity hypothesis is smuggled into the proof.
4. **Endpoint support?** Both J_n and I_n−J_n are exact positive-definite Gram matrices. Their spectra are strictly inside (0,1). The infinite μ is only claimed supported on [0,1]. Excluded r=−1 or s=−1 boundaries have zero beta shape and are not claimed.
5. **Moments versus a full law?** The mixed determinant moments are an independent calculation. They imply the full law at n=2 but are explicitly not used to infer the n≥3 law. That law comes from the correctly matched primary theorem.
6. **All sizes on one probability space?** The countable product space samples p_i,q_i once. J_n uses p_1,…,p_n and q_1,…,q_{n−1}; every size extends the same row-Gram array. Positive-shape conditions hold simultaneously on a probability-one event.
7. **Common measure versus generic interlacing?** The constructed bounded operator, cyclic e_1, determinant recurrence and measurable spectral measure provide the exact common-measure formulation. This is stronger than a generic corners coupling.
8. **Numerical exceptions?** Small-shape interlacing gaps may round to zero or become negative at machine precision. Some raw KS p-values are below 0.05 in the 14 correlated projection comparisons; none meets the Bonferroni 0.05/14 threshold. All raw results are retained. Neither simulation nor a corrected p-value is used as a proof.
9. **Scope?** A compact hard-wall V is not a smooth full-line quartic V. The general arbitrary-spectral-weight problem remains unresolved, and no classical finite-size theorem is relabeled a literature solution of that broader problem.

## Numerical verification completed

* check_jacobi.py, seed 240040: five sets of 12000 matrices, including β=0.8 and negative r,s, and β=4; 25 mixed moment checks. Maximum absolute mixed-moment z-score was 2.4295. Complement-Gram error was at most 4.45e−16 and reversal/transposition spectral error at most 1.12e−15. Small-shape strict interlacing has a −2.23e−16 floating-point gap; the exact proof is separate.
* Independent Wishart/MANOVA comparisons at β=1,2, n=4, r=2,s=3: 5000 model and 5000 direct Gaussian samples per β, seven statistics each. Maximum two-sample KS distance was 0.0312. The smallest raw p-value was approximately 0.0154, so a claim that every unadjusted test passed would be false. The familywise DKW/union bound for 14 projections and 5000 samples per law gives threshold sqrt(2 log(4·14/0.05)/5000)≈0.0530 at error probability 0.05 under identical ideal sampling laws; the observed maximum is below it. This is a numerical consistency check, not an identity theorem.
* check_cs_orientation.py, seed 400022: 1000 arbitrary-angle samples at each n=1,2,3,5,8,12. The entrywise signed reversal/transposition identity for B_22 had exactly zero computed error. The full 2n orthogonal model's orthogonality error was at most 4.45e−16; B_11/B_22 singular-value error at most 1.12e−15; comparison of the candidate's eigenvalues to B_11 squared singular values at most 1.23e−15. All assertions passed.

Outputs are saved in jacobi_numerical_checks.json and cs_orientation_checks.json. Jobs use small matrices, with array storage far below 1 GB and no long-running simulation.

## Formal verification scope

JacobiCheck.lean contains the exact two-component Cauchy–Schwarz defect identity, its unit-vector inequality, the complementary diagonal identity, and reproductions of the two previous algebraic identities. It imports only Mathlib.Data.Real.Basic and Mathlib.Tactic.Ring, and contains no sorry or native_decide. verify_second_lean.py runs the single command from ~/lean_verify with a one-hour timeout, records stdout in second_lean.log and writes second_lean_result.json on completion. The old unlogged session is unavailable, so its result is not guessed. Compilation status is reported in VERIFICATION.md; no formal success is assumed from the file alone.
