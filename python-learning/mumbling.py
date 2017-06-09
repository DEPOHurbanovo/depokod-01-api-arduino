def accum(s):
  string = ""
  counter = 1
  for character in s:
    if counter != 1:
      string += "-"

    for i in range(0, counter):
      string = string + (character.upper() if i == 0 else character.lower())

    counter += 1
    print(character)
  return string


print(accum("ZpglnRxqenU"))