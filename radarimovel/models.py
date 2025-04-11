# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Agencias(models.Model):
    id_agencia = models.AutoField(db_column='ID_agencia', primary_key=True)  # Field name made lowercase.
    id_rede = models.ForeignKey('RedeAgencia', models.DO_NOTHING, db_column='ID_rede', blank=True, null=True)  # Field name made lowercase.
    id_localizacao = models.ForeignKey('Localizacao', models.DO_NOTHING, db_column='ID_localizacao', blank=True, null=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=100, blank=True, null=True)  # Field name made lowercase.
    morada = models.CharField(db_column='Morada', max_length=100, blank=True, null=True)  # Field name made lowercase.
    licenca_ami = models.IntegerField(db_column='Licenca_AMI')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'agencias'

    def __str__(self):
        return self.nome


class Angaria(models.Model):
    nifconsultor = models.OneToOneField('Consultores', models.DO_NOTHING, db_column='nifconsultor', primary_key=True)  # The composite primary key (nifconsultor, id_imovel) found, that is not supported. The first column is selected.
    id_imovel = models.ForeignKey('Imovel', models.DO_NOTHING, db_column='id_imovel')
    data_entrada = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'angaria'
        unique_together = (('nifconsultor', 'id_imovel'),)


class Consultores(models.Model):
    nifconsultor = models.CharField(db_column='nifConsultor', primary_key=True, max_length=11)  # Field name made lowercase.
    idagencia = models.ForeignKey(Agencias, models.DO_NOTHING, db_column='IdAgencia', blank=True, null=True)  # Field name made lowercase.
    nome = models.CharField(max_length=255, blank=True, null=True)
    telefone = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    landingpage = models.CharField(db_column='landingPage', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'consultores'

    def __str__(self):
        return self.nome


class Imovel(models.Model):
    id_imovel = models.AutoField(db_column='ID_Imovel', primary_key=True)  # Field name made lowercase.
    nifproprietario = models.ForeignKey('Proprietario', models.DO_NOTHING, db_column='NIFProprietario')  # Field name made lowercase.
    idlocalizacao = models.ForeignKey('Localizacao', models.DO_NOTHING, db_column='IDLocalizacao', blank=True, null=True)  # Field name made lowercase.
    tipo_de_imovel = models.CharField(db_column='Tipo_de_imovel', max_length=255)  # Field name made lowercase.
    tipologia = models.CharField(db_column='Tipologia', max_length=255)  # Field name made lowercase.
    morada = models.CharField(db_column='Morada', max_length=255)  # Field name made lowercase.
    codigo_postal = models.CharField(db_column='Codigo_postal', max_length=255)  # Field name made lowercase.
    preco_pedido = models.DecimalField(db_column='Preco_pedido', max_digits=12, decimal_places=0)  # Field name made lowercase.
    fotos = models.TextField(db_column='Fotos', blank=True, null=True)  # Field name made lowercase.
    area_m2 = models.IntegerField(blank=True, null=True)
    garagem_estacionamento = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'imovel'


class Localizacao(models.Model):
    id_localizacao = models.AutoField(db_column='ID_Localizacao', primary_key=True)  # Field name made lowercase.
    zona = models.CharField(db_column='Zona', max_length=255)  # Field name made lowercase.
    distrito = models.CharField(db_column='Distrito', max_length=255)  # Field name made lowercase.
    concelho = models.CharField(db_column='Concelho', max_length=255)  # Field name made lowercase.
    freguesia = models.CharField(db_column='Freguesia', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'localizacao'

    def __str__(self):
        return self.freguesia


class Proprietario(models.Model):
    nifproprietario = models.CharField(db_column='NIFProprietario', primary_key=True, max_length=11)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=255)  # Field name made lowercase.
    telefone = models.IntegerField(db_column='Telefone', blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'proprietario'

    def __str__(self):
        return self.nome


class RedeAgencia(models.Model):
    idrede = models.AutoField(db_column='IDRede', primary_key=True)  # Field name made lowercase.
    densocial = models.CharField(db_column='DenSocial', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rede_agencia'

    def __str__(self):
        return self.densocial
