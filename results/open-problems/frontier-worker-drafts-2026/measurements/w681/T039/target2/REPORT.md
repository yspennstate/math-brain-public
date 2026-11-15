The operator criterion in the unmodified positive radial reduction reaches its numerical ceiling near rho = 0.44101422. Its Hilbert–Schmidt norm with the published center crosses 2 near 0.43251274. Equation (139) and its sharpened form (142) show no grid failure. These are numerical estimates; no new Gaussian noise-stability interval is proved.

Target 1(a) reproduces the published output exactly. Commit `6b720fe57bfe2a3c8fffc51521d00b31011aa1a3`, unmodified `plur_cert_positive.py`, gives 90 accepted slabs from 150 attempts, worst slab [0.38625,0.3875], finite upper 3.99929063236 and total certified upper 3.99929096609. Runtime here is 424.84 seconds. The full output and dependency/input hashes are in `logs/reproduction.txt` and `logs/reproduction_metadata.json`.

Targets 1(b,c) use the literal center in (150), literal kernel in (149) and denominator in (148). The weighted operator is compressed to the mean-zero subspace; additive centering cancels there. Radial Gauss–Legendre Nyström quadrature gives:

| Radial nodes | Cutoff | Angular nodes | rho_HS | rho_op |
|---:|---:|---:|---:|---:|
| 256 | 20 | 128 | 0.432512741320 | 0.441014219195 |
| 512 | 20 | 192 | 0.432512741320 | 0.441014219195 |
| 768 | 30 | 256 | 0.432512741320 | 0.441014219195 |

The largest root drift is 4.54e-13. This is observed convergence, not a rigorous error bar. The 56-point sweep covers [0.4,0.95] in steps of 0.01. The largest positive eigenvalue controls the operator norm throughout the sweep; the negative branch is small. Representative values follow (256 nodes, cutoff 20, 128 angular nodes):

| rho | HS norm | Mean-zero operator norm |
|---:|---:|---:|
| 0.40 | 1.89736807 | 1.87963496 |
| 0.43 | 1.99201407 | 1.96774632 |
| 0.44 | 2.02386950 | 1.99703031 |
| 0.45 | 2.05594599 | 2.02631640 |
| 0.50 | 2.22118340 | 2.17377235 |
| 0.60 | 2.59700751 | 2.48646183 |
| 0.70 | 3.09798138 | 2.85705723 |
| 0.80 | 3.88140866 | 3.35750987 |
| 0.90 | 5.40845686 | 4.18092711 |
| 0.95 | 7.04973798 | 4.91265584 |

At rho = 0.4 the finest HS estimate is 1.897368072736 and the operator estimate is 1.879634961484. Their ratio is 1.0094343378, a 0.943434% HS excess. The squared-norm ratio is 1.0189576824. At rho = 0.95, increasing the cutoff from 20 to 30 while fixing 512 radial and 192 angular nodes changes HS by 2.7e-10 and the operator by -1.27e-12. Doubling angular nodes alone at the same cutoff changes HS by -1.59e-12 and the operator by -3.11e-13.

Target 1(d) has no observed failure at any requested rho: 0.45, 0.5, 0.6, 0.7, 0.8 or 0.9. Each rho uses 81 values of a, spanning zero through all radial couplings induced by x,y in [0,7], with logarithmic coverage near zero. Each a uses 621 scalar coordinates (600 uniform panels plus exact simplex coordinates and perturbations near 1/3), and all pairs of the 496 simplex vectors of denominator 30. This is 187,421,526 scalar pairs and 119,563,776 vector pairs per inequality across the run. The largest signed residuals are 6.66e-16 for (139) and 6.66e-16 for (142), at the scale of rounding; the failure threshold is 1e-10. Eighteen selected cases repeat with doubled Fourier truncation. This grid does not prove the inequalities globally. Lemma A.2 and Corollary A.3 already state them for every a >= 0: rho enters only through a = 2rho xy/(1-rho^2).

