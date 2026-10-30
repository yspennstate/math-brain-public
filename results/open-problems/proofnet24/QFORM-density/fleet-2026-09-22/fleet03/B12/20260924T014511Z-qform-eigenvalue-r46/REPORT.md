SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B12, 2026-09-24T01:45:11Z.
attacking: overlap-compressed local spectral additions — many arbitrary signed packets sharing the same physical leakage plane should spend that plane only once, not once per packet.

# fleet03/B12 r46 — overlap-compressed local spectral additions

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Additional eigenvalue control  
Status: **PROVED SUPPORTING THEOREM / FULL QFORM OPEN**  
Continuity: **not claimed for the compiler as a whole**; the six-mode receiver used below establishes the stated essential density bound.

## 1. Motivation and first missing implication

The preceding fleet03/B12 local-row packet theorem allows arbitrary signed packets, but its direct packetwise form spends the sum of their local rank budgets. This can be grossly wasteful when many packets have large local parts whose physical row footprints overlap. The present run removes that loss.

The key point is deterministic and precedes probability: if all unbounded parts of many additions land in one `q`-dimensional physical row plane, then their **sum** is still only rank `q` on that physical carrier, independently of the number, signs, magnitudes, global ranks, or mutual commutation of the packets. The remaining transverse leakage is the only norm loss.

No rotated coordinate is declared independent and no random quadratic remainder is treated as convolution noise.

## 2. Matrix lemma: spend the common local footprint only once

For a real `m x n` matrix `M`, let `s_1(M)>=s_2(M)>=...` denote singular values.

### Lemma 2.1 — rank-plus-tail lower interlacing

Let

`N=L+R`, `rank(L)<=q`.

Then for every `k` with `k+q<=min(m,n)`, 

` s_k(M+N) >= [ s_(k+q)(M) - ||R||op ]_+. `                 (2.1)

#### Proof

The singular-value Weyl inequality

` s_(i+j-1)(X+Y) <= s_i(X)+s_j(Y) `

applied to

`M+R=(M+R+L)+(-L)`

with `(i,j)=(k,q+1)` gives, because `s_(q+1)(L)=0`,

` s_(k+q)(M+R) <= s_k(M+R+L). `                              (2.2)

The same inequality with the operator-norm perturbation `R` gives

` s_(k+q)(M+R) >= s_(k+q)(M)-||R||op. `                      (2.3)

Combining (2.2)-(2.3) proves (2.1). QED.

### Corollary 2.2 — exact local perturbation profile

For arbitrary `N` and every admissible `q`, choose `L` to be a best rank-`q` approximation to `N`. By Eckart--Young,

` ||N-L||op=s_(q+1)(N). `                                    (2.4)

Hence

` s_k(M+N) >= [s_(k+q)(M)-s_(q+1)(N)]_+. `                  (2.5)

Optimizing the spent rank gives

` s_k(M+N) >= max_(0<=q<=min(m,n)-k)`
`                [s_(k+q)(M)-s_(q+1)(N)]_+. `               (2.6)

The coefficient one on the tail is sharp already for scalar diagonal perturbations. The index shift by `q` is also sharp: a rank-`q` perturbation can cancel exactly `q` singular directions.

## 3. Overlap-compressed physical-row theorem

Let `H` be `m` ORIGINAL coordinates and `P_H` the row selector. Let

` A=A_*+sum_(j=1)^J T_j `                                    (3.1)

with every `T_j` symmetric, with no commutation or norm assumption. Suppose that for each packet we have a decomposition on the physical row bank

` P_H T_j = L_j+R_j. `                                       (3.2)

Define the **common physical footprint**

` V=span( Ran(L_1),...,Ran(L_J) ) subset R^m,`
` q_*=dim V,`

and the aggregate transverse leakage

` eps=||sum_j R_j||op. `                                     (3.3)

Then `L=sum_j L_j` has range contained in `V`, hence `rank(L)<=q_*`. Lemma 2.1 therefore gives:

### Theorem 3.1 — `QFORM-OVERLAP-COMPRESSED-LOCAL-ADDITION-v1`

For every `k` with `k+q_*<=m`, 

` s_k(P_H A) >= [s_(k+q_*)(P_H A_*)-eps]_+. `               (3.4)

Since `A` is symmetric,

` (P_H A)(P_H A)^T=(A^2)[H,H]. `                             (3.5)

Thus (3.4) is exactly the physical square-energy statement

` sqrt(lambda_k((A^2)[H,H]))`
`   >= [s_(k+q_*)(P_H A_*)-eps]_+. `                         (3.6)

The gain over a packetwise rank budget is that `q_*` is the dimension of the **union of the local large-mode footprints**, not the sum of their individual dimensions. Arbitrarily many packets may therefore spend the same physical direction only once.

### Equivalent best-plane form

For any `q`-plane `V subset R^m`, decompose the total local addition `N=P_H(A-A_*)` as

` L=P_V N,  R=(I-P_V)N. `                                    (3.7)

Then

` s_k(P_H A) >= s_(k+q)(P_H A_*)-||(I-P_V)P_H(A-A_*)||op. ` (3.8)

Optimizing over `V` recovers (2.5), because the minimum transverse norm over all `q`-planes equals `s_(q+1)(P_H(A-A_*))`.

## 4. Literal arbitrary-eigenvalue specialization

For one symmetric packet write its spectral decomposition

` T_j=sum_a theta_(j,a) v_(j,a) v_(j,a)^T. `                 (4.1)

Fix a threshold `h_j>0` and split

` T_j=T_j^hi+T_j^lo,`

where `T_j^hi` contains the eigenmodes with `|theta_(j,a)|>h_j`. Then

` ||T_j^lo||op<=h_j. `                                       (4.2)

Moreover

