**1: What is Generative AI?**

Generative AI is a type of AI that can create new content like text, images, music, videos, or code. It learns patterns from data and uses them to generate something new.

Unlike traditional AI, which only predicts or classifies things (like detecting spam emails), Generative AI makes new things.

Real-world examples:

1. Chatbots that answer questions.
2. AI art generators that make pictures from text.
3. Code assistants that help write programs.

In short, Generative AI learns from data and creates useful content.



**2: Self-Attention Explained (With Example)**
Use this sentence:
"The cat sat on the mat"
Explain clearly:

_What are Query Q, Key K, and Value V?_
* Each word is converted into a vector (a list of numbers representing its meaning).
* Query (Q): What we are “looking for.” For example, if the word is “cat”, its query vector asks: Which words in the sentence are important for me?
* Key (K): What each word “offers.” Each word has a key vector that says: How relevant am I to others?
* Value (V): The actual information of the word that we might use when combining words.

Example:

For the word “cat”, Q looks at all Ks in the sentence to see which words are important. If “mat” is related, it will pay more attention to it. The final output is a weighted sum of Vs.

**Why scale by √d_k?**

* d_k is the dimension of the key vectors.
* When vectors have large dimensions, the dot product of Q·K can become very large, making softmax produce tiny gradients (hard to train).
* Dividing by √d_k keeps the numbers smaller and stabilizes learning.


**Why apply Softmax?**

* After computing Q·K for each word pair, we get attention scores.
* Softmax converts these scores into probabilities that sum to 1.
* This tells the model how much attention to give each word.

Example: For “cat”, Softmax might give:

* “The”: 0.1, “cat”: 0.4, “sat”: 0.2, “on”: 0.1, “the”: 0.05, “mat”: 0.15
* These weights are used to combine the value vectors (V).



**What problem does attention solve that RNNs struggled with?**

* RNNs process words one by one, so remembering long-range dependencies (like “cat” → “mat”) is hard.
* Self-Attention allows every word to look at all other words at once, capturing long-distance relationships efficiently.





**Encoder vs Decoder Comparison**

| Component           | Encoder                                                                 | Decoder                                                                                                   |
| ------------------- | ----------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| **Main function**   | Reads the input and creates **contextual representations** of all words | Generates the output word by word using encoder information and previously generated words                |
| **Input**           | Original sentence (e.g., “The cat sat on the mat”)                      | Previous output words (during training, the target sequence; during inference, generated words so far)    |
| **Self-Attention**  | Standard self-attention (each word can see all other words)             | **Masked self-attention**: each word can only see **previous words**, not future ones (prevents cheating) |
| **Cross-Attention** | Not used                                                                | **Cross-attention**: each word attends to **encoder outputs** to get context from input                   |
| **Output**          | Encoded representations (vectors with context for each input word)      | Predicted next word probabilities, eventually forming the full output sequence                            |
| **Use Case**        | Understanding input                                                     | Generating output                                                                                         |


**Vision Transformers (ViT) – High-Level Explanation**

**Vision Transformers (ViT)** apply the transformer architecture, originally designed for text, to image understanding tasks. Instead of processing the entire image at once, ViT first divides the image into **small fixed-size patches**.

### Image Patches

An image is split into smaller blocks called **patches**. For example, a 224×224 image can be divided into **16×16 pixel patches**. Each patch acts like a “word” in a sentence. If the image is divided into many patches, the model treats them as a sequence similar to how text models process words.

### Converting Patches into Tokens

Each image patch is flattened into a one-dimensional vector (a list of pixel values). Then, a **linear projection layer** converts this vector into an embedding called a **token**. These tokens represent the visual information of each patch in a numerical form that the transformer can process. After this step, the image becomes a sequence of tokens just like a sequence of words in natural language processing.

### Positional Embeddings

Transformers do not naturally understand the **order or position** of tokens. In images, the position of each patch is very important (for example, the sky is usually above the ground). To solve this, **positional embeddings** are added to each patch token. These embeddings give the model information about where each patch is located in the image, allowing it to understand spatial relationships.

### Difference from CNNs

Conceptually, Vision Transformers are different from **Convolutional Neural Networks (CNNs)**. CNNs use **convolution filters** that scan over nearby pixels and learn local features such as edges or textures. Vision Transformers, however, use **self-attention**, allowing each patch to directly interact with every other patch in the image. This helps the model capture **global relationships** between different regions of the image rather than focusing mainly on local patterns.



