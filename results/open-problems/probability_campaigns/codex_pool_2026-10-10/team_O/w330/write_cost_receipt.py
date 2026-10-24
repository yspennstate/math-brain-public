from pathlib import Path
import json

def write_cost_receipt():
    root=Path(__file__).resolve().parent
    experiments=[]
    for path in (root/'measurements').glob('*.json'):
        item=json.loads(path.read_text(encoding='utf-8'))
        if isinstance(item,dict) and 'experiment' in item:
            experiments.append(item)
    result=dict(agent='w330',provider_token_usage='not exposed to worker',
        credit_spend='Billing not exposed; no paid external APIs invoked',
        public_web_reads=0,external_paid_api_calls=0,
        measured_experiments=len(experiments),
        experiments_seconds=round(sum(x['seconds'] for x in experiments),4),
        live_store_writes=0,counts_pending_audit=True,
        scope='Instrumented Python function time; excludes shell/tool queue latency and language-model inference cost')
    (root/'COST_RECEIPT.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    return result

if __name__=='__main__': print(json.dumps(write_cost_receipt()))
