# Neural network set up
## Weight Initialization
https://medium.com/usf-msds/deep-learning-best-practices-1-weight-initialization-14e5c0295b94

To avoid vanishing & exploding gradient, we need to initialize the nn's weight carefully. 

An old fashion way to initialize the weight is to draw a even distribution weight with bound of 

<img src = images/bound.png height = 100>. 
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
<img src = images/he.png height = 100>

(3) Tanh - Xavier initalization
<img src = images/Xavier.png height = 100>

## Convolutional Neural Network

It is a great way to reduce number of training examples by sharing weights and sparisity of connection - a value is the later layer is only responded to its receptive field (a fixed number of inputs and not all input).

In a signal processing prosperity, CNN doesn't use convolution but correlation. In signal processing, correlation doesn't need to flip the kernel but convolution does. 

A typical filter is the sobel filter, which is 
```
1   0  -1
3   0  -3
1   0  -1
```

For a N x N image, with a f x f filter, after convolution, the new image size is (N-f+1) x (N-f+1). If you choose 'valid', meaning no padding, 'same', means padded to same shape, which means p = f+1 /2. When padding is applied, then the new image size is (N-f+2p-1) ^2. Stride means jump and skip, which will have new image size (((N-f+2p)/d + 1) ^2, where in case it is not an int, you need to round it down. The benefit of stride is that it allows equal contribution to the later layer among each pixel. For example, if you don't use padding, the upper most left pixel will only be used one in the convolutional operation, while the middle of will be used multiple times.

The number of filter (Fn) will be the number of your channels for the next CNN layer. Don't forget for each filter, there is one bias term (b). Therefore, for a 3x3x3 fitler, if you have 10 of them, the total number of training parameters are 3x3x3 + 10 = 280

In CNN, the kernel's channel must matched the image channel. For example, for an RGB image, which has 3 channels, the filter must have 3 channel too, but you can have as many filter as your resource permitted. 
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

Activation matrix for channel last format:
m x Nh[l] x Nw[l] x Nc[l]
Activation matrix for channel first format:
m x Nc[l] x Nh[l] x Nw[l]
In keras, by default, it is channel last

m is the number of examples in this batch
```
A CNN layer is often followed by a pooling layer to reduce the the size of the image.

One special case of CNN filter is the 1x1 filter. It serves as a cross channel pooling layer. It also greatly reduced the number of parameters, allowing the network to go deeper. Together with residual connection, they are the key moving from VGG to ResNet with higher perfromance and less numebr of parameters. A 1x1 filter is basically introducing a fully connected layer into the CNN.

We can also do it reversly, to replace FCN, we can use a filter that has the same size as the image to convert the image to a 1D vector. 

<img src = images/11.png>

### CNN history
### 1. Classification

Resource:
http://cs231n.stanford.edu/slides/2019/cs231n_2019_lecture09.pdf
<img src = images/complex.png>

#### 1. LeNet-5 (1998)
<img src = images/LeNet5.png height = 200>
First generation of DCNN.

#### AlexNet (2012)
<img src = images/AlexNet.png height = 200>
It add dropout, ReLU activations, SGD with momentum.

#### GoogleNet/Inception(2014)
<img src = images/Incep.png height = 200>
It used batch normalization, RMSprop and most importantly Mlpconv (1x1 filter added in the middle), which serves as a non-linear filter. No FC layers.

Over the years, it has been developed for multiple version:
http://www.programmersought.com/article/7609143938/

<img src = images/Godeeper.png>
#### VGG(2014)
<img src = images/VGG.png height = 200>
Very uniform architecture but large number of parameters

#### ResNet(2015)
<img src = images/ResNet.png height = 200>
1X1 with skip connections to make the network go deeper

### 2. Object Detection

In image classification and object detection, usually you have one object. You can do image classification on multiple object in one images, but they require you to do one hot coding all your classes and your sigmoid instead of softmax in the last layer. See my github repo in predicting fashino attributes based on image data: https://github.com/YIZHE12/fashiontags

In object detection class, you have more than one object. For each object, you have two output - label (class) and bounding box coordinate (x, y, w, h)

Intersection over union (IOU):
Evaluation of the correctness of the bounding box. One bounding box is the labelled data. One bouding box is our prediciton. IOU is the size of overlapping areas between the two bounding box / union of the areas of the two bounding box. If IOU >= 0.5, then we say the prediciton is correct.


#### YOLO - you only look once
It segmented the images to gird and output the prediction of each grid. The values of x, y is between 0 and 1. It means the distance from the corner (said top left) of the gird cell to (said top left) corner of the bounding box. Therefore, it used the sigmoid function. For w and h, it can be larger than 1, meaning it can extend outside the gird. Therefore, it used an exp function.

Non-max suppresion: only keep the box with the highest pc if multiple box are selected for the same object

For different grid flagging the same object, only keep the one with the highest IOU.

Procedure of YOLO:
1. Assume there are 19x19 grid, then each grid has the output as \[pc bx by bh bw] if there is one class

2. Discard all boxes with pc<=0.6

3. Pick the box with the largest pc output that as a prediction

4. Discard any remainding box with IoU>=0.5 with the box output in the previous step






#### 3. GAN

### Other things about CNN

Note that CNN layer is often followed by Max Pool, Dropout and Batchnorm. Note that nowaday, often we use spatial dropout to remove the entrie feature map instead of a few neurons. 


# Neural network type
## [Restricted boltzmann machinese](http://deeplearning.net/tutorial/rbm.html)
A good example: https://github.com/hismael17/RBM

## Autoencoder
## [sparse coding model](https://blog.metaflow.fr/sparse-coding-a-simple-exploration-152a3c900a7c)



