from pathlib import Path
import sys
sys.set_int_max_str_digits(100000)
exec((Path(__file__).parent/'check_potential.py').read_text().split('\nassertions=[]')[0],globals())
def correction(data,p):
    v=4*p*(1-p);m=1-2*p;out={};mass=Q(0)
    for T in range(64):
        z=sum((Q(w,64)*m**(Z.bit_count()-T.bit_count()) for Z,w in enumerate(data['walsh']) if Z&T==T),Q(0))
        value=v**T.bit_count()*z*z;mass+=value;out=add(out,hm(value));ck(abs(z)<=1)
    ck(mass==1)
    return add(out,h2expr(v),-ev(data['Q'],p))
seed=gates['h'];p=Q(5,32);I=Q(sum(s.bit_count()*w*w for s,w in enumerate(seed['walsh'])),64**2)
ck(I==Q(9,8));R=scale(entropy(seed['walsh']),1/I);rows=[]
for stage,chosen in enumerate([p,None,None]):
    if stage==0:a=p
    elif stage==1:a=1-p
    else:a=p
    C=correction(seed,a);Qt=ev(seed['Q'],a)
    R=add(R,C,1/(Qt*I));I*=Qt;p=ev(seed['prob'],a)
    rows.append({'core_stage':stage+1,'dimension':6**(stage+2),'negative_probability':str(p),'I':str(I),'H_over_I':bounds(R)})
ck(p<Q(1,16))
psi=scale(h2expr(p),1/I)
data=gates['J'];C=correction(data,p);Qt=ev(data['Q'],p);outp=ev(data['prob'],p)
D=add(scale(h2expr(p),Qt),h2expr(outp),Q(-1));outI=Qt*I
debit=scale(C,1/outI);drop=scale(D,1/outI)
ck(enclose(add(scale(drop,64),debit,Q(-1)))[0]>0)
ck(enclose(add(scale(drop,64),debit))[0]>0)
ck(Q(1,16)<outp<Q(1,4))
nextR=add(R,debit)
familyupper=add(R,psi,Q(64));ck(enclose(familyupper)[1]<12)
dump('EXISTING_HIGH_E_CORE_ONEFLIP_PAYMENT.json',{'source_core':'A080 existing core: g0=h; g1=h(g0^6); g2=h((-g1)^6); g3=h(g2^6).','core_states':rows,'core_minority':str(p),'core_I':str(I),'retained_core_H_over_I':bounds(R),'available_output_entropy_potential':bounds(psi),'remaining_all_word_budget_upper':bounds(scale(psi,64)),'all_admissible_mixed_descendants_H_over_I_upper':bounds(familyupper),'all_admissible_mixed_descendants_H_over_I_below_12':True,'oneflip_child_dimension':7776,'oneflip_output_negative_probability':str(outp),'oneflip_I':str(outI),'signed_H_over_I_debit':bounds(debit),'owned_potential_drop':bounds(drop),'payment_margin_positive_debit':bounds(add(scale(drop,64),debit,Q(-1))),'payment_margin_negative_debit':bounds(add(scale(drop,64),debit)),'child_H_over_I':bounds(nextR),'checks':ar.checks,'runtime_seconds':time.perf_counter()-started,'new_erasure_claim':False,'full_fei':'OPEN'})
print(json.dumps({'checks':ar.checks,'runtime_seconds':time.perf_counter()-started,'core_p':float(p),'child_p':float(outp),'debit':bounds(debit)['display'],'remaining_budget':bounds(scale(psi,64))['display']}))
