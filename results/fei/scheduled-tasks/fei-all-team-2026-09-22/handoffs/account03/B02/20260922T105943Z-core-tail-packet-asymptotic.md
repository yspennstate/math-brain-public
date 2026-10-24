# account03/B02 handoff — core-tail packet asymptotic

Programme `FEI-ALL-TEAM-20260922T095941Z`; control revision `2026-09-22.3`; execution `WITHOUT_VERIFIED_BRAIN`; full FEI remains **OPEN**.

## New theorem
Fix all product biases except a tail coordinate `j`, write `u=1-2p_j`, and take the exact conditional Walsh packet at `u=0`:

`Ghat_u(S)=a_S+u b_S`, `Ghat_u(S+j)=sqrt(1-u^2) b_S`.

Let `beta=sum b_S^2`, `beta_dark=sum_{a_S=0} b_S^2`, and `beta_bright=beta-beta_dark`. Then the exact gate defect has the one-sided expansion

`D(u)=D(0)+ell_+ u + beta_bright u^2 log2(1/u^2)+O(u^2)` for `u->0+`,

and

`D(-v)=D(0)+ell_- v + beta_bright v^2 log2(1/v^2)+O(v^2)` for `v->0+`.

The sign is exact:

`beta_bright = sum_{a_S != 0} b_S^2 >= 0`.

Reason: the tail multiplier is exactly `It_j/V_j=beta`; its `h2(V_j)=h2(u^2)` payment contributes `+beta u^2 log`, while only dark spectral packets contribute `beta_dark u^2 log` to `Ht`, which enters the defect with a minus sign. Therefore near-unbiased tail entropy cannot itself create a negative hidden logarithmic debt.

## Strong Numaro application
Using the source truth SHA `f8a7bb2c738d86368305111633376b1a3a83d8ee1f1abcc9a37d841b0f9c7839`, core input 1 at `p=223/456`, and low-influence tail input 10 (zero-based bit 9):

- `beta_bright = 1/256`
- `beta_dark = 0`
- `It_tail(0)=1/256`
- `p_out(u)=1019/2048-u/512`
- first derivatives of core influence and total influence at `u=0` vanish exactly.

Applying the **latest** account01/B18 frontier exactly,
`epsilon=56721646463783/2500000000000000`, `lambda=18721807228217/500000000000000`,
the rational-log enclosure gives

- `ell_+ > 0.06107237995`
- `ell_- > 0.08530427322`.

So the strongest one-core Numaro witness becomes locally safer in this tail direction. The existing positive one-core reserve is retained rather than normalized away.

Primary report: `yspennstate/math-open-problems`, `proofnet24/P03-fei/fleet-2026-09-22/account03/B02/20260922T105943Z-core-tail-packet-asymptotic/REPORT.md` (commit `6bb5964cfb28f6bc5b93034694590fc87e2580cd`). Exact checker commit `214c2b687d6508dc60b4a36bf9957fe19d3ce403`; checker output commit `c99d0827a3bb06450498de6df142d32a93304574`; claims commit `bd114c1e071b1bc77f0bb8159646a2c96b8f1502`.

## Corrections / collaboration
A later B01 correction observed before finish refutes only a stronger **fixed positive global K_occ reserve** invariant; this result does not use that invariant and is unaffected. No current-programme artifact or commit existed for assigned partner `account04/B02` at three fresh checks, so no partner result was fabricated or substituted. Recipient `account01/B01` should combine this packet theorem with its current prime-gate strategy; account04/B02 should apply its eventual witness-family constraint result to the exact `beta_bright` / `ell_±` equations above.

## Next step
Rank every noncore Numaro coordinate by the exact triplet `(ell_+, ell_-, beta_bright)`. A two-bias counterexample near an unbiased tail can only come from a sufficiently negative regular one-sided term; the logarithmic entropy term is nonnegative. If all low-influence tails have positive one-sided slopes, switch path-A mechanism rather than probing smaller tail biases.
