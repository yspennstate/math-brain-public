PROVED (verify_certificates.py): 13,359 of the 13,368 original OPEN boxes are now fully closed. The final subdivision has 8,046 exclusion leaves, 7,702 positivity leaves and 9 OPEN leaves. The maximum additional bisection depth, measured from each supplied STRAT11 leaf, is 16. There are 2,389 split nodes. The full sign theorem for region (11) at N=6 remains OPEN.

PROVED (verify_obstruction.py): Complete closure by the two requested strictly signed Bernstein forms is impossible. Every one of the nine remaining leaves contains an exact disconnected equality point with T=0 and every weak feasibility polynomial nonnegative. Products of these constraints do not remove this obstruction. Nine is the minimum possible number of OPEN leaves under the requested per-original-box finite bisection scheme, and this run attains that minimum. This is an impossibility result for the requested certificate forms, not a counterexample to positivity on the strictly feasible region.

PROVED (verify_certificates.py): Original-box classification:

| Original boxes | Count |
|---|---:|
| Direct exclusion | 7,384 |
| Direct positivity | 5,314 |
| Fully closed after splitting | 661 |
| Still containing an OPEN descendant | 9 |
| Total | 13,368 |

PROVED (verify_certificates.py): Final leaf and chart-coordinate volume ledger:

| Kind | Leaves | Exact chart volume |
|---|---:|---:|
| Exclusion | 8,046 | 4113443097/67108864 |
| Positivity | 7,702 | 5427576081/134217728 |
| OPEN | 9 | 189/134217728 |

PROVED (verify_certificates.py): The OPEN chart volume falls from 3333609/32768 to 189/134217728. Their ratio is exactly 7/505720832. The three final volumes sum to the input volume exactly. These are chart-coordinate volumes, not volumes of feasible graphs.

PROVED (verify_obstruction.py): The remaining original node IDs are 12091, 12407, 14175, 15603, 15773, 19750, 20736, 21058 and 21550. remaining_open_boxes.json lists their final depth-16 descendant boxes, exact bounds and split paths. Five contain limits with two disjoint edges of weight 1/2 and one isolated vertex; four contain a triangle with weights 1/3 and two isolated vertices.

PROVED (verify_obstruction.py): Representative equality points, in coordinate order (t,v1,z1,v2,z2,z), are

    (4, -1, -sqrt(5), -1, -sqrt(5), sqrt(5)),
    (4, -1, -sqrt(15)/3, -1, -sqrt(15)/3, sqrt(15)).

PROVED (verify_obstruction.py): At both representatives tau=D=40, Delta=400, a=b=1, T=0, rank>0, ratio>0 and connected=0. All basic weak chart inequalities hold. The full nine-point bank is obstructions.json. Its replay encodes each coordinate as a rational pair A+B*sqrt(d), d in {5,15}; products, zeros and sign comparisons use Fraction arithmetic and rational squared comparisons. No floating square roots are used. All nine witnesses are outside the strict feasibility set, and none is a feasible rational counterexample.

PROVED (verify_obstruction.py): If p is one of these points, then sum lambda*g(p)>=0 for every nonnegative multiplier vector, including products. It therefore cannot have all Bernstein coefficients strictly negative on a box containing p. Similarly, T(p)-sum lambda*g(p)<=0, so that polynomial cannot have all coefficients strictly positive there. Bernstein basis functions are nonnegative and sum to one on the closed box. Every finite bisection retains a closed descendant containing p.

PROVED (verify_formulation.py, verify_certificates.py): The target is exactly STRAT10/cover_face.polynomials()[0], namely Cface_6/8. For V and M as in STRAT10, the constraints used are orientation, order12, order23, x3bound, all five row bounds, the nine nonzero edge polynomials, spectral00, spectral11, connected, rank and ratio=529*Delta-60*tau^2. The strict connected, rank and ratio premises are relaxed to nonnegative inequalities in the multipliers, which is safe. The inherited residual scale premise a>14/25 is used through 625*(tau^2-4*Delta)-(14*D-25*tau)^2>=0 only when 14*D-25*tau>=0 is proved on the entire box. Stronger ratio-dependent scale ceilings are omitted; certificates then apply to a larger set. Every sign assertion is conditional on the applicable scale premise. The canonical ROOT bounds and all named constraints are reproduced in the supplied source and exact_bernstein.py.

PROVED (verify_certificates.py): certificates.json contains each box, kind, rational-string multipliers, split tree and rational lower bound. One certificate uses products, at original node 12091, split path 0000010001. The other certificates use linear multipliers. Replay forms -sum lambda*g for exclusion and T-sum lambda*g for positivity, clears multiplier denominators, translates with integer arithmetic and verifies a strictly positive Bernstein lower bound. Of the 15,748 accepted certificates, 9,097 use full tensor coefficients and 6,651 use a sufficient absolute-coefficient envelope. The replay verifies the rational monomial-to-Bernstein identities and the envelope coefficient bounds exactly. NumPy object arrays only arrange arbitrary-precision integer arithmetic; no LP result or floating tolerance enters a proof.

PROVED (verify_samples.py): The ten worst numerical triage points, converted to exact decimal rationals, satisfy the basic chart constraints and have positive target values. An independent direct rational zero-face evaluation agrees at each point. NUMERICAL: their selection came from diag_all.json. OPEN: these finite checks do not prove signs at unsampled points. No feasible exact rational point with T<=0 was found.

PROVED (replay_all.py): All 15 replay checks passed, including the STRAT11 mathematical verifications, the exact overlay-to-input match, all new certificates, all nine obstructions, exact samples and source fingerprints. Run from this directory:

    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 -B replay_all.py

NUMERICAL: Independent certificate replay took 239.06 seconds; the full inherited-plus-new replay took 267.37 seconds. Details are in verification_summary.json, replay_summary.json and replay_all.out.

PROVED (verify_sources.py, inherited_replay.py): All 483 inherited files are unchanged. STRAT11 checks run through a read-only wrapper; its overlay is replayed without its file-writing main block. The provided inherited provenance bank names two absent transient files, STRAT9/codex.pid and STRAT10/codex.pid. Only those operational PID hashes are skipped, explicitly; every mathematical source and proof-input hash matches. This is the sole difference from the original STRAT11 provenance invocation.

NUMERICAL / operational: Discovery and certificate replay used four multiprocessing workers and single-thread numerical libraries; no subagents or language-model workers were started. The sandbox denied nice 5, shared mesh/checklist writes and ps. Largest recorded worker peak RSS was 717275136 bytes; the refinement parent peak was 264929280 bytes. The conservative sum 4*largest_worker_peak+parent_peak is 3134029824 bytes, or 2.919 GiB. These individual maxima need not coincide; simultaneous aggregate RSS was not sampled. Thus the recorded conservative bound is below 3 GiB, but does not establish a decimal 3000000000-byte cap. The LP matrix implementation was changed to avoid large temporary copies before the final refinement. Checkpoints are atomic and were written every 500 original boxes, with more frequent checkpoints during refinement. certificates_depth4.json and certificates_depth10.json preserve earlier stages; discover.py and refine.py support continuing from saved work.

OPEN: A full theorem on region (11) at N=6 is not asserted. Strict positivity on the feasible parts of the nine retained boxes needs a different certificate form, such as a nonnegative Bernstein remainder combined with a positive multiplier of a strict constraint, or an additional local theorem near the equality limits. Deeper finite splitting alone cannot meet the two strictly signed forms specified in the task.

Task: “STRAT12: close the 13,368 OPEN leaves of T104 5+1 region (11), N=6, by constrained Bernstein certificates” — received 2026-11-13 10:26 +04.
