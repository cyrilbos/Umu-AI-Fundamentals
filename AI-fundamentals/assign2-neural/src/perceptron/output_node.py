import math


class OutputNode:
    def __init__(self, emotion):
        self._emotion = emotion
        self._input_links = []

    def get_activation_level(self, image):
        node_sum = 0
        for input_link in self._input_links:
            input_node = input_link.input_node
            activation_level = input_node.get_activation_level(image)
            node_sum += input_link.weight * activation_level

        return 1 / (1 + math.exp(-node_sum))

    @property
    def input_links(self):
        return self._input_links

    @property
    def emotion(self):
        return self._emotion
