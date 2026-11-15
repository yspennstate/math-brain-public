Overall verdict: SOUND

The numbered mathematical claims and their proofs are sound under the stated limit formula and the permitted monotonicity theorem. I found no missing load-bearing step and no counterexample. This verdict concerns mathematical validity, not novelty or the accuracy of bibliographic claims that cannot be checked from the supplied source. There are notation-index corrections and one imprecise introductory asymptotic, detailed below. They do not affect the proofs.

I read the new source independently. All line numbers refer to the supplied, unmodified `PAPER.tex`. No author program, external mathematical document, browser, additional agent, or background service was used. All new files are in this directory. The numerical programs ran sequentially, with one computational process, one numerical thread, a 240-second timeout, inherited nice level 15, and measured peak resident memory below 40 MB. I did not modify the shared brain, checklist, or mesh: the specific instruction for this run forbids writes outside this folder.

## Theorem 1.1 — SOUND

Statement: lines 100–106. Proof: lines 269–291.

Extend the summand by zero for i>n. Nonnegativity and pointwise convergence justify Fatou at line 270; no summable majorant is being presumed. The finite limit sum is essential for the subsequent tail argument.

With fixed 0<epsilon<=1/3 and M>=2, the stated threshold n>=max(6,M/epsilon) is sufficient: L=floor(epsilon n)>=M>=2, 2L+2<=n, and n-L-1>=M. Thus every range in the four-way split is defined and there is neither omission nor overlap. On the middle range, n-i>=L+1>epsilon n, exactly the hypothesis of Corollary 2.4(b). On the window, i>=n-L gives the correct inequality f(i)<=K/log(n-L). The starting-state contribution is exactly f(n), not part of V(n,L).

For fixed epsilon, harmonic-number asymptotics give both limits in line 284, including the floor and the minus one. The denominator tends to log((1-epsilon)/epsilon)>=log 2>0. Consequently the window has limiting upper bound K/log((1-epsilon)/epsilon). Take M to infinity with epsilon fixed, using convergence of the limit sum; only then take epsilon to zero. The order of these limits in line 290 is correct. This proves the required upper bound and, with Fatou, convergence.

The preceding necessity observation at lines 92–98 is also valid in the finite-sum setting of Ansatz (i). If convergence held and f(n) did not tend to zero, choose a subsequence on which f(n)>=delta>0 and apply the displayed Fatou argument along that subsequence to the remaining terms. This would force a lower limit at least S+delta, where S is the finite limit sum.

## Theorem 1.2 — SOUND

Statement: lines 108–115. Proof: lines 388–419.

The auxiliary estimate at lines 382–385 is valid for every i>=2. The lower bound follows from h_(i-1)>=log i and 1/(i-1)>=1/i. The upper bound follows from h_(i-1)<=1+log i, i-1>=i/2, and log i>=log 2; the displayed numerical coefficient is less than 3.

Every property of the construction checks out:

1. **Choice of scales.** Since phi is positive and tends to infinity, each tail has a strictly positive infimum. Thus psi is positive, nondecreasing, tends to infinity, and is at most phi. The three lower constraints on N_j can be satisfied inductively, without any regularity or monotonicity assumption on phi.
2. **Windows and zero values.** L_j=floor(N_j/2^j) is a positive integer with L_j<=N_j/2 and N_j-L_j>=ceil(N_j/2). For j>=2 the separation gives N_j/2>=N_(j-1)+1>N_(j-1). Previous starting points lie below B_j, the current N_j lies above it, and all future starting points are larger. Hence the windows are disjoint and no N_k belongs to their union. In particular f(N_k)=0. The reference to N_(j-1) in line 398 is understood for j>=2; the first window needs no previous scale.
3. **Pointwise envelope.** For i in B_j, phi(i)>=psi(i)>=j^2 and log i<=log N_j, so j^2/log N_j<=phi(i)/log i. At every other i the assertion follows from f(i)=0.
4. **Decay and boundedness.** On B_j, f(i)<=1/j. Each fixed block is finite and the blocks escape to infinity, so this proves f(i)->0 as a sequence, not just along selected points. In particular f is bounded (indeed the stated estimates give f<=1).
5. **Finite limit sum.** There are exactly L_j elements in B_j. For each of them, a(i)<=6 log N_j/N_j. Thus the block contribution is at most 6j^2/2^j. This is summable (its sum over j>=1 is 36), so the full limit sum is finite.
6. **Divergence.** The constraints give N_j>=exp(2j+8)>=2^(j+3), hence L_j>=8 and L_j>=N_j/2^(j+1). Therefore lambda_j<= (j+4)log 2 and h_(N_j-1)>=log N_j>=2(j+4)>=2lambda_j. Corollary 3.2 applies, including j=1 when L_j may equal N_j/2. The block alone contributes at least j^2/[10(j+4)log 2], which tends to infinity. Earlier blocks contribute nonnegative terms and cannot spoil the bound.

