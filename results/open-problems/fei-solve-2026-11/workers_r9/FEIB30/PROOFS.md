# Proofs and conventions

All logarithms in costs are base two. Derivatives and asymptotic estimates use natural logarithms when indicated. Assume I>0; constant functions have no Q law. Give zero-mass terms their continuous interpretation. A predictor vanishing on Q support has infinite cost. The variational statement needs 0<K<infinity to be a finite inequality.

The formula Q(T,i)=mu(T+i)/I means first draw U from its size-biased law |U|mu(U)/I, then delete an element uniformly. Drawing U directly from mu and deleting an element uniformly would give mu(U)/|U|, and would be a different pair law. All computations here use the displayed formula for Q.

## The three facts in the brief

PROVED. Write a=mu(T), b=mu(T+i). The pair measure

    R(T,i)=(a+b)p_i(T)/(I K)

is normalized. Direct subtraction gives

    log2 K + E_Q log2(1/p) - L = D_KL(Q || R) >= 0.

This also identifies precisely what overhead measures. Equality holds whenever R=Q, including any positive common multiple of p=b/(a+b). The claim is not literally meaningful at the degenerate choice p identically zero; the support qualification above resolves it.

PROVED. Differentiating the finite positive polynomial up_t(T) gives

    t d/dt log up_t(T)
      = sum_{U>=T} (|U|-|T|) mu(U)t^{|U-T|}/up_t(T)
      = sum_{i notin T} t up_t(T+i)/up_t(T) = m_t(T).

Under the joint experiment U~mu and T formed by deleting each element with probability t, its joint probability is mu(U)(1-t)^|T| t^|U-T|. Thus the posterior law of U given T is exactly the law displayed in the brief; averaging the number deleted gives E_nu m_t=t I. No Boolean assumption is needed for these statements.

Integrate the derivative from zero to one for each T with mu(T)>0:

    B_1 := E_mu log2(up_1(T)/mu(T))
         = (1/ln 2) integral_0^1 E_mu m_t(T) dt/t.

For completeness the last FEI equivalence in the brief follows from Boolean granularity. D_T f takes values in integer multiples of 2^(1-|T|), for T nonempty, so

    |fhat(T)| = |E D_T f| <= E |D_T f|
                  <= 2^(|T|-1) E(D_T f)^2 = 2^(|T|-1) up_1(T).

Since up_1(empty)=1, this implies A_1:=E_mu log2(1/up_1(T)) <= H/2+I and B_1=H-A_1 >= H/2-I. Also B_1<=H because up_1(T)<=1. The thinning law nu_t(T)=(1-t)^|T| up_t(T) is normalized, and D(mu||nu_t)>=0 gives B_t<=I log2(1/(1-t)). In particular B_(1/2)<=I. Therefore, putting J=integral_(1/2)^1 E_mu m_t(T) dt,

    (ln 2)(H/2-2I) <= integral_(1/2)^1 E_mu m_t(T) dt/t <= 2J,
    J <= integral_0^1 E_mu m_t(T) dt/t = (ln 2) B_1 <= (ln 2) H.

Hence J=O(I) if and only if H=O(I). Nonnegativity also justifies every integration step. The norm identity up_t(T)=||T_sqrt(t) D_T f||_2^2 follows from the Fourier expansion of D_T f and Parseval.

PROVED. If psi is balanced then a nonempty Fourier block of f=F(psi,...,psi) determines exactly which outer variables occur, so

    mu_f(S)=mu_F(J) product_{j in J} mu_psi(S_j),
    J={j:S_j nonempty}.

In the sum over supersets S>=T, a block already hit by T contributes up_t^psi(T_j). An unhit block selected by the outer spectrum contributes theta=sum_{S nonempty} mu_psi(S)t^|S|. Summing over the outer superset of J proves exactly the displayed composition law. Balancedness makes theta=up_t^psi(empty).

## Biased composition and the exact tower recurrence

PROVED. Let the inner function g have mean m, spectral variance v0=1-m^2, and v_t=up_t^g(empty)-m^2. Expand the outer multilinear polynomial at m:

    F(z)=sum_J c_J product_{j in J}(z_j-m),
    c_J=sum_{A>=J} Fhat(A) m^|A-J|.

If S hits outer blocks J, Fourier expansion gives

    mu_f(S)=c_J^2 product_{j in J} mu_g(S_j).

In particular fhat(empty)=c_empty, not a product of inner empty coefficients. Define the outer polynomial

    U_v(J)=sum_{A>=J} c_A^2 v^|A-J|.

Then

    up_t^f(T)=U_(v_t)(J) product_{j in J} up_t^g(T_j).

This proves the biased extension used in referee.py. The c_J are not the usual uniform Fourier coefficients unless m=0. Their squares weighted by v0^|J| sum to one.

For a predictor p=P_t(r), keep three unnormalized edge sums of g:

    Z_K=sum_edges (mu(T)+mu(T+i)) P_t(r),
    Z_C=sum_edges mu(T+i) log2(1/P_t(r)),
    Z_L=sum_edges mu(T+i) log2(1+mu(T)/mu(T+i)).

