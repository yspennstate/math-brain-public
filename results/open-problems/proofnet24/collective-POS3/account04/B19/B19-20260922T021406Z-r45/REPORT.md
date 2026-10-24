# POS3 account04/B19 — autonomous-chain gap envelope and size-imbalance reduction

**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent target:** every finite nonchain poset of width at most three has an incomparable pair whose uniform-linear-extension ordering probability lies in `[1/3,2/3]`.  
**Parent status:** **OPEN / NOT PROVED**.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

This run continues `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z` and performs no brain-installation or benchmark work.

## 1. Exact source-bound state consumed

The current campaign lead version actually present at the scientific snapshot is:

1. **Team lead account04/B10**, `proofnet24/collective-POS3/account04/B10/20260922T011127Z-account04-B10-POS3-r11/REPORT.md`, blob `1e5a9682e4f90f38484a86e7199428de0b0160f8`. It proves that in a hypothetical width-three counterexample every element has its common strong-majority rank with probability `>1/81`, equivalently the joint three-chain majority cell satisfies `81 W_x(g_b(x),g_c(x))>E`. Its surviving route is a global consecutive-boundary/signed-flux incompatibility.

The named OTHER-account partner result actually consumed and applied is:

2. **Partner account01/B10**, `proofnet24/collective-POS3/account01/B10/20260922T010919Z-b10-pos3-r11/REPORT.md`, blob `b33f4c52f0da12d8bcb9f30b89c9ceb1a88b3936`. It proves by exact exhaustive certificate that no choice of three-chain cover and deleted chain can in general remove all strictly nested insertion profiles, even in a connected module-prime width-three poset. Thus the induction is not allowed to evade the weighted/nested defect by choosing a “better” cover. I use that negative result here by working with the exact autonomous-chain profile family `{0},[0,m],{m}` and proving a quantitative bound on the remaining corridor law, rather than assuming nested profiles can be removed.

I also use the following completed compatible results.

3. **account02/B10**, `proofnet24/collective-POS3/account02/B10/20260922T014627Z-account02-B10-pos3-r12/REPORT.md`, blob `acdb868b3e35a9248d494126311bfff3bfee150b`. It proves an exact endpoint blocker-product cap and that both Hasse-blocker channels at the first/last strong-majority boundary are active; this identifies the module-prime branch as genuinely multi-boundary rather than a one-boundary local problem.

4. **Prior account04/B19 autonomous-chain report**, `proofnet24/collective-POS3/account04/B19/B19-20260922T0113Z-r44/REPORT.md`. It proves that if
`C={c_1<...<c_m}` is autonomous, `Q=P\C`, and `D,N,U` are respectively the elements uniformly below, incomparable with, and uniformly above `C`, then for `tau in L(Q)`
`W_C(tau)=binom(m+K(tau),K(tau))`,
where `K(tau)` is the number of neutral elements of `N` lying after the last `D` and before the first `U`. It also proves that a minimal counterexample can only have a boundary-active autonomous chain and gives the exact conditional atom formula
`A(m,k,r,j)=binom(j+r-1,r-1) binom(m-j+k-r,k-r)`
for a central neutral element.

The previous B19 run paid only the singleton-neutral internal-gap case. The first uncovered autonomous-chain case is to determine how far that argument extends when several central neutral elements can occur.

## 2. Compact conditional end-to-end route

Assume POS3 is false and choose a counterexample of minimum cardinality. The existing reductions permit a width-exactly-three, incomparability-connected core with no proper autonomous nonchain. There are then two honest branches.

- **Module-prime / genuinely global branch.** The lead `>E/81` central-cell condition, the account01/B10 unavoidable nested-profile obstruction, and the account02/B10 two active endpoint Hasse channels must be coupled across consecutive strong-majority boundaries.
- **Proper autonomous-chain branch.** The preceding B19 report reduces the entire deletion bias to `K(tau)`. Constant `K` is already excluded by induction. What remained unpaid was whether a neutral element can split a nontrivial autonomous chain internally in the common strong-majority order when the central corridor is not constant.

This run resolves a large exact subcase of the second branch: **if the central corridor never contains more neutral elements than the chain length, then no neutral element can split the chain internally.**

## 3. Exact conditional gap distribution

Let `C={c_1<...<c_m}` be an autonomous chain with `m>=2`, put `Q=P\C`, and retain the trichotomy `Q=D disjoint_union N disjoint_union U`.

Fix `tau in L(Q)`. Suppose `n in N` is central in `tau`, `k=K(tau)`, and `n` is the `r`-th of the `k` central neutral elements. Let

`J_C(n)=#{i : c_i precedes n}`.

The preceding B19 report gives the exact lift count

`A(m,k,r,j)=binom(j+r-1,r-1) binom(m-j+k-r,k-r)`                 (3.1)

for `J_C(n)=j`, while the whole fiber has

`W(m,k)=binom(m+k,k)`                                           (3.2)

