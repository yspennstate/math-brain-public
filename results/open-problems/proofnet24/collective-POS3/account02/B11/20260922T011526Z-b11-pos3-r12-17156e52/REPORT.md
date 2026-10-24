# POS3 account02/B11 — autonomous-chain binomial corridor reduction

**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent POS3 status:** `OPEN / NOT PROVED`  
**Brain status:** `WITHOUT_VERIFIED_BRAIN`

## 1. Exact collective state consumed

This run follows OWNER CONTROL revision `2026-09-22.2` and the collective POS3 allocation; the superseded benchmark/installation duties were not resumed.

I consumed the exact prior account02/B11 ordinal-factorization report, blob `b71c5087c4982769946c31f1ec76242bf297fe17`: a cardinality-minimal counterexample may be assumed to have connected incomparability graph. I then consumed and applied the named OTHER-account partner result **account03/B19**, run `account03-B19-20260922T000316Z-pos3-r11`, report blob `106c46c118f9863c6fc7867d2ae536dd0786818e`. Its exact 9-element width-three certificate has 420 linear extensions, connected incomparability graph, no balanced extremal-anchor pair, and refutes the attempt to force a light insertion slice from connectedness alone.

The campaign lead **account04/B10** had no complete collective-POS3 archive entry at the initial scientific snapshot, but one appeared on the mid-run refresh and was read before this report: run `20260922T011127Z-account04-B10-POS3-r11`, report blob `1e5a9682e4f90f38484a86e7199428de0b0160f8`. It proves that in any width-at-most-three no-balanced candidate every element has more than `1/81` of all extensions at its rank in the common strong-majority order.

Two further exact dependencies sharpen the induction branch attacked here:

- account04/B19, report blob `ce30dae79d698103f026d4d871033238489b1fb1`: a cardinality-minimal counterexample has no proper autonomous nonchain;
- account02/B19, fresh same-account report blob `14588aa0c8cfb8bff56ebd7d08b3d361f6653a90`: expanding a proper autonomous chain can destroy a fixed balanced pair of the contracted quotient, even in an exact infinite width-three family, so fixed-pair contraction is not a valid induction.

Thus the remaining module branch is exactly the case of a **proper autonomous chain**. This report reduces that branch to a one-dimensional binomial corridor tilt and identifies the first missing migration implication.

## 2. Conditional end-to-end route

Assume POS3 is false and choose a counterexample `P` of minimum cardinality.

1. Width two is already solved, so `width(P)=3`.
2. By the prior account02/B11 theorem, `Inc(P)` is connected.
3. By account04/B19, every proper autonomous subset of `P` is a chain.
4. If a proper autonomous chain `M` exists, the theorem below shows that deleting `M` does **not** produce an arbitrary chain-insertion weight: the exact projected density depends only on a single integer, the number of externally incomparable elements in the active corridor, through one binomial coefficient.
5. If the migration dichotomy isolated in Section 6 can be proved, proper autonomous chains are eliminated too, so a minimal counterexample is module-prime. The surviving module-prime branch then also satisfies the campaign lead's `>1/81` pinned-rank atom, the existing `>E/3` heavy-slice marginals, and the double-blocker constraints at majority-block boundaries.

The first unpaid implication in this assigned structural branch is therefore the migration dichotomy in Section 6, not ordinal factorization and not fixed-pair contraction.

## 3. Exact binomial lift law for an autonomous chain

Let

`M={c_1<...<c_m}`

be a proper autonomous chain in a finite poset `P`, and put `Q=P\M`. Autonomy partitions `Q` into

- `D={q: q<c_j for every j}`;
- `I={q: q||c_j for every j}`;
- `U={q: c_j<q for every j}`.

Fix `tau=(q_1,...,q_n) in L(Q)`. Let

`a(tau)=max{position_tau(d): d in D}`, with `a=0` if `D` is empty,

and

`b(tau)=min{position_tau(u): u in U}`, with `b=n+1` if `U` is empty.

Because every `d in D` satisfies `d<c_1<...<c_m<u` for every `u in U`, transitivity gives `d<u`; hence `a<b`. Every `Q`-element strictly between the last `D` and first `U` position belongs to `I`. Define the **active corridor length**

