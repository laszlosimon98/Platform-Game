class MapIO:
    @staticmethod
    def load(file: str):
        result = list()
        with open(file, "r") as load:
            file = load.read().strip().split(",")
            for f in file:
                result.append(f)

        return result

    @staticmethod
    def save(file: str):
        pass
