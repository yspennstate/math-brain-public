TASK: B12 ACCOUNT: account02 RUN: 2026-09-21T15:57:15.964504Z — FEI approach 1: terminal-to-prefix information loss and hypercontractive Palm-row depth

STATUS: PARTIAL / FULL FEI OPEN. This run proves two universal Boolean structural lemmas for the sequential spectral-sample route and isolates a sharper information-loss quantity. It does not prove a dimension-independent FEI constant.

MODEL: GPT-5.6 Sol
THINKING LEVEL: UNKNOWN; source=not_exposed; requested=maximum actually supported
THINKING USAGE: reasoning tokens NOT_EXPOSED; provider thinking time NOT_EXPOSED; coverage=unavailable
RESEARCH EXECUTION: WITHOUT_VERIFIED_BRAIN. No brain retrieval/context was used or claimed.

## Measurable movement

Before this run, approach 1 had an exact Palm/uniform-thinning representation and a sharp *mean* depth obstruction for rare influences only as the next target. After this run there is a full one-parameter Laplace-transform bound for every derivative Palm row, an explicit all-scale shallow-prefix tail bound, and an exact reduction of the remaining selector difficulty to a single terminal-to-prefix information-loss quantity.

Fleet-rules moves used: #18 (say it in another language: rewrite selector entropy as an information-loss gap), #2 (attack the negation first: the arbitrary singleton-mixture law gives unbounded loss), and #3 (prove something stronger: replace a first-moment depth estimate by a parameterized hypercontractive tail inequality).

## 1. Normalization and Palm experiment

Let f:{-1,1}^n->{-1,1}, p_B=hat f(B)^2, and lambda=I(f)=sum_B |B|p_B>0. Let

  j_i = Inf_i(f) = sum_{B contains i} p_B,   pi_i=j_i/lambda.

Sample the size-biased spectral set B* by

  P(B*=B)=|B|p_B/lambda,

then choose X uniformly from B*. Thus P(X=i)=pi_i and, conditional on X=i,

  P(B*=B | X=i)=p_B/j_i  (i in B).

Finally order B* uniformly at random and let A be the unordered set of coordinates preceding X. Equivalently, with C=B*\{X}, draw U uniform on [0,1] and retain every member of C independently with probability U. All logarithms below are base 2 unless ln is written.

The previous B12 death-chain/Palm work gives

  H_sel(f)/lambda = H(X|A) - (1/lambda) sum_B p_B log(|B|!).      (1)

## 2. New exact reduction: terminal-to-prefix information loss

Because X is uniform in B*,

  H(X|B*) = (1/lambda) sum_B |B|p_B log |B|.

Define

  L_f := H(X|A)-H(X|B*) = I(X;B*)-I(X;A),

and

  G_f := (1/lambda) sum_B p_B [ |B|log|B| - log(|B|!) ].

Then (1) becomes the exact identity

  H_sel(f)/lambda = L_f + G_f.                                  (2)

For every integer k>=1,

  0 <= k log k - log(k!) <= k log e,

so

  0 <= G_f <= log_2 e = 1.4426950408889634... .                  (3)

Thus the full selector obstruction differs from L_f by at most one universal additive constant. In particular, combining (2) with the already established universal hazard payment gives a direct equivalence of finiteness: a universal upper bound L_f<=C_L implies full FEI with a dimension-independent constant, while FEI itself immediately bounds L_f from above. Using the previous B12 sharp-selector amplification C_sel=C_FEI gives the sharper relation

  C_FEI - log_2 e <= C_L <= C_FEI.                               (4)

With the current certified unrestricted lower bound C_FEI>6.521845710923046575 from the recovered TASKS/owner state, (4) forces

  C_L > 5.079150670034083... .                                  (5)

So this is not a cheap constant-1 information lemma: it carries essentially the full FEI difficulty.

Interpretation: L_f is exactly the amount of information about the distinguished spectral coordinate that is present in the terminal set B* but lost when one replaces B* by the random predecessor set A.

## 3. Why Booleanity is indispensable

For an arbitrary subset law, take p supported on singleton sets {i} with any high-entropy distribution pi. Then lambda=1, B*={X}, and A is always empty. Hence

  L = H(X),

