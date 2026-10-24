import pathlib,json
p=pathlib.Path('.')
claims=[
('For every beta>0, s>=0 and theta in [0,2pi], the stopped terminal-zero probability is H(s,theta)=1-(theta+s)/(2pi)+(s/(2pi))E[exp(-(beta/4)tau)]; at theta=0 it equals the bulk gap probability.','proved','ATTEMPT.md, Section 2','No closed nonlinear differential identity for this hitting transform has been proved.','Bounded stopped SDE, uniformly L2-bounded martingale, finite quadratic variation, bounded convergence.'),
('At zero drift the terminal-zero profile is H(0,theta)=1-theta/(2pi); interior starting points never hit either endpoint at finite time.','proved_special_case','ATTEMPT.md, Section 3','This zero-drift case does not solve the positive-gap Painleve derivation.','Exact bounded-martingale expectation and Lamperti SDE with bounded drift.'),
('The carousel generator is -cs partial_s+cs partial_theta+(1-cos theta)partial_thetatheta; the cotangent transform and discounted-hitting operator identity are exact.','proved','ATTEMPT.md, Section 4','Applying classical boundary derivatives to the physical probability requires regularity not assumed here.','Ito calculation; check_math.py checks operator identities symbolically.'),
('On an interval s>0, all formal differentiated entrance equations admit a unique smooth jet sequence for every arbitrary smooth boundary trace g.','proved','ATTEMPT.md, Section 5','No convergence of the formal theta expansion or extension to a globally bounded PDE solution is asserted.','Leibniz rule and triangular induction; check_math.py verifies first 12 equations; BoundaryAlgebra.lean checks the algebraic triangular step.'),
('The bulk sigma-PV equation admits Sigma(r)=-ar for every a. Normalization G(0)=1 and the physical intensity slope do not select the physical gap branch.','proved','ATTEMPT.md, Section 6','Extra source-side branch data and physical selection are needed; this is not a counterexample to Virag Question 9.','Exact substitution; SymPy check; BoundaryAlgebra.lean polynomial cancellation.'),
('Using the external Sine_2 determinantal theorem, G_2(s)=1-s/(2pi)+s^4/(576pi^2)+O(s^5), so the exponential PV branch is not the physical gap.','proved_special_case','ATTEMPT.md, Section 6','This determinant calculation is an external consistency check, not a generator-to-Painleve proof.','Gram determinant bound, two-point Taylor expansion, absolute Fredholm-series remainder estimate.'),
]
with (p/'CLAIMS.jsonl').open('w',encoding='utf8') as f:
 for claim,status,loc,gap,checks in claims:f.write(json.dumps({'problem_id':'D0047','claim':claim,'status':status,'proof_location':loc,'remaining_gap':gap,'checks':checks},ensure_ascii=False)+'\n')
# Show exact source wording, bibliography headers and preserved proof/check file sizes.
t=(p/'source.txt').read_text(encoding='utf8');i=t.find('Question 9');print(t[i:i+240])
print((p/'rumanov.txt').read_text(encoding='utf8')[:1900])
for n in ['STATUS.md','ATTEMPT.md','LITERATURE.md','CLAIMS.jsonl','lean_check.txt','checks.txt']:
 if (p/n).exists():print(n,(p/n).stat().st_size)
