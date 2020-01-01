import torch
from collections import OrderedDict

from cplxmodule.nn.relevance import Conv2dARD, LinearARD
from cplxmodule.nn.masked import Conv2dMasked, LinearMasked


class SimpleConvModel(object):
    """Simple convolutional model for MNIST.

    Use `__new__` returning a Sequential to mimic a smart model constructor,
    and simplify object reference via strings in JSON manifests.
    """
    Linear = torch.nn.Linear
    Conv2d = torch.nn.Conv2d

    def __new__(cls):
        return torch.nn.Sequential(OrderedDict([
            ("conv1", cls.Conv2d( 1, 20, 5, 1)),
            ("relu1", torch.nn.ReLU()),
            ("pool1", torch.nn.AvgPool2d(2, 2)),
            ("conv2", cls.Conv2d(20, 50, 5, 1)),
            ("relu2", torch.nn.ReLU()),
            ("pool2", torch.nn.AvgPool2d(2, 2)),
            ("flat_", torch.nn.Flatten(-3, -1)),
            ("lin_1", cls.Linear(4 * 4 * 50, 500)),
            ("relu3", torch.nn.ReLU()),
            ("lin_2", cls.Linear(500, 10)),
        ]))


class SimpleConvModelARD(SimpleConvModel):
    Linear = LinearARD
    Conv2d = Conv2dARD


class SimpleConvModelMasked(SimpleConvModel):
    Linear = LinearMasked
    Conv2d = Conv2dMasked


class SimpleDenseModel(object):
    Linear = torch.nn.Linear

    def __new__(cls):
        return torch.nn.Sequential(OrderedDict([
            ("flat_", torch.nn.Flatten(-3, -1)),
            ("lin_1", cls.Linear(1 * 28 * 28, 512)),
            ("relu2", torch.nn.ReLU()),
            ("lin_2", cls.Linear(512, 512)),
            ("relu3", torch.nn.ReLU()),
            ("lin_3", cls.Linear(512, 10)),
        ]))


class SimpleDenseModelARD(SimpleDenseModel):
    Linear = LinearARD


class SimpleDenseModelMasked(SimpleDenseModel):
    Linear = LinearMasked
