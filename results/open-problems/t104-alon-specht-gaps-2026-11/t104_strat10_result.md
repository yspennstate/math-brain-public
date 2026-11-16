OPEN: The full sign theorem on STRAT9 region (11) remains unproved. The exact extensions, finite numerical map and remaining region (R10) are recorded below. No numerical finding is used as a proof.

## PROVED partial

PROVED: At N=6 every admissible frame and ratio is now covered for a<=2849/5000 (previously 14/25). For every N>=6 the uniform ceiling is 129/250 (previously 64/125). Larger ratio-dependent ceilings are listed below. Certificates: fine_cells.json, cubic_cells.json, stacked_cells.json, cubic_allN_cells.json, together with the inherited banks. Replay: verify_extensions.py and verify_summary.py; inherited dependencies are replayed by replay_all.py.

PROVED: There are 139 new rational cells: 42 fine ratio cells, 42 cells using sextic inequalities, 11 finer split-scale cells, and 44 simultaneous all-N cells. The latter use the three coefficients of padding identity (5). Every saved margin and residual-matrix condition is checked exactly. Replay: verify_extensions.py. The extra two ratio-dependent analytic bounds are replayed by verify_analytic.py.

PROVED partial: The final N=6 ledger has 80,355 visits, 24,708 positive leaves, 10,226 excluded leaves, 5,244 OPEN leaves, and 40,177 split nodes. Of the positive leaves, 24,458 are certified for every N>=6. Certificate: global_cover.json. Replay: verify_cover.py. This reclassification had finished before the user's stop instruction; no further box splitting was run.

PROVED partial: The exact coordinate-volume ledger on the canonical root of volume 1152 is

| Ledger | Visits | Positive | Excluded | OPEN | Split | Positive volume | Excluded volume | OPEN volume |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Initial partition | 46,229 | 4 | 6,882 | 16,229 | 23,114 | 9/256 | 530145/512 | 59661/512 |
| Final partition | 80,355 | 24,708 | 10,226 | 5,244 | 40,177 | 21629007/1048576 | 1062587817/1048576 | 15467841/131072 |

PROVED: Both rows are exact partitions of the same root; they use different split geometries. The raw OPEN coordinate volume is larger in the final row, so no monotone volume reduction is claimed. These are chart-coordinate volumes, not a measure of admissible graphs or of (R10). The four initial positive boxes remain in the proved union. Certificates: baseline_cover.json and global_cover.json. Replays: verify_baseline.py and verify_cover.py. STRAT8's 5,272 OPEN leaves concern N=5 and are not an N=6 before count.

PROVED: The following are certified ceilings on each closed ratio interval, with the maximum of adjoining records available at a shared endpoint. Full small-ratio strips include their endpoints. Finite entries are rational certificates rather than estimated optima. The r=0 entry is auxiliary; the actual stratum has r>0. The complete machine-readable table is ceiling_table.csv and extension_summary.json. Replay: verify_summary.py.

| r interval | Old N=6 | New N=6 | Old all N>=6 | New all N>=6 |
|---|---:|---:|---:|---:|

| [0,1/10] | all scales | all scales | all scales | all scales |

| [1/10,3/25] | all scales | all scales | all scales | all scales |

| [3/25,7/50] | all scales | all scales | 71/125 | 119/200 |

| [7/50,3/20] | all scales | all scales | 71/125 | 3/5 |

| [3/20,4/25] | 71/125 | 3/5 | 71/125 | 3/5 |

| [4/25,9/50] | 71/125 | 121/200 | 71/125 | 121/200 |

| [9/50,1/5] | 71/125 | 76/125 | 71/125 | 76/125 |

| [1/5,11/50] | 119/200 | 611/1000 | 119/200 | 611/1000 |

| [11/50,6/25] | 119/200 | 613/1000 | 119/200 | 613/1000 |

| [6/25,13/50] | 119/200 | 123/200 | 119/200 | 123/200 |

| [13/50,7/25] | 119/200 | 617/1000 | 119/200 | 123/200 |

| [7/25,3/10] | 119/200 | 309/500 | 119/200 | 123/200 |

| [3/10,8/25] | 76/125 | 619/1000 | 3/5 | 307/500 |

| [8/25,17/50] | 76/125 | 619/1000 | 3/5 | 613/1000 |

| [17/50,9/25] | 76/125 | 31/50 | 3/5 | 153/250 |

| [9/25,19/50] | 76/125 | 31/50 | 3/5 | 611/1000 |

| [19/50,2/5] | 76/125 | 31/50 | 3/5 | 61/100 |

