
class Hello:

    def __init__(self):

        self.__call_val()

    def __call_val(self):
        print('Hi')


class He(Hello):

    def __init__(self):
        super(He, self).__init__()

ob = He()

