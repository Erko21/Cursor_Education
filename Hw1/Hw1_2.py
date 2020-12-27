#Composition
class Laptop():
    def __init__(self):
        hard_disk_1 = Hard_disk("These are files in hard disk 1")
        hard_disk_2 = Hard_disk("These are files in hard disk 2")
        self.hard_disks = [hard_disk_1, hard_disk_2]

    def show_files(self):
        print(self.hard_disks)
        for disk in self.hard_disks :
            print(disk.files)

class Hard_disk():
    def __init__(self, files):
        self.files = files
disk = Laptop()
disk.show_files()




#aggregation
class Guitar():
    def __init__(self, strings):
        self.strings = strings

    def play(self):
        print(f"I am playing on guitar with {self.strings.strings_type}")

class Strings():
    def __init__(self, strings_type):
        self.strings_type = strings_type

strings = Strings('metal')
metal = Guitar(strings)
metal.play()
strings_type = strings.strings_type
print(strings_type)