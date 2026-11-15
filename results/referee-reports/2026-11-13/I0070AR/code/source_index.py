from pathlib import Path
import re,json
rules={
'survey_arxiv':r'^(?:Theorem (?:3\.13|4\.7|5\.1|5\.7)|Proposition 5\.9|Assumption (?:4\.1|6\.1)|Problem 6|Lemma 4\.3)',
'survey_published':r'^(?:Theorem (?:3\.13|4\.7|5\.1|5\.7)|Proposition 5\.9|Assumption (?:4\.1|6\.1)|Problem 6|Lemma 4\.3)',
'critical_I_arxiv':r'^(?:Proposition 3\.(?:10|12)|Theorem 4\.[78])',
'critical_II_published':r'^(?:Theorem (?:4\.15|6\.3)|Corollary 6\.5|Proposition (?:3\.9|6\.8))',
'critical_II_arxiv':r'^(?:Theorem (?:4\.15|6\.3)|Corollary 6\.5|Proposition (?:3\.9|6\.8))',
'portal_published':r'^(?:Theorem (?:3\.9|4\.5|5\.3)|Lemma 2\.7)',
'variational_published':r'^(?:Theorem 3\.[3458]|Lemma 4\.1)',
'liu_arxiv':r'^(?:Theorem (?:1\.1|4\.1)|Definition 1\.1)',
'navier_published':r'^(?:Theorem (?:2\.4|4\.1)|Proof of Theorem 4\.1 Part)',
'reaction_arxiv':r'^Theorem (?:2\.12|4\.8)',
'singular_arxiv':r'^Lemma 3\.11',
 'temporal_published':r'^Theorem [13][. —]'}
records=[]
for name,pat in rules.items():
    page=0
    for lineno,line in enumerate((Path('sources')/(name+'.txt')).read_text().splitlines(),1):
        m=re.fullmatch(r'===== PDF PAGE (\d+) =====',line)
        if m: page=int(m[1])
        if re.search(pat,line): records.append(dict(source=name,pdf_page=page,line=lineno,text=line))
Path('data/source_locations.json').write_text(json.dumps(records,indent=2,ensure_ascii=False)+'\n')
print(f'{len(records)} candidate locators; incidental references retained for transparency')
