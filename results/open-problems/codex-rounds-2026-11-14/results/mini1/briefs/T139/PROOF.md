# Exact Fourier concentration on four variables

Write Boolean values as -1 and +1, with +1 meaning true. All expectations are uniform. For a Boolean function f on four variables, let

\[
\widehat f(S)=\frac1{16}\sum_{x\in\{-1,1\}^4}f(x)\prod_{i\in S}x_i.
\]

Let d(f) be the smallest number of terms in a DNF for f. The empty disjunction is false and has zero terms; the empty conjunction is true and has one term. Let w_1(f)>=...>=w_16(f) be the squared Fourier coefficients in decreasing order, including zeros. Define

\[
T_f(m)=\sum_{j=m+1}^{16}w_j(f),\qquad
F_t(m)=\max_{d(f)\le t}T_f(m),\qquad 0\le m\le16.
\]

## Finite result

Exhaustive exact computation gives F_2(m)=F_3(m)=A_m/256, where

| m | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| A_m | 256 | 220 | 184 | 148 | 112 | 80 | 64 | 48 | 32 | 28 | 24 | 20 | 16 | 12 | 8 | 4 | 0 |

For every t>=4,

\[
F_t(m)=1-\frac m{16}.
\]

Thus, for every 0<epsilon<1, the exact worst-case number of monomials needed at term budget t is

\[
K_t(\epsilon)=\min\{m:F_t(m)\le\epsilon\}.
\]

In particular K_2(epsilon)=K_3(epsilon) throughout this interval, and for t>=4,

\[
K_t(\epsilon)=\lceil16(1-\epsilon)\rceil.
\]

The values for t=0,1 are also saved in `tail_envelope.csv`.

## Exhaustion and arithmetic

Encode an assignment by a in {0,...,15}, with x_i=+1 if bit i-1 of a is one. Encode a function by the 16-bit integer M whose a-th bit is one exactly when the function is true at a. There are exactly 2^16=65,536 such functions.

A consistent conjunction chooses, independently for each variable, no constraint, a negative literal, or a positive literal. There are 3^4=81 conjunctions, including true. Every contradictory conjunction can be discarded from a DNF. Duplicate literals can be removed. Consequently these 81 truth sets suffice to represent every DNF on four variables.

The program constructs these truth sets in two ways: by testing each ternary pattern against all assignments, and by intersecting literal truth sets for each fixed-coordinate subset and each assignment to it. It checks equality of the resulting sets of 81 masks.

For each conjunction mask C there is an edge M -> M OR C of cost one. Paths from zero are precisely unions of conjunctions, with path length equal to the number of terms. The shortest path to M therefore has length d(f_M). A strict union adds a bit, so its integer mask is greater than the starting mask. Processing masks in increasing integer order and relaxing every edge computes all shortest paths. Self-edges cannot improve a distance. Predecessor pointers give explicit DNFs.

An independent calculation fixes the target on-set M. A prime implicant is a conjunction contained in M that cannot be enlarged by removing one literal while remaining in M. Every conjunction contained in M can be enlarged to a prime implicant. Replacing a term by such an enlargement leaves the represented union within M, so a minimum cover can be chosen from the prime implicants.

For an uncovered subset U of M, choose its least point a. With the allowed prime implicants fixed by M, the minimum remaining cover obeys

\[
h_M(\varnothing)=0,\qquad
h_M(U)=1+\min_{C\ni a} h_M(U\setminus C).
\]

Every cover must include a term containing a, giving the lower bound in this recurrence; adding that term to a minimum cover of the remainder gives the upper bound. Each recursive call removes a, so the recurrence terminates. Terms may overlap previously covered points: the allowed prime implicants are never restricted to U. This matters for exact DNF minimization. The computed h_M(M) agrees with the union shortest-path distance for all 65,536 masks.

The signed Fourier numerators b_S=16*hat(f)(S) are computed by an integer Walsh transform. The transform's character is (-1)^(a dot S), so its S-th output is multiplied by (-1)^|S| to match x_i=+1 when a_i=1.

Independently, let P_S be the assignments where the character product is +1. Expanding f=2*1_M-1 and chi_S=2*1_(P_S)-1 gives

\[
b_S=4|M\cap P_S|-2|M|-2|P_S|+16.
\]

This expression agrees with every transform coefficient. Parseval is checked as the integer identity sum_S b_S^2=256 for each function. A separate saved-data audit computes all coefficients a third way, by summing the sixteen explicit products f(x)*product_(i in S) x_i, without importing the enumeration program.

Sorting b_S^2 and summing the smallest 16-m values gives the numerator of T_f(m). Maximizing over all functions with d(f)<=t gives the table. This maximum is computed independently again from the saved per-function data. Every one of the 153 saved envelope entries for t=0,...,8 and m=0,...,16 includes a witness DNF whose truth table and tail are checked directly.

The minimum-term histogram is:

| d(f) | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|---|
| count | 1 | 81 | 1804 | 13472 | 28904 | 17032 | 3704 | 512 | 26 |

These counts sum to 65,536. The maximum term count eight also has a direct proof. Partition the cube into the eight pairs obtained by fixing x_2,x_3,x_4. The true points in each pair need at most one term: use the conjunction fixing those three variables if both are true, a full four-literal conjunction if exactly one is true, and no term if neither is true. Thus eight terms always suffice. Parity requires eight, since every conjunction with a free variable contains both a true point and a false point, and its eight true points must therefore be covered by singleton terms. Term budgets beyond eight add no functions.

## Explicit extremizers

The first five table entries m=0,...,4 are attained by the OR of two conjunctions on disjoint pairs of variables. Let A=(1+x_1)(1+x_2)/4 and B=(1+x_3)(1+x_4)/4 be their indicators. The signed Boolean function is

