from pathlib import Path
import json,urllib.request,urllib.parse
p=Path('LITERATURE.md')
with p.open('a',encoding='utf8') as f:
 f.write('''
## Verified source and papers

- Gil Kalai, *Three puzzles on mathematics, computation, and games*, ICM 2018, arXiv:1801.02602. Source statement verified in Section 3.3.4, PDF p.22; local `kalai_pdf.pdf` and `kalai.txt` preserve it. Fixed epsilon in (0,1), infinite finitely generated group, Cayley SRW, l1 independence. The absence of virtual real homomorphisms is a sufficient-condition conjecture, not a theorem.
- Itai Benjamini and Jeremie Brieussel, *Noise sensitivity of random walks on groups*, ALEA 20 (2023), 1201–1223, DOI 10.30757/alea.v20-42, arXiv:1901.03617v2 (17 June 2021). Theorem 1.4, arXiv PDF p.3: nonlazy dihedral SRW is not sensitive; lazy dihedral SRW is sensitive. Question 1.5 and Conjecture 1.6 on p.3 explicitly leave the general sufficient condition and Grigorchuk case open. Theorem 1.3 on p.2 concerns entropy sensitivity and partial entropy sensitivity of a permutational extension, and does not establish endpoint TV sensitivity on Grigorchuk.
- Ryokichi Tanaka, *Noise sensitivity on affine Weyl groups*, arXiv:2403.01658v5 (3 July 2025); Combinatorics, Probability and Computing, DOI 10.1017/S0963548325100126 (publication metadata from Semantic Scholar). Theorem 1.1, PDF p.2 requires support S union {id}. It is a special case with laziness and virtually abelian groups, not a resolution of the hypothesis in F0093.
- Jeremie Brieussel and Ryokichi Tanaka, *Noise sensitivity on virtually abelian groups*, arXiv:2512.08151v1 (9 December 2025). Theorem 1.1, PDF p.2 proves noise sensitivity iff no nonzero map onto Z for aperiodic, finite-second-moment, semigroup-generating walks on virtually abelian groups. This is not the general Liouville theorem and the infinite virtually abelian examples have virtual maps to R, outside the conjecture's sufficient-condition hypotheses. Example 1.4, PDF p.3 does supply a nonlazy aperiodic SRW example on D_infinity with four distinct symmetric generators {s1,s2,s1s2,s2s1}. Thus the existential SRW question has a positive special-case answer, but this does not meet the user's exact-case SOLVED_IN_LITERATURE requirement for the full problem.
- Ryokichi Tanaka, *Non-noise sensitivity for word hyperbolic groups*, arXiv:2211.03951v2, DOI 10.5802/afst.1803. Related obstruction on non-elementary hyperbolic walks, not Liouville cases (abstract returned by arXiv search).
- *Noise stability on hyperbolic groups*, arXiv:2501.08487, DOI 10.5802/ahl.273. Found in Semantic Scholar citations of Kalai; related non-Liouville direction, full text not inspected, no resolution claimed.

## Exact extracted statements (not full-problem solutions)

The following are word-for-word PDF text extractions; mathematical symbols and line breaks reflect PDF extraction. None is designated SOLVED_IN_LITERATURE.
''')
 for name,start,end in [('1901.03617','Question 1.5.','Another (unexpected)'),('1901.03617','Conjecture 1.6.','As for entropy'),('2512.08151','Theorem 1.1.','This Theorem 1.1')]:
  text=Path(name+'.txt').read_text(encoding='utf8');i=text.index(start);j=text.index(end,i);f.write('\n### '+name+'\n\n```text\n'+text[i:j].strip()+'\n```\n')
 if Path('semantic_retry.response').exists():
  js=json.loads(Path('semantic_retry.response').read_text());f.write('\nSemantic Scholar returned '+str(len(js.get('data',[])))+' citation entries, next cursor '+str(js.get('next'))+'. Relevant titles are reported above.\n')
 f.write('\nGitHub repository search returned zero repositories. This is not evidence that no paper exists. OpenAlex was repeatedly rate-limited, so its citing-source search could not be completed. Semantic Scholar supplied source citations instead. Prior ledger F0093-A001 read from the September intake: two invalid information-theoretic inferences are corrected in ATTEMPT.md. Repository path inventory was filtered for F0093/noise sensitivity/Brieussel and returned no matching path; this is not an exhaustive full-text repository search.\n')
queries={'arxiv_grigorchuk':'https://export.arxiv.org/api/query?search_query='+urllib.parse.quote('all:Grigorchuk AND all:noise')+'&max_results=30', 'openalex_cites_attempt':'https://api.openalex.org/works?filter=cites:doi:10.1142/9789813272880_0017&per-page=100'}
for name,url in queries.items():
 try:
  data=urllib.request.urlopen(url,timeout=25).read();Path(name+'.response').write_bytes(data);status='OK '+str(len(data))+' bytes'
 except Exception as e:status=str(e)
 with p.open('a',encoding='utf8') as f:f.write('\n- Search 2026-10-12 '+name+': '+url+'; '+status+'\n')
 print(name,status)
