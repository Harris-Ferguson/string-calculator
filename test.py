from calculator import StringCalculator

calc = StringCalculator()

def test(input, expected):
  result = calc.Add(input)
  if(result == expected):
    print("Test input {} passed with expected output of {}".format(input, result))
  else:
    print("Test input {} failed, expected {} and got {}".format(input, expected, result))


# q1 tests
test("1,2,5", 8)
test("", 0)
test("1", 1)
test("100, 400, 200", 700)
# q2 tests
test("1\n,2,5", 8)
test("1,\n2,4", 7)
# q3 tests
test("//;\n1;3;4", 7)
test("//$\n1$2$3", 6)
test("//@\n2@3@8", 13)