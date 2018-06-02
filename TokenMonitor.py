import websocket

try:
    import thread
except ImportError:
    import _thread as thread
import time

websocket.enableTrace(True)


class TokenMonitor:
    def __init__(self):
        self.name = 'Token Monitor'

        self.ws = websocket.WebSocketApp("wss://socket.etherscan.io/wshandler",
                                         on_message=self.on_message,
                                         on_error=self.on_error,
                                         on_close=self.on_close)
        self.ws.on_open = self.on_open
        self.ws.run_forever()

    def connect(self):
       # self.ws.connect("wss://socket.etherscan.io/wshandler")
        print("connected = {}".format(self.name))

    def on_message(self, ws, message):
        print("<< {}".format(message))

    def on_error(self, ws, error):
        print(error)

    def on_close(self, ws):
        print("### closed ###")

    def on_open(self, ws):
        self.ws.send("{'event': 'txlist', 'address': '0x2a65aca4d5fc5b5c859090a6c34d164135398226'}")

        def run(*args):
            while True:
                time.sleep(20)
                print(">> ping")
                ws.send("{'event': 'ping'}")
            print("closing websocket...")
            ws.close()
            print("thread terminating...")

        thread.start_new_thread(run, ())


if __name__ == '__main__':
    my_tnm = TokenMonitor()
    print("I'm a monitor!")

