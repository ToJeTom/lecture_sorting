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

def bubble_sort(lst):
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if lst[i]>lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
    return lst


def insertion_sort(lst):
    for i in range(1, len(lst)):
        insert = i
        tmp = lst[i]
        for j in range(i - 1, -1, -1):
           if tmp < lst[j]:
               lst[j+1]  = lst[j]
               insert = j
           else:
               break
        lst[insert] = tmp
    return lst


def main():
    a = read_data("numbers.csv")
    print(a)
    #ss = selection_sort(a["series_1"])
    #print(ss)
    #bs = bubble_sort(a["series_1"])
    #print(bs)
    IS = insertion_sort(a["series_1"])
    print(IS)




if __name__ == '__main__':
    main()

