import os, csv


def read_data(file_name):
    """
    Reads csv file and returns numeric data.

    :param file_name: (str), name of CSV file
    :return: (dict), dictionary with numeric data, keys - csv column names, values - numbers in each column
    """
    cwd_path = os.getcwd()
    file_path = os.path.join(cwd_path, file_name)
    data = {"series_1": [], "series_2": [], "series_3": []}
    with open(file_path, "r") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            for key, value in row.items():
                data[key].append(int(value))
    return data

def selection_sort(lst, direction="ascending"):
    if direction == "ascending":
        for i in range(len(lst) - 1):
            idx = i
            for j in range(i + 1, len(lst)):
                if lst[j] < lst[idx]:
                    idx = j
            lst[i], lst[idx] = lst[idx], lst[i]
        return lst
    else:
        for i in range(len(lst) - 1):
            idx = i
            for j in range(i + 1, len(lst)):
                if lst[j] > lst[idx]:
                    idx = j
            lst[i], lst[idx] = lst[idx], lst[i]
        return lst


def main():
    a = read_data("numbers.csv")
    print(a)
    b = selection_sort(a["series_1"])
    print(b)




if __name__ == '__main__':
    main()

