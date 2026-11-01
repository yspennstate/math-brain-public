from pathlib import Path
import psutil, json
rows=[]
for p in psutil.process_iter(['pid','name','cpu_times','memory_info']):
 try:
  if (p.info['name'] or '').lower() in ['lean.exe','lake.exe']:
   rows.append({'pid':p.pid,'name':p.info['name'],'cpu_seconds':sum(p.info['cpu_times'][:2]),'rss_mb':p.info['memory_info'].rss/1048576})
 except (psutil.NoSuchProcess,psutil.AccessDenied): pass
Path('lean_process_diagnostic.json').write_text(json.dumps(rows,indent=2),encoding='utf-8')
print(json.dumps(rows),flush=True)
