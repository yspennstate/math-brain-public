"""Write the additive primary-population finding from pinned experiment evidence."""
from pathlib import Path
from datetime import datetime,timezone
import argparse
import hashlib
import json
import subprocess
import sys


def main():
    p=argparse.ArgumentParser();p.add_argument('--evidence-root',type=Path,required=True);p.add_argument('--report',type=Path,required=True);p.add_argument('--mesh',type=Path,required=True);a=p.parse_args()
    now=datetime.now(timezone.utc).isoformat(); root=a.evidence_root; src=root/'source_v1'; out=root/'finding_v1';out.mkdir(exist_ok=False)
    manifest=json.loads((src/'MANIFEST.json').read_text(encoding='utf-8'))
    selected=[]; mutation=[]
    for name in ('PROTOCOL_PLIT.md','STAGE1_SIZING.json','grade_plit.py','stage1.py','run_plit_s1_haiku/results/STAGE1.md','run_plit_s1_opus/results/STAGE1.md'):
        old=next(r for r in manifest if Path(r['evidence'])==src/Path(name))
        selected.append({'subject':old['subject'],'source_type':'MUTABLE_TARGET','evidence':old['evidence'],'sha256':old['sha256'],'observed_at':old['observed_at'],'locator':name,'kind':'SOURCE_SNAPSHOT'})
        live=Path(old['subject']); mutation.append({'subject':str(live),'before_sha256':old['sha256'],'after_sha256':hashlib.sha256(live.read_bytes()).hexdigest(),'auditor_writes':0})
    (out/'MUTATION_LOG.json').write_text(json.dumps({'as_of':now,'scope':'Original experiment source and reports; additive audit tooling is separate','targets':mutation},indent=2)+'\n',encoding='utf-8')
    receipts=subprocess.run([sys.executable,str(a.mesh),'receipts','--agent','codex-brain-math-0907'],capture_output=True,text=True,encoding='utf-8',check=True)
    (out/'MESH_RECEIPTS.json').write_text(receipts.stdout,encoding='utf-8')
    record=next(r for r in json.loads(receipts.stdout)['receipts'] if r['message_id']=='msg-9d6202e2f7')
    def pin(file,kind,subject=None):
        file=Path(file);return {'subject':subject or str(file.resolve()),'source_type':'IMMUTABLE_SOURCE','evidence':str(file.resolve()),'sha256':hashlib.sha256(file.read_bytes()).hexdigest(),'observed_at':now,'locator':'entire file','kind':kind}
    mutation_pin=pin(out/'MUTATION_LOG.json','MUTATION_LOG')
    receipt_pin=pin(out/'MESH_RECEIPTS.json','NOTIFICATION_SEND_RECEIPT','mesh://message/msg-9d6202e2f7')
    reconstruction_pin=pin(root/'reconstruction_v2'/'RESULT.json','SOURCE_SNAPSHOT')
    def pending():return {'status':'PENDING','receipt_id':None,'occurred_at':None,'evidence':[]}
    metadata={'schema':'audit-report-v2','finding_id':'PLIT-0907-001','title':'The primary comparison changed population after sizing',
        'classification':'CONFIRMED GATE/REPORTING DEFECT','severity':'HIGH','state':'SENT',
        'audited_at':now,'audit_started_at':'2026-09-07T04:31:17Z','audit_deadline':'2026-09-07T07:28:19Z','mandate_status':'ACTIVE','owner_stop_evidence':[],
        'auditor':'codex-brain-math-0907','responsible_agent':'claude-daily-review-0907',
        'mutation_boundary':{'mode':'AUDIT_ONLY','audited_target_write_count':0,'evidence':[mutation_pin],'owner_authorization_evidence':[]},
        'snapshots':selected+[reconstruction_pin],
        'notification':{'required':True,'send':{'status':'SENT','receipt_id':record['message_id'],'occurred_at':record['created_at'],'evidence':[receipt_pin]},'delivery':pending(),'acknowledgement':pending()},
        'model_identity':{'runtime':'CODEX_CLI','requested_model':None,'served_model':None,'status':'UNVERIFIABLE','response_evidence':[]},
        'correction':{'required':True,'status':'PENDING','snapshots':[]},
        'reaudit':{'required':True,'status':'PENDING','audited_at':None,'auditor':None,'test':None,'evidence':[]},
        'refutation':{'status':'NOT_APPLICABLE','test':None,'evidence':[]},
        'human_review':{'status':'PENDING','reviewer':None,'reviewed_at':None,'checklist':{k:False for k in ('governing_prompt_and_scope','evidence_semantics_and_provenance','mutation_boundary','notification_delivery_and_ack','model_identity','mandate_timing_and_owner_stop','counter_case_and_impact','disclosure_safety')},'limitations':['Semantic truth is not machine-proved; deterministic validation is not semantic closure; source proof labels and response identity are not established by arithmetic.']}}
    # Receipt snapshot may already prove delivery/ack at its own observation time.
    if record.get('delivered_at'):
        metadata['notification']['delivery']={'status':'DELIVERED','receipt_id':record['message_id'],'occurred_at':record['delivered_at'],'evidence':[dict(receipt_pin,kind='NOTIFICATION_DELIVERY_RECEIPT')]};metadata['state']='NOTIFIED'
    if record.get('acked_at'):
        metadata['notification']['acknowledgement']={'status':'ACKNOWLEDGED','receipt_id':record['message_id'],'occurred_at':record['acked_at'],'evidence':[dict(receipt_pin,kind='NOTIFICATION_ACK_RECEIPT')]};metadata['state']='ACKNOWLEDGED'
    body='''
## Scope

Audit the overnight PLIT stage1 primary-population labels and sampling support.
The original experiment, keys, sample and serving machinery were not edited.
An additive report producer and synthetic controls were written as audit tooling;
those are author-verified and received a separate root review. This finding does
not certify proof labels, every corpus item, solver identity, or overall brain utility.

## Pinned evidence

The JSON metadata pins the observed protocol, sizing, old code and old reports.
The source_v1 manifest binds 1,676 local files, including every stage and pilot
verdict and complete frozen sample. Reconstruction_v2 binds the corrected arithmetic.
The two independent paths are protocol_report.py (Python records) and check_sqlite.py
(SQL joins and exact rational binomial recurrence). Neither imports grade_plit.py.

## Reproduction

The protocol's Hypotheses and tests section registers tier A; all tiers pooled
are explicitly secondary and descriptive. Amendment 3 assigns tier B only to
solvers whose pilot tier-A accuracy exceeds 85 percent. The pilots select A for
Haiku and B for Opus. The old grader nevertheless labels all 146 flawed items
PRIMARY for both solvers and recomputes a pilot rule from stage outcomes.

The registered comparisons reconstructed from the frozen rows are:

| Solver | Tier | Brain | None | Difference pp | Approximate 95% paired interval | Exact two-sided p | Pairs / sizing target |
|---|---|---:|---:|---:|---|---:|---:|
| Haiku | A |44/82|46/82|−2.44|[−13.64,8.76]|0.8318|82/120|
| Opus | B |37/64|38/64|−1.56|[−8.40,5.27]|1.0000|64/146|

All 1,170 planned stage arm/item rows exist and parse under the stricter reader.
The pooled −4.1pp values reproduce, but are not the registered primary analysis.
Stage sizing computed targets within each chosen tier, then sampled 146 flawed
items across both tiers; therefore serving completion did not attain the planned
primary-stratum pair counts. No new observed-power claim is made.

## Impact

The report answers a different population question under the primary label and
makes the planned study look adequately sized. It also invites treating a pooled
detection-only nominal significance as confirmatory harm, despite its descriptive
registration. Current evidence shows no clear improvement under these notes and
solvers. It does not establish equivalence, absence of useful brain functions, or
that generic note bulk caused the effect. Every result remains conditional on
the existing proof-label validity, which has known uncertainty.

## Strongest counter-case

An amendment could have replaced the primary tier rule with a pooled estimand,
or a different sample could supply the missing primary pairs. Reading the complete
current protocol and frozen samples refutes that explanation: amendment3 explicitly
retains tier A below ceiling, and the stage has 82 A plus 64 B. The pooled numbers
are arithmetically correct, so this is a label/scope/support defect, not fabricated
verdict counts. The sizing formula itself is a design approximation, not a guarantee
of achieved power even if its target is met.

## Required correction

Lead the experiment report and result memory with the registered tier comparisons;
label pooled and detection-only lines descriptive. Record the shortfall against
primary-stratum targets. Preserve the original stage and protocol; do not top up
after viewing outcomes and present the result as the original frozen test. A future
stage requires a separately frozen design and adequate per-stratum quotas.

## Re-audit criteria

A different reviewer must replay all raw counts and check corrected report/memory
bytes against the protocol. Inject ambiguous verdicts, duplicate keys, missing rows,
wrong arms, wrong primary tiers and changed snapshot members; each must reject or
produce an explicitly incomplete state. Keep semantic source review separate.

## Recurrence prevention

Name the registered population, primary metric and unit before computing a result.
Compare the target population to observed support, including exclusions and each
primary stratum. Complete transport or total row count cannot substitute for the
specified denominator. Carry descriptive/confirmatory roles into machine-readable
outputs and never promote nonsignificance to equivalence. Reuse the shared
measurement_population_mismatch_family_2026_07_16 mechanism; the additive producer
provides strict identity, pairing and target-support checks without changing the
frozen experimental rows.

## Human semantic review

Pending. Root independently found and corrected two weaknesses in the additive
reader (prefix verdict normalization and duplicate JSON key members); 20 controls
now pass and the reconstruction is unchanged. This is not independent semantic
validation of every source proof. The campaign is still active until its deadline;
this finding remains open for correction and re-audit.
'''
    a.report.parent.mkdir(parents=True,exist_ok=True)
    with a.report.open('x',encoding='utf-8') as f:f.write('# PLIT-0907-001\n\n```audit-report\n'+json.dumps(metadata,indent=2)+'\n```\n'+body)
    print(str(a.report))


if __name__=='__main__':main()
