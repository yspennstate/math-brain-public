from pathlib import Path
import json,xml.etree.ElementTree as E
p=Path('LITERATURE.md')
s=p.read_text(encoding='utf8')
s=s.replace('The precise theorem/page is recorded below after inspection.','Lemma 4 is on PDF pp. 10--11; Remark 2 on PDF p. 11 explicitly extends its continuity argument to periodic trees. The downloaded version is arXiv:1911.03330v2 (11 December 2019).')
s+='''\n## Verified survival-continuity input\n\nHuang, arXiv:1911.03330v2, Lemma 4, PDF p. 10:\n\n> Lemma 4. p(λ) is continuous on [0, ∞).\n\nRemark 2, PDF p. 11:\n\n> The same construction can be carried out on periodic trees straightforwardly, thus proving the continuity of survival probability p(λ) for the contact process on periodic trees. As a consequence, the contact process dies out at λ1 on periodic trees.\n\nHis periodic-tree convention gives one upward neighbor and b downward neighbors in the regular case; taking b=d-1 gives the present d-regular tree. This supplies the Section 2 input but addresses space-time survival, not the source's snapshot percolation question. It is not classified as SOLVED_IN_LITERATURE.\n'''
ns={'a':'http://www.w3.org/2005/Atom'}
for e in E.parse('arxiv_stationary_energy.txt').findall('a:entry',ns):
 aid=e.findtext('a:id',namespaces=ns)
 if '0907.2843' in aid:
  names=', '.join(a.findtext('a:name',namespaces=ns) for a in e.findall('a:author',ns))
  title=' '.join(e.findtext('a:title',namespaces=ns).split())
  s+=f'\nAdditional related lead returned by the stationary-percolation query: {names}, *{title}*, {aid}. This concerns the two-dimensional contact process, not T_d, and is not a source-matching solution.\n'
p.write_text(s,encoding='utf8')
print('Updated literature theorem locator')
