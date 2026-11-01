# SIVASHANKAR-2026-REGSUB-EVEN — terminal mathematical handoff

Native slot: `6aa7b53b0858819196d923203522c996`  
Category: HARD OUTSIDE  
Canonical claim: `operations/claims/SIVASHANKAR-2026-REGSUB-EVEN.md`  
Terminal trigger: third source-correct no-movement run after HARD Recovery 2/2; there is no Recovery 3.  
Status: `PARTIAL / SOURCE OPEN / ORDINARY RESEARCH TERMINATED BY PROTOCOL`.

## Exact source target

Varun Sivashankar, *Nearly Spanning Regular Subgraphs*, arXiv:2609.19777v1, Section 5, Conjecture 5.1. For every fixed even integer `k>=4`, with `delta_k(r)` exactly as defined by the source over finite simple `r`-regular graphs,

\[
\delta_k(r)=\Theta_k(r^{-2})
\qquad(r\to\infty\text{ through odd integers}).
\]

The source's written theorem gives `O(k/sqrt(r))`; the source mentions but omits a longer `O_k(log r/r)` flow proof. The omitted proof was never credited as fleet mathematics.

## Frozen metric at terminal handoff

\[
\beta_{\rm even}:=\sup\{\beta\in[0,2]: \forall\text{ fixed even }k\ge4,\ \delta_k(r)\le C_k r^{-\beta}\text{ for all sufficiently large odd }r\}.
\]

Certified before terminal run: `beta_even >= 1/2`.  
Certified after terminal run: `beta_even >= 1/2`.  
Target: `beta_even=2`.  
Recovery state: `2/2 consumed`; no Recovery 3.

## Source-closing reduction that should be preserved

For a connected bridgeless loopless graph `B` with `Delta(B)<=r`, define

\[
D_r(B)=\sum_{v\in V(B)}(r-d_B(v)),\qquad g_k(B)=|V(B)|-f_k(B).
\]

The source closes if one proves the uniform local repair theorem

\[
\boxed{g_k(B)\le C_k\frac{D_r(B)}r.}\tag{LOCAL-REPAIR}
\]

After deleting bridges in an `r`-regular graph, the bridge-block deficiencies sum to twice the number of bridges. Combined with the preserved O-West bridge estimate, LOCAL-REPAIR yields total uncovered fraction `O_k(r^-2)`, which together with Sivashankar's lower construction gives the source `Theta_k(r^-2)` statement.

## Reusable proved mechanisms

1. **Spanning threshold.** If `k` is even, `r>2k`, `B` is connected bridgeless loopless with `Delta(B)<=r`, and `D_r(B)<=r-2k`, then `B` has a spanning `k`-factor.
2. **Exact signed barrier formulation.** For disjoint `S,T`,
   \[
   \operatorname{def}_k(S,T)=k(|T|-|S|)-d_{B-S}(T)+q(S,T),
   \]
   and because `k` is even,
   \[
   g_k(B)=\min\{|X|:k(|X\cap T|-|X\cap S|)\ge\operatorname{def}_k(S,T)\ \forall S\cap T=\varnothing\}.
   \]
3. **Fractional signed repair.** The all-signed LP has the explicit feasible point `x_v=(r-d_B(v))/r`, so `LP_k(B)<=D_r(B)/r`. The older `s/(r-2k)` all-row claim is false and must never be revived.
4. **First-scale quantization.** Put `R=r-2k`. If `R<D_r(B)<=2R`, every positive barrier has `|T|-|S|=1`, `d-q` is even in `{0,2,...,k-2}`, and every positive integral row has unit signed demand. The all-signed integer demand is `rho_k(S,T)=ceil(def_k(S,T)/k)`.
5. **Realizability restrictions.** Genuine first-scale barriers obey stronger graph-incidence restrictions than scalar deficiency summaries; literal common-negative majority blowups are impossible. Exact nontrivial zero-slack rows sit on genuine two-edge-cut cactus structure.
6. **Clean exact one-cycle theorem.** In the clean single-gap even-cycle exact-zero-slack cactus subsystem, graph incidence allows at most two exact gap atoms, and all exact rows plus their reverses admit an integral repair of size at most two. This is restricted and does not imply LOCAL-REPAIR.

