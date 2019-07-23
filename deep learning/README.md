# Neural network basic
## Weight Initialization
https://medium.com/usf-msds/deep-learning-best-practices-1-weight-initialization-14e5c0295b94

To avoid vanishing & exploding gradient, we need to initialize the nn's weight carefully. 

An old fashion way to initialize the weight is to draw a even distribution weight with bound of <img src = images/bound.png height = 100>. 
```
np.random.uniform(-sqrt(6)/(size_l + size_l-1), sqrt(6)/(size_l + size_l-1), (size_l, size_l-1))
```

However, this will create a vanishing or exploding gradients. Therefore, nowaday, it is rarely use. 

For the b terms, usually, we set it to zero. For the W term, we can use several strategies based on the activation functions:

(1) sigmoid - random initalization
```
np.random.randn(size_l, size_l-1)
```
where size_l is the number of neurons in l layer

Later, people found out that by multiply the random initialization with a factor it can force the standard deviation of the weights close to 1. Therefore, we have the he and Xavier initalizaiton:

(2) Relu - he initalization
<img src = images/he.png height = 200>

(3) Tanh - Xavier initalization
<img src = images/Xavier.png height = 200>

## Convolutional Neural Network

In a signal processing prosperity, CNN doesn't use convolution but correlation. In signal processing, correlation doesn't need to flip the kernel but convolution does. 

A typical filter is the sobel filter, which is 
```
1   0  -1
3   0  -3
1   0  -1
```

For a N x N image, with a f x f filter, after convolution, the new image size is (N-f+1) x (N-f+1). If you choose 'valid', meaning no padding, 'same', means padded to same shape, which means p = f+1 /2. When padding is applied, then the new image size is (N-f+2p-1) ^2. Stride means jump and skip, which will have new image size (((N-f+2p)/d + 1) ^2, where in case it is not an int, you need to round it down. 

The number of filter (Fn) will be the number of your channels for the next CNN layer. Don't forget for each filter, there is one bias term (b). Therefore, for a 3x3x3 fitler, if you have 10 of them, the total number of training parameters are 3x3x3 + 10 = 280

```
Filter size: f[l]
Padding: p[l]
Stride: s[l]
Filter: f[l]

Each filter has Nc[l-1] channels
Number of filter is Nc[l]

Input layer shape:
Nh[l-1] x Nw[l-1] x Nc[l-1]
Output layer shape:
Nh[l] x Nw[l] x Nc[l]

We know that
Nh[l] = round down((Nh[l-1] - f[l] + 2 p[l] )/ s[l] +1)
Nw[l] = round down((Nw[l-1] - f[l] + 2 p[l] )/ s[l] +1)
Nc[l] = # filter

The number of weights: f[l] x f[l] x Nc[l-1] x Nc[l]
The number of bias: Nc[l]
Total number of training parameters: (f[l] x f[l] x Nc[l-1] +1) x Nc[l]

Activation matrix:
m x Nh[l] x Nw[l] x Nc[l]
m is the number of examples in this batch
```






In CNN, the kernel's channel must matched the image channel. For example, for an RGB image, which has 3 channels, the filter must have 3 channel too, but you can have as many filter as your resource permitted. 


# Neural network type
## [Restricted boltzmann machinese](http://deeplearning.net/tutorial/rbm.html)
A good example: https://github.com/hismael17/RBM

## Autoencoder
## [sparse coding model](https://blog.metaflow.fr/sparse-coding-a-simple-exploration-152a3c900a7c)



