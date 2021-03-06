from torchvision import datasets, transforms
from ..mnist.dataset import stratified_split


def get_dataset(cls, root, train=True):
    assert cls in (datasets.CIFAR10, datasets.CIFAR100)

    # CIFAR10/100 are multiclass datasets with colour 32x32 images:
    #  x is float-tensor with shape [..., 3, 32, 32], y is a list of labels
    return cls(root, transform=transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
    ]), target_transform=None, train=train, download=True)


class CIFAR10_Train(object):
    """Train sample from the CIFAR10 dataset."""

    def __new__(cls, root, train_size=None, random_state=None):
        dataset = get_dataset(datasets.CIFAR10, root, train=True)
        if train_size is None:
            return dataset

        train, valid = stratified_split(dataset, train_size=train_size,
                                        random_state=random_state)
        return train


class CIFAR10_Test(object):
    """Test sample from the CIFAR10 dataset."""

    def __new__(cls, root):
        return get_dataset(datasets.CIFAR10, root, train=False)


class CIFAR100_Train(object):
    """Train sample from the CIFAR100 dataset."""

    def __new__(cls, root, train_size=None, random_state=None):
        dataset = get_dataset(datasets.CIFAR100, root, train=True)
        if train_size is None:
            return dataset

        train, valid = stratified_split(dataset, train_size=train_size,
                                        random_state=random_state)
        return train


class CIFAR100_Test(object):
    """Test sample from the CIFAR100 dataset."""

    def __new__(cls, root):
        return get_dataset(datasets.CIFAR100, root, train=False)


class AugmentedCIFAR10_Train(object):
    """Train sample from the CIFAR10 dataset."""

    def __new__(cls, root, disable=False):
        if not disable:
            transform = [
                transforms.RandomCrop(32, padding=4),
                transforms.RandomHorizontalFlip()
            ]

        else:
            transform = []

        return datasets.CIFAR10(root, transform=transforms.Compose([
            *transform,
            transforms.ToTensor(),
            transforms.Normalize((0.4914, 0.4822, 0.4465),
                                 (0.2023, 0.1994, 0.2010)),
        ]), target_transform=None, train=True, download=True)


class AugmentedCIFAR10_Test(object):
    """Test sample from the CIFAR10 dataset."""

    def __new__(cls, root):
        return datasets.CIFAR10(root, transform=transforms.Compose([
            transforms.ToTensor(),
            transforms.Normalize((0.4914, 0.4822, 0.4465),
                                 (0.2023, 0.1994, 0.2010)),
        ]), target_transform=None, train=False, download=True)