which is unbounded with dimension. Therefore no purely set-theoretic inequality can bound L.

The rest of this report gives a Boolean-only mechanism that excludes precisely this low-degree failure mode.

## 4. New Palm-row hypercontractive theorem

Fix i with j_i>0. On the (n-1)-cube define the directional derivative slice

  g_i(x_{-i}) = [ f(x_i=1,x_{-i}) - f(x_i=-1,x_{-i}) ]/2.

Then g_i takes values in {-1,0,1}, ||g_i||_2^2=j_i, and

  hat g_i(C)=hat f(C union {i}).

Consequently, if Z=|B*|-1 conditional on X=i, then

  P(C | X=i)=hat g_i(C)^2/j_i,   Z=|C|.

Apply the standard Bonami-Beckner inequality

  ||T_rho g_i||_2 <= ||g_i||_{1+rho^2},  0<=rho<=1.

Since |g_i| is the indicator of its support,

  ||g_i||_{1+rho^2}^2 = j_i^{2/(1+rho^2)}.

After division by j_i this gives the exact dimension-free Palm-row bound

  E[ rho^{2Z} | X=i ]
    <= j_i^{(1-rho^2)/(1+rho^2)}.                               (6)

This is an analytic theorem, not a finite-pattern conjecture. It is a direct translation of classical hypercontractivity into the derivative Palm row; no novelty claim about Bonami-Beckner itself is made.

Two useful consequences follow.

### 4a. Fixed thinning: rare coordinates cannot remain empty

Let A_u be independent u-thinning of C. Taking rho^2=1-u in (6),

  P(A_u=empty | X=i) <= j_i^{u/(2-u)}.                           (7)

For the actual random prefix A, integrate u from 0 to 1. With a=ln(1/j_i),

  P(A=empty | X=i)
    <= integral_0^1 j_i^{u/(2-u)} du
    = 2 integral_0^1 exp(-a t)/(1+t)^2 dt
    <= min(1, 2/ln(1/j_i)).                                     (8)

At rho=0, (6) also yields the especially transparent terminal statement

  P(Z=0 | X=i) <= j_i.                                          (9)

Thus the arbitrary singleton-mixture obstruction cannot occur in a Boolean Fourier spectrum with many tiny influences.

### 4b. All-scale shallow-prefix tail bound

Write t=rho^2 in (0,1). From (6), for every integer r>=0,

  P(Z<=r | X=i)
    <= t^{-r} j_i^{(1-t)/(1+t)}.                                (10)

Conditional on Z, the actual random-prefix size R=|A| is uniform on {0,...,Z}. Therefore for every integer m>=1,

  P(R<m | X=i)
    <= t^{-r} j_i^{(1-t)/(1+t)} + m/(r+2).                      (11)

A convenient concrete choice is t=1/2 and

  r=floor( (1/4) log_2(1/j_i) ).

If log_2(1/j_i)>=4, this gives

  P(|A|<m | X=i)
    <= j_i^{1/12} + 4m/log_2(1/j_i),                            (12)

with the right side capped at 1. Hence for any m=o(log(1/j_i)), a vanishing-influence coordinate has a shallow prefix with probability tending to zero. This is strictly stronger than a first-moment statement and is the multiscale property the previous run was seeking.

## 5. Sharp mean-depth corollary by Boolean edge isoperimetry

There is also a sharper first-moment constant than differentiation of (6). Let E_i be the support of g_i on the (n-1)-cube and alpha_i=min(j_i,1-j_i). If the support indicator changes across coordinate j, then |D_j g_i|=1/2 at that directed boundary point. Hence

  Inf_j(1_{E_i}) <= 4 ||D_j g_i||_2^2.

Uniform-cube edge isoperimetry gives

  sum_{j != i} Inf_j(1_{E_i}) >= 2 alpha_i log_2(1/alpha_i).

Writing d_i=sum_{j != i} ||D_{ij}f||_2^2, one gets

  d_i >= (alpha_i/2) log_2(1/alpha_i).

But under the Palm row

  E[Z | X=i]=d_i/j_i,
  E[|A| | X=i]=d_i/(2j_i).