\[
f=-1+2A+2B-2AB.
\]

Its constant coefficient is -1/8. For each of the six nonempty subsets lying within one pair, the coefficient has absolute value 3/8. For each of the nine subsets meeting both pairs, it has absolute value 1/8. Hence the square numerators are 36 six times and 4 ten times, independently confirming those table entries.

For m=5,6,7, the saved witness mask 001b is

\[
(\neg y_1\land\neg y_2\land\neg y_4)
\ \lor\ (y_1\land\neg y_3\land\neg y_4),
\]

where y_i indicates x_i=+1. The two terms are disjoint. Its true assignments are a=0,1,3,4. For nonempty S, the Fourier numerator is twice the sum of the character over these four assignments, while the constant numerator is 2*4-16=-8. The character sum over them equals

\[
(-1)^{|S|}\bigl(1+(-1)^{s_1}+(-1)^{s_1+s_2}+(-1)^{s_3}\bigr),
\]

where s_i indicates membership in S and the expression is independent of s_4 apart from the displayed sign. As (s_1,s_2,s_3) varies, the bracket has absolute value 4 once, 2 four times, and 0 three times. Accounting for the two choices of s_4 and replacing the constant numerator gives square numerators 64 twice, 16 eight times, and 0 six times. Its tails at m=5,6,7 are therefore 80/256, 64/256, 48/256.

For m=8,...,16 a conjunction on all four variables attains the table. Its true set has one assignment. Its constant coefficient has absolute value 7/8 and each of the other fifteen coefficients has absolute value 1/8. Its tail is (16-m)/64 for m>=1.

For t>=4 the upper bound follows without enumeration: the m largest of sixteen nonnegative weights of sum one have sum at least m/16. To attain equality, let h be the XOR of y_1*y_2 and y_3*y_4, and put f=2h-1. A four-term DNF for h is

\[
(y_1y_2\neg y_3)\lor(y_1y_2\neg y_4)
\lor(\neg y_1y_3y_4)\lor(\neg y_2y_3y_4).
\]

Write A=y_1*y_2 and B=y_3*y_4 as above. Then f=-(1-2A)(1-2B). Each two-variable factor has four Fourier coefficients of absolute value 1/2. Since the variable pairs are disjoint, their product has sixteen coefficients of absolute value 1/4. Thus all sixteen squared weights are 1/16, attaining the upper bound for every m. Its truth mask is 7888. The independent minimum-cover checks give minimum term count four.

## Optimal constant for errors at most one half

For every n<=4, every t>=2, and every 0<epsilon<=1/2, a t-term DNF admits a polynomial with squared error at most epsilon and at most

\[
t^{\,2\log_2(1/\epsilon)}
\]

monomials. The constant 2, with this base of logarithm and this epsilon range, is optimal.

To prove the upper bound for n=4 and t=2,3, first consider epsilon<=1/4. Taking all sixteen Fourier coefficients gives zero error, and

\[
16\le\epsilon^{-2}=2^{2\log_2(1/\epsilon)}
\le t^{2\log_2(1/\epsilon)}.
\]

For 1/4<epsilon<=1/2, let m=floor(epsilon^(-2)). Then 4<=m<=15. The table satisfies

\[
(m+1)A_m^2\le256^2
\]

for every such m. In order m=4,...,15, the left sides are

\[
62720,38400,28672,18432,9216,7840,6336,4800,3328,2016,960,256,
\]

all at most 65,536. Consequently

\[
F_t(m)=\frac{A_m}{256}\le\frac1{\sqrt{m+1}}<\epsilon.
\]

The strict inequality follows from epsilon^(-2)<m+1. The retained count obeys m<=epsilon^(-2)<=t^(2 log_2(1/epsilon)), as required.

For t>=4, retaining all sixteen coefficients suffices, because t^(2 log_2(1/epsilon))>=t^2>=16.

A function on fewer than four variables can be padded with unused variables. Its minimum DNF size is unchanged: padding preserves any DNF, and restricting the unused variables in any padded DNF yields a DNF on the original variables with no more terms. Its nonzero Fourier coefficients are also unchanged. Hence the assertion extends to n<=4.

For optimality, use the disjoint-pairs example. Its three largest squared coefficients sum to 27/64<1/2, and its four largest sum to 36/64>=1/2. Thus squared error at most 1/2 requires four monomials. For any polynomial supported on a set of characters, Parseval makes its best coefficients exactly the corresponding Fourier coefficients; arbitrary real coefficients cannot improve this tail. At t=2 and epsilon=1/2 the proposed count with constant C is 2^C, so C>=2.

The epsilon restriction cannot be removed while retaining constant 2. For the same example at epsilon=27/32, the count would be (32/27)^2=1024/729<2, permitting at most one monomial. Its best one-monomial squared error is 1-9/64=55/64>27/32. This does not contradict Mansour's conjecture, which allows a larger constant.

## Reproduction

```sh
OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 compute_four_variable.py > computation_output.txt 2>&1
OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 audit_saved_data.py > audit_output.txt 2>&1
```

`functions.csv` contains one row per function, with minimum DNF term count and sixteen signed Fourier numerators, all with denominator 16. `tail_envelope.csv` contains exact tails with denominator 256 and explicit witness terms. A witness term is a four-entry list with -1 meaning an absent literal, 0 a negative literal, and 1 a positive literal. `spectral_types.csv` and `spectral_types_by_terms.csv` give the spectrum multiplicities and their distribution by minimum term count.

This is a finite computation and its corollary. It gives no uniform bound as the number of relevant variables grows.
