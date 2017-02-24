import tensorflow as tf

#read up  little more on placeholders. BUT it basically is a way to feed data from outside the model
#in varaibles, all the values were defined from inside (constant as a starting point). BUT if we want to get data from outside (like a variable to a function). that variables cant do. Use placebolders

#my placeholder is just an float 32. How do I define a matrix?
a = tf.placeholder(tf.float32)

#my function or data flow operation is b, which multiplies a by 2
b = 2*a
complex_dict = {a: [[1, 2, 3],[4, 5, 6]]}
with tf.Session() as session:
    #feed in my variable using feed_dict. Simple scalar to start with
    result = session.run(b, feed_dict={a:3.5})
    print result

    #multiple by a more complex variable. A matric
    complex_result = session.run(b, feed_dict=complex_dict)
    print complex_result

