from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,copy
RUN=Path(__file__).resolve().parents[1]; OUT=RUN/'out'
load=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
save=lambda p,x:p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
sha=lambda s:hashlib.sha256(s.encode()).hexdigest()
cert=load(OUT/'INDEPENDENT_CHECK.json'); assert cert['status']=='PASS'
census=load(OUT/'CLAIM_CENSUS.json')
source=next(x for x in census if x['record']['claim_id']=='A073-NONZERO-ERASURE-BINARY-REMAINDER' and '\\A073\\' in x['source'])
c=copy.deepcopy(source['record']); recorded=c['statement_sha256']; c['statement_sha256']=sha(c['exact_statement'])
c['review_records'].append({'reviewer':'A100/fleet05','timestamp':datetime.now(timezone.utc).isoformat(),
    'verdict':'ACCEPT_AT_FULL_ORIGINAL_STATED_SCOPE_NO_REPAIR','scope':'Entire unchanged explicit-family v1: complete normalized positive-erasure row, binary KL chain, dedicated remainder-only reserve, unbounded retained local row price and bounded H/I; no arbitrary partition or universal terminal bank.',
    'independent_method':'Direct finite signed quadratic/gate coefficients, conditional likelihood ratio and physical edges; independent all-labeled two-bit spectator tensor validation and Jensen/strict-Gibbs reconstruction.',
    'proof_source':str(RUN/'REVIEW.md'),'validation_source':str(OUT/'INDEPENDENT_CHECK.json'),
    'source_recorded_statement_sha256':recorded,'statement_only_sha256':c['statement_sha256'],
    'material_repair_to_reviewed_version':False,'contributor_conflict':False,
    'scope_guard':'Stronger Jensen consequence is a separate A100 claim, not a repair or new version of this source.'})
c['status']='INDEPENDENTLY_ACCEPTED_AT_FULL_ORIGINAL_SCOPE_BY_A100';c['first_unproved_line']=None
statement='For every even d>=2 let delta=2^-d, b(y)=(-1)^(sum_j y_(2j-1)y_(2j)), q(u,v)=-1 only at (1,1), and F_d=b(y)+1_(y=0)(q(u,v)-1). For either i in {u,v}, with complete normalized laws mu_i(T)=p_(T+i)/e_i and r_i(T)=p_T+p_(T+i), retaining only the other pair coordinate gives influence-weighted lost conditional KL L_i=e_i[D(mu_i||r_i)-D(Cmu_i||Cr_i)], where e_i=delta/2. Put R(delta)=(1+delta-3delta^2/4)/(1+delta^2/4). Then 0<L_i/e_i<=log2(R(delta))/2<=log2(77/65)/2<1/8. Their combined loss satisfies L_u+L_v<=delta log2(R(delta))/2<delta^2/(2ln2), and also L_u+L_v<delta/8<=Inf_(y1)/20. The same row divergences and remainders hold after tensoring with any common Boolean spectator on independent fresh coordinates. These allowances pay only the two discarded conditional KL remainders; retained M_i/e_i>d/2+3/4 remains unpaid, and no globally available or repeatedly reusable terminal reserve is asserted.'
new={'claim_id':'A100-BINARY-REMAINDER-JENSEN-BOUND','version':1,'exact_statement':statement,
     'hypotheses':['Actual finite uniform Boolean signs in the displayed family; d even and >=2; bits and ordinary physical influence',
                   'Complete residual reference is marginalized, not conditioned on derivative support; KL zero terms continuous',
                   'Common spectator is independent on fresh physical coordinates; both row laws share its same normalized spectrum',
                   'Dedicated physical reserve, if used, is exclusive to these two remainder bills; no universal core payment assumed'],
     'statement_sha256':sha(statement),'contributors':['A100/fleet05; explicit boundary family credited to A073'],
     'proof_source':{'path':str(RUN/'REVIEW.md'),'locator':'New quantitative refinement: Jensen bound','checker':str(RUN/'code/check_binary.py'),'output':str(OUT/'INDEPENDENT_CHECK.json')},
     'proof_dependencies':[{'claim_id':'A073-NONZERO-ERASURE-BINARY-REMAINDER','version':1,'usage':'Unchanged family/signed row identities independently reconstructed above; original lemma accepted by A098 and separately A100'}],
     'review_records':[],'status':'SCOPED_ANALYTIC_JENSEN_REFINEMENT_PROVED_PENDING_INDEPENDENT_REVIEW',
     'supersedes':[],'refutes':[],'first_unproved_line':None,'next_consumers':['A073','A096','A001','A098','A099','A085','A094','B20']}
save(RUN/'CLAIMS.json',[c,new]); print('Saved original-source independent review and separately pending Jensen refinement.',flush=True)
