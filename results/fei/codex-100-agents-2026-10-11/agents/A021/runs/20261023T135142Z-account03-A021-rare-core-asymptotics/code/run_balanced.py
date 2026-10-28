from pathlib import Path
import hashlib,json,subprocess,sys
R=Path(__file__).resolve().parents[1]
spec={'family':'same t2 adjacent DATA edit using one arbitrary balanced Boolean controller on3 controls','domain':'ALL70 truth tables with4 positive and4 negative values; pilot first2 lexicographic combinations','case_count':70,'symmetry':'none','arithmetic':'integer Walsh and exact Fraction prime-log identities with proved40-term enclosures','memory_estimate_mb':100,'pilot_max_seconds':60,'main_max_seconds':120,'helper_version':{n:hashlib.sha256((R/'code'/n).read_bytes()).hexdigest() for n in ('balanced.py','check.py','arithmetic.py')},'all_dimensional_bridge':'Analytic BALANCED_COROLLARY.md Parseval/light-heavy argument, not finite extrapolation.'}
(R/'BALANCED_SPEC.json').write_text(json.dumps(spec,indent=2)+'\n',encoding='utf-8')
for label,args,timeout in [('balanced_pilot',['--pilot'],60),('balanced_full',[],120)]:
 p=subprocess.run([sys.executable,'-X','utf8',str(R/'code/balanced.py'),*args],capture_output=True,text=True,encoding='utf-8',timeout=timeout)
 (R/'out'/(label+'.log')).write_text(p.stdout+p.stderr,encoding='utf-8');print(label,p.returncode,p.stdout[-1400:],p.stderr[-1400:],flush=True)
 if p.returncode:raise SystemExit(p.returncode)
