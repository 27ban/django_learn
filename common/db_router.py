class DbRouter(object):
    def db_for_read(self, model, **hints):
        print('read')
        return 'read'

    def db_for_write(self, model, **hints):
        print('write')
        return 'default'
