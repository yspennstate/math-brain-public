Overall verdict on the Theorem: **SOUND**.

The stated inequality for every n≥14 follows after the small proof repairs below. The printed manuscript has missing justifications, and its claim that the same printed constants work from n=10 is false. All gaps affecting the theorem are filled here. The numerical search found no counterexample.

The verdicts below concern the manuscript as written; “filled” means that this report supplies the omitted argument.

| Statement | Verdict | Reason |
|---|---|---|
| Step 1 | CORRECT | Independent polynomial and determinant expansions agree; C is strictly positive. |
| Normalisation | GAP | Sign reversal must include reversing the sorted coordinate order; filled. |
| Step 2 (I) | CORRECT | The quadratic is negative at both endpoints and eps≤1. |
| Step 2 (II) | CORRECT | The missing derivative calculation is nonnegative; both root ranges cover all required eps. |
| Step 3 | GAP | “The ratio grows” needs proof, and eps=0 needs separation from strict comparisons; both filled. |
| Remark 1 | GAP | The note lists zeros without proving exhaustiveness; filled: these are the only two families. |
| Remark 2 | WRONG | The printed 0.002 bound fails at n=10,11,12, and the printed 1% comparison fails at n=10. A changed-constants proof from n=10 is supplied. |
| Remark 3 | CORRECT | Sorting identifies the largest product within each sign. |

Step 1. Write A=n²−6n+6. Expanding the proposed right side gives the coefficients

$$
q:\quad 2(n-3)-2=2(n-4),
\qquad p^2:\quad -2(n-3),
$$
$$
\text{constant}:\quad
-\frac{2(n-3)+A}{n}=-(n-4),
\qquad m:\quad C.
$$

This is exactly the defining expression for Psi. The script also expands both sides formally in the polynomial ring Q[n,q,p²,m] after clearing n(n−1); the difference is zero.

The Gram matrix, using sum x=0, is

$$
\begin{pmatrix} n&0&T\\0&T&P\\T&P&Q\end{pmatrix}.
$$

Its six-term determinant expansion is nTQ−nP²−T³. Positive semidefiniteness and T>0 give q−p²≥1/n. For every n≥5, A=(n−3)²−3≥1, hence C=(n−1)(A+2nq)>0. In particular there is no sign problem in T³Psi≥G_M.

Command: `nice -n 15 /Library/Frameworks/Python.framework/Versions/3.13/bin/python3 audit.py 1`.

Normalisation. The problematic line is “Sort x decreasingly, replace x by -x if x_1 + x_n < 0, and scale so that x_1 = 1. Then x_1 = 1 >= b”. Literally this can fail: take n=14 and x=(1 repeated 13 times,−13). Negating, then scaling the first coordinate to 1, returns the original vector, so b=13. Insert “re-sort after changing sign”, or replace x by (−x_n,…,−x_1).

With that correction, all operations preserve Psi. Under scaling by c≠0, T,P,Q and the pair products scale by c²,c³,c⁴,c², respectively. Permutations and simultaneous sign reversal preserve the defining ratios. A nonzero sum-zero vector has both signs, so its sorted largest coordinate is strictly positive and its smallest is strictly negative. Thus scaling is legitimate, x_1 cannot be zero, and 0<b≤1.

In (I), x_2<0 would force x_2+x_(n−1)<0, so eps=x_2≥0. The case condition gives x_(n−1)≥−eps; sorting puts every middle coordinate in [−eps,eps]. The pair (1,2) gives M=eps≤mT. In (II), x_(n−1)>0 would contradict the case condition, so eps=−x_(n−1)≥0. Now x_2≤eps, and sorting again gives the entire middle interval. The last pair gives M=b eps≤mT.

In both cases, Y2≤(n−2)eps² and delta=1−b=−sum middle belongs to [0,(n−2)eps]. On x_2+x_(n−1)=0 the two eps values coincide. The two choices of M can differ: eps≥b eps, and both are valid lower bounds. There is no inconsistency.

