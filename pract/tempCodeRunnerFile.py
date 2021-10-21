        rational = Rational(9, 45)
        print(rational.showData()) # 1/5
        print(rational.showPoint()) # 0.2

        zero = Rational(9, 0) # Zero division
        print(zero.showData()) # 1/2
        print(zero.showPoint()) # 0.5

        test = Rational(5, 55)
        print(test.showData()) # 1/11
        print(test.showPoint()) # 0.090909090909

        obj = rational + test
        print(obj.showData()) # 16/55

        obj /= zero
        print(obj.showData()) # 32/55