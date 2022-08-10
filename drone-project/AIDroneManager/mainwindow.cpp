#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <iostream>
#include <thread>
#include <string>
#include <QGraphicsScene>
#include <QGraphicsView>
#include <QGraphicsPixmapItem>

QGraphicsScene *m_graphicsScene;

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    m_graphicsScene = new QGraphicsScene(this);
    ui->graphicsView->setScene(m_graphicsScene);


    ui->setupUi(this);
    std::string path = "test";
    refresh_image_thread();


}

MainWindow::~MainWindow()
{

    delete ui;
}
void MainWindow::refresh_image_thread(void){
    m_graphicsScene->clear();
    QImage image("../connection/images/recived15.jpg");
    QGraphicsPixmapItem* item = new QGraphicsPixmapItem(QPixmap::fromImage(image));
    item->setPos(0,0);
    item->setScale(1);
    m_graphicsScene->addItem(item);

}