lifts. Therefore

`Pr(J_C(n)=j | tau)=A(m,k,r,j)/W(m,k)`.                         (3.3)

If `n` is noncentral then `J_C(n)` is forced to the endpoint `0` or `m`, so every interior atom is zero.

## 4. New binomial envelope

### Theorem 4.1 — internal gap envelope for `k<=m`

For integers

`m>=2`, `1<=k<=m`, `1<=r<=k`, `1<=j<=m-1`,

one has

`A(m,k,r,j) <= binom(m+k-2,k-1)`.                               (4.1)

Consequently

`Pr(J_C(n)=j | tau)`
`<= [m k]/[(m+k)(m+k-1)]`
`<= 1/3`.                                                       (4.2)

### Proof of (4.1)

Set

`A0=j+r-1`, `B0=m-j+k-r`.

Then `A0+B0=m+k-1`, and the left side of (4.1) is

`binom(A0,r-1) binom(B0,k-r)`.

We compare it to the Vandermonde expansion of

`binom(m+k-2,k-1)`.

There are two cases.

**Case 1: `j>=r`.** Use Pascal on the second factor:

`binom(B0,k-r)`
`=binom(B0-1,k-r)+binom(B0-1,k-r-1)`.

Hence the left side equals

`binom(A0,r-1)binom(B0-1,k-r)`
`+binom(A0,r-1)binom(B0-1,k-r-1)`.

In the Vandermonde expansion for the two blocks of sizes `A0` and `B0-1`, the first term above is the summand with first-block choice `r-1`, while the summand with first-block choice `r` is

`binom(A0,r)binom(B0-1,k-r-1)`.

Because

`binom(A0,r)/binom(A0,r-1)=j/r >=1`,

those two Vandermonde summands dominate the two displayed terms. Thus (4.1) holds.

**Case 2: `j<r`.** Since `m>=k`, one must have

`m-j >= k-r+1`;                                                (4.3)

otherwise integer inequalities `j<=r-1` and `m-j<=k-r` would imply `m<=k-1`.

Now use Pascal on the first factor:

`binom(A0,r-1)`
`=binom(A0-1,r-1)+binom(A0-1,r-2)`.

The Vandermonde expansion for blocks of sizes `A0-1` and `B0` contains the corresponding summands

`binom(A0-1,r-1)binom(B0,k-r)`

and

`binom(A0-1,r-2)binom(B0,k-r+1)`.

By (4.3),

`binom(B0,k-r+1)/binom(B0,k-r)`
`=(m-j)/(k-r+1) >=1`.

So these two target summands dominate the Pascal split of the left side, proving (4.1) again. We use the usual convention that out-of-range binomial coefficients are zero. `□`

Dividing (4.1) by (3.2) gives

`binom(m+k-2,k-1)/binom(m+k,k)`
`=mk/[(m+k)(m+k-1)]`.

It remains to show this is at most `1/3`. Write `m=k+d` with `d>=0`. For `k>=2`,

`(m+k)(m+k-1)-3mk`
`=k(k-2)+d(k-1)+d^2 >=0`.

For `k=1`, `m>=2` and the same difference is `m(m-2)>=0`. This proves (4.2). Equality can occur at the smallest boundary cases, but the counterexample heavy gap is **strictly** greater than `1/3`.

## 5. Strong-majority consequence

The following step does not assume a uniform deletion law.

### Lemma 5.1 — a no-balanced chain comparison has a `>1/3` threshold atom

Fix `n||C` and define

`p_i=Pr(c_i precedes n)`.

Because `c_i<c_{i+1}`, the events are nested and

`p_1>=p_2>=...>=p_m`.

If no pair `(c_i,n)` is balanced, every `p_i` lies in `(0,1/3)` or `(2/3,1)`. Hence there is a threshold `g in {0,...,m}` in the common strong-majority order.

If `0<g<m`, then

`Pr(J_C(n)=g)=p_g-p_{g+1}>1/3`.                                (5.1)

For `g=0`, `Pr(J_C(n)=0)=1-p_1>2/3`; for `g=m`,
`Pr(J_C(n)=m)=p_m>2/3`.

Thus an internal strong-majority gap necessarily carries **strictly more than one third** of all ambient extensions. This is exactly the autonomous-chain specialization of the account01/B10 heavy-slice normal form, derived directly from the true ambient uniform law.

### Theorem 5.2 — low-corridor autonomous chains cannot be split internally

Let `P` have no balanced incomparable pair and let `C` be an autonomous chain of length `m>=2`. Define

`kappa(C)=max_{tau in L(P\C)} K(tau)`.

If

`kappa(C)<=m`,                                                   (5.2)

then every `n in N` lies entirely before all of `C` or entirely after all of `C` in the common strong-majority order. In particular no neutral element splits `C` internally.

**Proof.** Fix an interior `j`. Conditional on any deletion word `tau`:

