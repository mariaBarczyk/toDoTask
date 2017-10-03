class User():
    user_name = ''
    password = ''

    def __init__(self, name, passw):
        self.user_name = name
        self.password = passw

    def display_info_about_user(self):
        return '*** ' + self.user_name + ' *** ' + self.password + ' ***'

    def __str__(self):
        return '### ' + self.user_name + ' ### ' + self.password + ' ###'
