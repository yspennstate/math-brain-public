# POS3 handoff — account02/B10 one-distinguisher balance theorem

Run: `B10-20260922T024630Z-pos3-r13`  
Outcome: `ESSENTIAL_STEP_APPLIED`; parent POS3 remains **OPEN / NOT PROVED**.  
Source report: `proofnet24/collective-POS3/account02/B10/B10-20260922T024630Z-pos3-r13/REPORT.md`, creation commit `323a69741a233c0341a9bc047e850f210f76e102` in `yspennstate/math-open-problems`.

## Inputs actually applied

- Campaign lead account04/B10 `20260922T011127Z-account04-B10-POS3-r11`, report blob `1e5a9682e4f90f38484a86e7199428de0b0160f8` (`>1/81` pinned strong-majority-rank atom).
- Named partner account03/B11 `B11-20260922T021330Z-pos3`, report blob `84167cd7b3a69dc8e4c699fc5ca0e5c9ba5e4a8d` (exact two-gap fibers; 121-extension two-distinguisher witness).
- Partner predecessor account03/B11 `20260922T011439Z-account03-B11-pos3-r12`, report blob `3443c6ccc4436b9eaf060884c4eec6fc85dc1792` (first-boundary two Hasse blockers; every blocker-sibling distinguisher lies strictly after `B_2`).
- account02/B10 predecessor blob `acdb868b3e35a9248d494126311bfff3bfee150b` (both endpoint Hasse flow channels active).

## New theorem

Let `a,b` be incomparable in any finite poset. If exactly one vertex distinguishes their poset relations, then

`1/3 <= Pr(a precedes b) <= 2/3`

under the uniform law on all linear extensions.

After swap/order dual, write the unique distinguisher as `a<z`, `b||z`. Delete `{a,b,z}` and fix an arbitrary extension skeleton `tau` of the remainder. Since every remaining vertex sees `a,b` identically, their admissible insertion intervals coincide: after shifting, `I_a=I_b={0,...,m-1}`. The relation `a<z` forces `I_z={d,...,m-1+e}` with `d,e>=0`.

For the three possible relative orders let the exact lift counts be

- `B_tau`: `b<a<z`,
- `C_tau`: `a<b<z`,
- `D_tau`: `a<z<b`.

Then exact gap counting gives `B_tau=C_tau`. Also

`D_tau = sum_{k=d}^{m-1}(k+1)(m-k)`

(with value zero when `d>=m`), whereas

`C_tau = sum_{j=0}^{m-1}(j+1) #{k in I_z:k>=j}`.

For every `j>=d`, the latter multiplicity is `m+e-j >= m-j`, hence `D_tau<=C_tau` fiberwise. Summing over all skeletons without reweighting gives

`N(b<a)=C`, `N(a<b)=C+D`, `0<=D<=C`,

so `1/2<=Pr(a<b)<=2/3` in this orientation. Symmetries cover the other unique-distinguisher types. Zero distinguishers gives the usual label-swap probability `1/2`.

## Endpoint consequence

In any no-balanced-pair poset, **every incomparable pair has at least two distinguishers**. Therefore the account03/B11 first-boundary blocker siblings `s_1,s_2` have at least **two distinct** distinguishers, and every one of them lies strictly after the whole second majority block `B_2`. Dually the last-boundary sibling pair has at least two distinct delayed distinguishers before the penultimate block.

This combines with the account02/B10 predecessor: the first endpoint has both Hasse deletion-flow channels active **and** at least two distinct later structural distinguisher channels.

The count `>=2` is sharp from current local information. The partner's exact 121-extension witness has precisely two distinguisher vertices `{4,5}` for `(3,6)` and `Pr(3<6)=82/121>2/3`; it is not a POS3 counterexample because it has a balanced escape pair.

## Next exact obligation

Couple the **two active endpoint Hasse flows** to the **at least two delayed blocker-sibling distinguishers** through the next adjacent strong-majority boundary, with the original linear-extension multiplicities retained. Force one of: a balanced pair, a four-antichain, or a proper autonomous nonchain. One-fork/one-distinguisher closures are now eliminated.

Exact verifier/output in the source run folder ends with `POS3_ONE_DISTINGUISHER_BALANCE_REGRESSION_PASS`. No novelty claim, no finite-census closure, and no induced-uniform-law substitution is made.
