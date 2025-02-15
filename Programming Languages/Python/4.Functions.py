def func(abc):
    try:
        for i in range(int(abc)):
            print("I am the best all i have to do is try",i)
    except TypeError as e:
        print(f"Please use number{e}")
    except ValueError as e:
        print(f"Value Error{e}")
    finally:
        print("Done executed lol") 

func(123)
func("1221")
func("abc")