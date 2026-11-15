"""Resumable uniform-rho certificate, exact outward slabs and per-slab witnesses."""
from pathlib import Path
import argparse,datetime,hashlib,json,sys,time
import certify_fine_cells as fine
core=fine.core;ROOT=fine.ROOT

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--max-seconds',type=int,default=480);cli=ap.parse_args();start=time.perf_counter()
    args=argparse.Namespace(table_rho_max=.43,cutoff=8.,q_bins=2048,a_bins=8192,exp_bins=65536,v_panels=64,precision=100,x_panels=1600,chunk=24,power_steps=40,label='fine',rho_min=.4,rho_max=.43,rho_panels=30)
    hw=core.hardware();core.ctx.prec=100
    files=['scripts/run_fine_certificate.py','scripts/certify_fine_cells.py','scripts/fine_tables.py','scripts/certify_positive_cells_graded.py','scripts/certify_positive_cells_centered.py','scripts/certify_positive_cells_scaled.py','scripts/certify_positive_cells.py','scripts/measure_operator.py','cut_bounds/plur_cert.py','cut_bounds/plur_cert_positive.py']
    hashes={name:hashlib.sha256((ROOT/name).read_bytes()).hexdigest() for name in files}
    statefile=ROOT/'logs/fine_checkpoint.json'
    if statefile.exists():
        state=json.loads(statefile.read_text(encoding='utf-8'));assert state['input_hashes']==hashes,'Certificate source changed'
    else:
        edges=[.4,.4015]+[j/1000 for j in range(402,431)]
        state={'input_hashes':hashes,'accepted':[],'pending':[[edges[i],edges[i+1],1600] for i in reversed(range(len(edges)-1))],'attempts':0}
    meta={'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'argv':sys.argv,'parameters':vars(args),'hardware':hw,'input_hashes':hashes,'python':sys.version,'numpy':fine.graded.np.__version__,'scipy':core.scipy.__version__,'flint':core.flint.__version__,'random_generator':None,'seed':None,'reproduction':'Table stages are generated from scratch or recipe/hash-verified checkpoints. Quantile accuracy, quartic-fit accuracy and power-iteration accuracy are not assumed; the resulting exact binary64 partition, center and positive witness are verified using directed interval operations.'}
    (ROOT/'logs/fine_run_metadata.json').write_text(json.dumps(meta,indent=2)+'\n',encoding='utf-8')
    tabs=core.tables(args)
    def checkpoint():
        temporary=statefile.with_suffix('.json.part')
        temporary.write_text(json.dumps(state,indent=2)+'\n',encoding='utf-8')
        temporary.replace(statefile)
    checkpoint()
    while state['pending']:
        if time.perf_counter()-start>cli.max_seconds-100:
            print('TIME CHECKPOINT; resume this same command.',flush=True);break
        lo,hi,n=state['pending'].pop();args.x_panels=n
        row=core.certify(lo,hi,args,tabs);state['attempts']+=1
        with (ROOT/'logs/fine_attempts.jsonl').open('a',encoding='utf-8') as f:f.write(json.dumps(row)+'\n')
        print(json.dumps({k:row[k] for k in ('rho_lo','rho_hi','x_panels','finite_operator_upper','outside_hs_squared_upper','operator_upper','pass','seconds')}),flush=True)
        if row['pass']:
            state['accepted'].append(row)
            with (ROOT/'logs/fine_accepted.jsonl').open('a',encoding='utf-8') as f:f.write(json.dumps(row)+'\n')
        elif hi-lo>0.00025:
            mid=(lo+hi)/2;state['pending'].append([mid,hi,n]);state['pending'].append([lo,mid,n])
        elif n<2400:state['pending'].append([lo,hi,2400])
        elif n<3200:state['pending'].append([lo,hi,3200])
        elif hi-lo>0.0000625:
            mid=(lo+hi)/2;state['pending'].append([mid,hi,n]);state['pending'].append([lo,mid,n])
        else:
            state['pending'].append([lo,hi,n]);checkpoint();raise RuntimeError('Enclosure limit: no full certificate claimed')
        checkpoint()
    endpoint=max((r['rho_hi'] for r in state['accepted']),default=.4)
    summary={'complete':not state['pending'],'certified_prefix_endpoint':endpoint,'accepted_slabs':len(state['accepted']),'pending_slabs':len(state['pending']),'attempts':state['attempts'],'worst_operator_upper':max((r['operator_upper'] for r in state['accepted']),default=None),'elapsed_seconds_this_chunk':time.perf_counter()-start}
    (ROOT/'logs/fine_summary.json').write_text(json.dumps(summary,indent=2)+'\n',encoding='utf-8');print('SUMMARY',json.dumps(summary),flush=True)
    return 0 if summary['complete'] else 3
if __name__=='__main__':raise SystemExit(main())
