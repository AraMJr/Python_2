
counter = 1     # global counter


# test function takes an output and checks it against a single or list of expected outputs. default expected is None
def test(actual, expected=None, subtest=False):
    global counter  # global test number
    boolean = False  # whether test passed
    try:
        if type(expected) is not list and expected is not None:
            expected = [expected]
        if not subtest:
            print(f"test {counter} -> ", end="")
        try:
            if (actual is None and expected is None) or (actual in expected):
                if not subtest:
                    print("passed")
                boolean = True
            else:
                if not subtest:
                    print("failed\t[ actual { " + str(actual) + " }  expected { " + str(*expected) + " } ] ")
        except TypeError:
            if not subtest:
                print("failed\t[ actual { " + str(actual) + " }  expected { " + str(expected) + " } ] ")
    except Exception:
        boolean = False
        if not subtest:
            print("failed\t[ encountered error ] ")
    counter += 1
    return counter - 1, boolean


if __name__ == "__main__":
    # testing the tests ;)
    test(test("output", "output", True), (counter-1, True))
    test(test("output", "error", True), (counter-1, False))
    test(test(None, subtest=True), (counter-1, True))
    test(test(24, 24, True), (counter-1, True))
    test(test(3.45, 3.45, True), (counter-1, True))
    test(test(True, True, True), (counter-1, True))
    test(test(True, False, True), (counter-1, False))

