import json
from pathlib import Path
root=Path(__file__).resolve().parent
cert=json.loads((root/'evidence/P0242_family.json').read_text(encoding='utf-8'))
text='''# P0242: stationary-flow lumping has asymptotic amplification 3/2

Label: proof candidate with an exact algebraic certificate; independent audit PENDING w347. This supplies a lower bound on any universal comparison constant, not an upper bound or a complete solution. No novelty claim.

Earlier work read: the original store attempt requiring strong lumpability, and `Probability_P0242_Aldous_Fill_open_problem_4_45_lumping_2026-09-14.md`. The latter disproves K=1 and reports a finite witness with ratio 1.48220..., but explicitly has no asymptotic argument. The source is Aldous--Fill, Open Problem 4.45, PDF p.149 of the 2014 recompilation, and its stopping-time/halting-state identity.

For s>0 take the following symmetric weight matrix on states 0,1,2,3:

    W = [[0, 0, 1, 0],
         [0, 2s, 1, 2s],
         [1, 1, 0, s],
         [0, 2s, s, 4s^2]].

Let w_i be its row sums: (1,4s+1,s+2,4s^2+3s), with total 4(s+1)^2. The discrete chain P_ij=W_ij/w_i is irreducible and reversible with pi_i=w_i/(4(s+1)^2). Set Q=P-I if using the rate-one continuous-time version. Lump states 2,3 into A by stationary flows. The coarse symmetric weights, in order 0,1,A, are

    W_hat = [[0, 0, 1],
             [0, 2s, 2s+1],
             [1, 2s+1, 4s^2+2s]].

This is stationary-flow lumping, rather than strong lumpability: from state 2 the transition probability into {0} is 1/(s+2), whereas from state 3 it is zero.

For each target j let H_ij be the expected hitting time, the unique solution of H_jj=0 and -sum_k Q_ik H_kj=1 for i!=j. The standard optimal-stopping identity is

    t_stop(P) = max_(i,j) D_ij,
    D_ij = H_ij - sum_k pi_k H_kj.

It applies to randomized stopping times with stationary terminal law. The same linear systems compute the rate-one continuous-time quantity. The certificate below lists every rational D entry. `p0242_family.py` verifies the hitting equations, stationarity, and detailed balance as symbolic identities, with no floating point arithmetic. Uniqueness of the hitting solutions follows from irreducibility, so these identities identify the actual H matrices.

The entrywise limits as s tends to infinity are:

    D -> [[-infinity, 2, -infinity, 2],
          [2, -infinity, 1, 2],
          [-infinity, 1, -infinity, 1],
          [2, 2, 1, 0]],

    D_hat -> [[-infinity, 3, 1],
              [3, -infinity, 2],
              [1, 2, 0]].

Each limit is obtained by comparing numerator and denominator degrees and leading coefficients in the exact expressions below. For a fixed finite collection, the limit of its maximum is the maximum of its extended-real limits when at least one is finite. Consequently t_stop(P_s) tends to 2 and t_stop(P_hat_s) tends to 3, and their ratio tends to 3/2. Any constant K valid for all reversible chains and stationary-flow lumpings must therefore satisfy K>=3/2.

This proof does not establish existence of a universal K, or that 3/2 is sufficient. The dependency on the standard stopping-time identity, the precise stationary-flow convention, and the entire rational certificate must be independently checked before promotion.

Exact D entries (row i, column j):

'''
for name,key in [('fine','fine_D'),('coarse','coarse_D')]:
    text+=name+'\n\n'
    for i,row in enumerate(cert[key]):
        for j,expr in enumerate(row):
            text+=f'    D[{i},{j}] = {expr}\n'
    text+='\n'
text+='Checks: '+str(cert['exact_residual_checks'])+' symbolic residual identities passed in '+str(round(cert['elapsed_seconds'],3))+' seconds. Eight exact parameter values were evaluated; at s=1000 the ratio is '+cert['table'][-1]['ratio']+' = '+str(cert['table'][-1]['ratio_float'])+'.\n\nNEXT: w347 independently verify the stopping-time identity and certificate; then add the lower-bound lemma and edges to the P0242 problem and earlier attempt.\n'
(root/'proofs/P0242.md').write_text(text,encoding='utf-8')
row={'row_id':'S1.O.w333.006','problem_id':'P0242','result_type':'lemma','label':'proof candidate; exact symbolic certificate','statement':'Any universal stationary-flow-lumping comparison constant for worst optimal expected stationary stopping times of finite reversible chains must be at least 3/2. The explicit four-state family has fine t_stop ->2 and coarse t_stop ->3.','proof_path':(root/'proofs/P0242.md').as_posix(),'measurement':{'checks':50,'parameter_values':8,'ratio_at_1000':cert['table'][-1]['ratio'],'elapsed_seconds':cert['elapsed_seconds']},'audit_status':'PENDING w347','source_quote':'The K half remains open: the two constructions above stay below 1.5, and I have no argument in either direction.'}
with (root/'results.jsonl').open('a',encoding='utf-8') as f:
    f.write(json.dumps(row)+'\n')
print(row['row_id'],'saved; candidate universal K lower bound 3/2')
