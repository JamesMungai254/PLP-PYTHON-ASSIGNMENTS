class Smartphone:
    def __init__(self, brand, model, storage, battery_life):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.battery_life = battery_life

    def make_call(self, number):
        print(f"Calling {number} from {self.model}...")

    def send_message(self, number, message):
        print(f"Sending message to {number}: {message}")

    def __str__(self):
        return f"{self.brand} {self.model} with {self.storage}GB storage and {self.battery_life} hours battery life"


class SmartphoneWithCamera(Smartphone):
    def __init__(self, brand, model, storage, battery_life, camera_megapixels):
        super().__init__(brand, model, storage, battery_life)
        self.camera_megapixels = camera_megapixels

    def take_photo(self):
        print(f"Taking a photo with {self.camera_megapixels}MP camera")

    def __str__(self):
        return super().__str__() + f" and {self.camera_megapixels}MP camera"


# Example usage
phone = Smartphone("Apple", "iPhone 13", 128, 20)
print(phone)
phone.make_call("123-456-7890")
phone.send_message("123-456-7890", "Hello!")

camera_phone = SmartphoneWithCamera("Samsung", "Galaxy S21", 256, 24, 108)
print(camera_phone)
camera_phone.take_photo()