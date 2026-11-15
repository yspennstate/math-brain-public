# C001 v2: logarithmic-band improvement using the chi-log cumulant

Kind: bound (constant update of accepted C001 narrowing); target: 2. Author: codex-w690. Independently ACCEPTED by an agent; see audit TSV.
This strengthens accepted C001 v1; it does not solve the full target.
The method remains HXP's initialization/perturbation/escape argument, now
with a fractional-moment Chernoff estimate and explicit polynomial costs.

## Explicit statement

In the same fixed nonzero-data setting and W-coordinate learning-rate
convention as v1, for sufficiently large L,

    max(d_x,d_y) <= m <= L/(420 log L),       0 <= eta <= 1

imply, with probability at least

    1 - m/L - L^(-612/8335),

that loss stays in [0.4,0.6]||Y||_F^2 for all integer

    0 <= t <= floor(exp(L/(21000m))).

The horizon constant is weaker than v1, but the covered width interval is
larger. Keep v1 where it is stronger. The eta<=1 condition does not extend
HXP Theorem 5.1's allowance of eta up to exp(c L^gamma).

A parameterized version below covers every fixed C>250+20sqrt(66), with
m<=L/(C log L), probability tending to one, and a positive horizon
exp(h_C L/m). The threshold is about 412.4808 and is a limit of this
particular power-counting argument, not an impossibility theorem about GD.

## A fractional chi-log estimate

For 0<=s<=2 and a layer with output dimension d<=m, put

    F_d(s) = log E (chi_d/sqrt(d))^s
           = (s/2) log(2/d) + log Gamma((d+s)/2)-log Gamma(d/2).

We have F_d(0)=F_d(2)=0. The trigamma identity and its integral lower bound give

    psi_1(x)=sum_(n>=0) 1/(x+n)^2 >= integral_0^infinity 1/(x+t)^2 dt = 1/x.

Thus, throughout [0,2],

    F_d''(s) = psi_1((d+s)/2)/4
              >= 1/(2(d+s)) >= 1/(2(m+2)).

Subtract the quadratic with this second derivative and zero endpoints.
The difference is convex with zero endpoint values, hence nonpositive.
Consequently

    F_d(s) <= -s(2-s)/(4(m+2)).                          (V2.1)

This proves the needed estimate directly from the exact chi-square
moment formula; it is a Chernoff bound on the sum of log-norm increments.
The classical trigamma series is also tabulated at NIST DLMF 5.15.1,
https://dlmf.nist.gov/5.15.E1 .

Conditioning successively on the previous layers gives, for a fixed unit
vector and a block P of length k,

    E ||P v||^s <= exp(-k s(2-s)/(4(m+2))).               (V2.2)

Since s<=2,

    ||P||^s <= ||P||_F^s
             = (sum_j ||P e_j||^2)^(s/2)
             <= sum_j ||P e_j||^s,

so E||P||^s is bounded by m times the right side of (V2.2).
This dimension factor is retained.

## Initialization at the explicit parameters

Use the normalized A_i=W_i/sqrt(d_i) from v1, with beta=1, and set

    q=L/m, K=L^(3/2), a=4/175, b=403/21000,
    h=1/21000, delta=exp(-b q).

First suppose m>=10000. By the same second-moment calculation as v1,

    Pr[some block norm > K] <= L^2 m/K^2 = m/L.         (V2.3)

For a block with j-i>=L/10, set s=1/2 in (V2.2). Its half-moment is at most

    m exp(-3L/(160(m+2)))
       <= m exp(-(125/6668)q),

because m/(m+2)>=10000/10002. Markov applied to this half-moment, followed
by the union over L^2 blocks, yields

    Pr[some long block norm > exp(-a q)]
       <= L^3 exp(-(125/6668-a/2)q)
       <= L^(-612/8335),                               (V2.4)

where the last equality of exponents follows exactly from

    420(125/6668-a/2)-3 = 612/8335 > 0.

Thus the two deterministic initial-product properties hold with the
probability stated above. No independence between block events is used.

## Perturbation and GD induction, with new powers

