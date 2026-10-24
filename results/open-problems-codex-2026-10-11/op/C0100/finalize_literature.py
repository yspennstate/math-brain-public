from pathlib import Path
import json,xml.etree.ElementTree as E
p=Path('LITERATURE.md');s=p.read_text(encoding='utf8');s+='\n## Subsequent searches (same date)\n'
for e in json.loads(Path('search_log.json').read_text()):
 if e['url'] not in s:s+=f"- {e['date']}: {e['service']}; {e['url']}; HTTP {e.get('status','error')}; {e.get('error','raw response saved')} .\n"
s+='''
## Bibliographic clarification and exact theorem comparison

The source DOI verified from Crossref is **10.1090/bull/1573**, not the exploratory 1563. A source-resolution request to OpenAlex using the correct DOI also returned 429. Its response explicitly says the free daily budget shared by the network IP is used up. Thus a reliable OpenAlex citing-work list was not obtained. The guessed OpenAlex ID above must not be used as a verified source identifier. Semantic Scholar's direct ARXIV:1611.00411/citations endpoint also returned 429.

- Wesley Pegden and Charles K. Smart, Stability of Patterns in the Abelian Sandpile, Annales Henri Poincare 21(4) (2020), 1383–1399, DOI 10.1007/s00023-020-00898-1; arXiv:1708.09432v2 (26 Jan 2020).
- Lionel Levine, Wesley Pegden and Charles K. Smart, Apollonian structure in the Abelian sandpile, Geometric and Functional Analysis 26(1) (2016), 306–336, DOI 10.1007/s00039-016-0358-7; arXiv:1208.4839v2.
- Andrew Melchionna, The sandpile identity element on an ellipse, Discrete and Continuous Dynamical Systems 42(8) (2022), first page 3709 (Crossref supplies no last page), DOI 10.3934/dcds.2022029; arXiv:2007.05792v2 (1 July 2023).
- Lionel Levine, Wesley Pegden and Charles K. Smart, The Apollonian structure of integer superharmonic matrices, Annals of Mathematics 186(1) (2017), 1–67, DOI 10.4007/annals.2017.186.1.1; arXiv:1309.3267. Used as the structure-theory reference recalled and cited by the pattern-stability paper; not a theorem of all height-fraction limits.

The following sentences in the pattern-stability paper are decisive for avoiding a false literature resolution (PDF/printed p. 6, section 2.5):

> Note that for the standard ≤3 cutoff, our solutions u_n correspond via Δu_n + 1 to the unique recurrent configuration equivalent to the all-ones configuration on Z² ∩ nΩ, whereas the identity element is the unique recurrent configuration equivalent to the all-zeros configuration.

(The equation notation is transcribed into Unicode; the prose is unchanged.) Thus Theorem 1's square model is not the requested square identity, and is not the point-source stabilization. The introduction, p. 2, says Sportiello's ansatz can be adapted to the cutoff-3 square and “yields the continuum limit of the sandpile identity on the square”; this sentence is a lead, not a stated and proved identity theorem here. Section 2.5 expressly distinguishes that ansatz from the rigorously treated model.

Pattern-stability Theorem 10, PDF/printed p. 7, is the precise external estimate used in ATTEMPT.md:

> There is a universal constant C_10 > 0 such that if h ≥ C_10, r ≥ C_10|V|, hr ≥ C_10|V|³, R ≥ C_10hr, and v : Z² → Z is recurrent and satisfies |v − o| ≤ h² in B_R, then, for a (1 − C_10 R⁻¹rh)-fraction of points x in B_{R−r}, there is a translation õ_x of o such that v = õ_x in B_r(x).

Mathematical notation is faithfully transcribed. The local version used in our reductions is an implication argued from its proof and local Lemma 14; hence even if that reduction closed the problem, it would be our argument rather than SOLVED_IN_LITERATURE under the requested standard.

Ellipse Theorem 4.3, PDF/printed p. 13, has r(k)=o(k^(1/4)) and r(k)≥3|V|³ and proves limsup f(k,A) k^(1/4)/r(k)≤C g(A). Its section 4 (p. 12) fixes A in Gamma^+ with positive determinant and in the fundamental domain of the Apollonian packing corresponding to (x,y) in [0,2]², with 0<lambda_1≤1<lambda_2. Thus it is not a result for arbitrary ellipses. ATTEMPT.md section 9 derives the ball-frequency special case explicitly and keeps these assumptions.

The Apollonian paper's Corollary 1.4 (p. 6) assumes three connected open regions on which the limiting odometer is already quadratic with pairwise tangent Hessians; it fills the intervening region by an Apollonian triangulation. The subsequent paragraph says the near-ubiquity of those regions is inferred from numerical evidence and that going beyond dependence on local boundary knowledge requires global geometry, a considerable challenge. Therefore the old intake's unconditional patch-cover statement is not established by that reference.

## Other relevant abstract-screened papers
'''
ns={'a':'http://www.w3.org/2005/Atom'};seen=set();targets=['2308.12183','2603.12006','2607.26169','0809.3416','1711.04285','1502.06284','1806.10823']
for file in ['arxiv.xml','arxiv_target.xml','arxiv_identity_recent.xml']:
 r=E.parse(file).getroot()
 for e in r.findall('a:entry',ns):
  ident=e.findtext('a:id',namespaces=ns)
  if any(t in ident for t in targets) and ident not in seen:
   seen.add(ident);title=e.findtext('a:title',namespaces=ns).replace('\n',' ');authors=', '.join(x.findtext('a:name',namespaces=ns) for x in e.findall('a:author',ns));date=e.findtext('a:published',namespaces=ns)[:10]
   s+=f'- {authors}, {title}, {ident}, first submission {date}. Abstract/title screened; no theorem of the exact C0100 objects identified.\n'
s+='''
## Read-only earlier-work searches

- math_recall.py "sandpile Pegden Smart height frequencies periodic patches" (2026-10-12).
- brain.py recall "sandpile mistakes" and "sandpile height fraction convergence" (2026-10-12); the first mostly returned unrelated records, explicitly not treated as mathematical evidence.
- rg for C0100 in probability_1000_intake_* directories, after resolving the PowerShell directory glob; also in codex_pool_2026_10_10. Relevant files: claude_20260907/problems.jsonl and attempts.jsonl; team_O/w333/proofs/C0100.md and final_results.jsonl. F0132 is the neighboring square-identity conjecture; its literature status was unverified.
- git ls-tree origin/master filtered for C0100, then git show origin/master:probability_campaigns/codex_pool_2026-10-10/team_O/w333/proofs/C0100.md and its evidence/C0100_intake.json. The only recorded answers found were the prior conditional patch theorem and generic weak-* counterexample. No repository working tree was modified.

Conclusion: no paper was found that states and proves the full point-source ball-frequency refinement together with the wired-square identity question. This is a bounded unsuccessful search, with the cited quota limitations, not a claim that the problem must still be open throughout the entire literature. Verdict remains PARTIAL.
'''
p.write_text(s,encoding='utf8')
