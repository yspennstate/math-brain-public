import json
import pathlib
import re

root=pathlib.Path('~/<private-repo>/06_math_research/probability_1000_intake_claude_20260907/raw')
jobs=[('heydenreich_hofstad_highd_2017_statements.txt',r'Open Problem 9\.1|Open Problem 16\.3'),('pete_pgg_notes_statements.txt',r'Conjecture 12\.7')]
result=[]
for filename,pattern in jobs:
    with (root/filename).open(encoding='utf-8') as stream:
        for line_no,line in enumerate(stream,1):
            match=re.search(pattern,line)
            if match:
                record={'path':str(root/filename),'line':line_no,'statement_context':line[match.start():match.start()+950].strip()}
                result.append(record)
                print(json.dumps(record,ensure_ascii=False))
pathlib.Path('primary_target_checks.json').write_text(json.dumps(result,indent=2,ensure_ascii=False),encoding='utf-8')