The resulting counterexample has polynomial growth with k=0 and also defeats the version of the occupation sum omitting its starting-state term.

## Proposition 1.3(a) — SOUND

Statement: lines 128–135. Proof: lines 421–457.

The path has at most n-1 nonzero jumps, whose sum is n-1. Conditional on departure from m>=2 its expected jump is (m-1)/h_(m-1)=g(m). Each such m is visited at most once. Taking expectations therefore yields the first identity, with no stopping-time integrability issue. The second is termwise cancellation a(i)g(i)=6/pi^2, with exactly n-1 terms.

The restricted estimate at lines 428–432 also holds pathwise before taking expectations: once the chain enters {1,...,r}, the jumps originating at states <=r telescope from its entry state to 1. Their sum is at most r-1; if it skips the set except for 1 the sum is zero. The jump *into* the set from a larger state is correctly excluded.

For the linear asymptotic, multiplying by h_(i-1)<=h_(n-1) gives the upper bound. Restricting to i>=r+1 gives h_(i-1)>=h_r and drift mass at least (n-1)-(r-1)=n-r. For r=ceil(n/log n), eventually 2<=r<n, r=o(n), and h_r/log n->1. The two bounds thus both have leading term n log n. Since h_k<=k, g>=1 and the difference between weights i and i-1 contributes at most n-1=o(n log n).

For completeness, the small remainder implicit in lines 445–448 is controlled by

    sum_{k=1}^{n-1} h_k/k = (h_(n-1)^2 + sum_{k=1}^{n-1} 1/k^2)/2 = O(log^2 n).

Together with sum_{i=2}^n h_(i-1)=n h_(n-1)-(n-1), this gives the stated limit asymptotic. This is elementary completion of the displayed calculation, not a missing assumption. Finally the eta bound at lines 450–456 treats the finitely many small indices by a uniform constant, uses a(n,i)<=1 and a(i)<=1 correctly, and finishes by letting eta decrease to zero.

## Proposition 1.3(b) — SOUND

Statement: lines 136–139. Proof: lines 459–476.

For j>=5, N_j=2^(j^2), L_j=floor(N_j/j^2) satisfies N_j/(2j^2)<=L_j<=N_j/j^2 and 8<=L_j<=N_j/2. The separation N_j/2>N_(j-1) holds because j^2-1>(j-1)^2. Thus the union defines a {0,1}-valued weight unambiguously; no future block intersects {2,...,N_j}.

On B_j, i lies between N_j/2 and N_j. The function log x/x decreases throughout that interval. Its value at N_j gives the lower bound (6/pi^2)j^2 log 2/N_j. For the upper bound it is enough to use log i<=log N_j and 1/i<=2/N_j in a(i)<=3log i/i. Multiplication by the lower and upper estimates for L_j gives exactly 3log 2/pi^2 and 6log 2. Hence every block supplies a fixed positive amount to the limit sum, making it infinite; through block j the partial limit sum is at most 6j log 2 (there are actually j-4 blocks).

