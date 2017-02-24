import tensorflow as tf
#base intialize values of v1 to 0. This is not a 0 dim array, but a value of 0
#also, we need to place in all values in tf variables or constants. Nothing just open or static
one = tf.constant(1)
v1 = tf.Variable(0)

#this is a simple example of how we define constants of 0, 1, 2 dimentions
const = tf.constant(1)
const2 = tf.constant([2, 3, 4])
const3 = tf.constant([[1, 2, 3],[4, 5, 6]])

#we define every function as an operation. E.g. assign a const to a var. Add etc
#these are more like functions that we would call in later in the dataflow graph
add1 = tf.add(v1, one)
assign = tf.assign(v1, add1)
#The ABOVE LINE is actually the trickist part of the whole ex. 
#we are calling assign below, but how does ADD get executed. Is it just becaise the add1 is called as a input to assign which in turn gets pulled?
#could be, but to validate

#and, before we use anything, initialize all the variables
init = tf.initialize_all_variables()

#this is a standard format to perform session ops. You dont need to close if defined this way
with tf.Session() as session:
    session.run(init) #initialize all variables
    print session.run(v1) #what is the value of the varaible before we start
    for _ in range(3):
        session.run(assign)
        print session.run(v1)
