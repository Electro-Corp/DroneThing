#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <string>
#include <iostream>
namespace Ui {
class MainWindow;
}

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit MainWindow(QWidget *parent = 0);
    ~MainWindow();

private slots:
    void on_test_model_clicked();
    /*
     * PYTHON MAIN.pY ARGS
     * python3 main.py iscustom istraining model_path checkpoint_path
     *
     */
    void runMainpy(int iscustom, int istraining, std::string model_path, std::string checkpoint_path, int minist, int Epochs);
    void on_load_model_button_clicked();

    void on_commandLinkButton_clicked();

private:
    Ui::MainWindow *ui;
};

#endif // MAINWINDOW_H
