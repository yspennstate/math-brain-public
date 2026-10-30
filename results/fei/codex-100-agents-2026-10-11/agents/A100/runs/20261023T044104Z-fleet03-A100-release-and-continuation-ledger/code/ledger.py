from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,re
RUN=Path(__file__).resolve().parents[1]; OUT=RUN/'out'; AGENT=RUN.parent.parent; ROOT=AGENT.parent.parent
PREV=AGENT/'runs/20261022T235742Z-fleet03-A100-release-and-continuation-ledger'
def load(p): return json.loads(p.read_text(encoding='utf-8-sig'))
def save(p,x): p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def digest(s): return hashlib.sha256(s.encode()).hexdigest()
now=datetime.now(timezone.utc).isoformat(); census=load(OUT/'CLAIM_CENSUS.json'); claims=load(RUN/'CLAIMS.json')
specs=[(c['claim_id'],c['version']) for c in claims]
groups={}
for x in census+[{'source':str(RUN/'CLAIMS.json'),'record':c,'statement_only_sha256':c['statement_sha256']} for c in claims]:
    c=x['record']; groups.setdefault((c['claim_id'],str(c.get('version')),c.get('exact_statement','')),[]).append(x)
full_verdicts={'ACCEPT_AT_STATED_SCOPE','HOLDS_AT_STATED_SCOPE','HOLDS','ACCEPT_AT_STATED_FINITE_SCOPE',
    'ACCEPT_AT_ORIGINAL_STATED_SCOPE_NO_REPAIR','ACCEPT_REPORTED_THEOREM_AT_STATED_SCOPE',
    'ACCEPT_AT_EXACT_STATED_SCOPE_CONDITIONAL_ON_DECLARED_BASELINE','HOLDS_AT_ENTIRE_ORIGINAL_STATEMENT_SCOPE',
    'HOLDS_AT_EXACT_STATED_SCOPE','HOLDS_AT_EXPLICIT_STATED_SCOPE','HOLDS_AT_FULL_STATED_SCOPE','HOLDS_AT_ORIGINAL_SCOPE',
    'HOLDS_AT_ORIGINAL_STATED_SCOPE_NO_REPAIR','HOLDS_AT_ORIGINAL_WHOLE_SCOPE_NO_REPAIR','HOLDS_AT_STATED_BOOLEAN_SCOPE',
    'HOLDS_AT_STATED_SCOPE_WITH_ACCEPTED_NODE_BOUNDARY_DEPENDENCY','HOLDS_AT_WHOLE_ORIGINAL_SCOPE_NO_REPAIR',
    'INDEPENDENTLY_ACCEPTED_AT_STATED_SCOPE_BY_A081'}
