## WEEK 11
### DAY 14 | 11 October | [14. Python Data Science NumPy and Pandas](https://www.youtube.com/watch?v=0qlhv8tk8RE&feature=youtu.be)   

**[Summary](https://www.linkedin.com/posts/iiec-rise_iiec-iiecabrrise-iiecabrconnect-activity-6723269390499880960-G4Js/)**
-  `lists` and `arrays` are data types used for storing data in rows and column. However, lists cannot be used to perform column-wise operations, where as arrays can.
-  `.shape` - used to check the dimension of the data. `.type()` - used to check the datatype of the variable.
-  If the array contains more than one column then it is known as `matrix`.
-  `.astype()` function is used to change the datatype.
-  `unicode` is a datatype with strings, integers (as a mixture). The mathematical operations can only preformed on integers so we convert from `unicode` to `int`.
-  In numpy we can provide the field name, it supports (in market people believe it cant so we move to pandas), example to demonstrate the field name in numpy, `a` had no field names.
```python
a = numpy.array([[1, "sai", 10], [2, "sia", 20], [3, "ias" ,30]])
a
type(a)
a.shape
a.dtype
# if you observe the dtypes of a ('<U21'), c('int64') and d ('<U1') are different at a: we have mixture of numericals and strings, c: its only numericals and d: has only strings. The dtype values for different mixture and individual datatypes is different.
# inorder to provide the filed names, we need to update it
a.dtype = {'names' : ['StudentRollNo', 'StudentName', 'StudetnAttendance'], 'formats' : [numpy.int64, numpy.unicode, numpy.int64]}
a


t = numpy.array([1, 2, 3])
t
t.dtype = {'names' : ['ID'], 'formats' : [numpy.int64]}
t
```
-  `formats` keyword is used to mention the data type of a particular column stored in an array.
-  In `numpy` array, a `2D array` is called `matrix` and a `1D array` is called a `vector`. In `pandas` is just a library extension of numpy that can help to reduce the complexity induced by writing a code for numpy. Numpy is hard-corded, whereas pandas is built on numpy.
-  `pandas.read_csv()` extension is one of the file formats which are extensively used in numpy or pandas to read the datasets stored in files. It stands for comma separation file format.
-  We can use `<variable name>.columns` to retrieve all the names of column fields in an array.
-  The `.iloc[]` function helps retrieve data present at particular location of an array.