# **Кинотеатр**
# Дан массив кресел (один ряд) кинотеатра
# 0 кресло сводобно
# 1 кресло занято
# Нужно посадить человека как можно дальше от всех
# И вернуть число, количество кресел до ближайщего человека
# Напр
# 1, 0 ,1, 0, 0, 0, 0, 0, 1 -. 2
# Два кресла тк если сажаем на место X то два места свободных слева, и справа
# 1, 0 ,1, 0, 0, X, 0, 0, 1 -. 2
# int find_seat(const std::vector<int>& row)
# find_seat(row={1, 0, 0, 0, 1}) -> 2
# find_seat(row={1, 0, 1, 0, 0, 1, 0, 0, 0, 1}) -> 2
# find_seat(row={1, 0, 1, 0}) -> 1
# [0, 0, 1, 0]
# | -1
# {1, 1, 0, 1, 0}
# - 1 -1 2 3
# [1, 0,0,0]
# 1 4
# func find_seat(row []int32]) int {
# if len(row) == 0 {
# return 0
# }
# if len(row) == 1 {
# return 1
# }
# split_result := false
# index_from := -1
# max_value = 1 // default
# for i:=0 ; i< len(row); i++ {
# if index_from == -1 && row[i] == 0 {
# index_from = i
# continue
# }
# if row[i] == 1 {
# if index_from != -1 {
# empty_space = i - index_from // 2- 0 = 2
# if index_from > 0 && index_from < len(row) - 1 {
# empty_space = empty_space / 2 + 1
# }
# if empty_space > max_value {
# max_value = empty_space
# }
# }
# index_from = -1
# }
# }
# if index_from != -1 {
# empty_space = len(row) - index_from
# if empty_space > max_value {
# max_value = empty_space
# }
# }
# return max_value
# }