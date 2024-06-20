# How To Finetune, Evaluate and Visualize BiFormer on CIFAR100 Dataset

## Environment Setup

Please make sure you have installed [conda](https://docs.conda.io/projects/conda/en/stable/), then you can create the environment with the command below:

```bash
bash scripts/envtool.sh create
conda activate biformer
```

If you are using slurm clusters, it is recommended to create a slurm config file for each available cluster:

```bash
export CLUSTER_ID=[YOUR_CLUSTER_ALIAS]
cp configs/slurm/sz10.yaml configs/slurm/${CLUSTER_ID}.yaml && vim configs/slurm/${CLUSTER_ID}.yaml
```
hence you can launch experiments in any available cluster consistently with `+slurm=${CLUSTER_ID}`.

If you want to manually config the environment, you can use the following commands:

```bash
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
pip3 install fvcore timm einops fairscale omegaconf
````

## Data Preparation

You can manually download the CIFAR100 dataset from [here](https://www.cs.toronto.edu/~kriz/cifar.html) and put it in the `data` folder as follows.

```Shell
├── data
    ├── cifar-100
        ├── cifar-100-python
            ├── meta
            ├── test
            ├── train
```

Or you can follow the code to download the dataset automatically:

## Finetune and Evaluate

To finetune the BiFormer on CIFAR100 dataset, you need to download the pretrained model.

|       name        |                                            model                                             |
|:-----------------:|:--------------------------------------------------------------------------------------------:| 
|    BiFormer-T     | [onedrive](https://api.onedrive.com/v1.0/shares/s!AkBbczdRlZvChHEOoGkgwgQzEDlM/root/content) |
|    BiFormer-S     | [onedrive](https://api.onedrive.com/v1.0/shares/s!AkBbczdRlZvChHDyM-x9KWRBZ832/root/content) |
|    BiFormer-B     | [onedrive](https://api.onedrive.com/v1.0/shares/s!AkBbczdRlZvChHI_XPhoadjaNxtO/root/content) |
|   BiFormer-STL    | [onedrive](https://api.onedrive.com/v1.0/shares/s!AkBbczdRlZvChSf-m7ujkvx9lIQ1/root/content) |
| BiFormer-STL-nchw | [onedrive](https://api.onedrive.com/v1.0/shares/s!AkBbczdRlZvChWYrKbWbMgqd2Ai0/root/content) |

After downloading the checkpoints, you need to put them in the `checkpoints` folder and rename them as follows.

```Shell
├── checkpoints
    ├── biformer_base_in1k.pth
    ├── biformer_small_in1k.pth
    ├── biformer_stl_in1k.pth
    ├── biformer_stl_nchw_in1k.pth
    ├── biformer_tiny_in1k.pth
```

Now you can finetune the model on CIFAR100 dataset with the following command.

```bash
scripts/finetune.sh
```

And you can evaluate the finetuned model with the following command.

```bash
scripts/evaluate.sh
```


