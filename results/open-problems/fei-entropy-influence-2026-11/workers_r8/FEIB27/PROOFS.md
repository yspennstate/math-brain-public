# Proofs and limitations of the dictionary

Throughout, entropy and logarithms use base two. The Fourier coefficient convention is the uniform Walsh basis, and truth-table bit x is one exactly when f(x)=-1.

## 1. The local dictionary cannot supply a universal bound

PROVED. Write delta=Inf_i. Every term used in census.cpp is nonnegative and at most delta. This is immediate for a sum of mu(S) over S containing i with a multiplier in [0,1]. It covers the singleton term, M_i=sum_{S containing i}mu(S)/|S|, the degree cap, each noisy influence, and each low-level truncation. For the perspective term, M_i<=delta gives delta log2(1+M_i/delta)<=delta, with value zero when delta=0.

The suggested normalized second-order term is exactly

    sum_{j != i} sum_{S containing i,j} mu(S)/(|S|-1)
      = sum_{S containing i, |S|>=2} mu(S) =: B_i.

Each Fourier set contributes |S|-1 equal shares. In particular sum_i B_i=I-W_1, with W_1=sum_i mu({i}), and B_i<=delta.

For Boolean restrictions, h=(f_0-f_1)/2 has values 0,+1,-1, so E|h|=Eh^2=delta. Likewise g=(f_0+f_1)/2 has E|g|=1-delta. Its deficit 1-E|g| reproduces delta; E|g| itself has no O(I) sum, since it equals one at every coordinate of a constant function.

Consequently any fixed nonnegative coefficients give

    sum_k c_k t_k(f,i) <= (sum_k c_k) Inf_i(f).

It remains to exhibit an unbounded E_i/Inf_i. The following construction gives an exact two-point law, rather than an asymptotic estimate for majority.

Let k be positive and even, let y be k bits, and set

    b(y)=(-1)^(y_1 y_2 + y_3 y_4 + ... + y_(k-1) y_k).

The two-bit factor has Walsh coefficients (1,1,1,-1)/2. By taking products, every Walsh coefficient of b is +/-2^(-k/2). At y=0, b(0)=1; hence the sum of all its coefficients is one. Writing B=2^(k/2), the fractions of positive and negative coefficients are (1+1/B)/2 and (1-1/B)/2.

Adjoin x, with f(0,y)=b(y) and f(1,y)=b(y) except f(1,0)=-1. Then

    h=1_{y=0},  g=b-1_{y=0},  delta=2^-k.

For every T, hhat(T)=2^-k, so rho_h is uniform over the 2^k subsets. The ratio p_T/q_T is (B-1)^2 on the positive coefficients of b and (B+1)^2 on the negative coefficients. Define

    F(r)=log2(1+r)+r log2(1+1/r).

Homogeneity of Phi now gives the exact expression

    E_x/delta = (1+1/B) F((B-1)^2)/2
              + (1-1/B) F((B+1)^2)/2.

For k>=4 every ratio is at least (B-1)^2, and F(r)>=log2(r). Thus E_x/delta >=2 log2(B-1), which diverges. Moreover F(r)=log2(r)+log2(e)+o(1), so E_x/delta=k+log2(e)+o(1).

Therefore no finite coefficients in this whole dictionary can give a universal per-coordinate inequality. Allowing signed coefficients would not rescue it either if the sum of absolute coefficients stayed bounded. This says nothing adverse about the summed inequality: the bad coordinate can be paid for by other coordinates. The explicit family is nonmonotone; the separate majority-hiding family in FLOW gives an obstruction within monotone functions as well, but its asymptotic is not needed for this proof.

## 2. Most summed terms fail for a different reason

PROVED. Except for Inf_i and B_i, every tested term has a sum bounded by a constant times Var(f), rather than merely I(f). The constants below are sufficient, not optimized:

| Term | Upper bound on its sum over coordinates |
| --- | --- |
| singleton or M_i | Var |
| degree cap min(1,2/|S|) | 2 Var |
| noisy influence at fixed rho<1 | (1-rho^2)^(-2) Var |
| delta log2(1+M_i/delta) | log2(e) Var |
| truncation to levels at most r | r Var |

The spectral sums follow by exchanging the coordinate and Fourier-set sums. For the noise term, k rho^(2(k-1)) <=sum_{l>=1}l rho^(2(l-1))=(1-rho^2)^(-2). For the perspective use log2(1+x)<=x/ln 2 and sum_i M_i=Var.

These bounds cannot control summed erasure entropy uniformly. Consider OR of m disjoint clauses of width w. Use the +/-1 encoding f=2 product_j(1-A_j)-1, where A_j is the clause indicator. If i is in the first clause, let A be the conjunction of its w-1 mates and B the product of the other clause complements. In the +/-1 convention for x_i,

    h=A B,  g=2B-A B-1,
    delta=2^(-(w-1)) (1-2^-w)^(m-1).

