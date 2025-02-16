# Implementor - TV (Bridge Interface)
class TV:
    def turn_on(self):
        pass

    def turn_off(self):
        pass

# Concrete Implementors - Different TV Brands
class SonyTV(TV):
    def turn_on(self):
        print("Sony TV is now ON")

    def turn_off(self):
        print("Sony TV is now OFF")

class SamsungTV(TV):
    def turn_on(self):
        print("Samsung TV is now ON")

    def turn_off(self):
        print("Samsung TV is now OFF")

# Abstraction - Remote Control
class RemoteControl:
    def __init__(self, tv):
        self.tv = tv  # Bridge connection

    def turn_on(self):
        self.tv.turn_on()

    def turn_off(self):
        self.tv.turn_off()

# Concrete Abstraction - Advanced Remote (with extra features)
class AdvancedRemoteControl(RemoteControl):
    def mute(self):
        print("TV is now Muted")

# Client Code
if __name__ == "__main__":
    sony_tv = SonyTV()
    samsung_tv = SamsungTV()

    remote1 = RemoteControl(sony_tv)  # Standard remote for Sony TV
    remote2 = AdvancedRemoteControl(samsung_tv)  # Advanced remote for Samsung TV

    remote1.turn_on()  # Output: Sony TV is now ON
    remote2.turn_on()  # Output: Samsung TV is now ON

    remote2.mute()  # Output: TV is now Muted
