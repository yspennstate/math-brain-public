# The exact leading loss of the fixed edge reference

Let g_m=2[(OR_i x_i) AND (OR_j y_j)]-1 on 2m independent uniform bits, m>=2. Use its exact m^2 prime pairs, lambda_ij=1/m, beta=1/m, one fresh control and gamma=6/5. Psi is the complete nonempty-data signed correction of the source distributed lift. Its T=empty control-only overhead and inherited (1/2)R_g remain separate. The following is uniform over the old actual-forest posteriors:

    Psi/I(g_m) = (1/4)log2 m + 1/20 + o(1).              (1)

This strengthens A015's lower bound on this SAME correction. The coefficient 1/4 replaces the earlier lower-bound coefficient 15/64 because this computes the limit, rather than weakening finite-m factors. It is not a new estimate of H/I or of the reference infimum.

Put a=2^-m. Direct product expansion and physical pivot counting give

    I=4ma(1-a), v=4(1-a)^2(2a-a^2),
    |ghat(T)|=2a(1-a) for nonempty within-side T,
    |ghat(T)|=2a^2 for T meeting both sides.

For a within-side T of size s, EVERY record has k=s, all owned blocks and intersections have size one, and all gates are separate roots. The exact occupation/root sum is consequently

    L0=m^-s,  J1=s! m^-s 2^(4(s-1)/5).                  (2)

No posterior is optimized or replaced in (2). With S distributed as Binomial(m,1/2), B_m=E log2(S!) and 0!=1, the within-side contribution divided by I is exactly

    W_m=(1-a)/(2m) [m log2 m - B_m
                             -(4/5)(m/2-1+a)].         (3)

The factor 1/4 in Psi is retained: there are two within-side families, each coefficient squared is 4a^2(1-a)^2, and sum_s binom(m,s)=2^m. These three factors give (3).

For cross-side T, every used edge has (owned size,intersection) in {(1,1),(1,2),(2,2)}. Its occupation ratios satisfy 1/9<=w_l(0)<=1 and 1/2<=w_l(1)<=1. Raising to the fifth power checks these finitely many rational comparisons exactly. Therefore, choosing any one fresh owner gives Z>=9^-k, while summing all k possible owners gives Z<=k. The exact root factor is >=1 and <=(k-1)!4^(k-1), since c<=k and all root rarities equal 1/4. With k<=2m,

    (9m)^(-2m)<=J1(T)<=(8m)^(2m),
    m^(-2m)<=L0(T)<=1.

The bounds hold recordwise and hence under the SAME posterior. Total cross mass is 4a^2(1-a)^2, so its signed contribution C_m obeys the TWO-SIDED estimate

    |C_m|/I <= a(1-a)log2(9m) -> 0.                    (4)

This is stronger than using only a lower bound on cross compensation. It supplies the missing upper control needed for an asymptotic equality.

Keep the EXACT normalizers

    D=(1+1/(4m))^(m^2)-1,
    D'=(1+1/(8m^2))^(m^2)-1.

The normalizer contribution divided by I is exactly

    Q_m=(1-a)(2-a)/(2m) log2(2D'/D).                    (5)

For x>=0, x-x^2/2<=ln(1+x)<=x follows by differentiating the differences, with equality at zero. Thus ln D/m ->1/4 (write ln D=m^2 ln(1+1/(4m))+ln[1-(1+1/(4m))^(-m^2)]). The bracket tends to one: the preceding lower bound makes its subtracted term decay exponentially. Also 1/8<=D'<=e^(1/8)-1 by Bernoulli and ln(1+x)<=x. Hence log(2D') is bounded and

    Q_m -> -(log2 e)/4.                               (6)

The negative normalizer has a NONZERO limiting contribution; discarding it would give the wrong constant in (1).

For completeness the only factorial asymptotic required is

    B_m/m = (1/2)log2 m -(1+log2 e)/2 + o(1).          (7)

Integral comparison of the increasing function ln x gives ln(s!)=s ln s-s+O(1+ln(m+1)), uniformly in integers 0<=s<=m, with 0 ln0=0. Set X=S/m. E X=1/2 and Var X=1/(4m). On X>=1/4, the derivative of x ln x has absolute value at most one; the complementary probability is <=4/m by Chebyshev and x ln x is bounded on [0,1]. Cauchy-Schwarz therefore gives E[X ln X]=(1/2)ln(1/2)+O(m^-1/2). Taking the FINITE expectation of the uniform integral-comparison bound proves (7). This argument handles changing binomial domains; no unjustified passage of a limit through an infinite posterior sum is used.

Equations (3),(7) yield W_m-(1/4)log2 m -> (1+log2 e)/4-1/5. The factor a log m tends to zero. Adding (4),(6) gives 1/4-1/5=1/20, proving (1). Every denominator I,m,D,D',L0,J1 is strictly positive throughout m>=2. The exact prime-table argument uses monotonicity: minimal positive implicants must force one literal on each side, so the primes are precisely these pairs; negative literals cannot belong to a minimal implicant.

This is a proof of a fixed selected-transfer loss, not a lower bound on optimal queue cost. By SCALE_CANCELLATION.md, shifting its scale charge to a normalized OLD reference does not lower the combined selected-mass bill at the SAME FINAL weights. A repair must change a substantive final reference, representation or witness family and then pay all retained costs.
