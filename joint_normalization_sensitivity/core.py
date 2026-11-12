from .common import number,unique_ids,identifier
def run(data):
 joints=data['joints'];eps=number(data.get('epsilon',1e-8),0,1);floor=number(data['counterfactual_minimum_std'],1e-12,1e6);identifier(data['unit'])
 if not isinstance(joints,list)or len(joints)>1000:raise ValueError('joints')
 unique_ids(joints);out=[]
 for j in joints:
  mean=number(j['mean'],-1e9,1e9);std=number(j['std'],0,1e9);value=number(j['live_value'],-1e9,1e9);denom=std+eps
  if denom<=0:raise ValueError('zero_denominator')
  original=(value-mean)/denom;counter=(value-mean)/(max(std,floor)+eps)
  out.append({'id':j['id'],'normalized':original,'counterfactual_normalized':counter,'floor_would_change_training_transform':std<floor,'unit':data['unit']})
 return {'joints':out,'policy_changed':False,'safe_robot_motion_proven':False}