Therefore

  E[|A| | X=i]
    >= [alpha_i/(4j_i)] log_2(1/alpha_i).                        (13)

In particular, for j_i<=1/2,

  E[|A| | X=i] >= (1/4) log_2(1/j_i).                           (14)

The constant 1/4 is sharp: for the Boolean function that is +1 at one cube vertex and -1 everywhere else, j_i=2^{1-n} for every i and equality holds in (14): E(|A||X=i)=(n-1)/4.

## 6. A universal KL lower bound, and why it is not enough

Let r_A be the posterior law of X given A. Since X never belongs to A, r_A is supported on A^c. Therefore

  D(r_A || pi)
    = D(r_A || pi(.|A^c)) + log_2[1/(1-pi(A))]
    >= log_2[1/(1-pi(A))].

Averaging,

  I(X;A) >= E_A log_2[1/(1-pi(A))].                              (15)

This cleanly quantifies the information gained merely by eliminating the coordinates already observed in the prefix. It is useful for parity-like spectra, but it is not a full bridge: in uniform-profile clustered examples such as tribes, pi(A) can be tiny even when the identities inside A convey substantial block information. Thus the surviving task is not prefix *depth* alone; it is a row-geometry/reverse-data-processing inequality that combines (6)/(11) with the identities of the retained derivative Fourier coordinates.

## 7. Decisive failed shortcut

A tempting pure information-theoretic statement would be

  I(X;B*) - I(X;A) <= O(1)

for every subset law. The singleton-mixture example in section 3 disproves this with loss H(pi). Thus any proof of a bounded L_f must explicitly use Boolean Fourier structure. Equations (6)-(12) are one such structural input, but they do not by themselves prove bounded L_f because degree/depth does not control the identity information in the derivative rows.

## 8. Executed finite checks

The attached checker exhaustively enumerated every Boolean function for n=1,2,3,4 (65,812 truth tables), checking 261,866 nonzero coordinate rows. It verified:

- the exact selector/loss decomposition numerically on 65,804 nonconstant functions;
- the rho^2=1/2 specialization of (6) in exact rational arithmetic, namely [E(2^{-Z}|X=i)]^3 <= j_i, on all 261,866 rows;
- the sharp mean-depth inequality (14), with observed minimum ratio exactly 1/4 for n=2,3,4;
- 77 exact one-point equalities for dimensions 2 through 12.

The finite maxima of L_f found were 0, 0.25, 0.566427871625756, 0.938492238490708 for n=1,2,3,4. These are finite diagnostics only and are not extrapolated to a universal bound. Checker result digest:

  sha256:8c02f459c3a53060e41f31a92ed7d140ab1e9112c7a357c437bb52b20cf1d691

## 9. Literature check and coordination

A fresh public search found the September 18, 2026 plateaued-function FEI result (Potapov, arXiv:2609.21563), the May 2026 stopping-binary-tree/restriction paper of González-MacManus-Pereyra (arXiv:2606.00246), and the 2025 information-theoretic strengthening of Han's inequality (Li-Han, arXiv:2512.03117). None of those search hits was treated as establishing the Palm-row loss theorem above, and no novelty claim is made from a negative search.

This B12 scope is complementary to B13's restriction/profile toll, B14's erasure/selector work, B15's spectral remainder, B16's signed transport, B17's buried-atom/cancellation mechanisms, and B18's integration work. The next B12 step is specifically a Boolean reverse-data-processing estimate for the derivative rows: lower-bound I(X;A) relative to I(X;B*) using row identity geometry in addition to the new all-scale depth control.

## Ledger

PROVED (from exact algebra + standard named theorems): (2)-(3), Palm-row hypercontractive inequality (6), consequences (7)-(12), sharp mean-depth inequality (13)-(14), exclusion-KL inequality (15).

DISPROVED: any dimension-free terminal-to-prefix information-loss bound for arbitrary subset laws (singleton-mixture counterexample).

FINITE SELF-CHECKED: exhaustive n<=4 diagnostics and one-point equalities n<=12 as listed above.

OPEN: a universal Boolean bound on L_f, therefore full FEI H(f)<=C I(f).
