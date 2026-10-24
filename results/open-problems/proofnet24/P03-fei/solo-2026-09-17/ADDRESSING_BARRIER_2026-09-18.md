# Every positive-power edge majorant fails

Status: proved below, self-checked, novelty UNVERIFIED. This is an obstruction to an attempted proof of FEI, not a counterexample to FEI. It supersedes the proposed interior-moment attack in the initial `NEXT_STEPS.md`.

All logarithms are base two. For Fourier probabilities p_S=fhat(S)^2, edges mean unordered pairs of subsets differing in one coordinate. Put

    T_gamma(f) = sum_edges min(p_S,p_T)^(1-gamma) max(p_S,p_T)^gamma.

The sum is over edges with two positive endpoints; a zero-endpoint edge contributes zero by definition. This agrees with the continuous formula for 0<=gamma<1, which contains the entire originally proposed range 0<gamma<=1/2. With this convention, for every fixed gamma>0 there is NO finite universal constant C_gamma with T_gamma(f)<=C_gamma I(f). In particular gamma=1/4 is false, not merely unproved.

## 1. The explicit Boolean family

Let m>=2 be even, N=2^m, x in {0,1}^m, z in {+1,-1}, and let y=(y_a : a in {0,1}^m) be N independent sign bits. Define

    g(x)=(-1)^(x_1 x_2+x_3 x_4+...+x_{m-1}x_m),
    h(x,y)=y_x,
    f_m(z,x,y)=[(1+z)/2]g(x)+[(1-z)/2]h(x,y).       (1)

This is Boolean pointwise: z selects one of two Boolean branches. Its dimension is n=m+1+N. We do not claim to enumerate its truth table at large m.

Write chi_S(x)=(-1)^(sum_{i in S}x_i). The two-bit Walsh transform of (-1)^(x_1 x_2) is (1,1,1,-1)/2. Tensoring gives

    ghat(S)=s_S/sqrt(N),  s_S in {+1,-1}.

The address indicator has expansion

    1{x=a}=N^(-1) sum_S chi_S(a) chi_S(x).

Consequently the complete nonzero Fourier coefficients of (1), indexed by (S,b,D) with b the presence of z and D a data subset, are

    fhat(S,b,empty)=s_S/(2 sqrt(N)),                    (2)
    fhat(S,b,{a})=(-1)^b chi_S(a)/(2N).                 (3)

Every coefficient with |D|>=2 is zero. Equations (2)-(3) are derived from (1), not assumed compatible squared coefficients: Boolean realizability and its signed convolution identities hold exactly.

There are 2N coefficients of squared magnitude 1/(4N), and 2N^2 of squared magnitude 1/(4N^2). Each group has total mass 1/2.

## 2. Exact invariants and the power obstruction

For each x-coordinate and z, all nonzero adjacent pairs have equal masses. Each such coordinate has influence 1/2, edge-minimum sum 1/2, and erasure entropy 1. A data coordinate y_a has influence 1/(2N). This also follows directly: it matters exactly when z=-1 and x=a.

Across all data coordinates there are exactly 2N^2 nonzero edges, each with masses

    r=1/(4N),  s=1/(4N^2),  r/s=N.

No other nonzero-edge types exist. Thus

    I(f_m) = (m+2)/2,
    T_gamma(f_m) = (m+1+N^gamma)/2,                    (4)
    T_gamma(f_m)/I(f_m) = (m+1+2^(gamma m))/(m+2).

For every fixed gamma>0 the last expression tends to infinity along even m. This proves the claimed obstruction. At gamma=0 it instead equals one: the elementary T_0<=I is sharp on this family.

The precise actual entropy quantities are

    H(f_m) = 2+3m/2,
    B(f_m) = m+1 + [(N+1)log(N+1)-N log N]/2,          (5)
    L(f_m) = [m+1+log(N+1)]/2.                         (6)

Proof of (5): the two spectral groups above give H=(1/2)log(4N)+(1/2)log(4N^2). The x and z erasure terms sum to m+1. By homogeneity E(r,s)=h(r)+h(s)-h(r+s), the data edges give

    2N^2 E(1/(4N),1/(4N^2))
      = [(N+1)log(N+1)-N log N]/2.

Proof of (6): along each x or z direction the endpoint containing the coordinate has mass 1/2 and downward ratio one, hence contributes 1/2 to L. Along data directions the total containing-endpoint mass is 1/2 and the downward ratio is N. This gives (6).

