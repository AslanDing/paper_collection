# Towards Understanding Self-Supervised Representation Learning

###### Why does training on a self-supervised learning task (using abundant unlabeled data) help with solving a
data-scarce downstream task? How does one formalize transferring of “knowledge & skills”?

 (Distributional assumptions) Unlabeled data distribution implicitly contains information about the
downstream classification task(s) of interest

(Representation learning) Models pre-trained on an appropriate SSL task can encode this signal through
learned representations that can subsequently solve downstream classification tasks with linear classifiers.

###### Why are low-dimensional representations, learned by solving a self-supervised learning task,able to solve downstream tasks with linear classifiers?


Empirical Rademacher complexity

represent the set 多样性

Contraction Mapping Principle