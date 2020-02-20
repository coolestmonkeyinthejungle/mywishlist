import mysql.connector as mdb
import ast

from wishlist.myui import Ui_MainWindow
from PyQt5 import QtGui, QtWidgets, QtCore


def converter(my_data):
    """Функция конвертации данных для дальнейшей подстановки в таблицу"""
    def cvt(data):
        try:
            return ast.literal_eval(data)
        except Exception:
            return str(data)

    return tuple(map(cvt, my_data))


class LineItemDelegate(QtWidgets.QStyledItemDelegate):
    """Делегат для создания LINE EDIT в ячейках таблицы"""
    cellEditingStarted = QtCore.pyqtSignal(int, int)

    def createEditor(self, parent, option, index):
        """Создание LINE EDIT в ячейке"""
        editor = QtWidgets.QLineEdit(parent)
        if index.column() == 1 or index.column() == 3:  # Задаем максимальную длину для имени и ссылки
            editor.setMaxLength(50)
        elif index.column() == 2:  # Создаем валидатор на целые числа для цены
            editor.setValidator(QtGui.QIntValidator())
        elif index.column() == 4:
            editor.setMaxLength(100)  # Задаем максимальную длину для примечания
        if editor:
            self.cellEditingStarted.emit(index.row(), index.column())
        return editor

    def setEditorData(self, editor, index):
        """Заносим данные в поле LINE EDIT"""
        editor.setText(index.data())

    def setModelData(self, editor, model, index):
        """Отображение введеных данных в ячейках"""
        value = editor.text()
        model.setData(index, value)


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        """Конструктор класса, в котором мы подгружаем даннные с файла, созданном в QtDesigner,
         а также дополнительно настраиваем  виджеты в главном окне и создаем подключение к БД"""
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.style_ui()
        self.database_connection()


    def style_ui(self):
        """Дополнительно настраиваем виджеты в окне"""
        self.column_label = ['id', 'Название', 'Цена', 'Ссылка', 'Примечание']
        self.column_name = ['id', 'name', 'price', 'link', 'comment']
        self.column_dict = {self.column_label[i]: self.column_name[i] for i in range(len(self.column_label))}
        self.ui.tableWidget.setHorizontalHeaderLabels(self.column_label)
        self.ui.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.ui.tableWidget.setColumnHidden(0, True)
        header = self.ui.tableWidget.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.start = 0
        self.delegate = LineItemDelegate(self)
        self.delegate.cellEditingStarted.connect(self.start_edit)
        self.ui.tableWidget.setItemDelegate(self.delegate)
        self.ui.tableWidget.cellChanged.connect(self.end_edit)
        self.ui.saveButton.clicked.connect(self.save_clicked)
        self.ui.deleteButton.clicked.connect(self.delete_clicked)
        self.ui.priceEdit.setValidator(QtGui.QIntValidator())
        self.ui.nameEdit.setMaxLength(50)
        self.ui.linkEdit.setMaxLength(100)
        self.ui.commentEdit.setAcceptRichText(False)
        self.ui.commentEdit.textChanged.connect(self.text_input_changed)

    def database_connection(self):
        """Настраиваем и проверяем подключение к БД"""
        self.con = mdb.connect(host='mysqldev', port=3306, user='user', passwd='password', database='mywishlist')
        if self.con.is_connected():
            self.cur = self.con.cursor()
            self.cur.execute("CREATE TABLE IF NOT EXISTS wishes("  # Создаем нашу БД, если она еще не создана
                             "id int NOT NULL auto_increment," 
                             "name varchar(50) NOT NULL,"
                             "price int(10) NOT NULL,"
                             "link varchar(50),"
                             "comment varchar(100),"
                             "PRIMARY KEY (id))")
            self.load_data()
        else:
            self.show_error_message()

    def start_edit(self):
        """Проверка на то, начал ли пользователь изменение ячейки в таблице"""
        self.start = 1
        column = self.ui.tableWidget.currentItem().column()
        if column == 1:
            self.previous_item = self.ui.tableWidget.currentItem().text()  # Записываем предыдущее значение
            # для подстановки в случае введенного пустого значения имени

    def end_edit(self):
        """Проверка на то, закончил ли пользователь изменения в таблице"""
        if self.start == 1:  # Проверка условия на начало изменения ячеек пользователем, а не программой
            row = self.ui.tableWidget.currentItem().row()
            column = self.ui.tableWidget.currentItem().column()
            if column == 1 and not self.ui.tableWidget.currentItem().text():  # Проверка вводит ли пользователь пустое
                # значение вместо имени
                self.show_warning_message()
                item = QtWidgets.QTableWidgetItem(self.previous_item)  # Возвращаем значение до введенного пустого
                self.ui.tableWidget.setItem(row, column, item)
            id_item = self.ui.tableWidget.item(row, 0).text()
            data = self.ui.tableWidget.currentItem().text()
            current_column_label = self.ui.tableWidget.horizontalHeaderItem(column).text()
            current_column_name = self.column_dict[current_column_label]
            self.update_data(current_column_name, id_item, data)
        self.start = 0

    def save_clicked(self):
        """Функция вызываемая при нажатии пользователем на кнопку сохранить"""
        name_value = self.ui.nameEdit.text()
        price_value = self.ui.priceEdit.text()
        if name_value and price_value:
            link_value = self.ui.linkEdit.text()
            comment_value = self.ui.commentEdit.toPlainText()
            params = (name_value, price_value, link_value, comment_value)
            self.insert_data(params)
            self.load_data(" ORDER BY id DESC LIMIT 1")
        else:
            self.show_warning_message()

    def insert_data(self, params):
        """Функция для вставки данных в БД"""
        query = "INSERT INTO wishes(name,price,link,comment) VALUES(%s,%s,%s,%s)"
        self.cur.execute(query, params)
        self.con.commit()

    def load_data(self, options=""):
        """Загрузка данных из БД"""
        self.cur.execute("SELECT * FROM wishes" + options)
        result = self.cur.fetchall()
        for row in result:
            self.add_to_table(converter(row))

    def add_to_table(self, columns):
        """Добавление данных в таблицу"""
        row_position = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.insertRow(row_position)
        for i, column in enumerate(columns):
            item = QtWidgets.QTableWidgetItem(str(column))
            self.ui.tableWidget.setItem(row_position, i, item)

    def delete_clicked(self):
        """Функция вызываемая при нажатии пользователем на кнопку удалить"""
        rows = self.ui.tableWidget.selectionModel().selectedRows()
        del_rows = 0
        for r in rows:
            id_item = self.ui.tableWidget.item(r.row() - del_rows, 0)
            self.delete_data(id_item.text())
            self.ui.tableWidget.removeRow(r.row() - del_rows)
            del_rows += 1

    def delete_data(self, id_item):
        """Удаление данных из БД"""
        query = "DELETE FROM wishes WHERE id = %s"
        self.cur.execute(query, (id_item,))
        self.con.commit()

    def update_data(self, current_column_name, id_item, data):
        """Изменение данных в БД"""
        params = (data, id_item)
        query = "UPDATE wishes SET {} = %s WHERE id = %s".format(current_column_name)
        self.cur.execute(query, params)
        self.con.commit()

    def text_input_changed(self):
        """Функция вызывааемая при изменении TEXT EDIT  пользователем
        и проверяющая не превышает ли текущая длина текста максимальное значение """
        max_input_len = 100
        if len(self.ui.commentEdit.toPlainText()) > max_input_len:  # Проверяем текущую длину текста
            text = self.ui.commentEdit.toPlainText()
            text = text[:max_input_len]
            print(len(text), text)
            self.ui.commentEdit.setPlainText(text)  # Если текст больше максимаьной длины то обрезаем его и возвращаем
            # курсор
            cursor = self.ui.commentEdit.textCursor()
            cursor.setPosition(max_input_len)
            self.ui.commentEdit.setTextCursor(cursor)

    def closeEvent(self, event):
        """Событие при закрытиии программы. Закрываем соединение с БД"""
        try:
            self.cur.close()
            self.con.close()
        except Exception:
            pass

    def show_warning_message(self):
        """Вызов сообщения о предупреждении"""
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        msg.setText("Имя и цена не должны быть пустыми!")
        msg.setWindowTitle("Неверно")
        msg.exec_()

    def show_error_message(self):
        """Вызов сообщения об ошибке"""
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setText("Ошибка подключения к БД!")
        msg.setWindowTitle("Ошибка")
        msg.buttonClicked.connect(self.closeEvent)
        msg.exec_()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainApp = MyWindow()
    MainApp.show()
    sys.exit(app.exec_())
