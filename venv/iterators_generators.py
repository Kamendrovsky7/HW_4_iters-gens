import types



#---------1 задание------------------------------------------------------------------------------

class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.list = []
        if len(self.list_of_list) > 0:
            for j in self.list_of_list:
                self.list.extend(j)
        return self

    def __next__(self):
        if len(self.list) == 0: raise StopIteration
        item = self.list.pop(0)
        return item

def test_1():

        list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

        for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

            assert flat_iterator_item == check_item

        assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()

#---------2 задание------------------------------------------------------------------------------

def flat_generator(list_of_lists):
    list = []
    digit = 0
    for j in list_of_lists:
        digit += len(j)
        list.extend(j)
    while digit != 0:
        item = list.pop(0)
        yield item
        digit -= 1

def test_2():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    test_2()

#---------3 задание------------------------------------------------------------------------------


class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.lists = [iter(self.list_of_list)]

    def __iter__(self):
        return self

    def __next__(self):
        while self.lists:
            try:
                item = next(self.lists[-1])
                if isinstance(item, list):
                    self.lists.append(iter(item))
                else:
                    return item
            except StopIteration:
                self.lists.pop()
        raise StopIteration


def test_3():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()
