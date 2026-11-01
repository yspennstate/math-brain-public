from pathlib import Path
import json
P=Path('.')
# Reconcile claims immediately, preserving the formerly conjectured target as a refuted claim.
p=P/'CLAIMS.jsonl';rows=[json.loads(l) for l in p.read_text(encoding='utf8').splitlines()]
for c in rows:
 if c['status']=='conjecture' and '(MB)' in c['claim']:
  c.update(claim='The matching bound (MB) proposed in the first attempt is false for every nonzero principal charge under the stated cell embedding; it also fails with all eight lattice faces distinct at s=1/4.',status='counterexample',proof_location='SECOND_ATTEMPT.md A1 and A4',remaining_gap='This refutes the auxiliary hypothesis, not the electric-field scaling limit. A corrected Onsager bound OB remains unproved.',checks='Rational fusion is exact; irrational fusion uses Dubedat Proposition 23. Distinct-face proof uses a 3x3 occupation determinant, nonnegative two-edge probability, and proved mixing; numerical and Lean checks supplied.')
 if c['claim'].startswith('A uniform balanced dimer matching bound (MB)'):
  c['remaining_gap']='MB has now been refuted for the actual embedding, so this implication is only formal. The usable corrected conditional result is OB -> convergence in SECOND_ATTEMPT.md A3b.'
new=[
('The full two-cluster fusion region that defeats MB nevertheless contributes at most C epsilon^(4(n-1)-2n s^2) to integrated 2n-point moments, hence vanishes for n>=2 and |s|<1/2.','proved','SECOND_ATTEMPT.md A2','Other partial and mesoscopic collision configurations need different estimates.','Direct cell-count volume and modulus-one bound; exponent positivity checked in FusionExponents.lean.'),
('For any bounded planar K, m>=2, and 0<q<1, the nearest-neighbor majorant product_a min_(b!=a)|z_a-z_b|^(-q) is integrable on K^m and has a quantitative collision-tail bound.','proved','SECOND_ATTEMPT.md A3a','This is a geometric integration theorem; no dimer estimate follows automatically.','Expansion into functional directed graphs; leaf integration; cycle Cauchy-Schwarz; L^(1+delta) and Holder.'),
('If the corrected nearest-neighbor Onsager estimate OB holds for the principal-charge dimer field, phase-randomized renormalized fields converge in law locally in H^(-t), t>1, to the imaginary Gaussian chaos candidate.','proved_special_case','SECOND_ATTEMPT.md A3b','OB is unproved; the original pinned phase and endpoint remain unresolved.','Explicit integrable majorant repairs dominated convergence; uses existing separated-point theorem and prior tightness/moment-determination proof.'),
('The corrected dimer Onsager estimate OB for all n and arbitrary collisions is a sufficient new target.','conjecture','SECOND_ATTEMPT.md A3','Not proved; no claim of transfer from Ising or Gaussian correlation inequalities.','n=1 follows from the verified two-point bound; exact fusion cases are compatible but do not prove general n.'),
('At s=1/4 the product of electric fields at four consecutive faces is a local three-edge observable with mean modulus D>=1/4; its correlation with a distant even translate tends to D^2>=1/16.','proved_special_case','SECOND_ATTEMPT.md A4','Canonical infinite-volume uniform square-grid measure only; this is a fusion statement, not the desired field limit.','Full Fourier inverse and decay argument, occupation determinant D=7/16+c/2-c^2, probability c^2<=1/16; Lean lower bound.'),
('Exact finite fusion and numerical canonical-kernel computations support the charge-fusion formulas and local determinant calculation.','numerical_evidence','fusion_checks.py; fusion_checks.json; distinct_fusion_checks.py; distinct_fusion_checks.json; local_fusion_symbolic.txt','Fourier quadrature has no certified error bound and is not used to establish nonvanishing.','281 exhaustive finite tilings at five rational charges; 455 distinct four-face cluster scans; grids 64 through 512; exact SymPy polynomial expansion.')
]
for claim,status,loc,gap,checks in new:rows.append({'problem_id':'F0087','claim':claim,'status':status,'proof_location':loc,'remaining_gap':gap,'checks':checks})
p.write_text(''.join(json.dumps(c,ensure_ascii=False)+'\n' for c in rows),encoding='utf8')
print('Saved',len(rows),'reconciled claims.')
