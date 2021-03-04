from fibo import do_fibo
if __name__=='__main__':
    user_num = int(input('Type any positive integer: '))
    result = do_fibo(user_num)

    print(f"치킨을 {result}마리 주문하세요. 맥주는 {result*500}ml가 적당해 보이네요.")
