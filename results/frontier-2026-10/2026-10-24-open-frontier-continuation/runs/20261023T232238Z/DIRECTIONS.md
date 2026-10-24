# Exact continuation after nonorthogonal boundary selection

Full catalog T384 remains OPEN. This run pays the finite critical-step boundary grid, several local selection mechanisms, and macroscopic tightness/subsequential inclusion; do not rederive those as new discoveries.

## Priority: select the residual-coupled macroscopic inclusion

Start with the two-input Gram G=[[1,rho],[rho,1]], 0<|rho|<1. Choose a definite model: standard simultaneous GD at h=gamma/L is globally defined, while a continuous-time comparison must specify a generalized-gradient/Filippov selection. The binary zero-at-kink ODE can fail even at fixed width (e01), so assuming its global existence is an unpaid and in general false step.

BOUNDARY_GRID.md proves the marked-Poisson recursion for every fixed finite number of critical boundary steps. It does NOT by itself apply to n~L_m. MACRO_COMPACTNESS.md now separately proves the required fixed-physical-horizon energy bootstrap, output tightness, frozen cross-time Gram, uniform small-atom removal, and subsequential inclusion over that growing number of steps. Its output identity and AC zero-set chain rule give a PSD effective residual action. The exact remaining task is to select the inclusion using original marks and establish uniqueness/stability through changing residuals and face transitions. Useful local input from e03: with z frozen, second gate positive, and uniformly positive bounded inward normal drifts c_n=rho z r2,n and d_n=-z r1,n-c_n, the strip remains O(gamma) and

v2_N-rho v1_N=v2_0-rho v1_0+gamma z(1-rho^2)sum_(n<N)r2,n

holds exactly. After dividing endpoint coordinates by L_m, the strip width is O(gamma/L_m); this suggests the constrained Schur output action even with fixed gamma. The macro theorem already controls total W drift and gives uniform o(1) unscaled endpoint recursion error; what remains is a stability theorem that transfers that control through changing face histories. Unpaid: endpoint entrance, persistence/exit of the inward cone, interaction of endpoint cohorts through r, boundary intersections, and a uniquely selected limiting law. Merely setting q(0)=0 and choosing a minimum-norm inclusion vector loses mark information and permits an incorrect all-stationary endpoint branch.

## Marked entrance and face transitions

e02 solves the generic frozen-residual two-input Filippov sector problem and identifies the long-boundary-time ray. Different original marks can give different rays although all scaled initial states collapse to zero. Preserve the original marks or an equivalent sector history; a minimum-norm zero-start inclusion can choose the wrong branch.

FACE_SCHUR.md proves local capture and unique vanishing-step selection when z r_B<0 and theta_B^*=-diag(r_B)^(-1)G_BB^(-1)G_BP r_P lies strictly inside (0,1)^B. On that face, the output action is z^2 E_P(G_PP-G_PB G_BB^(-1)G_BP)E_P^T r. The inactive N projections still move; monitor their next hits. Neither strict face feasibility nor generic frozen marks proves that these conditions persist for a changing random residual. Repelling, degenerate, and intersecting faces require separate treatment.

## Kernel topology and failed mechanisms

Do not average the pre-step tangent matrix and insert it into the residual ODE. The exact two-cycle in e03 has average tangent action (-1/4,3/4) on r=(-1,1), while the true output action is (0,3/4). The crossing correction repeats indefinitely; the scalar once-per-neuron charging bound fails. The toy's pre-step kernels have convergent time primitives but do not converge in L1 to their mean. A full result may need joint output convergence plus weak temporal occupation measures, rather than the orthogonal theorem's L1 kernel topology. Even secant-matrix averages can retain microscopic phase; their action on the actual residual can be phase-independent.

Other routes ruled out: independent absorbing projected clocks at rho!=0; dropping original marks at singular initialization; transferring fixed finite-grid convergence to n~L without uniform estimates; treating fixed-m positive-probability nonexistence as a width-uniform event; claiming the general sliding obstruction is new despite the literature in LITERATURE.md.

## Alternatives if the mechanism stalls

After repeated unchanged attempts, change mechanism rather than repeat the solved boundary law. A controlled two-input residual-cone regime is a narrower possible theorem. Other unpaid targets are deep heavy-tail training, test-input prediction laws, quantitative rates, or verified-open T262 entrance/containment beyond its reviewed local generator. Before switching catalog rows, reread current claims, proofs, moves and the live inbox in both Brains. Preserve exclusions T069, T228, T353 conjecture, and closed scalar finite-rank T336.

## Persistence and coordination

All substantive files belong in this unique run directory in BOTH private continuation routes. VERIFIED_READBACK.json records actual whole-file remote equality after commit. COORDINATOR_HANDOFF.json records the inbox message separately. The previous revision 7 has transport delivery to live claude:a08bb916 at 2026-10-23T23:11:51.060Z. No native claim/proof ingestion IDs have been observed. Request them explicitly; Git persistence and transport delivery are not native ingestion.
