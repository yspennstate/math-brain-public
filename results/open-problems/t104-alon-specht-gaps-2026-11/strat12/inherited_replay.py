"""Run one STRAT11 verification without writing in either source directory."""
import os,sys,runpy,json,importlib,hashlib
from pathlib import Path

HERE=Path(__file__).resolve().parent
SOURCE=HERE/'STRAT11'
sys.dont_write_bytecode=True
sys.path.insert(0,str(SOURCE))

def readonly_sources(event,args):
    # Python audit hooks fail closed on source-directory writes. Existing
    # inherited verifier main blocks are only run when they are read-only.
    if event=='open':
        path,mode,flags=args
        if isinstance(path,(str,bytes,os.PathLike)):
            p=Path(os.fsdecode(path)).resolve()
            if SOURCE in p.parents or HERE/'STRAT10' in p.parents:
                if (isinstance(mode,str) and any(c in mode for c in 'wax+')) or flags & (os.O_WRONLY|os.O_RDWR|os.O_CREAT|os.O_TRUNC|os.O_APPEND):
                    raise PermissionError('Inherited proof sources are read-only: '+str(p))
    elif event in ('os.remove','os.rename','os.rmdir','os.mkdir'):
        for path in args[:2]:
            if isinstance(path,(str,bytes,os.PathLike)):
                p=Path(os.fsdecode(path)).resolve()
                if SOURCE in p.parents or HERE/'STRAT10' in p.parents:
                    raise PermissionError('Inherited proof source mutation denied: '+str(p))

def main():
    script=sys.argv[1]
    allowed=['verify_provenance.py','verify_frame.py','verify_filters.py','verify_cone.py',
             'verify_corner.py','verify_examples.py','verify_rotation.py','verify_corner_faces.py','verify_overlay.py']
    assert script in allowed
    os.chdir(SOURCE);sys.addaudithook(readonly_sources)
    if script=='verify_provenance.py':
        # The provided copy omits two transient PID files. Recheck every
        # actual proof input, and record this precise difference from the
        # original driver rather than forging missing operational files.
        missing=[]
        for name,digest in json.loads((SOURCE/'source_hashes.json').read_text()).items():
            p=SOURCE/name
            if not p.exists():
                missing.append(name)
            else:
                assert hashlib.sha256(p.read_bytes()).hexdigest()==digest,name
        assert set(missing)=={'STRAT9/codex.pid','STRAT10/codex.pid'}
        for name,digest in json.loads((SOURCE/'provenance.json').read_text()).items():
            assert hashlib.sha256((SOURCE/name).read_bytes()).hexdigest()==digest,name
        print('PROVED: all STRAT11 mathematical source/input fingerprints matched.')
        print('OPEN: literal inherited provenance skips only absent operational PID files:',missing)
    elif script=='verify_overlay.py':
        mod=importlib.import_module('verify_overlay')
        result,leaves=mod.replay()
        expected=json.loads((SOURCE/'remaining_open_boxes.json').read_text())['boxes']
        assert sorted(leaves,key=lambda x:x['node'])==sorted(expected,key=lambda x:x['node'])
        assert result==json.loads((SOURCE/'cover_summary.json').read_text())
        print('PROVED: STRAT11 overlay leaves exactly match the STRAT12 input; source files were not rewritten.')
    else:
        runpy.run_path(str(SOURCE/script),run_name='__main__')

if __name__=='__main__':main()
