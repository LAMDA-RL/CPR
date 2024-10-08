from UtilsRL.misc import NameSpace
import torch.nn as nn

seed = 0
task = None

discount = 0.99
tau = 0.005

actor_hidden_dims = [256, 256]
critic_hidden_dims = [256, 256]
actor_lr = 0.0003
critic_lr = 0.0003
batch_size = 256

actor_update_interval = 2
policy_noise = 0.2
noise_clip = 0.5
max_action = 1.0

max_epoch = 1000
step_per_epoch = 1000

eval_interval = 10
eval_episode = 10
save_interval = 50
log_interval = 10

actor_weight_decay = False
actor_dropout = False
actor_nomr_layer = False
actor_activation = nn.ReLU
actor_sn = False

critic_weight_decay = False
actor_dropout = False
actor_nomr_layer = False
critic_activation = nn.ReLU
critic_sn = False

group = "default"

name = "original"
class wandb(NameSpace):
    entity = None
    project = None

debug = False
