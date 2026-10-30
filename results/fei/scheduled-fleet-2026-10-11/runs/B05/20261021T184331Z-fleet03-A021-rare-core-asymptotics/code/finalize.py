from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
R=Path(__file__).resolve().parents[1]; A=R.parents[1]
def write(p,s): p.write_text(s,encoding='utf-8',newline='')
def dump(p,s): write(p,json.dumps(s,indent=2)+'\n')
old=A.parent/'A025/runs/20261021T162308Z-fleet03-A025-rare-event-counterfamily/code/check.py'
utils=old.read_text(encoding='utf-8').split('def run():')[0]
write(R/'code/old_utilities.py',utils)
dump(R/'out/HELPER_PROVENANCE.json',{'source':str(old),'source_sha256':hashlib.sha256(old.read_bytes()).hexdigest(),'copied_part':'all definitions before def run(); no old run executed','local_path':'code/old_utilities.py','local_sha256':hashlib.sha256(utils.encode()).hexdigest()})
target='For every even m>=4 and activation width t>=0 in the original A025 balanced quadratic bent three-label two-edit family, the physical policy x, then y0 at x=0, then y1 at BOTH y0 children has R3=p(3m-6+3t)delta/4 and complete original-terminal S3=8 IT3-HT3>=p(3m+2+4t). The already booked Rold and Ux fit delta/4 and delta/6 of SAME S3; the new reached rare-partner excess Uy fits the disjoint delta/12 fraction. Complete controller continuations and all five leaves obey 10I-H>=2IT3+(1-delta/2)S3. The proposed transport Uy<=delta S_current/12 to EVERY later data-history cut is false: exposing all data leaves Sfinal=8p(1+t)-A(t), while Uy>=p delta(m/16-17/8); 3m>134+32t certifies failure (t=0: all even m>=46).'
claim={
 'claim_id':'A021-SAME-OWNER-PARTNER-CONTINUATION','version':1,'exact_statement':target,
 'hypotheses':['Uniform cube; base-two Fourier entropy and total physical influence','PROOF.md exact original A025 family; even m>=4; t>=0 integer','Original fair two-controller weights (1/2,1/4,1/4), balancing sign z unqueried','SAME physical bank includes activation; all terminal spectra and original reaches retained'],
 'statement_sha256':hashlib.sha256(target.encode()).hexdigest(),'contributors':['A021','A025 (source second-query continuation and returning-query obstruction)'],
 'proof_source':['PROOF.md','OBSTRUCTION.md','code/check.py','code/replay.py','code/boundary.py'],
 'proof_dependencies':['A021 run20261014T075029Z DERIVATION final owner subclause, rederived here','A025 run20261021T162308Z PROOF second-query and single-edit clauses, reconstructed at scoped use only','Elementary Fourier entropy/pivot identities; scalar two-amplitude entropy and tensorization'],
 'review_records':[{'reviewer':'A021','scope':'Independent analytic reconstruction of A025 second-query, coincident-label controller, and returning-erasure subclauses only; not independent review of own extension','status':'SCOPED_SOURCE_CLAUSES_HOLD'}],
 'status':'AUTHOR_CHECKED_PROOF_PENDING_INDEPENDENT_REVIEW','supersedes':[],'refutes':['Fixed-third-fraction transport Uy<=delta S_current/12 at all later original-terminal cuts'],
 'first_unproved_line':'Transport the remaining ancestor/source credit through arbitrary nonflat core queries, retaining every old debit and full terminal entropy; the fixed fraction of current terminal surplus is explicitly false.',
 'next_consumers':['A025','A029','A028','A023','A087','A094']}
