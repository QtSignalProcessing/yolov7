import argparse

import yaml

from wandb_utils import WandbLogger

WANDB_ARTIFACT_PREFIX = 'wandb-artifact://'


def create_dataset_artifact(opt):
    with open(opt.data) as f:
<<<<<<< HEAD
        data = yaml.load(f, Loader=yaml.SafeLoader)  # data dict
=======
        data = yaml.safe_load(f)  # data dict
>>>>>>> cad7acac832fcd4a9c2e09e773050a57761e22b9
    logger = WandbLogger(opt, '', None, data, job_type='Dataset Creation')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
<<<<<<< HEAD
    parser.add_argument('--data', type=str, default='data/coco.yaml', help='data.yaml path')
    parser.add_argument('--single-cls', action='store_true', help='train as single-class dataset')
    parser.add_argument('--project', type=str, default='YOLOR', help='name of W&B Project')
=======
    parser.add_argument('--data', type=str, default='data/coco128.yaml', help='data.yaml path')
    parser.add_argument('--single-cls', action='store_true', help='train as single-class dataset')
    parser.add_argument('--project', type=str, default='YOLOv5', help='name of W&B Project')
>>>>>>> cad7acac832fcd4a9c2e09e773050a57761e22b9
    opt = parser.parse_args()
    opt.resume = False  # Explicitly disallow resume check for dataset upload job

    create_dataset_artifact(opt)