`r(tau)=b(tau)-a(tau)-1`.

### Theorem 3.1 — autonomous-chain binomial fiber

For every `tau in L(Q)`, the number of linear extensions of `P` restricting to `tau` is exactly

`W_M(tau)=binom(m+r(tau),m)`.

Consequently

`e(P)=sum_{tau in L(Q)} binom(m+r(tau),m)`,

and the restriction of a uniform random linear extension of `P` to `Q` has exact law

`mu_M(tau)=binom(m+r(tau),m)/e(P)`.

### Proof

Every member of `M` must occur after every member of `D` and before every member of `U`. Therefore no member of `M` can be inserted before the last `D` or after the first `U` in `tau`.

Conversely, every `Q`-element in the open interval between those two boundary positions lies in `I` and is incomparable with every member of `M`. Thus, once `tau` is fixed, the only freedom is to interleave the ordered `m`-term chain `c_1,...,c_m` with the fixed ordered list of the `r(tau)` corridor elements. Every such shuffle is valid and every lift arises uniquely this way. Choosing the `m` positions occupied by `M` among the `m+r(tau)` positions gives exactly `binom(m+r(tau),m)` lifts. Summing fibers gives the other formulas. `□`

This is substantially simpler than a general deleted-chain corridor: for an autonomous chain, all insertion information collapses to the single scalar `r(tau)`.

### Corollary 3.2 — exact outside-pair reweighting

For incomparable `x,y in Q`,

`Pr_P(x<y)`

`= [sum_{tau in L(Q)} binom(m+r(tau),m) 1{x<tau y}]`

`  / [sum_{tau in L(Q)} binom(m+r(tau),m)]`.

Thus contraction can fail only through correlation of the pair event with this one-dimensional binomial tilt.

## 4. Exact cross-pair kernel and heavy module gaps

The same fiber description gives a closed kernel for pairs meeting the module. Suppose `z in I` lies in the active corridor of `tau` and is the `k`-th corridor element. In a lift let `H_z` be the number of `M`-elements preceding `z`. For `0<=h<=m`, the number of lifts of `tau` with `H_z=h` is

`binom(k-1+h,h) binom(r(tau)-k+m-h,m-h)`.

Indeed, before `z` one shuffles `h` module elements with the first `k-1` corridor elements, and after `z` one shuffles the remaining `m-h` module elements with the remaining `r-k` corridor elements. Summing over `h` gives `binom(m+r,m)`, as required.

If `z` lies before the active corridor then `H_z=0` in every lift; if it lies after the active corridor then `H_z=m` in every lift. Therefore every module/outside probability is an exact sum of these kernels over `tau`.

Now assume `P` has no balanced pair. For fixed `z in I`, put

`p_j=Pr_P(c_j<z)=Pr(H_z>=j)` for `1<=j<=m`,

with conventions `p_0=1` and `p_{m+1}=0`. If no pair `(c_j,z)` is balanced, none of `p_1,...,p_m` lies in `[1/3,2/3]`. Since the sequence is nonincreasing from `1` to `0`, there is an index `h(z) in {0,...,m}` such that

`p_h>2/3` and `p_{h+1}<1/3`.

Hence

`Pr(H_z=h(z))=p_h-p_{h+1}>1/3`.      (4.1)

So a no-balanced candidate containing an autonomous chain has a very rigid additional property: **every element externally incomparable with the module has more than one third of all full extensions placing it in one particular gap of the module.** This is the autonomous-chain version of the heavy-gap phenomenon, now derived directly from exact full-extension probabilities.

Also, because one member of `M` is incomparable with every element of `I`, `width(I)<=2`; otherwise a 3-antichain in `I` together with that member of `M` would give a 4-antichain in `P`.

## 5. Minimal-counterexample consequence

Let now `P` be a cardinality-minimal POS3 counterexample and let `M` be a proper autonomous chain with `|M|=m>=2`.

First, `Q=P\M` is a nonchain. If `Q` were a chain, then `P` would be the union of the two chains `Q` and `M`, hence would have width at most two, contradicting `width(P)=3`.