Command: `nice -n 15 /Library/Frameworks/Python.framework/Versions/3.13/bin/python3 audit.py 2`.

Step 2 (I). Let F(e)=(n−2)e²−n(n−1)e+2. Direct substitution gives

$$
F(e_1)=-\frac1{10}+\frac{441(n-2)}{100n^2(n-1)^2}<0,
\qquad F(1)=-n(n-2)<0.
$$

The first inequality holds already for n≥5: (n−2)/(n²(n−1)²) decreases for n≥3, and its correction at n=5 is 1323/40000<1/10. Convexity gives F≤0 throughout [e1,1]. Here eps=x_2≤x_1=1, so eps cannot exceed 1. The use of T≤2+(n−2)eps² and M=eps has the right direction.

Step 2 (II). Sorting gives b≥eps, and the sum gives b≥1−(n−2)eps. For every eps≥0,

$$
\frac{d}{db}\frac{b\,\mathrm{eps}}{1+b^2+(n-2)\mathrm{eps}^2}
=\frac{\mathrm{eps}\,[1+(n-2)\mathrm{eps}^2-b^2]}
{[1+b^2+(n-2)\mathrm{eps}^2]^2}\ge0\quad(0\le b\le1).
$$

Thus the claimed monotonicity holds for every occurring eps, indeed for every nonnegative eps. If eps≥1/(n−1), substituting b=eps works exactly when (n−1)²eps²≥1. If eps≤1/(n−1), the lower value 1−(n−2)eps is positive. Clearing its positive denominator gives

$$
-(n-2)(n^2-1)\left(\mathrm{eps}-\frac{2}{(n-2)(n+1)}\right)
\left(\mathrm{eps}-\frac1{n-1}\right)\ge0.
$$

These are precisely the two stated roots. The lower root is smaller for n≥5. Also e2≤e1 is equivalent to (n−7)(n+6)≥0.

The complete ranges are [0,e1] for Step 3 and [e1,1] for Step 2 in (I); in (II) they are [0,e2], [e2,1/(n−1)], and [1/(n−1),1]. In particular eps between e2 and e1 is covered in (II), as is every eps>1/(n−1). The endpoints deliberately overlap; the ranges are not disjoint if “exactly” is read as requiring disjointness.

Command for both cases, including exact substitutions for n=5,…,5000: `nice -n 15 /Library/Frameworks/Python.framework/Versions/3.13/bin/python3 audit.py 3`.

Step 3. The following checks are independent of the numerical search.

* M≥kappa eps follows from M=eps in (I), and from b≥1−(n−2)e2=(n−1)/(n+1) in (II). Writing kappa≤M/eps requires eps>0. When eps=0, every middle coordinate is zero and b=1, so Psi=0 directly.
* With eps≤e1, Y2≤(n−2)e1²≤1/500 and 1≤T≤1001/500. The function (n−2)/(n²(n−1)²) decreases for n≥3: its derivative has the sign of −3n²+9n−4.
* Expanding directly gives 2Q−T²=(1−b²)²+2Y4−2(1+b²)Y2−Y2²≥−4Y2−Y2². Here b≤1 and Y4≥0 are used.
* Since 1−b³=(1−b)(1+b+b²), it lies in [0,3delta]⊂[0,3(n−2)eps]. Also |Y3|≤sum over the middle coordinates of |x_i|³≤eps Y2 and Q=1+b⁴+Y4≥1.
* The coefficient (n−4)T is positive, so the first term uses a lower bound on 2Q−T². The coefficient −2(n−3) is negative, so its lower bound uses the upper bound P²≤(3(n−2)eps+eps Y2)². In the last term, both M and its coefficient are nonnegative. Replacing Q by 1 lowers it, and then replacing M by kappa eps lowers it again. These substitutions produce exactly the displayed lower bound for G_M.

