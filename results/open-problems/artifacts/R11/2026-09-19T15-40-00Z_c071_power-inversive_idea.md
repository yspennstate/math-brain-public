# R11 I0054 — idea before code: power-inversive translation hierarchy

Model runtime requested by owner: GPT-6 maximum. Actual report metadata for this run will state the runtime truthfully; this file is only the mathematical idea receipt.

Previous complete state: C070/U049, fixed metric 69 -> 70. This run uses nonrepeating B-moves #3, #14, #25.

## B3 — prove a stronger compiler, not just one cubic example

For fixed integer r>=1 and primes p with gcd(r,p-1)=1, define

phi_{p,r}(0)=0,   phi_{p,r}(x)=x^{-r} for x != 0.

Then phi_{p,r} is a permutation of F_p. For distinct visible offsets a_1,...,a_m and nonzero Fourier vector h, the translated m-vector t -> (phi(t+a_1),...,phi(t+a_m)) has additive-character phase

R_h(X)=sum_j h_j/(X+a_j)^r.

At any pole with h_j != 0 mod p the pole order is exactly r. For p>r this excludes Artin-Schreier degeneracy, so the classical rational-function Weil bound gives O_{m,r}(sqrt(p)); Erdos-Turan-Koksma then gives star discrepancy O_{m,r}(p^{-1/2}(log p)^m). Threshold-box counts therefore imply the same CTCS split-rate limit B(i,j) as U049, with quantitative error O_{m,r}(p^{-1/2}(log p)^{m+1}) + O_m(p^{-1}). This should yield finite-restriction path-TV convergence by the same hidden-label lumpability/uniformization argument.

## B14 — use the acting group explicitly

The additive group F_p acts regularly by translation on every threshold base set

S_u^{(r)}={x in F_p: phi_{p,r}(x)<u}.

The tree proposal family is the orbit {S_u^{(r)}-t : t in F_p}. This makes the model deterministic and algebraic. It also gives an exact finite-tree property: every pair of distinct ambient labels is separated by some translated threshold because phi_{p,r} is injective.

For the concrete new class choose r=3 and, for each N, p_N = least prime p>=N with p congruent 2 mod 3. Then gcd(3,p_N-1)=1, so x -> x^{-3} is a permutation. Infinitely many primes 2 mod 3 is classical (and elementary); no prime-gap rate is needed, only p_N -> infinity.

## B25 — double-count the full-ambient root split sizes

For N=p (all ambient labels present), every threshold u mask has exactly u red labels, independently of the particular permutation phi. Hence summing proposal clocks over all p translations and both complementary thresholds shows that the aggregate root hazard for size {i,p-i}, i<p/2, is exactly

p/[i(p-i)].

On the CTCS side, summing the specified split rate B(i,p-i) over the C(p,i) subsets gives

C(p,i) B(i,p-i)=p/[i(p-i)].

So every permutation-threshold translation model has the exact CTCS aggregate root split-size rates at full ambient size p, even when its labeled split array is highly anisotropic. The labeled array is therefore the correct non-equivalence invariant.

## concrete finite witness to test exactly

At N=4, p=5, r=3, x^{-3}=x on F_5^*. Preliminary exact hand calculation predicts the three unordered 2|2 specified split rates have multiset

{0, 1/6, 1/3}.

Compare: source/C070 {1/6,1/6,1/6}; C069 {0,1/4,1/4}. The zero pattern and the ratio 2 between the two nonzero balanced rates survive leaf relabeling and positive global time rescaling, so this should separate C071 from the source, C070 and C069. Repository search before code found no retained I0054 artifact containing the exact signature `0,1/6,1/3`.

If the exact checker confirms the identities and no proof gap appears, count C071 and move 70 -> 71. Otherwise leave the metric unchanged and report the failure.
