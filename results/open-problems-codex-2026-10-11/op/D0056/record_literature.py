from pathlib import Path
import xml.etree.ElementTree as E,json
ns={'a':'http://www.w3.org/2005/Atom'}
r=E.parse('arxiv_http.json')
with open('LITERATURE.md','a',encoding='utf8') as f:
 f.write('''

## Search limitations and corrections

All URLs above are queries run from Python urllib on 2026-10-11. Raw successful responses are retained in this folder. OpenAlex consistently returned HTTP 429; its source and source-citing queries could not be inspected. The early OpenAlex `cites:W2609440919` call used an unverified candidate identifier and provides no source-citation evidence; discard that query for inference. After Crossref identified the exact source DOI, direct source lookup and citing-work queries with that DOI were attempted and also rate-limited. Semantic Scholar text and arXiv-paper queries returned 429, but its DOI-based citation endpoint succeeded. GitHub returned zero repositories for the stated query. No built-in web search was used.

## Verified source

Xinxing Chen, Bernard Derrida, Yueyun Hu, Mikhail Lifshits, Zhan Shi, *A max-type recursive model: some properties and open questions*, arXiv:1705.04787v2 (26 June 2019); in *Sojourns in Probability Theory and Statistical Physics III* (2019), pp. 166–186. DOI: 10.1007/978-981-15-0302-3_6.

PDF p. 1: “To avoid trivial discussions, we assume that X₀ is not almost surely a constant.” This standing hypothesis matters and is absent from the supplied transcription.

PDF p. 3, Conjecture 1 (text and formula transcribed, with mathematical superscripts restored):

> Conjecture 1. Assume (4). Then we have
> P(Xₙ ≠ 0) ∼ [4/(m − 1)²] [1/n²], n → ∞.

Condition (4) on that page is (m−1)E(X₀ m^{X₀}) = E(m^{X₀}) < ∞. The recursion is equation (1), PDF p. 1, with deterministic m≥2 independent copies and decrement 1.

PDF p. 4: “Possibly some additional integrability conditions, such as E(X₀³ m^{X₀}) < ∞ in Theorem 3 below, are necessary for our conjectures to hold.”

## Decisive external input; not a printed solution to D0056

Xinxing Chen and Zhan Shi, *The stable Derrida–Retaux system at criticality*, arXiv:2006.06140v1 (11 June 2020); *In and Out of Equilibrium 3: Celebrating Vladas Sidoravicius*, Progress in Probability (2020), pp. 239–264. DOI: 10.1007/978-3-030-60754-8_12.

PDF p. 3, Theorem 1.1, verbatim prose with mathematical formula layout restored:

> Theorem 1.1. Let (Yₙ, n ≥ 0) be such that (m − 1)E(Y₀ m^{Y₀}) = E(m^{Y₀}) < ∞. Under assumption (1.4), there exist constants c₂ ≥ c₁ > 0 such that for all n ≥ 1,
> c₁ n^{α−2} ≤ ∏_{i=0}^{n−1} [E(m^{Yᵢ})]^{m−1} ≤ c₂ n^{α−2}.

Assumption (1.4) is P(Y₀=k) ∼ c₀ m^{−k}k^{−α}, k→∞, for 2<α<4 and c₀>0. Page 1 additionally assumes P(Y₀≥2)>0 throughout. PDF p. 4 explicitly includes the case α=3. The upper-bound proof was checked on PDF pp. 20–21; its truncated third weighted moment is c(3n−1) for the explicit law here.

Application, line by line: ATTEMPT.md section 3 constructs a probability law with m=2, α=3, c₀=c>0, finite critical weighted first moment, and P(X₀≥2)>0. The theorem therefore gives Qₙ≤Cn. Sections 4–5 prove that qₙ∼4/n² would imply eₙ>3/(2n) eventually. Section 6 then gives Qₙ≥Kn^{3/2}, contradicting the published upper bound. The implication from survival to the incompatible product is proved in our note, not stated as this theorem in print; therefore the verdict is SOLVED, not SOLVED_IN_LITERATURE.

## Strongest directly relevant survival theorem inspected

Xinxing Chen, Yueyun Hu, Zhan Shi, *The sustainability probability for the critical Derrida–Retaux model*, arXiv:2108.05610v1 (12 August 2021); *Probability Theory and Related Fields* 182 (2022), 641–684. DOI: 10.1007/s00440-021-01091-z (online publication 19 October 2021).

PDF p. 3, Theorem 1.2 assumes E(t^{Y₀})<∞ for some t>m and gives P(Yₙ≥1)=n^{−2+o(1)} and E(Yₙ)=n^{−2+o(1)}. This has stronger hypotheses and no sharp multiplicative constant. It does not solve the exact question.

PDF p. 4 states that the universal coefficient should require E(Y₀³m^{Y₀})<∞; for m=2 and tails c₀ 2^{−k}k^{−α}, its equation (1.5) predicts coefficient α(α−2)/2. At α=3 this is 3/2. This prediction is not used as a theorem.

## All arXiv topic matches and their search summaries

The following exact bibliographic entries and abstracts came from the logged broad arXiv query; their presence does not certify a theorem. The unrelated exclusion-process match is omitted from the relevant-paper list.

''')
 for e in r.findall('a:entry',ns):
  title=' '.join(e.find('a:title',ns).text.split())
  if 'exclusion process' in title: continue
  authors=', '.join(a.find('a:name',ns).text for a in e.findall('a:author',ns))
  aid=e.find('a:id',ns).text;date=e.find('a:published',ns).text[:10]
  summ=' '.join(e.find('a:summary',ns).text.split())
  f.write(f'- {authors}. *{title}*. {aid}, first submitted {date}. Search abstract: {summ}\n\n')
 f.write('## Semantic Scholar source-citing works\n\n')
 d=json.loads(Path('semantic_citing.json').read_text(encoding='utf8'))
 for x in d.get('data',[]):
  p=x.get('citingPaper',{});f.write(json.dumps(p,ensure_ascii=False)+'\n\n')
 f.write('''## Read-only earlier work and its audit

The intake directories were searched with rg for D0056; the prior attempt D0056-A001 was read. Its claim that eₙ∼2/((m−1)n) automatically yields the survival constant by taking differences is unsupported without additional regularity. The present persistent-gap proof avoids that issue.

Read-only git tree search and `git show origin/master:research7_2026-09-17/R7-02/paper_d0059_stable_tail_refutation/main.tex` retrieved the earlier D0059 stable-tail argument; a read-only copy is in prior_D0059_readonly.txt. Its explicit normalization and product-exponent argument were checked independently. That result concerns endpoint generating functions, not survival, so it is a lead rather than a previously proved D0056 answer.

Brain topic and mistakes recall and math-store recall were run as requested. They found no directly relevant theorem card. No brain/store/ledger/repository writes were intentionally made.

## Status conclusion

No fetched paper was found to state and prove the exact survival assertion under exactly the original hypotheses. Current evidence instead supports the counterexample proved in ATTEMPT.md. The stronger finite-third-weighted-moment question is outside the solved claim; the bounded and partially rate-limited search does not establish its current global status.
''')
print('Literature references, source quotations, theorem scope, searches and limitations saved.')
print(json.dumps(d,ensure_ascii=False,indent=2))
