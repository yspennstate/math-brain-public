"""Append the 2026-09-09 E0024 partial row from the ultracode workflow (integrator; run once under the mesh claim)."""
import json, datetime
now = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
row = {"attempt_id":"E0024-A002","author":"ultracode workflow wf_f1c21e21-f2d attack:E0024, verified by three refuters (math / fidelity / prior art), integrated by claude-prob1000-e0077-0908","problem_id":"E0024","schema":"probability-attempt.v1","recorded_at":now,"substantive":True,
 "method":"Energy comparison. With psi = Phi(x) + Psi(y) and psi' = Phi(x) + Re Psi(y), the Kanda-Forst condition |Im Psi| <= c(1 + Re Psi) gives the pointwise two-sided bound (1/K) Re(1/(lambda+psi')) <= Re(1/(lambda+psi)) <= K Re(1/(lambda+psi')) with K = 2(1+c^2) for lambda >= 1 (algebraic identity certified in Lean U_E0024.lean); multiply by |nu-hat|^2 and integrate to compare lambda-energies; conclude by the survey's Theorem 4.2 (resolvent-density criterion for (H)).",
 "result":"PARTIAL (Question 4' stays open). Theorem A: if Y is Kanda-Forst and Z = (X,Y), Z^s = (X,Y^s) have resolvent densities, then Z satisfies (H) iff Z^s does - so for Kanda-Forst partners the product question reduces to the symmetric-partner question; with X also Kanda-Forst (Rao's class, product-stable by A001) the answer is yes. Lemma B: two Levy processes with resolvent densities, equal Re psi and |Im psi - Im psi'| <= c(1+Re psi) satisfy (H) together and have the same finite-1-energy measures. VERIFIER CORRECTION (accepted): the comparison inequality is the survey's own (4.10)-(4.11) in the proof of Proposition 4.8 (from Hu-Sun 2018, Lemma 4.6), so Theorem A is a corollary of the survey's displayed inequalities plus Theorem 4.2, not a new mechanism. The case that matters for Getoor's conjecture (X outside Rao's class) is untouched.",
 "key_identity":"2(1+c^2)(a^2+(b+d)^2) - (a^2+b^2) = (b+2d)^2 + 2(c^2 a^2 - d^2) + a^2 + 2c^2(b+d)^2.",
 "independent_check":"Math verifier re-derived every step and recompiled the Lean file (axioms propext/Classical.choice/Quot.sound); fidelity verifier matched Questions 4 and 4' against the PDF text lines 705-708 and 902-905; prior-art verifier found no resolution after the 2021 survey (arXiv API, OpenAlex, Semantic Scholar citations, zbMATH). Memo: prob1000_lean_20260908/ultracode_20260909/E0024/memo.md.",
 "obstruction":"X outside Rao's class; nothing here bears on it."}
with open('attempts.jsonl','a',encoding='utf-8') as f: f.write(json.dumps(row, ensure_ascii=False)+'\n')
P=[json.loads(l) for l in open('problems.jsonl',encoding='utf-8') if l.strip()]
for r in P:
    if r['problem_id']=='E0024':
        r['result_status']='partial_result'; r['status_note']='2026-09-09: Kanda-Forst partner reduces to a symmetric partner (corollary of the survey\'s (4.10)-(4.11) + Thm 4.2); open. Attempt E0024-A002.'
with open('problems.jsonl','w',encoding='utf-8',newline='\n') as f:
    for r in P: f.write(json.dumps(r, ensure_ascii=False)+'\n')
print("E0024 row appended")
