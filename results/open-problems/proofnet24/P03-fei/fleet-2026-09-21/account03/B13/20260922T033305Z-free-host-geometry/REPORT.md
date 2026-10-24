# B13 — changing the Numaro free-host geometry: an exact influence law and a 850,500-gate falsification search

**Outcome:** `AUXILIARY_ONLY / CANDIDATE_REFUTED_AT_TESTED_GEOMETRY_SHELLS`  
**Full unrestricted uniform-cube FEI:** **OPEN / NOT PROVED.**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; authenticated GitHub sources were consumed directly, but no authenticated mathematical-brain retrieval/receiver context was used.

## 1. Exact live target and why this run changes method

The live owner target is the all-gate inequality

\[
\Gamma(p_{\rm out})+\widetilde H_G(p)
\le
\sum_i \operatorname{It}_i(G;p)
\frac{\Gamma(p_i)+h(V_{p_i})}{V_{p_i}},
\qquad V_u=4u(1-u),
\tag{G}
\]

for one symmetric nonnegative finite-cap potential and every Boolean gate/product bias. The source-exact gate-reformulation report proves that this is equivalent to full FEI. At the all-unbiased point of a balanced gate, `(G)` forces

\[
R(G):=\frac{H(G)}{I(G)-1}\le \Gamma(1/2).
\tag{1.1}
\]

The old claim that the two-input AND/read-once center is globally extremal has already been refuted by the certified shared-graft balanced gates, so this run does **not** repeat that settled falsification.

The named other-account result consumed and applied is

`account04/B18/20260922T031308Z-global-shared-core-invariant/REPORT.md`, observed report blob `630d799d165e6d18c67c59cec7421758230e9ee4`.

It proves that at

\[
C^\dagger=6.521851214
\tag{1.2}
\]

the known fixed nine-host shared-core transform is safe for every balanced `C^dagger`-safe input and every source-valid signed singleton, and that arbitrary balanced disjoint composition cannot escape that fixed-core mechanism. Its remaining obligation is to change the host/core geometry, use a stronger prime seed, or move to nonuniform bias.

This run takes the first option. Instead of varying the selected singleton `b` inside the already-closed nine-host operator, it asks whether the **locations and signs of the free host edges themselves** can be changed while retaining an actual balanced monotone Boolean gate.

The exact candidate tested is therefore:

> **FREE-HOST-GEOMETRY-v1.** Keep the published Numaro nine-bit `y=0` outer slice and the same published balanced 18-bit Numaro gadget, but replace the canonical nine host edges by another pairwise compatible collection of individually free outer edges. On each host feed the host pivot into the gadget's same small-influence auxiliary input and give the other 17 gadget inputs fresh variables. Require exact balance and monotonicity. Search for a balanced gate with `R>C^dagger`, equivalently a uniform-bias gate margin larger than the current center.

This is a different source-valid Boolean mechanism from the preceding scalar-`b` semigroup optimization.

## 2. The free-host geometry of the published nine-bit slice

Let `B:{0,1}^9->{-1,1}` be the exact `y=0` slice reconstructed from the published Numaro source table. It is monotone in the source convention and has

\[
\sum_x B(x)=18.
\tag{2.1}
\]

For a coordinate edge `e=(u,u+e_p)`, call `e` **individually free** when replacing both endpoint values by an arbitrary monotone two-state gadget cannot create a monotonicity violation on any of the other incident core edges. Concretely, for every non-pivot edge leaving a host endpoint the fixed upper neighbor must be `-1`, and for every non-pivot edge entering a host endpoint the fixed lower neighbor must be `+1`.

An exact finite enumeration of all `9*256=2304` directed coordinate edges gives exactly **81** individually free edges, split as follows:

\[
\begin{array}{c|c|c|c}
\text{lower Hamming weight} & B\text{ on both endpoints} & \text{count} & \text{role}\\\hline
3 & -1 & 36 & \text{lower negative free edges}\\
4 & +1 & 9 & \text{middle positive free edges}\\
5 & +1 & 36 & \text{upper positive free edges}.
\end{array}
\tag{2.2}
\]

The nine hosts in the published source construction are **exactly all nine** middle positive free edges. Those nine are pairwise compatible and, in fact, have no cross-host adjacency conflict with any of the other 72 free edges. Cross-sign outer edges never conflict; the only conflicts are within the 36 upper edges or within the 36 lower edges.

Thus the source geometry is not the only realizable free-host geometry. There are many exact alternative Boolean constructions to test.

## 3. PROVED: exact influence penalty for every free-host deformation

Let `h` be the published balanced monotone 18-bit source gadget, let

\[
I(h)=\frac{261}{128},\qquad b=\widehat h(\{d\})=\operatorname{Inf}_d(h)=\frac1{256},
\tag{3.1}
\]

where `d` is one of its small-influence auxiliary coordinates, and put `w=1/256`.