For the three comparisons, set

$$
D=\frac{(n-1)^2(n^2-6n+6)}{n+1},\quad
L_1=4.002(n-4)(n-2)e_1,\quad
L_2=2(n-3)(3(n-2)+0.002)^2e_1,\quad H=37.9(n-2).
$$

The checks are L1<D/100, L2≤H and 0.99D≥H. All decimal constants here are exact rationals. At n=14:

| Quantity | Exact value | Decimal |
|---|---:|---:|
| e1 | 3/260 | 0.0115384615384615 |
| e2 | 1/90 | 0.0111111111111111 |
| (n−2)e1² | 27/16900 | 0.00159763313609467 |
| L1 | 18009/3250 | 5.54123076923077 |
| D/100 | 9971/750 | 13.2946666666667 |
| L2 | 10693188033/32500000 | 329.021170246154 |
| H | 2274/5 | 454.8 |
| 0.99D | 329043/250 | 1316.172 |

The manuscript’s “1316 against 455” is rounding of 1316.172 against 454.8. Every comparison, and the Y2 bound, was checked with rational arithmetic for every integer n=14,…,5000. All 4,987 rows are saved in [exact_comparisons.json](exact_comparisons.json).

Here are proofs for all larger n as well, filling the line “and the ratio grows with n”:

$$
L_1<4.002\cdot2.1=\frac{42021}{5000}
<\frac{D(14)}{100}=\frac{9971}{750}\le\frac{D(n)}{100}.
$$

The last inequality holds because (n−1)²/(n+1) and n²−6n+6 are positive increasing functions for n≥5. For the second comparison,

$$
\frac{L_2}{n-2}
=\frac{189}{5}\frac{(n-3)(n-2)}{n(n-1)}
\left(1+\frac1{1500(n-2)}\right)^2
<\frac{189}{5}\left(\frac{18001}{18000}\right)^2<\frac{379}{10}
\quad(n\ge14).
$$

Finally, polynomial division and differentiation give

$$
\frac D{n-2}=n^2-7n+14+\frac{-18n+34}{n^2-n-2},
$$
$$
\left(\frac D{n-2}\right)'
=2n-7+\frac{18n^2-68n+70}{(n^2-n-2)^2}>0\quad(n\ge4).
$$

The numerator quadratic has negative discriminant −416 and positive leading coefficient. This proves the required monotonicity, so the n=14 comparison holds thereafter.

To finish the sign argument explicitly, the first negative term costs at most (D/100)T eps≤(D/100)T²eps. The second costs at most H eps≤0.99D T²eps. The remaining positive term is 2n(n−1)kappa eps. Thus G_M>0 when eps>0 in Step 3. At eps=0 the direct equality check applies; the manuscript’s strict “less than” comparison cannot literally hold as 0<0.

Command for all these exact numbers: `nice -n 15 /Library/Frameworks/Python.framework/Versions/3.13/bin/python3 audit.py 4`.

Boundary checks. These tests use n=14 exactly, without replacing the thresholds by rounded decimals. Here e1=3/260 and e2=1/90. Put 0^r for r repeated zero entries and use the same convention for other repeated entries.

| Vector | Boundary checked | Exact Psi | Decimal |
|---|---|---:|---:|
| (1,0^12,−1) | eps=0; b=1 | 0 | 0 |
| (1,e1,0^10,−e1,−1) | eps=e1 in I; b=1 | 3058171533064440/309039175947529 | 9.89574064093 |
| (1,e2,0^10,−e2,−1) | eps=e2; b=1 | 5066210201220/531637854301 | 9.52943843301 |
| (1,(−e1)^12,−(1−12e1)) | eps=e1 in II | 2866787329923/302919972238 | 9.46384389495 |
| (1,(−e2)^12,−13/15) | eps=e2 in II | 260876/28561 | 9.13399390778 |
| (1,(−1/13)^13) | b=eps=1/13; one positive | 0 | 0 |
| (1,0^11,−1/2,−1/2) | b=eps=1/2 in II | 847/3 | 282.333333333 |
| (1,1,(−1/6)^12) | many equal coordinates | 4235/6 | 705.833333333 |
| 1^7,(−1)^7 | many equal coordinates; b=1 | 720/7 | 102.857142857 |
| (1,−1/2,(−1/24)^12) | one positive; unequal negatives | 32741269/1361886 | 24.041123119 |
| (1,1/20,(−1/20)^11,−1/2) | both cases apply; b<1 | 1075511085/16777216 | 64.1054561734 |

