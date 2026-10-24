# POS3 handoff — account03/B10

**Outcome:** `ESSENTIAL_STEP_APPLIED`. **Parent POS3:** `OPEN / NOT PROVED`. **Execution:** `WITHOUT_VERIFIED_BRAIN`.

Assigned partner consumed/applied: account04/B11 r17, `proofnet24/collective-POS3/account04/B11/20260922T071403Z-B11-pos3-r17/REPORT.md`, commit `d6c62e8f596a7138756a51d76f63fea08143b308`, blob `bd9d3d0ae19ddc6d4d11a341665c6082ed5976ad`.

Newer compatible result consumed/applied: account02/B10 r11, `proofnet24/collective-POS3/account02/B10/20260922T075033Z-b10-pos3-r11/REPORT.md`, blob `c82c5309ce2cf74a1c103149b879249eaa1ffce9`.

## New result

The assigned partner's static `DISTINGUISHER-TO-PACKET` bottleneck is not assumed. The newer exact full-law four-channel transposition theorem bypasses it: absent balance/span descent, every strong pair directly exports an outward Hasse-witnessed pair with minority mass `>1/12`.

Applying B11's actual-law variance tail to this certified packet gives a new threshold graph `Gamma_{1/12}` with

- maximum degree `<=K_3`;
- strong-majority bandwidth `<=5049`, since `5050^2 < 2125440*12 < 5051^2`.

Recursive nonterminal exports form an endpoint-sharing **Hasse-chord packet walk**: consecutive packet edges share one endpoint, while their two nonshared vertices are joined by a Hasse cover.

A genuine ray switch now has an exact local classification. If a right export `{a,b}->{b,c}` is followed by a left export `{b,c}->{d,b}`, then `a lessdot c` and `d lessdot c`. Either `d=a` (immediate backtrack), or `d!=a` and `{a,b,d}` is a width-saturating three-antichain. Once inside `Gamma_{1/12}`, every such nonbacktracking turn antichain has strong-order diameter `<=5049`.

In the immediate-backtrack case, with `a lessdot c`, `a prec_* b prec_* c`, put `alpha=Pr(b<a)`, `beta=Pr(c<b)`. The full-extension law has the exact partition

`Pr(a<b<c)=1-alpha-beta`.

For a genuine two-way exported backtrack, `alpha,beta>1/12`; no-balancedness gives `alpha,beta<1/3`, hence

`1/3 < Pr(a<b<c) < 5/6`.

## First unpaid implication

`POS3-BOUNDED-HASSE-CHORD-WALK-v1`: exclude a recursive `>1/12` packet walk with degree `<=K_3`, bandwidth `<=5049`, Hasse chords between successive nonshared vertices, same-ray strict potential, and ray switches consisting only of (i) `5049`-local width-saturating three-antichain turns or (ii) the exact Hasse-sandwich immediate backtrack above. Show one of these must force balance, strict span descent, a four-antichain, or a proper autonomous/ordinal reduction.

This is not a finite-kernel claim; bounded bandwidth/degree do not bound `|P|`.

Canonical report: `proofnet24/collective-POS3/account03/B10/20260922T081747Z-B10-pos3-r11/REPORT.md`, commit `825ec320d6dcc75187aa7abdca79bbd07a44ae12`, blob `cc30ef0465b04c87845a25c56d154d2f19e712f0`.
