from pathlib import Path
import json
P=Path('.')
p=P/'LITERATURE.md';s=p.read_text(encoding='utf8').replace('Authors require independent metadata verification before citation in a paper.','Both authors were verified directly in the retrieved arXiv Atom author fields.');p.write_text(s,encoding='utf8')
p=P/'ATTEMPT.md';s=p.read_text(encoding='utf8').replace('as in the cited construction and moment results.','by Corollary 3.11 and formula (3.4) of Junnila–Saksman–Webb (PDF pp.26–28), which justify precisely this moment passage for smooth log-covariance regular parts.')
insert=r'''
### Explicit counterexample to an invalid inference
Separated-point moment convergence plus negative-Sobolev tightness alone does not justify integrating a limiting correlation kernel. On the unit flat torus let A be uniform, let ζ be an independent uniform unit complex phase, and let Q_epsilon(A) be the axis-aligned torus square of side epsilon centered at A. Set

    S_epsilon(z)=ζ epsilon^(−2) 1_{Q_epsilon(A)}(z).

For any fixed distinct z,w, E S_epsilon(z)overline(S_epsilon(w))=0 once epsilon is smaller than their torus distance divided by sqrt(2): they cannot both lie in the square. Its expectation is also zero. Every fixed multipoint moment at distinct insertions is eventually zero: moments of nonzero net phase vanish, and a balanced moment with at least two insertions requires the same square to contain two distinct fixed points.

However S_epsilon(φ)=ζ epsilon^(−2)∫_{Q_epsilon(A)}φ(z)d²z tends almost surely to ζφ(A). The error is at most the uniform modulus of continuity of φ at distance sqrt(2)epsilon. Thus the limit distribution is ζδ_A, not zero. For t>1 this convergence even holds in H^(−t): each Fourier coefficient converges, its absolute value is ≤1 (with normalized unit-torus basis), and the summable sequence (1+|k|²)^(−t) dominates the squared coefficient errors up to a factor 4. Dominated convergence in the Fourier series proves the assertion. The limiting second moment of a test pairing is ∫|φ|², despite all separated two-point kernels being eventually zero.

This is a counterexample to a reasoning shortcut, **not a dimer counterexample**. Its spike amplitude epsilon^(−2) is different from that of the electric field here. It makes explicit why P6 cannot drop the collision hypothesis merely because P2a establishes tightness.

'''
s=s.replace('## 8. Hostile-referee audit and remaining gaps',insert+'## 8. Hostile-referee audit and remaining gaps');p.write_text(s,encoding='utf8')
claims=[
('For the pinned quarter-normalized domino height, h(f) modulo Z is the stated parity table; charge shifts by 2pi have a deterministic lattice phase and full observable period 8pi.','proved_special_case','ATTEMPT.md §2; HeightResidue.lean','No scaling-limit identification follows from this algebra.','Lean kernel exit 0; exhaustive finite residues through 6x6.'),
('For the canonical zero-slope infinite-volume uniform square-grid Gibbs measure, alpha not congruent to 0 or pi modulo 2pi, the unrenormalized electric field has test-pairing mean-square decay O(epsilon^(2s^2)), s the principal charge representative.','proved_special_case','ATTEMPT.md §3','Uses Dubedat Proposition 23 as an existing theorem; half-integer charge endpoint and other Gibbs/domain settings not covered.','Checked normalization, finite parity uniformity, Fubini and integrability exponent p<1/2.'),
('In that setting the raw field tends to zero locally in H^(-t) for t>1, and epsilon^(-s^2) times the field is tight locally in H^(-t).','proved_special_case','ATTEMPT.md §3 P2a','Tightness does not identify a nontrivial renormalized limit.','Fourier-series expectation bound; explicit compact-embedding proof.'),
('At alpha=2pi m the pinned embedded field is deterministic and tends to 1 if m is divisible by 4, otherwise to 0.','proved_special_case','ATTEMPT.md §4','An additive height shift changes the global phase; this is not the nontrivial renormalized field.','Four parity-class values and complete-block cancellation.'),
('On finite planar bipartite domino graphs the phase-adjusted twisted Kasteleyn determinant ratio equals the electric correlator.','proved','ATTEMPT.md §5','Asymptotics of twisted determinants still require analysis.','Complete determinant-expansion proof using Kasteleyn enumeration theorem; two-path finite verification.'),
('For the balanced pure-log Gaussian correlation kernel F_p and 0<p<=1, F_p is at most the sum over matchings of products of cross distances to power -p.','proved','ATTEMPT.md §6','No implication to discrete dimer collision estimates has been established.','Complete Cauchy determinant proof and subadditivity proof; 60 exact rational and 450 numerical checks.'),
('A uniform balanced dimer matching bound (MB), together with Dubedat Theorem 24, implies convergence of the explicitly phase-randomized principal-charge field to imaginary Gaussian chaos in local H^(-t), t>1.','proved_special_case','ATTEMPT.md §7','MB is unproved; phase-randomization modifies the pinned original field.','Dominated moment convergence, Gaussian candidate via JSW Theorem 1.1 and Corollary 3.11, moment determination, Sobolev tightness.'),
('The uniform balanced dimer collision estimate (MB) in ATTEMPT.md (7.1) is a plausible sufficient target for the principal-charge renormalized field limit.','conjecture','ATTEMPT.md §7','Not proved even though its Gaussian analog is proved; could require modification.','Only separated-point asymptotics verified; no discrete coalescence estimate claimed.'),
('Separated-point moment convergence and H^(-t) tightness for t>1 do not by themselves justify integration of limiting correlators.','counterexample','ATTEMPT.md §7 explicit counterexample','This is a toy random-square spike, not a counterexample to the dimer problem.','Complete almost-sure test-pairing and Fourier H^(-t) convergence proofs.'),
('Exhaustive tiling enumeration verifies residues and the finite determinant identity on five rectangles through 6x6.','numerical_evidence','finite_checks.py; finite_checks.json','Finite floating-point checks say nothing about infinite-volume asymptotics.','7052 tilings total; determinant discrepancies <9e-16.'),
]
with (P/'CLAIMS.jsonl').open('w',encoding='utf8') as f:
 for claim,status,loc,gap,checks in claims:f.write(json.dumps({'problem_id':'F0087','claim':claim,'status':status,'proof_location':loc,'remaining_gap':gap,'checks':checks},ensure_ascii=False)+'\n')
(P/'STATUS.md').write_text('''STATE: DONE
NEXT: Prove or disprove the uniform balanced dimer collision estimate (MB), then control the pinned phase and alpha congruent to pi modulo 2pi.
VERDICT: PARTIAL
2026-10-11: Confirmed source statement and quarter-height normalization; fetched Kenyon, Dubedat PDF/TeX, and Junnila–Saksman–Webb.
2026-10-11: Searched arXiv, OpenAlex, Crossref, Semantic Scholar, GitHub and read-only brain/ledgers/repository; exact solved-in-literature criterion not met. OpenAlex remained rate-limited; citation coverage is incomplete.
2026-10-11: Proved special-case raw distributional zero limit, deterministic resonances, renormalized tightness, finite determinant reduction, Gaussian collision bound, and conditional random-phase chaos convergence.
2026-10-11: Exhaustive finite tilings and Cauchy identity checks passed; integer path-residue algebra passed Lean kernel check without sorry/native_decide.
2026-10-11: Stopped with collision estimate, half-integer endpoint, pinned-sector identification and general-domain gaps stated precisely in ATTEMPT.md. DONE records completion of this bounded attempt, not solution of the open problem.
''',encoding='utf8')
print('Saved final records:',len(claims),'claims')
