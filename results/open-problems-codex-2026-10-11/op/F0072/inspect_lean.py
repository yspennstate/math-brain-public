import time,json
try:
 import psutil
 for p in psutil.process_iter(['pid','name','create_time','cpu_times','memory_info']):
  if p.info['name'] and p.info['name'].lower() in ['lean.exe','lake.exe','lean','lake']:
   print(json.dumps({'pid':p.pid,'name':p.info['name'],'elapsed':time.time()-p.info['create_time'],'cpu_seconds':sum(p.info['cpu_times'][:2]),'rss':p.info['memory_info'].rss}),flush=True)
except Exception as e: print(repr(e))