All these exact values agree for x and −x, and for a scaled permutation. The b=eps example (1,0^11,−1/2,−1/2) is in case (II), with eps=b=1/2>1/(n−1). The overlap example uses the same eps in both cases but different valid M values. These finite tests supplement the analytic boundary arguments; they are not being used as a proof over a continuum.

Command: `nice -n 15 /Library/Frameworks/Python.framework/Versions/3.13/bin/python3 audit.py 5`. Full vectors and exact values: [boundaries.json](boundaries.json).

Independent numerical search. This used the defining moment expression for Psi, not the Step 1 identity. Every nondecreasing positive integer partition of n into two, three and four blocks was enumerated. Arbitrary real assignments to these blocks cover every ordering of block values. No integer block sizes were sampled or rounded.

Two blocks have no remaining continuous freedom after centering and scaling. For three blocks, a 64-point circle grid was used; for four blocks, a 102-point sphere grid. Every three- or four-block partition received continuous tangent pattern refinement from its three best grid starts, with up to 90 iterations. Up to six worst candidates in each batch also received SLSQP epigraph optimization with every eligible pair-product constraint. Block values may coalesce at an optimum. The count was 142,524 partitions in 649 batches, including all 119,239 four-block partitions at n=257.

There were also 770 full-vector samples per n: Gaussian, heavy-tail, sparse and one-positive vectors, plus dense and sparse perturbations of both equality families at scales 1, 10^−1, 10^−2, 10^−3, 10^−4, 10^−6 and 10^−8. Eighteen of the worst and more diverse candidates per n were refined with an analytic-gradient L-BFGS-B optimizer. In total this was 30,030 samples and 702 full-vector local starts.

The smallest *confirmed* value found is exactly 0 for each tested n, attained at

$$ A_n=(1,0^{n-2},-1). $$

This specifies a vector for every row below. The second equality family also gives exact zero. “Raw” is the smallest floating reading, retained without clipping. “Exact recheck” is the decimal rendering of the exact rational value at the saved worst-float vector, after treating its binary coordinates as exact rationals and subtracting their exact mean. Full fractions and every coordinate are in [search_summary.json](search_summary.json).