The checks address the strongest ways these estimates could be wrong: a missing radial Jacobian, a wrong J normalization, failure to impose the weighted mean constraint, a center that changes the constrained operator, inadequate cutoff, or unresolved angular quadrature. Twenty J values agree with a direct radial marginal to relative 3.51e-13. Sixteen K entries agree with independent Bessel arc formulas to relative 2.9e-14. Projection, eigenvector and centered-versus-uncentered controls pass. Cutoff and angular refinements vary one setting at a time. Detailed rows, metadata and commands are saved under `logs/` and `proofs/NUMERICAL_METHOD.md`.

The dossier's 3.99929 is a certified slab upper bound, not the actual value of h_+^2. A bound close to 4 at rho about 0.387 does not locate the actual HS crossing. A proposed dossier correction is saved in `patches/01_t039_measured_reach.diff`; the live dossier is untouched.

Target 2 is worth a modest certification effort below approximately 0.441. HS alone has room until approximately 0.4325, so interval refinements may already extend the published 0.4 range. A certified operator estimate may recover the small further gap. The unmodified operator is numerically above 2 by rho = 0.45; reaching 0.615 requires a stronger estimate or another reduction. The hardest remaining piece is a rigorous infinite-dimensional upper bound over a whole rho interval, with every quadrature and tail error enclosed. No theorem beyond the published range is claimed.

