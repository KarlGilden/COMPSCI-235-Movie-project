class Actor:
    def __init__(self, actor_full_name: str):
        if actor_full_name == "" or type(actor_full_name) is not str:
            self.__actor_full_name = None
        else:
            self.__actor_full_name = actor_full_name

        self.__colleagues = set()

    @property
    def actor_full_name(self) -> str:
        return self.__actor_full_name.strip()

    @property
    def colleagues(self):
        return self.__colleagues

    @actor_full_name.setter
    def actor_full_name(self, actor):
        self.__actor_full_name = actor.strip()
    
    def __repr__(self):
        return f"<Actor {self.__actor_full_name}>"

    def __eq__(self, other):
        if self.__actor_full_name.lower() == other.__actor_full_name.lower():
            return True
        else:
            return False

    def __lt__(self, other):
        return self.__actor_full_name.lower() < other.__actor_full_name.lower()

    def __hash__(self):
        return hash(self.__actor_full_name)
    
    def add_actor_colleague(self, colleague):
        self.__colleagues.add(colleague)

    def check_if_this_actor_worked_with(self, colleague):
        if colleague in self.__colleagues:
            return True
        else:
            return False