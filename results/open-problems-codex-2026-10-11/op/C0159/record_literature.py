from pathlib import Path
import json,fitz,re
s=Path('source_arxiv_extracted.txt').read_text(encoding='utf-8').splitlines()
for i,l in enumerate(s):
 if '[57]' in l or '[101]' in l: print('\n'.join(s[i:i+9]))
for name in ['bell_abs','light_rays_abs']:
 s=Path(name+'.txt').read_text(encoding='utf-8')
 print(name,re.findall(r'\[Submitted[^<]+|\[v\d\][^<]+',s)[:6])
logs=[json.loads(x) for x in Path('search_log.jsonl').read_text(encoding='utf-8').splitlines()]
body='''# Literature audit — C0159, 2026-10-11

## Status and source verification

No paper retrieved states and proves the full question under arbitrary transitivity. This is NOT SOLVED_IN_LITERATURE. Search coverage has explicit limitations: OpenAlex was HTTP 429 throughout; the Semantic Scholar source-citation request succeeded but keyword search and the Bell citation request were rate-limited. Negative search results are not a proof of absence.

Olle Häggström and Johan Jonasson, “Uniqueness and non-uniqueness in percolation theory”, Probability Surveys 3 (2006), 289–344, DOI 10.1214/154957806000000096; arXiv:math/0612812v1, 28 December 2006. The Project Euclid endpoint returned HTTP 200 with an Incapsula HTML block (1165 bytes), not a PDF. The full paper was retrieved instead from https://arxiv.org/pdf/math/0612812 and its title page confirms the journal and DOI. Local copy: source_arxiv.txt (PDF bytes) and source_arxiv_extracted.txt.

The correct locator is the END OF SECTION 5, printed pp.308–309, PDF pp.20–21, immediately before Section 6. The quoted passage is:

> “Suppose for some p in the non-uniqueness regime of a transitive nonamenable graph G that we can find two infinite clusters C1 and C2 that come within distance 1 from each other in infinitely many places. Call two such infinite clusters strongly neighboring.”

> “If this is the case for any p, then G is said to exhibit cluster repulsion. Häggström et al. [57] conjectured that cluster repulsion holds for any transitive graph, and supplemented their conjecture with a non-transitive counterexample. Very recently, Timár [101] proved the conjecture under the additional assumption of unimodularity, by means of an ingenious mass-transport argument. The nonunimodular case remains open.”

These quotations normalize PDF ligatures and diacritics, and concatenate the text split across pp.308–309. The source discussion is iid bond percolation, with transitive, connected finite-degree graphs. It defines contact at distance ONE, not an arbitrary bounded radius. ATTEMPT.md explicitly proves an all-finite-radius continuity reduction, and retains the intake's stronger target without claiming the definitions equivalent. No simultaneous-in-p almost-sure assertion is inferred.

## Relevant exact references and scope

1. Ádám Timár, “Neighboring clusters in Bernoulli percolation”, Annals of Probability 34(6) (2006), 2332–2343, DOI 10.1214/009117906000000485, arXiv:math/0702873v1 (28 February 2007). Full text retrieved. Theorem 1.1, printed p.2332, PDF p.1:

> “Let G be a quasi-transitive unimodular graph and consider Bernoulli(p) edge percolation on it. Then any two infinite clusters touch each other in only finitely many vertices almost surely.”

The introduction specifies local finiteness and touching at distance 1. The theorem requires unimodularity, so it does not solve C0159. The 2006 journal year and 2007 arXiv posting are different dates, not a bibliographic error.

2. Sasha Bell, Tasmin Chu, Owen Rodgers, Grigory Terlov, and Anush Tserunyan, “Heavy repulsion of clusters in Bernoulli percolation”, arXiv:2509.10631v1 (2025). Full text retrieved (19 PDF pages). Theorem 1.2, printed/PDF p.3, verbatim apart from math typography:

> “Suppose G is a connected locally finite quasi-transitive nonunimodular graph. Then any two heavy clusters come within unit distance of each other only in a light set of vertices P_p-almost surely.”

The preceding definitions fix Bernoulli(p) bond percolation and light = finite total Haar-stabilizer weight. Question 1.1 on p.2 asks repulsion at any p; p.3 explicitly says “Question 1.1 still remains open.” Line-by-line scope comparison: transitive graphs are quasi-transitive, but only HEAVY clusters are covered; unit distance is R=1; LIGHT is not FINITE; and no all-finite-radius conclusion is asserted. This is a lead and the input theorem for Section 1 of ATTEMPT.md, not a published solution. Pages 2–3 also recall continuity of two-point connectivity as sufficient, leaving only countably many exceptional p. The final proof in ATTEMPT.md supplies the detailed sprinkling argument for every finite radius.

3. Ádám Timár, “Percolation on nonunimodular transitive graphs”, Annals of Probability 34(6) (2006), 2344–2364, DOI 10.1214/009117906000000494; arXiv:math/0702875v1. Full text retrieved. It treats critical percolation, heavy clusters and nonunimodular examples, not a solution of cluster repulsion. Its grandmother graph is the grandparent graph used in this attempt.

4. Tom Hutchcroft, “Nonuniqueness and mean-field criticality for percolation on nonunimodular transitive graphs”, arXiv:1711.02590; Journal of the American Mathematical Society, DOI 10.1090/jams/953. Abstract retrieved through arXiv search and Semantic Scholar citation metadata. Establishes p_c<p_h<=p_u, not cluster repulsion. Full text not fetched in this attempt.

5. Pengfei Tang, “Heavy Bernoulli-percolation clusters are indistinguishable”, arXiv:1809.01284. Abstract retrieved via arXiv search. Heavy indistinguishability does not give unweighted repulsion.

6. Grigory Terlov and Ádám Timár, “Weighted-amenability and percolation”, arXiv:2502.02560v2 (2025). Abstract retrieved via arXiv search. Weighted amenability and heavy phase thresholds are adjacent topics; no repulsion solution is stated in the retrieved abstract.

7. Shirshendu Chatterjee, Yang Chen, and Grigory Terlov, “β-Skewed Maximal Spanning Forests”, arXiv:2609.11845v1 (2026). Full text retrieved. Its forest equalities and counterexample concern a different question. Example 2.3 confirms the grandparent weight ratios k,k^2,1/k,1/k^2. No cluster-repulsion theorem was found in the retrieved text.

8. Martin P. W. Zerner, “Infinite light rays and infinite clusters with infinitely many pivots”, arXiv:2610.12460, retrieved following the source's Semantic Scholar citation list. Full text retrieved. This is about Lorentz mirror trajectories and bundled random one-ended trees with variable parallel-edge multiplicities, not two distinct Bernoulli clusters on a fixed transitive graph. The title's “light rays” refers to trajectories, not modular-weight light clusters. No inference of a transitive counterexample is justified. The metadata may be newer than the nominal session date; it is recorded as retrieved evidence, not used to certify chronology.

9. Gábor Pete, “A note on percolation on Z^d: isoperimetric profile via exponential cluster repulsion”, Electronic Communications in Probability 13 (2008), DOI 10.1214/ECP.v13-1390; arXiv:math/0702474. Crossref and arXiv abstract retrieved. Finite versus infinite cluster estimates on Z^d do not resolve the question.

## Searches and fetches (all performed 2026-10-11)

Every HTTP request made in this attempt is listed below with the exact encoded query URL and the result. Raw responses are saved beside this file; search_log.jsonl is the machine-readable ledger. An OpenAlex citing-source filter request was attempted but rate-limited before any result could be validated; its DOI filter spelling was not validated as an OpenAlex works-ID lookup.

'''
for row in logs:
 body += '- **'+row['service']+'**: `'+row['url']+'` — '+(row.get('error') or str(row.get('status'))+'; '+str(row.get('bytes'))+' bytes')+'\n'
