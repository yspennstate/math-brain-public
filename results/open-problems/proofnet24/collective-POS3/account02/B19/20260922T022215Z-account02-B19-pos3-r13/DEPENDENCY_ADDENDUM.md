# B19 POS3 r13 late dependency addendum — exact ideal-block transfer adversary

The initial immutable `REPORT.md` was already written when the newest named-partner handoff arrived on `math-research-brain` main. I did not rewrite that report. This append-only addendum consumes and applies the later dependency.

## Newest named partner actually consumed

account03/B10 handoff `account03-B10-20260922T0214Z-explicit-variance-residue.md`, Git blob `b3d822d616c5d4cdbde17c6e340867465e0c7219`, binds canonical scientific report commit `74c9f4506b5cdb47f0418c8ab8a3de0934abfa8b`, report blob `3e50b4d0adaa18c79a96079139d660b832418a2d`. Its newest exact conclusions include: every hypothetical POS3 counterexample has rank variance `<6560` everywhere and `<65/16` on first/last strong-majority blocks; and the live next obligation is still **ideal-block weighted balance transfer / two-fringe charge** under the exact projected weight `W_C`, not a uniform projected law.

I also consumed the later account01/B19 ideal-block handoff blob `f1f0eacfcb9f4d908947b7b640944ed6d7b69b34`. It proves that deleting the first ideal majority chain produces exact one-sided weights `W_C`, a uniform component plus non-prefix component, and a rank-one adjacent-swap commutator. Its stated residual IBWT is: if a uniformly balanced quotient pair is pushed outside `[1/3,2/3]` by `W_C`, force a balanced pair touching the deleted chain.

## Direct application of those results to the new family

In the r13 family `P_m`, the chain

`I_m={b<c_1<...<c_m}`

is an **order ideal chain**. Delete it. The quotient `Q` has elements `{a,x,d,e}` with relations

`a<d`, `a<e`, `x<d`.

Its five uniform linear extensions are

1. `a x d e`,
2. `a x e d`,
3. `a e x d`,
4. `x a d e`,
5. `x a e d`.

Thus under the genuine uniform law on `L(Q)`,

`nu(a<x)=3/5`, `nu(d<e)=2/5`, `nu(x<e)=4/5`.

Specializing the exact ideal-chain insertion recurrence gives the five lift weights

`w1=(m+1)(m+4)/2`,

`w2=w3=(m+1)(m+2)(m+6)/6`,

`w4=(m+1)(m+2)/2`,

`w5=(m+1)(m+2)(m+3)/6`.

Their sum is exactly

`(m+1)(m^2+9m+16)/2 = e(P_m)`.

Therefore the exact weighted projected law is the actual uniform law of `P_m` after forgetting `I_m`; no biased law has been replaced by a uniform surrogate. Under this exact weight,

`mu(a<x)=(2m^2+19m+36)/(3(m^2+9m+16)) > 2/3`,

while

`mu(d<e)=2(m+3)/(m^2+9m+16) < 1/3`.

So **both** quotient-balanced pairs `a||x` and `d||e` are pushed out of the balance band by the exact deletion weight. The IBWT alternative is realized only by pairs touching the deleted chain.

But the main r13 theorem shows those chain-touching balanced pairs can first occur at depth asymptotic to

`alpha_* m`,  `alpha_*=1-sqrt(2/3)=0.183503...`

from the endpoint. Hence this family is an exact adversary to any proof of IBWT that attempts to charge only `O(1)` first interruptions or, more generally, only an `o(m)` endpoint fringe.

This **does not refute IBWT itself** and is not a POS3 counterexample. The hypothetical-counterexample hypotheses used by account03/B10/account01/B19 impose additional strong-majority and no-balanced-touching constraints that `P_m` does not satisfy. The correct consequence is narrower and useful:

> Any valid ideal-block weighted-transfer proof must either exploit those counterexample-specific constraints in an essential way, or control a genuinely global/linear-depth portion of the deleted-chain corridor. Purely combinatorial bounded-fringe charging cannot suffice.

This makes the residual from the initial report more source-aligned: the autonomous-chain contraction branch and the current ideal-block weighted-transfer branch meet at the same missing mechanism, a **global weighted corridor crossing/charge**.

## Exact verification

`verify_pos3_ideal_block_projection.py` checks the five lift-weight formulas independently by integer interleaving enumeration for `m=1,...,12`, verifies their sum against `e(P_m)`, and prints the uniform quotient versus exact weighted probabilities at `m=12`.

Verifier SHA-256: `39f5f859a19e37fd83cea2d23ec46a0af57a3c9e68034025ff7e937fc95f9d08`.  
Output SHA-256: `8e5b50a0bcf05738219643c7cde6b8abe4647117666716b39889465ff6fc3cf1`.  
Terminal marker: `POS3_IDEAL_BLOCK_PROJECTION_PASS`.

At `m=12` the five exact weights are `104,546,546,91,455`, summing to `1742`, and the projected probabilities are `nu(a<x)=3/5 -> mu(a<x)=46/67`, `nu(d<e)=2/5 -> mu(d<e)=15/134`, `nu(x<e)=4/5 -> mu(x<e)=46/67`.

**Classification remains `CANDIDATE_REFUTED`** for bounded-depth/local migration and bounded-fringe weighted-transfer selectors. Parent POS3 remains OPEN.