For a chosen compatible host set `E`, write `s_e=B(u_e)=B(u_e+e_{p_e}) in {+1,-1}` and let `r_e=|u_e|`. Define

\[
a(x)=B(x)-\sum_{e\in E}s_eP_e(x),
\]

and on host `e` insert a fresh copy of `h` whose distinguished coordinate `d` is the existing pivot `x_{p_e}`. Because the hosts are disjoint and pairwise nonadjacent, the resulting function is Boolean and monotone. Balance is equivalent to

\[
\sum_{e\in E}2s_e=18,
\qquad\text{i.e.}\qquad \#E_+-\#E_-=9.
\tag{3.2}
\]

For one host, `P_e` has singleton Fourier coefficient `w chi_i(u_e)` in every non-pivot coordinate and zero in the pivot, while `Q_e=P_e chi_{p_e}` has singleton coefficient `w` only at the pivot. Hence the change in the **core** singleton sum is

\[
w[-s_e(8-2r_e)+b].
\tag{3.3}
\]

The 17 fresh gadget coordinates contribute

\[
w[I(h)-b].
\tag{3.4}
\]

Since a monotone Boolean function has total influence equal to its singleton Fourier sum in this convention, the `b` terms cancel exactly. Therefore

\[
\boxed{
I(F_E)=I(B)+w\sum_{e\in E}\bigl[I(h)-s_e(8-2r_e)\bigr].
}
\tag{3.5}
\]

For the three free-edge classes in (2.2), the geometric surcharge `-s_e(8-2r_e)` is respectively `2,0,2`. Thus the canonical middle hosts are the unique zero-surcharge free edges.

Parameterize a balanced deformation by:

- `m`: number of canonical middle hosts removed and replaced by upper positive hosts;
- `s`: number of additional upper/lower host pairs.

Then the host count is `9+2s` and (3.5) gives the exact dimension-free identity

\[
\boxed{
I(F_{m,s})-I(F_{0,0})
=\frac{m}{128}+\frac{517s}{16384}.
}
\tag{3.6}
\]

In particular every noncanonical free-host deformation pays a strictly positive influence penalty before any entropy gain is considered. This is an analytic statement for the whole source-valid free-host family, not a numerical observation.

## 4. Decisive finite falsification search in the nearest geometry shells

For every tested geometry the Fourier spectrum was computed from the exact 512-point core formula

\[
\widehat F_{\rm core}
=\widehat B-\sum_{e\in E}s_e\widehat P_e
+b\sum_{e\in E}\widehat Q_e,
\tag{4.1}
\]

while every host has the same exact fresh-coordinate tail. The checker reconstructs the published source table and its hash, classifies all 81 free edges by integer tests, enforces pairwise host compatibility and balance, uses (3.5) as an exact rational influence check, and evaluates the entropy of the compressed spectrum. The entropy sweep is float64 and therefore is reported as a decisive finite computation, **not** an interval certificate or a universal theorem. The separation from the canonical gate is orders of magnitude larger than roundoff.

I exhaustively evaluated **850,500 distinct actual balanced monotone Boolean gates** in six nearest deformation shells:

| shell | exact geometry | gates | best `H` | exact `I` | best `R=H/(I-1)` | old-reference `c_G=4(R-6.4548)` |
|---|---|---:|---:|---:|---:|---:|
| canonical | `m=0,s=0` | 1 | 7.014850042680291 | 2.075592041015625 | **6.521850083658612** | **0.268200334634450** |
| A1 | replace 1 middle by 1 upper | 324 | 7.019574248206868 | 2.083404541015625 | 6.479181120679492 | 0.097524482717969 |
| A2 | replace 2 by 2 compatible uppers | 19,440 | 7.027098963956537 | 2.091217041015625 | 6.439689539137171 | -0.060441843451315 |
| A3 | replace 3 by 3 compatible uppers | 362,880 | 7.030526577870698 | 2.099029541015625 | 6.397031485954156 | -0.231074056183374 |
| B1 | add 1 upper + 1 lower | 1,296 | 7.140936411493676 | 2.107147216796875 | 6.449852651170782 | -0.019789395316870 |
| B2 | add 2 compatible uppers + 2 compatible lowers | 291,600 | 7.267248106116009 | 2.138702392578125 | 6.382043414928025 | -0.291026340287900 |
| C11 | remove 1 middle; add 2 uppers + 1 lower | 174,960 | 7.146073272578660 | 2.114959716796875 | 6.409265881917546 | -0.182136472329816 |

The largest noncanonical value in these 850,500 gates is A1,

\[
R_{\rm A1,max}=6.479181120679492,
\tag{4.2}
\]

which is already below the canonical one-step shared graft by

\[
\boxed{0.04266896297912037}.
\tag{4.3}
\]

It is below the current fixed center `C^dagger` by

