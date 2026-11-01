# Keystone (bulk overlap moment) — synthesis after the session-16 assault

Lead, 2026-06-28. The central open problem `prob:pc` (non-Gaussian universality upper side, which
also governs the Gumbel law) is the BULK overlap moment
```
E[(1-|rho|^2)^{-d_F/2} ; D >= eps m] <= 1 + o(1),     rho = <u_S,u_T>,  D = m-|S∩T| = Theta(m),
```
for the unit normals of two random (m-1)-row spans of an iid mean-0 var-1 bounded-density matrix.
Two focused agents + lead verification reduce it as follows.  Equivalently, conditioning on the
shared span, in F^D: u = null vector of D-1 iid isotropic vectors g_i (= projections of the
disjoint rows), e a fixed unit vector, X := ||P_W e||^2 = 1-|rho|^2, a := d_F/2.

## The reduction (what is now proved vs the lone remaining input)

**(T) TAIL — PROVED** (standard RV08 net+small-ball; `notes/keystone_tail.md`, lead-verified).
For arbitrary fixed unit e,
```
P{ X <= y } = P{ |<e,u>|^2 >= 1-y } <= (C sqrt(y))^{D-1} + 2 e^{-cD},    C,c depending on (K0,K,F),
```
with the tuned form P{X<=y} <= 2 e^{-cD y^{-1/2}} + (C y^{1/4})^{D-1}.  Proof: operator-norm bound
||sum g_i g_i^*|| <= R^2 D (covariance estimation), a delta-net of the polar cap
{|<e,v>|>=sqrt(1-y)} of size (C0 sqrt(y)/delta)^{D-1}, union bound, and tensorized small-ball
P{||Ax||^2 <= R^2 D delta^2} <= (C2 K R delta)^{D-1} per net point.  The delta CANCELS
(cap-smallness sqrt(y) = per-coordinate gain), killing the spurious sqrt(D) blowup of the
elementary per-vector route.  Exponent (D-1)/2 is the exact Gaussian/Beta value.  Hypothesis:
iid isotropic sub-Gaussian with bounded scalar density (same as the 2D lemma).  Numerically
confirmed (D=12; gauss/rademacher/uniform): P(X<=y)/y^{(D-1)/2} = O(1), <1 throughout.

**(A) ASSEMBLY — PROVED given (M)** (`notes/keystone_tail.md` Section 3).
Given mu1 := E[1-X] = E|rho|^2 = O(1/D): split E[X^{-a}] over {X<=y1},{y1<X<=1/2},{X>1/2}.
The singular part is o(1) by the tuned tail (T); the bands are o(1) by Markov using mu1=O(1/D).
Hence E[X^{-a}] = 1 + o(1) (indeed 1 + a*mu1 + o(mu1) with a second-moment input). Only the MEAN
mu1 is needed, not concentration.

**(M) TYPICAL VALUE mu1 = E|rho|^2 = O(1/D):**
- DISJOINT pairs (D=m): PROVED EXACTLY, E|rho|^2 = 1/m. By coordinate symmetry (the iid entry law
  is invariant under signed permutations / phase-permutations and u_S is equivariant),
  E[u_S u_S^*] = I_m/m exactly; for disjoint S,T the normals are independent so
  E|rho|^2 = tr((I/m)^2)·... = 1/m.  (`notes/keystone_typical.md`.)
- OVERLAPPING pairs (D<m): REDUCED to one operator estimate. Conditioning on the shared span E,
  u_S,u_T are conditionally iid in E^perp ~= F^D with conditional projector mean
  M_E := E[u u^* | E]; then E[|rho|^2 | E] = tr(M_E^2), and 1/D <= tr(M_E^2) <= lambda_max(M_E).
  So mu1 = O(1/D) follows from the DELOCALIZATION-IN-EXPECTATION bound
        lambda_max(M_E) = sup_{||w||=1} E[|<u,w>|^2 | E] <= C/D.
  Conditional ISOTROPY E[g_i g_i^* | E] = I_{E^perp} is proved and pins tr(M_E)=1 (so the average
  eigenvalue is 1/D) — but ONLY the trace. Isotropy alone does NOT give flatness: an explicit
  isotropic law has lambda_max(M_E) ≈ 0.648 (numerically verified). So (M) for overlapping pairs
  needs the specific structure of projections of iid rows, NOT just isotropy. This is the lone gap.

