def pad_sequences(seqs, pad_value=0, max_len=None):
    """
    Returns: np.ndarray of shape (N, L) where:
      N = len(seqs)
      L = max_len if provided else max(len(seq) for seq in seqs) or 0
    """
    if max_len is None:
        max_len = max((len(seq) for seq in seqs), default=0)
    
    result = np.full((len(seqs), max_len), pad_value)
    for i, seq in enumerate(seqs):
        result[i, :len(seq)] = seq[:max_len]
    
    return result