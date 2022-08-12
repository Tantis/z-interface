
from config.network import HttpState


class LoginProcess:

    @staticmethod
    def first_login(response):

        print(1)
        return HttpState.State._ok, response, HttpState.Success.HTTP_SUCCESS

    @staticmethod
    def continue_login(response):
        print(2)
        return HttpState.State._ok, response, HttpState.Success.HTTP_SUCCESS
