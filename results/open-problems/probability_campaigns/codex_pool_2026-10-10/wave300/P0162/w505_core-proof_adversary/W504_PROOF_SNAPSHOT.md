# Restriction entropy and the coordinate-selection gap

Worker w504, 2026-10-10. These are mathematical arguments by the worker, pending independent review by w506. They are not a proof of the FEI conjecture. No novelty is asserted. Definitions and the primary-source target are in STATEMENT.md. All logarithms here have base 2.

## 1. Exact defect identity

Fix a coordinate i of a Boolean function f. Let g=f_i^+ and h=f_i^-. For every Fourier index T on the remaining coordinates set u=ghat(T), v=hhat(T), w_T=(u^2+v^2)/2. For w_T>0 put p_T=u^2/(u^2+v^2) and q_T=(u-v)^2/[2(u^2+v^2)]. Ignore zero-weight indices. Then sum_T w_T=1 and

    Inf_i(f)=sum_T w_T q_T,
    Delta_i(f)=sum_T w_T [1+h_2(q_T)-h_2(p_T)],

where h_2 is binary entropy. These are equalities, including zero coefficients. Proof: fhat(T)=(u+v)/2 and fhat(T union {i})=(u-v)/2. Their squared masses are w_T(1-q_T), w_T q_T. Hence H(f)=H(w)+sum w_T h_2(q_T). Meanwhile the probability law P(B=+,T)=u^2/2, P(B=-,T)=v^2/2 has uniform branch marginal. Its entropy is both 1+[H(g)+H(h)]/2 and H(w)+sum w_T h_2(p_T). Subtract the two equalities. Parseval justifies the uniform marginal; no independence between B and T is assumed.

The extra term 1-h_2(p_T) is nonnegative. Dropping it gives a lower bound, not an upper bound, on Delta_i. This identity is derived here directly; it does not assume any constant-preserving equivalence of alternative source inequalities.

The influence splitting equality is

    I(f)=Inf_i(f)+[I(g)+I(h)]/2.

Indeed for T not containing i, the average squared coefficients of g and h are fhat(T)^2+fhat(T union {i})^2; multiply by |T| and sum. The missing contribution is exactly the i-influence.

## 2. Proved reduction, unproved input

If there exists one finite universal K such that every nonconstant Boolean f has a coordinate i with Delta_i(f)<=K Inf_i(f), then FEI holds with the same K. Induct on the number of variables: constants have zero entropy and influence; apply the hypothesis to f and the induction hypothesis separately to its two Boolean restrictions; then use the influence equality above. Irrelevant variables can simply be removed. This is a sufficient reduction already present in Gonzalez--MacManus--Pereyra (2026), Ansatz 1.1. It is not a proof of the coordinate-selection input, and necessity is not asserted.

## 3. A family for which the right coordinate can be proved

Use bit coordinates b in {0,1}^m, with Walsh characters (-1)^(s dot b); this is the same uniform cube after x_j=(-1)^b_j. Let m=2k>=2, a=2^(-k), t=a^2=2^(-m), and

    g_m(b)=(-1)^(b_1 b_2 + b_3 b_4 + ... + b_(m-1) b_m),
    h_m(b)=g_m(b)-2 1_{b=0},
    F_m(b,z)=g_m(b) if z=0, and h_m(b) if z=1.

Both restrictions and F_m are Boolean because g_m(0)=1. The Walsh transform of one pair is (1,1,1,-1)/2, so by the product formula ghat_m(s)=a epsilon_s with epsilon_s=(-1)^(s_1 s_2+...+s_(m-1)s_m). Among the 2^m indices the signs have counts N_+=(2^m+2^(m/2))/2 and N_-=(2^m-2^(m/2))/2, since sum_s epsilon_s=2^(m/2). These facts follow directly from the two-bit transform, without a classification of bent functions.

Because the indicator at zero has every coefficient t, Fhat_m(s,0)=a epsilon_s-t and Fhat_m(s,1)=t. The selector influence is t. Each base coordinate has influence 1/2+t: g_m has influence 1/2 in that coordinate, and flipping g_m at zero increases its disagreement probability by 2t on the edge {0,e_j}; averaging the two z-restrictions gives the assertion. Consequently

    I(F_m)=m/2+(m+1)t.

For c>=0 and a positive parameter d define

    L(c,d)=sum_(epsilon=+-1) [(1+epsilon d)/2]
             (1-c epsilon a)^2 log_2[(1-c epsilon a)^2],

with 0 log 0=0. The two exact entropy formulas are

    H(F_m)=m(1+t)-L(1,a),
    H(h_m)=m-L(2,a).

To verify the first, the selector-present slice contains 2^m masses t^2, giving 2mt. The selector-absent slice has masses t(1-epsilon a)^2 and total mass 1-t, giving m(1-t)-L(1,a). The second formula follows similarly from hhat_m=a(epsilon-2a), whose squared masses sum to one.

### 3a. The selector is a provably bad coordinate

Its exact defect is

    Delta_z(F_m)=mt-L(1,a)+L(2,a)/2.

