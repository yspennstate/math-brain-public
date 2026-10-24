import json, pathlib

ROOT=pathlib.Path(__file__).resolve().parent
base=pathlib.Path('~/<private-repo>/06_math_research/probability_1000_intake_claude_20260907')
records=[]
for name in ['brain_bundle_C006p02.json','brain_bundle_C006a05.json']:
    path=base/name
    data=json.loads(path.read_text(encoding='utf-8'))
    def walk(obj):
        if isinstance(obj,dict):
            direct=json.dumps({k:v for k,v in obj.items() if isinstance(v,(str,int,float,bool))},ensure_ascii=False).lower()
            if 'p0309' in direct or 'positive-temperature crystalline gibbs' in direct:
                records.append({'path':str(path),'record':obj})
                print(json.dumps(records[-1],ensure_ascii=False,indent=2))
                return
            for value in obj.values(): walk(value)
        elif isinstance(obj,list):
            for value in obj: walk(value)
    walk(data)
(ROOT/'P0309_EXTRACT.json').write_text(json.dumps(records,ensure_ascii=False,indent=2),encoding='utf-8')