Whenever the rest of the spectral set meets the w-1 mates, ghat=-hhat. Such sets carry rho_h mass 1-2^(-(w-1)), because A has a flat Fourier spectrum. On that mass Phi(p,q)=2q. Hence

    E_i >=2(1-2^(-(w-1))) delta.

Choose m=floor((ln 2)2^w). Then I=mw delta grows as w ln 2, while Var<=1. Therefore sum_i E_i grows without bound. Every fixed combination whose total is O(Var) fails. The only unresolved summed directions in this dictionary must retain Inf_i or B_i. A combination containing Inf_i cannot improve the certified objective sum c_k over the Inf_i-only solution, since all other terms are pointwise at most Inf_i.

This proves failure of the variance-budget directions; it does not prove the surviving B_i direction or FEI.

For the LP, independent term budgets give the valid but sometimes loose objective C=sum_k c_k. A sharper joint budget is available for all the linear spectral terms: if t_k(f,i)=sum_{S containing i}mu(S)w_k(|S|), then C=max_{d>=1}sum_k c_k w_k(d) certifies sum_i sum_k c_k t_k<=C I. The tested kernels are all nonincreasing after degree three; with c_k>=0, degrees one, two and three therefore certify every dimension. This is the objective in joint_fit.json. In particular singleton_i+B_i=Inf_i, so that pair reproduces the Inf_i bound with the same joint budget, rather than paying twice. The perspective term is omitted from this exact joint-kernel fit because it is nonlinear; its independent-budget fit remains valid.

## 3. Certified potential budgets

PROVED. All eight potential functionals in search.py are nonnegative. Their budgets Theta_k<=b_k I are

    I:1, Var:1, sum mu log2(1+|S|):1,
    sum_i Inf_i^2:1, sum mu |S|2^-|S|:1/2,
    H(|U|):3, h2(Var):2, two-block skeleton entropy:2+log2(3).

The first five follow from Parseval, Var<=I, log2(1+k)<=k for nonnegative integers k, 0<=Inf_i<=1, and 2^-k<=1/2 for k>=1. Thus the logarithmic functional is an admissible potential, contrary to the brief's parenthetical description of it as not O(I).

