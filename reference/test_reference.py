import unittest
from domamutzer_reference import PolicyConfig,reciprocal_policy_score,trust_region_blend,windowed_rerank

class Tests(unittest.TestCase):
    def test_zero_gate_is_incumbent(self):
        s,d=trust_region_blend(.7,.1,0,.8)
        self.assertAlmostEqual(s,.7,12); self.assertEqual(d,0)
    def test_bounded_move(self):
        s,d=trust_region_blend(.5,.999,1,.4)
        self.assertLessEqual(abs(d),.40000001); self.assertGreater(s,.5)
    def test_policy(self):
        sup={'profile_confidence':.95,'shared_evidence':.8,'coverage_balance':.9}
        out=reciprocal_policy_score(incumbent_score=.5,p_ab=.9,p_ba=.8,forward_support=sup,reverse_support=sup,cfg=PolicyConfig(max_logit_shift=.6))
        self.assertGreater(out['score'],.5); self.assertLessEqual(abs(out['applied_logit_delta']),.6000001)
    def test_windows(self):
        rows=[{'id':str(i),'incumbent_score':1-i*.01,'score':i/20} for i in range(20)]
        out=windowed_rerank(rows,5); pos={r['id']:i for i,r in enumerate(out)}
        for i in range(20): self.assertEqual(i//5,pos[str(i)]//5)

if __name__=='__main__': unittest.main()