Let ||A_i-A_i(0)||<=delta for every layer and z=L K delta. At
q>=420 log L,

    z <= L^(-139/25).

The same expansion as v1 gives all perturbed block norms <=2K.
For blocks with j-i>=L/4, one-perturbation terms have one initial gap
with index difference >=L/10 (L>=40); their total is <=z exp(-a q).
The sum of the terms with at least two perturbations is bounded by

    2 L^2 K^3 delta^2 = 2 L^(13/2) exp(-2b q)
                      <= 2 L^(-1/50) exp(-a q).

For sufficiently large L this is at most exp(-a q), so every such
long perturbed product has norm at most 3 exp(-a q), exactly as in v1.

Output and gradient estimates therefore give

    ||U||_F <= 3 exp(-a q)||X||_F,
    ||A_i(t+1)-A_i(t)|| <= eta G K exp(-a q),
    G=7||X||_F||Y||_F.

The output is at most ||Y||_F/20 for sufficiently large L, since a*420=48/5.
For N=floor(exp(h q)), eta<=1, and all t<=N, summing the update bounds gives

    ||A_i(t)-A_i(0)|| / delta
       <= G L^(3/2) exp(-(a-b-h)q)
       <= G L^(-1/50) <= 1/2,

for sufficiently large L. This closes the neighborhood induction and
proves the plateau, with the same [0.45125,0.55125] inner loss bounds as v1.

The exact exponent balances are

    420b - 5/2 = 139/25,
    420(2b-a) - 13/2 = 1/50,
    420(a-b-h) - 3/2 = 1/50.

For the finitely many widths m<10000, take L sufficiently large that
10000<=L/(10000 log L). Then accepted v1 applies simultaneously to all
these widths. Its horizon exp(q/1000) is longer than exp(q/21000), and its
failure probability 1/L+L^-47 is at most m/L+L^(-612/8335).
This proves the explicit result uniformly over the stated interval.

## The limiting constant within this argument

For clarity, this section optimizes the proof architecture, not the GD
problem. Let C be fixed, q>=C log L, retain K=L^(3/2), and write

    A=a C, B=b C, H=h C, H>0.

The deterministic proof needs the strict inequalities

    B>5/2,   2B-A>13/2,   A-B-H>3/2.                    (V2.5)

The last two imply A>19/2+2H. Conversely, if A>19/2+2H, one can choose B
in ((A+13/2)/2, A-3/2-H); then B>5/2 automatically.

For any fixed s in (0,2), the moment estimate and the block/dimension union
give a positive polynomial tail exponent when, for all sufficiently large m,

    C s(2-s)/40 - s A > 3.                              (V2.6)

The factor m/(m+2) tends to one; choose a fixed sufficiently large cutoff
M_0 to preserve any strict margin in (V2.6). Widths below M_0 are again
covered by v1 for sufficiently large L.

Let A decrease to 19/2 and H decrease to zero. The supremum over s of
the left side of (V2.6), before subtracting 3, is

    max_(0<s<2) [C s(2-s)/40 - (19/2)s].

For C>190 it is attained at s=1-190/C and equals

    C/40 - 19/2 + (1805/2)/C.

It exceeds 3 precisely on the relevant branch

    C > 250+20sqrt(66).

For each such C, continuity allows A>19/2, H>0 and s in (0,2) with strict
margins; then choose B and M_0 as above. The preceding proof gives
probability tending to one and horizon exp(h_C q), h_C=H/C>0.

For C at or below this limiting value, this particular collection of
polynomial-envelope and cumulant inequalities cannot supply a positive
horizon exponent. Other envelopes, trajectory information, or methods may
do better. In particular this is no obstruction to the research target C=1.

## Research routing

This completes the lead-authorized bounded constant exercise. It still
does not cover L/(420 log L)<m<=L/log L. Accepted C002 explains why retaining
the same deterministic neighborhood at q~log L is not sufficient.
The lead's next priority is target 1, polynomial-time GD for every fixed
m=cL. Do not spend another session tuning the constants in this argument.
