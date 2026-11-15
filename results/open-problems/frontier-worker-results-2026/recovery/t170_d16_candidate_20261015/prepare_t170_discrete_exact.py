from pathlib import Path
import json,hashlib,subprocess,os
H=Path(__file__).resolve().parent;W=Path('~/brain_workers/w676/T170')
screen=json.loads((H/'T170_SCREEN_new16_RECEIPT.json').read_bytes());assert screen['screen_margin']>0
base=W/'scripts/certify_bpn_exact.cpp';raw=base.read_bytes().decode();prefix=raw[:raw.index('static std::uint64_t table_hash(')]
prefix=prefix.replace('std::chrono::seconds(265)','std::chrono::seconds(500)').replace('265 second foreground guard','500 second foreground guard')
main=(H/'t170_discrete_screen.cpp').read_bytes().decode().split('int main(int argc,char**argv)',1)[1]
main='int main(int argc,char**argv)'+main
assert 'SCALE=1;MINIMUM_RATES=1;' in main
main=main.replace('SCALE=1;MINIMUM_RATES=1;','SCALE=1ULL<<40;MINIMUM_RATES=1;').replace('std::vector<double> g(last+1)','std::vector<U> g(last+1)')
source=H/'t170_discrete_exact.cpp';assert not source.exists();source.write_bytes((prefix+main).encode())
binding=json.loads(Path('~/brain_workers/w683/checks/t170_c012_binding_own.json').read_bytes())
gamma=[r['upper_units'] for r in binding['inputs']['gamma_boundaries']]
rates=(H/'t170_discrete_d16.txt').read_text(encoding='utf-8').splitlines()[2]
inputfile=H/'t170_discrete_exact_d16.txt';assert not inputfile.exists();inputfile.write_text('16 11 10000\n'+' '.join(map(str,gamma))+'\n'+rates+'\n',encoding='utf-8')
vc=Path('C:/Program Files (x86)/Microsoft Visual Studio/18/BuildTools/VC/Tools/MSVC/14.50.35717');sdk=Path('C:/Program Files (x86)/Windows Kits/10');version='10.0.26100.0'
compiler=vc/'bin/Hostx64/x64/cl.exe';env=dict(os.environ)
env['PATH']=str(compiler.parent)+os.pathsep+env.get('PATH','')
env['INCLUDE']=';'.join(map(str,[vc/'include']+[sdk/'Include'/version/x for x in ['ucrt','shared','um','winrt','cppwinrt']]))
env['LIB']=';'.join(map(str,[vc/'lib/x64',sdk/'Lib'/version/'ucrt/x64',sdk/'Lib'/version/'um/x64']))
args=[str(compiler),'/nologo','/O2','/EHsc','/std:c++17','/Fo:'+str(H/'t170_discrete_exact.obj'),'/Fe:'+str(H/'t170_discrete_exact.exe'),str(source)]
with (H/'T170_DISCRETE_EXACT_BUILD.log').open('wb') as out:p=subprocess.run(args,cwd=H,env=env,stdout=out,stderr=subprocess.STDOUT,timeout=120,creationflags=subprocess.CREATE_NO_WINDOW|subprocess.BELOW_NORMAL_PRIORITY_CLASS)
assert p.returncode==0,'Read exact build log'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
r={'status':'PASS build only','base_source_sha256':sha(base),'source_sha256':sha(source),'input_sha256':sha(inputfile),'exe_sha256':sha(H/'t170_discrete_exact.exe'),'compiler_sha256':sha(compiler),'args':args,'scale':2**40,'guard_seconds':500,'admission':'PENDING rigorous run and two independent exact-content reviews'}
(H/'T170_DISCRETE_EXACT_BUILD_RECEIPT.json').write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8');print(json.dumps(r))
