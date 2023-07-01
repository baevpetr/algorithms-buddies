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
# Тут сложная задача
# Дан массив точек координаты x,y
# Нужно проверить есть ли среди точек вертикальная линия, относительно которой точки стоят зеркально
# И если есть вернуть тру либо false если такая линия есть
# //points: [ [1,2], [3,4]]
# func validate(points [][]int) bool {
# check_hashtable = make(map[int]map[int]bool)
# min = 99999999
# max = -99999999
# if len(points) == 0 {
# return false
# }
# // обработать нечентное количество
# for i:=0; i<len(points); i++ {
# x := points[i][0]
# y := points[i][1]
# if x < min {
# min = x
# }
# if x > max {
# max = x
# }
# if _, ok := check_hashtable[x]; !ok {
# check_hashtable[x] = make(map[int]bool)
# }
# check_hashtable[x][y] = true
# }
# //10, 20
# //20 + 10 = 30
# median := 2*min + (max - min)
# for i:=0; i<len(points); i++ {
# x := points[i][0]
# y := points[i][1]
# second_x := 0
# if x*2 < median {
# second_x = x + median - 2*x
# } else {
# second_x = x - (2*x - median)
# }
# if _, ok := check_hashsetable[second_x]; !ok {
# return false
# }
# if _, ok := check_hashsetable[second_x][y];!ok {
# return false
# }
# }
# return true
# }
