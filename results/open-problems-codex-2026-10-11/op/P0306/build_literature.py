import pathlib,json,xml.etree.ElementTree as E
ROOT=pathlib.Path(__file__).resolve().parent
ns={'a':'http://www.w3.org/2005/Atom'}
text='''# P0306 literature audit — 2026-10-11

## Verified source and exact question

Manan Bhatia, Ewain Gwynne, Brin Harper, *Dimension lower bounds in random geometry via Lipschitz functions*, arXiv:2606.10496v1, submitted 9 June 2026. Source PDF saved as source_pdf.pdf; page-delimited text is source_extracted.txt. The online PDF identifies v1. URL: https://arxiv.org/pdf/2606.10496.

Conjecture 1.4, PDF/printed page 7, verbatim mathematical transcription (overline restored from PDF typography):

> Conjecture 1.4. Let h be a Neumann GFF and consider the LQG surface (H̄, D_h). Then we have
> dim_{D_h}(T_{2-star} ∩ R) = 1.

The preceding sentence reads:

> In this paper, we additionally conjecture that for all values of γ and LQG surfaces with boundary, the set of 2-stars on the boundary is always one dimensional.

Theorem 1.3, PDF/printed page 6, opening and part (1), verbatim mathematical transcription:

> Theorem 1.3. Fix γ ∈ (0, 2). Let h be a Neumann (free-boundary) GFF on the upper half plane H, and let D_h be the associated γ-LQG metric on H̄. Then the following hold almost surely.
> (1) dim_{D_h}(T_{2-star} ∩ R) ≥ 1, dim_{Euc}(T_{2-star} ∩ R) ≥ Δ^{∂}_{KPZ}(γ, 1).

Source p.4 defines a k-star by k almost-disjoint geodesics emanating from it, where the interiors of those geodesics are mutually disjoint. Section 2.4, p.13, normalizes h by zero average on the unit semicircle and states that the ambient metric extends continuously to the boundary. Thus the boundary Hausdorff dimension uses the ambient distance, not a new intrinsic length metric on R. Fixing gamma precedes the almost-sure statement; no simultaneous assertion for all gamma is inferred.

The source p.6 says the bulk star dimensions are computed in the Brownian-map case, with metric dimension 5-k for k<=5, and says the general-gamma equality for bulk three-stars is still conjectural. The intake phrase “bulk analogues are computed” cannot be used for every gamma.

## Search provenance and limits

Every HTTP query below was made with Python urllib from the shell, with the raw successful response saved locally. search_log.jsonl records response codes and failures. No built-in web search was used. Searches do not certify absence of a solution. OpenAlex failed repeatedly with HTTP 429, so its citing-works search could not be completed: the source work ID could not be resolved. Semantic Scholar's citations endpoint succeeded and returned an empty indexed list, which does not certify that no citations exist.

'''
for line in (ROOT/'search_log.jsonl').read_text().splitlines():
    r=json.loads(line)
    text+=f"* {r['date']} — `{r['service_query']}`: {r['url']}\n  Result: {r.get('error',str(r.get('status'))+'; saved '+r.get('saved',''))}.\n"
text+='\n## Relevant retrieved records and leads\n\n'
seen=set()
for name in ['arxiv_title.txt','arxiv_boundary.txt','arxiv_recent.txt','arxiv_stars.txt']:
    if not (ROOT/name).exists():continue
    for e in E.parse(ROOT/name).findall('a:entry',ns):
        title=' '.join(e.find('a:title',ns).text.split())
        if not any(w in title.lower() for w in ['liouville quantum','lqg','random geometry','directed landscape']):continue
        url=e.find('a:id',ns).text
        if url in seen:continue
        seen.add(url)
        authors=', '.join(a.find('a:name',ns).text for a in e.findall('a:author',ns))
        date=e.find('a:published',ns).text
        abstract=' '.join(e.find('a:summary',ns).text.split())
        text+=f'* {authors}. *{title}*. {url}, submitted {date}.\n  Abstract: {abstract}\n'
text+='''
## Additional exact references verified in the source bibliography

* Manan Bhatia. *The d_gamma/2-variation of distance profiles in gamma-Liouville quantum gravity*. Communications in Mathematical Physics 406(3):58 (2025); source [Bha25], p.51. Used by the source for boundary confluence, not a boundary star dimension equality.
* Liam Hughes and Jason Miller. *Equivalence of metric gluing and conformal welding in gamma-Liouville quantum gravity for gamma in (0,2)*. Annales de l'Institut Henri Poincare (B) Probabilites et Statistiques 61(3):1961–2003 (2025); source [HM25], p.52. Boundary metric extension is cited as Proposition 1.7; not a solution of P0306.
* Ewain Gwynne. *Geodesic networks in Liouville quantum gravity surfaces*. Probability and Mathematical Physics 2(3):643–684 (2021), arXiv:2010.11260; source [Gwy21], p.52; DOI 10.2140/pmp.2021.2.643 independently returned by Crossref. Bulk network results do not establish this boundary dimension.
* Jean-Francois Le Gall. *Geodesic stars in random geometry*. Annals of Probability 50(3):1013–1058 (2022), arXiv:2102.00489; source [Le 22], p.53. Brownian-map bulk star result; different set.
* Jason Miller and Wei Qian. *Geodesics in the Brownian map: Strong confluence and geometric structure*. Memoirs of the American Mathematical Society, no.1602 (2025); source [MQ25], p.53. Brownian-map bulk geometry; no boundary theorem extracted here.
* Ewain Gwynne and Joshua Pfeffer. *KPZ formulas for the Liouville quantum gravity metric*. Transactions of the American Mathematical Society 375(12):8297–8324 (2022), arXiv:1905.11790; source [GP22], p.52. Independence-based KPZ identities cannot be applied to the field-dependent star set without their hypotheses.

## Brain and prior-work audit

Read-only math recall: query “boundary geodesic two star Bhatia Gwynne Harper”, then card claim_0ee88dfa0805e2a0eecd49dd9ac201fba9f64ee855aa3a2979a4eea74d00c154. Read-only memory queries: “LQG boundary star sets mistakes” and “One-dimensional boundary two-star set in LQG”. Memory hits were mostly unrelated and were not used as mathematical evidence. The math-card snowflake warning was checked independently in ATTEMPT.md Section 5.

The named intake ledgers and origin/master tree were searched read-only for P0306. Prior ledger search details and matched rows are saved in prior_ledger_matches.txt when available; no repository or brain records were written. Exact later candidate-PDF assessments are recorded below.

'''
(ROOT/'LITERATURE.md').write_text(text,encoding='utf-8')
print('Wrote literature audit:',len(text),'characters')
