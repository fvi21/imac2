from django.db import models
from core.models import Pacientes

# Create your models here.

class Antecedentes(models.Model):
    id_antecedentes=models.AutoField(primary_key=True)
    paciente_antecedente=models.OneToOneField(Pacientes,on_delete=models.CASCADE,null=True)
    fcrv_hta = models.BooleanField(default=False, null=True )
    fcrv_dta = models.BooleanField(default=False, null=True )
    fecha_fcrv_hta = models.DateField(null = True)
    fecha_fcrv_dta = models.DateField(null = True)
    anteced_fliar = models.BooleanField(default=False, null=True)
    dislipemia = models.BooleanField(default=False, null=True)
    estres = models.BooleanField(default=False, null=True)
    tabaquismo = models.BooleanField(default=False, null=True )
    ex_tabaquismo = models.BooleanField(default=False, null=True )
    sedentarismo = models.BooleanField(default=False, null=True)
    chagas = models.BooleanField(default=False, null=True)
    marcapasos = models.BooleanField(default=False, null=True)
    resincron = models.BooleanField(default=False, null=True)
    cdi = models.BooleanField(default=False, null=True )
    crm_hta = models.BooleanField(default=False, null=True)
    fecha_crm_hta = models.DateTimeField(null = True)
    pm = models.BooleanField(default=False, null=True)
    pm_da = models.BooleanField(default=False, null=True)
    pm_dg = models.BooleanField(default=False, null=True)
    pm_cx = models.BooleanField(default=False, null=True)
    pr = models.BooleanField(default=False, null=True)
    pr_dg = models.BooleanField(default=False, null=True)
    pr_cx = models.BooleanField(default=False, null=True)
    pv = models.BooleanField(default=False, null=True)
    pv_da = models.BooleanField(default=False, null=True)
    pv_dg = models.BooleanField(default=False, null=True)
    pv_cx = models.BooleanField(default=False, null=True)
    infarto = models.BooleanField(default=False, null=True)
    fecha_infarto_reciente = models.DateField(null = True)
    atc1 = models.BooleanField(default=False, null=True)
    atc1_da = models.BooleanField(default=False, null=True)
    atc1_dg = models.BooleanField(default=False, null=True)
    atc1_cx = models.BooleanField(default=False, null=True)
    atc1_cd = models.BooleanField(default=False, null=True)
    atc1_stent_bms = models.BooleanField(default=False, null=True)
    atc1_stent_des = models.BooleanField(default=False, null=True)
    atc2 = models.BooleanField(default=False, null=True)
    atc2_da = models.BooleanField(default=False, null=True)
    atc2_dg = models.BooleanField(default=False, null=True)
    atc2_cx = models.BooleanField(default=False, null=True)
    atc2_cd = models.BooleanField(default=False, null=True)
    atc2_stent_bms = models.BooleanField(default=False, null=True)
    atc2_stent_des = models.BooleanField(default=False, null=True)
    atc3 = models.BooleanField(default=False, null=True)
    atc3_da = models.BooleanField(default=False, null=True)
    atc3_dg = models.BooleanField(default=False, null=True)
    atc3_cx = models.BooleanField(default=False, null=True)
<<<<<<< HEAD
    atc3_cd = models.BooleanField(default=False, null=True)
=======
    atc2_cd = models.BooleanField(default=False, null=True)
>>>>>>> 7927276fd1b2c4dd6dc819fd275d3e6d654cb1e2
    atc3_stent_bms = models.BooleanField(default=False, null=True)
    atc3_stent_des = models.BooleanField(default=False, null=True)
    otros_antecedentes = models.TextField(null = True)

class Meta: #aplicando un metodo para que pase a español en el admin del framework
        verbose_name= "Antecedente"#aca los paso al español en singular
        verbose_name_plural="Antecedentes"#aca los paso al español en prural
        ordering = ["created"] #con esta funcion puedo ordenar los objetos a medida que los creo
    