body+='''
## Read-only research brain and earlier records

Ran math_recall.py with “percolation cluster repulsion Timar heavy clusters” and later “Haggstrom Schonmann connectivity function continuity repulsion”. Ran brain.py recall with “nonunimodular percolation cluster repulsion” and “nonunimodular percolation mistakes”. No relevant checked theorem was identified in the initial results. Read-only rg search for C0159 under 06_math_research located the intake and C0159-A001. That attempt left a tilted-mass-transport gap and suggested upward parallel clusters on the grandparent graph; Propositions 3.1–3.2 and Theorem 6.1 give a checked mathematical response to that lead. The ledger's statement that a counterexample needs contacts in one modular class was not accepted as a theorem. The present superlevel bound shows why summably decreasing weights are instead an unresolved possibility in general.

Ran git ls-tree -r --name-only origin/master with C0159/cluster-repulsion path patterns in ~/math-open-problems; no matching path was returned. No repository working tree was touched. No brain/store write command was invoked.

## Conclusion

Bounded searches found no full published answer, and the 2025 paper expressly retains the open question. The correct research verdict is PARTIAL: the written attempt proves the grandparent-graph special case and a general continuity reduction, while the arbitrary nonunimodular case remains unproved. No novelty claim is made for these special-case arguments.
'''
Path('LITERATURE.md').write_text(body,encoding='utf-8')
