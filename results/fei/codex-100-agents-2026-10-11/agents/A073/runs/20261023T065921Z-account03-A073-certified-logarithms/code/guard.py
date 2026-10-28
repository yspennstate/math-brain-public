from pathlib import Path
from fractions import Fraction as F
import importlib.util,json,hashlib,time
R=Path(__file__).resolve().parents[1];O=R/'out'
sp=importlib.util.spec_from_file_location('own_activation_helpers',R/'code/check.py');c=importlib.util.module_from_spec(sp);sp.loader.exec_module(c)
spec={'family':'actual width3 point core activation after b1/a0; no intervening physical query; old full alpha1/7 vs fresh alpha1/2','case_count':1,'symmetry':'none','arithmetic':'Fraction Boolean spectrum/coherent channel, exact integer product plus fixed16-term certified log interval','memory_MB':35,'max_runtime_seconds':55,'helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
c.save('GUARD_FROZEN.json',spec);start=time.monotonic()
root,blocks,_,_=c.b.make((3,));n=root.child(2,1).child(1,0)
old=c.lift(n,c.coreq(blocks,{},F(1,7)));new=c.lift(n,c.coreq(blocks,{},F(1,2)))
assert old.p==new.p and old.I==new.I
lo,hi=c.diff(n.p,new.q,old.q);assert lo>F(1,16)
ratio=F(1)
for s,p in n.p.items():ratio*=(old.q[s]/new.q[s])**int(64*p)
N=12**6*13;D=7**6*28
assert ratio==F(N,D)**2 and N>4*D
c.save('INCREASING_ALPHA_GUARD.json',{'status':'PASS_ADVERSARIAL_GUARD','source_unchanged':True,'old_alpha':'1/7','new_alpha':'1/2','price_bits':'(1/32)log2(N/D)','N':N,'D':D,'certified_positive_margin':'price > 1/16 bits','integer_comparison':'N>4D','integer_margin':N-4*D,'price_interval':[lo,hi],'old_complete_reference':old.q,'new_complete_reference':new.q,'actual_spectrum':n.p,'runtime_seconds':time.monotonic()-start,'scope':'Excluded increasing-profile reset, not a refutation of the fixed-alpha theorem or FEI. No physical query/phase release occurs at this conversion.'})
addition='\nAdversarial sign guard: code/guard.py uses the SAME actual width3 activation source with no intervening query, but increases alpha from1/7 to1/2. The complete conversion is POSITIVE >1/16 bit, exactly(1/32)log2(N/D), N=12^6*13,D=7^6*28,N>4D. out/INCREASING_ALPHA_GUARD.json records the full source/reference laws. Thus the sign gate can fail on a genuinely changed profile; the fixed/decreasing-alpha hypothesis is essential, and source phase release alone does not price arbitrary reference edits.\n'
report=(R/'REPORT.md').read_text(encoding='utf-8');report=report.replace('## proof dependencies and changed downstream conclusions',addition+'\n## proof dependencies and changed downstream conclusions');(R/'REPORT.md').write_text(report,encoding='utf-8')
proof=(R/'PROOF.md').read_text(encoding='utf-8');proof=proof.replace('First unsupported universal line:',addition+'\nFirst unsupported universal line:');(R/'PROOF.md').write_text(proof,encoding='utf-8')
claims=json.loads((R/'CLAIMS.json').read_text(encoding='utf-8'));claims[0]['proof_source']+=['code/guard.py','out/INCREASING_ALPHA_GUARD.json'];c.save('GUARD_RECEIPT.json',{'status':'saved','proof_statement_unchanged':True})
(R/'CLAIMS.json').write_text(json.dumps(claims,indent=2)+'\n',encoding='utf-8')
manifest={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(R.rglob('*')) if p.is_file() and p.name!='MANIFEST.json'};c.save('MANIFEST.json',manifest)
with (R.parents[1]/'LEARNED.md').open('a',encoding='utf-8') as f:f.write('\n2026-10-23 guard: at an actual width3 activation with source fixed and no query, increasing full spike alpha1/7 to1/2 costs(1/32)log2(12^6*13/(7^6*28))>1/16 bit because numerator>4*denominator. Fixed-alpha refresh theorem is not a free arbitrary-profile edit; any extension must retain the increasing-shape price.\n')
print(json.dumps({'guard':'PASS','positive_price':'>1/16 bits','integer_margin':N-4*D,'runtime_seconds':time.monotonic()-start}))