full_verdicts.update({'ACCEPT_AT_FULL_STATED_SCOPE_NO_REPAIR', 'ACCEPT_AT_FULL_ORIGINAL_STATED_SCOPE', 'ACCEPT_AT_FULL_ORIGINAL_STATED_SCOPE_NO_REPAIR', 'ACCEPT_AT_FULL_STATED_SCOPE_WITHOUT_REPAIR', 'ACCEPT_AT_STATED_UNIFORM_SCOPE', 'ACCEPT_AT_STATED_SCOPE_NO_SUBSTANTIVE_REPAIR', 'ACCEPT_AT_STATED_SCOPE_WITHOUT_REPAIR', 'HOLDS_AT_ORIGINAL_FORMAL_STATEMENT_NO_REPAIR', 'FORMAL_STATEMENT_HOLDS_UNCHANGED_AUXILIARY_ERROR_ISOLATED', 'HOLDS_FULL_STATED_NARROW_CLAIM', 'FORMAL_STATEMENT_HOLDS_AT_UNCHANGED_SCOPE_WITH_AUXILIARY_SOURCE_ERROR', 'ACCEPT_AT_FULL_STATED_SCOPE'})
full_verdicts.add('HOLDS_AT_FULL_ORIGINAL_STATED_SCOPE')
full_verdicts.update({'HOLDS_AT_FULL_NAMED_TWO_RESET_SCOPE_WITHOUT_REPAIR','HOLDS_AT_FULL_ORIGINAL_STATED_SCOPE_NO_REPAIR'})
full_verdicts.update({'HOLDS_AT_EXACT_SUPPLIED_REFERENCE_SCOPE','HOLDS_AT_EXACT_FIRST_FRONTIER_SCOPE'})
accepted=[]; partial=[]; pending=[]; withdrawn=[]; ignored=[]
for (cid,version,statement),records in groups.items():
    evidence=[]
    for x in records:
        c=x['record']
        for rv in c.get('review_records',[]):
            if not isinstance(rv,dict) or not rv.get('reviewer'): continue
            verdict=str(rv.get('verdict','')).upper(); who=str(rv['reviewer'])
            if rv.get('reviewed_version') is not None and str(rv['reviewed_version'])!=version:
                ignored.append({'claim_id':cid,'claim_version':version,'reason':'review explicitly concerns another version','source':x['source'],'review':rv}); continue
            if 'CONTRIBUTOR' in verdict or rv.get('contributor_conflict') or rv.get('reviewer_contributed_repair') or rv.get('substantive_repair_supplied') or rv.get('material_repair_to_reviewed_version'):
                ignored.append({'claim_id':cid,'claim_version':version,'reason':'repair contributor or declared conflict; not independent acceptance','source':x['source'],'review':rv}); continue
            reviewer_ids=set(re.findall(r'(?<![A-Za-z0-9])A\d{3}(?!\d)',who))
            contributor_ids=set(re.findall(r'(?<![A-Za-z0-9])A\d{3}(?!\d)',' '.join(map(str,c.get('contributors',[])))))
            if reviewer_ids & contributor_ids:
                ignored.append({'claim_id':cid,'claim_version':version,'reason':'reviewer listed as contributor','source':x['source'],'review':rv}); continue
            evidence.append({'reviewer':who,'verdict':verdict,'source':x['source'],'scope':rv.get('scope',rv.get('scope_guard',rv.get('method'))),'review_record':rv})
    row={'claim_id':cid,'version':records[0]['record'].get('version'),'exact_statement':statement,
         'statement_only_sha256':digest(statement),'hypotheses':records[0]['record'].get('hypotheses',[]),
         'hypothesis_variants':[json.loads(s) for s in sorted({json.dumps(x['record'].get('hypotheses',[]),sort_keys=True,ensure_ascii=False) for x in records})],
         'sources':[x['source'] for x in records],'review_evidence':evidence,
         'A100_full_reconstruction_this_stage':cid=='A094-CANONICAL-RETURN-POSITIVE-DEBIT-EXACT' and version=='1',
         'source_statuses':sorted({str(x['record'].get('status')) for x in records}),'remote_copy_verified_this_stage':False}
    if cid=='A021-UNIFORM-RARE-CORE-EXPANSION' and version=='1':
        row['release_status']='WITHDRAWN_AS_FULL_CLAIM_FALSE_REMAINDER'; withdrawn.append(row)
    elif any(e['verdict'].startswith(('GAP','ERROR','REFUT','RETRACT','REJECT')) for e in evidence):
        row['release_status']='FULL_ACCEPTANCE_WITHHELD_SCOPE_OBJECTION'; partial.append(row)
    elif any(e['verdict'] in full_verdicts for e in evidence):
        row['release_status']='RECORDED_ACCEPTANCE_AT_ORIGINAL_SCOPE'; accepted.append(row)
    elif any(('ACCEPT' in e['verdict'] or e['verdict'].startswith('HOLDS')) and 'PENDING' not in e['verdict'] and 'DEFERRED' not in e['verdict'] for e in evidence):
        row['release_status']='PARTIAL_OR_SPECIFIED_CLAUSE_ACCEPTANCE_ONLY'; partial.append(row)
    else:
        row['release_status']='NO_FULL_INDEPENDENT_ACCEPTANCE_OBSERVED'; pending.append(row)
ledger={'snapshot_utc':now,'full_FEI_status':'OPEN','interpretation':'Versioned local adoption proposal; full-scope upstream review receipts are not fresh A100 proof reconstructions. Fragment acceptance does not accept a manuscript, prove universal payment, or verify a remote release.',
        'full_verdict_dictionary':sorted(full_verdicts),'accepted':accepted,'partial':partial,'pending':pending,'withdrawn_as_full_claim':withdrawn,
        'counts':{'accepted_statement_versions':len(accepted),'partial_statement_versions':len(partial),'pending_statement_versions':len(pending),'withdrawn_statement_variants':len(withdrawn)},'ignored_nonindependent_or_other_version_reviews':ignored}
save(OUT/'THEOREM_RELEASE_LEDGER.json',ledger)
old=load(PREV/'out/THEOREM_RELEASE_LEDGER.json'); old_ids={(x['claim_id'],str(x['version'])) for x in old['accepted']}; new_ids={(x['claim_id'],str(x['version'])) for x in accepted}
save(OUT/'ACCEPTANCE_DELTA.json',{'previous_recorded_statement_groups':len(old['accepted']),'current_recorded_statement_groups':len(accepted),
    'newly_observed_id_versions':[{'claim_id':c,'version':v} for c,v in sorted(new_ids-old_ids)],
    'no_longer_full_id_versions':[{'claim_id':c,'version':v,'reason':'Author-owned review-certificate wrapper is not itself independently accepted by its author; underlying source review remains recorded at its stated subclaim scope.' if c=='A009-SCOPED-REVIEW-A007-AFFINE-NORMALIZER' else 'See exact current version review evidence; not automatically a mathematical refutation.'} for c,v in sorted(old_ids-new_ids)],
    'counts_guard':'Changed intake and explicit additional full-review verdict spellings change counts; new groups are not necessarily newly proved theorems. Previous files remain unchanged.'})

print(json.dumps(ledger['counts'],indent=2),flush=True)