The lower-bound corollary's remaining condition holds already at j=5: 25log 2>2log 400. The difference j^2log 2-2log(16j^2) is increasing for real j>=5, so it holds for every later j. The floor estimate gives lambda_j<=log(16j^2). Consequently the occupation sum at N_j is at least j^2log 2/[10log(16j^2)]. Division by the upper bound for its positive denominator gives j/[60log(16j^2)]->infinity. This proves the asserted infinite limsup. Denominators are positive for every sufficiently large n.

## Remark 1.4 — SOUND

Lines 146–153. Non-increasingness gives f(i)sum_{k=2}^i a(k)<=sum_{k>=2}a(k)f(k). The elementary lower bound a(k)>=6/[pi^2(k-1)] and h_(i-1)>=log i give the first inequality. Thus f(i)<=K/log i with K=(pi^2/6) times the finite limit sum, and Theorem 1.1 applies.

## Lemma 2.1 — SOUND

Lines 190–209. All parameters are integers as in the preceding definition of W. For n-L<=m<=n, the event that the next state belongs to W(n,L) is exactly 1<=d<=m-n+L. At m=n-L this is empty, and h_0=0 handles it correctly. The numerator is at most h_L, the denominator at least h_(n-L-1), and n>=2L+2 makes n-L-1>=L+1, so rho<1 and the displayed denominator is strictly positive even at the endpoint n=2L+2.

Once the chain exits W union {n}, strict decrease prevents re-entry. At least k window visits is therefore exactly the event that all of X_1,...,X_k are in W. Applying the conditional bound successively by the Markov property gives probability at most rho^k. Summing the tail probabilities from k=1 gives rho/(1-rho), not 1/(1-rho); this correctly excludes the starting state.

## Lemma 2.2 — SOUND

Lines 213–231. In the first-step equation, jumps d>s land below i and contribute zero. For 1<=d<=s the new state is at least i. The denominator h_(i+s-1)>=h_i has the correct direction. Reindexing by r=s-d gives exactly 0<=r<=t-1 and 1<=d<=t-r. All terms are nonnegative, so replacing h_(t-r) by h_t and extending the remaining sum to S_t is valid. Rearrangement is permitted because t<i implies h_t<h_i. When t=0, S_0=a(i,i)=1 and the bound is an equality; the intermediate sums are empty.

## Lemma 2.3 — SOUND

Lines 233–243. For every m=i,...,i+t, n>=i+t and the permitted monotonicity theorem imply a(n,i)<=a(m,i). Averaging over all t+1 values and then over the t values excluding m=i gives the two inequalities used in the proof. For the second bound, S_t-1<=h_t/(h_i-h_t), obtained by subtracting one from Lemma 2.2. The exclusion t=0 from this second bound is necessary and present. There is no use of monotonicity in i, no rate assumption, and no uniform convergence assumption.

## Corollary 2.4 — SOUND

Lines 245–267. For 1<=t<=i/2,

    h_i-h_t = sum_{k=t+1}^i 1/k >= (i-t)/i >= 1/2.

For t=0 the same lower bound follows directly from h_i>=1; equation (2.2)'s displayed range r>=1 need not be extended to r=0. Thus the half-range estimate is valid at every stated endpoint.

For (a), t=floor(i/2)<i and t+1>i/2. Also h_i=h_(i-1)+1/i<=h_(i-1)(1+1/i), and the last algebraic comparison is exactly 4(i^2-1)<=6i^2. This includes i=2.

For (b), the first case follows from pi^2<=pi^2/(2epsilon). In the other case t=n-i is a positive integer less than floor(i/2), hence less than i/2, and t+1>epsilon n>=epsilon i. The resulting bound 2h_i/(epsilon i) is exactly 1/(2epsilon) times the bound 4h_i/i already compared with pi^2a(i). All constants and inequality directions are correct.

## Remark 2.5 — SOUND

Lines 293–303. Monotonicity together with the limit formula gives a(n,i)>=a(i) for every n>=i, establishing the lower ratio bound termwise. Eventually the denominator is positive and tends to infinity. With epsilon=1/3 and M=2, the proof of Theorem 1.1 bounds the part outside the window by (3pi^2/2) times the corresponding partial limit sum. The window has bounded contribution and f(n) tends to zero. Dividing by the divergent denominator removes that bounded remainder. Finiteness of the full limit sum was used only in the later M-limit of the theorem proof, so it is not incorrectly reused here.

