from pathlib import Path
import json,hashlib,datetime,ctypes
R=Path(__file__).resolve().parents[1];(R/'out').mkdir(exist_ok=True)
ROOT=R.parents[3]
def save(p,v):p.write_text(json.dumps(v,indent=2)+'\n',encoding='utf-8')
receipts=[]
def rd(p):
 b=p.read_bytes();t=b.decode('utf-8-sig');receipts.append({'path':str(p),'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b)});return t
board=rd(ROOT/'BOARD.md');lead=rd(ROOT/'claude/B01/STREAM_NOTES.md')
save(R/'out/BOARD_LINES.json',board.splitlines())
for l in board.splitlines():
 if l.startswith(('# FEI','- A001 |','- A003 |','- A005 |','- A079 |','- A085 |','- A090 |','- A094 |','- A096 |','- A097 |','- A099 |')):print(l)
latest={}
for a in ['A085','A090','A094','A096','A097','A099','A086']:
 ds=sorted(p for p in (ROOT/'agents'/a/'runs').iterdir() if p.is_dir() and (p/'REPORT.md').exists())
 latest[a]=str(ds[-1]);print(a,ds[-1])
save(R/'out/LATEST_SOURCES.json',latest)
for a in ['A085','A090','A097','A099']:
 d=Path(latest[a]);t=rd(d/'REPORT.md');(R/'out'/('SOURCE_'+a+'_REPORT.txt')).write_text(t,encoding='utf-8')
 print('\n'+a+' REPORT\n'+t[:15000])
state=Path(r'~\.claude\compute\compute_state.json')
cs=json.loads(rd(state));print('GOVERNOR_TS',cs['ts'])
class MS(ctypes.Structure):
 _fields_=[('dwLength',ctypes.c_ulong),('dwMemoryLoad',ctypes.c_ulong)]+[(n,ctypes.c_ulonglong) for n in ['ullTotalPhys','ullAvailPhys','ullTotalPageFile','ullAvailPageFile','ullTotalVirtual','ullAvailVirtual','ullAvailExtendedVirtual']]
s=MS();s.dwLength=ctypes.sizeof(s);ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(s))
actual={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'available_ram_MB':s.ullAvailPhys//1048576,'commit_available_MB':s.ullAvailPageFile//1048576,'stale_governor_ts':cs['ts'],'governor_restarted':False}
save(R/'out/COMPUTE_SNAPSHOT.json',actual);print('ACTUAL_MEMORY',actual)
save(R/'out/INTAKE_RECEIPTS.json',receipts)
