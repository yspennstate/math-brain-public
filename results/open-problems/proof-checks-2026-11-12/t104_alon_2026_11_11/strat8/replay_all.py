"""PROVED certificates / OPEN residual: all exact replay, no NumPy or solver.

Run from this folder with python3 -B replay_all.py. No network or subprocess.
"""
import os,json,time,hashlib,resource
from pathlib import Path
os.environ['OPENBLAS_NUM_THREADS']='1'
os.environ['OMP_NUM_THREADS']='1'


def main():
    start=time.time()
    from axis_bernstein import replay_conversion
    from zero_face import main as algebra
    from verify_domain import replay as domain
    from verify_boxes import replay as boxes
    from pendant_certificate import replay as pendant
    from exact_witnesses import main as witnesses
    from witness_residual import replay as residual
    from verify_cover import replay as cover
    algebra();domain();replay_conversion();n=boxes();pendant();witnesses();residual();stats=cover()
    files=['provenance.json','axis_bernstein.py','zero_face.py','face_intervals.py','centered_bounds.py','cover_face.py',
           'verify_domain.py','verify_boxes.py','verify_cover.py','pendant_certificate.py',
           'exact_witnesses.py','witness_residual.py','moment_bounds.py','directional_bounds.py',
           'rational_rays.py','replay_all.py','face_boxes.json','exact_witnesses.json',
           'global_cover.json','positive_partition_boxes.json','open_boxes.json',
           'pendant_certificate.json','strong_moment_cells.json','enhanced_moment_cells.json',
           'directional_moment_cells.json','prior_face_boxes.json','prior_weight_moment_cells.json']
    hashes={name:hashlib.sha256(Path(name).read_bytes()).hexdigest()for name in files}
    result=dict(status='PROVED: all saved certificates replayed; OPEN: full residual positivity',
                local_boxes=n,global_counts=stats['counts'],
                elapsed_seconds=time.time()-start,maxrss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
                sha256=hashes)
    assert result['maxrss_bytes']<4*1024**3
    with open('verification.json','w')as f:json.dump(result,f,indent=2)
    print('PROVED: all exact replay completed, seconds',round(result['elapsed_seconds'],2),
          'maximum RSS bytes',result['maxrss_bytes'],flush=True)
    print('OPEN: the retained frontier has not been proved nonnegative.',flush=True)
    with open('LOG.md','a')as f:
        import datetime
        f.write('\nPROVED: '+datetime.datetime.now().astimezone().isoformat(timespec='seconds')+
                '. Full exact replay passed: '+str(n)+' local boxes; global counts '+str(stats['counts'])+
                '; 34 residual witnesses and the pendant subface theorem. Peak RSS '+str(result['maxrss_bytes'])+
                ' bytes. verification.json records hashes and results. The residual OPEN leaves are not certified.\n')

if __name__=='__main__':main()
