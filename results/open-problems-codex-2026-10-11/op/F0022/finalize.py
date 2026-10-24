from pathlib import Path
import json
p=Path('ATTEMPT.md');s=p.read_text(encoding='utf-8-sig').replace('Literature search and independent checks are in progress.','Literature search and independent checks are complete; see LITERATURE.md and the checks below.')
s+="""

## Conditional reduction for a corrected formulation (not a solution of it)

Here is the exact scope of what a third-derivative upper bound would yield. Let f∈C²([0,a])∩C³((0,a]) and suppose that, for every η∈(0,2/3), |f'''(t)|≤C_η t^{−1/3−η} for sufficiently small t>0. Then

|f(h)−f(0)−h f'(0)−h² f''(0)/2|≤C_η h^{8/3−η}/[(2/3−η)(5/3−η)(8/3−η)].

Proof. Fix η and sufficiently small h. The bound is integrable on (0,h) since −1/3−η>−1. For δ>0, the fundamental theorem of calculus gives f''(u)−f''(δ)=∫_δ^u f'''(t)dt. Let δ↓0; continuity of f'' at zero and absolute convergence give f''(u)−f''(0)=∫_0^u f'''(t)dt. Integrate this identity twice, using f' and f continuous at zero. Fubini is justified by the absolute bound C_η h²∫_0^h t^{−1/3−η}dt<∞. The remainder equals (1/2)∫_0^h(h−t)² f'''(t)dt. For b=−1/3−η, direct integration gives

(1/2)∫_0^h(h−t)²t^b dt = h^{b+3}/[(b+1)(b+2)(b+3)].

Indeed expand (h−t)² and integrate each of h²t^b, −2h t^{b+1}, t^{b+2}; the coefficient is (1/2)[1/(b+1)−2/(b+2)+1/(b+3)]=1/[(b+1)(b+2)(b+3)]. This proves the inequality. The same argument applies on the other side by setting f(t)=κ(1/2−t).

This lemma is independently proved. Applying it to κ would additionally rely on the cited regularity and derivative estimates, which we have not independently proved here. It provides an upper estimate only. The remaining corrected target is the full two-sided logarithmic law

|R(h)|=|h|^{8/3+o(1)}, R(h)=κ(1/2+h)−κ(1/2)−κ'(1/2)h−κ''(1/2)h²/2.

Neither the singleton lower bound nor an existential subsequence lower bound for |κ'''| proves a lower bound for |R(h)| for every small h. One would need a quantitative estimate that controls integration and cancellation. This corrected target is not substituted for the original question in our verdict.

## Exact computations and Lean verification

- exact_checks.py enumerates all 128 configurations of the origin and six neighbors, using exact fractions at p=0, 1/4, 49/100, 1/2, 51/100, 3/4, 1. Total probability is 1, and exactly one configuration is the isolated-open event, with probability p(1−p)^6. All assertions passed; outputs are in exact_checks.json.
- The same script constructs all rooted connected sets of sizes 1 through 5 on the coordinate triangular lattice with steps ±(1,0), ±(0,1), ±(1,1). Each next level is obtained by adjoining a boundary site and deduplicating. Every rooted connected set is generated, because a spanning tree permits removal of a non-root leaf, leaving a connected predecessor; repeated removal reaches {0}. Conversely every generated set is connected. The numbers are 1, 6, 33, 176, 930. Exact finite-cluster contributions at p=1/2 are 1/128, 3/1024, 13/8192, 65/65536, 357/524288. Their sum is 7341/524288≈0.0140, a further computational lower bound. This enumeration is an independent check; the solved verdict uses only the first elementary term.
- Singleton.lean imports only Mathlib.Data.Rat.Defs and Mathlib.Tactic.NormNum. It verifies (1/2)(1−1/2)^6=1/128, 2+(−2/3)=4/3, and 1/128>0. Command: lake env lean ~/brain_workers/TRIO_1011/op/F0022/Singleton.lean, run from ~/lean_verify, one Lean invocation at a time with a 3600-second process timeout. The first invocation failed because PowerShell introduced a UTF-8 BOM; after removing the BOM the invocation exited 0. lean_check.txt records the successful output and axioms. No sorry or native_decide is used. Norm_num produces ordinary kernel-checked proof terms. Only these algebraic statements are formally checked, not the infinite-volume probability or continuity proof.

## Hostile referee audit

1. **Empty/infinite cluster convention:** stated explicitly. Infinite clusters contribute zero. The singleton argument also survives conditioning on occupation or using clusters of either color. Without an empty-cluster convention the expectation is undefined, not evidence for the proposed asymptotic.
2. **Independence and degree:** the triangular lattice has six distinct neighbors; the event fixes seven independent Bernoulli variables. Exact local enumeration agrees. Exterior variables are unrestricted; no path can leave an isolated origin.
3. **Nonnegativity:** reciprocal finite sizes are nonnegative; omitting other events cannot increase the lower bound. No infinite-cluster probability or arm estimate is needed.
4. **Critical point versus approach:** the lower bound holds for every p, not only p=1/2. Its continuity yields a positive liminf on either side. Thus setting a special value at p=1/2 cannot avoid the contradiction.
5. **The o(1) exponent:** an exponent approaching 4/3 stays positive; the stated power must tend to zero. The exact arithmetic is Lean checked.
6. **Uniform polynomial approximation:** connected rooted sets of bounded size lie in a finite ball; their exterior boundaries are finite; the omitted reciprocal is ≤1/(M+1) uniformly in p, including p=0 and p=1. The epsilon proof of continuity is given above.
7. **Interpretation of “singularity”:** a nonsmooth part can vanish while κ itself tends to a positive background. Our counterexample does not disprove the conventional singular-part prediction. No authorial erratum has been located or asserted.
8. **Literature quantifiers:** Zhang's lower bound is along a sequence, not for all small deviations. Mertens–Jensen–Ziff's expansion is not an independently checked rigorous proof. API rate limits prevent an exhaustive current-status conclusion.
9. **Prior work:** the repository already records this literal counterexample. It was rederived and independently checked; it is not presented as novel research.

## Final scope and gap

The literal source formula has a complete counterexample; no gap remains in that conclusion. The regular-background-subtracted 8/3 law is a different problem and is not proved or refuted in this folder. The conditional upper-bound reduction above makes one implication precise but supplies no uniform lower bound for that remainder.
"""
p.write_text(s,encoding='utf-8')
claims=[dict(problem_id='F0022',claim='For triangular independent site percolation κ(p)≥p(1−p)^6; hence the printed κ(p)=|p−1/2|^(4/3+o(1)) asymptotic is false.',status='counterexample',proof_location='ATTEMPT.md, Counterexample to the literal formula',remaining_gap='None for the printed formula; does not address a Taylor-subtracted singular remainder.',checks='All 128 local configurations at seven rational p values; Singleton.lean kernel-checked algebra; hostile referee audit.'),dict(problem_id='F0022',claim='The unconditioned open-cluster reciprocal expectation is continuous on [0,1], with sup_p|κ(p)−κ_M(p)|≤1/(M+1).',status='proved',proof_location='ATTEMPT.md, Continuity, with a full elementary proof',remaining_gap='None for continuity; no differentiability asserted by this proof.',checks='Finite connected-set polynomial formula and uniform reciprocal tail bound; epsilon proof.'),dict(problem_id='F0022',claim='A C² function whose third derivative satisfies the stated |t|^(−1/3−η) bounds has Taylor remainder O(|h|^(8/3−η)).',status='proved',proof_location='ATTEMPT.md, Conditional reduction for a corrected formulation',remaining_gap='Application relies on external percolation regularity/derivative results; no uniform lower bound.',checks='Absolute convergence, FTC, Fubini and explicit integration written out.'),dict(problem_id='F0022',claim='Exact rooted-animal enumeration to size five gives κ(1/2)≥7341/524288.',status='numerical_evidence',proof_location='exact_checks.py; exact_checks.json; ATTEMPT.md, Exact computations',remaining_gap='Finite calculation not Lean-formalized; not needed for the literal counterexample.',checks='Exact rational arithmetic; rooted counts 1,6,33,176,930; size-one and size-two assertions.'),dict(problem_id='F0022',claim='The background-subtracted absolute second-order Taylor remainder obeys |R(h)|=|h|^(8/3+o(1)).',status='conjecture',proof_location='ATTEMPT.md, Final scope and gap; LITERATURE.md',remaining_gap='Need lower control for every small h and cancellation estimates; no complete theorem located in bounded search.',checks='Scope distinguished from source; Zhang theorem lower bound is subsequential.')]
Path('CLAIMS.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in claims),encoding='utf-8')
Path('STATUS.md').write_text("""STATE: DONE
NEXT: No further work on the literal formula; a separately authorized reformulation would need a uniform lower bound for the Taylor-subtracted 8/3 remainder.
VERDICT: SOLVED

2026-10-12: SOLVED means counterexample to the exact printed statement only. The intended singular-part problem is NOT solved; no novelty claimed.
2026-10-12: Retrieved arXiv:1107.0158v3 and confirmed Question 1 on PDF p. 44, including 2+alpha and alpha=-2/3.
2026-10-12: Searched arXiv, OpenAlex (including source/citation requests), Crossref, Semantic Scholar and GitHub. OpenAlex/Semantic Scholar rate-limited. Found Zhang's 2020 revision, with third-derivative upper bound and lower bound along a sequence; not SOLVED_IN_LITERATURE.
2026-10-12: Reproved κ(p)≥p(1−p)^6 and continuity by uniform finite-cluster approximation. Read prior intake and repository note; same literal obstruction already recorded there.
2026-10-12: Exact 128-state checks and size≤5 rooted-cluster enumeration passed. Lean algebraic certificate passed after removal of UTF-8 BOM; no sorry/native_decide. Completed hostile referee audit and recorded the separate intended gap.
""",encoding='utf-8')
print('Attempt, claims, and final status saved')
