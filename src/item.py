
class Item():
    def __init__(self, item_name, item_description):
        self.name= item_name
        self.description= item_description

        def __str__(self):
            print(f"{self.description} {self.name}")
        
        def __repr__(self):
            for i in self.items:
                print(f"{i.description} {i.name}")