| n | Confirmed minimum found | Raw floating Psi | Exact recheck at raw vector | Block partitions: 2 / 3 / 4 |
|---:|---:|---:|---:|---|
| 5 | 0 at A_5 | -2.44249065418e-15 | 0 | 2 / 2 / 1 |
| 6 | 0 at A_6 | -2.22044604925e-15 | 0 | 3 / 3 / 2 |
| 7 | 0 at A_7 | -2.22044604925e-15 | 0 | 3 / 4 / 3 |
| 8 | 0 at A_8 | -8.881784197e-16 | 0 | 4 / 5 / 5 |
| 9 | 0 at A_9 | -9.7699626167e-15 | 0 | 4 / 7 / 6 |
| 10 | 0 at A_10 | 0 | 0 | 5 / 8 / 9 |
| 11 | 0 at A_11 | -6.2172489379e-15 | 0 | 5 / 10 / 11 |
| 12 | 0 at A_12 | 0 | 0 | 6 / 12 / 15 |
| 13 | 0 at A_13 | -5.3290705182e-15 | 0 | 6 / 14 / 18 |
| 14 | 0 at A_14 | 2.22044604925e-15 | 0 | 7 / 16 / 23 |
| 15 | 0 at A_15 | -1.24344978758e-14 | 0 | 7 / 19 / 27 |
| 16 | 0 at A_16 | 2.6645352591e-15 | 0 | 8 / 21 / 34 |
| 17 | 0 at A_17 | -1.24344978758e-14 | 0 | 8 / 24 / 39 |
| 18 | 0 at A_18 | 1.7763568394e-15 | 8.66887639452e-15 | 9 / 27 / 47 |
| 19 | 0 at A_19 | -2.84217094304e-14 | 1.72364243126e-15 | 9 / 30 / 54 |
| 20 | 0 at A_20 | -2.48689957516e-14 | 0 | 10 / 33 / 64 |
| 21 | 0 at A_21 | -2.84217094304e-14 | 8.75414031754e-15 | 10 / 37 / 72 |
| 22 | 0 at A_22 | -2.13162820728e-14 | 1.02812573256e-15 | 11 / 40 / 84 |
| 23 | 0 at A_23 | -6.03961325396e-14 | 0 | 11 / 44 / 94 |
| 24 | 0 at A_24 | -3.19744231092e-14 | 5.69516198274e-15 | 12 / 48 / 108 |
| 25 | 0 at A_25 | -4.61852778244e-14 | 7.16696268217e-15 | 12 / 52 / 120 |
| 26 | 0 at A_26 | -2.84217094304e-14 | 3.12489897459e-15 | 13 / 56 / 136 |
| 27 | 0 at A_27 | -3.5527136788e-14 | 8.48529022654e-15 | 13 / 61 / 150 |
| 28 | 0 at A_28 | -2.48689957516e-14 | 8.84586519772e-15 | 14 / 65 / 169 |
| 29 | 0 at A_29 | -3.90798504668e-14 | 0 | 14 / 70 / 185 |
| 30 | 0 at A_30 | -7.46069872548e-14 | 2.35497143045e-14 | 15 / 75 / 206 |
| 31 | 0 at A_31 | -2.13162820728e-14 | 0 | 15 / 80 / 225 |
| 32 | 0 at A_32 | -7.46069872548e-14 | 2.37423221922e-15 | 16 / 85 / 249 |
| 33 | 0 at A_33 | -4.97379915032e-14 | 6.75801479226e-15 | 16 / 91 / 270 |
| 34 | 0 at A_34 | -7.1054273576e-14 | 1.94786249402e-14 | 17 / 96 / 297 |
| 35 | 0 at A_35 | -1.27897692437e-13 | 0 | 17 / 102 / 321 |
| 36 | 0 at A_36 | -7.81597009336e-14 | 1.89501029629e-14 | 18 / 108 / 351 |
| 37 | 0 at A_37 | -3.5527136788e-14 | 2.55786137903e-15 | 18 / 114 / 378 |
| 38 | 0 at A_38 | -9.23705556488e-14 | 7.18408164302e-15 | 19 / 120 / 411 |
| 39 | 0 at A_39 | -5.68434188608e-14 | 0 | 19 / 127 / 441 |
| 40 | 0 at A_40 | -5.68434188608e-14 | 7.6002855191e-15 | 20 / 133 / 478 |
| 64 | 0 at A_64 | -2.62900812231e-13 | 3.52671382695e-14 | 32 / 341 / 1906 |
| 100 | 0 at A_100 | -5.40012479178e-13 | 0 | 50 / 833 / 7153 |
| 257 | 0 at A_257 | -2.18847162614e-12 | 7.91558964468e-14 | 128 / 5504 / 119239 |

