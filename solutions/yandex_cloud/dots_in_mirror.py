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