Since h_m has at most 2^m Fourier atoms, H(h_m)<=m, hence L(2,a)>=0. Using ln r<=r-1 for r>0 (and the continuous zero convention),

    L(1,a) <= [sum_epsilon ((1+epsilon a)/2)
                         (1-epsilon a)^2 ((1-epsilon a)^2-1)]/ln 2
             =3t(1-t)/ln 2.

The last equality uses E[epsilon]=a and expands a polynomial. Thus

    Delta_z(F_m)/Inf_z(F_m) >= m-3(1-t)/ln 2 -> infinity.

This disproves a universal bound that must hold for EVERY coordinate. It does not disprove FEI or the EXISTS-coordinate missing lemma. The independent adversary w505 found a bent-selector obstruction before reading this packet; this family is complementary context, not a separate novelty claim.

### 3b. Every base quadratic coordinate is good (the main special-case result)

Fix any base coordinate j. When b_j=1, its partner contributes a parity and the other pairs stay quadratic, so H(F_m|b_j=1)=m-2: the exceptional point b=0 cannot occur. When b_j=0, the quadratic part consists of m-2 bits and is independent of the partner bit and z. The restriction equals that quadratic function except for a flip at one point of these m bits.

Its zero-control Walsh block has coefficients 2a epsilon-2t, with sign weights (1+2 epsilon a)/2. Its other three control blocks each have coefficients -2t. The zero-control block has mass 1-3t; each other block has mass t. The same entropy calculation gives

    H(F_m|b_j=0)=m-2+3mt-L(1,2a).

This formula also holds for m=2: the quadratic core has zero variables and its sole Walsh sign is +1. Therefore

    Delta_j(F_m)=2-(m/2)t-L(1,a)+L(1,2a)/2.

The difference of the L terms simplifies exactly to

    L(1,2a)-2L(1,a)
      =-[(1-a)^2 log_2(1-a)+(1+a)^2 log_2(1+a)].

For 0<=a<=1/2, R(u)=u^2 log_2 u is convex on [1/2,3/2], because R''(u)=(2 ln u+3)/ln 2>0 there. Jensen gives R(1-a)+R(1+a)>=2R(1)=0. Thus L(1,2a)<=2L(1,a), and

    Delta_j(F_m)<=2-(m/2)t < 4(1/2+t)=4 Inf_j(F_m).

This proves an explicit suitable-coordinate bound for all m in this family. It does not assert that the entire family is closed under arbitrary restrictions, and hence does not invoke the general induction with an unstated closure assumption.

### 3c. Direct FEI special case with constant 2

The selector-present spectral mass is t. Conditional on either presence or absence there are at most 2^m possible base indices, so by the chain rule H(F_m)<=m+h_2(t). Also -(1-t)ln(1-t)<=t, hence h_2(t)<=mt+t/ln 2. For m>=2,

    H(F_m)<=m+(m+1/ln 2)t <=m+2(m+1)t=2I(F_m).

No conditional probabilities are multiplied, and no independence is needed. This is a proved special case, pending independent review; not a solution of P0162.

## 4. Single hardest remaining gap

Prove, or refute with a family, the universal suitable-coordinate input: there is a finite K such that every nonconstant Boolean f admits at least one coordinate i with Delta_i(f)<=K Inf_i(f). The construction proves why a fixed selector cannot be used, while its base-coordinate calculation succeeds. No argument here extends that calculation to arbitrary Boolean restrictions. A general proof must use the Boolean Fourier convolution constraints beyond just the normalized weights w_T and small Inf_i. Otherwise the term h_2(q_T)/q_T can diverge as q_T tends to zero. This is the unresolved input; the reduction and the special family above do not close it.

The exact remaining input can be localized to all-small-influence functions. From section 1 and 0<=h_2<=1, every coordinate has 0<=Delta_i(f)<=2. Fix any tau in (0,1), for example tau=1/16. If there is a uniform K_0 for suitable-coordinate selection whenever ALL influences of f are less than tau, then every other f has a coordinate with Inf_i>=tau and Delta_i<=2<=(2/tau) Inf_i. Thus the universal suitable-coordinate lemma follows with K=max(K_0,2/tau), and the reduction gives FEI. Conversely, the universal selection lemma obviously implies its all-small-influence restriction. For tau=1/16 the unresolved statement is therefore: some finite K_0 works for a suitable coordinate of EVERY Boolean f with max_i Inf_i(f)<1/16. This is a proved localization of the gap, not a proof of its all-small-influence input. The positive family in section 3 has large base-coordinate influences and does not settle this hard regime.

The owner scar fei_most_influential_coordinate_fails_by_composition_2026_09_24 explicitly warns that a bad selector can become the unique most influential coordinate after balanced disjoint compositions. We do not propose that rule. The owner small-influence reduction in fei_opus_wave1_reduction_small_influences_gates_and_ltf_2026_09_23 is relevant prior work; our simple Delta<=2 argument above is recorded as a transparent sufficient reduction, not as a new theorem.

NEXT: Independently check section 3b and identify a structural reason that forces a good coordinate for arbitrary Boolean spectra.
