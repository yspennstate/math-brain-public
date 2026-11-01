# Balanced transfer operators and a fourth-moment certificate for the Möbius graph

19 September 2026. Target: H = K(5,5) minus C(10).

**Outcome:** a quantitative lower bound valid for every finite symmetric nonnegative regular kernel, with a freely chosen positive diagonal balancing vector. It can certify the target inequality without evaluating the fifth trace. It is not automatically at least one for every kernel, and the full Sidorenko inequality has not been proved. The arguments and computations are same-assistant work, not an independent audit. Publication novelty is unverified.

## 1. Inherited representation

On a finite probability space with p_i>0, let W_ij=W_ji>=0 and sum_j p_j W_ij=1. Put

    C_ijk = sum_u p_u W_ui W_uj W_uk,
    T_(ij,jk) = p_k C_ijk,

with other entries zero. The previous transfer note proves

    t_H(W) = Tr(T^5).

On L^2(p tensor p), let R reverse the coordinates and define

    (Fh)(u,i) = sqrt(W_ui) sum_j p_j W_uj h(i,j).

Then T=R F*F. Its nonzero eigenvalues, counted algebraically, are those of the self-adjoint operator K=F R F*. In an orthonormal coordinate basis,

    K_(ui,vj) = sqrt(p_u p_i p_v p_j W_ui W_vj) W_uj W_vi.

K is entrywise nonnegative. Its spectral radius rho is therefore an eigenvalue and equals its operator norm. These facts do not assert that K is positive semidefinite.

The new results below use this particular representation. They do not infer a fifth-trace inequality from a bound on rho alone.

## 2. A sharper Perron lower bound

Write W^(j) for integral-operator powers, so multiplication includes the p weights. Let

    beta_0 = t_C4(W) = Tr(W^4),
    m_2 = sum_(u,i) p_u p_i W_ui (W^(3)_ui)^2.

### Proposition 2.1

    rho >= sqrt(m_2) >= beta_0 >= 1.

**Proof.** In the orthonormal pair basis set g_ui=sqrt(p_u p_i W_ui). Regularity gives ||g||^2=1. Direct multiplication gives

    (Kg)_ui = g_ui W^(3)_ui.

Consequently

    <g,Kg> = sum p_u p_i W_ui W^(3)_ui = Tr(W^4)=beta_0,
    ||Kg||^2=m_2.

The operator norm bound yields sqrt(m_2)<=rho and Cauchy--Schwarz yields beta_0<=sqrt(m_2). Finally W is a self-adjoint Markov operator with eigenvalue one; all other fourth powers are nonnegative. Therefore Tr(W^4)>=1. QED.

For U=W-1 the lower bound beta_0 is exactly 1+Tr(U^4). A nonconstant W therefore has rho>1. Also, the earlier quantity

    A = integral W(x,y) U^(3)(x,y)^2 dxdy

satisfies the sharper bound A>=(Tr(U^4))^2, by applying Cauchy--Schwarz in the probability measure W(x,y)dxdy. Indeed integral W U^(3)=Tr(U^4). This strengthens A>=0 but does not control the complete signed remainder.

For comparison, the inherited entropy argument gives rho>=exp(integral W^2 log W^2), with W^2 interpreted as the operator square. Neither this entropy bound nor Proposition 2.1 is itself the missing fifth-trace comparison.

### Rational Krylov lower bounds

All additional Rayleigh bounds can be computed without square roots. On active edges W_ui>0 define

    nu_ui=p_u p_i W_ui,
    L_(ui,vj)=p_v p_j W_vj W_uj W_vi.

Then nu is a probability measure, nu_s L_st=nu_t L_ts, and K is the symmetric realization of L. Starting with h_0=1, let h_(r+1)=Lh_r. Each

    beta_r = [sum_s nu_s h_r(s) h_(r+1)(s)]
             /[sum_s nu_s h_r(s)^2]

is a valid lower bound on rho. beta_0 is the four-cycle density above. For rational p and W these are rational numbers. Taking the maximum of any finite collection, including beta_0, preserves a certified lower bound beta>=1. No monotonicity of the individual Rayleigh quotients is assumed.

## 3. A cyclic Gram identity controls negative eigenvalues

The following lemma needs only full symmetry and nonnegativity of C, not its particular latent-moment representation.

Let D be multiplication by q_ij=sum_k p_k C_ijk. For complex h, expansion and cyclic relabeling give

    <h,Dh> + 2 Re<h,Th>
       = (1/3) sum_(i,j,k) p_i p_j p_k C_ijk
           |h_ij+h_jk+h_ki|^2 >=0.                 (3.1)

If Th=lambda h, this implies

    Re lambda >= -(1/2) max_(i,j) q_ij.

For the kernel-derived T, all eigenvalues are real, so this is a lower spectral bound. The row sums separately bound rho(T)<=max q_ij. It is not valid to replace max q_ij by rho(T) in the lower bound without a further proof.

### Positive diagonal balancing

Let z_i>0 be arbitrary and define

    q(z) = max_(i,j) [sum_k p_k C_ijk z_k^2]/(z_i z_j).

### Proposition 3.2