## Status: keystone reduced to ONE estimate
The bulk overlap moment, hence the full non-Gaussian universality upper side AND the explicit
Gumbel law, now follow from the SINGLE delocalization-in-expectation estimate
```
  lambda_max( E[ u u^* | E ] ) <= C/D   for the null vector u of D-1 projected iid rows in E^perp,
```
i.e. mu1 = E|rho|^2 = O(1/D) for overlapping pairs. The tail (T) and assembly (A) are proved by
standard techniques; the disjoint typical value is exact. This is a genuine, large reduction of the
keystone: from "vague hard pair-correlation" to "one null-vector delocalization-in-expectation bound,
everything else proved." 

HONEST CAVEATS. (T) is a complete proof SKELETON via published methods (RV08 invertibility,
Vershynin18/LPRT05 operator-norm + tensorized small-ball), not a verbatim citation of the [RV16]
no-gaps THEOREM (which is coordinate-block/sup-norm, not a fixed-direction polar small-ball);
no new idea is needed but it must be written out. (M)-overlapping is genuinely open: isotropy is
insufficient (counterexample), and the elementary symmetry does not transfer to the oblique
subspace E^perp. Whether mu1=O(1/D) holds for projected iid rows is the precise residual question;
it is a delocalization-in-expectation statement, plausibly true and a recognized RMT object, but
not proved here.

## Manuscript actions
- Sharpen `prob:pc`: state that the upper side reduces (tail + assembly proved) to
  mu1 = E|rho|^2 = O(1/D) equivalently lambda_max(E[u u^*|E]) <= C/D; disjoint case exact;
  overlapping case = the open delocalization-in-expectation estimate.
- Optionally promote (T) to an appendix and the disjoint (M) computation to the universality section.
- Sources to add: RV16 (no-gaps), LPRT05, Vershynin2018 (already discussed in the tail note).

## SESSION 19--20 UPDATE: the overlapping case is now CLOSED (modulo the local law)
The "lone gap" above (mu1=E|rho|^2=o(1) for overlapping pairs, equiv. lambda_max(E[uu^*|E])=o(1)) is
RESOLVED. (i) The assembly bar was sharpened to mu1=o(1), SUFFICIENT AND NECESSARY
(`notes/keystone_assembly_bar.md`). (ii) The lambda_max~0.648 "counterexample" was a D=2 artifact
(decays ~1/D), REFUTED (`notes/keystone_weak_deloc.md`). (iii) CLOSURE via resolvent monotonicity
(`notes/residual_locallaw.md`, manuscript Prop appB:resolvent + Cor appB:closure): u is the EXACT null
eigenvector of Q=GG^*, so u u^* <= eta(Q+eta)^{-1}, giving
lambda_max(E[uu^*|E]) <= eta||E[(Q+eta)^{-1}]|| <= (1+o(1)) eta m(-eta) = (1+o(1))sqrt(eta) -> 0
(eta=1/log D), with the OFF-SUPPORT resolvent norm from the anisotropic local law [KnowlesYin2017,
BEKYY2014] applied to the projected sample covariance (separable model; off-support => hard edge never
resolved). Compression + operator-norm-in-expectation handled (`notes/residual_compression.md`,
`residual_lsv.md`). NET: II.B universality upper side + the explicit Gumbel law are PROVEN modulo one
standard off-support local-law application. prob:pc is reframed as: a self-contained proof avoiding the
local law. This supersedes the "not proved here" caveat above.