- if `n` is noncentral, `Pr(J_C(n)=j|tau)=0`;
- if `n` is central, then `k=K(tau)<=kappa(C)<=m`, so Theorem 4.1 gives `Pr(J_C(n)=j|tau)<=1/3`.

The actual ambient law is a convex combination of these conditional fiber laws with their exact weights `W_C(tau)`. Therefore

`Pr(J_C(n)=j)<=1/3`

for every interior `j`. Lemma 5.1 says an internal strong-majority gap would have probability strictly greater than `1/3`, contradiction. `□`

## 6. Arbitrary-size induction corollaries

### Corollary 6.1 — size-imbalance necessary for a block-splitting chain module

If a proper autonomous chain `C` of length `m>=2` in a hypothetical minimal counterexample is split internally by any neutral element in the common strong-majority order, then

`kappa(C)>=m+1`,                                                 (6.1)

and hence

`|N|>=m+1`.                                                      (6.2)

So a block-splitting autonomous chain must have **strictly more neutral vertices than chain vertices**.

This is a new arbitrary-size size-imbalance constraint, not a finite census.

### Corollary 6.2 — if `|N|<=|C|`, the module is one strong-majority chain segment

Since `K(tau)<=|N|`, condition `|N|<=m` implies `kappa(C)<=m`. Therefore every neutral element lies before or after the whole chain. Every `d in D` is poset-below every member of `C`, and every `u in U` is poset-above every member. Thus **no element of `P\C` lies between two consecutive elements of `C` in the common strong-majority order**.

Consequently `C` is a contiguous segment of that order and is contained in a single maximal contiguous chain block.

This strictly extends the preceding B19 singleton-neutral result: it handles arbitrarily many neutral vertices whenever their total number does not exceed the module length, and more generally handles any larger `N` for which no deletion word has more than `m` central neutrals.

## 7. How this integrates with the lead/partner global route

The partner account01/B10 result rules out the false shortcut “choose a cover/deletion with no nested profiles.” The new theorem does not use that shortcut. It pays an exact special case where the profile family is forced by autonomy and the corridor multiplicity is known exactly.

The lead account04/B10 and account02/B10 results remain the correct residual for the module-prime branch: simultaneous `>E/3` bands, `>E/81` central cells, and two active endpoint Hasse channels must still be coupled across boundaries.

For the autonomous-chain induction branch, the residual is now narrower:

1. constant corridor `K` — already eliminated by induction;
2. nonconstant corridor with `kappa(C)<=|C|` — **cannot split the chain internally** by this run;
3. any chain module that actually spans more than one strong-majority chain block must satisfy the exact large-neutral condition `kappa(C)>=|C|+1`, hence `|N|>|C|`.

Thus the next chain-module implication is no longer an arbitrary weighted deletion problem: it starts only in the regime where a width-at-most-two neutral region contains more vertices than the autonomous chain and some deletion word places at least `m+1` of them simultaneously in the central window.

This does not close POS3; it removes a genuine infinite family of the induction residual.

## 8. Exact computation

The authoritative verifier for the binomial envelope is

`verify_autonomous_chain_k_le_m.py`.

It uses only the Python standard library and exact integer/rational arithmetic. It checks every tuple

`2<=m<=60`, `1<=k<=m`, `1<=r<=k`, `1<=j<=m-1`

for a total of `1,673,535` exact atom inequalities, including the envelope and the `<=1/3` bound. The captured output is

`verify_autonomous_chain_k_le_m.out`

and ends with

`POS3_AUTONOMOUS_CHAIN_K_LE_M_CHECK_PASS`.

The execution was run with site initialization disabled. The symbolic proof above is the proof of Theorem 4.1; the finite computation is regression evidence only.

An earlier, weaker verifier in this same immutable run folder checks only `k<=2`; it is preserved as history but is superseded by the `k<=m` verifier and is not the source of the theorem claimed here.

## 9. Claim status and failure boundary

- Exact autonomous-chain fiber/corridor law: inherited **PROVED**.
- Partner claim that nested defects cannot globally be removed by cover choice: inherited **EXACTLY REFUTED shortcut**, and applied.
- Binomial envelope (4.1) for every `k<=m`: **PROVED**.
- Internal gap probability `<=1/3` under `kappa(C)<=m`: **PROVED**.
- Size-imbalance condition `kappa(C)>=m+1`, hence `|N|>=m+1`, for any internally split autonomous chain in a no-balanced candidate: **PROVED**.
- Claim that every boundary-active autonomous chain is impossible: **NOT PROVED**. The surviving `|N|>|C|` / large-central-corridor case is retained explicitly.
- Parent width-three `1/3–2/3` target: **OPEN / NOT PROVED**.

No novelty or priority claim is made. No benchmark gold, credentials, scheduler identifiers, machine paths, unrelated private data or transcripts, email, Drive, paid API/model/Codex call, remote workflow, public posting, or permission change was used.
