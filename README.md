# Persistent-Label-Encoder
Persistent Label Encoder for Training and Inference in Machine learning 

For more generic approach, the above jupyter notebook has a custom function for fit and transform separately,

- The fit function gets train DataFrame and categorical columns list returns a Dict of label encoder classes.
- The Dict is pickled and loaded at the inference.
- The transform function gets Inference DataFrame, categorical columns list and the encoder Dict pickle path and returns the label encoded DataFrame.


For function code and working example, please refer to the jupyter notebook,
