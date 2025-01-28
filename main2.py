from database import SessionLocal, init_db
from services.book_service import BookService, ClientService, OrderService, PaymentService, AdminService


def main():
    init_db()
    db = SessionLocal()

    try:
        book_service = BookService(db)
        book_service.add_book(author='Дж. Д. Сэллинджер', book_name='Над пропастью во ржи', book_picture="book_pictures/TheCatcherInTheRye.jpg", price=800)
        book_service.add_book(author='Дж. Оруэл', book_name='1984', book_picture="book_pictures/1984.jpg", price=1000)
        book_service.add_book(author='Ф. Достоевский', book_name='Преступление и наказание', book_picture="book_pictures/CrimeAndPunishment.jpg", price=1500)
        book_service.add_book(author='Э. М. Ремарк', book_name='Три товарища', book_picture="book_pictures/3Friends.jpg", price=499)
        book_service.add_book(author='М. Твен', book_name='Приключения Гекльберри Финна', book_picture="book_pictures/adventure.jpeg", price=1200)
        book_service.add_book(author='Н. Гоголь', book_name='Мёртвые души', book_picture="book_pictures/DeadSouls.jpg", price=599)
        book_service.add_book(author='А. Рыбаков', book_name='Кортик', book_picture="book_pictures/Kortik.jpg", price=500)
        book_service.add_book(author='Э. М. Ремарк', book_name='Чёрный Обелиск', book_picture="book_pictures/BlackObelisc.jpg", price=800)
        book_service.add_book(author='Ф. Достоевский', book_name='Идиот', book_picture="book_pictures/Idiot.jpg", price=1199)
        book_service.add_book(author='Э. М. Ремарк', book_name='На западном фронте без перемен', book_picture="book_pictures/AllQuite.jpg", price=900)
        book_service.add_book(author='М. Твен', book_name='Приключения Тома Соера', book_picture="book_pictures/TomSoier.jpg", price=350)
        book_service.add_book(author='Н. Гоголь', book_name='Вий', book_picture="book_pictures/viy.jpg", price=700)
        book_service.add_book(author='С. Кинг', book_name='Зелёная миля', book_picture="book_pictures/GreenMile.jpg", price=400)
        book_service.add_book(author='Дж. Оруэл', book_name='Скотный двор', book_picture="book_pictures/SkotDvor.jpg", price=950)
        book_service.add_book(author='М. Пьюзо', book_name='Крестный отец', book_picture="book_pictures/father.jpg", price=800)
        book_service.add_book(author='А. Кристи', book_name='Десять негритят', book_picture="book_pictures/10niggers.jpg", price=1000)
        book_service.add_book(author='М. Булгаков', book_name='Мастери и Маргарита', book_picture="book_pictures/master.jpg", price=550)
        book_service.add_book(author='Г. Тропольский', book_name='Белый Бим Чёрное ухо', book_picture="book_pictures/whiteBim.jpg", price=200)
        book_service.add_book(author='В. Волков', book_name='Волшебник Изумрудного города', book_picture="book_pictures/magician.jpg", price=1000)
        book_service.add_book(author='Р. Брэдбери', book_name='451° по Фаренгейту', book_picture="book_pictures/451.jpg", price=900)
        book_service.add_book(author='Оскар Уайлд', book_name='Портрет Дориана Грея', book_picture="book_pictures/DorianGrey.jpg", price=700)
        book_service.add_book(author='А. Экзюпери', book_name='Маленький принц', book_picture="book_pictures/littleprince.jpg", price=600)
        book_service.add_book(author='Л. Толстой', book_name='Анна Каренина', book_picture="book_pictures/anna.jpg", price=400)
        book_service.add_book(author='Х. Ли', book_name='Убить пересмешника', book_picture="book_pictures/kill.jpg", price=1100)
        book_service.add_book(author='Е. Петров', book_name='Двенадцать стульев', book_picture="book_pictures/12chairs.jpg", price=250)
        book_service.add_book(author='А. Дюма', book_name='Граф Монте-Кристо', book_picture="book_pictures/monte-kristo", price=450)
        book_service.add_book(author='Ф. Фиджеральд', book_name='Великйи Гэтсби', book_picture="book_pictures/gatsby.jpg", price=1300)
        book_service.add_book(author='А. Пушкин', book_name='Евгений Онегин', book_picture="book_pictures/onegin.jpg", price=750)
        book_service.add_book(author='Ч. Паланик', book_name='Бойцовский клуб', book_picture="book_pictures/fightClub.jpg", price=500)
        book_service.add_book(author='М. Лермонтов', book_name='Герой нашего времени', book_picture="book_pictures/hero.jpg", price=300)
        book_service.add_book(author='М. Булгаков', book_name='Собачье сердце', book_picture="book_pictures/dog'sHeart", price=550)
        book_service.add_book(author='Э. Хемингуэй', book_name='Старик и море', book_picture="book_pictures/grandAndSea.jpg", price=350)
        book_service.add_book(author='А. Грибоедов', book_name='Горе от ума', book_picture="book_pictures/sad_from_knowledge.jpg", price=700)
        book_service.add_book(author='И. Гете', book_name='Фауст', book_picture="book_pictures/faust.jpg", price=650)
        book_service.add_book(author='И. Гончаров', book_name='Обломов', book_picture="book_pictures/oblomov.jpg", price=400)
        book_service.add_book(author='Г. Маркес', book_name='Сто лет одиночества', book_picture="book_pictures/100years.jpg", price=550)

        client_service = ClientService(db)
        client_service.add_client(client_name='Jeka_2004', phone_number=79145977429, password='321')
        client_service.add_client(client_name='ЭФИОП', phone_number=79216889023, password='3=d+8~-_&K^tk)')
        client_service.add_client(client_name='Vezzub', phone_number=79626447280, password=')enxlV)9-A$TX2')
        client_service.add_client(client_name='Крисси', phone_number=79265614969, password='C*-M7/QB>2>pQ/')
        client_service.add_client(client_name='AGRESSSIYA', phone_number=79690992148, password='-E0Lkq6s6T.cN2')
        client_service.add_client(client_name='Фаган', phone_number=79419635500, password='kusPYZ3b/-;=@+')
        client_service.add_client(client_name='Кот чучмек', phone_number=79823791711, password='!sxnSC-VCz5w4S')
        client_service.add_client(client_name='Лысая фея', phone_number=79953243123, password='_u4FOO6Sm{d-YZ')
        client_service.add_client(client_name='Moreee', phone_number=79169495493, password='BuKQz4-:gxU=g;')
        client_service.add_client(client_name='Axolotik', phone_number=79185255925, password='8!4K_UaBg14]C(')

        order_service = OrderService(db)
        order_service.add_order(client_name=1, book_name=7, address='ул. Мухина, д. 76, кв. 40', payment=1,
                                delivery_date='2024-11-30')

        payment_service = PaymentService(db)
        payment_service.add_payment(payment_status='Оплачен')
        payment_service.add_payment(payment_status='Не оплачен')

        admin_service = AdminService(db)
        admin_service.add_admin(login='Вова', password='123')
        admin_service.add_admin(login='Андрей', password='c$nWmbSF')
        admin_service.add_admin(login='Зюзя', password='xo?3ExaT')
        admin_service.add_admin(login='Никита', password='Bit~z~tW')
        admin_service.add_admin(login='Женя', password='Q#GdYLrW')

    finally:
        db.close()


if __name__ == '__main__':
    main()