| [2/5,21/50] | 76/125 | 31/50 | 74/125 | 76/125 |

| [21/50,11/25] | 76/125 | 619/1000 | 74/125 | 607/1000 |

| [11/25,23/50] | 76/125 | 619/1000 | 74/125 | 121/200 |

| [23/50,12/25] | 76/125 | 309/500 | 74/125 | 603/1000 |

| [12/25,1/2] | 76/125 | 309/500 | 74/125 | 3/5 |

| [1/2,13/25] | 603/1000 | 617/1000 | 289/500 | 299/500 |

| [13/25,27/50] | 603/1000 | 77/125 | 289/500 | 119/200 |

| [27/50,14/25] | 603/1000 | 123/200 | 289/500 | 593/1000 |

| [14/25,29/50] | 603/1000 | 123/200 | 289/500 | 59/100 |

| [29/50,3/5] | 603/1000 | 307/500 | 289/500 | 587/1000 |

| [3/5,31/50] | 119/200 | 613/1000 | 563/1000 | 117/200 |

| [31/50,16/25] | 119/200 | 153/250 | 563/1000 | 291/500 |

| [16/25,33/50] | 119/200 | 61/100 | 563/1000 | 579/1000 |

| [33/50,17/25] | 119/200 | 609/1000 | 563/1000 | 23/40 |

| [17/25,7/10] | 119/200 | 76/125 | 563/1000 | 571/1000 |

| [7/10,18/25] | 293/500 | 303/500 | 547/1000 | 71/125 |

| [18/25,37/50] | 293/500 | 121/200 | 547/1000 | 141/250 |

| [37/50,19/25] | 293/500 | 603/1000 | 547/1000 | 14/25 |

| [19/25,39/50] | 293/500 | 3/5 | 547/1000 | 557/1000 |

| [39/50,4/5] | 293/500 | 597/1000 | 547/1000 | 553/1000 |

| [4/5,41/50] | 287/500 | 119/200 | 53/100 | 549/1000 |

| [41/50,21/25] | 287/500 | 74/125 | 53/100 | 273/500 |

| [21/25,43/50] | 287/500 | 589/1000 | 53/100 | 271/500 |

| [43/50,22/25] | 287/500 | 587/1000 | 53/100 | 539/1000 |

| [22/25,9/10] | 287/500 | 73/125 | 53/100 | 107/200 |

| [9/10,91/100] | 14/25 | 5837/10000 | 64/125 | 531/1000 |

| [91/100,23/25] | 14/25 | 5823/10000 | 64/125 | 531/1000 |

| [23/25,93/100] | 14/25 | 363/625 | 64/125 | 527/1000 |

| [93/100,47/50] | 14/25 | 5793/10000 | 64/125 | 527/1000 |

| [47/50,19/20] | 14/25 | 5777/10000 | 64/125 | 131/250 |

| [19/20,24/25] | 14/25 | 2881/5000 | 64/125 | 131/250 |

| [24/25,97/100] | 14/25 | 2873/5000 | 64/125 | 13/25 |

| [97/100,49/50] | 14/25 | 573/1000 | 64/125 | 13/25 |

| [49/50,99/100] | 14/25 | 2857/5000 | 64/125 | 129/250 |

| [99/100,1] | 14/25 | 2849/5000 | 64/125 | 129/250 |


PROVED: An exact new scalar inequality for every zero-sum unit vector u in R^5 is

    (sum u_i^3)^2 >= 3 sum u_i^4 - 3/2.

PROVED: Write the sorted, unnormalized vector as U_i=sum_j[(5-j) if i<j, else -j] z_j, z_j>=0, j=1,...,4, and put t=sum U_i^2. With (x,b,c,y)=(z_1,z_2,z_3,z_4), define

    K=3xy(x-y)+b(x^2+2xy-2y^2)+c(2x^2-2xy-y^2).

PROVED: The homogeneous sextic (sum U_i^3)^2+(3/2)t^3-3t sum U_i^4 equals 625 K^2 plus nonnegative monomials, all listed as rational coefficients in cubic_moment_certificate.json. Dividing by t^3 proves the bound. Replay: verify_cubic_moment.py. An independent rational orthant Gram certificate is retained in cubic_sos.json and replayed by verify_cubic_sos.py.

PROVED: Apply this to alpha u +/- beta w and average. If n=alpha^2+beta^2, then

    [(alpha^3 d+3alpha beta^2 f)^2
      +(3alpha^2 beta e+beta^3 h)^2]/n^3
       >= 3(alpha^4 A+6alpha^2 beta^2 C+beta^4 B)/n^2-3/2.

