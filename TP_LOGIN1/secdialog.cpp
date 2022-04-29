#include "secdialog.h"
#include "ui_secdialog.h"
#include <QPixmap>
#include <QFile>
#include <QString>
#include <QTextStream>
#include <QTextEdit>
#include <QMessageBox>

SecDialog::SecDialog(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::SecDialog)
{
    ui->setupUi(this);
    QPixmap pix("../TP_LOGIN1/img/Meteo01.png"); // importation d'une image
    ui->label_images->setPixmap(pix.scaled(2000,250,Qt::KeepAspectRatio)); // Positionnez l'image dans un emploacemnt dédiée

    QString date =ui->lineEdit_saisie_date->text();
}

SecDialog::~SecDialog()
{
    delete ui;
}

void SecDialog::on_pushButton_temperature_clicked()
{

    QString ligne;
    QString mot;
    QString temperature_str;
    int compteur;

    QFile Releve_meteo("Releve_meteo.txt");
    QTextStream lecture_temperature(&Releve_meteo);

    if(!Releve_meteo.open(QFile::ReadOnly | QFile::Text))
    {
        //ui->plainTextEdit_affichage->setPlainText("Fichier ouvert");

        while (!lecture_temperature.atEnd())
        {
            for (compteur=0;compteur<29;compteur++)
            {
                ligne=lecture_temperature.readLine();

            }
            for (compteur=29;compteur<90;compteur++)
            {

            }
            ui->plainTextEdit_affichage->setPlainText(ligne);
        }


    }
    else
    {
        QMessageBox::warning(this,"Lecture","ERREUR : Impossible d'ouvrir le fichier !");
        ui->plainTextEdit_affichage->setPlainText("ERREUR : Impossible de lire le fichier");
    }







}

void SecDialog::on_pushButton_humidite_clicked()
{

}

void SecDialog::on_pushButton_vitesse_du_vent_clicked()
{

}

void SecDialog::on_pushButton_direction_du_vent_clicked()
{

}

void SecDialog::on_pushButton_quitter_clicked()
{

}
