from pathlib import Path
import json,hashlib
team=Path(__file__).resolve().parents[5]
for who in ['A066','A067','A069']:
    for p in (team/'agents'/who/'runs').rglob('CLAIMS.json'):
        for c in json.loads(p.read_text(encoding='utf-8-sig')):
            variants={}
            for key in ['statement','exact_statement']:
                for ascii in [True,False]:
                    b=json.dumps({key:c['exact_statement'],'hypotheses':c['hypotheses']},sort_keys=True,separators=(',',':'),ensure_ascii=ascii).encode()
                    variants[key+str(ascii)]=hashlib.sha256(b).hexdigest()
            print(c['claim_id'],c['statement_sha256'],variants)
