import json,pathlib
root=pathlib.Path(__file__).resolve().parent
claims=[
{'problem_id':'P0331','claim':'In d>=3 the homogeneous mean-zero periodic Coulomb ensemble has uniform stability and local whole-point-process TV bounded by sqrt(2^(d-1) ell^d (C_d beta+(1+log N)/N)) for cubes of side ell<=L/2, L=N^(1/d)>=8.','status':'proved_special_case','proof_location':'SECOND_ATTEMPT.md Section 3','remaining_gap':'Periodic ensemble only; beta ell^d->0 is smaller than the full sub-Debye range. No source-boundary transfer or energy sharpness.','checks':'Correct positive torus shell shift and self term; heat-kernel positivity with absolute Fubini; entropy conditioning and geometry; Ewald quadrature.'},
{'problem_id':'P0331','claim':'In full-space d=3 a local law within fixed small TV of unit PPP on a growing cube forces the source corrected local energy F_Omega+C0*n to exceed c R^2 with fixed positive probability. This applies to most bulk cells in the explicit entropy regime.','status':'proved_special_case','proof_location':'SECOND_ATTEMPT.md Section 4','remaining_gap':'R^2 is smaller than the allowed R^3 volume energy; no sharpness contradiction.','checks':'Uses source Lemma 7.8 (7.1.36), exact spherical Taylor error, Poisson fourth moments and event-only TV transfer.'},
{'problem_id':'P0331','claim':'For the mean-zero periodic d=3 ensemble, the unproved uniform bound log Z_N(2 beta)<=C N beta^(3/2) would imply whole-point-process TV convergence for all ell=o(beta^(-1/2)) with ell^3 log N/N->0.','status':'proved_special_case','proof_location':'SECOND_ATTEMPT.md Section 7','remaining_gap':'Debye-Huckel finite-volume free-energy premise is unproved here; periodic/source-boundary and energy-sharpness gaps remain.','checks':'Convexity secant inequality and exact relative entropy identity give D/N<=f_N(2 beta); then apply proved spatial entropy lemma.'}]
f=root/'CLAIMS.jsonl'
existing=[json.loads(s) for s in f.read_text(encoding='utf8').splitlines()]
with f.open('a',encoding='utf8') as out:
    for c in claims:
        if c['claim'] not in [x['claim'] for x in existing]: out.write(json.dumps(c)+'\n')
print('Periodic, actual-energy lower bound, and conditional-reduction claims saved.')
