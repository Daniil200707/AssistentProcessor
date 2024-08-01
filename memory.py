class ShortcutMemory:
    """
    Remember for short time
    """
    def __init__(self):
        self.memory = []

    def remember(self, data):
        """
        Remember data to list
        :param data: user text
        :return: None
        """
        self.memory.append(data)

        if len(self.memory) > 4:
            del self.memory[0]

    def get_memory(self):
        """
        Gives memory of separately words
        :return: words_list
        """
        words_list = []
        for element in self.memory:
            words = element.split()
            for word in words:
                words_list.append(word)

        return words_list

class LongTermMemory:
    """
    Remember for long time
    """

    def __init__(self):
        self.memory = {}
        self.len_memory = len(self.memory)

    def remember(self, data: list):
        """
        Remember data for dict
        :param data: List of words
        :return: none
        """
        for word in data:
            data_count = data.count(word)
            if data_count > 1:
                if self.len_memory < 1:
                    self.memory[word] = []
                else:
                    association = []
                    for element in data:
                        if element in data:
                            association.append(element)
                    self.memory[word] = association

