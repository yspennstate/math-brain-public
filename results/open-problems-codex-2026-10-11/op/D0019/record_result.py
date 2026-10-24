import pathlib,json,xml.etree.ElementTree as ET
# Add exact references of related broad-search hits, explicitly as leads only.
raw=json.loads(pathlib.Path('crossref.response').read_text(encoding='utf8'))['message']['items']
keys=['The Zero Set of Fractional Brownian Motion Is a Salem Set','On the Fourier structure of the zero set of fractional Brownian motion','A Marstrand projection theorem for lines','Stochastic integration with respect to local time of the Brownian sheet and regularising properties of Brownian sheet paths']
with pathlib.Path('LITERATURE.md').open('a',encoding='utf8') as f:
 f.write('\n## Related search hits (not used as solutions)\n\n')
 for x in raw:
  title=x.get('title',[''])[0]
  if title in keys:
   auth='; '.join(' '.join([a.get('given',''),a.get('family','')]).strip() for a in x.get('author',[]));venue='; '.join(x.get('container-title',[]));date=x.get('published',{}).get('date-parts',[])
   f.write(f'- {auth}, **{title}**, {venue}; publication date {date}; volume {x.get("volume","")}, pages/article {x.get("page",x.get("article-number",""))}, DOI https://doi.org/{x.get("DOI","")}. Related model or general projection theorem; not a source-matching resolution.\n')
 f.write('\n- arXiv also returned Enkelejd Hashorva and Yuliya Mishura, **Boundary Non-Crossings of Additive Wiener Fields**, arXiv:1402.2620v2; *Lithuanian Mathematical Journal* 54(3), 277–289 (2014). The projection in its abstract is an RKHS projection, not a zero-set projection; discarded.\n')
 f.write('- Semantic Scholar source citations additionally listed **Packing dimension of images of additive Lévy processes** (2013), DOI 10.1090/S0002-9947-2013-05970-3, and **Hausdorff dimension of limsup random fractals** (2013), DOI 10.1214/EJP.V18-2273. These metadata-only leads were not used.\n')
claims=[
 {'problem_id':'D0019','claim':'For the positive-parameter two-parameter Brownian sheet in d=2 or d=3, almost surely every orthogonal line projection of its zero set has Hausdorff dimension 2-d/2; hence no sheet-dependent random exceptional projection exists.','status':'proved','proof_location':'LITERATURE.md: exact Theorem 1.2 quotation and line-by-line application; ATTEMPT.md: Complete application proof','remaining_gap':'None for the intended source hypotheses. Invokes Chen-Woessner Theorem 1.2 and Proposition 1.1 rather than claiming an independent proof of them.','checks':['Fetched full arXiv:2405.20019v2','Theorem 1.2 page 2 explicitly quantifies all nonzero linear maps on a common almost-sure event','Proof Section 2 pages 4-7 includes Uniformity in p','Source page 3 verifies d=2,3 and page 34 gives Open Problem 4','Scalar linear image is isometric to orthogonal line projection','Crossref confirms J. Theor. Probab. 38 (2025), article 33, DOI 10.1007/s10959-024-01399-1']},
 {'problem_id':'D0019','claim':'Every possibly sheet-dependent random line is covered by the same probability-one event of the literature theorem; independence of its direction is unnecessary.','status':'proved','proof_location':'ATTEMPT.md: Complete application proof','remaining_gap':'None, conditional on the cited all-maps theorem.','checks':['Universal quantifier inside almost-sure statement, explicitly emphasized by authors','Pointwise specialization to L(omega), no uncountable intersection of fixed-direction events']}
]
pathlib.Path('CLAIMS.jsonl').write_text(''.join(json.dumps(c,ensure_ascii=False)+'\n' for c in claims),encoding='utf8')
pathlib.Path('STATUS.md').write_text('STATE: DONE\nNEXT: None; the source-matching literature resolution and its complete application are recorded.\nVERDICT: SOLVED_IN_LITERATURE\n\n2026-10-12: Fetched Khoshnevisan arXiv:math/0510518v1; verified Open Problem 4 on page 34, the d=2,3 range on page 3, and the positive-parameter convention.\n2026-10-12: Queried arXiv, OpenAlex (including a citing-source query), Crossref, Semantic Scholar and GitHub. OpenAlex requests were rate-limited; Semantic Scholar source citations and arXiv independently identified the resolver. All requests and outcomes saved in LITERATURE.md.\n2026-10-12: Read-only checkout supplied a lead to Chen-Woessner; independently fetched full arXiv:2405.20019v2 and checked Theorem 1.2 page 2 and its Section 2 proof. Crossref verifies publication in Journal of Theoretical Probability 38 (2025), article 33.\n2026-10-12: Exact theorem quotation, hypothesis match and complete deduction for arbitrary random orthogonal line projections saved. Answer: no, almost surely, for d=2,3. No unresolved mathematical gap in the intended question; no new proof or formalization claimed.\n',encoding='utf8')
# Artifact checks.
for file in ['STATUS.md','LITERATURE.md','ATTEMPT.md','CLAIMS.jsonl']:
 p=pathlib.Path(file);print(file,p.stat().st_size)
assert pathlib.Path('STATUS.md').read_text(encoding='utf8').splitlines()[0]=='STATE: DONE'
for line in pathlib.Path('CLAIMS.jsonl').read_text(encoding='utf8').splitlines():json.loads(line)
print('Status format and JSONL checked.')