## Remark 2.6 — SOUND as a mathematical comparison

Lines 305–310. For fixed theta<1 with a nonempty integer range 1<=t<=i^theta, h_t/h_i is bounded away from 1 as i grows; for 0<=theta<1 its upper limit is at most theta. Thus the lemma's bound is indeed of order h_t/(t h_i), with constants allowed to depend on theta. For theta<0 the stated range is eventually empty.

I did not inspect BCM Theorem 1.1(iii), so I cannot certify its citation or exact formulation. Its quoted upper bound can nevertheless be checked independently here. Expand the first-step recursion into compositions of t. Every departure denominator is at least h_i. If C_k(t) is the sum of 1/(d_1...d_k) over positive d_1+...+d_k=t, symmetry gives

    t C_k(t) = k sum_{d_1+...+d_(k-1)<=t-1} 1/(d_1...d_(k-1))
               <= k h_(t-1)^(k-1).

The k=1 case is interpreted directly. For 1<=t<i this yields

    a(i+t,i) <= [1/(t h_i)] [1-h_(t-1)/h_i]^(-2).

This proves the quoted order C_theta/(t h_i) in the stated subpower range without any extra outside theorem. The factor h_t comparison is correct (it is bounded when t stays bounded). The main proofs do not use this remark.

## Lemma 3.1 — SOUND

Lines 316–344. For any current state m<=n, the conditional probability of a jump of size at most y is at least q. The cases y>m-1 and m=1 are explicitly handled by probability one. Iterating conditional probabilities, without assuming independence, gives P(E)>=q^T.

For states m>=n-L>=2 the truncated expected jump is exactly min(y,m-1)/h_(m-1), at most y/h_(n-L-1). Thus the unconditional expectation of Z has the stated bound. If E occurs and the chain has gone below n-L by time T, all jumps up through its first crossing are included in Z, including the crossing jump. Their sum exceeds L. Markov's inequality with threshold L is valid; replacing the strict threshold by a weak upper probability bound only weakens it.

On E intersect {X_T>=n-L}, the chain has never reached 1. All of X_1,...,X_T are therefore distinct states of the window, and there are T visits. No conditioning of the expectation of Z on E is made or needed. There is no unstated constraint Ty<=L or T<=L. For large T the lower bound can be negative; this is harmless and is included in the exact grid checks.

## Corollary 3.2 — SOUND

Lines 346–378. Under its hypotheses n>=16, so Lemma 3.1 applies. The choices T=floor(H/lambda)>=2 and y=ceil(L/8) satisfy its integer constraints. The useful floor inequality floor(x)>=2x/3 for x>=2 is valid on every interval [k,k+1), k>=2; it is not the generally false bound floor(x)>=x-1 rounded in the wrong direction.

Since y>=L/8, equation (2.2) gives H-h_y<=log((n-1)/y)<=lambda. Put x=lambda/H<=1/2. The function (1-x)^(1/x) decreases on (0,1); its logarithmic derivative has numerator -x/(1-x)-log(1-x)<0. As T<=1/x and 0<1-x<1, raising this base to T gives a value at least its 1/x power. Hence q^T>=1/4.

The ceiling bound y/L<=2/9 is valid: it is 1/8 at L=8, and for L>=9 it follows from (L+7)/8<=2L/9. The L terms in H-h_(n-L-1) are each at most 1/(n-L), so this difference is at most L/(n-L)<=1. The bound H>=2log 16>5.5 consequently gives H/h_(n-L-1)<=H/(H-1)<=5.5/4.5<1.23. The remaining constants are independently evaluated below:

    2*1.23/(9 log 16) = 0.0985841611274... < 0.099,
    (2/3)*(0.25-0.099) = 0.100666666666... > 0.1.