PROVED: Nonnegative multipliers for (alpha,beta)=(1,0),(0,1),(1,1),(2,1),(1,2) are added to the STRAT9 cells. Subtract the displayed squares from the cubic residual matrices and add their affine moment lower bounds. The remaining two matrices are checked PSD throughout the ratio interval. verify_cubic_identities.py checks every subtraction exactly; cubic_cells.py uses rational Bernstein controls and all 33 moment-polytope vertices. These are degree-six frame inequalities; no floating optimization is used by their replay.

PROVED: An explicit pressure family has r=1 and

    U=(-4,1+s,1+s,1-s,1-s), W=(0,1,-1,-1,1),
    a=E=(5+s^2)/(5+10s-s^2), 0<s<=1/100.

PROVED: This connected zero-edge endpoint satisfies every inherited residual filter (11). Its exact value is

    T6=s(1100-335s+185s^2+19s^3+26s^4-11s^5)
          /[4(s^2+5)(s^2-10s-5)^2] > 0.

PROVED: Thus positive values in the old residual tend to zero. This rules out a uniform strictly positive lower bound on that residual; it does not rule out negative values elsewhere. Its inward radial rays have positive T6. The padding coefficients also have positive rational Bernstein certificates, extending the family and its rays to every integer N>=6. Certificate: pressure_family.json. Replay: verify_family.py. All inherited moment-filter signs, admissibility inequalities and all 48 zero-edge chart exclusions are checked exactly.

PROVED: exact_samples.json gives 36 rational residual points close to the numerical searches, with exact positive actual-scale and endpoint values. Replay: verify_samples.py. Their finite positivity does not prove a neighborhood or the full residual. New positive neighborhoods are certified separately by new_face_boxes.json and verify_new_boxes.py.

PROVED: new_face_boxes.json adds 37 rational positive neighborhoods for every N>=6, each containing an endpoint satisfying every old (11) filter. Replay: verify_new_boxes.py. The chart helper precise_charts.py first rescales large integer columns by positive rationals; normalized frames and charts are invariant, while the inherited square-root enclosure becomes sufficiently narrow. No floating enclosure is accepted.

PROVED: The new residual is nonempty. new_residual_witness.json gives r=999/1000 and the connected endpoint scale

    a=20000007333334000/20076659350332667,
    T6=174621586158760197641778469643046357769/40307233128375024043210488174960246657780 > 0.

PROVED: This exact point misses both actual-scale and endpoint versions of every new moment bound, both analytic bounds, and every old, new, baseline and final positive box in every zero-edge chart. It has r<1, so the r=1 pressure-family theorem does not apply. Replay: verify_new_residual.py. Its finite positive sign does not certify a neighborhood or remove it from the continuous residual definition.

PROVED: Exact replay command, from this folder:

    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 -B replay_all.py

PROVED: replay_all.py runs every retained exact certificate sequentially and prints PASS/FAIL per script. Source hashes are pinned in provenance.json and checked by verify_provenance.py. Exact proof replay needs the standard library and SymPy; numerical discovery additionally uses NumPy/SciPy/Clarabel. All writes stayed in this folder, source folders were read-only, and no network, language-model workers or subagents were used. Discovery used at most four processes and single-thread numerical settings. The sandbox refused priority changes; no successful renicing is claimed. The replay has a 1 GiB peak-RSS guard, below the requested 4 GB limit.

PROVED: Every current exact certificate passed. The one full sequential run reported a tuple/list metadata mismatch in verify_family.py. Returning the reconstructed edge/rest metadata as lists changed no certificate value; its targeted rerun passed. The original FAIL and correction remain in replay_all.out, with original failures and their resolution separated in replay_summary.json. The full run was not repeated. No box splitting or new numerical search followed the stop instruction.

## NUMERICAL

NUMERICAL: The residual map sampled 160,000 rays with seed 101113, using endpoint and inward scales. It retained 2,878 points after every condition of STRAT9 (11), including both moment tests and all chart exclusions, evaluated with floating tolerances. Twenty-four local searches found T approximately 0.0004710738034 and T/a^2 approximately 0.0004714865756 at r approximately 0.9997473372, a approximately 0.9995621693 and a/E approximately 0.9998654730. The endpoint zero edge is {1,5} in one-based labels. The actual minimum weight is approximately 1.34527e-5. No negative value was found. These are sampled values, not global minima or a proof of sign. Files: residual_map.json, residual_samples.npz; discovery replay: map_residual.py.