Therefore minimality supplies at least one pair balanced under the **uniform** law on `L(Q)`. But every pair in `P` is unbalanced. By Corollary 3.2, the single scalar weight

`w(tau)=binom(m+r(tau),m)`

must push every uniform-balanced pair of `Q` outside `[1/3,2/3]`.

In particular `r(tau)` cannot be constant on `L(Q)`: if it were constant then `w` would be constant, the projected law would be uniform, and a balanced pair of `Q` would remain balanced in `P`.

Combining with (4.1), any proper autonomous chain surviving in a minimal counterexample must simultaneously satisfy:

1. `Q` is a smaller nonchain of width at most three;
2. `I` is nonempty and has width at most two;
3. the active-corridor length `r(tau)` varies over `L(Q)`;
4. the binomial tilt `binom(m+r(tau),m)` destroys **every** uniform-balanced pair of `Q`;
5. for every `z in I`, one module gap has full-extension mass `>1/3`.

This is the genuinely unresolved chain-module core exposed by the present reduction.

## 6. First missing implication: autonomous-chain migration dichotomy

The natural exact closure statement is now:

> **Autonomous-chain migration dichotomy (candidate).** Let `P` have width at most three and contain a proper autonomous chain `M`, with `Q=P\M` nonchain. Then either
> 
> (A) some incomparable pair with one endpoint in `M` is balanced in `P`, or
> 
> (B) some incomparable pair `x,y in Q` that is balanced under the uniform law of `Q` remains balanced under the exact binomially tilted law induced from `P`.

If this candidate is proved, no cardinality-minimal POS3 counterexample can contain a proper autonomous chain: minimality supplies a uniform-balanced pair in `Q`, and either branch contradicts that `P` is a counterexample. Combined with account04/B19, this would make the minimal counterexample fully module-prime.

Two tempting stronger statements are false; the next two sections show that both branches of the candidate are genuinely needed.

## 7. Named partner application: quotient balance can be destroyed

Apply Theorem 3.1 to the exact 9-element account03/B19 certificate with covers

`0<2, 0<3, 0<4, 1<4, 2<5, 3<6, 4<7, 4<8, 5<8, 6<8`.

The chain

`M={2<5}`

is autonomous. Relative to `M`, `D={0}`, `U={8}`, and

`I={1,3,4,6,7}`.

Deleting `M` gives a 7-element quotient/remainder `Q` with exactly `25` linear extensions. The active-corridor data are

`r=3`: 3 quotient extensions, weight `binom(5,2)=10`;

`r=4`: 12 quotient extensions, weight `binom(6,2)=15`;

`r=5`: 10 quotient extensions, weight `binom(7,2)=21`.

Thus

`3*10 + 12*15 + 10*21 = 420 = e(P)`,

recovering the partner's exact extension count from the new binomial law.

More importantly, in the **uniform** quotient law,

`Pr_Q(0<1)=16/25`,

which is balanced. After expanding the autonomous chain, the exact binomial tilt gives

`Pr_P(0<1)=5/7 > 2/3`.

So even this concrete autonomous-chain contraction destroys a balanced outside pair. Fixed-pair quotient preservation is false, consistent with the fresh account02/B19 infinite family.

But the same partner poset has

`Pr_P(2<3)=1/2`.

Thus branch (A) of the migration dichotomy rescues this example exactly where branch (B) fails. This is a direct new use of the named partner's source-valid certificate.

## 8. Complementary exact adversary: a module need not have a balanced cross pair

The converse shortcut is also false. Let `P_7` have elements `0,...,6` and Hasse covers

`0<1, 1<2, 2<5, 3<5, 5<6`,

with element `4` otherwise isolated. Then

`M={5<6}`

is an autonomous chain: `0,1,2,3` are below every member of `M`, while `4` is incomparable with both members. The poset has width exactly three, connected incomparability graph, and exactly `28` linear extensions.

Here `Q=P_7\M` has `20` linear extensions. The corridor length is `0` on 16 quotient extensions (weight 1) and `1` on 4 quotient extensions (weight 3), giving

`16*1+4*3=28`.

The only module/incomparable-outside pairs are unbalanced:

`Pr(5<4)=2/7`,

`Pr(6<4)=1/7`.

