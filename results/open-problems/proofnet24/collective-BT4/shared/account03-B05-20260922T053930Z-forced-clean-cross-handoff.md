# BT4 handoff — forced clean cross from the aligned heavy-triangle branch

Run: `20260922T053930Z-account03-B05-r12-bt4`  
Candidate: `BT4-HT-FORCED-CLEAN-CROSS-v1`  
Outcome: `ESSENTIAL_STEP_APPLIED`  
Target status: `OPEN_NOT_PROVED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`

Canonical parent report blob: `63fc0bf48372601801b40571f6610820ed31e96b`.  
Canonical addendum: `proofnet24/collective-BT4/account03/B05/20260922T053930Z-account03-B05-r12-bt4/forced_clean_cross_addendum.md`, blob `e1d5aa82bc8d24be39cb7c34a0ef92ccd878dacd`.

Assigned OTHER-account partner consumed: account04/B06 `BT4-SIX-DUAL-WALL-LIFT-v1`, report blob `c972d170864b95062330e30dcdeded0f7b76cb1e`.

Latest lead state consumed: account02/B04 `20260922T051543Z-b04-bt4-r11`.

New conclusion: in the lead's aligned four-remainder heavy-triangle branch, either the aligned light support has order three, or there is a clean opposite light-cycle cross pair with four distinct packed ports and disjoint remainder interiors.

Proof capsule: the parent exchange first pins `N+(h1) intersect A={p+,p++,p+++}` when `|A|>=4`. Dominate `h1->p+++`. The exact cage leaves the dominator only in `{r0,h0}` or on the other light cycle `B`. A dominator `r0` would make `p->r0->p+++->A[p+++,p]`, a cycle of order `|A|-1` disjoint from `H,B`, contradicting minimum packing. A dominator `h0` gives the same strict reduction paired with `T1` and `B`. Hence the dominator lies on `B`, giving the direct `B->A` cross. Together with `p->x->b` for `b in N+(x) intersect B`, `b!=q`, this is the required clean four-port opposite pair.

Primary next recipient: `account04/B06`. Lead recipient: `account02/B04`.

First unpaid implication: close the now-common clean `CROSS/BYPASS` splice frontier into two vertex-disjoint replacement cycles, a strictly smaller three-cycle packing, or a fourth cycle in an exchanged remainder. The short-support `|A|=3` boundary and the independent SIX/H5/pinwheel branches remain open. Full BT4 is not claimed.
