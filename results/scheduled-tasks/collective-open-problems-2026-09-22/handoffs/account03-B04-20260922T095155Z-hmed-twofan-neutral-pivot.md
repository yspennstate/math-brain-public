# account03/B04 -> account04/B05 — BT4 H-mediated two-fan neutral pivot

Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Run: `account03-b04-20260922t095155z-r11`  
Outcome: `ESSENTIAL_STEP_APPLIED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`

## Exact other-account source consumed

Assigned partner `account04/B05`, run `b05-20260922t074314z-r35`, candidate `BT4-R4-DIRECT-3X3-CYCLE-FACTOR-v1`.

Canonical source: `yspennstate/math-open-problems:proofnet24/collective-BT4/account04/B05/b05-20260922t074314z-r35/report.md`  
Exact source blob: `ab5f354238ef330125494b0afa5c8e4799716534`.

Its exact aligned R4 cage and H-mediation alternative were used; no peer PASS label was borrowed.

## New source-bound result

Canonical report: `yspennstate/math-open-problems:proofnet24/collective-BT4/account03/B04/20260922T095155Z-account03-B04-bt4-r11/report.md`  
Creation commit: `654b16561fa76ea629e970253b43f1f87f4481e2`  
Readback blob: `06c33bc5ad285dc15cbd80945534ce87c485e93f`  
Candidate: `BT4-R4-HMED-TWOFAN-NEUTRAL-PIVOT-v1`.

In the exact aligned heavy-triangle cage, the neutral triangle exchange `T0=h0->r0->x->h0` has remainder `{h1,h2,r1,r2}`. Remainder-arc maximality and the five already forced arcs show that `h1` and `r2` are nonadjacent. Together with orientation, the exact cage, the shifted triple `N+(h1) cap A={p+,p++,p+++}`, and exact outdegree seven, this forces exactly two B-neighbors of `h1`.

Using the fixed inport `q->h1`, global minimum of packed order localizes those two targets exactly:

`N+(h1) cap B = {q+,q++}`.

The equality target `q++` yields the size-neutral cycle

`B* = q->h1->q++->B[q++,q]`,

so `(T0,A,B*)` is another minimum-order three-packing with remainder

`R*={h2,r1,r2,q+}`.

Remainder maximality gives `e(R*)<=5`; the three fixed arcs `r1->h2`, `r1->r2`, `h2->r2` imply `d^+_{R*}(q+)<=2`. Old B chordlessness and `h1->q+` give exactly one `q+` outneighbor on `B*`, namely `q++`. Exact outdegree seven therefore gives

`|N+(q+) cap (T0 union A)| = 6-d^+_{R*}(q+) >= 4`.

Hence this H-mediated branch reduces to a SIX-type pair overload, a new fan of size at least three on `T0` or `A`, or the unique balanced residual profile `(2,2,1,2)`.

## Receiver target and first remaining blocker

Primary receiver: `account04/B05`.  
Secondary receiver: BT4 lead `account02/B04`.

Earliest remaining implication: `BT4-R4-HMED-FREED-QPLUS-CLOSE-v1`.

Close the neutral exchanged state `(T0,A,B*)`: apply only source-valid splice machinery to the SIX/heavy-fan alternatives, then eliminate or splice the exact balanced `(2,2,1,2)` freed-`q+` state while preserving literal vertex-disjointness. A valid closure must produce four disjoint directed cycles, a strict smaller three-packing, a cyclic exchanged remainder, or another already-proved campaign exit.

No full BT4 proof or novelty claim is made. No scheduler mutation, cross-account native action, email, Drive, public posting, paid/remote model/API/Codex, credentials, or private transcript material was used.
