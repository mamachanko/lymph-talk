import lymph


class Listen(lymph.Interface):

    @lymph.event('greeting')
    def on_greeting(self, event):
        print('Somebody greeted %s' % event['name'])