In particular H/I=3-2/(m+2)<3, B/I tends to 3, and L/I tends to 2. For the B limit, use

    (N+1)log(N+1)-N log N
      = log N+(N+1)log(1+1/N)
      = m+1/ln(2)+o(1).

The failure of T_gamma<=C_gamma I is therefore emphatically NOT an FEI counterexample. The proposed scalar majorant loses exponentially more than the actual logarithmic entropy on these functions.

## 3. Logarithmic growth is the critical scale

For a nonnegative function Phi on [0,infinity), define

    W_Phi(f)=sum_edges min(p_S,p_T) Phi(|log(p_S/p_T)|),

again assigning zero to an edge with a zero endpoint. The same count gives

    W_Phi(f_m)=[(m+1)Phi(0)+Phi(m)]/2.                 (7)

Hence if Phi(m)/m is unbounded along even integers, no universal bound W_Phi<=C I can hold. This kills not only exponential moments Phi(t)=2^(gamma t), but t^(1+epsilon), t log(2+t), and every majorant with superlinear growth along those scales. No monotonicity assumption on Phi is needed for (7); the stated sequence condition is needed for its consequence.

Let

    M_f(t)=sum_edges min(p_S,p_T) 1{|log(p_S/p_T)|>=t}.

For this family, M_f(t)=1/2 for 0<t<=m, and zero for t>m. In particular

    M_f(m)/I(f_m)=1/(m+2).

Therefore a universal tail estimate M_f(t)<=C I(f)/(1+t)^(1+epsilon) is false for every epsilon>0. More generally no nonnegative nonincreasing integrable envelope w(t) can satisfy M_f(t)<=C I(f) w(t) for all f,t: the even-m examples force w(m)>=1/[C(m+2)], and monotonicity then forces a divergent harmonic lower bound on its integral. Without monotonicity a conclusion based only on isolated points would be invalid; we do not make it.

Thus a universal bound on the integral of M must exploit scale allocation depending on f. It cannot follow from an integrable uniform monotone tail envelope. This does not prove that a scale-allocation argument exists.

## 4. An exact logarithmic version of the live target

Set

    K(f)=sum_edges min(p_S,p_T) |log(p_S/p_T)|,
    M(f)=sum_edges min(p_S,p_T).

For r>=s>0,

    E(r,s)=s log(r/s)+(r+s)log(1+s/r).

Since log(1+t)<=t/ln(2), the final term lies between zero and 2s/ln(2). Continuity covers zero endpoints. Hence

    K<=B<=K+(2/ln2) M<=K+(2/ln2) I.                  (8)

The last inequality orients each edge toward its endpoint containing the toggled coordinate: min(p_S,p_T) is at most that endpoint's mass, and their sum is I. Also, layer cake gives K=integral_0^infinity M_f(t) dt (the choice >= rather than > does not change the integral).

Thus a universal K<=C I is equivalent, up to constants, to the live B bound and hence to full FEI by `ERASURE_REDUCTION.md`. Equation (8) itself is only a reformulation. The substantive new obstruction is that no superlinear enlargement of this logarithmic cost can be bounded universally.

For (1), K=m/2 and M=I=(m+2)/2. The real logarithmic cost can be charged to selector/address directions, whereas the data influence alone is only 1/2.

## 5. Checks and limits

`check_addressing_barrier.py` computes full integer Walsh transforms for m=2 and, when NumPy is installed, m=4; verifies every nonzero signed coefficient and the absence of others; verifies exact influence, entropy and the entire nonzero-edge histogram; and checks the signed convolution identity on the m=2 table. For m=4, T_(1/4)=7/2 and I=3 are checked with exact rational fourth roots. Large-m ratio examples are evaluations of the proved formula (4), not truth-table searches.

`addressing_barrier_certificate.json` records the actual checks. The all-m theorem is justified by the algebra above, not finite enumeration. Self-checks are not independent audits.

The first exploratory variant considered one rare bent marker with a large majority selector. Its heuristic balance suggested an obstruction only for gamma>1/3. It was abandoned before making a theorem claim: replacing the one marker by independently addressed data bits yields (1), which settles every positive gamma without Gaussian asymptotics or a majority estimate. No remaining obligation relies on that abandoned heuristic.

## 6. Continuation

Do not try gamma=1/8, gamma approaching zero but fixed, or another superlinear log majorant. All are covered by this obstruction. The original logarithmic target remains open. A positive, limited selector-to-data charging lemma is proved separately in `SELECTOR_CHARGING_2026-09-18.md`; its architecture assumption is essential to the proof and does not solve the full conjecture.