## Final-run B7 theorem: exact excess decomposition

For a disjoint pair `(S,T)`, let `U=V(B)\(S\cup T)`. For every connected component `C` of `B[U]`, write

\[
t_C=e(C,T),\qquad s_C=e(C,S),
\]

and set `m_T=e(B[T])`, `m_S=e(B[S])`. Let `q_T` be the number of `U`-components with odd `t_C`, and `q_S` the number with odd `s_C`. Then

\[
\boxed{\frac{d_{B-S}(T)-q_T}{2}=m_T+\sum_C\left\lfloor\frac{t_C}{2}\right\rfloor.}\tag{E_T}
\]

The reverse identity is

\[
\boxed{\frac{d_{B-T}(S)-q_S}{2}=m_S+\sum_C\left\lfloor\frac{s_C}{2}\right\rfloor.}\tag{E_S}
\]

These are identities, not estimates: `d_{B-S}(T)=2m_T+sum_C t_C`, and subtracting the parity count removes exactly one from each odd `t_C`.

Consequences for `e_T=(d_{B-S}(T)-q_T)/2`:

- `m_T<=e_T`;
- at most `e_T` components have `t_C>=2`;
- every other `T`-touched `U` component has `t_C=1`.

The same statements hold on the `S` side with `e_S`.

### Two-sided near-tight rows are exact cactus plus O_k(1) defects

Suppose a nontrivial height-zero row has `2e_T<k` and its reverse also has `2e_S<k`. Then both integerized row demands are zero. Hence any all-signed feasible omitted set must satisfy

\[
|X\cap T|=|X\cap S|.
\]

Moreover there are at most `e_T+e_S=O_k(1)` `U`-components on which either `t_C>=2` or `s_C>=2`, and `m_T+m_S<=e_T+e_S`. On every other component touching `S\cup T`, `t_C,s_C\in\{0,1\}`. Bridgelessness excludes `(t_C,s_C)=(1,0)` and `(0,1)`, because the unique boundary edge would be a bridge; connectedness excludes `(0,0)` for a nontrivial row. Therefore every nonexceptional component has

\[
(t_C,s_C)=(1,1),
\]

so the two-sided near-tight row is an exact two-edge-cut cactus row plus only `O_k(1)` exceptional incidence/internal-edge defects.

This is the strongest clean stability statement obtained by the final campaign.

## Final-run B7 obstruction: one-sided excess is not a finite defect parameter

The same conclusion is false if only one signed orientation has small excess. Let odd `r>=4k+1` and

\[
B=K_{r-1,r}
\]

with parts `L` of size `r-1` and `R` of size `r`. Then `B` is finite, simple, connected, bridgeless, `Delta(B)=r`, and

\[
D_r(B)=r,
\]

so it lies in FIRST-SCALE because `r-2k<r<=2(r-2k)`.

Choose `u in R` and

\[
S=L,\qquad T=R\setminus\{u\},\qquad U=\{u\}.
\]

Then `|S|=|T|`, while deleting `S` leaves no edges incident to `T`. Thus

\[
d_{B-S}(T)=q_T=0,\qquad e_T=0,\qquad \rho_k(S,T)=0.
\]

However

\[
e(S,U)=r-1.
\]

For the reverse row, `d_{B-T}(S)=r-1`; since `r` is odd, `r-1` is even and `q_S=0`, hence

\[
e_S=\frac{r-1}{2}=\Theta(r).
\]

