"""
Разработать класс SuperStr, который наследует
функциональность стандартного типа str и содержит два
новых метода:
● метод is_repeatance(s), который принимает некоторую
строку и возвращает True или False в зависимости от того,
может ли текущая строка быть получена целым
количеством повторов строки s. Считать, что пустая
строка не содержит повторов
● метод is_palindrom(), который возвращает True или False в
зависимости от того, является ли строка палиндромом вне
зависимости от регистра. Пустую строку считать
палиндромом.
"""


class SuperStr(str):
    def is_repeating(self, s):
        if len(self) != 0:
            return self.replace(s, '') == ''
        return False

    def is_palindrome(self):
        return self.lower() == self[::-1].lower()


str1 = SuperStr("abaaba")
str2 = SuperStr("abracadabra")
str_s = "aba"

print(str1.is_repeating(str_s))
print(str2.is_repeating(str_s))

print(str1.is_palindrome())
print(str2.is_palindrome())
