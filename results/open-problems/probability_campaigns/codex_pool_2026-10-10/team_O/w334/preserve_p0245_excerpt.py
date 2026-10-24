from pathlib import Path
import json

here=Path(__file__).resolve().parent
path=Path('~/Downloads/Probability_1000_20h_20260906/sources/aldous_fill_2014/text.txt')
text=path.read_text(encoding='utf-8-sig')
offset=text.find('Open Problem 6.30')
assert offset>=0
excerpt=text[offset:offset+600]
assert 'reversible chain' in excerpt and '(n' in excerpt
out=json.loads((here/'primary_source_excerpts.json').read_text(encoding='utf-8'))
if not any(x['problem_id']=='P0245' for x in out):
    out.append({'problem_id':'P0245','path':str(path),'excerpts':[{'pattern':'Open Problem 6.30','character':offset,'text':excerpt}]})
    (here/'primary_source_excerpts.json').write_text(json.dumps(out,indent=2,ensure_ascii=False),encoding='utf-8')
print(json.dumps({'primary_excerpt_records':len(out),'P0245_locator_preserved':True}))