Thus the positive lower bound survives all rounding estimates. Finally H>=log n gives the second displayed inequality. The case L=n/2 is included in this corollary; it does not require Lemma 2.1's stricter upper-bound range.

## Independent numerical checks

Programs: `audit_exact.py` and `audit_numerics.py`. Their complete saved outputs follow. Neither imports or assumes the existence of an author program. `build_report.py` only assembles this report.

`audit_exact.py` uses `fractions.Fraction` for every small-n occupation probability and every rational bound. The factors pi^2 in Corollary 2.4 cancel exactly against the formula for a(i), so those comparisons are rational too. It checks all admissible t in its specified grid, all window widths for Lemma 2.1, all y<=L for Lemma 3.1, and both exact identities of Proposition 1.3(a) (the limit identity after multiplying by pi^2/6). It also checks the restricted drift estimate used in the linear asymptotic. For Corollary 3.2, whose hypotheses do not hold on the smallest states, it uses 60-decimal arithmetic at seven admissible grid points. For example n=144,L=72 fails the harmonic-number hypothesis and is correctly excluded; n=160,L=80 qualifies.

`audit_numerics.py` evaluates all eight table rows; the first three are independently recalculated with 60-decimal arithmetic. At n=4000 it computes the full occupation row by the requested descending recursion and checks it against a separate algorithm that propagates probability mass down from each state. Their maximum absolute difference is 2.22e-16. The limit linear sum is also recomputed from a 60-decimal closed harmonic identity, rather than only by summing the original terms.

Every numerical claim in the first two paragraphs of Section 5 is supported: only n and the window states enter its triangular recursion, giving O(L^2) arithmetic operations; the drift sum and ratio agree to the stated precision; 32930.33, 33176.20, 19165.35, 20168.71 and 1.2211 all round correctly. The maximizer in the last calculation is i=2667. All eight table rows round to the published four decimals, and all four dash locations are correct. In the log below a numeric `lower` is printed even when `applicable=False`; those values are not claimed as bounds in those rows.

Finite grids and floating-point agreement do not establish asymptotics or the general inequalities. Those conclusions rest on the proof audits above.

### Output of `audit_exact.py`

```text
EXACT FRACTIONS: all checks passed; n=2..40; Lemma2.2 i=2..20, all t<i; Lemma3.1 n=4..30, all L,y, T=1,2,3,4,8,16,40.
  (4.2) below-r drift: 780
  Cor2.4(a) first: 507
  Cor2.4(a) second: 507
  Cor2.4(b): 2838
  Lemma2.1: 361
  Lemma2.2: 209
  Lemma2.3 first: 5910
  Lemma2.3 second: 5130
  Lemma3.1: 28413
  Prop1.3(a) drift identity: 39
  Prop1.3(a) limit identity: 39
  Remark2.6 independent renewal bound: 190
  absorption: 39
Exact samples: a(4,2)=7/11, a(4,3)=6/11
Cor3.2 n=160, L=80: V=3.584582192486, bound=0.203754028848, Lemma3.1=0.436671392890
Cor3.2 n=256, L=128: V=3.961125780773, bound=0.220748164476, Lemma3.1=0.518058615649
Cor3.2 n=512, L=170: V=3.249434539998, bound=0.214161927100, Lemma3.1=0.505926580598
Cor3.2 n=512, L=256: V=4.524857543093, bound=0.245783420920, Lemma3.1=0.627694765154
Cor3.2 n=1024, L=256: V=3.038350267777, bound=0.216640832434, Lemma3.1=0.515122118255
Cor3.2 n=1024, L=341: V=3.688617213799, bound=0.236178867612, Lemma3.1=0.600318653004
Cor3.2 n=1024, L=512: V=5.094929088887, bound=0.270801040542, Lemma3.1=0.725041131593
Cor3.2 admissible 60-digit cases: 7
Cor3.2 constant 2*1.23/(9 log16)=0.09858416112741249950292819
Cor3.2 final coefficient (2/3)*(0.25-0.099)=0.1006666666666666666666667
Elapsed seconds: 1.746
Peak resident bytes (macOS): 21135360; inherited nice: 15
```

