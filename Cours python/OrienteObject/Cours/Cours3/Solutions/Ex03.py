from abc import ABC, abstractmethod

class Tool(ABC):
    @abstractmethod
    def use(self):
        pass


class Hammer(Tool):
    def use(self):
        return "Je frappe avec un marteau."


class Screwdriver(Tool):
    def use(self):
        return "Je visse avec un tournevis."


class Wrench(Tool):
    def use(self):
        return "Je serre avec une clé."


# Exemple d'utilisation
tools = [Hammer(), Screwdriver(), Wrench()]

for tool in tools:
    print(tool.use())
