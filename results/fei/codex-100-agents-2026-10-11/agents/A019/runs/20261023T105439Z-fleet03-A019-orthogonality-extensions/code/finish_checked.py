from pathlib import Path
import runpy,sys
R=Path(__file__).resolve().parents[1]
def read(p):
 with p.open('r',encoding='utf-8',newline='') as f:return f.read()
def write(p,s):
 with p.open('w',encoding='utf-8',newline='') as f:f.write(s)
p=R/'code/check_obstruction.py';s=read(p)
if 'root_margin=' not in s:
 marker=' ck(c.positive(sub(bank,c.const(Q(3,4)))));ck(c.nonneg(bill))'
 assert marker in s
 s=s.replace(marker,marker+'\n if k==8:\n  root_margin=add((1,c.const(6+J/2-p/2)),(-1,cp))\n  ck(c.positive(add((1,root_margin),(-1,bank),(-1,c.const(Q(5,8))))))\n  ck(c.positive(add((1,c.const(4*(1-p+J/2))),(-1,corecost))))')
 write(p,s)
p=R/'out/DERIVATION.md';s=read(p);start=s.index('This is not a disproof of FEI.')
s=s[:start]+'''This is not a disproof of FEI. Indeed H1/I(h1) tends to (4/3)H0<4;
the analogous full-root H/I limit is the same. The later physical influences
are nonzero, but that does not establish an unused credit: B already contains
J/2 from original influence. NEXT must audit allocation between B, its full
terminal obligations and any proposed query credit. Use only a VERIFIED
unallocated original owner, or change the stopping potential. Simply adding
4Inf_v to B could double count the same source. Every old debit, signed
reserve and full inherited terminal must remain. This ownership audit and
compatible cumulative potential are the first unpaid universal line. FEI OPEN.
''';write(p,s)
p=R/'code/finalize_stage.py';s=read(p)
replacements={
 'Allocate the still-unused original event-coordinate influence to the explicit G_m tensor exposure, retaining B,U,Tq and all complete inherited leaves; prove a cumulative signed-reference invariant rather than renew source or leave all later influence unspent.':'Audit ORIGINAL event-influence allocation between B and terminal obligations on the tensor; use only a VERIFIED unallocated owner for query credits, or change the stopping potential. Retain U,Tq and all full inherited leaves; never credit already-allocated influence twice.',
 'Pay relevant subsequent queries from their actual unused original influence stock without renewing a bank or dropping the old debit/full terminals.':'First identify a VERIFIED unused owner after J/2 already allocated in B; price queries or change the potential without double counting, renewing a bank, or dropping old debits/full terminals.',
 'The new physical event-coordinate influence is real and remains available for the next mechanism; it cannot be replaced by a renewed bank.':'The physical event-coordinate influence is nonzero, but no additional unallocated credit is certified: B already contains J/2. The next audit must reconcile that allocation with terminal obligations; adding query credits without this audit could double count.',
 'The first unpaid universal line is this cumulative original-influence allocation on the explicit tensor example':'The first unpaid universal line is this allocation audit and a compatible cumulative stopping potential on the tensor',
 'The remaining bridge is a conserved allocation of the ORIGINAL unused event influence under inherited references.':'The remaining bridge is an allocation audit under inherited references: determine whether any ORIGINAL event influence is unallocated after B and all terminal obligations; change the potential if none is.',
 'NEXT: Allocate actual UNUSED original event influence on tensor after old U/full Tq, with all inherited full terminals; A018/A020 review two new scoped claims.':'NEXT: Audit tensor source ownership: B contains J/2; certify any unused owner or change potential, old U/full Tq and all full inherited terminals retained; A018/A020 review.',
 'NEXT: actual unused event-influence allocation.':'NEXT: audit ownership before additional credit (B contains J/2).',
 'NEXT must use actual original event influence, not renew source.':'NEXT must audit whether any original influence is unallocated after B (which contains J/2) and all terminal obligations; no new credit is certified.',
 'Universal same-reference cumulative influence allocation remains open.':'Universal same-reference influence OWNERSHIP and cumulative potential remain open.'
}
for a,b in replacements.items():s=s.replace(a,b)
write(p,s)
sys.argv=[str(R/'code/check_obstruction.py')]
runpy.run_path(sys.argv[0],run_name='__main__')
sys.argv=[str(p)]
runpy.run_path(str(p),run_name='__main__')