NUMERICAL: An independent full-matrix calculation rechecked every retained raw residual sample and its numerical filters. The maximum N=6 formula discrepancy was 2.55351295663786e-15. The directly evaluated local-search minimum was 0.0004710738033741537. No negative value was found. Replay: audit_numeric.py; data: numeric_audit.json. N=7 and N=10 checks used the N=6 residual sample, not samples of their entire residual domains.

NUMERICAL: The exact final-residual witness has a approximately 0.9961820332924364 and T6 approximately 0.0043322642763050905. These decimal renderings are not used in its proof.

NUMERICAL: The full sequential replay took 814.385 seconds and peaked at 169.641 MiB RSS. These operational measurements are separate from exact certificate signs.

## OPEN

OPEN: What remains is the continuous set (R10) below, including the corner neighborhood approaching (r,a)=(1,1) and the retained 5,244 OPEN leaves. The pressure family itself is proved, but no punctured corner neighborhood is proved. The numerical searches do not settle the sign there. The exact witness shows the final residual is nonempty. No claim is made that every OPEN leaf is feasible or that the whole residual has been localized to one quantified corner box. A separate STRAT11 run can attack the corner by a first-order expansion; this run starts no such work.

PROVED: Here are the exact definitions for the final residual. Let u,w be orthonormal zero-sum vectors in R^5, r=b/a in (0,1], lambda=(2+a(1+r))/4, and

    omega_ij=lambda/5+a u_i u_j+ar w_i w_j,
    D_ij=-1-r-20(u_i u_j+r w_i w_j),
    E=2/max(3-r,max_(i<j) D_ij).

PROVED: Write A=sum u_i^4, B=sum w_i^4, C=sum u_i^2 w_i^2, d=sum u_i^3, e=sum u_i^2 w_i, f=sum u_i w_i^2, h=sum w_i^3, and m=A+rB+(1+r)C. The exact expression is

    T6=9/80+a(11m-2(1+r))/8+a^2(H+R),
    H=[100(1+r)m-1600(A+r^2B)-1280(1+r^2)C
          -640rC+415(1+r^2)-66r]/320,
    R=3d^2+3r^2h^2+(1+4r)e^2+(r^2+4r)f^2
          +2(1+r)(df+rhe).

PROVED: verify_algebra.py derives this identity from the original ordered-pair definitions and verifies the padding identity (5) of STRAT9. It also verifies the corrected radial identity

    T_N(a)=(1-a^2/E^2)C_N+a(1-a/E)L_N
               +(a^2/E^2)T_N(E),
    C_N>0, L_N>0, N>=6.

PROVED: Define the record bank K to contain moment_cells.json, allN_optimized_cells.json, fine_cells.json, cubic_cells.json, stacked_cells.json and cubic_allN_cells.json. A record is applicable when its closed ratio interval contains r. For a record without cubic_multipliers use cells.lower_value and padding.lower_coefficients; for a record with that field use cubic_cells.lower_value and cubic_cells.lower_coefficients. Put

    P_6^c(x)=lower_value((A,B,C),x,r,vector_from_record(c)),
    P_N^c(x)=sum_(j=0)^2 (N-6)^j
                  lower_coefficients((A,B,C),x,r,vector)[j]/(N-2)^2,
    P_N^cells(x)=max_(applicable c in K) P_N^c(x).

PROVED: These are valid lower bounds at every actual feasible scale x, including outside a record's saved scale interval. Residual matrix positivity needs only its saved ratio interval. Scale intervals enter the uniform ceiling certificates. The all-N identity leaves a nonnegative remainder that is omitted from P_N^c. The definition agrees with P_6^c at N=6. Two additional analytic bounds below are included in P_N^new.

PROVED: Put eta(r)=2+2r/(r^2+4r+1), and define

    R_u=eta(r)(3A-3/2)-C,
    R_w=r^2[eta(r)(3B-3/2)-C].

PROVED: On r>=3/25 both are exact lower bounds for R. For R_u the identity is

    R-R_u=eta(r)(d^2-3A+3/2)
      +[(1+r)d+(r^2+4r+1)f]^2/(r^2+4r+1)
      +[(1+4r)e+r(1+r)h]^2/(1+4r)
      +r^2(2+10r-r^2)h^2/(1+4r)+(C-f^2).

