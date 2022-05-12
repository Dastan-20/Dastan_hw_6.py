class Cars:
    brand = "Bmw, Mercedes"

    def __init__(self, title, model, max_speed, color, weight, hp):
        self.title = title
        self.model = model
        self.max_speed = max_speed
        self.color = color
        self.weight = weight
        self.hp = hp

    def start_engine(self):
        print(f"{self.title} {self.model}  engine started!")

    def stop_engine(self):
        print(f"{self.title} {self.model} engine stop!")

    def info(self):
        print(f"{self.title} {self.model} {self.weight} {self.hp} {self.max_speed} {self.color} информация о машине!")




mercedes = Cars("Mercedes", "S ClassG", 250, "black", "2.5 tons", 450 )
mercedes.start_engine()
bmw = Cars("Bmw", "M5 f90", 300, "blue", "2 tons", 600 )
bmw.start_engine()

mercedes = Cars("Mercedes", "S ClassG", 250, "black", "2.5 tons", 450 )
bmw.stop_engine()
mercedes.stop_engine()

mercedes = Cars("Mercedes", "S ClassG", 250, "black", "2.5 tons", 450 )
bmw.info()
mercedes.info()
