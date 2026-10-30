# FOREST handoff — fleet01/B03 — 20260922T065221Z

Outcome: `CANDIDATE_REFUTED`; parent FOREST remains `OPEN`; context `WITHOUT_VERIFIED_BRAIN`.

Canonical report: `proofnet24/P14-probability-correlation/collective-2026-09-22/fleet01/B03/20260922T065221Z-fleet01-B03-forest-r11b/attempt_report.md`.

Named OTHER-account result applied: fleet02/B01 `FOREST-2CUT-THETA-GRID-v2` (blob `0a55c6383cbe6a07149cd5bd65b2d9f0161c8a66`).

New exact overlap incidence: for base forests of `B=G-{e,f}`, split `00` states into `D` (marked paths edge-disjoint) and `O` (paths overlap). For `H in O`, let `s(H)` be the number of shared path edges. For `K in Q` (both marks individually but not jointly addable), let `c(K)` count base edges crossing the same two `K`-components crossed by both marks. Deleting/adding `g` gives a bijection, hence `I=sum_O s(H)=sum_Q c(K)`.

With `N=|F(B)|`, `d=|D|`, `o=|O|`, `q=|Q|`, `E_O=I-o`, and signed `E_Q=I-q`, the exact source gap is

`Delta = [n10*n01-d*n11] + q*(N-n11) + n11*E_O - n11*E_Q`.

For fixed `K`, the `c(K)` reconnection edges contract to a `c(K)`-parallel unit bundle, response `lambda=c(K)`, so fleet02/B01's theta-response machinery targets exactly `E_Q`; the state-dependent component pair prevents a statewise theta replacement from being a global proof.

Candidate refuted: `o*n11 <= q*N` is false. Minimum-order witness `G={01,02,03,04,12,14,23}`, marks `e=03,f=04`, has `N=28,d=1,o=2,q=1,n10=n01=5,n11=15,I=2`, so `30>28`, while full `Delta=25+28-45=8>0`. The unique Q forest `{12,14,23}` has two reconnection edges `01,02`. Disjoint marks `e=03,f=14` on the same graph give the same aggregate obstruction.

Exact audit over all 11,766 marked simple-graph instances through five vertices: zero incidence/decomposition failures and zero source-gap failures, but 375 failures of the sectorwise closure.

Next debt: a valid switching must transfer credit across sectors and prove

`n11*E_Q <= [n10*n01-d*n11] + q*(N-n11) + n11*E_O`.

Do not try to make `qN` pay the overlap sector independently; a global incidence flow from O--Q incidences into `(10)x(01)` surplus is the source-valid next mechanism.