Thus the stronger claim “every autonomous chain has a balanced cross pair” is false even with width three and connected incomparability graph.

Nevertheless the quotient pair `(1,3)` has

`Pr_Q(1<3)=1/2`

and remains

`Pr_P(1<3)=1/2`.

So branch (B) rescues this example exactly where branch (A) fails. The two exact adversaries therefore support the need for a migration *dichotomy*, rather than either one-sided shortcut.

## 9. Development-only exact stress test of the candidate dichotomy

The companion standard-library verifier does three things:

1. checks the named partner 9-point calculations above;
2. checks the 7-point complementary adversary above;
3. exhaustively generates naturally labelled quotient posets `Q` through 5 elements, all isotone `D/I/U` type assignments with `I` nonempty, and module lengths `m=2,3`; after full transitive closure it retains only width-at-most-three instances with connected incomparability graph, and checks both rescue branches exactly.

The run examined `28,550` generated structured instances (not claimed to be 28,550 nonisomorphic independent posets). Results:

- `28,316` had a balanced module/outside pair (branch A);
- `234` lacked such a cross pair but had a uniform-balanced quotient pair that remained balanced after expansion (branch B);
- `0` failed both branches.

This is finite regression/adversarial evidence only; it is **not** an arbitrary-size proof of the migration dichotomy and is not counted as closure of POS3.

The final executable terminated with

`POS3_AUTONOMOUS_CHAIN_BINOMIAL_CHECK_PASS`.

Execution SHA-256 values:

- script: `29c739af21f90a0e557e8d9798bf90474fb8068dfdc038d1c80969c121d61cb2`;
- output: `54ee56dbe13aded7e771522b2648871cba5e715798bb4fd9d29970dc11104fda`.

An initial regression attempt correctly tripped an assertion because the harness fed the pre-expansion `Q` relation rather than the induced `Q=P\M` relation after transitive closure; expanding `M` forces additional `D<U` relations. The harness was corrected, the theorem statement was not weakened, and the complete final suite was rerun successfully. `TEST_NOTES.md` records this without preserving environment-specific stack text.

## 10. Integration with the campaign lead

The lead's fresh theorem says that every element of any true no-balanced width-three candidate has `>E/81` extensions at its common-majority rank. The present theorem is orthogonal and complementary:

- in the **chain-module branch**, all module deletion bias is exactly the scalar binomial tilt `binom(m+r,m)`, and absence of module-cross balance forces a `>1/3` heavy module gap for every `z in I`;
- if the migration dichotomy eliminates that branch, the residual minimal counterexample is module-prime, incomparability-connected, width exactly three, at least 15 elements by the inherited frontier, and subject simultaneously to the lead's `>E/81` pinned central cells, the existing `>E/3` heavy marginals, and the global double-blocker/majority-block constraints.

So the new reduction cleanly separates the still-unpaid induction issue from the module-prime alignment issue rather than mixing their probability laws.

## 11. Claim status

- Exact autonomous-chain binomial fiber `W_M(tau)=binom(m+r(tau),m)`: **PROVED**.
- Exact scalar projected law on `Q`: **PROVED**.
- Exact cross-pair shuffle kernel: **PROVED**.
- In a no-balanced candidate, every `z in I` has a module-gap atom `>1/3`: **PROVED**.
- In a minimal counterexample with a proper autonomous chain, `Q` is nonchain, `r(tau)` is nonconstant, and every uniform-balanced quotient pair must be destroyed by the same scalar binomial tilt: **PROVED**.
- Fixed quotient-pair preservation under chain expansion: **REFUTED**, including directly on the named partner's 9-point certificate.
- “Autonomous chain always has a balanced cross pair”: **REFUTED** by the exact 7-point example above.
- Autonomous-chain migration dichotomy: **OPEN CANDIDATE**, with 28,550 exact generated structured instances and zero failures; finite evidence is not closure.
- Parent POS3 target: **OPEN / NOT PROVED**.

No novelty or priority claim is made. No benchmark gold, held-out labels, credentials, scheduler identifiers, machine paths, unrelated private data/transcripts, email, Drive, paid API/model/Codex, remote workflow, permission change, or public posting was used.