PROVED: Every summand is nonnegative by the sextic inequality, Bessel, or its displayed sign. The second bound has an analogous square identity; its only extra scalar factor is 2r^2+10r-1, strictly positive on [3/25,1]. verify_analytic.py matches both identities and their exact Bernstein signs. Set A_6^i(x)=cells.base_value((A,B,C),x,r)+x^2 R_i. For N>=6 use padding.base_coefficients plus (16,8,1)x^2 R_i and evaluate the polynomial in N-6 divided by (N-2)^2. Define

    P_N^new(x)=max(P_N^cells(x), A_N^u(x), A_N^w(x)).

PROVED: This adds ratio-dependent higher-degree multipliers, with no numerical acceptance step. Their rational denominator r^2+4r+1 is strictly positive. Replay: verify_analytic.py; implementation: analytic_moments.py.

PROVED: Define V6new(r) as the maximum of 14/25 and all applicable ahi in moment_cells.json, fine_cells.json, cubic_cells.json, stacked_cells.json and cubic_allN_cells.json. Define Vinfnew(r) as the maximum of 64/125 and all applicable ahi in allN_optimized_cells.json and cubic_allN_cells.json. The base ceilings and the explicit parent links of stacked_cells.json ensure that these are continuous-in-scale covered intervals down to zero. All ratio intervals include their endpoints; the maximum convention resolves shared boundaries exactly.

PROVED: Let B6 be the union of the 47 old boxes in face_boxes.json, the 37 new boxes in new_face_boxes.json, the four positive boxes in baseline_positive_partition_boxes.json, and every box in positive_partition_boxes.json. Let Binf use the same old and new local boxes and allN_partition_boxes.json instead of the full N=6 positive partition; the four baseline boxes are also valid for every N>=6. All are explicitly listed closed rational boxes. Their coordinates are (t,v1,z1,v2,z2,z), with

    V1=(v1,z1), V2=(v2,z2),
    V3=(1-t-v1-v2,-z-z1-z2), V4=(t,0), V5=(-1,z),
    M=V^T V, tau=tr M, Delta=det M, D=20t-tau,
    a=[tau+sqrt(tau^2-4Delta)]/D,
    b=[tau-sqrt(tau^2-4Delta)]/D.

PROVED: zero_face.py verifies Cface_N=10(N-2)^2 D^2 Delta T_N. The factor is positive on every feasible rank-two-gap chart. The numerator's three coefficients in N-6 are used throughout; an N=5 polynomial is never substituted for this expression. New local and partition boxes certify the numerator by exact centered integer inclusion or rational Bernstein controls. Feasibility of surrounding, non-graph chart points is unnecessary for a sign certificate.

PROVED: Let F be all permutations and inward radial rays of the explicit r=1 pressure family above. This definition depends on the projector Q=uu^T+ww^T, so it includes every orthonormal eigenframe of that same repeated gap. Every graph in F is covered for every N>=6.

OPEN: The final N=6 region still requiring a covering sign proof is exactly the following intersection:

    u,w orthonormal and zero-sum;
    3/20<r<=1, omega_ij>=0, carrier connected;
    V6new(r)<a<=E, a<2/(3-r);
    P_6^new(a)<0 and P_6^new(E)<0;
    the true endpoint at E is connected;
    for every zero edge there, both endpoint orders, all permutations
      of the remaining three vertices, and both reflections of the
      second chart coordinate, the chart point lies outside B6;
    the graph does not belong to F.                         (R10)

PROVED: Every case outside (R10) is covered by an inherited or new theorem, a nonnegative pointwise lower bound, the radial identity, a face box, or the pressure-family theorem. Thus every counterexample must satisfy (R10). This is a finite exact exclusion description; it is not a sign assertion inside (R10). Closed boxes and all chart symmetries are retained, including graphs with multiple zero weights.

OPEN: For each N>=7 the corresponding exact remaining region replaces 3/20 by 3/25, V6new by Vinfnew, P_6^new by P_N^new and B6 by Binf in (R10). The family exclusion F is unchanged. These statements concern five-vertex carriers with isolated vertices, and make no assertion about larger connected carriers.

PROVED: Every canonical endpoint chart of a graph in (R10) lies in an OPEN leaf: all positive leaves are explicitly excluded, and every excluded leaf violates a necessary condition or has an already covered endpoint scale. The canonical root is t in [1,4], v1 in [-1,0], z1,z2 in [-4,4], v2 in [-1,1/2], z in [0,4]. Replays: verify_domain.py, zero_face.py, verify_cover.py. This implication is for N=6; N>=7 uses the stated Binf exclusions without treating the N=6 excluded ledger as an all-N cover.

PROVED: Task: “shrink region (11), aiming to close it” — received 2026-11-13 at approximately 08:33 +04. Finalization and stop instruction received during this run; no additional splitting followed it.
