import unittest,copy,json
from joint_normalization_sensitivity import run
DEMO={'unit': 'degrees', 'counterfactual_minimum_std': 1, 'joints': [{'id': 'idle', 'mean': 0, 'std': 1.48e-06, 'live_value': 0.2}]}
class DomainTests(unittest.TestCase):
 def test_tiny_spread_amplifies_small_motion(self):
  x=run(DEMO)['joints'][0];self.assertGreater(x['normalized'],100000);self.assertLess(x['counterfactual_normalized'],.21)
 def test_floor_is_counterfactual_not_policy_patch(self):
  x=run(DEMO);self.assertFalse(x['policy_changed']);self.assertFalse(x['safe_robot_motion_proven'])
 def test_zero_denominator(self):
  x=copy.deepcopy(DEMO);x['epsilon']=0;x['joints'][0]['std']=0
  with self.assertRaises(ValueError):run(x)
