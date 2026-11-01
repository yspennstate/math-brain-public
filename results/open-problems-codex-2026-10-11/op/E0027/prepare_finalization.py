from pathlib import Path
script="""from pathlib import Path
import json
root=Path(__file__).resolve().parent
log=(root/'second_lean_check.log').read_text(encoding='utf-8')
assert 'EXIT_CODE: 0' in log and 'error:' not in log and 'sorryAx' not in log, 'Final Lean run is not yet checked.'
lean=(root/'SecondScalarChecks.lean').read_text(encoding='utf-8')
assert 'sorry' not in lean and 'native_decide' not in lean
checks=json.loads((root/'second_checks.json').read_text(encoding='utf-8'))
assert checks['passed'] and checks['counts']['tuples']==6000
p=root/'CLAIMS.jsonl'
claims=[json.loads(l) for l in p.read_text(encoding='utf-8').splitlines()]
for c in claims:
 if c['proof_location'].startswith('SECOND_ATTEMPT.md, Route 1 result'):
  c['checks']='Complete clipped-excess proof; 6000 exact rational cases; final SecondScalarChecks.lean compiled with exit 0 and no sorryAx.'
 if c['proof_location'].startswith('SECOND_ATTEMPT.md, Route 1 same-sign'):
  c['checks']='Universal same-sign squared-denominator inequality kernel-checked; clipped-excess certificate kernel-checked; 3022 exact same-sign tuples.'
 if c['proof_location'].startswith('SECOND_ATTEMPT.md, Route 2 proof'):
  c['checks']='Explicit Hellinger split, Cauchy-Schwarz; 3000 exact rational cases and universal small-Hellinger scalar inequality kernel-checked.'
p.write_text(''.join(json.dumps(c)+'\\n' for c in claims),encoding='utf-8')
with (root/'SECOND_ATTEMPT.md').open('a',encoding='utf-8') as f:
 f.write('\\n\\nFinal formal check: the corrected SecondScalarChecks.lean compiled successfully. All three printed axiom lists contain only propext, Classical.choice, and Quot.sound; none contains sorryAx. See second_lean_check.log. The failed run is retained separately and is not counted as verification. The only formal correction was a theorem-name reference; the mathematical inequalities did not change.\\n\\nFinal verdict for the user-requested second attempt: PARTIAL. The cancellation-split special case and density-free Hellinger special case are proved as deductions from explicitly verified published inputs. The unrestricted independent-sum problem has neither a proof nor a counterexample here. STATE is DONE for this attempt, with the gap stated above.\\n')
with (root/'ATTEMPT.md').open('a',encoding='utf-8') as f:
 f.write('\\n## 13. Renewed attempt completed\\n\\n2026-10-12: See SECOND_ATTEMPT.md for the two new approaches, full cancellation-split EKFR theorem, same-sign corollary, free scalar obstruction (not Levy exponents), and density-free local-absolute-continuity comparison. The first route avoids energy inclusion but still needs a common decomposition and control of exceptional cancellation frequencies. The second forces finite variation in the added jump component. All new exact checks passed; the corrected three-lemma Lean file has exit 0 and no sorryAx. The original unrestricted question remains unresolved. Final STATE: DONE; VERDICT: PARTIAL.\\n')
(root/'STATUS.md').write_text('''STATE: DONE
NEXT: Determine whether negative definiteness of genuine Levy exponents controls the exceptional cancellation-set integral, or find a transfer argument for general (H) without global EKFR decompositions.
VERDICT: PARTIAL

2026-10-12: First attempt established common-Rao, dominated-perturbation, proportional-exponent and Gaussian special cases; a genuine stable example refutes automatic energy inclusion into either summand. No unrestricted solution or exact literature solution found.
2026-10-12: Reopened at user request, read ATTEMPT.md and its gap, and asked the read-only math store two gap-specific questions. Wrote two untried approaches in SECOND_ATTEMPT.md before pursuing them.
2026-10-12: Selected transfer of integrable EKFR remainders through a frequency split. Proved (H) for the sum under a reciprocal-integrable exceptional cancellation set; same-sign imaginary exponents suffice. Only the sum needs resolvent densities if individual (H) is given.
2026-10-12: Proved that free scalar EKFR data need not be closed under addition. The example violates Levy negative definiteness and is explicitly not a counterexample to E0027.
2026-10-12: Checked the neighbouring local-absolute-continuity theorem, derived a density-free Hellinger perturbation case, and proved it forces finite variation of the added jumps and complete exponent domination. Checked an infinite-activity example on a lower-dimensional invariant subspace.
2026-10-12: Newly retrieved the original EKFR paper arXiv:1210.2016v3 and verified its theorem and density hypothesis. Follow-up sources and brain queries are appended to LITERATURE.md.
2026-10-12: 6000 exact rational remainder/cancellation checks and 3000 Hellinger checks passed. The corrected SecondScalarChecks.lean compiled with exit 0; all three printed axiom lists have no sorryAx. First failed compile is preserved separately.
2026-10-12: Closed the renewed attempt as DONE/PARTIAL. The original (H)+(H) implication remains unresolved; SECOND_ATTEMPT.md states exactly what the two routes still require. No SOLVED verdict is claimed.
''',encoding='utf-8')
assert len(claims)==14
assert (root/'STATUS.md').read_text().splitlines()[0]=='STATE: DONE'
print('Renewed attempt finalized: DONE/PARTIAL, 14 claims, all three Lean scalar statements checked.')
"""
Path('finalize_second.py').write_text(script,encoding='utf-8')
print('Prepared finalization script; formal success is required before it can close STATUS.')
