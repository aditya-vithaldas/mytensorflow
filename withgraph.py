import tensorflow as tf
a = tf.constant(10, name="a")
b = tf.constant(90, name="b")
y = tf.Variable(a+b*2, name="y")
model = tf.initialize_all_variables()
with tf.Session() as session:
	#this would merge all the summaries into the default graph
	#i dont know what exactly a graph is at the moment, but I would get there
    merged = tf.merge_all_summaries()

    #this would write all the summaries into the graph

    writer  = tf.train.SummaryWriter("/tmp/tensorflowlogs", session.graph_def)
    session.run(model)
    print (session.run(y))

#at the end of it, can view the tensorflowboard using the following command
#tensorboard --logdir=/tmp/tensorflowlogs
#not able to get it working on a remote web server. to get there soon
