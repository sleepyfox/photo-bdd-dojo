class Camera:
    def __init__(self):
        self.counter = 1
        self.photos = []

    def take_photo(self):
        self.photos.append(self.counter)
        last_photo_id = self.counter
        self.counter += 1
        return last_photo_id # ID of picture just taken

    def photo_stream(self):
        return self.photos

    def approve(self):
        return True
