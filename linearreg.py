import numpy as np 
import tensorflow as tf 

#here, we basically generate 100 random samples. (we dont pick a range??)
#we define y as a the function plus minus a error. What really is that, focus that out later. But this i the sample generator. 
#output, has to be very close slope = 3 and intercept = 2
x_data = np.random.rand(100).astype(np.float32)
y_data = x_data * 3 + 2
y_data = np.vectorize(lambda y: y +np.random.normal(loc=0.0,scale=0.1))(y_data)
#see the sample values. 
print zip(x_data, y_data)[0:5]

#start with 2 random values for a and b. Eventualy they have to converge, but start with random
a = tf.Variable(0.0)
b = tf.Variable(5.0)

#y is defined as actual value. This is what we would compare with the real y to see how close we are to the outcome
y = a*x_data + b

#we are defining out loss function, which is the sun of square error
loss = tf.reduce_mean(tf.square(y - y_data))

#this is wehre the real meat takes place. We start with the learning rate, and mention that we really want to minimize loss, using gradiant descent 
#this is the function that would be called later iteratively
#THESE 3 LINES ARE BASICALLY CORE
learning_rate = 0.5
optimizer = tf.train.GradientDescentOptimizer(learning_rate)
train = optimizer.minimize(loss)

#the next 3-4 steps are the standard steps to run for all tf apps
init = tf.initialize_all_variables()
with tf.Session() as session:
	session.run(init)

	train_data = []

	#iterate 100 times to get to the right items.. Or is it, that we are just going through the 100 variables that we generated earlier? Probably the latter
	#go through all the data points which we have
	for step in range(100):
		
		#this is the part that I really dont understand. HOW DO a and b GET UPDATED? HOW DOES THE train / Minimize FUNCTION EVEN KNOW IT HAS TO UPDATE a AND b
		evals = session.run([train, a, b])[1:]

		if step % 5 == 0:
			print "a is " 
			print session.run(a)
			print "b is " 
			print session.run(b)
			print(step, evals)
			train_data.append(evals)
