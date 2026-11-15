# Composition and erasure proofs

All logarithms are base two. Phi(p,q)=p log(1+q/p)+q log(1+p/q), with continuous values on the axes. Boolean signs are +1 and -1; input bit x represents (-1)^x. E_i is conditional entropy in bits, not the averaging operator. All mathematical statements below have an explicit status.

## 1. Balanced-inner composition — PROVED

Let F have k coordinates and psi have m coordinates, with E psi=0. For a spectral set S write S_j for its intersection with block j and A={j:S_j is nonempty}. Expanding F in characters gives

    fhat(S)=Fhat(A) product_{j in A} psihat(S_j).

Indeed an inactive outer variable contributes the constant 1, and an active outer variable must contribute a nonempty inner set because psihat(empty)=0. There is exactly one outer set contributing. Squaring proves the hierarchical spectral law in the brief: choose V~mu_F, then independent U_j~mu_psi, j in V, and take their union. Every U_j is nonempty.

Fix i in block 1 and write a=psihat({i})^2 and d_F=Inf_1(F). Fix the outside nonempty-block pattern V' subset {2,...,k} and the actual spectral sets of these blocks; their common multiplicative weight is K=product_{j in V'} mu_psi(S_j).

If the trace B in block 1 minus i is nonempty, the two paired squared masses are K mu_F(V'+1) mu_psi(B) and K mu_F(V'+1) mu_psi(B+i). Homogeneity of Phi and summation over outside sets and V' make their contribution d_F E_i(psi). The omitted inner pair B=empty has endpoints 0,a and contributes zero.

