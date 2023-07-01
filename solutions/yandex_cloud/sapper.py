# **Сапёр**
# Задача состоит из нескольких этапов:
# 1. написать функцию создания поля с минами. Задаем размеры поля, кол-во мин
# 2. расставить чиселки кол-ва мин в соседних клетках.
# 3. написать функцию, которая лавинно открывает клетки с 0 мин + их границы. В игре такое есть.
# ```
# import (
# "math/rand"
# )
# const MINE = -1
# Cons OPEN = -2
# func getMineField(field_width int, field_height int mines_count int): (*[][]int8, err) {
# if (field_width <= 0 || field_height <= 0) {
# return nil, errors.New("Wrong field size")
# }
# if mines_count <= 0 {
# return nil, errors.New("Field should have at least one mine")
# }
# field_size = field_width * field_height;
# if mines_count >= (field_size) - 1 {
# return nil, errors.New("Too many mines for field")
# }
# field := make([][]int8, field_width)
# mines_left := mines_count
# for i := 0; i< field_width; i++ {
# field[i] := make([]int8, field_height)
# }
# for mines_left > 0 {
# for i := 0; i< field_width && mines_left > 0; i++ {
# for j := 0; j< field_height && mines_left > 0; j++ {
# //0. 0.3 0.5 1.
# //10/100 = <0.1
# if rand.Float32() < ((float64)mines_count / (float64)(field_size)) {
# if field[i][j] != MINE {
# field[i][j] = MINE
# mines_left--;
# }
# }
# }
# }
# }
# return *field, nil
# }
# [1 2 3]
# [4 X 6]
# [7 8 9]
# func setCount(*[][]int8 array, width, height int) {
# for i := 0; i< width; i++ {
# for j := 0; j< height ; j ++ {
# if array[i][j] == MINE {
# // 1 2 3
# if i - 1 >= 0 && j - 1 >= 0 {
# if array[i-1][j-1] != MINE {
# array[i-1][j-1]++ // 1
# }
# }
# if i - 1 >= 0 {
# if array[i-1][j] != MINE {
# array[i-1][j]++ // 2
# }
# }
# if i - 1 >= 0 && j + 1 < heigth {
# if array[i-1][j+1] != MINE {
# array[i-1][j+1]++ // 3
# }
# }
# // 7 8 9
# if i + 1 < width && j - 1 >= 0 {
# if array[i+1][j-1] != MINE {
# array[i+1][j-1]++ // 7 }
# }
# if i + 1 < width{
# if array[i+1][j] != MINE {
# array[i+1][j]++ // 8
# }
# }
# if i + 1 < width && j + 1 < heigth {
# if array[i+1][j+1] != MINE {
# array[i+1][j+1]++ // 9
# }
# }
# // 4 6
# if j-1>= 0 {
# if array[i][j-1] != MINE {
# array[i][j-1]++ // 9
# }
# }
# if j + 1 <height {
# if array[i][j+1] != MINE {
# array[i][j+1]++ // 9
# }
# }
# }
# }
# }
# написать функцию, которая лавинно открывает клетки с 0 мин + их границы. В игре такое есть.
# // функция открывает все рядом ячейки принимает х у
# План действий
# If x y == mine { return true }
# Stack =
# Stack.append ( x, y)
# While stack.notempty()
# X, y = stack.pop()
# Stack.append([x+1, y])
# Stack.append([x-1, y])
# Stack.append([x, y-1])
# Stack.append([x, y+1])
# X y = OPEN
# }
# Type Struct point {
# Int x
# Int y
# }
# Func open(x, y int): bool { // true если ткнул в мину
# var stack []point
# }
# size_t maxOnes(const std::vector<int>& v);
# assert(maxOnes({0, 0}) == 0);
# assert(maxOnes({1, 0}) == 1);
# assert(maxOnes({0, 1}) == 1);
# assert(maxOnes({1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1}) == 5);
# assert(maxOnes({1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1}) == 6);
# # 0 1 0 1
# # 1 1
# # O(1) - память
# # O(n) - алгоритм
# def maxOnes(a) -> int:
# m: int = 0
# left: int = 0
# right: int = 0
# if len(a) == 1:
# return 0
# for i in range(len(a)):
# if a[i] == 1:
# right += 1
# if a[i] == 0:
# m = max(m, right + left)
# left = right
# right = 0
# if right == len(a):
# return len(a) - 1
# m = max(m, right + left)
# return m
