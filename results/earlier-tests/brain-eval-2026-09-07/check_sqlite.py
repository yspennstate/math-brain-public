"""Independent reconstruction lane: keyed SQL aggregation from pinned raw JSON.

This deliberately imports no grader or protocol-report implementation. It checks
the observed vocabulary before using exact string scoring. Unknowns stop it.
"""
import argparse
import json
from pathlib import Path
import sqlite3
from fractions import Fraction


def main():
    p=argparse.ArgumentParser(); p.add_argument('--snapshot',type=Path,required=True); p.add_argument('--result',type=Path,required=True)
    a=p.parse_args(); reference=json.loads(a.result.read_text(encoding='utf-8'))
    db=sqlite3.connect(':memory:')
    db.execute('create table answer_key(id text primary key, truth text, tier text, step integer)')
    for line in (a.snapshot/'plit_keys.jsonl').read_text(encoding='utf-8').splitlines():
        row=json.loads(line)
        db.execute('insert into answer_key values(?,?,?,?)',(row['item_id'],row['truth'],row.get('tier'),row.get('fault_step')))
    db.execute('create table answers(solver text, arm text, id text, verdict text, step integer, primary key(solver,arm,id))')
    for solver in ('haiku','opus'):
        for path in (a.snapshot/('run_plit_s1_'+solver)/'verdicts').rglob('*.json'):
            row=json.loads(path.read_text(encoding='utf-8')); answer=row['answer']
            if answer['verdict'] not in ('valid','flawed'):
                raise ValueError('SQL lane needs an explicit additional vocabulary mapping')
            db.execute('insert into answers values(?,?,?,?,?)',(solver,row['arm'],row['item_id'],answer['verdict'],answer['fault_step']))
    findings=[]
    for solver,tier in (('haiku','A'),('opus','B')):
        actual=[]
        for arm in ('brain','none','placebo'):
            n,correct=db.execute('select count(*),sum(a.verdict="flawed" and a.step=k.step) from answers a join answer_key k on a.id=k.id where a.solver=? and a.arm=? and k.truth="flawed" and k.tier=?',(solver,arm,tier)).fetchone()
            actual.append((n,correct))
        expected=reference['solvers'][solver]['primary']
        for idx,other in enumerate((1,2)):
            c=expected[idx]
            assert c['n']==actual[0][0]==actual[other][0]
            assert c['correct']==[actual[0][1],actual[other][1]]
            assert c['comparator_errors_available_for_gain']==actual[other][0]-actual[other][1]
            assert c['comparator_correct_available_for_harm']==actual[other][1]
            assert c['conditional_effect_range_pp']==[-100*actual[other][1]/actual[other][0],100*(actual[other][0]-actual[other][1])/actual[other][0]]
            rows=db.execute('select (a.verdict="flawed" and a.step=k.step)-(b.verdict="flawed" and b.step=k.step) from answers a join answers b on a.id=b.id and a.solver=b.solver join answer_key k on a.id=k.id where a.solver=? and a.arm="brain" and b.arm=? and k.truth="flawed" and k.tier=?',(solver,('none','placebo')[idx],tier)).fetchall()
            delta=[x[0] or 0 for x in rows]
            counts=[delta.count(1),delta.count(-1)]
            assert c['discordants']==counts
            # Binomial recurrence in exact rational arithmetic, distinct from comb sums.
            n_dis=sum(counts); term=Fraction(1,2**n_dis); tail=term
            for k in range(1,min(counts)+1):
                term*=Fraction(n_dis-k+1,k); tail+=term
            probability=float(min(Fraction(1),2*tail))
            assert c['mcnemar_exact_two_sided_p']==probability
        findings.append({'solver':solver,'tier':tier,'brain_none_placebo':actual,'primary_disagreements':0})
    print(json.dumps({'sql_rows':db.execute('select count(*) from answers').fetchone()[0],'checks':findings},indent=2))


if __name__=='__main__':
    main()
