word1, word2, word3 = list(map(str, input().split()))


if word1 == "Нет" and word2 == "Нет" and word3 == "Нет":
    print("Кот")
if word1 == "Нет" and word2 == "Нет" and word3 == "Да":
    print("Жираф")
if word1 == "Нет" and word2 == "Да" and word3 == "Нет":
    print("Курица")
if word1 == "Нет" and word2 == "Да" and word3 == "Да":
    print("Страус")
if word1 == "Да" and word2 == "Нет" and word3 == "Нет":
    print("Дельфин")
if word1 == "Да" and word2 == "Нет" and word3 == "Да":
    print("Плезиозавры")
if word1 == "Да" and word2 == "Да" and word3 == "Нет":
    print("Пингвин")
if word1 == "Да" and word2 == "Да" and word3 == "Да":
    print("Утка")