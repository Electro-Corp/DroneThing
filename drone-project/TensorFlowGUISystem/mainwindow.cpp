/*
 * TENSORFLOW GUI
 * A program to simplify training and
 * testing AI models created with
 * Tensorflow.
 */
#include "mainwindow.h"
#include "ui_mainwindow.h"
//QT
#include <QFileDialog>
#include <QMessageBox>
// C++
#include <cstdlib>
#include <memory>
#include <stdexcept>
#include <string>
#include <array>
#include <iostream>
/*
 * PYTHON MAIN.py ARGS
 * python3 main.py iscustom istraining model_path checkpoint_path database_path minist Epochs
 */

std::string model_path;

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
}

MainWindow::~MainWindow()
{
    delete ui;
}
std::string exec(const char* cmd) {
    std::array<char, 128> buffer;
    std::string result;
    std::unique_ptr<FILE, decltype(&pclose)> pipe(popen(cmd, "r"), pclose);
    if (!pipe) {
        throw std::runtime_error("popen() failed!");
    }
    while (fgets(buffer.data(), buffer.size(), pipe.get()) != nullptr) {
        result += buffer.data();
    }
    return result;
}

void MainWindow::runMainpy(int iscustom, int istraining, std::string model_path_for, std::string checkpoint_path, int minist, int Epochs){

    std::string finalcommand = "python3 ~/DroneTHing/drone-project/TensorFlowGUISystem/tensorflow_engine/main.py ";
    finalcommand = finalcommand + std::to_string(iscustom) + " ";
    finalcommand = finalcommand + std::to_string(istraining)+ " ";
    finalcommand = finalcommand + model_path_for+ " ";
    finalcommand = finalcommand + checkpoint_path + " ";
    finalcommand = finalcommand + std::to_string(minist) + " ";
    finalcommand = finalcommand + std::to_string(Epochs) + " ";
    std::cout<<"EXECUTING.."<<std::endl;
    std::cout<<finalcommand << std::endl;
    //std::system(finalcommand.c_str());
    ui->output->setText(QString::fromStdString(exec(finalcommand.c_str())));

}
void MainWindow::on_test_model_clicked()
{
    //runMainpy(ui->radioButton_2->isChecked(),1,model_path,ui->checkpoint_path->text().toStdString(),ui->radioButton->isChecked());

}

void MainWindow::on_load_model_button_clicked()
{
    QString file1Name = QFileDialog::getOpenFileName(this,
             tr("Open Model"), "/home/$USERNAME", tr(""));
    ui->loaded_model_path->setText(file1Name);
    model_path = ui->loaded_model_path->text().toStdString();

}

void MainWindow::on_commandLinkButton_clicked()
{
    ui->output->setText("Please wait.. running command..");
    QMessageBox msgBox;
    msgBox.setText("You are about to train. This is a very resource intensive task, and you will see this application freeze while it is training. Press 'OK' to continue...");
    msgBox.exec();
    runMainpy(ui->radioButton_2->isChecked(),1,ui->saved_model_path->text().toStdString(),ui->checkpoint_path->text().toStdString(),ui->radioButton->isChecked(),ui->e_time->value());
}
