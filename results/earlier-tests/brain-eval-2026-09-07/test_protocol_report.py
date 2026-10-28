from pathlib import Path
from tempfile import TemporaryDirectory
import hashlib
import itertools
import json
import unittest

from protocol_report import EvidenceError, contrast, normalize_verdict, read_json, read_keys, read_trial, verify_manifest


class ReportTests(unittest.TestCase):
    def test_ceiling_and_floor_have_asymmetric_effect_room(self):
        ids=['a','b','c','d']
        rows={'brain':{i:{'full_credit':True} for i in ids},'none':{i:{'full_credit':True} for i in ids}}
        result=contrast(rows,ids,'brain','none')
        self.assertEqual(result['conditional_effect_range_pp'],[-100,0])
        self.assertEqual(result['comparator_errors_available_for_gain'],0)
        for i in ids:rows['none'][i]['full_credit']=False
        result=contrast(rows,ids,'brain','none')
        self.assertEqual(result['conditional_effect_range_pp'],[0,100])
        self.assertEqual(result['comparator_correct_available_for_harm'],0)
    def setUp(self):
        self.tmp=TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root=Path(self.tmp.name)
        self.keys={'x':{'truth':'flawed','tier':'A','fault_step':2}, 'y':{'truth':'clean'}}
        self.put('SAMPLE.json',{'item_ids':['x','y'],'requested':2,'n_faulted':1,'n_clean':1})
        for arm in ('none','brain','placebo'):
            for iid in ('x','y'):
                self.put(f'verdicts/{arm}/{iid}.json',{'item_id':iid,'arm':arm,'answer':
                    {'verdict':'flawed' if iid=='x' else 'valid','fault_step':2 if iid=='x' else None}})

    def put(self,relative,data):
        p=self.root/relative; p.parent.mkdir(parents=True,exist_ok=True)
        p.write_text(json.dumps(data),encoding='utf-8'); return p

    def test_complete_population(self):
        sample, rows=read_trial(self.root,self.keys)
        self.assertEqual(len(sample['item_ids']),2)
        self.assertTrue(rows['brain']['x']['full_credit'])
        self.assertFalse(rows['brain']['y']['detected'])

    def test_missing_row_does_not_shrink_population(self):
        (self.root/'verdicts/brain/x.json').unlink()
        with self.assertRaisesRegex(EvidenceError,'Incomplete brain: 1/2'):
            read_trial(self.root,self.keys)

    def test_wrong_arm(self):
        self.put('verdicts/brain/x.json',{'item_id':'x','arm':'none','answer':{'verdict':'flawed','fault_step':2}})
        with self.assertRaisesRegex(EvidenceError,'arm mismatch'):
            read_trial(self.root,self.keys)

    def test_filename_identity(self):
        (self.root/'verdicts/brain/x.json').rename(self.root/'verdicts/brain/renamed.json')
        with self.assertRaisesRegex(EvidenceError,'identity'):
            read_trial(self.root,self.keys)

    def test_duplicate_sample(self):
        self.put('SAMPLE.json',{'item_ids':['x','x']})
        with self.assertRaisesRegex(EvidenceError,'duplicate sample'):
            read_trial(self.root,self.keys)

    def test_unknown_verdict(self):
        self.put('verdicts/brain/x.json',{'item_id':'x','arm':'brain','answer':{'verdict':'timeout','fault_step':None}})
        with self.assertRaisesRegex(EvidenceError,'Unrecognized'):
            read_trial(self.root,self.keys)

    def test_ambiguous_prefixes_are_not_verdicts(self):
        for value in ('valid-ish','validity unknown','flawed? uncertain','flawless','invalid?'):
            with self.subTest(value=value):
                with self.assertRaisesRegex(EvidenceError,'Unrecognized'):
                    normalize_verdict(value)

    def test_closed_verdict_aliases(self):
        for value in ('valid','clean','correct','sound','true',' VALID '):
            self.assertEqual(normalize_verdict(value),'clean')
        for value in ('flawed','invalid','incorrect','false',' FLAWED '):
            self.assertEqual(normalize_verdict(value),'flawed')

    def test_boolean_step_not_integer(self):
        self.put('verdicts/brain/x.json',{'item_id':'x','arm':'brain','answer':{'verdict':'flawed','fault_step':True}})
        with self.assertRaisesRegex(EvidenceError,'positive integer'):
            read_trial(self.root,self.keys)

    def test_missing_key(self):
        with self.assertRaisesRegex(EvidenceError,'missing answer keys'):
            read_trial(self.root,{'y':self.keys['y']})

    def test_malformed_json(self):
        (self.root/'verdicts/brain/x.json').write_text('{',encoding='utf-8')
        with self.assertRaises(EvidenceError):
            read_trial(self.root,self.keys)

    def test_duplicate_json_member(self):
        p=self.root/'duplicate.json'; p.write_text('{"count": 1, "count": 2}',encoding='utf-8')
        with self.assertRaisesRegex(EvidenceError,'Duplicate JSON'):
            read_json(p)

    def test_unsupported_sample_composition(self):
        self.put('SAMPLE.json',{'item_ids':['x','y'],'n_faulted':2})
        with self.assertRaisesRegex(EvidenceError,'composition'):
            read_trial(self.root,self.keys)

    def test_duplicates_in_keys(self):
        p=self.root/'keys.jsonl'; row=json.dumps({'item_id':'x',**self.keys['x']})
        p.write_text(row+'\n'+row+'\n',encoding='utf-8')
        with self.assertRaisesRegex(EvidenceError,'Duplicate key'):
            read_keys(p)

    def test_duplicate_key_member_cannot_overwrite_truth(self):
        p=self.root/'keys.jsonl'
        p.write_text('{"item_id":"x","truth":"flawed","truth":"clean","tier":"A","fault_step":2}\n',encoding='utf-8')
        with self.assertRaisesRegex(EvidenceError,'Duplicate JSON member: truth'):
            read_keys(p)

    def test_nonfinite_json_refuses(self):
        for value in ('NaN','Infinity','-Infinity'):
            with self.subTest(value=value):
                p=self.root/'not_json.json'; p.write_text('{"value":'+value+'}',encoding='utf-8')
                with self.assertRaisesRegex(EvidenceError,'Nonfinite'):
                    read_json(p)

    def test_descriptive_does_not_emit_p_value(self):
        rows={'brain':{'x':{'full_credit':True}},'none':{'x':{'full_credit':False}}}
        r=contrast(rows,['x'],'brain','none',inference=False)
        self.assertEqual(r['difference_pp'],100)
        self.assertNotIn('mcnemar_exact_two_sided_p',r)

    def test_exact_sign_test_by_exhaustive_null_assignments(self):
        # Independent route: enumerate equiprobable signs, no binomial formula.
        for plus in range(5):
            for minus in range(5):
                n=plus+minus
                if not n:
                    continue
                signs=[1]*plus+[-1]*minus
                rows={'brain':{i:{'full_credit':s==1} for i,s in enumerate(signs)},
                      'none':{i:{'full_credit':s==-1} for i,s in enumerate(signs)}}
                got=contrast(rows,list(range(n)),'brain','none')['mcnemar_exact_two_sided_p']
                outcomes=list(itertools.product((-1,1),repeat=n))
                expected=sum(abs(sum(x))>=abs(plus-minus) for x in outcomes)/len(outcomes)
                self.assertAlmostEqual(got,expected)

    def test_empty_comparison_refuses(self):
        with self.assertRaisesRegex(EvidenceError,'empty population'):
            contrast({'brain':{},'none':{}},[],'brain','none')

    def test_manifest_mutation_and_missing_member(self):
        files=[p for p in self.root.rglob('*') if p.is_file()]
        rows=[{'evidence':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in files]
        self.put('MANIFEST.json',rows)
        verify_manifest(self.root)
        self.put('unlisted.json',{'x':1})
        with self.assertRaisesRegex(EvidenceError,'inventory'):
            verify_manifest(self.root)
        (self.root/'unlisted.json').unlink()
        self.put('SAMPLE.json',{'tampered':True})
        with self.assertRaisesRegex(EvidenceError,'drift'):
            verify_manifest(self.root)


if __name__=='__main__':
    unittest.main()