For the entropy budgets, use the established edge-isoperimetric consequence I>=(V/2)log2(1/V)+V, V=Var. It appears as Proposition 2 in [O'Donnell, Wright and Zhou](https://yuanz.web.illinois.edu/papers/fei-icalp.pdf), Section 3.2. Since -(1-V)log2(1-V)<=V/ln 2<=2V, it gives h2(V)<=2I. Conditional on |U|>=1, the geometric reference law Pr[G=k]=2^-k and nonnegative relative entropy give H(|U| conditional nonempty)<=I/V. Splitting off the empty set therefore gives H(|U|)<=h2(V)+I<=3I, the paper's Theorem 5. For the two-block skeleton there are at most three nonempty outcomes, so its entropy is at most h2(V)+V log2(3)<=(2+log2(3))I. The partition used in code is the first floor(n/2) labels versus the rest; under restrictions labels retain their relative order.

These are budget proofs. They do not assert that the potentials have helpful restriction drops.

For any spectral linear functional Theta_w=sum_S mu(S)w(|S|), averaging a uniform restriction at i replaces the pair a=fhat(T), b=fhat(T+i) by a+b and a-b. Squaring and averaging removes the cross term. Thus

    Theta_w(f)-avg Theta_w(f_b)
      =sum_{S containing i}mu(S)[w(|S|)-w(|S|-1)].

For w(k)=k the drop is delta; for log2(1+k) it is at most delta; for k2^-k it is at most delta/2. The variance drop is fhat({i})^2<=delta. Also, for j!=i, the two child influences have average Inf_j, so convexity of the square implies that the drop of sum_j Inf_j^2 is at most delta^2<=delta. None of these five potentials alone can improve a delivered C+K constant over zero potential, because its drop is at most its own budget times delta at every coordinate.

## 4. A finite-census obstruction for the entire potential span

PROVED, WITH AN INTERVAL CERTIFICATE FOR THE EXPLICIT WITNESS. Suppose one census function f has D_i=(E_i+J_i)>=R Inf_i for every relevant coordinate, and every potential's drop d_ki<=b_k Inf_i on every relevant coordinate. For Theta=sum a_k Theta_k, a_k>=0, any successful chosen-coordinate inequality gives

    R Inf_i <= C Inf_i +sum a_k d_ki
             <=(C+sum a_k b_k) Inf_i.

So its delivered constant C+sum a_k b_k is at least R. This lower bound respects the existential coordinate: it holds at every possible chosen coordinate. If zero potential works across the census at R, it is optimal within this span, using these certified budgets.

The witness is OR of eight disjoint two-variable clauses. Its truth table and Fourier coefficients are exact integers. interval_audit.py independently constructs those integers and encloses the entropy expressions using directed interval arithmetic. It verifies the necessary inequalities on every coordinate. The certificate is interval_audit.json. The ordinary MILP in search.py separately encodes the coordinate choice with binary selectors, and must agree with the interval lower bound.

This is a finite-census impossibility of improving the certified delivered constant with this span. It is not a theorem that these potentials cannot establish some larger universal constant.

For the literal form (T) in the brief, the same symbol C bounds both the step coefficient and Theta/I. Under our certified coefficient budget K=sum a_k b_k<=C, the witness gives R<=C+K<=2C. Conversely choose C=R/2 and Theta=C I. The exact restriction identity I-avg I_children=Inf_i then makes the right side of the step inequality 2C Inf_i=R Inf_i. Thus whenever zero potential works on the finite census at R, this potential works for literal form (T) at C=R/2. The two lower bounds match. The literal common-C optimum is therefore R/2 (about 3.001873028279544), while the delivered C+K optimum is R (about 6.003746056559088). This is an accounting identity; it gives no stronger FEI constant. common_constant.json records both conventions.

## 5. What the pointwise laws and the quoted impossibility do not prove

PROVED. The positive log moment L_i=E_{rho_h}[log2(p/q)]_+ satisfies

    delta L_i <= E_i <=delta[L_i+1+log2(e)].

Indeed, Phi(p,q)=p log2(1+q/p)+q log2(1+p/q), the first summand is at most q log2(e), and max(0,log2 r)<=log2(1+r)<=1+max(0,log2 r). Sum over T, treating zero masses by continuity. A uniform upper bound on min_i L_i would therefore give FEI through the tree identity. That bound remains a conjecture, even if it survives a census and a million perturbations.

PROVED logical limitation. A bad coordinate, or two functions with identical (Var,influences) at one chosen coordinate and different step costs, cannot rule out a potential depending on those statistics when the requirement is SOME coordinate. In particular Theta=0 is itself a function of those statistics. Its good-coordinate inequality is equivalent to boundedness of the FEI constant. FLOW 12(w)'s comparison is an obstruction to bounding every queried coordinate by that local information; it is not a proof excluding all such best-coordinate supersolutions.

HEURISTIC. The surviving summed B_i direction could be worth studying as a strengthened FEI formulation, but no proof, equivalence with the same constant, or claim of novelty is supplied here.

## 6. A proved local refinement involving the surviving second-order term

PROVED. Put B_i=Inf_i-fhat({i})^2 and A_i=Var(f)-Inf_i. Both are nonnegative. Then

    E_i <= (2+log2(e)) B_i + B_i log2(1+A_i/B_i),

with the right side interpreted as zero when B_i=0. This is a refinement of the relative-variance step estimate, not FEI: the last term has no known O(I) sum.

Here are all the steps. Let m=ghat(empty)=E f and b=hhat(empty)=fhat({i}). The Boolean restrictions imply g and h have disjoint supports, |g| and |h| are their support indicators, E|h|=delta and E|g|=1-delta. Hence |b|<=delta and |m|<=1-delta. Parseval gives sum_{T nonempty}q_T=delta-b^2=B_i and sum_{T nonempty}p_T=1-delta-m^2=A_i.

The scalar inequality Phi(p,q)<=2 sqrt(pq) gives

    Phi(m^2,b^2)<=2|mb|<=2delta(1-delta)<=2B_i.

For completeness, prove that scalar inequality without an assumed entropy estimate. It is trivial if p or q vanishes. Otherwise Phi is symmetric and homogeneous, so set p=e^u,q=e^-u,u>=0. In natural-log units Phi equals

    G(u)=2cosh(u) ln(2cosh(u))-2u sinh(u).

For u>0, set F(u)=u coth(u)-ln(2cosh(u)). Direct differentiation gives F'(u)=(tanh(u)-u)/sinh(u)^2<=0, because (u-tanh(u))'=tanh(u)^2>=0 and u-tanh(u)=0 at zero. Also F(u) tends to zero as u tends to infinity: coth(u)-1=2/(e^(2u)-1) and ln(2cosh(u))=u+ln(1+e^(-2u)). Thus F(u)>=0. Consequently G'(u)=-2sinh(u)F(u)<=0 and G(u)<=G(0)=2ln 2. Restoring the common scale proves Phi(p,q)<=2sqrt(pq).

Concavity and homogeneity of Phi imply sum_{T nonempty}Phi(p_T,q_T)<=Phi(A_i,B_i). One can see this directly as the log-sum inequality, applied separately to the two parts of Phi. Finally

    Phi(A,B)=A log2(1+B/A)+B log2(1+A/B)
            <=B log2(e)+B log2(1+A/B).

Add the empty-set estimate. If B_i=0, h has only its constant coefficient and is constant in real space. Since h takes values 0,+1,-1, delta is zero or one. In either case g and h cannot have simultaneous nonzero Fourier mass, and E_i=0, as required.

CHECKED NUMERICALLY. `python3 search.py refined` independently tests this estimate on the retained hard witnesses and generated controls, and compares the scalar Phi bound over a wide ratio range. Output: refined.json. No novelty claim is made.

## 7. Proof attempts that still stop at FEI

PROVED limitation of the attempted tools. The uncertainty estimate |hhat(T)|<=delta implies every atom of rho_h is at most delta, so H(rho_h)>=log2(1/delta). This lower bound concerns the derivative spectrum alone. It does not bound its positive log ratio against p: the bent construction in Section 1 obeys both real-space identities gh=0 and g^2+h^2=1 while that ratio diverges. Using those identities at just one coordinate cannot prove the needed best-coordinate assertion.

The log-Sobolev/support-density estimate delta log2(1/delta)<=2 I(h) can pay a bad coordinate by derivative influence. But summing I(D_i f) over i gives sum_S |S|(|S|-1)mu(S), which is not bounded by a dimension-independent multiple of I; parity already makes the quotient n-1. Normalizing the second-order influence down to B_i removes exactly the degree factor that paid for the logarithm. This explains the gap rather than bridging it. Shearer's erasure bound sum_i E_i<=H(mu) similarly returns the entropy whose O(I) bound is the original problem. No attempted argument here proves the surviving summed inequality or the best-coordinate log-moment conjecture.

## 8. An exact transitive counterexample to the half-mass candidate at p<=4q

PROVED, WITH EXACT INTEGER ARITHMETIC. On m pairs (a_j,b_j), define the monotone Boolean event

    F_m = OR_j(a_j AND b_j) OR (AND_j a_j) OR (AND_j b_j),

and f_m=1-2F_m. Pair permutations and simultaneous exchanges of all a_j with b_j preserve the event and act transitively on the 2m coordinates. Every coordinate therefore has the same influence and conditional spectral ratio law. There is no better coordinate hidden by the following computation.

Fix a_1. The remaining variables are b_1 and L=m-1 pairs. For a spectral set T, let s indicate b_1 in T and let r,u,v,z count the remaining pairs with neither element in T, only a, only b, or both, respectively. Put N=2*4^L, the remaining cube size. In the ordinary disjoint-pair tribes function the integer Walsh numerators of h and g, with denominator N, are

    H0=(-1)^(s+z) 3^r,
    G0=(3 if s=0 else -1) H0 - N 1_{T empty}.

To verify these formulas, the Fourier coefficients of 1_{b_1=1} are (1/2,-1/2), those of 1-1_{a=b=1} are (3/4,1/4,1/4,-1/4), and g=(2-b_1) product_{j>=2}(1-a_j b_j)-1. Multiply these factors and clear the denominator N.

Adding the two transversal clauses changes the original event at exactly two points: one chooses a=1,b=0 in every pair, and its complement chooses a=0,b=1. On the remaining cube their characters are chi_A=(-1)^(u+z) and chi_B=(-1)^(s+v+z). The first lies in a_1=1 and the second in a_1=0. Consequently the modified numerators are exactly

    H=H0+chi_A-chi_B,    G=G0-chi_A-chi_B.

There are L!/(r!u!v!z!) spectral sets for each choice of r,u,v,z,s. The derivative-sensitive set loses one original point and gains one, so its support size remains 3^L. Parseval gives sum_T H^2=N 3^L. Thus the desired conditional mass is the exact rational number

    sum_{r,u,v,z,s: G^2<=4H^2} [L!/(r!u!v!z!)] H^2 / (N 3^L).

At m=9 this finite integer sum has numerator 429970409 and denominator 859963392. Twice the numerator is 22574 smaller than the denominator, proving that the conditional mass is strictly below one half. These integers are generated in transversal_certificate.json by `python3 transversal_certificate.py`. The script independently builds all 262144 truth-table values, takes an integer Walsh transform, and checks that its entire (G,H) histogram equals the multinomial formula, not merely that the final fraction agrees.

The candidate held on the restriction-closed census and both directed proposal streams, but is false on this larger transitive function. The larger stress family also raises the observed best-coordinate positive-log moment above the original census maximum; it remains below two in the checks. The data and the scopes stay separate in stress.json and REPORT.md.
