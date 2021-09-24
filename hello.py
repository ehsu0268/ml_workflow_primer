import tensorflow as tf

hello = tf.constant('Hello, TensoFlow!')

# start tf session
sess = tf.Session()

# run the op
print(sess.run(hello))