No reading was below −10^−9. The most negative floating reading, −2.1884716261411086×10^−12 at n=257, becomes a positive 7.915589644681867×10^−14 in exact arithmetic at its represented vector. Every reported worst-float vector was checked in exact rational arithmetic using all coordinate pairs, and every one is nonnegative. The initial 80-digit mpmath checks also agree, apart from numerical residues around 10^−78 at exact zeros.

For n=5,…,13, no negative value was found. The repaired proof below certifies nonnegativity for n=10,…,13. For n=5,…,9, this search does not establish that negatives cannot exist.

This is exhaustive over integer block sizes, with numerical continuous optimization of block values. It is **not** a certified global continuous optimization for n=5,…,9. If “optimised exactly over values” requires that stronger certificate, that part was not obtained. For n≥10 the analytic proof supplies the global minimum 0 independently of optimizer convergence.

Commands:

```sh
nice -n 15 /Library/Frameworks/Python.framework/Versions/3.13/bin/python3 search.py random --budget 180
nice -n 15 /Library/Frameworks/Python.framework/Versions/3.13/bin/python3 search.py blocks --budget 160
nice -n 15 /Library/Frameworks/Python.framework/Versions/3.13/bin/python3 search.py summary
nice -n 15 /Library/Frameworks/Python.framework/Versions/3.13/bin/python3 verify_search.py
```

The partition enumeration was independently checked by the recurrence p(n,k)=p(n−1,k−1)+p(n−k,k), with uniqueness and validity of every saved partition. A second evaluator retained the actual T rather than assuming T=1 and checked every stored candidate. The full-vector gradient was checked by central differences at n=5,14,40,257; relative discrepancies were below 1.8×10^−9. Post-SLSQP vectors need not have unit T to machine precision, but the saved objective uses their actual T; homogeneity makes this harmless. Verification details: [search_validation.json](search_validation.json). Optimized values for every block partition are saved in [block_batches](block_batches/); the random/local results and seeds are in [random_progress.json](random_progress.json).

Remark 1. The line is “Equality in the theorem: the vector (1, 0, ..., 0, -1) (eps = 0) and, in Step 2 (II), the vector (1, -1/(n-1), ..., -1/(n-1)) (eps = b = 1/(n-1)).” What is missing is a proof that these exhaust the zeros. We showed Step 3 is strictly positive whenever eps>0, and eps=0 gives the first family. Any other equality must occur in Step 1. Both nonnegative summands there must vanish, so q−p²=1/n and m=1/[n(n−1)].

Equality in the Gram determinant makes (x_i²) a linear combination of 1 and x, because 1 and x are independent. Thus x_i²=alpha+beta x_i for all i, so there are exactly two distinct coordinate values, a>0 and −b<0. If both multiplicities are at least two, both a² and b² are eligible pair products, so m≥1/n>1/[n(n−1)]. One multiplicity must therefore be one. The sum-zero condition gives, up to scaling, permutation and sign, (1,−1/(n−1),…,−1/(n−1)). Conversely its Gram term vanishes and its m is exactly 1/[n(n−1)]. These two families are the only zeros for every n≥14.

Remark 2. The line “the same computation goes through from n = 10” is false if it means the printed constants. Step 2 itself works for all four parameters: the thresholds are as follows.

| n | e1 | e2 | (n−2)e1² | Is this ≤0.002? |
|---:|---:|---:|---:|---|
| 10 | 7/300 | 1/44 | 49/11250 | no |
| 11 | 21/1100 | 1/54 | 3969/1210000 | no |
| 12 | 7/440 | 1/65 | 49/19360 | no |
| 13 | 7/520 | 1/77 | 539/270400 | yes |

Using the printed constants, the remaining exact comparisons are:

