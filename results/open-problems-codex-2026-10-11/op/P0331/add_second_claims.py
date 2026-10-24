import json,pathlib
r=pathlib.Path(__file__).resolve().parent
claims=[
dict(problem_id='P0331',claim='An exchangeable N-point law on a volume-N set with labeled relative entropy <=B has sum of spatial marginal divergences from unit PPP <=B+h_N, where h_N<=1+log N.',status='proved',proof_location='SECOND_ATTEMPT.md Section 1',remaining_gap='Entropy lemma, not energy sharpness.',checks='Exact canonical conditioning and product-reference decomposition included.'),
dict(problem_id='P0331',claim='For the full-space hard-cube Coulomb ensemble in d>=3, mean squared cell point-process TV is <=(K_d beta v+v(1+log N)/N)/2. At beta=N^(-1/3) in d=3 this gives growing bulk windows of side order N^(1/12) with random-cell TV O(N^(-1/24)).',status='proved_special_case',proof_location='SECOND_ATTEMPT.md Section 2',remaining_gap='Spatial average and most cells, not every prescribed center. No electric-energy-law contradiction.',checks='Prior complete stability proof; exact entropy lemma; temperature and bulk buffer exponents checked.')]
f=r/'CLAIMS.jsonl'
old=[json.loads(s) for s in f.read_text(encoding='utf8').splitlines()]
with f.open('a',encoding='utf8') as out:
    for c in claims:
        if c['claim'] not in [x['claim'] for x in old]: out.write(json.dumps(c)+'\n')
print('Second-attempt claims saved.')
