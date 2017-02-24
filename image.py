import matplotlib.image as mp_image
filename = "image.jpg"
input_image = mp_image.imread(filename)
#print input_image
print input_image.ndim
print input_image.shape

import matplotlib.pyplot as plt
import tensorflow as tf 
x = tf.Variable(input_image, name="x")
model = tf.initialize_all_variables()
with tf.Session() as session:
	x=tf.transpose(x, perm=[1,0,2])
	session.run(model)
	result=session.run(x)
	print "trying to imshow fig"
	plt.imshow(result)
	print "trying to save fig"
	plt.savefig("node.png")
	print 'trying to display'
	plt.show()
#plt.imshow(input_image)
#plt.show()
