class BubbleSort:
    @staticmethod
    def bubble_sort(input_list: list) -> list:
        """

        Parameters
        ----------
        input_list : list
        """
        end_index = 0
        while end_index != len(input_list)-2:
            for i in range(len(input_list)-1, end_index, -1):
                a = input_list[i]
                b = input_list[i-1]
                if a < b:
                    input_list[i], input_list[i-1] = input_list[i-1], input_list[i]
            end_index += 1
        return input_list

    @staticmethod
    def bubble_sort_reversed(input_list: list) -> list:
        """

        Parameters
        ----------
        input_list : list
        """
        end_index = len(input_list)-1
        while end_index != 1:
            for i in range(end_index):
                a = input_list[i]
                b = input_list[i+1]
                if a > b:
                    input_list[i], input_list[i+1] = input_list[i+1], input_list[i]
            end_index -= 1
        return input_list
