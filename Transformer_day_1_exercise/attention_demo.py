import numpy as np
from typing import Tuple


def softmax(x: np.ndarray) -> np.ndarray:
    exp_x = np.exp(x - np.max(x, axis=-1, keepdims=True))
    return exp_x / np.sum(exp_x, axis=-1, keepdims=True)


def scaled_dot_product_attention(
    Q: np.ndarray,
    K: np.ndarray,
    V: np.ndarray
) -> np.ndarray:
    d_k: int = K.shape[-1]
    scores: np.ndarray = (Q @ K.T) / np.sqrt(d_k)
    attention_weights: np.ndarray = softmax(scores)
    output: np.ndarray = attention_weights @ V
    return output


if __name__ == "__main__":
    np.random.seed(42)

    seq_len: int = 4
    d_k: int = 8
    d_v: int = 8

    Q: np.ndarray = np.random.rand(seq_len, d_k)
    K: np.ndarray = np.random.rand(seq_len, d_k)
    V: np.ndarray = np.random.rand(seq_len, d_v)

    attention_output: np.ndarray = scaled_dot_product_attention(Q, K, V)

    print("Attention Output:")
    print(attention_output)