### Output of `audit_numerics.py`

```text
n=4000 reverse-recursion / forward-flow max absolute difference: 2.22e-16
drift occupation sum: 3999.0000000000518; exact target: 3999
drift limit sum: 2431.1004803142528; ratio: 1.644934066848248; pi^2/6: 1.644934066848226
linear occupation sum: 32930.330544509779; n log n: 33176.198560408113
linear limit sum: 19165.346953214266; (6/pi^2)n log n: 20168.710241362634
max a(4000,i)/a(i) subject to Cor2.4(a): 1.221052072361, at i=2667
Table1: n L V lower upper applicable [60-digit V when cross-checked]
2^9 56 1.620003562398 0.158758280396 2.209465791891 False mp=1.6200035623982398142308375 error=2.4587e-16
2^10 64 1.406642153783 0.154743451738 1.757167712819 False mp=1.4066421537827251122430101 error=5.6411e-17
2^14 1024 2.285479123025 0.211895744990 2.773441921715 True mp=2.2854791230253930181367787 error=4.1803e-18
2^16 4096 2.728385547781 0.240467645291 3.284847375283 True
2^18 16384 3.171680477219 0.269039191794 3.796617319891 True
2^22 16384 1.741274979068 0.207570418230 1.855418618981 True
2^30 16384 0.904744670408 0.162277611456 0.927053214287 False
2^40 16384 0.563197571673 0.140802573025 0.570492897454 False
independent closed-identity linear limit n=4000: 19165.3469532142805419541795941
Elapsed seconds: 2.181
Peak resident bytes (macOS): 37371904; inherited nice: 15
```

## Notation appendix audit

The meanings listed in the appendix are correct. Several entries give a section or a containing lemma rather than an exact first occurrence. I use the natural convention that the introductory body, rather than the abstract or macro definitions, determines first appearances. Under a literal whole-document convention, a(n,i), a(i), and phi already occur in the abstract, and those locations would also need adjustment.

| Appendix entry (source line) | Meaning and first-appearance check |
|---|---|
| h_r (555) | Correct; first used as h_(m-1) in the kernel, line 51, defined at 53. |
| (X_t) (556) | Correct; line 48. |
| P_n, E_n (557) | Correct; line 54. |
| a(n,i), a(i) (558–559) | Correct in the body; lines 60–63. |
| weight, occupation sum, limit sum (560–562) | Correct; terminology introduced at 79–80. |
| asymptotic symbols, C (563) | Correct; lines 55–56. C is also a generic bound constant in Remark 2.6. |
| gamma_* (564) | Correct; line 87. |
| K (565) | Correct; Theorem 1.1, line 101. |
| phi (566) | Correct in the body; Theorem 1.2, line 109. |
| N_j (567) | Correct; Theorem 1.2, lines 110–111. |
| g(i) (568) | Correct; lines 121–124. |
| W(n,L), V(n,L) (569–570) | Correct; lines 156–163. |
| rho (571) | Correct meaning; specifically the **proof** of Lemma 2.1, line 201. |
| S_t(i) (572) | Correct; statement of Lemma 2.2, line 216. |
| epsilon, M (573) | Meanings are correct locally. First appearances differ: epsilon is already used at lines 84–85, then in Corollary 2.4(b), line 249; M first appears in Theorem 1.1's proof at 271. Split the entry. |
| D_s (574) | Correct; line 314. |
| y, T, q (575) | Correct; statement of Lemma 3.1, line 317. |
| indicator (576) | Correct meaning; specifically the **proof** of Lemma 3.1, line 329. |
| Z (577) | Correct; line 329. |
| E (578) | Correct; line 325. |
| tau (579) | Correct; line 334. |
| lambda (580) | Correct; Corollary 3.2, line 347. |
| H (581) | Correct; proof of Corollary 3.2, line 354. |
| c, eta (582) | Correct meanings, but c first appears in the **statement** of Proposition 1.3(a), line 132; eta first appears in its proof, line 450. Split the entry. |
| psi (583) | Correct; proof of Theorem 1.2, line 389. |
| L_j, B_j (584) | Correct; proof of Theorem 1.2, line 394, with different choices in Proposition 1.3(b), line 460. |