Primary sources: Steven Heilman, [arXiv:2608.00333v1](https://arxiv.org/abs/2608.00333v1), Sections 1.3–1.4, 8–9, Appendix A pp.38–43, especially (139), (142), (148)–(152) and Lemma A.4; [author's certificate at the pinned commit](https://github.com/sheilman77/cut_bounds/tree/6b720fe57bfe2a3c8fffc51521d00b31011aa1a3). PDF pages 40–41 were inspected visually to restore the symbols dropped by extraction. Primary abstract metadata confirms author, v1 date and arXiv nonexclusive distribution license. Brain queries did not return the aligned-arc or positive-simplex results; attributed card drafts and the numerical owner-work draft are staged under `bundles/`, inside this task's permitted folder, for the reviewer to copy to the inbox.

2026-10-14T22:32:35.694571+00:00 | 1(a) | Certificate reproduction completed and measured.
2026-10-14T22:32:35.694571+00:00 | 1(b) | Literal published-center HS crossing estimated and refined.
2026-10-14T22:32:35.694571+00:00 | 1(c) | Weighted mean-zero norm crossing estimated and refined; independent normalization and centering controls passed.
2026-10-14T22:32:35.694571+00:00 | 1(d) | All requested arc grids completed; no failure candidate.
Rung: numerical evidence for the extension; reproduction of an existing directed certificate for the published range. No independent PASS has been received.
NEXT: Reviewer audit T039-C001–C003 v1 and the proposed dossier correction, then decide staffing for target 2.

2026-10-14T22:42:12.550800+00:00 | PACKAGE | Four card drafts and one measured hook proposal staged locally; exact edge quotes and dependency graph checked. Log encoding originals preserved. Chart visually inspected. Source/script hashes match the experiment metadata. All assigned foreground computations completed; no process is left running by this task.

2026-10-14T22:50:13.915332+00:00 | RECONCILE | Original package identities rechecked; target 1(a)-(d) remain complete, with no repeated mathematical run. The repeated reminder reads the superseded parent checkpoint. Task status remains NEEDS_REVIEW for an agent.

2026-10-15T00:13:28.167132+00:00 | ARCHIVE | 33 research-evidence files archived on main; exact source blobs checked, outgoing secret scan clean, remote tree verified. Link: https://github.com/yspennstate/brain-repo/tree/6b2032d48b9cae20e9d87d0614f7b477ad28d2cf/06_math_research/frontier/measurements/w681/T039. The archive retains numerical-evidence status and unreviewed card/hook drafts. No math store or live dossier was changed; no mathematical computation was repeated.
NEXT: T039 target 1 reviewer audit C001-C003 v1; decide target 2 after that review.

2026-10-15T00:31:59.174849+00:00 | CLOSED | All deliverables and the verified archive are saved; 53 manifested files passed the final hash check. The handoff lease was released. The administrative completion marker could not synchronize because the shared checklist lock stayed held; its error is preserved in logs/closure_actions.txt and no lock was changed. No task process remains running. NEXT: an agent audits T039-C001-C003 v1.

2026-10-15T01:23:12.653225+00:00 | Target 2: C004 comparison lemma saved. Initial -I import failed, intentionally tiny smoke had no positive J lower enclosure, and full-size pilot hit its 580 s limit before producing a bound. Switched to smaller checkpointed tables and the analytic J lower bound; no interval extension claimed yet.

2026-10-15T01:56:15.882612+00:00 | T039 target 2 initial prefix: three directed slabs prove operator upper <= 1.998371111346653 <2 on [0.40,0.4015], extending the source theorem to rho=803/2000. Proof unaudited. Witness/coverage validation and proof saved; remaining endpoint work continues.
2026-10-15T02:43:50.070982+00:00 | Target 2 fine prefix: {"at": "2026-10-15T02:43:50.070982+00:00", "command": ["C:\\Python314\\python.exe", "-B", "-X", "utf8", "~\\brain_workers\\w681\\T039\\scripts\\run_fine_certificate.py", "--max-seconds", "360"], "exit_code": 3, "run_log": "logs\\fine_chunk_20261015T023836Z.txt", "endpoint": 0.42275, "accepted_slabs": 32, "pending_slabs": 29, "worst_operator_upper": 1.9994729860206248, "complete": false}
2026-10-15T02:48:43.844664+00:00 | ARCHIVE RECEIPT RECOVERED | Development draft main=100d154300c9964843ea6e2baf9de5e9f196bebc, base=adbc2dcc993955e01f678aab00776b8cb19d7d63; outgoing secret scan clean; push and first ls-remote in target2_publication_delivery.txt verify delivery. A redundant final ls-remote timed out. This archive predates the new interval certificate.
2026-10-15T02:55:30.590929+00:00 | Target 2 fine prefix: {"at": "2026-10-15T02:55:30.590929+00:00", "command": ["C:\\Python314\\python.exe", "-B", "-X", "utf8", "~\\brain_workers\\w681\\T039\\scripts\\run_fine_certificate.py", "--max-seconds", "480"], "exit_code": 3, "run_log": "logs\\fine_chunk_20261015T024837Z.txt", "endpoint": 0.426, "accepted_slabs": 45, "pending_slabs": 16, "worst_operator_upper": 1.9994729860206248, "complete": false}
2026-10-15T03:06:24.288487+00:00 | Target 2 fine prefix: {"at": "2026-10-15T03:06:24.288487+00:00", "command": ["C:\\Python314\\python.exe", "-B", "-X", "utf8", "~\\brain_workers\\w681\\T039\\scripts\\run_fine_certificate.py", "--max-seconds", "480"], "exit_code": 3, "run_log": "logs\\fine_chunk_20261015T025944Z.txt", "endpoint": 0.4275, "accepted_slabs": 51, "pending_slabs": 10, "worst_operator_upper": 1.9994729860206248, "complete": false}
2026-10-15T03:11:56.067335+00:00 | ARCHIVE PREPARED | {"at": "2026-10-15T03:11:56.067335+00:00", "repository": "https://github.com/yspennstate/brain-repo.git", "checkout": "~\\brain_workers\\w681\\T039\\publication_checkout", "base": "3fcf4d79a80a10cc99067798244e77688e13da52", "head": "cee186e154a61f3ac60469bd2092ba24cfbfff19", "files": 84, "changed_files": 79, "source_bytes": 6516364, "endpoint": 0.4275, "state": "prepared; clean outgoing scan and verified delivery required"}
2026-10-15T03:19:55.542773+00:00 | Target 2 fine prefix: {"at": "2026-10-15T03:19:55.542773+00:00", "command": ["C:\\Python314\\python.exe", "-B", "-X", "utf8", "~\\brain_workers\\w681\\T039\\scripts\\run_fine_certificate.py", "--max-seconds", "480"], "exit_code": 3, "run_log": "logs\\fine_chunk_20261015T031211Z.txt", "endpoint": 0.429, "accepted_slabs": 57, "pending_slabs": 4, "worst_operator_upper": 1.9994729860206248, "complete": false}
2026-10-15T03:27:29.383210+00:00 | ARCHIVE STUCK | Numerical cache ignore refusal fixed by explicitly naming three verified .npz files. Subsequent publisher exhausted its two push attempts; inspect target2_progress_delivery.txt before another approach. No delivered state claimed.
2026-10-15T03:29:18.632681+00:00 | Target 2 fine prefix: {"at": "2026-10-15T03:29:18.632681+00:00", "command": ["C:\\Python314\\python.exe", "-B", "-X", "utf8", "~\\brain_workers\\w681\\T039\\scripts\\run_fine_certificate.py", "--max-seconds", "480"], "exit_code": 0, "run_log": "logs\\fine_chunk_20261015T032437Z.txt", "endpoint": 0.43, "accepted_slabs": 61, "pending_slabs": 0, "worst_operator_upper": 1.9994729860206248, "complete": true}
2026-10-15T03:33:34.397821+00:00 | ARCHIVE CAS RECOVERY | unpublished head=d8491b8883eeabf3f5b893145410dd8b5573d282, parent=e33be0fb350de1f4568487ba164148aaa203577e; all 79 changed paths verified in own scope. Recognize remote main CAS races, fetch/rebase and scan anew; never force push.
2026-10-15T03:40:03.487189+00:00 | TARGET 2 COMPLETE / UNAUDITED | C005 v2: full operator norm <= 1.9994729860206248 < 2 over [0.40,0.43]; 61 slabs. Combined theorem [0.10,0.43]. Radial cells replace the proposed Laguerre basis. Exact validation and all proof files saved.
2026-10-15T03:40:05.164744+00:00 | BRAIN DRAFTS | bundle_002.json: an elementary operator-bound lemma, an explicitly unaudited own-work extension record, and the attributed Heilman radial-weight lower bound (153), with an exact quoted dependency rationale. Complete-tail hook staged locally. No live ingestion or hook installation performed.
2026-10-15T03:51:02.132680+00:00 | ARCHIVE VERIFIED | main=8e6168da151ef91cdc88ff5d1091d80b7449507a, 84 files, secret scan clean, remote tree matched; this snapshot covers .4275. Final .43 snapshot follows.
2026-10-15T03:51:02.132680+00:00 | FINAL LOCAL CHECK | C005 v2, 61 slabs, exact endpoint coverage and final arithmetic; endpoint matrix and all 4000 witness rows recomputed; 3-card bundle and quoted relation validated; checklist complete; independent audit pending.
2026-10-15T03:57:23.942181+00:00 | ARCHIVE PREPARED | {"at": "2026-10-15T03:57:23.942181+00:00", "repository": "https://github.com/yspennstate/brain-repo.git", "checkout": "~\\brain_workers\\w681\\T039\\publication_checkout", "base": "7a6505b8b4c9590a45b6efb8308230893942adec", "head": "330649824007c60a77ddaf2853c49088f0b0eb66", "files": 115, "changed_files": 40, "source_bytes": 8612933, "endpoint": 0.43, "state": "prepared; clean outgoing scan and verified delivery required"}

2026-10-15T04:10:20.520279+00:00 | Archive recovery: the final certificate is complete; publication rebase stopped on three generated files (CLAIMS_DRAFT.jsonl, README.md, SNAPSHOT_MANIFEST.json) changed by the already delivered partial snapshot. Resolve these against the full rho=.43 payload, preserving all peer paths; no scientific rerun. Earlier remote main compare-and-swap race and ignored NPZ staging are recorded and handled by bounded race retries and three explicitly hash-checked additions.

2026-10-15T04:12:08.680983+00:00 | ARCHIVE RECOVERY | Three generated files resolved from the complete rho=.43 snapshot; older partial payload confirmed. Peer paths preserved. Route history closed; Laguerre scope mismatch and looser rescaling explicitly marked dead. Certificate remains proof (unaudited), pending C005 v2/C004 v2 review.
