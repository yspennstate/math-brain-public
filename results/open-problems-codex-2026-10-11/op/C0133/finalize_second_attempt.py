from pathlib import Path
import json

root = Path(__file__).resolve().parent
lean = json.loads((root / 'fresh_history_lean_result.json').read_text(encoding='utf-8-sig'))
assert lean['returncode'] == 0, 'Do not finalize without the corrected check passing.'
source = (root / 'FreshHistoryChecks.lean').read_text(encoding='utf-8-sig')
assert 'sorry' not in source and 'native_decide' not in source
claims = [json.loads(line) for line in (root / 'CLAIMS.jsonl').read_text(encoding='utf-8-sig').splitlines() if line.strip()]
checks = ['Complete handwritten proof in FRESH_HYPERPLANE_PROOF.md; thirteen-point hostile review in FRESH_HYPERPLANE_REFEREE.md.',
          'Exact published input hypotheses checked; deterministic path input also independently proved in DETERMINISTIC_PLANE_LEMMA.md.',
          '65,536 planar eight-step paths and 108,130 finite cover cases checked; exact rational posterior-freshness stress test.',
          'FreshHistoryChecks.lean passed exit 0, no sorry/native_decide; scope is finite weighted likelihood steps, not the whole probability proof.']
full = {'problem_id': 'C0133',
        'claim': 'For spatially IID elliptic cookie stacks on Z^d, X_n/n converges to zero almost surely on the complement of spatial transience, simultaneously yielding the result for every direction.',
        'status': 'proved', 'proof_location': 'FRESH_HYPERPLANE_PROOF.md Sections 1-6',
        'remaining_gap': '', 'checks': checks}
for i, item in enumerate(claims):
    if item['claim'].startswith('Candidate full proof'):
        claims[i] = full
    if 'infinitely exchangeable annealed arrow stacks' in item['claim']:
        item['remaining_gap'] = 'Arrow exchangeability is a special-class assumption; the general case is separately proved by the fresh-hyperplane argument.'
        item['checks'].append('Exact Zerner Theorem 1 verified and its special-case application completed in SECOND_ATTEMPT.md Section 8.')
new = [
    {'problem_id':'C0133', 'claim':'Under IID, EL, almost-sure infinite range and P(A_e)=0, every deterministic finite history ending on its initial coordinate plane has shifted fresh-half-space positive-excursion probability p_pi,L tending to zero.',
     'status':'proved', 'proof_location':'FRESH_HYPERPLANE_PROOF.md Sections 1-2', 'remaining_gap':'', 'checks':checks[:2]+checks[3:]},
    {'problem_id':'C0133', 'claim':'The pre-history conditional bound at a first fresh plane implies an almost-sure empirical excursion-frequency bound via bounded martingale differences in residue classes; bounded plane-visit diameter gives a finite-history cover.',
     'status':'proved', 'proof_location':'FRESH_HYPERPLANE_PROOF.md Sections 3-5', 'remaining_gap':'', 'checks':checks},
    {'problem_id':'C0133', 'claim':'The target zero-speed conclusion holds for infinite exchangeable annealed arrow stacks by an exact IID strictly elliptic RWRE representation.',
     'status':'proved_special_case', 'proof_location':'SECOND_ATTEMPT.md Sections 1-3, 5 and 8', 'remaining_gap':'This is a special class; the general conclusion is proved separately.',
     'checks':['Full finite-alphabet representation and ellipticity proofs; exact source verification of Zerner (2002), Theorem 1, p.192.']},
    {'problem_id':'C0133', 'claim':'An IID uniformly elliptic two-cookie planar model with opposite horizontal biases cannot have the same averaged path law as any IID Markovian RWRE with the same first-step marginals.',
     'status':'counterexample', 'proof_location':'SECOND_ATTEMPT.md Section 6', 'remaining_gap':'Counterexample to universal RWRE representation only; it does not contradict C0133.',
     'checks':['Exact three-step probabilities 3/256 versus at least 4/256; SecondChecks.lean checked the algebra with exit 0.']}
]
claims.extend(new)
(root / 'CLAIMS.jsonl').write_text(''.join(json.dumps(c,ensure_ascii=False)+'\n' for c in claims),encoding='utf-8')
(root / 'fresh_candidate_claim.json').write_text(json.dumps(full,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
with (root / 'CHECK_HISTORY.md').open('a',encoding='utf-8') as out:
    out.write('\n\n2026-10-12 second attempt: SecondChecks.lean passed five finite algebraic identities/inequalities; fresh_history_experiments.py passed exact finite cover and likelihood stress tests. FreshHistoryChecks.lean first failed to parse ASCII membership notation, then passed after the Unicode membership and explicit Finset.sum correction. Final exit code: 0; elapsed seconds: '+str(lean['elapsed_seconds'])+'. Axioms: propext, Classical.choice, Quot.sound. No sorry/native_decide. Full stochastic proof is handwritten, not formally certified by these finite checks. The deterministic plane lemma was independently reproved and its limit order reviewed.\n')
status = (root / 'STATUS.md').read_text(encoding='utf-8-sig').splitlines()
status[0] = 'STATE: DONE'
status[1] = 'NEXT: None required for this attempt; full proof and referee record are ready for independent mathematical review.'
status[2] = 'VERDICT: SOLVED'
status.append('2026-10-12: Closed the second attempt with a complete proof under exactly IID and EL. The new finite-history fresh-hyperplane domination plus a martingale frequency law contradicts positive limsup speed when directional escape has probability zero. The published range/slab/two-sided zero-one results finish the vector statement. Thirteen possible failures checked, deterministic lemma proved independently, exact finite tests passed, and corrected finite likelihood Lean checks passed exit 0. No remaining mathematical gap identified. This is an original proof, not SOLVED_IN_LITERATURE; the full stochastic argument is not claimed Lean-formalized.')
(root / 'STATUS.md').write_text('\n'.join(status)+'\n',encoding='utf-8')
print('STATE: DONE; VERDICT: SOLVED;',len(claims),'claims recorded; finite likelihood Lean exit',lean['returncode'])
