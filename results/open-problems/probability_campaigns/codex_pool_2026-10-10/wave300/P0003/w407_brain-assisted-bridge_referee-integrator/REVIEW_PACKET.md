# P0003 independent referee packet (2026-10-10)

Target P0003: Grimmett, arXiv:2205.07318, Question 2.2. It asks whether uniform n-step honeycomb SAWs from the origin converge weakly, after suitable rescaling, to SLE(8/3). The source leaves the scale and curve formulation open. Duminil-Copin--Smirnov, arXiv:1007.0575v2, Section 4, Conjecture 1 instead studies critical length-weighted walks between boundary marks of a planar domain. That is a related ensemble, with no transfer theorem supplied here. Current openness is UNKNOWN after bounded checks.

## w405, finite restriction identity L1: KEEP

Reproduction: an a-to-b path avoids a closed obstacle A precisely when every vertex it visits and every embedded edge segment it traverses survives the deletion rule in ATTEMPT.md. This is a weight preserving bijection between avoiding paths in G and paths in G^A. Summing x_c^length yields P(avoid A)=Z(G^A)/Z(G), provided Z(G)>0. Dividing each surviving weight by Z(G^A) gives the conditional law when that denominator is positive. The edge condition is necessary for an obstacle that crosses an edge interior. This is a finite graph identity only; it says nothing about limits.

## w405, outer buffer lemma L2: KEEP

I checked the strict inequalities independently. On nonempty compact subsets of compact S, K -> dist(K,A) is 1-Lipschitz in Hausdorff distance. Write d_n=dist(K_n,A), d=dist(K,A). The inclusions N_{r_m}(A) subset A_m subset N_{R_m}(A) give P(d_n>R_m) <= P(K_n avoids A_m) <= P(d_n>r_m). Weak convergence of d_n and Portmanteau give P(d>R_m) <= q_m <= P(d>=r_m). Both exterior terms tend to P(d>0) as positive r_m,R_m tend to zero. Compactness makes d>0 exactly K cap A empty. No zero-contact-mass assumption or interchange of n and m is used. This proves the stated abstract lemma; it does not prove the fixed-buffer ratios for SAW.

## w405, raw avoidance counterexample R1: KEEP

For A=[-1/4,1/4] x [-1,0] and a=(-1,0), b=(1,0), every broken line a -> (0,1/n) -> b stays above A over its x-range and is simple. Under the common linear parametrization it converges uniformly to a -> (0,0) -> b, which meets A. Thus avoidance probabilities change from 1 to 0. This confirms that a raw avoidance event is not continuous under weak curve convergence.

## w405, conditional SLE identification C1: FIX for chordal claim; DROP as a P0003 reduction without transfer

The logical route is plausible for Duminil-Copin--Smirnov's chordal ensemble under T, B, C, but the packet must state B for a class covering every smooth hull in LSW Proposition 3.3 and verify each mapped outer buffer remains a hull in that class. Proposition 3.3 requires a probability measure on its sample space Omega: connected, unbounded, real-line contact only at 0, and connected complement. T's simple interior curve assumption supplies this after mapping, if its endpoint and boundary behavior is justified. The final step from trace law to oriented curve law is only sketched. Keep C1 as a conditional chordal sketch. It does not establish Grimmett's fixed-n origin question: that requires a separate ensemble transfer, endpoint law and spatial scaling. The chordal sketch itself still lacks curve tightness T and the positive endpoint partition-ratio asymptotic B. LSW Theorem 6.1 proves the SLE(8/3) restriction probability; it does not prove lattice ratio convergence.

## w406, cycle-space obstruction: KEEP

Independent derivation: orient each internal edge u_e -> v_e, set d_e=v_e-u_e and X_e=(d_e/2)F(m_e). Its contributions to the two endpoint equations are +X_e and -X_e. Boundary half-edge values are zero, hence the local relation is B X=0 for the ordinary incidence matrix. For connected G, a spanning tree gives rank(B)=|V|-1; the row sum is zero, so dim_C ker B=|E_int|-|V|+1. On a six-edge face choose X_e=delta/2 along the oriented cycle, or F(m_e)=delta/d_e. This has |F|=1, zero values elsewhere and zero boundary values. Adjacent face-midpoint values differ by 1 across distance sqrt(3)delta/2, precluding any uniform Holder estimate. This verifies a bounded non-equicontinuous kernel mode. It is not a SAW path-sum observable; extra path-sum constraints might exclude it. Duminil-Copin--Smirnov themselves say the vertex equation does not determine F from boundary values and describe it as divergence-free with possible curl (Section 4).

## w406, random-quadrangulation theorem scope: KEEP

Gwynne--Miller's arXiv:1608.00956 abstract concerns a SAW-decorated random quadrangulation and metric-measure convergence. Deterministic Euclidean honeycomb SAW is a different model. No transfer theorem was provided. This is a source-scope correction, not a new result.

## Source/board correction to w405

The currently read W0300_O/TEAM_BOARD.md has no exact P0003 row (`rg -n -F P0003 ...` returned no hit). The packet's sentence that it assigns P0003 to w333 is unsupported by that board as currently present. This does not affect L1, L2, or R1.

NEXT: Define the fixed-n scale/topology and require a transfer theorem before applying a chordal result to P0003. Independently, a chordal proof still needs fixed-buffer ratio estimates and curve tightness. If w407 authors a new mathematical lemma, obtain w410's independent audit.
