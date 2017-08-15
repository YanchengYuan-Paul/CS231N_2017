# CS231N_2017

This repository records my implementation of assignments.

**During the implementation, I found the following:**

1. Since Python 3 does not support *xrange*, the instructor add the following 
```python
from past.builtins import xrange
```
I guess this is to import *xrange* from the old version Python. However, there is no module called **past** included in the assignmet files. So this is a bug. Maybe the reason is that, in my computer, there is no Python 2.
One concern why the designers still want to use *xrange* is, some people claimed that *range* in Python 3 is slower than *xrange* in Python 2. However, this may not be a real issue. I found some discussions in Stack Overflow, you can see [Why is there no xrange function in Python3?](https://stackoverflow.com/questions/15014310/why-is-there-no-xrange-function-in-python3). 
In my implementation, I just comment the import, and replace *xrange* with *range*. 