class Target:
    def request(self):
        return "Target: The default target's behavior."


class Adaptee:
    def specific_request(self):
        return ".eetpadA eht fo roivaheb laicepS"

class Adapter(Adaptee, Target):
    def request(self):
        return f"[Translated] - {self.specific_request()[::-1]}" 

def client_code(target: 'Target') -> None:
    print(target.request())

if __name__ == "__main__":
    print("Client: Working just fine with Target Objects")
    target = Target()
    client_code(target=target)
    adaptee = Adaptee()
    print("Client: The Adaptee class has a weird interface. "
          "See, I don't understand it:")
    print(f"Adaptee: {adaptee.specific_request()}", end="\n\n")
    adapter = Adapter()
    client_code(adapter)