Therefore one-sided `e_T=O_k(1)` does **not** imply an `O_k(1)` boundary-incidence state space or proximity to a minimum/minimum+1 cut in the ordinary cut-cardinality sense. The example is not a source counterexample and does not refute first-scale rounding; it refutes the proposed finite-defect reduction based on one-sided `d-q` alone.

## B16 outcome

No finite checker was built. The symbolic B7 analysis shows that the full `h=0, rho=0` class does not reduce to a finite state space as a function of one-sided `e=(d-q)/2`: the `K_{r-1,r}` family has `e_T=0` but `Theta(r)` opposite boundary. Enumerating a finite two-sided subclass would be a restricted exercise and would not address the source-level obstruction. Under the 90/10 rule, checker churn was therefore rejected.

## B22 literature transfer and exact mismatch

The nearest structural tools organize **actual cut cardinality**:

- Dinitz-Nutov, STOC 1995, *A 2-level cactus model for the system of minimum and minimum+1 edge-cuts in a graph and its incremental maintenance*;
- Cornelsen-Dinitz-Wagner (2001), planarity/representation work for the 2-level cactus;
- Ghanbari-Šámal (2026), *A Near-Linear-Time Algorithm for Finding a Well-Spread Perfect Matching in Bridgeless Cubic Graphs*, using a cactus representation of genuine 2-edge-cuts.

The final `K_{r-1,r}` row shows the precise transfer failure: the signed factor parameter `d_{B-S}(T)-q_T` can be zero while the opposite boundary has size `r-1`. Thus a min/min+1 cut representation cannot by itself encode all dangerous `rho=0` signed rows. What is missing is a **one-sided signed-barrier stability/rounding theorem** that uses the complete family of reverse and nonpositive rows, not merely near-mincut geometry.

## Exact remaining blocker

A future reassignment should not restart with generic cactus or scalar-deficiency arguments. The surviving local problem is:

> Control the one-sided height-zero signed rows for which `rho_k(S,T)=0` and `(d_{B-S}(T)-q_T)=O_k(1)` but the reverse excess may be `Theta(r)`, simultaneously with the two-sided cactus-like rows, by an `O_k(D_r(B)/r)` integral support set; or construct a genuine source-valid family showing this is impossible.

A minimal first-scale decision problem is whether an `O_k(1)` repair for the two-sided near-tight cactus core can always be chosen so that every one-sided `rho=0` row remains nonnegative. A failure must be graph-realizable; abstract signed clutters do not suffice.

## Exhausted method/recovery map

Substantive method triples used on this source:

`B2/B11/B25`; `B3/B19/B30`; `B4/B24/B27`; `B12/B13/B18`; `B1/B9/B26`; `B8/B14/B20`; `B6/B15/B21`; `B5/B10/B23`; final `B7/B16/B22`.

HARD Recovery 1/2 and HARD Recovery 2/2 are consumed. The third post-Recovery-2 same-obligation no-movement trigger occurred in the final `B7/B16/B22` run. Protocol therefore terminates ordinary SIVASHANKAR research in this slot. No Recovery 3 is permitted.

## Audit / prior-art state

- Source status remains OPEN/PARTIAL in this track.
- Internal lemma novelty is UNVERIFIED.
- No independent P26 full audit for this source claim.
- No distinct OTHER-track full audit.
- No paper folder and no source closure.

## Successor admission screening in the same slot

Exactly one queue candidate was screened after terminalization: `I0006` (Bou-Rabee–Panagiotis, arXiv:2609.02820). Admission fails immediately on ownership: at the captured master, `operations/claims/I0006.md` is `CLAIMED / ACTIVE / HARD OUTSIDE`, owned by `R7-06`, native ID `6aabe827777c8191a43330b4a87d481d`. Therefore it is not a lawful successor for this slot and no duplicate claim is permitted.

No successor is admitted in this terminal run. The native slot should remain enabled only as a successor-admission gate, preserving its existing recurrence, until a genuinely unassigned outside source passes exact source/current-open/ownership/classification/metric checks.
