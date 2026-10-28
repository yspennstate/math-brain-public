from pathlib import Path
import re,json,hashlib
R=Path(__file__).resolve().parents[1]
def read(p):return p.read_bytes().decode('utf-8')
def write(p,s):p.write_bytes(s.encode('utf-8'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
for name in ['PILOT.json','VALIDATION.json','SPEC_RECEIPT.json']:
 p=R/'out'/name
 assert p.exists(),name
 write(R/'out'/('V1_'+name),read(p))
for name in ['DERIVATION.md','FROZEN_SPEC.md','code/check.py','code/finish.py']:
 p=R/name;s=read(p)
 # Simultaneous replacement affects constants, not digit strings in dates.
 s=re.sub(r'(?<!\d)(14|20|17|23)(?!\d)',lambda m:{'14':'10','20':'16','17':'13','23':'19'}[m[0]],s)
 s=s.replace('stage16','stage20')
 write(p,s)
p=R/'DERIVATION.md';s=read(p)
anchor='## 2. Quadratic phase with two possibly overlapping flat edits'
assert s.count(anchor)==1
extra='''### Sharper affine half-spectrum price

The norm-seven estimate alone gives14d, but the actual half-spectrum in (8) gives10d. For a physical direction e_i and nonempty flat A with direction space V_A, its Fourier support is W_A=V_A^perp. If e_i is not in V_A (a transverse query), exactly half of W_A has i in its label; therefore each half of the flat-indicator spectrum has l1 mass1/2. If e_i is in V_A (a tangent query), all support excludes i. Multiplication by the affine character of q translates these supports: a tangent flat contributes half-mass1 when q excludes i, and0 when q contains i; a transverse flat still contributes1/2. Empty flats contribute0.

If both A and B are tangent, their union is invariant under i. The actual f is then either independent of i or changes sign identically along i, so each Fourier fiber has at most one nonzero coefficient and B_i=0. Otherwise at least one flat is transverse, and their nonempty intersection is also transverse. When q excludes i, the half-spectrum triangle bound is at most1+2(1/2)+2(1)+2(1/2)=5, including its character term. When q contains i, the character term and tangent-flat terms contribute0, so the bound is at most3. Equation (8) thus proves B_i<=10d for EVERY coordinate of an affine phase with a two-flat union edit. These are bounds on the same actual half-spectrum, not separately spent banks. In the degree-three pivot cases below the bounds were already<=10d, so the hereditary class improves toK10.

'''
s=s.replace(anchor,extra+anchor)
s=s.replace('If q is affine, apply (8) and norm seven.','If q is affine, apply the sharper affine half-spectrum price above.')
anchor='## 4. Exact first unsupported line'
extra='''### Credit needed for changed inner means

The inherited remainder bound explicitly asks for at most6*d_F units of credit per ACTUAL lifted query. Over any physical prefix its accumulated positive remainders are at most6*I_spent_prefix. The influence identity leaves the exact unspent source potential6*sum_l p_l I(f_l) from an ORIGINAL reserve6*I(f_root), provided this reserve was earmarked and each earlier debit was booked against it. This specifies a sufficient influence-priced credit with both full terminals retained; it does not establish that a previously diminished threshold10 bank possesses that reserve. Any old debit U must still be subtracted; a new reserve cannot be installed retrospectively. Thus the inner two-flat K10 repair closes, while changing its inner-output means in actual OR composition still needs this same-account6*d_F payment to retain threshold10. Threshold16 avoids additional bad-node debit without claiming payment of old threshold10 liabilities.

'''
assert s.count(anchor)==1;s=s.replace(anchor,extra+anchor);write(p,s)
p=R/'FROZEN_SPEC.md';write(p,read(p)+'\nVersion2 freezes the sharper actual half-spectrum proof before rerun. V1 pilot/full/spec receipts are preserved in out/V1_*.json. Revised checker tests K10; pilot/full domains, count, arithmetic and caps unchanged.\n')
p=R/'code/check.py';s=read(p)
anchor="d,norm=audit(v,i)\n"
assert s.count(anchor)==1
s=s.replace(anchor,anchor+"  if branch=='affine' and d:\n   ws=fwht(v);le(Q(sum(abs(ws[t]) for t in range(len(v)) if not t>>i&1),len(v)),5)\n")
write(p,s)
out=dict(checker_sha256=sha(R/'code/check.py'),spec_sha256=sha(R/'FROZEN_SPEC.md'),frozen_before_execution=True,version=2)
write(R/'out/SPEC_RECEIPT.json',json.dumps(out,indent=2))
write(R/'out/AUDIT_SPEC_RECEIPT.json',json.dumps(dict(checker_sha256=sha(R/'code/audit.py'),spec_sha256=sha(R/'AUDIT_SPEC.md'),frozen_before_execution=True),indent=2))
print(json.dumps(out))
