import pathlib,subprocess,json
R=pathlib.Path(__file__).parent
Q={
'rough_data_curl':'https://arxiv.org/pdf/2607.13341',
'critical_perturbations_curl':'https://arxiv.org/pdf/2602.00895',
'openalex_citing_doi':'https://api.openalex.org/works?filter=cites:https%3A%2F%2Fdoi.org%2F10.1007%2Fs00030-025-01090-2&per-page=100',
}
log=[]
for k,u in Q.items():
 try:
  p=subprocess.run(['curl.exe','-L','--max-time','35','-sS','-w','\nHTTP_STATUS:%{http_code}',u],capture_output=True,timeout=45)
  data,_,status=p.stdout.rpartition(b'\nHTTP_STATUS:')
  suffix='.pdf' if data.startswith(b'%PDF') else '.json'
  (R/(k+suffix)).write_bytes(data)
  res={'service':k,'date':'2026-10-12','query':u,'exit':p.returncode,'http_status':status.decode(errors='replace'),'bytes':len(data),'stderr':p.stderr.decode(errors='replace')[:300]}
  if suffix=='.pdf':
   import pymupdf
   d=pymupdf.open(stream=data,filetype='pdf');(R/(k+'.txt')).write_text('\n'.join(f'\nPAGE {i+1}\n'+pg.get_text() for i,pg in enumerate(d)),encoding='utf8')
  log.append(res)
 except Exception as e:log.append({'service':k,'date':'2026-10-12','query':u,'error':str(e)})
(R/'curl_followup_log.json').write_text(json.dumps(log,indent=2),encoding='utf8')
print(json.dumps(log,indent=2))
