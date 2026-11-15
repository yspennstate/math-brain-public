from pathlib import Path
from datetime import datetime
import json,hashlib,subprocess,time
H=Path(__file__).resolve().parent;W=Path('~/brain_workers/w676/T170')
start=time.monotonic();cap=10000
f=[0]*(cap+1)
for n in range(1,cap+1):f[n]=f[n-1]+(n-1).bit_count()
checks=0
for n in range(2,cap+1):
 for b in range(1,n//2+1):
  assert f[n-b]+f[b]+b<=f[n],(n,b)
  checks+=1
rates={}
for d in [16,17]:
 m=d-1;rate=[2*m*n-2*f[n] for n in range(cap+1)]
 assert all(0<rate[n]<=2*m*n for n in range(1,cap+1))
 assert all(rate[n]**m>=(2*m)**m*n**(m-1) for n in range(1,cap+1))
 rates[d]=rate
receipt={'at':datetime.now().astimezone().isoformat(),'status':'PASS finite exact split inequalities and integer rate comparison','cap':cap,'split_checks':checks,'seconds':time.monotonic()-start,'f_1000':f[1000],'rates_1000':{d:r[1000] for d,r in rates.items()},'scope':'Computational part of unary-hypercube embedding proof only; no FPP comparison or admission verdict'}
(H/'T170_DISCRETE_RATE_RECEIPT.json').write_bytes((json.dumps(receipt,indent=2)+'\n').encode())
q=json.loads(Path('~/brain_workers/w683/checks/t170_c012_binding_own.json').read_bytes())
gammas=[row['upper_units']/2**40 for row in q['inputs']['gamma_boundaries']]
sourcepath=W/'scripts/certify_bpn_numeric.cpp';original=sourcepath.read_bytes().decode('utf-8')
prefix=original[:original.index('static std::uint64_t table_hash(')]
main=r'''
int main(int argc,char**argv) {
 try {
  if(argc!=2) throw std::runtime_error("usage: own-discrete-screen input");
  std::ifstream in(argv[1]);int last,maximum;
  in>>DIM>>last>>maximum;SCALE=1;MINIMUM_RATES=1;
  std::vector<double> g(last+1);for(int n=1;n<=last;n++)in>>g[n];
  ISO.resize(maximum+1);for(int& r:ISO)in>>r;
  if(!in || last<6 || last>11)throw std::runtime_error("bad input");
  Table empty;
  Table p=stage({1000},{1000},empty,g[1]);
  p=stage({10000,1000},{100,10},p,g[2]);
  p=stage({1000,100,10},{100,10,10},p,g[3]);
  p=stage({1000,100,10,10},{100,100,10,1},p,g[4]);
  p=stage({1000,100,100,10,1},{100,10,10,1,1},p,g[5]);
  for(int n=6;n<=last;n++){
   std::vector<int> box(n,1),keep(n,1);box[0]=1000;box[1]=100;box[2]=10;box[3]=10;
   keep[0]=100;keep[1]=10;keep[2]=10;
   if(n==last){std::fill(keep.begin(),keep.end(),0);keep[0]=1;}
   p=stage(box,keep,p,g[n]);
  }
  return 0;
 }catch(const std::exception&e){std::cerr<<e.what()<<"\n";return 2;}
}
'''
source=H/'t170_discrete_screen.cpp';assert not source.exists();source.write_bytes((prefix+main).encode())
for d,rate in rates.items():
 (H/f't170_discrete_d{d}.txt').write_text(f'{d} 11 {cap}\n'+' '.join(format(x,'.17g') for x in gammas)+'\n'+' '.join(map(str,rate))+'\n',encoding='utf-8')
receipt.update(source_base_sha256=hashlib.sha256(sourcepath.read_bytes()).hexdigest(),screen_source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),boundary_receipt_sha256=hashlib.sha256(Path('~/brain_workers/w683/checks/t170_c012_binding_own.json').read_bytes()).hexdigest())
(H/'T170_DISCRETE_RATE_RECEIPT.json').write_bytes((json.dumps(receipt,indent=2)+'\n').encode())
cmd=H/'build_t170_discrete_screen.cmd'
cmd.write_text('@echo off\ncall "C:/Program Files (x86)/Microsoft Visual Studio/18/BuildTools/VC/Auxiliary/Build/vcvars64.bat" >nul\nif errorlevel 1 exit /b %errorlevel%\ncl /nologo /O2 /EHsc /std:c++17 /Fo:"'+str(H/'t170_discrete_screen.obj')+'" /Fe:"'+str(H/'t170_discrete_screen.exe')+'" "'+str(source)+'"\n',encoding='utf-8')
with (H/'T170_DISCRETE_BUILD.log').open('wb') as out:
 p=subprocess.run(['cmd.exe','/d','/c',str(cmd)],cwd=H,stdout=out,stderr=subprocess.STDOUT,creationflags=subprocess.CREATE_NO_WINDOW|subprocess.BELOW_NORMAL_PRIORITY_CLASS,timeout=120)
assert p.returncode==0,'Read T170_DISCRETE_BUILD.log'
print(json.dumps(receipt))
