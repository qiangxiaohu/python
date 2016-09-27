def main_setup():
    while True:
        main_running=input("您好，商城请选择1，ATM接口选择2，exit退出")
        while True:
            if main_running.isdigit:
                if main_running=='1':
                    main_shop=input("欢迎来到商城接口，购买商品请选择1，添加商品请按2，exit退出")
                    if main_shop.isdigit:
                        if main_shop=='1':
                            import shop
                            import ATM
                            shop.Mythred.show('xxx')
                            money = shop.Mythred.user_shop('xxx')
                            shop_money = ATM.atm_tired.show_atm('xxxx')
                            shop_money=int(shop_money)
                            shoping_money=shop_money-money
                            print("您已经购买了商品,余额为%s"%shoping_money)
                        if main_shop=='2':
                            import shop
                            shop.Mythred.add_shop('xxx')
                            continue
                    if main_shop=='exit':
                        break
                if main_running=='2':
                    main_atm = input("欢迎来到ATM接口，查询余额请选择1，存款请按2，取款请按3，exit退出")
                    if main_atm=='1':
                        import ATM
                        ATM.atm_tired.show_atm('xxxx')
                        continue
                    if main_atm=='2':
                        import ATM
                        ATM.atm_tired.deposit('xxxx')
                        continue
                    if main_atm=='3':
                        import ATM
                        ATM.atm_tired.draw('xxxx')
                        continue
                    if main_atm=='exit':
                        break
        if main_running=='exit':
            break
main_setup()