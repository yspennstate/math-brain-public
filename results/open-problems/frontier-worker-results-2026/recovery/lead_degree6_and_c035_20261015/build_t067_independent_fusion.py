from pathlib import Path
import os,json,subprocess,hashlib
H=Path(__file__).resolve().parent
vc=Path('C:/Program Files (x86)/Microsoft Visual Studio/18/BuildTools/VC/Tools/MSVC/14.50.35717');sdk=Path('C:/Program Files (x86)/Windows Kits/10');v='10.0.26100.0'
cl=vc/'bin/Hostx64/x64/cl.exe';assert cl.is_file()
env=dict(os.environ);env['PATH']=str(cl.parent)+os.pathsep+env.get('PATH','');env['INCLUDE']=';'.join(map(str,[vc/'include']+[sdk/'Include'/v/x for x in ['ucrt','shared','um','winrt','cppwinrt']]))
env['LIB']=';'.join(map(str,[vc/'lib/x64',sdk/'Lib'/v/'ucrt/x64',sdk/'Lib'/v/'um/x64']))
assert not (H/'T067_INDEPENDENT_FUSION_BUILD_RECEIPT.json').exists()
args=[str(cl),'/nologo','/O2','/EHsc','/std:c++17','/Fo:'+str(H/'t067_independent_fusion.obj'),'/Fe:'+str(H/'t067_independent_fusion.exe'),str(H/'t067_independent_fusion.cpp')]
with (H/'T067_INDEPENDENT_FUSION_BUILD.log').open('wb') as out:p=subprocess.run(args,env=env,cwd=H,stdout=out,stderr=subprocess.STDOUT,timeout=120,creationflags=subprocess.CREATE_NO_WINDOW|subprocess.BELOW_NORMAL_PRIORITY_CLASS)
assert p.returncode==0,'Read build log'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
r={'status':'Build PASS only; no mathematical audit','source_sha256':sha(H/'t067_independent_fusion.cpp'),'exe_sha256':sha(H/'t067_independent_fusion.exe'),'compiler_sha256':sha(cl),'args':args}
(H/'T067_INDEPENDENT_FUSION_BUILD_RECEIPT.json').write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8');print(json.dumps(r))
