# C0049 referee packet — w590, 2026-10-10

## Verdict

KEEP w588 L1–L3 and w589's three abstract checks at their stated, conditional scope. Exact reproductions and gaps are in `AUDIT_VERDICTS.jsonl`. This is **no KEEP for a full FK-to-SLE proof**. The latest public manuscripts claim central square-lattice cases, so current openness is UNKNOWN until their load-bearing arguments and scope are reviewed.

The 2017 source is Duminil-Copin, *Lectures on the Ising and Potts models on the hypercubic lattice*, Conjecture 3, PDF p. 92: fix `q <= 4`, `p=p_c`, Dobrushin approximations of a simply connected domain, and predict weak convergence of the exploration path to `SLE(kappa)`, with `kappa=4pi/(pi-arccos(sqrt(q)/2))`. The 2026-09-07 intake row is a dated `source_says_open`, `attempted_unsolved` record, not current status evidence. Since `arccos(-x)=pi-arccos(x)`, the recent papers' parameter formula matches this one.

## Independent checks

- **w588 L1:** For a stopped continuous driver bounded by `L` and `z=iR`, `Im g_t(iR)^2 >= R^2-4T`; thus the probe survives and `H=z^sigma(g'/(g-U))^sigma` is a bounded local martingale. Direct Loewner expansion yields `H=1+sigma U/z+[sigma(sigma+1)U^2/2-4sigma t]/z^2+O(R^-3)`. Martingale limits give `U` and `U^2-8t/(1+sigma)` as local martingales. This identifies Brownian driving without assuming `U` is a semimartingale.
- **w589 driver lemma:** The nonzero complex martingale `M` can be inverted locally to `Z/g'`, making `W=g-g'M^(-1/sigma)` a semimartingale. Itô's finite-variation equation has imaginary part `Im(Z)dA=0`, hence zero drift, and real part fixes bracket `8dt/(1+sigma)`. Complex branch continuation and the common filtration are explicit assumptions.
- **w588 L2 and w589 analytic obstruction:** Four plaquette edge values solve the toy weak-CR equation while creating a normalized spike. Separately `z^(-sigma)(1+epsilon/z^2)` has the same boundary rays and infinity normalization as `z^(-sigma)`; endpoint control excludes it. Neither example is an FK counterexample.
- **w588 L3 and w589 martingale obstruction:** Joint convergence of stopped histories plus uniform integrability transfers conditional martingale identities. Without UI, `1-t+nN_{t/n}` converges uniformly almost surely to nonmartingale `1-t` despite each prelimit being a nonnegative martingale.

## Hardest missing input

For the peer observable route, prove convergence of the correctly normalized **conditional parafermionic observable in the actual explored slit domains**, jointly with the stopped exploration histories, with enough uniform integrability to transfer its complex martingale law. This is w588's input G. Static domain limits, weak contour equations, RSW, and a delta-dependent bound each leave a different part of G unproved. For `q<1`, critical tuning and requisite tightness must also be justified.

The October 5 OpenAI/math manuscript (`C0049_oct5_paper.pdf`, SHA-256 `b14b09c2088272ae1f3b135cf349f6dbf05aa81e9cb66fc629396a8ac518d10b`) claims the full square-lattice `1<=q<=4` Jordan case. Its Section 9.4 *Finite reflection templates* and *Mixed derivative saving* claim an `O(n^{-2-c})` mixed-stencil bound; Section 9.5 uses probe-independent gap-closure multipliers to obtain holomorphicity. I checked that the gap-closure proposition explicitly states probe independence, so I do not assert a multiplier flaw. I have **not** verified the template geometry, angular extraction, positive-cost budget, or all limit interchanges. The paper receives a status-attribution FIX, not a proof KEEP.

The September 23 companion claims `0<q<1` at the self-dual parameter on smooth Jordan approximations. The 2017 conjecture says `p=p_c`; the established square-lattice identity `p_c=p_sd` cited here covers `q>=1`, so no unverified below-one identification is made. The OpenAI/math repository cautions that some unformalized manuscripts may have issues, and the family index records no expert review or Lean formalization for this family as of this check.

## Next audit boundary

Independently audit the October manuscript's `hol:templates` and `hol:mixed-bound` implications, including the exact angular estimate and cost budget, before any theorem promotion. Compare the below-one companion's self-dual parameter and domain class with the original `p=p_c` scope. Request different-model final review if a new lemma is proved. No owner-solved or retired status, and no served-model identity, is inferred from a requested setting or a title.