Every eigenvalue lambda of the original T satisfies

    -q(z)/2 <= lambda <= rho(T) <= q(z).             (3.2)

**Proof.** Let Z=sum_i p_i z_i^3 and set

    p'_i=p_i z_i^3/Z,
    C'_ijk=Z C_ijk/(z_i z_j z_k).

C' remains symmetric and nonnegative. Its transfer matrix T' on L^2(p' tensor p') is similar to T: with S_(ij,ij)=z_i z_j^2,

    T'=S^(-1) T S,
    T'_(ij,jk)=p_k C_ijk z_k^2/(z_i z_j).

Thus the maximum row sum of T' is q(z). Apply (3.1) to C',p' and apply the row-sum spectral-radius bound. Similarity preserves all eigenvalues. QED.

The change of measure is only a transfer-matrix device: it is not asserted that an arbitrary entrywise rescaling of W remains regular.

If z_i=exp(x_i), log q(z) is the maximum of the convex functions

    log sum_k p_k C_ijk exp(2x_k-x_i-x_j).

The balancing proposal can therefore be found by a finite-dimensional convex optimization, after fixing the additive gauge. However the proof needs neither numerical optimality nor a claimed global optimizer. Any positive rational z gives a rigorous upper bound q(z) by direct rational evaluation. The exact verifier accepts only those rational values.

## 4. A lower bound using moments through order four

Let tau_j=Tr(T^j) for j=2,3,4. Here tau_3=t_K33(W), and tau_4 is the cube density. No Sidorenko theorem for either graph is assumed in the following proof.

Choose any certified beta satisfying 0<=beta<=rho(T), for example beta=t_C4(W), or a finite maximum of the Rayleigh bounds in Section 2. Set a=q(z)/2.

### Theorem 4.1

For every b in [0,beta],

    t_H(W) >= (2b-a) tau_4 +(2ab-b^2) tau_3 -ab^2 tau_2
                  + beta^2(beta-b)^2(beta+a).       (4.1)

Equivalently, with r_j=tau_j-beta^j,

    t_H(W) >= beta^5 +(2b-a)r_4 +(2ab-b^2)r_3 -ab^2 r_2.
                                                        (4.2)

This is a universal quantitative inequality on the stated class. The expression on the right is not asserted to be >=1 for every W and every choice of parameters.

**Proof.** All eigenvalues lambda of K lie in [-a,rho], by Proposition 3.2. The polynomial

    p_b(x)=x^2(x-b)^2(x+a)

is nonnegative on [-a,infinity). It is nondecreasing on [b,infinity), because each of its three nonnegative factors is nondecreasing there. Since rho>=beta>=b,

    Tr p_b(K) >= p_b(rho) >= p_b(beta).

Expansion gives

    p_b(x)=x^5+(a-2b)x^4+(b^2-2ab)x^3+ab^2 x^2.

Substitute the trace identities and rearrange. This proves (4.1); subtracting the powers of beta proves (4.2). QED.

A particularly simple consequence, obtained with b=0, is

    t_H(W) >= beta^4(beta+a)-a tau_4.                (4.3)

This does not make the invalid comparison tau_5>=tau_3. The retained repository counterexample to that comparison is consistent with (4.1).

### Best b within this certificate

Define

    D = r_3+a r_2,       N = r_4+a r_3.

Then D>=0. Indeed x^2(x+a)>=0 for every eigenvalue and is increasing for x>=0, so

    tau_3+a tau_2 >= rho^2(rho+a) >= beta^2(beta+a).

The right side of (4.2) is the concave quadratic

    beta^5-a r_4+2Nb-Db^2.

For D>0 its maximum on [0,beta] occurs at

    b = min(beta, max(0,N/D)).

If D=0, equality in the preceding nonnegative sum forces N=0; any b has the same value and the verifier chooses zero. Thus all quantities in an exact finite certificate are rational whenever W,p,z,beta are rational. tau_5 is not an input to the lower bound.

### Bounded-kernel passage

For the unbalanced choice z=1 the result extends to bounded graphons on a standard probability space. One can take

    a = (1/2) esssup_x integral W(x,y)^2 dy.

Conditional expectations on refining finite partitions preserve symmetry, nonnegativity and regularity. Their row L2 norms do not increase past the displayed supremum, by Jensen. All graph and multigraph densities appearing in beta=t_C4(W),tau_2,tau_3,tau_4 and t_H converge by bounded-kernel telescoping. Use b_n=min(b,beta_n) and pass to the limit. This proves (4.1) in that infinite-dimensional class as well. The optimized finite balancing statement is not promoted to arbitrary unbounded measurable gauges without an additional approximation argument.

## 5. Exact successes outside the previous local neighborhood

The attached program uses only integers and Fraction arithmetic. It reconstructs the gauge similarity and the entire cyclic Gram identity, checks the edge-space self-adjointness, and evaluates the certificate from tau_2,tau_3,tau_4. For validation only, it separately computes tau_5 and a direct five-variable density and verifies agreement.

### The earlier four-block obstruction

Use the symmetric integer flow from GLOBAL_ATTEMPT.md:

    Q = [[547845,22,30967151,932390],
         [22,27,5,2177],
         [30967151,5,870744517,32344047],
         [932390,2177,32344047,216028]].

