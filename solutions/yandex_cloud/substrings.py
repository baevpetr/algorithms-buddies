# **Подстроки**
# // Задана строка S из малых латинских букв, требуется узнать длину
# // наибольшей подстроки состоящей не более чем из двух различных символов.
# // word_le = 0
# // max(max, word_len)
# // wo -> wr
# // wowwwwwrod test abaabbba test
# func getMax(word string) int {
# max_len := 2
# word_len := len(word)
# if (word_len < 2) {
# return word_len
# }
# current_char1 := word[0]
# current_char2_not_set := true
# repeated_from := 0
# repeated_char := word[0]
# current_char2 := word[0]
# total_word_len = 0
# for i:=1; i < word_len; i++ {
# if current_char2_not_set {
# if word[i] == current_char1 {
# continue
# }
# current_char2 = word[i]
# current_char2_not_set = false
# repeated_from = i
# repeated_char = word[i]
# continue
# }
# if word[i] != current_char1 && word[i] != current_char2 {
# repeated_len := i - total_word_len
# total_word_len = repeated_from
# if current_char1 == repeated_char {
# current_char2 = word[i]
# } else {
# current_char1 = word[i]
# }
# if repeated_len > max_len {
# max_len = repeatedlen
# }
# }
# if word[i] != repeated_char {
# repeated_from = i
# repeated_char = word[i]
# }
# }
# repeated_len := len(word) - total_word_len
# if repeated_len > max_len {
# max_len = repeatedlen
# }
# return max_len
# }
# repeated_from = 0
# // ""
# // "w" - 1
# // "ww" - 2
# // "wa" - 2
# // "wac" - 2
# // "wacvghjyt" = 2
# // "wwaaaac" = 6
# // "acccc" = 5
# // "aaabddddd" = 6
