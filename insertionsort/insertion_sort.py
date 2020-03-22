class InsertionSort:
    @staticmethod
    def insertion_sort(input_list):
        sorted_list = input_list[0]
        for i_idx, i_val in enumerate(1, range(input_list)):
            for s_idx, s_val in enumerate(range(sorted_list), 0, -1):
                if i_val < s_val:
                    sorted_list.


