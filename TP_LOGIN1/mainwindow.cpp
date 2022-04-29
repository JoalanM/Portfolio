#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QMessageBox>
#include <QPixmap>

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    QPixmap pix("../TP_LOGIN1/img/blog-wp-login.png");
    ui->label_IMAGE->setPixmap(pix.scaled(4000,100,Qt::KeepAspectRatio));
}

MainWindow::~MainWindow()
{
    delete ui;
}


void MainWindow::on_pushButton_connexion_clicked()
{
    QString identifiant = ui->lineEdit_identifiant->text();
    QString mot_de_passe = ui->lineEdit_mot_de_passe->text();

    if(identifiant == "MYRTIL" && mot_de_passe == "admin")
    {
        QMessageBox::information(this, "Connexion", "Connexion réussite ");
        hide();
        secDialog = new SecDialog(this);
        secDialog->show();
    }
    else
    {
        QMessageBox::warning(this,"Connexion", "Identifiant et/ou mot de passe incorrect");
    }
}
