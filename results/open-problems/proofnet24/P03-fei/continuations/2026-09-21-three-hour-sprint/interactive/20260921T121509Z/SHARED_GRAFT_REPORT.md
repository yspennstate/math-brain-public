# FEI sprint result 2: a shared-core graft improves the reproduced lower bound

21 September 2026. Status: explicit balanced Boolean construction with a complete structural proof and exact-rational numerical certificate. Full FEI remains OPEN. WITHOUT_VERIFIED_BRAIN. This result improves the independently reproduced Numaro July 2026 baseline; no publication-priority or global-current-record claim is made. No public submission is authorized or performed.

## Result

Let C_FEI be the supremum of H(f)/I(f) over nonconstant uniform-cube Boolean functions. The construction below proves

C_FEI > 6.521850083658.

More precisely, a balanced monotone Boolean function F on 162 input bits has

I(F)=68013/32768

and

7.014850042680291613033104756310658624299893163
 <= H(F) <=
7.014850042680291613033104756310658624299893164.

Consequently its balanced-composition amplification gives

6.521850083658612443633672199029299526203969334
 <= H(F)/(I(F)-1) <=
6.521850083658612443633672199029299526203969335.

The independently reproduced external seed gives H(g)/(I(g)-1) in

[6.521845710923046575658143972948578468366662292,
 6.521845710923046575658143972948578468366662293].

Comparing the NEW LOWER endpoint with the OLD UPPER endpoint certifies a strict gain greater than

0.000004372735565867975528226080721057837307041.

The improvement is small but genuine; it is not a renamed certificate for the same example. The 162-bit function itself has a much smaller raw H/I. The displayed FEI lower bound uses the proved balanced-composition amplification, not an erroneous substitution of H/(I-1) for H/I on a single function. At depth 25, the actual finite amplified Boolean function already has H/I > 6.52185000677728131714, strictly above the old limiting baseline. The existence of some finite amplification above the safe headline floor follows equally from convergence to the certified larger limit.

## 1. External starting seed and attribution

Use exactly the 18-bit balanced monotone seed g recovered in REPORT.md, with source-table SHA-256

f8a7bb2c738d86368305111633376b1a3a83d8ee1f1abcc9a37d841b0f9c7839.

It is Numaro's July 22, 2026 construction, developed from Mosaic Intelligence's earlier seed. The source is https://numaro.tech/assets/research/fei/check_c71_n18.py, documented at https://numaro.tech/research/fourier-entropy-influence-2026/ and in https://github.com/teorth/optimizationproblems/pull/130. The starting seed, its old lower bound, and the standard O'Donnell-Tan amplification are not attributed to this sprint.

The nine core input bits have integer index x in {0,...,511}. Define a(x) to be the source value outside the following nine host edges and zero on their endpoints:

j=0: (78,79), pivot bit 0;
j=1: (113,121), pivot bit 3;
j=2: (228,484), pivot bit 8;
j=3: (170,186), pivot bit 4;
j=4: (149,151), pivot bit 1;
j=5: (338,466), pivot bit 7;
j=6: (284,316), pivot bit 5;
j=7: (291,295), pivot bit 2;
j=8: (393,457), pivot bit 6.

The exact source core mask is in external_seed_recovery.json and reconstruct_external_seed.py. Each edge has a weight-four lower endpoint and weight-five upper endpoint. Let P_j be its indicator and Q_j=P_j chi_{pivot_j}, where chi_i=(-1)^{x_i}. The source is

g(x,y)=a(x)+sum_{j=0}^8 P_j(x) chi_{y_j}.

The source's exact entropy is recorded in cancellation_certificate.json, its influence is 261/128, and its nine auxiliary singleton coefficients and influences are all 1/256. The source value convention is true=-1.

## 2. New construction: reuse the core coordinate, do not make it independent

For each host edge j introduce 17 fresh variables z_j, disjoint from all other new variables and the nine outer core inputs. Take a fresh copy of the full source seed g. Feed its zero-based input 9 from the existing outer coordinate x_{pivot_j}; feed its other 17 inputs from z_j. Call this local gadget G_j(x_{pivot_j},z_j). Set

F(x,z_0,...,z_8)=a(x)+sum_{j=0}^8 P_j(x) G_j(x_{pivot_j},z_j).

There are 9+9*17=162 input bits. Since the hosts are pairwise disjoint, F is always +/-1: off all hosts it equals a(x), and on host j it equals G_j. This is NOT ordinary disjoint block composition at the outer core: the distinguished gadget input is deliberately the already-present coordinate of its host edge. Treating it as an extra independent bit loses the gain.

Balance is exact. The fixed core a has mean zero. On each host, its pivot coordinate is uniform on the two endpoints and the fresh gadget inputs are uniform, so the balanced gadget has conditional mean zero. Thus E F=0.

Monotonicity follows from the free-edge property and the source's monotonicity. The checker examines all 9*256=2304 directed core edges. An edge between two hosts is allowed only if both endpoints belong to the same host and it is that host's pivot edge. If a directed edge leaves a host for a fixed cell, the fixed upper value must be -1; if it enters a host from a fixed cell, the lower value must be +1; fixed-to-fixed edges are monotone. These finite conditions hold exactly for the recovered core. On the remaining within-host edge, G_j is monotone in its distinguished input. All fresh-input directions are monotone because g is monotone. Hence F is monotone on the whole 162-cube without enumerating 2^162 points.