Let r_i=sum_j Q_ij, Z=sum_i r_i, p_i=r_i/Z and W_ij=Z Q_ij/(r_i r_j). Use the exact rational gauge

    z = (1, 2143535544/10^8, 99592757/10^8, 101314111/10^8).

The unbalanced q is about 94.0799; direct rational substitution of this gauge makes q about 1.00258. No optimizer accuracy is used in the certificate. With beta=t_C4(W) and the rational optimal b, (4.1) proves

    t_H(W) > 33/25 = 1.32.

The actual rational lower bound is about 1.3232237373, while the separately computed density is about 1.3240183060. Decimal displays are descriptive only. The exact bound is greater than 33/25 by a positive rational checked by the program. This same kernel defeats the earlier off-diagonal Gram sign shortcut. Its ||W-1||_infinity exceeds 5400, so the previous half-radius local theorem does not cover it.

### A generic five-block example

Take the symmetric flow with each row summing to 42:

    Q = [[32,1,2,3,4], [1,23,5,6,7], [2,5,18,8,9],
         [3,6,8,15,10], [4,7,9,10,12]].

Then p_i=1/5 and W=5Q/42. Already with z=1 and beta=t_C4(W), the bound proves

    t_H(W)>39.

The exact certificate's lower bound is about 39.1375. The separate direct calculation is about 56.9116. No equality of eigenvalues or vanishing third-moment tensor is used. Its sup-norm deviation is 59/21>1/2.

The constant kernel and the normalized complete-triangle host are checked separately, including the degenerate D=0 case and zero entries of W.

## 6. What remains unresolved

The earlier principal-eigenvalue bound alone left the signed fifth trace uncontrolled. The present argument controls that signed trace quantitatively by a valid spectral floor and a nonnegative polynomial. This is a further inequality, not a universal resolution.

It is still necessary to show that suitable parameters give a right side >=1 for every kernel, or to control the part left below one by an additional argument. The first scalar choice need not work: for a direct sum on masses 1/100 and 99/100, W is diagonal with entries 100 and 100/99. The choice beta=t_C4(W)=2 can give a negative lower bound, even though the target is true. Additional Rayleigh steps improve beta, but no uniform finite-step success theorem is proved here.

Even the generic facts 'real spectrum, rho>=1, eigenvalues>=-1/2, third trace>=1, fourth trace>=1' do not imply fifth trace>=1. The nonnegative symmetric matrix consisting of a stochastic triangle block and ten scalar blocks 3/10 has eigenvalues

    1, -1/2, -1/2, and ten copies of 3/10.

Its third and fourth traces exceed one but its fifth trace is 4809/5000<1. This matrix is not claimed to arise from W; it is a precise warning against discarding the remaining moment structure.

Numerical exploration suggests stronger lower spectral ratios and positive fifth remainders for the sampled kernel-derived matrices, but these are not theorems. In particular, no replacement of q(z)/2 by rho/3 is made in this proof.

## 7. Provenance, literature, and reproduction

The starting transfer identities are in ../2026-09-19-sidorenko-transfer/TRANSFER_PROGRESS.md. The mixed-spectrum results are in ../2026-09-19-sidorenko-mixed-spectrum/MIXED_SPECTRUM.md. The exact off-diagonal Gram witness and failed third-trace comparison are in ../2026-09-19-sidorenko-global-attempt/GLOBAL_ATTEMPT.md. Earlier notes were preserved without changing their closure or audit status.

This continuation uses standard Rayleigh, Cauchy--Schwarz, spectral mapping, Perron--Frobenius, and convexity principles. No claim is made that these general tools are new. The new work here is the displayed specialization, cyclic balancing identity, combined certificate, and its exact application to the saved obstruction. A specialist literature comparison is still needed for priority.

Relevant primary sources inspected on 19 September 2026:

- Joonkyung Lee and Bjarne Schuelke, Convex graphon parameters and graph norms, arXiv:1910.08454: the fixed graph and its failure to be weakly norming. https://arxiv.org/abs/1910.08454
- David Conlon and Joonkyung Lee, Sidorenko's Conjecture for Blow-ups, Discrete Analysis 2021:2, arXiv:1809.01259v3: the symmetrization/blow-up route, not a justification of the missing half-exponent inequality. https://arxiv.org/html/1809.01259v3
- Seonghyuk Im, Ruonan Li and Hong Liu, Sidorenko's conjecture for subdivisions and theta substitutions, published online 10 December 2025, Lemma 2.2, citing Coregliano--Razborov Theorem 8.2: reduction to regular graphons. The journal page lists these THREE authors; an older repository reference that additionally named Mubayi and Zhou should not be copied. https://www.cambridge.org/core/journals/combinatorics-probability-and-computing/article/sidorenkos-conjecture-for-subdivisions-and-theta-substitutions/7587A22E3A717B29DBAB2A6E99875345

Run python check_balanced_moments.py. The accompanying JSON is generated by that program. All theorem claims remain restricted to their written statements; this note does not mark the full conjecture solved or assert an independent audit.
