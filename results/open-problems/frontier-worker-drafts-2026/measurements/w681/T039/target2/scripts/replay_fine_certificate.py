"""Rebuild selected accepted matrices using saved exact centers and witnesses."""
from pathlib import Path
import argparse,hashlib,json,time
import certify_fine_cells as fine

core=fine.core;ROOT=fine.ROOT
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--start',type=int,default=0);ap.add_argument('--count',type=int,default=1);ap.add_argument('--max-seconds',type=int,default=400);cli=ap.parse_args()
    state=json.loads((ROOT/'logs/fine_checkpoint.json').read_text(encoding='utf-8'))
    for name,value in state['input_hashes'].items():assert hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==value,name
    meta=json.loads((ROOT/'logs/fine_run_metadata.json').read_text(encoding='utf-8'))
    args=argparse.Namespace(**meta['parameters']);core.hardware();core.ctx.prec=args.precision
    tabs=core.tables(args);started=time.perf_counter();outcomes=[]
    rows=state['accepted'];start=cli.start if cli.start>=0 else len(rows)+cli.start
    chosen=rows[start:start+cli.count];assert chosen
    for index,row in enumerate(chosen,start):
        if time.perf_counter()-started>cli.max_seconds-100:break
        args.x_panels=row['x_panels']
        coefficients=[float.fromhex(c) for c in row['center_coefficients_binary64_hex']]
        core.pos.CENTER=tuple((c,) for c in coefficients)
        # Bypass numerical center selection: the saved dyadic coefficients are inputs.
        B,tail,info=fine.graded.original_majorant(row['rho_lo'],row['rho_hi'],args,tabs)
        assert hashlib.sha256(B.tobytes()).hexdigest()==row['matrix_upper_sha256'],'Matrix differs'
        assert info['radial_edges_sha256']==row['radial_edges_sha256']
        assert tail==row['outside_hs_squared_upper'],'Tail differs'
        witnesspath=ROOT/row['witness_file'];assert hashlib.sha256(witnesspath.read_bytes()).hexdigest()==row['witness_sha256']
        saved=json.loads(witnesspath.read_text(encoding='utf-8'))
        v=core.np.array([float.fromhex(x) for x in saved['v_binary64_hex']])
        expected=core.np.array([float.fromhex(x) for x in saved['row_upper_binary64_hex']])
        assert len(v)==len(B) and core.np.all(v>0)
        for i in range(len(B)):
            _,upper=core.base.sum_enclosure(core.base.mul_pos_hi(B[i],core.base.div_pos_hi(v,float(v[i]))))
            assert upper==expected[i],('Row differs',i)
        assert float(expected.max())==row['finite_operator_upper']
        lam=core.base.ball(row['finite_operator_upper'],row['finite_operator_upper']);tau=core.base.ball(tail,tail)
        total=core.base.bounds((lam*lam+tau).sqrt())[1]
        assert total==row['operator_upper'] and total<2
        outcome={'accepted_row_index':index,'rho':[row['rho_lo'],row['rho_hi']],'x_panels':row['x_panels'],'operator_upper':total,'matrix_and_all_rows_recomputed':True,'matrix_sha256':row['matrix_upper_sha256']}
        outcomes.append(outcome);print(json.dumps(outcome),flush=True);del B
    result={'requested_rows':len(chosen),'replayed_rows':len(outcomes),'complete':len(outcomes)==len(chosen),'outcomes':outcomes,'seconds':time.perf_counter()-started,'scope':'Recomputes interval matrix entries, full outside tail and every witness row. Uses source tables whose recipe and byte hashes are checked; regenerate table stages separately for a fully fresh run.'}
    (ROOT/f'logs/fine_replay_{start}_{cli.count}.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    return 0 if result['complete'] else 3
if __name__=='__main__':raise SystemExit(main())
