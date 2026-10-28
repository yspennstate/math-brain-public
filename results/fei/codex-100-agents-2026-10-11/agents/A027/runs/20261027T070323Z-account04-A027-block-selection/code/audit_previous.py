from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parents[1]
OLD=R.parent/'20261023T141418Z-account03-A027-block-selection'/'code'
dest=R/'code'/'previous_audit';dest.mkdir(exist_ok=True)
for n in ['base.py','exact.py']:(dest/n).write_bytes((OLD/n).read_bytes())
s=(OLD/'check.py').read_text(encoding='utf-8')
s=s.replace("receipts=[]", "receipts=[]; BILLS=[]")
s=s.replace("eta_release=Q(0)\n    def walk", "eta_release=Q(0); qloss={}; rawtotal=root[2]\n    def walk")
s=s.replace("nonlocal release,terminal,Dleaves,eta_release", "nonlocal release,terminal,Dleaves,eta_release,qloss,rawtotal")
s=s.replace("NODE+=1", "qloss=add((1,qloss),(w,refund)); rawtotal=add((1,rawtotal),(w,raw)); NODE+=1")
s=s.replace("POL+=1", "ck(rawtotal==add((1,Dleaves),(1,qloss)),'NEW actual FULL raw transaction telescope including query loss');\n    actualslack=add((1,b.Bs[1]),(Q(-1,4),rawtotal)); envelopegap=add((1,root[3]),(-1,rawtotal));\n    BILLS.append({'theta':str(theta),'mode':mode,'policy':policy,'qloss':enc(qloss),'rawtotal':enc(rawtotal),'original_slack':enc(actualslack),'envelope_slack':enc(envelopegap),'original_paid':x.bounds(actualslack)[0]>=0,'envelope_paid':x.bounds(envelopegap)[0]>=0}); POL+=1")
s=s.replace("out={'status':'PASS'", "(R/'out/PHYSICAL_BILLS.json').write_text(json.dumps(BILLS,indent=2),encoding='utf-8');\nout={'status':'PASS'")
# Generated checker lives two levels deeper: bind all helper outputs to the NEW run.
for n in ['base.py','exact.py']:
    p=dest/n; z=p.read_text(encoding='utf-8').replace('parents[1]','parents[2]');p.write_text(z,encoding='utf-8')
s=s.replace('parents[1]','parents[2]')
(dest/'check.py').write_text(s,encoding='utf-8')
print(json.dumps({'generated_checker_sha256':hashlib.sha256(s.encode()).hexdigest(),'domain':'same 300 previous labelled policies; new full physical bill checks only; no independent reproduction claim'}))