| n | L1 versus D/100 | L2 versus H | 0.99D versus H | Entire printed argument closes? |
|---:|---|---|---|---|
| 10 | 14007/3125 > 1863/550 | 7057176049/37500000 ≤ 1516/5 | 16767/50 ≥ 1516/5 | no |
| 11 | 2647323/550000 < 61/12 | 3827817021/17187500 ≤ 3411/10 | 2013/4 ≥ 3411/10 | no |
| 12 | 14007/2750 < 363/50 | 14176890063/55000000 ≤ 379 | 35937/50 ≥ 379 | no |
| 13 | 1386693/260000 < 1746/175 | 1905981007/6500000 ≤ 4169/10 | 172854/175 ≥ 4169/10 | yes |

For a feasible counterexample to the bound, at n=10 take x=(1,(7/300)^4,(−7/300)^4,−1). It is normalized, sum zero, and in case (I) with eps=e1, but Y2=49/11250>1/500. This is a counterexample to a printed bound, not to the theorem. Analogous middle entries ±e1 realize the failures at n=11 and n=12 (take b=1−e1 when the number of middle entries is odd).

The remark's intended extension is true after changing the constants. Use Y2≤0.005, T≤2.005, first-term coefficient 4.005, a 2% first-term allowance, and 0.005 in the P² estimate. Let L1′ and L2′ be L1 and L2 with those replacements. The exact checks are:

| n | L1′ < D/50 | L2′ ≤ H | 0.98D ≥ H |
|---:|---|---|---|
| 10 | 5607/1250 < 1863/275 | 1129430449/6000000 ≤ 1516/5 | 91287/275 ≥ 1516/5 |
| 11 | 1059723/220000 < 61/6 | 55689711/250000 ≤ 3411/10 | 2989/6 ≥ 3411/10 |
| 12 | 5607/1100 < 363/25 | 2268756063/8800000 ≤ 379 | 17787/25 ≥ 379 |
| 13 | 555093/104000 < 3492/175 | 305012407/1040000 ≤ 4169/10 | 24444/25 ≥ 4169/10 |

These changes work uniformly for n≥10. The maximum Y2 bound decreases, starting at 49/11250<1/200. For n≥11, L1′<4.005·2.1=8.4105<D(11)/50=61/6; n=10 is covered by its exact row. Also

$$
\frac{L_2'}{n-2}
<\frac{189}{5}\left(1+\frac1{4800}\right)^2<37.9\qquad(n\ge10).
$$

The already proved monotonicity of D/(n−2) extends the last comparison from n=10 to all larger n. The same sign argument then finishes the proof. Thus the theorem admits the stronger threshold n≥10, but the manuscript needs those explicit constant changes to justify that remark.

Command: `nice -n 15 /Library/Frameworks/Python.framework/Versions/3.13/bin/python3 audit.py 7`. The printed constants are recorded in [remark2_constants.json](remark2_constants.json), and the repaired ones in [remark2_repaired.json](remark2_repaired.json).

Remark 3. For a sorted vector, every product of two positive coordinates is at most x_1x_2, and every product of two negative coordinates is at most x_(n−1)x_n. Mixed-sign products are nonpositive. At least one of the two extreme products is nonnegative when n≥3. Zero coordinates, including the two-nonzero-coordinate case, cause no exception. Hence mT=max(x_1x_2,x_(n−1)x_n).

What remains unchecked: certified global numerical minimization over the continuous three- and four-block values at n=5,…,9, and a proof or disproof of the full inequality in that smaller range. Nothing in that limitation affects the n≥14 theorem, for which the analytic argument is complete after the stated repairs.

All scripts and generated files stayed in this folder. There was no browsing, no push, no visible window, no other agent and no concurrent numerical worker. The numerical library thread counts were set to one. The longest computation lasted 127.62 seconds; peak measured resident memory was about 130 MB. Every computation was launched with `nice -n 15`; this sandbox denied the priority adjustment and the observed inherited niceness was 10. That execution limitation is recorded rather than claiming the adjustment succeeded.

Task: “You are refereeing a short mathematical note” — ALLN_PROOF.md; 11 November 2026, 10:19 (+04:00, Asia/Tbilisi).