` Ran(P_H T_j^hi)`
`  subset span{P_H v_(j,a): |theta_(j,a)|>h_j}. `             (4.3)

Consequently, if the projected high-eigenvalue vectors from **all packets together** lie in a common `q_*`-dimensional physical plane `V`, then Theorem 3.1 applies with

` eps <= ||sum_j P_H T_j^lo||op <= sum_j h_j. `              (4.4)

All high eigenvalues may have arbitrary sign and arbitrary magnitude; there may be arbitrarily many of them and the packets need not commute. Only their *combined physical footprint dimension* is charged.

If in addition the low spectral parts have pairwise orthogonal global spectral supports, then their sum is block diagonal on orthogonal subspaces and the stronger bound holds:

` eps <= ||sum_j T_j^lo||op=max_j ||T_j^lo||op<=max_j h_j. ` (4.5)

Thus multiple orthogonal spectral bands cost the maximum small threshold rather than its sum.

## 5. Actual application of the designated fleet04/B12 result

The current designated partner is fleet04/B12 r8:

`yspennstate/math-open-problems@bcb9fd2641440a89d6e4967781d755618e163001`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B12/20260924T002154Z-fleet04-B12-multihub-shear-r8/REPORT.md`.

Its completed multihub shear theorem states that for an eight-coordinate physical carrier `H`, with hub dimension `p=2`, transverse reserve `ell=6`,

` s_2(Lambda)>=4,  s_6(R)=2,`
` ||Lambda^(-1)W^T||op<=1,`

one has

` s_8(P_H A_*) >= gamma(1)*2 = sqrt(5)-1. `                  (5.1)

Here `A_*` already permits the partner's arbitrary signed aligned spectral packets.

Now add **any number** of further symmetric packets `T_1,...,T_J`. Suppose their unbounded/high parts may be completely arbitrary globally but their combined `H`-row ranges lie in one common two-plane `V` (not required to equal the partner hub plane), while

` ||sum_j R_j||op <= 1/100 `                                  (5.2)

for the aggregate transverse local leakage. Theorem 3.1 spends that common plane once: `q_*=2`. With `k=6`, (5.1)-(5.2) give the actual final-matrix inequality

` s_6(P_H A)`
`   >= s_8(P_H A_*)-1/100`
`   >= sqrt(5)-1-1/100`
`   = 1.2260679774997898... =: g. `                           (5.3)

This is a strict multi-packet improvement over paying two rank directions per packet. For example, with just two packets whose individual local high parts each have rank two but use the same physical plane, a packetwise sum would spend four directions and would ask for an unavailable `s_10` reserve on the eight-row carrier. Equation (5.3) still spends only two.

Because row restriction is a contraction,

` s_6(A)>=s_6(P_H A)>=g>1, `                                  (5.4)

so the full final matrix is in the owner's target class and in fact has six global singular values above one.

Taking `G=A^2`, equation (5.3) gives

` lambda_6(G[H,H])>=g^2. `                                   (5.5)

We may therefore apply the completed fleet02/B12 six-mode theorem

`QFORM-SIX-MODE-SPECTRAL-SQUARE-CARRIER-v1`,

canonical source

`yspennstate/math-open-problems@e6c20a6e5a077c71e1ae7ac27e71d889a5e6a004`.

For `m=8`, `N=binom(8,2)=28`, choose its canonical parameters

` b=g/2,  a=g/(4N),  kappa=g/(4N),  s=g. `                    (5.6)

The four receiver bounds are then

`8N sqrt(6 pi m)/g                  = 2243.515238502045...`,
`4 pi N/g                           = 286.981132905509...`,
`3*400^(1/3)*(4N/g)^(5/6)*g^(-1/6)= 919.690543684381...`,
`10 sqrt(2e)/(sqrt(3)g)             = 10.979613733772...`.     (5.7)

Hence the **full ambient quadratic form**, retaining every added packet, all outside coefficients and all couplings allowed by the receiver, obeys

` ||p_(X^T A X)||_(infinity,ess) <= 2243.515238502045. `      (5.8)

No input moments, bounded support, log-concavity, centering, or diagonal-basis independence are used.

## 6. Deterministic finite checks

A seeded checker tested 10,000 random rectangular instances of the core overlap inequality. Each trial used an `8 x 16` baseline, between two and seven arbitrarily large local packets whose high parts all had column space inside the same random two-plane, and an aggregate dense transverse tail with random operator norm at most `0.2`.

Result:

` trials=10000`
` violations=0`
` minimum_margin=0.01935417353930946`
` median_margin=0.8944772862214622`.                          (6.1)

A second seeded test checked the optimized inequality (2.5) on 10,000 unrestricted random matrix pairs and found zero violations. These checks are only sanity tests; the proof is the singular-value argument above.

## 7. Scope, corrections, and remaining gap

This theorem is a coefficient-matrix stability result. It does **not** assert that the bare hypothesis `s_3(A)>=1` always yields an eight-row partner carrier, a low-dimensional local addition plane, or the six-mode receiver premises. It therefore does not solve the full conjecture.

The result is nevertheless useful for the exact assignment: many arbitrary smaller and larger added eigenvalues of either sign may be retained without any probabilistic independence assumption, and overlapping physical leakage is charged by its union dimension rather than once per packet.

The full target remains **OPEN / NOT PROVED / NOT DISPROVED**.

The next structural implication is to derive, from the bare three-large-eigenvalue condition, either (i) a bounded physical carrier on which the destructive local spectral leakage has low common-plane dimension, or (ii) a proved projected-crossing/grouped-bank/ridge/hub receiver when this common-plane condition fails.

Current brain status for this run: `WITHOUT_VERIFIED_BRAIN`; repository transport is not native learned-memory ingestion.