\[
0.04267009332050797.
\tag{4.4}
\]

The best A1 move removes the canonical host `(393,457)` in pivot 6 and inserts the upper free edge `(451,455)` in pivot 2. The best balanced-pair augmentation inserts upper `(62,63)` in pivot 0 and lower `(161,169)` in pivot 3; it reaches only

\[
R=6.449852651170782.
\]

So the extra entropy created by these natural geometry perturbations does not remotely pay the exact influence surcharge (3.6).

### What was refuted

The claim

> “The current fixed-core scalar ceiling can likely be escaped merely by relocating a few free host edges within the same published nine-bit Numaro outer slice, while keeping the same balanced source gadget and uniform bias.”

is **REFUTED for the six exhaustive geometry shells above**. It is not refuted for every possible compatible free-host set, for a different outer core, for different local gadgets on different hosts, or for nonuniform input bias.

## 5. A second changed mechanism tested and found worse

I also tested a different source-valid way to reuse another existing coordinate: on selected host pairs, restrict one additional source-gadget coordinate to `+1` or `-1` in balance-preserving pairs rather than keeping every local gadget balanced. The exact compressed formula is

\[
\widehat F_{\rm core}
=\widehat A+b_u\sum_j\widehat Q_j
+\sum_j \sigma_j(c_v\widehat P_j+d_{uv}\widehat Q_j),
\tag{5.1}
\]

where `c_v=\widehat h({v})`, `d_uv=\widehat h({u,v})`, and the signs/restrictions are paired so the total mean remains zero. Exhaustive checks over all nine small-influence choices `u`, every second coordinate `v`, and all paired restriction patterns with up to four `+/-` pairs found the original un-restricted shared graft strictly best. For the best second-coordinate pair `(u,v)=(9,10)`, the best ratios for 0,1,2,3,4 restriction pairs were

\[
6.521850083658612,
6.521794459042285,
6.521738824342346,
6.521683169225980,
6.521627508650685.
\tag{5.2}
\]

This second search is exploratory float computation and is not part of the 850,500-shell count or an interval certificate. It rules out another obvious “reuse one more core coordinate” escape before investing in a larger construction.

## 6. Exact old/new implication and next attack

- `exact_candidate_version`: all-gate `(G)` with the current fixed-center candidate `C^dagger=6.521851214`; this run tests the necessary balanced-uniform condition on changed Numaro host geometry.
- `prior_missing_implication`: account04/B18 closes the same fixed nine-host transform and explicitly leaves changed host/core geometry and arbitrary prime gates open.
- `consumed_peer_artifact`: `account04/B18/20260922T031308Z-global-shared-core-invariant/REPORT.md`, blob `630d799d165e6d18c67c59cec7421758230e9ee4`.
- `applied_to_claim`: rather than re-optimize its scalar `b`, I changed the actual source host geometry and derived the exact influence law (3.5)-(3.6), then searched source-valid Boolean gates in six exhaustive nearby geometry shells.
- `new_proved_inference`: equation (3.5), including the exact surcharge (3.6), for every compatible free-host deformation of this source slice; exact finite classification (2.2) of its 81 individually free edges.
- `exact_failed_claim`: small free-host relocation/augmentation within this outer slice would produce a stronger balanced-uniform obstruction. Refuted on 850,500 explicit gates in the enumerated shells; this remains a finite-family statement.
- `replacement_obligation`: change the outer core itself or use genuinely heterogeneous high-quality local gadgets, or move to nonuniform bias. Repeating fixed-core scalar optimization or the nearest free-host relocations is not promising.
- `remaining_implication`: prove `(G)` for arbitrary composition-prime Boolean gates/all interior biases with one finite-cap potential, or find a stronger source-valid gate/bias obstruction. Full FEI is still open.
- `next_recipient`: primary `account03/B18` (all-gate integrator), secondary `account04/B18` (fixed-core closure owner) and `account03/B17` (construction adversary).
- `full_problem_change`: **OPEN -> OPEN**. This is a structural payment plus a substantive falsification search, not a universal FEI upper bound.

## 7. Verification and scope

`CHECKER.py` reconstructs the published source from its source-table slices, verifies the published truth-table SHA-256, derives the free-edge classification and pair compatibility by integer tests, reconstructs the compressed Fourier spectra, checks the exact influence surcharge against the Fourier calculation, and enumerates the reported shells. `CHECK_OUTPUT.txt` records the executed summary. The entropy maximization is intentionally labelled finite float64 evidence; no novelty/publication-priority claim is made from a search miss.

Scoped privacy review: only mathematical formulas, published-source reconstruction constants, sanitized repository-relative provenance, and nonsecret content hashes are present. No credentials, scheduler identifiers, machine paths, raw private transcripts, benchmark gold, unrelated private data, email/Drive action, paid model/API/Codex call, workflow dispatch, permission change, or public-release action is included.
