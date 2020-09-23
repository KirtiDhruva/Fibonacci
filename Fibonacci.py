"""
Created on Fri Sep 18 13:09:32 2020
@author: Kirti Dhruva
"""
class Fibonacci:

    def __init__(self):

        self.index = 0
        self.previous = 0
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):

        self.index += 1

        if self.index == 1:
            return 0, self.index

        if self.index == 2:
            return 1, self.index

        temp = self.previous + self.current
        self.previous = self.current
        self.current = temp
        return self.current, self.index

    def reset(self):
        self.__init__()

    def get_series(self, count, start='current'):

        if start == 'reset':
            self.reset()

        elif start != 'current':
            print(f'start: Unknown keyword "{start}"')
            return

        series = []
        indexes = []

        count += self.index

        for value, index in self:
            series.append(value)
            indexes.append(index)
            if index == count:
                break
        return series, indexes

    def get_series_normalised(self, count, start='current'):

        series, indexes = self.get_series(count, start)

        for i in range(len(series)):
            series[i] = series[i]/series[-1]

        return series, indexes


    def get_ratios1(self, count, start='current'):

        series, indexes = self.get_series(count, start)

        ratios = []

        for i, index in enumerate(indexes[:-1]):
            ratios.append(series[i]/series[i+1])

        return ratios, indexes

    def get_ratios2(self, count, start='current'):

        series, indexes = self.get_series(count, start)

        ratios = []

        for i, index in enumerate(indexes[:-1]):
            if index == 1:
                ratios.append(0)    #could be changes to None
                continue
            ratios.append(series[i+1]/series[i])

        return ratios, indexes