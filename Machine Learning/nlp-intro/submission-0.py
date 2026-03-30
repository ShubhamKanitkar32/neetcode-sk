import torch
import torch.nn as nn
from torchtyping import TensorType
from typing import List

class Solution:
    def get_dataset(self, positive: List[str], negative: List[str]) -> TensorType[float]:
        # 1. Build vocabulary: collect all unique words, sort them, assign integer IDs starting at 1
        # 2. Encode each sentence by replacing words with their IDs
        # 3. Combine positive + negative into one list of tensors
        # 4. Pad shorter sequences with 0s using nn.utils.rnn.pad_sequence(tensors, batch_first=True)
        all_sen = positive + negative
        vocab = set()

        for sen in all_sen:
            for word in sen.split():
                vocab.add(word)
        
        word_to_id = {}
        for i, word in enumerate(sorted(vocab)):
            word_to_id[word] = i+1

        encoded = []
        for sen in all_sen:
            ids = []
            for word in sen.split():
                ids.append(word_to_id[word])
            encoded.append(torch.tensor(ids))
        
        return nn.utils.rnn.pad_sequence(encoded, batch_first=True)

