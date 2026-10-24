"""Run only the integrator's schema reader, on our draft; no ingestion."""
from pathlib import Path
import ast, importlib.util, json, sqlite3, sys, time

ROOT=Path(__file__).resolve().parent
LIVE=Path(r'~\math-brain-build\tools\integrate_drafts.py')

def main():
    sys.dont_write_bytecode=True
    reference=ROOT/'reference';reference.mkdir(exist_ok=True)
    source=LIVE.read_text(encoding='utf-8')
    copied=reference/'integrate_drafts.py'
    copied.write_text(source,encoding='utf-8')
    tree=ast.parse(source)
    functions=[node for node in tree.body if isinstance(node,ast.FunctionDef) and 'spec must be mathbrain-draft-v1' in (ast.get_source_segment(source,node) or '')]
    assert len(functions)==1
    name=functions[0].name
    assert len(functions[0].args.args)==1
    def no_database(*args,**kwargs):
        raise RuntimeError('Schema-only validation must not open any database')
    sqlite3.connect=no_database
    sys.path.insert(0,r'~\math-brain-build\src')
    spec=importlib.util.spec_from_file_location('w441_draft_schema_reference',copied)
    module=importlib.util.module_from_spec(spec)
    sys.modules[spec.name]=module
    spec.loader.exec_module(module)
    start=time.perf_counter()
    payload,errors=getattr(module,name)(ROOT/'drafts'/'bundle_001.json')
    receipt={'command':'python -X utf8 validate_bundle.py','validator_source':str(LIVE),'copied_reference':str(copied),'actual_function':name,'seconds':time.perf_counter()-start,'errors':errors,'entry_count':len(payload.get('entries',[])),'relation_count':len(payload.get('relations',[])),'database_open_guard':'sqlite3.connect disabled during import and validation','live_database_opened':False,'ingestion_run':False,'mathematical_proof_check':False}
    (ROOT/'DRAFT_SCHEMA_CHECK.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(receipt,indent=2))
    if errors:raise SystemExit(1)

if __name__=='__main__':main()
