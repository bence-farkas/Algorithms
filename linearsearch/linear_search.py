class LinearSearch:
    @staticmethod
    def linear_search(input_list, requested_element):
        for idx, i in enumerate(input_list):
            if i == requested_element:
                return idx
        return -1

    @staticmethod
    def linear_search_extended(input_list, requested_element):
        indexes = []
        for idx, i in enumerate(input_list):
            if i == requested_element:
                indexes.append(idx)
        if len(indexes) > 0:
            return indexes
        else:
            return -1