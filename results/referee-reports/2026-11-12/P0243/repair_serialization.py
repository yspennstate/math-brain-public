from pathlib import Path
p=Path('stopping_audit.py')
s=p.read_text().replace('json.dump(summary,f,indent=2)','json.dump(summary,f,indent=2,default=lambda x:x.item())').replace('json.dumps(summary,indent=2)','json.dumps(summary,indent=2,default=lambda x:x.item())')
p.write_text(s)
