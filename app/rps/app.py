import qi
import helper
import rps_lib

class RPS:

    def echo(self, message):
        return message

    def do_something(self):
        pass

def main():
    app = qi.Application()
    app.start()
    session = app.session
    my_service = RPS()
    session.registerService("RPS", my_service)
    app.run()

if __name__ == "__main__":
    main()