## 3. Exact Fourier calculation

Write A(S)=ahat(S), w=1/256, h=H(g), i=I(g), and b=ghat({9})=1/256. The transforms of P_j and Q_j each have 256 nonzero coefficients, all with absolute value w. P_j has Fourier support on subsets not containing pivot_j, while Q_j has support on those containing it. Their supports are disjoint.

The coefficient with no fresh gadget coordinates is

Fhat(S,empty)=A(S)+b sum_j Qhat_j(S).                         (3.1)

For a nonempty fresh subset T in block j, the coefficient over core S is

Phat_j(S) ghat(T) + Qhat_j(S) ghat(T union {9}),               (3.2)

with T identified with the 17 nondistinguished gadget inputs. Because the two core supports are disjoint, these terms never interfere. There are no coefficients involving fresh inputs from two different blocks, since F is a sum of localized single-gadget terms.

Thus every nonzero gadget coefficient other than the empty coefficient and its distinguished singleton is replicated 256 times, scaled by w. Its total entropy contribution is w times its original entropy plus 16w times its mass. Define

H_core(b)=sum_S phi((A(S)+b sum_j Qhat_j(S))^2),
phi(t)=-t log2 t.

Then exactly

H(F)=H_core(b)+9w [h-phi(b^2)+16(1-b^2)].                    (3.3)

There is no approximation or assumption about independent core and gadget coordinates in this formula.

Influence can be calculated in two different exact ways. Since F is monotone, sum its singleton coefficients. The fixed core contributes 513/256; a host's distinguished core coefficient contributes wb and its fresh coordinates contribute w(i-b). Hence

I(F)=513/256+9wi=68013/32768.                                (3.4)

Independently, summing degree times squared coefficients from (3.1)-(3.2) gives the same rational value. A tail coefficient corresponding to an original gadget support U has mean total degree |U|+4 across its 256 core replicas. The core weighted contribution and all tails are accumulated as exact fractions in the checker. Parseval is also verified as an exact integer identity.

## 4. Why this improves the seed

For comparison, the original seed has H(g)=H_core(0)+9*16w. Put

K(b)=H_core(b)-H_core(0)-9w[phi(b^2)+16b^2].

Equations (3.3)-(3.4) become

H(F)=H(g)+9w H(g)+K(b),
I(F)-1=(1+9w)(I(g)-1).

Therefore

H(F)/(I(F)-1) - H(g)/(I(g)-1)
 = K(b)/[(1+9w)(I(g)-1)].                                   (4.1)

At b=1/256 the exact-rational entropy enclosure proves K(b)>0, with the strict ratio gain quoted above. This explains why simply substituting an independent balanced record gadget would not improve the amplified ratio: it corresponds to b=0 and K(0)=0. Sharing the correct existing core coordinate changes the core Fourier masses beneficially.

The earlier majority-of-three shared graft had too much distinguished influence b=1/2 and a worse gadget entropy/influence ratio; all nine such single-host trials failed. The successful gadget is the recovered record seed itself, sharing one of its SMALL-influence auxiliary inputs. Both the failed trials and successful method are retained.

## 5. Numerical certificate, not a 162-bit brute-force claim

The new spectrum is represented by an exact multiplicity histogram containing 6,380,242 nonzero coefficients. Their squared-coefficient denominator can be taken to be 2^54=18014398509481984. The compact histogram has few distinct squared values and is saved as shared_graft_spectrum_histogram.json. Zero coefficients need not be enumerated. Every coefficient and its multiplicity comes from the proved formulas (3.1)-(3.2).

certify_shared_graft.py independently checks the old full truth-table hash, old balance/monotonicity/influence, all free-edge core conditions, the new histogram's exact Parseval sum, and the new spectral influence. It then encloses every needed logarithm with the exact Fraction atanh-series routine from rational_entropy_certificate.py, N=80 terms after dyadic range reduction. Every improvement comparison is between rational endpoints. No floating-point value decides the strict gain.

As a separate finite test of the compression implementation, a single host is grafted with majority-of-three. That 19-bit function is actually expanded to all 524,288 values. Its complete integer Walsh histogram agrees EXACTLY with the compressed histogram after the known denominator rescaling, and both influence calculations give 1045/512. This is a code regression for the formula, not a substitute for the structural proof of the large construction. The finite regression table hash is recorded in shared_graft_certificate.json.

Reproduce with:

python certify_shared_graft.py

Dependencies are the already committed reconstruction, Walsh, and rational-log modules in this directory, plus NumPy. No network, model API, hidden answers or new external execution capability is needed. The 162-variable function is not claimed to have been brute-force enumerated.

## 6. Full-problem implications and assignments

This is a lower-bound improvement. It raises the constant that a universal FEI proof must accommodate; it does NOT prove that a finite universal constant exists, and it does not contradict the restricted read-once upper bound.

Useful next work for the existing sprint workers: B13's composition/numerics lane should generalize (3.3)-(3.4) to heterogeneous gadgets or larger free faces and search for a larger certified positive correction, rather than rerun the old seed. The independent construction lane should try qualitatively different gadgets and certify both influence and Boolean realizability. Universal-proof lanes should retain the new obstruction and seek a dimension-independent upper payment, not another proposed universal constant below the certified lower bound. No worker should be reassigned away from brain or benchmark work by this handoff.

The parameter choices have not been globally optimized. The exact full-FEI upper-bound question remains OPEN.
