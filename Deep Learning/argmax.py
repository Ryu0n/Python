import tensorflow as tf

x = [[2, 4, 6],
    [9, 3, 1]]

y = [[[1, 2, 3],
      [4, 5, 6]],
     [[5, 6, 2],
      [4, 7, 1]]]


with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    # argmax, axis : one-hot-encoding을 적용할 차원
    # axis=0 : 열로 비교 (같은 차원대의 다른 애들중에서 같은 인덱스끼리 비교)
    # aixs=1 : 행으로 비교
    # axis
    print('argmax_2d')
    print('axis=0\n',tf.argmax(x, axis=0).eval(session=sess))
    print('axis=1\n',tf.argmax(x, axis=1).eval(session=sess))

    # argmin
    print('\nargmin_2d')
    print('axis=0\n',tf.argmin(x, axis=0).eval(session=sess))
    print('axis=1\n',tf.argmin(x, axis=1).eval(session=sess))

    # axis=2
    print('\nargmax_3d')
    print('axis=0\n', tf.argmax(y, axis=0).eval(session=sess))
    print('axis=1\n', tf.argmax(y, axis=1).eval(session=sess))
    print('axis=2\n', tf.argmax(y, axis=2).eval(session=sess))