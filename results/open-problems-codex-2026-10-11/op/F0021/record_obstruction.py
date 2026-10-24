from pathlib import Path
p=Path('.')
with p.joinpath('ATTEMPT.md').open('a',encoding='utf-8') as f:f.write(r'''

## Example 8: capped-model confinement alone cannot justify transfer (proved logical obstruction)
This is a deterministic, n-dependent example, NOT an iid environment under Assumption 3 and NOT a counterexample to Question 5.
Fix beta>0, 1/2<xi<1, and 0<kappa<1/3. Set every accessible omega to zero except omega_{n,n}=n^2. Cap above at n^kappa. For sufficiently large n, (n,n) is outside the tube |x|<=ceil(n^xi). The unique path visiting (n,n) is the all-right path, with probability 2^{-n}. Consequently

Z_n=1+2^{-n}(exp(beta n^2)-1),
Z_n^T=1+2^{-n}(exp(beta n^kappa)-1)->1.

The tube-restricted partition function R_n is simply the bare walk's probability of staying in the tube. For each i<=n, the two-sided Chernoff bound gives P(|S_i|>ceil(n^xi))<=2 exp(-n^{2xi}/(2n)). A union bound over i shows 1-R_n<=2n exp(-n^{2xi-1}/2)->0. Thus the capped polymer's tube mass R_n/Z_n^T tends to one, whereas the original polymer's tube mass R_n/Z_n tends to zero. Moreover log Z_n is at least beta n^2-n log 2, and log Z_n^T tends to zero, so the difference is far larger than n^{1/3}. This illustrates precisely why confinement of only the capped model is insufficient for Proposition 5's application.
''')
with p.joinpath('LITERATURE.md').open('a',encoding='utf-8') as f:f.write(r'''

## Additional local searches (2026-10-12)
All were read-only.
- `rg -n -m 3 F0021 ~/<private-repo>/06_math_research --glob '*.jsonl' --glob '*.md'` (intake and campaign records).
- `git -C ~/math-open-problems ls-tree -r --name-only origin/master` (initial tree enumeration, output too large; subsequent queries were filtered).
- Same tree enumeration piped to `rg 'F0021|C0120'` and limited to first 35 paths.
- Tree enumeration restricted to probability_campaigns and piped to `rg 'F0021'` (no matching paths).
- `rg -n 'Assumption 1|Zβ|\[DZ16\]|\[BT19\]|\[GL' source.txt` (source model and reference locations).
- `rg -n 'Theorem|alpha|stable|2602' newchaos.txt` (PDF-extracted text contained null bytes; searched pages were subsequently read with PyMuPDF).
- Python XML parsing of saved arXiv entries by titles and summaries; Python extraction of Crossref titles, DOI, dates and reference metadata; Python reading of the complete saved Semantic Scholar citing inventory. Scripts and raw outputs are retained in this folder.
''')
print('Saved logical obstruction and complete local-search log.')