dump(R/'CLAIMS.json',[claim])
progress={
 'protocol_revision':'2026-10-11-execution-v2','run_id':R.name,'stream':'B05','packet_id':'A021',
 'gap_id':'C024-SAME-OWNER-MIXED-DATA-TRANSFER','attempt_id':'A021-stage17-partner-owner-and-final-cut-obstruction',
 'method':'Consume A025 completed second query; exact spectral and edge proof of third-query payment; complete original-terminal owner; analytic final-cut counterexample to fixed-fraction transport.',
 'mathematical_delta':'Returning bad partner and its opposite sibling paid with additional disjoint delta/12 of SAME owner; total booked fraction delta/2<=1/32. Fixed-third-fraction arbitrary-cut transport fails if3m>134+32t.',
 'deliverable_status':'COMPLETE_LOCAL_REVIEW_PENDING','mathematical_status':'SCOPED_PROOF_AND_POTENTIAL_OBSTRUCTION; FULL_FEI_OPEN',
 'claim_versions_used':['A021 final owner subclause at run20261014T075029Z','A025 second-query/returning-erasure subclauses at run20261021T162308Z'],
 'claims_created_or_changed':[{'claim_id':claim['claim_id'],'version':1}],
 'source_artifacts':['PROOF.md','OBSTRUCTION.md','out/SOURCE_RECEIPTS.json','SEARCH_SPEC.json','REPLAY_SPEC.json','out/DIRECT.json','out/REPLAY.json','out/BOUNDARY.json','out/LEAN.json'],
 'next_consumers':claim['next_consumers'],
 'next_action':'Use the SAME ancestor credit plus signed slack earned by intervening actual data queries to cross the certified final-owner-collapse obstruction; first obtain an all-prefix invariant on this family, then remove quadratic/point profile.',
 'stagnant_substantive_attempts':0,
 'blockers':['General source-credit transport remains open; independent review and supervisor copy pending','Full FEI has neither an accepted proof nor an actual unbounded-ratio family'],
 'packet_ids':['A021']}
dump(R/'PROGRESS.json',progress); dump(R/'PACKET_DELTA.json',progress)
write(A/'STATUS.md','STATE: A021 stage17: returned rare partner plus opposite sibling paid from SAME owner; bookings total delta/2<=1/32; fixed-third-fraction all-cut transport fails at t=0 even m>=46; exact validation saved; FEI OPEN.\nNEXT: Carry SAME ancestor credit and earned signed query slack through all data prefixes across final-terminal-owner collapse; A025/A029/A028/A087/A094 review.\n')
stamp=datetime.now(timezone.utc).isoformat()
with (A/'WORKLOG.md').open('a',encoding='utf-8',newline='') as f:
 f.write('\n'+stamp+' stage17 '+R.name+': consumed A025 second-query result; derived R3=p(3m-6+3t)delta/4, full five-leaf terminal lower bound, new Uy fraction delta/12, old fractions preserved. Exact checker first failed only because independently subtracted equal entropy intervals gave positive zero-bill error; fixed by truth-table equality, retained receipt. Independent DFT replay. Proved fixed-third-fraction transport false at3m>134+32t, all even m>=46 at t=0; full FEI open. No work stopped or background work launched.\n')
with (A/'LEARNED.md').open('a',encoding='utf-8',newline='') as f:
 f.write('\nStage17: On SAME A025 family query x,y0(at x=0),y1 in BOTH y0 children. Partner d=(p delta,p(1-delta)); each conditional R release=3pdelta/2, remaining aggregate R3=p(3m-6+3t)delta/4. Five-leaf IT3=p[(m+1)/2+(m-2)delta/2+t]; S3>=p(3m+2+4t). Original Rold and Ux retain delta/4 and delta/6 bookings; reached Uy<=pm delta/4 fits new disjoint delta/12, totaldelta/2<=1/32. Singleton/coincident-label controller proof retains all terminals. Complete10I-H>=2IT3+(1-delta/2)S3. Do NOT iterate fractions without checking the owner: Uy>=pdelta(m/16-17/8), but after ALL data Sfinal=8p(1+t)-A(t)<=8p(1+t). Thus fixed-third-fraction transport fails whenever3m>134+32t (t=0 all even m>=46). A global potential needs ancestor memory/source scale or earned signed query slack; it cannot merely reprice all old debt as O(delta) of current terminal surplus. Equal-table zero entropy decrements must be certified as exact zero, not by subtracting independent intervals.\n')
print(json.dumps({'artifacts':'initial protocol and rolling files saved','claim':claim['claim_id'],'helper_saved':True}))
