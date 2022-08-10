#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <iostream>
#include <thread>
#include <string>


MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{


    ui->setupUi(this);
    std::string path = "test";
//    std::cout<<"Creating Thread.."<<std::endl;
//    std::thread imageThread(&MainWindow::refresh_image_thread,this);
//    this_thread::sleep_for(2s);
//    std::cout<<"Waited.."<<std::endl;


//    imageThread.join();
//    std::cout<<"Joined Thread.."<<std::endl;

}

MainWindow::~MainWindow()
{
    delete ui;
}
void MainWindow::refresh_image_thread(void){
    std::cout<<"Thread is here"<<std::endl;
    while (true){

        ui->label->setText(QString::fromStdString("bruh"));
    }

}
