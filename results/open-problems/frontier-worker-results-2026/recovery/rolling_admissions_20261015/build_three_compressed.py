from pathlib import Path
import os,json,subprocess,hashlib
H=Path(__file__).resolve().parent
vc=Path('C:/Program Files (x86)/Microsoft Visual Studio/18/BuildTools/VC/Tools/MSVC/14.50.35717');sdk=Path('C:/Program Files (x86)/Windows Kits/10');v='10.0.26100.0'
cl=vc/'bin/Hostx64/x64/cl.exe';assert cl.is_file()
env=dict(os.environ);env['PATH']=str(cl.parent)+os.pathsep+env.get('PATH','');env['INCLUDE']=';'.join(map(str,[vc/'include']+[sdk/'Include'/v/x for x in ['ucrt','shared','um','winrt','cppwinrt']]))
env['LIB']=';'.join(map(str,[vc/'lib/x64',sdk/'Lib'/v/'ucrt/x64',sdk/'Lib'/v/'um/x64']))
assert not (H/'T170_THREE_COMPRESSED_BUILD_RECEIPT.json').exists()
args=[str(cl),'/nologo','/O2','/EHsc','/std:c++17','/Fo:'+str(H/'t170_three_compressed.obj'),'/Fe:'+str(H/'t170_three_compressed.exe'),str(H/'t170_three_compressed.cpp')]
with (H/'T170_THREE_COMPRESSED_BUILD.log').open('wb') as out:p=subprocess.run(args,env=env,cwd=H,stdout=out,stderr=subprocess.STDOUT,timeout=120,creationflags=subprocess.CREATE_NO_WINDOW|subprocess.BELOW_NORMAL_PRIORITY_CLASS)
assert p.returncode==0,'Read build log'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
r={'status':'Build PASS only; no mathematical audit','source_sha256':sha(H/'t170_three_compressed.cpp'),'exe_sha256':sha(H/'t170_three_compressed.exe'),'compiler_sha256':sha(cl),'args':args}
(H/'T170_THREE_COMPRESSED_BUILD_RECEIPT.json').write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8');print(json.dumps(r))
