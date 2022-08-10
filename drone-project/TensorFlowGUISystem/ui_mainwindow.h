/********************************************************************************
** Form generated from reading UI file 'mainwindow.ui'
**
** Created by: Qt User Interface Compiler version 5.9.5
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAINWINDOW_H
#define UI_MAINWINDOW_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QCommandLinkButton>
#include <QtWidgets/QGroupBox>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QRadioButton>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QTextBrowser>
#include <QtWidgets/QToolBar>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QWidget *centralWidget;
    QLabel *label;
    QGroupBox *load_model_group;
    QLabel *loaded_model_path;
    QCommandLinkButton *load_model_button;
    QGroupBox *groupBox;
    QRadioButton *radioButton;
    QRadioButton *radioButton_2;
    QGroupBox *groupBox_2;
    QGroupBox *groupBox_3;
    QLabel *Saved_model_path_label;
    QLineEdit *saved_model_path;
    QLabel *label_2;
    QLineEdit *checkpoint_path;
    QCommandLinkButton *commandLinkButton;
    QGroupBox *groupBox_4;
    QCommandLinkButton *test_model;
    QTextBrowser *output;
    QMenuBar *menuBar;
    QToolBar *mainToolBar;
    QStatusBar *statusBar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QStringLiteral("MainWindow"));
        MainWindow->resize(1287, 836);
        centralWidget = new QWidget(MainWindow);
        centralWidget->setObjectName(QStringLiteral("centralWidget"));
        label = new QLabel(centralWidget);
        label->setObjectName(QStringLiteral("label"));
        label->setGeometry(QRect(10, 30, 801, 51));
        load_model_group = new QGroupBox(centralWidget);
        load_model_group->setObjectName(QStringLiteral("load_model_group"));
        load_model_group->setGeometry(QRect(10, 90, 241, 121));
        loaded_model_path = new QLabel(load_model_group);
        loaded_model_path->setObjectName(QStringLiteral("loaded_model_path"));
        loaded_model_path->setGeometry(QRect(10, 30, 221, 17));
        load_model_button = new QCommandLinkButton(load_model_group);
        load_model_button->setObjectName(QStringLiteral("load_model_button"));
        load_model_button->setGeometry(QRect(50, 70, 177, 31));
        groupBox = new QGroupBox(centralWidget);
        groupBox->setObjectName(QStringLiteral("groupBox"));
        groupBox->setGeometry(QRect(10, 220, 541, 331));
        radioButton = new QRadioButton(groupBox);
        radioButton->setObjectName(QStringLiteral("radioButton"));
        radioButton->setGeometry(QRect(10, 40, 241, 23));
        radioButton_2 = new QRadioButton(groupBox);
        radioButton_2->setObjectName(QStringLiteral("radioButton_2"));
        radioButton_2->setGeometry(QRect(10, 70, 221, 23));
        groupBox_2 = new QGroupBox(groupBox);
        groupBox_2->setObjectName(QStringLiteral("groupBox_2"));
        groupBox_2->setGeometry(QRect(240, 30, 281, 161));
        groupBox_3 = new QGroupBox(groupBox);
        groupBox_3->setObjectName(QStringLiteral("groupBox_3"));
        groupBox_3->setGeometry(QRect(20, 190, 511, 121));
        Saved_model_path_label = new QLabel(groupBox_3);
        Saved_model_path_label->setObjectName(QStringLiteral("Saved_model_path_label"));
        Saved_model_path_label->setGeometry(QRect(10, 30, 131, 17));
        saved_model_path = new QLineEdit(groupBox_3);
        saved_model_path->setObjectName(QStringLiteral("saved_model_path"));
        saved_model_path->setGeometry(QRect(140, 30, 271, 25));
        label_2 = new QLabel(groupBox_3);
        label_2->setObjectName(QStringLiteral("label_2"));
        label_2->setGeometry(QRect(10, 70, 131, 17));
        checkpoint_path = new QLineEdit(groupBox_3);
        checkpoint_path->setObjectName(QStringLiteral("checkpoint_path"));
        checkpoint_path->setGeometry(QRect(140, 70, 271, 25));
        commandLinkButton = new QCommandLinkButton(groupBox);
        commandLinkButton->setObjectName(QStringLiteral("commandLinkButton"));
        commandLinkButton->setGeometry(QRect(20, 100, 201, 41));
        groupBox_4 = new QGroupBox(centralWidget);
        groupBox_4->setObjectName(QStringLiteral("groupBox_4"));
        groupBox_4->setGeometry(QRect(270, 100, 201, 111));
        test_model = new QCommandLinkButton(groupBox_4);
        test_model->setObjectName(QStringLiteral("test_model"));
        test_model->setGeometry(QRect(10, 40, 177, 41));
        output = new QTextBrowser(centralWidget);
        output->setObjectName(QStringLiteral("output"));
        output->setGeometry(QRect(570, 20, 681, 751));
        MainWindow->setCentralWidget(centralWidget);
        menuBar = new QMenuBar(MainWindow);
        menuBar->setObjectName(QStringLiteral("menuBar"));
        menuBar->setGeometry(QRect(0, 0, 1287, 22));
        MainWindow->setMenuBar(menuBar);
        mainToolBar = new QToolBar(MainWindow);
        mainToolBar->setObjectName(QStringLiteral("mainToolBar"));
        MainWindow->addToolBar(Qt::TopToolBarArea, mainToolBar);
        statusBar = new QStatusBar(MainWindow);
        statusBar->setObjectName(QStringLiteral("statusBar"));
        MainWindow->setStatusBar(statusBar);

        retranslateUi(MainWindow);

        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QApplication::translate("MainWindow", "CT Tensorflow model Manager", Q_NULLPTR));
        label->setText(QApplication::translate("MainWindow", "<html><head/><body><p><span style=\" font-size:26pt;\">Tensorflow models Manage GUI </span></p></body></html>", Q_NULLPTR));
        load_model_group->setTitle(QApplication::translate("MainWindow", "Load Model", Q_NULLPTR));
        loaded_model_path->setText(QString());
        load_model_button->setText(QApplication::translate("MainWindow", "Load model", Q_NULLPTR));
        groupBox->setTitle(QApplication::translate("MainWindow", "Train Model", Q_NULLPTR));
        radioButton->setText(QApplication::translate("MainWindow", "Use MINIST Fashion Database", Q_NULLPTR));
        radioButton_2->setText(QApplication::translate("MainWindow", "Use custom", Q_NULLPTR));
        groupBox_2->setTitle(QApplication::translate("MainWindow", "Custom", Q_NULLPTR));
        groupBox_3->setTitle(QApplication::translate("MainWindow", "All", Q_NULLPTR));
        Saved_model_path_label->setText(QApplication::translate("MainWindow", "Saved Model path: ", Q_NULLPTR));
        saved_model_path->setText(QApplication::translate("MainWindow", "/home/$USERNAME/", Q_NULLPTR));
        label_2->setText(QApplication::translate("MainWindow", "Checkpoint paths: ", Q_NULLPTR));
        checkpoint_path->setText(QApplication::translate("MainWindow", "/home/%USERNAME", Q_NULLPTR));
        commandLinkButton->setText(QApplication::translate("MainWindow", "Train model based on data", Q_NULLPTR));
        groupBox_4->setTitle(QApplication::translate("MainWindow", "Test model", Q_NULLPTR));
        test_model->setText(QApplication::translate("MainWindow", "Test Model", Q_NULLPTR));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H
