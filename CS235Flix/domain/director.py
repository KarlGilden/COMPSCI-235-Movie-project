class Director:

    def __init__(self, director_full_name: str):
        if director_full_name == "" or type(director_full_name) is not str:
            self.__director_full_name = None
        else:
            self.__director_full_name = director_full_name.strip()

    @property
    def director_full_name(self) -> str:
        return self.__director_full_name

    @director_full_name.setter
    def director_full_name(self, director):
        self.__director_full_name = director

    def __repr__(self):
        return f"<Director {self.__director_full_name}>"

    def __eq__(self, other):
        if self.__director_full_name.lower() == other.__director_full_name.lower():
            return True
        else:
            return False

    def __lt__(self, other):
        return self.__director_full_name < other.__director_full_name

    def __hash__(self):
        return hash(self.__director_full_name)
