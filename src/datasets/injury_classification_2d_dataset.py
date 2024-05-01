
import torch
import numpy as np

from torch.utils.data import Dataset
from raw_dataset import RawDataset


class InjuryClassification2DDataset(Dataset):
    '''
    Dataset for training the "2D injury classification model".
    '''
    
    def __init__(self, raw_dataset: RawDataset, sample):
        self.pairs = []
        for i in range(len(raw_dataset)):
            (
                images,
                bowel_healthy,
                extravasation_healthy,
                kidney_condition,
                liver_condition,
                spleen_condition
            ) = raw_dataset[i]

            labels = {
                'bowel': bowel_healthy,
                'extravasation': extravasation_healthy,
                'kidney': kidney_condition,
                'liver': liver_condition,
                'spleen': spleen_condition
            }

            sampled_images = sample(images)
            for image in sampled_images:
                self.pairs.append({
                    'image': image,
                    'labels': labels
                })

    def __len__(self):
        return len(self.pairs)
    
    def __getitem__(self, index):
        '''
        Get the `index`-th image-label pair.

        Parameters
        ----------
        `index`: the index

        Returns
        -------
        `{'image': np.array, 'labels': {'bowel': np.float32, 'extravasation': np.float32, 'kidney': np.array, 'liver': np.array, 'spleen': np.array}}`
        '''
        return self.pairs[index]
        


if __name__ == '__main__':
    raw_dataset = RawDataset()

    dataset = InjuryClassification2DDataset(raw_dataset, lambda x: x)

    for image, label in dataset:
        print(image.shape)
        print(label.shape)