from pathlib import Path
import json
from html.parser import HTMLParser
x=json.loads(Path('site_repo_actions.txt').read_text());print('ACTIONS')
for r in x.get('workflow_runs',[]):print(r['name'],r['status'],r['conclusion'],r['head_sha'],r['created_at'],r['html_url'])
x=json.loads(Path('site_proof_tree.txt').read_text());print('TREE SHA',x['sha'])
class P(HTMLParser):
 def __init__(self):super().__init__();self.s=[]
 def handle_data(self,d):self.s.append(d)
p=P();p.feed(Path('site_proof_page.txt').read_text());s=' '.join(p.s);Path('site_proof_page_plain.txt').write_text(s,encoding='utf8')
print('PAGE TEXT',s)
print('VERIFICATION',Path('site_proof_verify.txt').read_text())
