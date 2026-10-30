# B10 / A046 — frozen half-tax candidate and exact boundary intake

**Run:** `20261011T235503Z-fleet01-B10-a046-half-tax-intake`  
**Primary packet:** A046 (Current-candidate intake)  
**Attempt:** `A046-HALF-TAX-INTAKE-1`  
**Candidate:** `B10-A046-HALF-BIAS-TAX@1`  
**Status:** candidate frozen; exact lower boundary proved in prior accepted evidence; new finite two-bit scan passed; candidate remains OPEN. Full FEI remains OPEN.

## Exact candidate

For every finite genuine Boolean sign under every interior product law and every physical reveal block `A`, let

\[
M_A=H(S_A\mid S_B),\qquad J_A=I(Z;S_B),
\]

and

\[
\Delta_A(p)=\sum_{i\in A}
\bigl[h_2(p_i)+\log_2\max\{p_i,1-p_i\}\bigr].
\]

The frozen candidate is

\[
\boxed{J_A\le M_A+\tfrac12\Delta_A(p).}
\tag{C}
\]

This is a genuinely changed coefficient, not the refuted tax-free helper and not an obsolete numerical repair.  The independently accepted B09 theorem proves coefficient `1`.  The accepted review also reconstructs the exact Boolean AND boundary and proves every universal coefficient must be at least `1/2`.  Candidate (C) asks whether the lower endpoint is sufficient.

## Exact boundary

For `g(x,y)=(-1)^{xy}`, reveal `X`, let `P(X=1)=p` and `P(Y=1)=q`.  With `s=4q(1-q)` and `c=4q^2`, the original sources prove

\[
J_A=h_2(sp)-p h_2(s),
\]

\[
M_A=(1-sp)h_2\!\left(\frac{cp(1-p)}{1-sp}\right)+sp h_2(p).
\]

For `p<1/2`, `Delta(p)=p log_2((1-p)/p)`, and hence

\[
\lim_{p\downarrow0}\frac{J_A-M_A}{\Delta(p)}=4q(1-2q).
\]

Completing the square,

\[
4q(1-2q)=\frac12-8(q-\tfrac14)^2\le\frac12.
\]

Thus the hardest fixed-`q` rare boundary is uniquely `q=1/4` and saturates (C).  Every smaller coefficient is rigorously refuted.  This does not prove (C) away from that boundary or in higher arity.

## New bounded diagnostic

`scan_b10_half_tax.py` exhaustively evaluated all 16 two-bit truth tables and both singleton reveals on a declared grid of 235 biases per input (linear points `i/400`, `1<=i<200`, plus `2^-k`, `2<=k<=40`).  It evaluated 1,767,200 gate/bias/reveal instances and found no violation of (C).  The maximum observed ratio

\[
\frac{J_A-M_A}{\Delta_A}=0.49303368801064995
\]

occurred for an AND-equivalent truth table, rare bias `p=2^-40`, other bias `q=1/4`, matching the analytic saturation.  The scan is IEEE-double numerical evidence only; it is not a continuum certificate and makes no higher-arity claim.

Command: `python3 scan_b10_half_tax.py | tee CHECK.out`.  Randomness: none.

## Controls and exact scope

The corrected signed-interval certificate refutes only coefficient zero.  The rare-refund, weighted-TC, pivotal-credit, fixed-prefix, raw-convolution and overlap-product controls concern different helper quantities and are retained in `KNOWN_FALSIFIERS.md`.  The fixed-Renyi point-defect obstruction is also retained: fixed lower-order spectral Renyi entropy cannot replace Shannon entropy, whereas (C) uses Shannon conditional entropies.

Even if (C) were proved, full FEI would remain open: a restriction/composition proof must still pay the selected sequence of `M_A+(1/2)Delta_A` without reusing influence and must retain terminal entropy.  Disjoint tensor additivity does not imply arbitrary-composition additivity.

## Source pins

- B10 contract blob `00939b50127519cdd7089770b49884220fa34d1d`.
- Protocol blob `457358ff62cbf1141a72096bcabdf95bf18c1be2`.
- Stream index blob `58e3eb0b1f0e9c03ebf709f83ad496ee8f2df704`.
- Packet status blob `66a78ef3249a89d481a47320f990dc2aec002ccb`.
- Claim registry blob `bef50513c8309b0e601aec42470bc09162f26ea8`.
- Obstruction registry blob `d9c8b8632d019aa9e4d5c7394001d116fd21d94e`.
- B09 original theorem report blob `71b68e4decf9658a42fef6bb2668e19f25bd214a`.
- B09 endpoint report blob `144d7c0b8646bd01a119d932df2e14846ec24d91`.
- B18 independent review blob `ab9aa1c03c1e15dca57aa04d8f5aac7c5a8bfb43`.
- Corrected interval repair blob `c3adb486c8ca9f7a35f384ee82942eef66bd64be`.
- Fixed-Renyi source blob `c575d18146a9a9d2bdee006dc3856947565442bc`.

## Handoff

A046 is complete as an intake artifact but not independently accepted.  Route (C) to A047 for analytic boundary search and to A048 for exact tensor/activation stress.  The most useful next step is a proof or certified counterexample to (C) for all two-bit gates over the continuum bias square, before any larger arity search.  Review targets are A092 and A087.

No independent review, native Brain ingestion, full-FEI solution, new worker, scheduler change, merge, deployment, or public release is claimed.  The runtime exposed no separate model or reasoning-effort selector.