Nontrivial mathematical symbols used but not given their own entries are:

- p(m,m-d), the transition kernel, first at line 51;
- f, the weight sequence, already at Ansatz 20, line 71 (its meaning is given indirectly by the existing “weight” entry);
- B, the arbitrary subset of states in the visit-count identity, first at line 180; this is different from a construction block B_j;
- theta, the fixed subpower exponent in Remark 2.6, first at line 306;
- x=lambda/H in the proof of Corollary 3.2, first at line 359;
- lambda_j=log(8N_j/L_j), first at line 413, reused at line 471.

For a literally exhaustive symbol index, also add roles/ranges for n (starting state), i and m (states), d (jump size), t (time or starting-point offset), s (jump/offset index), r (harmonic index or truncation state), j (sequence/summation or block index), k (growth exponent or summation/index variable), ell (starting point in S_t), and L (window width). These are conventional local variables, not undefined objects, and their omission is not a mathematical gap. Standard notation log, pi, set braces, floor/ceiling, sums, infimum, liminf/limsup and the positive integers needs no dedicated entry unless the appendix is intended to index literally every sign. The generic sequences x_n,y_n in the asymptotic definition are also conventional and differ from the local scalar x in Corollary 3.2.

## Corrections and clarifications, by source location

None of the following changes is needed to repair a numbered theorem or proof.

1. **Lines 169–172, introductory window comparison.** “The limits ... add up to about (6/pi^2)2^(-j)log n” should specify its approximation regime. For fixed j>=1 and L=floor(n/2^j), the precise asymptotic is

       sum_{i=n-L}^{n-1} a(i) ~ (6/pi^2)[-log(1-2^(-j))] log n.

   The coefficient 2^(-j) is the further narrow-window approximation -log(1-u)~u as u->0; it is not the exact coefficient for fixed j. For example j=1 gives log 2 rather than 1/2. If only comparability is intended, replace “about” with “of order” and specify the range. Likewise “of order (log n)/j visits” is conditional on the preceding window and harmonic-number hypotheses when deduced from the displayed bounds, and should say so. This heuristic is not used in any proof.
2. **Line 398, N_(j-1).** Qualify the comparison with “for j>=2.” N_0 is not defined or needed. The disjointness and zero-value argument for the first block is immediate.
3. **Appendix line 573, first appearance of epsilon and M.** Split this row. Epsilon first occurs at lines 84–85 in the cited polynomial-decay condition and is first used as a splitting fraction in Corollary 2.4(b), line 249; M first occurs at line 271.
4. **Appendix line 582, first appearance of c and eta.** Split this row. Point c to the statement of Proposition 1.3(a), line 132; eta belongs to its proof, line 450.
5. **Appendix lines 571 and 576.** For exact locations use “proof of Lemma 2.1” for rho and “proof of Lemma 3.1” for the indicator.
6. **Appendix lines 555–584, symbol coverage.** Add p, the local x, theta and lambda_j if the appendix is meant to cover all substantive symbols; include f directly or label its existing terminology row “f; weight.” Add B if local set symbols are indexed. The full list of conventional unindexed variables and the abstract/body convention is given above.

No correction is required to the constants, inequalities, numerical values, Table 1, uses of Fatou, or uses of the allowed monotonicity result. In particular monotonicity is used only with the target i fixed, and to compare a(n,i) with its limit. The separate attribution to BCM Theorem 1.1(iii) in Remark 2.6 is not an extension of Theorem 1.1(i) and is not used to prove a main result; its claimed bound has the independent derivation above. Other bibliographic descriptions and the wording of the original Ansatz have been treated as supplied context, without attempting forbidden external verification.

Task: “You are refereeing a mathematical paper before it is posted.” Received for this run on 12 November 2026, approximately 16:57 Asia/Tbilisi (first recorded local clock: 16:57:44).
