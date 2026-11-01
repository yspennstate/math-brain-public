"""Synthetic transport controls only; these fixtures are never corpus items."""
import copy,json,tempfile,unittest
from pathlib import Path
import export_reviewed_calibration as e

def fixture():
    data={name:[] for name in ['items','keys','sources','splits','pairs']};judgments=[]
    for group in range(3):
        ids=[]
        for truth in ['clean','flawed']:
            identifier=f'synthetic-{group}-{truth}';ids.append(identifier)
            item=dict(schema='proof-bank-item/v1',item_id=identifier,bank_version='synthetic-control',claim='Synthetic parsing control.',argument_steps=[dict(n=1,text='original' if truth=='clean' else 'changed')],prompt='Synthetic fixture, not mathematics.')
            key=dict(item_id=identifier,truth=truth,fault_step=None if truth=='clean' else 1)
            source=dict(item_id=identifier,item_sha256=e.digest(item),key_sha256=e.digest(key),claim=item['claim'],original_steps=['original'],normalization_disclosure='Synthetic control only.',proof_group=f'p{group}',paper_id=f'family{group}')
            data['items'].append(item);data['keys'].append(key);data['sources'].append(source);data['splits'].append(dict(item_id=identifier,split='calibration'))
            judgments.append(dict(item_id=identifier,accepted_truth=truth,fault_step=key['fault_step']))
        data['pairs'].append(dict(proof_group=f'p{group}',paper_family=f'family{group}',item_ids=ids,split='calibration'))
    review=dict(schema='independent-calibration-semantic-review/v1',reviewer='synthetic-independent',decision='ACCEPT_SIX_FOR_PRIVATE_CALIBRATION_ONLY',items=judgments,counts=dict(items=6,distinct_source_proofs=3,paper_families=3))
    return data,review

def bind(data,review):
    blobs={k+'.jsonl':(''.join(json.dumps(r)+'\n' for r in rows)).encode() for k,rows in data.items()}
    review['input_files']={k:e.sha(v) for k,v in blobs.items()}
    return blobs

class Controls(unittest.TestCase):
    def setUp(self):self.data,self.review=fixture()
    def run_check(self):return e.validate_packet(bind(self.data,self.review),self.review,'synthetic-author')
    def reject(self):
        with self.assertRaises((ValueError,KeyError,TypeError)):self.run_check()
    def test_valid_packet(self):self.assertEqual(self.run_check()[1]['accepted_forms'],6)
    def test_duplicate_json_member(self):
        with self.assertRaises(ValueError):e.parse('{"x":1,"x":2}')
    def test_nonfinite(self):
        with self.assertRaises(ValueError):e.parse('{"x":NaN}')
    def test_drift(self):
        blobs=bind(self.data,self.review);blobs['items.jsonl']+=b' '
        with self.assertRaises(ValueError):e.validate_packet(blobs,self.review,'synthetic-author')
    def test_same_reviewer(self):self.review['reviewer']='synthetic-author';self.reject()
    def test_nonacceptance(self):self.review['decision']='PENDING';self.reject()
    def test_missing_review(self):self.review['items'].pop();self.reject()
    def test_duplicate_review(self):self.review['items'].append(copy.deepcopy(self.review['items'][0]));self.reject()
    def test_duplicate_item(self):self.data['items'].append(copy.deepcopy(self.data['items'][0]));self.reject()
    def test_extra_solver_field(self):self.data['items'][0]['truth']='clean';self.reject()
    def test_boolean_fault(self):self.review['items'][1]['fault_step']=True;self.reject()
    def test_wrong_verdict(self):self.review['items'][0]['accepted_truth']='flawed';self.reject()
    def test_missing_disclosure(self):self.data['sources'][0]['normalization_disclosure']='';self.reject()
    def test_wrong_source_hash(self):self.data['sources'][0]['item_sha256']='0'*64;self.reject()
    def test_changed_claim(self):self.data['sources'][0]['claim']='different';self.reject()
    def test_heldout(self):self.data['splits'][0]['split']='heldout';self.reject()
    def test_missing_pair(self):self.data['pairs'].pop();self.reject()
    def test_pair_reuse(self):self.data['pairs'][1]['item_ids']=self.data['pairs'][0]['item_ids'];self.reject()
    def test_wrong_group(self):self.data['pairs'][0]['proof_group']='wrong';self.reject()
    def test_wrong_counts(self):self.review['counts']['paper_families']=1;self.reject()
    def test_alternate_count_names(self):
        self.review['counts']['forms']=self.review['counts'].pop('items')
        self.review['counts']['source_proofs']=self.review['counts'].pop('distinct_source_proofs')
        self.assertEqual(self.run_check()[1]['accepted_forms'],6)
    def test_conflicting_count_aliases(self):self.review['counts']['forms']=8;self.reject()
    def test_solver_export_hides_original_ids_and_labels(self):
        values,summary=self.run_check()
        with tempfile.TemporaryDirectory() as folder:
            root=Path(folder);out=root/'export'
            receipt=e.write_private(values,summary,self.review,root/'review.json','f'*64,out,root)
            solver=(out/'solver_input'/'items.jsonl').read_text(encoding='utf-8')
            self.assertNotIn('synthetic-0-clean',solver)
            self.assertNotIn('"truth"',solver)
            self.assertNotIn('fault_step',solver)
            self.assertEqual(len(e.records(solver.encode())),6)
            self.assertEqual(receipt['published_source_soundness'],'NOT_CERTIFIED_BY_THIS_EXPORTER')
    def test_private_root_boundary(self):
        values,summary=self.run_check()
        with tempfile.TemporaryDirectory() as folder:
            root=Path(folder)
            with self.assertRaises(ValueError):e.write_private(values,summary,self.review,root/'r','f'*64,root/'outside',root/'private')

if __name__=='__main__':unittest.main()