Let B_K,B_C,B_L be these same sums restricted to T=empty. Keep also, for each coordinate i, its singleton mass a_i=mu_g({i}) and noisy singleton norm u_i=up_t^g({i}), grouping equal coordinates with multiplicities. Set

    M=sum_j sum_{J subset [k] minus j} c_(J+j)^2 v0^|J|.

An edge with T_j nonempty has its upper and lower spectral masses multiplied by the same c_(J+j)^2 times sibling masses, and its noisy ratio r is unchanged. Summing the siblings gives M. Consequently its entire contribution is M(Z-B).

For all remaining edges, the deleted element empties its inner block. For each outer j, sibling active set J, and inner coordinate i, set

    a=c_J^2 v0^|J|,
    b=c_(J+j)^2 v0^|J| a_i,
    r=u_i U_(v_t)(J+j)/U_(v_t)(J).

Add the three edge costs with these a,b,r, and call the resulting vector E. The recurrence is

    Z_f=M(Z_g-B_g)+E,
    I_f=M I_g,
    a_(j,i)^f=c_{j}^2 a_i,
    u_(j,i)^f=U_(v_t)({j}) u_i,
    v_t^f=sum_{J nonempty} c_J^2 v_t^|J|.

Compute B_f directly from the new singletons and up_t^f(empty). Finally logK=log2(Z_K/I), cost=Z_C/I and L=Z_L/I. This is a finite exact algebraic/logarithmic recurrence; its evaluation here is float64, not interval-certified exact arithmetic. It never enumerates a tower truth table. Expanding Z-B recursively partitions edges by the level at which deleting their element first empties a block. For a balanced self-tower, the probability a deletion empties an inner depth-h block is W1(g_h)/I(g_h)=(W1(base)/I(base))^h.

The same recurrence tracks the posterior-mean numerator sum_edges mu(T)*t*r: replace every edge cost by a*t*r and the empty boundary by m^2*t*r. This is how tower m/I values in the saved tables were evaluated.

The four balanced monotone four-variable representatives were obtained by exact enumeration in referee.py. The truth-set convention is negative output at set bits, input bits ordered least-significant first; unused variables remain included in n but contribute no edges of positive mass.

## Balanced self-towers really do converge

PROVED. For a fixed balanced Boolean gate G that is not a dictator or negated dictator, each of logK, cost, L, and Ov converges in its self-tower, for every fixed 0<t<1 and all three predictors. Constants in this statement may depend on the gate and t; it is not a proof of the uniform conjecture P.

Here is a quantitative summability argument. Write a=I(G), w=W1(G), rho=w/a<1 and phi(t)=sum_S mu_G(S)t^|S|. The strict inequality follows because equality would force all spectral mass onto singletons and hence G to be a dictator. The tower g_h has I=a^h, W1=w^h, and its spectral generating function is phi iterated h times. If w>0, then

    phi^h(t) <= t [w+(1-w)t]^h,
    (phi^h)'(t) <= C_(G,t) w^h.

The second inequality follows by the chain rule: phi'(s)=w+O_G(s), the orbit tends geometrically to zero, and the product of (1+O_G(phi^j(t))) converges. When w=0, singleton masses vanish; after the first level only false-positive boundary terms remain, and the derivative decays faster than any fixed exponential while I grows exponentially. The same summability conclusion follows directly.

For w>0 let epsilon be the smallest positive mass of the base spectrum. Every positive singleton mass at depth h is a product of h base singleton masses, hence is at least epsilon^h. In a boundary edge with positive upper mass the noisy ratio satisfies

    r >= epsilon^(h+1),

since the child's noisy singleton is at least its singleton mass, the relevant outer noisy numerator is at least a positive base mass, and its denominator is at most one. For the child's own empty edge the same bound holds with exponent h. Therefore all boundary log losses and exact erasure costs on positive upper mass are O_(G,t)(h+1). Their total upper spectral mass, after division by influence, is rho^h. The recurrence thus bounds the successive differences of cost and L by C(h+1)rho^h.

For K the upper-mass contribution is also O(rho^h). For the lower-mass part note all three predictors satisfy P_t(r)<=r. In the outer boundary sum,

    c_J^2 P_t(u_i U(J+j)/U(J)) <= u_i U(J+j),

because c_J^2<=U(J). Summing the finitely many outer pairs bounds this contribution by a gate-dependent constant times sum_i up_t^(g_h)({i}). The last sum is exactly (phi^h)'(t). After division by I(g_h), it is O(rho^h). The removed child boundary contributes at most W1(g_h)/I(g_h). Thus successive differences of K are absolutely summable as well.

Finally the predictor inequality and L>=0 give K_h>=2^(-cost_h), so the finite limiting K is positive. Taking its logarithm preserves convergence. This proves the assertion and supplies a convergent series specified by the finite recurrence. Numerically estimated limits are reported separately from this existence proof. For the biased AND/OR, tribes, and PM towers, depth-six values alone are numerical evidence; this argument does not silently extend to moving biases.
