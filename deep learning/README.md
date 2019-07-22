# Weight Initialization
https://medium.com/usf-msds/deep-learning-best-practices-1-weight-initialization-14e5c0295b94

To avoid vanishing & exploding gradient, we need to initialize the nn's weight carefully. 

For the b terms, usually, we set it to zero. For the W term, we can use several strategies based on the activation functions:

(1) sigmoid - random initalization

np.random.randn(size_l, size_l-1)

where size_l is the number of neurons in l layer

(2) Relu - he initalization
<img src = images/he.png>

(3) Tanh - Xavier initalization
<img src = images/Xavier.png>



