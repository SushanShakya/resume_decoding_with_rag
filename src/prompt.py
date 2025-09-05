from src.utils import Utils


class Prompt:
    @staticmethod
    def system():
        file = "system.prompt"

        with open(Utils.prompt_path(file)) as f:
            content = f.read()

        return content
