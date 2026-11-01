import json,time,math
from pathlib import Path
import check as c
R=Path(__file__).resolve().parent.parent
rows=[]
for r in [3,5,9]:
    f=[-1 if (z&3)==0 else 1 for z in range(1<<r)]
    s=c.info(f,True)
    c.check(s['H']=={2:c.Q(2)})
    c.check(s['I']==1)
    alpha=c.Q(sum(v*v for label,v in enumerate(s['a']) if label),1<<(2*r))
    c.check(alpha==c.Q(3,4))
    c.check(c.physical(f,range(2,r))==0)
    rows.append({'r':r,'fiber_count':1<<(r-2),'H_bits_exact':2,'I_exact':1,'alpha':'3/4',
                 'crude_flag_alphabet_bound':'h2(3/4)+(3/4)*r','theorem_control_coefficient':'2*r+2/ln2',
                 'relevant_controls':[0,1]})
rejected=[]
for r in [3,4]:
    for j in [2,3]:
        g=[-1]+[1]*7;fs=c.presets(3,r,j);leaves=[]
        for z in range(1<<r):
            f=[g[x]*(-1 if z in fs[x] else 1) for x in range(8)]
            s=c.leaf(f)
            if s['U']>s['I']:
                leaves.append({'z':z,'truth_values':f,'U':s['U'],'I':s['I'],'H_prime_log_map':s['H']})
        c.check(bool(leaves))
        rejected.append({'family':'pointdefect','r':r,'preset':j,'fibers':fs,'rejected_actual_leaves':leaves})
epsilon=c.Q(math.comb(16,8),1<<16)
mask_core_influence=c.Q(1,4)*2*16*epsilon
c.check(16*c.Q(1,4)**2==1)
c.check(c.Q(16-2*8,4)==0)
c.check(mask_core_influence==c.Q(6435,4096)>1)
c.check(c.Q(16,4) not in [-1,1])
c.check(16==1<<4)
real_guard={'seed':'psi=(1/4)sum_{i=1}^{16} x_i; normalized real, not Boolean',
            'spectral_energy_core':1,'spectral_entropy_bits':4,'core_edit_support':'Hamming layer weight 8',
            'controls':'r2, z00 only','maximum_fiber_size':1,'fiber_cap':'1/4',
            'support_density':epsilon,'F_equals_psi':'every edited seed value is zero',
            'mask_core_influence':mask_core_influence,'ownership_failure':'1 < 6435/4096'}
out={'complete':True,'cases':8,'assertions':c.ASSERTIONS,'elapsed_seconds':time.perf_counter()-c.START,
     'flag_bound_dimension_loss':rows,'U_admission_rejections':rejected,'non_Boolean_ownership_guard':real_guard}
(R/'out/DIAGNOSTIC.json').write_text(json.dumps(c.enc(out),indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k not in ['flag_bound_dimension_loss','U_admission_rejections','non_Boolean_ownership_guard']}))
