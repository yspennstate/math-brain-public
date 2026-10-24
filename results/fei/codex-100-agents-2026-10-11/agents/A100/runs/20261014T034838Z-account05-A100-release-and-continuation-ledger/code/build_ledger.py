from pathlib import Path
RUN=Path(__file__).resolve().parents[1]
PREV=RUN.parent/'20261014T010218Z-account05-A100-release-and-continuation-ledger'
s=(PREV/'code/release.py').read_text(encoding='utf-8')
chunk=s[s.index('groups={}'):s.index('md=[')]
head='''from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,re
RUN=Path(__file__).resolve().parents[1]; OUT=RUN/'out'; AGENT=RUN.parent.parent; ROOT=AGENT.parent.parent
PREV=AGENT/'runs/20261014T010218Z-account05-A100-release-and-continuation-ledger'
def load(p): return json.loads(p.read_text(encoding='utf-8-sig'))
def save(p,x): p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\\n',encoding='utf-8')
def digest(s): return hashlib.sha256(s.encode()).hexdigest()
now=datetime.now(timezone.utc).isoformat(); census=load(OUT/'CLAIM_CENSUS.json'); claims=load(RUN/'CLAIMS.json')
specs=[(c['claim_id'],c['version']) for c in claims]
'''
extras={'ACCEPT_AT_FULL_ORIGINAL_STATED_SCOPE','ACCEPT_AT_FULL_ORIGINAL_STATED_SCOPE_NO_REPAIR',
        'ACCEPT_AT_FULL_STATED_SCOPE','ACCEPT_AT_FULL_STATED_SCOPE_NO_REPAIR','ACCEPT_AT_FULL_STATED_SCOPE_WITHOUT_REPAIR',
        'ACCEPT_AT_STATED_SCOPE_NO_SUBSTANTIVE_REPAIR','ACCEPT_AT_STATED_SCOPE_WITHOUT_REPAIR','ACCEPT_AT_STATED_UNIFORM_SCOPE',
        'FORMAL_STATEMENT_HOLDS_AT_UNCHANGED_SCOPE_WITH_AUXILIARY_SOURCE_ERROR',
        'FORMAL_STATEMENT_HOLDS_UNCHANGED_AUXILIARY_ERROR_ISOLATED','HOLDS_AT_ORIGINAL_FORMAL_STATEMENT_NO_REPAIR','HOLDS_FULL_STATED_NARROW_CLAIM'}
chunk=chunk.replace('accepted=[]; partial=[]; pending=[]; withdrawn=[]; ignored=[]',
                    'full_verdicts.update('+repr(extras)+')\naccepted=[]; partial=[]; pending=[]; withdrawn=[]; ignored=[]')
(RUN/'code/ledger.py').write_text(head+chunk+'\nprint(json.dumps(ledger[\'counts\'],indent=2),flush=True)\n',encoding='utf-8')
print('Built source-preserving ledger classifier; no upstream or prior-run file changed.')
