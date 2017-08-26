# CS231N_2017

This repository records my implementation of assignments.

**During the implementation of assignment 1, I found the following:**

1. Since Python 3 does not support *xrange*, the instructor add the following 
  ```python
  from past.builtins import xrange
  ```
  I guess this is to import *xrange* from the old version Python. However, there is no module called **past** included in the assignmet files. So this is a bug. Maybe the reason is that, in my computer, there is no Python 2.
  One concern why the designers still want to use *xrange* is, some people claimed that *range* in Python 3 is slower than *xrange* in Python 2. However, this may not be a real issue. I found some discussions in Stack Overflow, you can see [Why is there no xrange function in Python3?](https://stackoverflow.com/questions/15014310/why-is-there-no-xrange-function-in-python3). 
  In my implementation, I just comment the import, and replace *xrange* with *range*. 

2. After you implemented **neural_net.py**, you will test the implementation via a toy model in the *Train the network* section in **two_layer_net.ipynb**. There is a small bug in the sample testing code. This reason is the default value of *batch_size* is **200** in **TwoLayerNet.train**, which exceed the dimension of toy data **X**. So, instead of 

  ``` python
  net = init_toy_model()
  stats = net.train(X, y, X, y,
            learning_rate=1e-1, reg=5e-6,
            num_iters=100, verbose=False)

  print('Final training loss: ', stats['loss_history'][-1])

  # plot the loss history
  plt.plot(stats['loss_history'])
  plt.xlabel('iteration')
  plt.ylabel('training loss')
  plt.title('Training Loss history')
  plt.show()
  ```
  I change it to 

  ```python
  net = init_toy_model()
  stats = net.train(X, y, X, y,
            learning_rate=1e-1, reg=5e-6,
            num_iters=100, verbose=False, batch_size = X.shape[0])

  print('Final training loss: ', stats['loss_history'][-1])

  # plot the loss history
  plt.plot(stats['loss_history'])
  plt.xlabel('iteration')
  plt.ylabel('training loss')
  plt.title('Training Loss history')
  plt.show()
  ```

3. When I try to run the **Extract Features** section in **features.ipynb**, I encounter the following errors:

  ```python
  Typerror: slice indices must be integers or None or have an __index__ method
  ```
  To handle this error, I modified the function **hog_feature** in *assignment1/cs231n/features.py*. In stead of 
  ```python
  orientation_histogram[:,:,i] = uniform_filter(temp_mag, size=(cx, cy))  [cx/2::cx, cy/2::cy].T
  ```
  in **line** 121, I change it to 

  ```python
  orientation_histogram[:,:,i] = uniform_filter(temp_mag, size=(cx, cy))  [int(cx/2)::cx, int(cy/2)::cy].T
  ```

**During the implementation of Assignment 2, I found the following:**

1. Still, like in the assignment 1, comment the following
  ```python
  # from past.builtins import xrange
  ```

  Also, if you use *Anaconda* directly, it may not install the package **future**, you need to add it. 

