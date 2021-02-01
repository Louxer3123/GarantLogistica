import sqlite3
import logging

logger = logging.getLogger('FDataBase')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler('gl.log', encoding='utf-8')
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('[LINE:%(lineno)d]# %(asctime)s - %(levelname)s - %(name)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


class DataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def addUser(self, login, email, hash):
        try:
            self.__cur.execute(f"SELECT COUNT() as `count` FROM users WHERE login LIKE '{login}'")
            res = self.__cur.fetchone()
            if res['count'] > 0:
                logger.info("Пользователь с таким логином уже существует")
                return False

            self.__cur.execute("INSERT INTO users VALUES(NULL, ?, ?, ?)", (login, email, hash))
            self.__db.commit()
        except sqlite3.Error as e:
            logger.error("Ошибка добавления пользователя в БД " + str(e))
            return False

        return True

    def getUser(self, user_id):
        try:
            self.__cur.execute(f"SELECT * FROM users WHERE id = {user_id} LIMIT 1")
            res = self.__cur.fetchone()
            if not res:
                logger.info("Пользователь не найден")
                return False

            return res
        except sqlite3.Error as e:
            logger.error("Ошибка получения данных из БД " + str(e))

        return False

    def getUserByLogin(self, login):
        try:
            self.__cur.execute(f"SELECT * FROM users WHERE login = '{login}' LIMIT 1")
            res = self.__cur.fetchone()
            if not res:
                logger.info("Пользователь не найден")
                return False

            return res
        except sqlite3.Error as e:
            logger.error("Ошибка получения данных из БД " + str(e))

        return False

    def getNews(self, id_news):
        try:
            self.__cur.execute(f'SELECT title, text FROM articles WHERE id = {id_news} LIMIT 1')
            res = self.__cur.fetchone()
            if res:
                return res
        except sqlite3.Error as e:
            logger.error("Ошибка получения данных из БД " + str(e))

        return False

    def getAllNews(self):
        try:
            self.__cur.execute(f'SELECT id, title, text FROM articles')
            res = self.__cur.fetchall()
            if res:
                return res
        except sqlite3.Error as e:
            logger.error("Ошибка получения данных из БД " + str(e))

        return []

    def getCity(self):
        try:
            self.__cur.execute(f'SELECT name_city FROM city')
            res = self.__cur.fetchall()
            if res:
                return res
        except sqlite3.Error as e:
            logger.error("Ошибка получения данных из БД " + str(e))

        return []

    def addNewOrder(self, cityto, cityfrom, addressfrom, terminalfrom, addressto, terminalto, date, length, width,
                    height, weight, size, quantity, all_length, all_size, all_quantity, all_weight, all_width,
                    all_height, all_hard, doc_length, doc_height, doc_weight, transporations, goods, dop_uslugi, senders,
                    recipients, payment):
        try:
            self.__cur.execute(
                f'INSERT INTO orders VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                (
                    cityto, cityfrom, addressfrom, terminalfrom, addressto, terminalto, date, length, width, height,
                    weight,
                    size, quantity, all_length, all_size, all_quantity, all_weight, all_width, all_height, all_hard,
                    doc_length,
                    doc_height, doc_weight, transporations, goods, dop_uslugi, senders, recipients, payment))
            self.__db.commit()
        except sqlite3.Error as e:
            logger.error("Ошибка добавления заявки в БД " + str(e))
            return False

        return True