If B is empty, the paired masses are K mu_F(V') and K a mu_F(V'+1). Summing K over all outside inner sets equals one. Define

    T_{F,1}(a)=sum_{V' subset {2,...,k}} Phi(mu_F(V'), a mu_F(V'+1)).

Consequently

    E_i(f)=d_F E_i(psi)+T_{F,1}(a),
    Inf_i(f)=d_F Inf_i(psi).

These identities also hold for nontransitive F and psi; the target indices must then be retained.

## 2. Unbalanced-inner composition — PROVED

Write c=E psi, t=1-c^2>0, and

    K_A(c)=sum_{B containing A} Fhat(B) c^{|B minus A|}.

When a block trace is empty, either the outer block was inactive or its psi factor contributed c. Expanding and collecting all these terms before squaring gives, exactly,

    fhat(S)=K_A(c) product_{j in A} psihat(S_j),
    A={j:S_j nonempty}.

Thus it is generally WRONG to use the uniform outer spectral measure and let its active blocks independently hit the empty set: amplitudes from these possibilities interfere.

There is a correct probability law. Let M_c(A)=t^{|A|} K_A(c)^2. The functions product_{j in A}(z_j-c)/sqrt(t) are an orthonormal basis for signs of mean c; their coefficients in F are t^{|A|/2} K_A(c). Parseval gives sum_A M_c(A)=1. Choose V~M_c, then independently, for each j in V, choose a NONEMPTY inner set with probability mu_psi(T)/t. The resulting union has the spectral law of f. This reformulation has absorbed every empty-block interference into the biased outer coefficients.

Put b=psihat({i})^2, d=Inf_i(psi), e=E_i(psi), and

    alpha(c)=sum_{B subset {2,...,k}} t^{|B|} K_{B+1}(c)^2,
    T(c,b)=sum_B t^{|B|} Phi(K_B(c)^2, b K_{B+1}(c)^2).

For a nonempty target trace B, the same homogeneity argument as above gives alpha times the inner erasure cost with its empty pair removed. The empty pair of psi contributes Phi(c^2,b). The empty target trace of f contributes T(c,b). Therefore

    E_i(f)=alpha(c)[e-Phi(c^2,b)]+T(c,b),
    Inf_i(f)=alpha(c)d,
    fhat({i})=K_{1}(c) psihat({i}),
    E f=K_empty(c).

Equivalently, the biased thinned term is sum_B Phi(M_c(B),(b/t)M_c(B+1)), and the inherited erasure is (d_{M_c,1}/t)[e-Phi(c^2,b)]. Here d_{M_c,1}=t alpha(c). Constants psi are handled by substituting its fixed output into F, giving a constant composite.

Let eta(T)=mu_psi(T)/t on nonempty T. Entropy of the hierarchical law, since its labels are recoverable from the union, gives

    H(f)=H(M_c)+I(M_c) H(eta),
    I(f)=I(M_c) I(psi)/t,
    H(eta)=[H(psi)-(-c^2 log(c^2))]/t+log(t).

These statements include all empty atoms; H(M_c) is the entropy of the whole biased outer spectrum.

## 3. Balanced transitive towers — PROVED

Let the balanced transitive base F have n>=2 variables, single-coordinate influence delta, singleton mass b, total influence lambda=n delta, entropy H0, and T(a)=T_{F,1}(a). Depth zero is a dictator; F^{(r+1)}=F applied to n disjoint copies of F^{(r)}. The wreath product of the outer transitive group and independent transitive groups within the blocks acts transitively on leaves and fixes the composite.

Induction using section 1 gives

    Inf_leaf(F^{(r)})=delta^r,
    singleton_mass_leaf(F^{(r)})=b^r,
    I(F^{(r)})=lambda^r,
    H(F^{(r)})=H0 (lambda^r-1)/(lambda-1),
    G_r=sum_{j=0}^{r-1} T(b^j)/delta^{j+1},
    sum_i E_i(F^{(r)})=lambda^r G_r.

At lambda=1 the entropy expression means r H0. If delta=1, transitivity forces every coordinate always pivotal, hence F is parity up to sign; then b=0 and all these erasure costs vanish. Otherwise 0<delta<1. Since D_i F takes values in {0,+1,-1}, |Fhat({i})|=|E D_i F|<=E|D_i F|=delta. Thus b<=delta^2.

For 0<a<=1, concavity and homogeneity imply

    T(a)<=Phi(1-delta,a delta)
         <=a delta[1/ln(2)+log(1+1/(a delta))].

Consequently the displayed series for G_infinity converges, and its tail from j=L is at most

    sum_{j>=L} (b/delta)^j [1/ln(2)+log(1+1/delta)+j log(1/b)].

This is a sum of geometric and arithmetico-geometric series. If b=0, G_infinity=T(1)/delta=G(F), exactly. This convergence proof also supplies a rigorous truncation bound without materializing a tower truth table. For nonconstant balanced F, I>=1 follows from Parseval; equality implies Fourier support only at level one. Write F=sum_j a_j x_j. The coefficient of x_j x_k in F²=1 is 2a_j a_k, so at most one a_j is nonzero; Parseval makes that coefficient +1 or -1. Thus F is a dictator up to sign. A transitive base with n>=2 is not a dictator, so lambda>1.

There is no universal identity G_infinity=lim H/I minus a base-independent constant: balanced parity has both zero; balanced majority of odd arity has G_infinity=0 but strictly positive limiting H/I. More detailed nonzero examples are computed in towers.json. This does not decide any equality between global suprema.

## 4. All transitive towers, including unbalanced bases — PROVED

For a transitive base F let c_0=0, s_0=d_0=1, R_0=0, H_0=0 and I_0=1. At stage r use c=c_r, t=1-c^2, b=s_r^2 and the kernels of section 2. Define

    c_{r+1}=K_empty(c),
    s_{r+1}=s_r K_1(c),
    d_{r+1}=d_r alpha(c),
    R_{r+1}=R_r + [sum_{B nonempty} t^{|B|}
                  Phi(K_B(c)^2,b K_{B+1}(c)^2)]/[alpha(c)d_r].

Then

    E_leaf(F^{(r)})=d_r R_r+Phi(c_r^2,s_r^2),
    G_r=R_r+Phi(c_r^2,s_r^2)/d_r,
    I_r=n^r d_r,
    sum_i E_i=n^r[d_r R_r+Phi(c_r^2,s_r^2)].

The H recurrence is exactly section 2 with psi=F^{(r)}. These are functions only of the finite base table. The R recurrence follows by subtracting the empty-pair term at the next stage: the B=empty term of T(c,b) is exactly Phi(c_{r+1}^2,s_{r+1}^2). Every R increment is nonnegative. This stable recurrence avoids subtraction of close entropies.

Here is a proof that G_r has a finite limit for every nonconstant transitive base of arity n>=2. Parity bases have G_r=0. For a nonparity base, alpha(c)<1 for every c strictly between -1 and 1. Otherwise D_1 F is always +-1 on the full-support biased product measure. Every input is then pivotal in coordinate 1; transitivity makes every input pivotal in every coordinate, forcing parity. Also alpha(c)>0 in the interior, so d_r is positive and nonincreasing.

Suppose d_r did not tend to zero. The product formula would force alpha(c_r)->1. Since alpha<1 on each compact interior interval, |c_r|->1. At any endpoint epsilon where alpha(epsilon)=1, all n neighbors of the constant input epsilon have the opposite output. Therefore, writing B(c)=E_c F=K_empty(c), a first-order expansion at that endpoint gives

    [1-B(c)^2]/[1-c^2] -> n.

All c_r remain strictly inside (-1,1), since a nonconstant Boolean function under a full-support input distribution is nonconstant. There are only two endpoints. The preceding limit implies that, eventually, t_{r+1}/t_r>(n+1)/2>1. This contradicts t_r->0. Hence d_r->0.

The singleton bound used in section 3 applies to the Boolean tower as well: |s_r|<=d_r. Thus

    0<=Phi(c_r^2,s_r^2)/d_r
       <=d_r[1/ln(2)+log(1+d_r^-2)] ->0.

The known finite-gate composition theorem of O'Donnell–Tan bounds H/I uniformly over all read-once formulas over a fixed finite gate basis (Theorem 3 of the opened paper). Every tower here is such a formula, so G_r<=H/I is uniformly bounded. Thus the increasing sequence R_r is bounded and converges. Consequently

    lim_r G_r=R_infinity
       =sum_{r>=0} [sum_{B nonempty} (1-c_r^2)^{|B|}
          Phi(K_B(c_r)^2,s_r^2 K_{B+1}(c_r)^2)]/[alpha(c_r)d_r].

This limit formula is proved, with the boundedness step explicitly relying on the existing finite-gate FEI theorem. The bias c_r need not converge for this argument. A numerical R_r is always a lower bound for the limit; an unbalanced numerical tail without a separate bound is not a certified limit.

## 5. Numerical checks — CHECKED NUMERICALLY

`OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 checks.py` writes composition_check.json. It exhausts all two-by-two outer/inner truth-table pairs up to constant inner functions, and checks additional seeded random examples up to twelve composite variables. It compares complete spectral amplitudes, each target coordinate's erasure and influence, singleton coefficients, H and I against the recurrences. This is an independent full truth-table route, not a check of the recurrence against itself. Exact counts and errors are in that JSON file.

## 6. An explicit tower truncation bound — PROVED (using O'Donnell–Tan)

An explicit, deliberately loose finite-gate constant is

    C_n=2(2^n-1)4^n/ln(2).

To see this from the opened paper rather than its asymptotic notation, Lemma 4.1 bounds each nonempty-set adjusted entropy term by 4^n/ln(2) times the variance of one biased derivative. Sum over at most 2^n-1 sets, bound every chosen derivative variance by their sum, and use sum_j Var(D_j F)<=2(I(F)-Var(F)), as in its Theorem 2 proof. Corollary 4.2 propagates this same constant to every read-once formula over gates of arity at most n, for every product distribution.

For a transitive such formula Q at common input bias c, set t=1-c^2 and M=its biased squared Fourier law. Its adjusted entropy is

    H_adj=sum_{A nonempty} M(A) log(t^{|A|}/M(A)).

The preceding theorem gives H_adj<=C_n I(M). Hence

    H(M)<=[C_n+log(1/t)+1/ln(2)] I(M),

because the empty-atom entropy is at most Var(Q)/ln(2)<=I(M)/ln(2). Transitivity and the entropy chain rule give E_1(M)/d_1(M)<=H(M)/I(M).

For any paired masses p,q and 0<a<=1,

    Phi(p,aq)<=a Phi(p,q)+a q[log(1/a)+1/ln(2)].

Indeed its first term is at most aq/ln(2), and its second term is at most aq[log(1/a)+log(1+p/q)]; the latter logarithmic term is one nonnegative part of a Phi(p,q). Sum the inequality over the pairs of M.

Now place an arbitrary additional upper tower Q over the depth-L inner tower. Section 2 and the definition of R show that its increase in R is the nonempty-pair thinned outer sum divided by alpha_Q d_L. Dropping the nonempty restriction only increases it. Apply the last inequality with a=s_L^2/t and d_1(M)=t alpha_Q. The log(1/t) and log(t/s_L^2) terms cancel, giving

    0<=R_infinity-R_L
      <=(s_L^2/d_L)[C_n+log(1/s_L^2)+2/ln(2)].             (TAIL)

For s_L=0 the tail is zero. This bound is uniform in the number of additional upper levels and passes to the limit. It gives a mathematical truncation error for every base, without any convergence assumption for the bias dynamics. Ordinary floating-point rounding is a separate issue and must still be audited. The same statement applies to mixed towers using the maximum gate arity.

## 7. Symmetric functions — PROVED, using the published symmetric FEI theorem

Let X_i=1[i in U]. For any ordering pi,

    sum_i H(X_i|X_{-i})
      <=sum_j H(X_{pi(j)}|X_{pi(1)},...,X_{pi(j-1)})=H(U),

by conditioning reducing entropy and the chain rule. Symmetry makes every E_i equal and every influence equal to I/n. Therefore E_1/Inf_1=(sum_i E_i)/I<=H/I. O'Donnell–Wright–Zhou's Theorem 1 gives

    E_1<=12.04 Inf_1

for every symmetric Boolean function. One can read their entropy bound directly in terms of W_r=P(|U|=r): symmetry makes U conditional on |U| uniform on its level, so

    H(U)=H(W)+sum_r W_r log binom(n,r).

Their Theorem 5 bounds the first term by 3I; Theorem 4 and log binom(n,r)<=r log(en/r) bound the second by 9.04I. The deduction to erasure is written above; the two analytic estimates are cited existing results, not re-proved here. Majority with odd arity has E_i=0: its Fourier support is only on odd levels, so the parity of U minus i determines whether i belongs to U.

## 8. ORs and thresholds of shifts of a fixed pattern — PROVED subclass bound

A pattern is a conjunction of w literals at distinct cyclic positions. Let f be the OR over all its cyclic shifts. It is cyclically invariant and has DNF width w, with any overlapping terms and with either sign of literal. More generally, requiring at least l shifts to occur is a DNF of width at most wl: choose any l shifts and conjoin their literal requirements. Inconsistent conjunctions are omitted. Set W=w in the OR case and W=wl in the threshold case.

Here is a full route to the explicit bound E_1<=(W+7.94)Inf_1. The argument works first for any width-W DNF, to establish the entropy bound; transitivity is used only at the last step.

At a coordinate let delta=Inf_i, g=E_i f and h=D_i f. Split the Phi sum into its empty pair and all other pairs. Concavity and homogeneity yield

    E_i<=Phi((E f)^2,(E h)^2)+Phi(Var(g),sum_{T nonempty} hhat(T)^2)
       <=Phi(1,delta^2)+Phi(Var(f),delta).

The inequalities use |E h|<=E|h|=delta and g^2+h^2=1. Since Phi is increasing,

    Phi(1,delta^2)<=delta^2/ln(2)+delta^2 log(1+delta^-2)
                    <=(1/ln(2)+1.1611)delta,
    Phi(V,delta)<=delta/ln(2)+delta log(1+V/delta).

The scalar bound x log(1+x^-2)<=1.1611 on (0,1] follows by differentiating: with y=x^-2 the stationary equation is ln(1+y)=2y/(1+y); its positive maximum is below 1.1611. The restriction-mixing cost J_i obeys J_i<=(2/ln(2))delta. For completeness, pair restriction amplitudes a,b and let u=(a+b)/2, v=(a-b)/2. The usual two-point entropy inequality

    ((a^2+b^2)/2)log((a^2+b^2)/2)
       -(a^2 log(a^2)+b^2 log(b^2))/2 >= -2v^2/ln(2)

can be proved as follows. Negating either amplitude leaves its left side unchanged and can only increase (a-b)^2 when signs differ; thus take both amplitudes nonnegative. Homogeneity reduces to a=1,b=z>0. After multiplying by 2 ln(2), the required inequality is D(z)>=0 for

    D(z)=(1+z^2)ln((1+z^2)/2)-z^2 ln(z^2)+(1-z)^2.

Here D(1)=D'(1)=0 and D''(z)=2[ln u+1/u-1]>=0, where u=(1+z^2)/(2z^2); the last inequality follows from ln u>=1-1/u. Continuity handles zero amplitudes. Summing over Fourier pairs gives J_i<=2 sum v^2/ln(2). Combining these bounds gives

    E_i+J_i<=delta[6.94+log(1+Var(f)/delta)].             (STEP)

The constant 6.94 exceeds 4/ln(2)+1.1611. The two-point scalar inequality is also verified over a dense scalar grid in subclass_checks.json; its analytic proof above is the standard two-point logarithmic Sobolev inequality, not a new theorem.

We need a coordinate with variance/influence bounded in terms of W. Select any nonempty satisfiable term t of width k<=W. For each input x with f(x)=-1, flip the disagreeing literals of t in a fixed variable order. Its endpoint satisfies t, so at least one traversed edge is pivotal. Charge x to the first such edge. At the j-th term variable, each pivotal edge is charged by at most 2^{j-1} possible x, because only the preceding coordinates can differ from the edge's initial endpoint. Dividing the counts by 2^n gives

    P[f=-1]<=sum_{j=1}^k 2^{j-1} Inf_{v_j}/2
            <=(2^k-1)max_j Inf_{v_j}/2.

Here the DNF output convention is +1 for satisfied; flipping the overall output changes none of H,I,E,J. Thus some term coordinate has delta>=2 P[f=-1]/(2^W-1). Since Var(f)<=4P[f=-1],

    Var(f)/delta<=2(2^W-1).

Every restriction is again a width-W DNF after simplifying constants. At each nonconstant decision-tree node choose a coordinate satisfying this last inequality. The exact restriction identities are

    H(f)=average_b H(f_b)+E_i+J_i,
    I(f)=average_b I(f_b)+delta.

Induct from constant leaves, apply (STEP), and use

    6.94+log(1+2(2^W-1))<W+7.94

to obtain H(f)<=(W+7.94)I(f). For the cyclic shift functions all E_i and all influences agree, so section 7's chain-rule bound gives the promised E_1<=(W+7.94)Inf_1.

This is a proved bound depending on pattern width (and on the shift threshold l). It does not supply one constant uniform in w or l. No literature novelty is asserted; the width-dependent route is already present in the supplied FLOW.

## 9. The size-biased deletion law — PROVED

This identity does not require transitivity. Let I=sum_S |S| mu(S)>0 and define a probability law on marked nonempty spectral sets by

    Q(U,i)=mu(U)/I,  i in U.

Its total mass is one. Equivalently, choose U with probability |U|mu(U)/I and then choose i uniformly from U. Under transitivity the marked coordinate is uniform on [n], since Q(i)=Inf_i/I=1/n. Conditional on that coordinate, U minus i has law mu(T+i)/Inf_i.

Define L(r)=r log(1+1/r)+log(1+r), with L(0)=0. A pair with q=mu(T+i)>0 contributes q L(mu(T)/q) to E_i. Pairs with q=0 contribute zero. Thus, exactly,

    (sum_i E_i)/I = E_Q L(mu(U minus i)/mu(U)).

The first term of L lies between zero and 1/ln(2); the second lies between [log r]_+ and 1+[log r]_+. Therefore

    E_Q[log(mu(U minus i)/mu(U))]_+
      <=(sum_i E_i)/I
      <=1+1/ln(2)+E_Q[log(mu(U minus i)/mu(U))]_+.

For a transitive function this is exactly G(f). Choosing U with law mu and then choosing a uniform element of U, WITHOUT the size bias, is incorrect.

## 10. What invariant-measure entropy inequalities leave open — PROVED obstruction; proof attempt remains OPEN

For independent Bernoulli(p) inclusion bits the measure is invariant under every permutation, I=np, and E_i=h2(p). Hence (sum_i E_i)/I=h2(p)/p is unbounded as p decreases to zero. Shearer/Han gives sum_i E_i<=H and is an equality on these laws. Thus coordinate invariance and these entropy inequalities alone cannot prove the desired bound; Boolean Fourier structure must enter.

Even the singleton necessary condition does not eliminate every such measure. For p=1/n, singleton mass p(1-p)^{n-1} violates mu({i})<=Inf_i^2 for large n. But for p=2 ln(n)/n and sufficiently large n it satisfies this inequality: (1-p)^{n-1}<=exp(-p(n-1))=n^{-2+2/n}<=p. Also sum_i Inf_i^2=np^2 tends to zero. These assertions concern candidate probability laws; they are not claimed to be Boolean spectra.

There is a useful exact obstruction from Booleanity. If a product Bernoulli(p) law with 0<p<1 is the exact uniform-cube Fourier spectrum of a Boolean function, then p is rational (it is an influence), and necessarily p=1/2. To prove this, write a_S=fhat(S). The convolution equation for the singleton shift i is

    0=sum_S a_S a_{S symmetric-difference {i}}
      =2 sqrt(p(1-p)) sum_{T subset [n] minus i}
          epsilon_T p^{|T|}(1-p)^{n-1-|T|},

where epsilon_T is the sign of a_T a_{T+i}, each +1 or -1. Set z=p/(1-p), divide by the nonzero common factor, and group by |T|. This gives an integer polynomial in z with constant coefficient +-1 and leading coefficient +-1, since each of the extreme levels contains one set. The rational root theorem forces its positive rational root to be z=1. Therefore p=1/2. For n=1 the polynomial is a nonzero constant, so no such nontrivial p exists. Bent functions show that p=1/2 is possible in some even dimensions. This obstruction excludes the exact product counterexample, but supplies no quantitative control of approximate product laws and no bound for G.

## 11. Convolution attempt — identities PROVED; needed estimate OPEN

Booleanity gives f^2=1, so for every nonempty R,

    sum_S fhat(S) fhat(S symmetric-difference R)=0.

Writing f=g+x_i h, the identities gh=0 and g^2+h^2=1 hold pointwise because one restriction pair either agrees or disagrees. Fourier transformation gives

    ghat* hhat=0,
    ghat* ghat+hhat* hhat=delta_empty,

where convolution is over the subset group with symmetric difference. In particular sum_T ghat(T)hhat(T)=0. Split this last sum into positive and negative products: their absolute totals agree. That cancellation alone does not bound the q-weighted positive logarithm of ghat(T)^2/hhat(T)^2. Cauchy–Schwarz only gives sum_T |ghat(T)hhat(T)|<=sqrt(delta(1-delta)); Jensen applied to the likelihood ratio gives a logarithm of 1/delta again.

A proof of the unrestricted transitive bound would need an additional quantitative statement using the full convolution system in all coordinates. Neither the equal-influence condition nor the one-shift orthogonality yields that statement in this attempt. The explicit product-law obstruction in section 10 is one consequence, not the missing inequality.

## 12. Supremum questions — OPEN / HEURISTIC

The mixed constructions provide explicit transitive lower bounds for both G_* and A_*, since all coordinates of each finite composition are equivalent. They do not identify the supremum over transitive f. The supplied bracket C_*-2/ln(2)<=G_*<=A_*<=C_* concerns all Boolean functions; it does not turn either endpoint into an equality for the transitive subclass.

HEURISTIC: transitive towers are a productive family for lower bounds, because the singleton leakage adds erasure over successive scales while transitivity equalizes coordinates. This is supported by the explicit computations, not a theorem that symmetrizing an arbitrary function preserves its minimum-coordinate ratio. No argument here proves that the transitive supremum equals G_*, or C_* minus any explicit universal constant. The base-dependent gaps in section 3 show why a per-base constant subtraction cannot establish such an identity.

## 13. An explicit transitive witness above four — PROVED construction; INTERVAL-CHECKED value

Let M on nine signs return -1 exactly when the graph with left and right vertex sets {0,1,2} and edge (r,c) present when z_{3r+c}=-1 has a perfect matching. Let N=-M. Set f_0(x)=x. For j>=1 apply gate N when j is odd and gate M when j is even to nine disjoint copies of f_{j-1}. This specifies the function without a large truth table.

Permuting the three left vertices and the three right vertices preserves M and acts transitively on its nine input edges. The same group preserves N. At each layer the wreath-product argument of section 3 gives transitivity on all leaves. Hence every coordinate of f_j has exactly the same positive influence and erasure entropy, and its minimum coordinate ratio equals G(f_j).

The interval implementation uses the equivalent row/column DNF on a 3-by-3 array. Here is an explicit proof of the equivalence. Split the six permutations of three letters into three even and three odd permutations. Every original edge belongs to exactly one even and one odd perfect matching. Send that edge to the array position indexed by those two matchings. Each even perfect matching becomes a full row and each odd perfect matching a full column. Thus the six matching terms become exactly the six row/column terms. `pm_isomorphism.py` constructs this coordinate permutation and verifies all 512 inputs in `pm_isomorphism.json`. Applying this relabeling recursively within the disjoint blocks preserves every tower statistic.

`python3 interval_witness.py` evaluates section 4's recurrence with outward interval arithmetic at ninety decimal digits. It uses the original nine-variable truth values, obtains biased coefficients by the direct pair transform

    (u,v) -> (((1+c)u+(1-c)v)/2, (u-v)/2),

and encloses x ln x continuously at zero when calculating Phi. Thus it does not rely on subtracting two full spectral entropies. `interval_witness.json` gives

    4.50504996749762 < G(f_7) < 4.50504996749764,
    number of variables = 9^7 = 4,782,969.

The numerical inequality is CHECKED by outward intervals; the reduction of the full function to these intervals is PROVED by sections 2–4. This provides the explicit lower bounds

    G_* >= 4.50504996749762,
    A_* >= 4.50504996749762,
    sup_{transitive f} G(f) >= 4.50504996749762.

The same interval script checks G(M composed with M)>4 already at 9^2=81 variables; its value is about 4.048135961762372. The seven-layer construction is the best retained finite witness in this folder; no global optimality or novelty claim is made.

The period [N,M], read from bottom to top, is equivalently self-composition of the transitive 81-input gate M composed with N. `periodic_audit.py` computes its limit as about 4.50501525844266655424811530523, with the analytic truncation bound of section 6; the direct coefficient transform at 260 decimal digits agrees with a Fourier/zeta calculation at 120 digits. The bound is on truncation; only the finite-witness file above uses outward intervals for rounding. Finite G can exceed its limit because the positive empty-pair term in section 4 disappears asymptotically.

## 14. The 6.278 base, with all path types accounted for — PROVED recurrence; CHECKED NUMERICALLY

Hod section 1.2 explicitly notes that the displayed O'Donnell–Tan base is biased, then supplies this balanced replacement with the same entropy and influence:

    g3=(x1 OR x2) AND (x3 OR x4) AND (x1 OR x3 OR x5)
           AND (x3 OR x5 OR x6).

Our truth convention takes a satisfied clause as true=-1. `hod_reconstruct.py` checks its balance, H=3.924340782942887 bits and I=13/8, giving the amplification H/(I-1) above 6.278944. Its coordinate influences are 3/8,5/16,1/2,1/4,1/8,1/16, so it is not transitive.

For a balanced but nontransitive base, retain a separate thinned function T_j(a) for each outer coordinate. For a leaf path built from bottom to top, let d be its current influence and b its singleton mass. Adding outer coordinate j changes

    d -> delta_j d,
    b -> b_j b,
    G -> G + T_j(b)/(delta_j d).

This is section 1 without discarding target indices. It is wrong to replace the minimum over all paths by the minimum of the limits of constant-coordinate paths.

The reconstructed g3 is monotone, so b_j=delta_j^2 and b=d^2 along every path. Future increments therefore depend only on d and the new coordinate j; among paths with the same d only the smallest current G need be retained. This gives an exact finite-depth dynamic program. Every product influence for g3 has the form 3^a 5^b 2^-h, so the integer triple (a,b,h) identifies it exactly. The scalar G values are evaluated numerically. `ot_tower_dp.py` implements this recurrence and records its surviving states and a minimizing path at each depth.

Here is a uniform tail bound justifying passage from paths to the infinite tower. Put rho=max_j delta_j<1 and delta_min=min_j delta_j>0. Section 3's coarsening bound implies that, for every next coordinate, the increment is at most

    d[1/ln(2)+log(1+1/(d^2 delta_min))]
       <=d[C0+2 log(1/d)],
    C0=1/ln(2)+log(1+1/delta_min).

The function x[C0+2 log(1/x)] is increasing on (0,1] here, since C0>=2/ln(2) for these bases. After l further levels d_l<=d rho^l. Summing the geometric and arithmetico-geometric series bounds every path's remaining cost by

    B(d)=d[(C0+2 log(1/d))/(1-rho)
                +2 log(1/rho) rho/(1-rho)^2].

Thus the minimum finite-depth G is a lower bound for the minimum infinite-path limit, and min_state[G+B(d)] is an upper bound. Both converge together. Branches whose current G already exceeds a feasible upper bound can be discarded because all future increments are nonnegative.

CHECKED NUMERICALLY: for g3, the minimum tower limit is about 3.6848626341, as bracketed in `ot_tower_dp.json`; it is smaller than every constant-path limit. For Hod's neighboring balanced improved base, obtained by replacing the last clause by (x2 OR x4 OR x6), the minimum tower limit is about 4.0148464660. These are nontransitive comparisons, not the best transitive witnesses. The analytic B(d) controls truncation; the DP's floating-point evaluations are not interval certificates. The finite transitive record in section 13 has its own interval check.
