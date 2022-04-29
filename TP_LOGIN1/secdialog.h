#ifndef SECDIALOG_H
#define SECDIALOG_H

#include <QDialog>

namespace Ui {
class SecDialog;
}

class SecDialog : public QDialog
{
    Q_OBJECT

public:
    explicit SecDialog(QWidget *parent = nullptr);
    ~SecDialog();

private slots:
    void on_pushButton_temperature_clicked();

    void on_pushButton_humidite_clicked();

    void on_pushButton_vitesse_du_vent_clicked();

    void on_pushButton_direction_du_vent_clicked();

    void on_pushButton_quitter_clicked();

private:
    Ui::SecDialog *ui;
};

#endif // SECDIALOG_H
