from django.db import models

# Create your models here.

class BusinessUnit(models.Model):
    # 事业部

    name = models.CharField(max_length=20,verbose_name='名称')


    class Meta:
        db_table ='businessunit'
        verbose_name = '事业部门'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Environment(models.Model):

    # 环境
    name = models.CharField(max_length=20,verbose_name='名称')
    to_b = models.ForeignKey(to=BusinessUnit, on_delete=models.CASCADE,default=1)

    def __str__(self):
        return "%s|%s"%(self.id,self.name)


    class Meta:
        db_table = 'environment'
        verbose_name = '环境类型'
        verbose_name_plural = verbose_name


class RecordingTime(models.Model):

    pub_date = models.DateField(verbose_name='历史⽇期')

    class Meta:
        db_table = 'recordingtime'

    def __str__(self):
        return str(self.pub_date)

class IpInfo(models.Model):
    # ip信息
    TYPE_CHOICES = (
        (0, '虚拟机'),
        (1, '物理机')
    )
    TYPE_CHOICES2 = (
        (0, 'service'),
        (1, 'big_data')
    )

    name = models.CharField(max_length=20, verbose_name='ip名称')

    memorytotal = models.IntegerField(verbose_name='内存总量')

    memoryuse = models.IntegerField(verbose_name='内存使用量')

    memoryrate = models.CharField(max_length=18, verbose_name='内存使用率')

    cpucore = models.IntegerField(default=4, verbose_name='cpu核数量')

    averageload = models.DecimalField(max_digits=6,decimal_places=3,verbose_name='平均load值')

    cpurate = models.CharField(max_length=10,verbose_name='cpu使用率',default='0')

    disktotal = models.DecimalField(max_digits=18,decimal_places=1,verbose_name='磁盘总量')

    diskrate = models.CharField(max_length=10, verbose_name='硬盘使用率')

    diskuse = models.DecimalField(max_digits=18,decimal_places=1,verbose_name='磁盘使用量')

    servertype = models.SmallIntegerField(choices=TYPE_CHOICES, default=0, verbose_name='类型')

    env = models.ForeignKey(Environment, on_delete=models.CASCADE, verbose_name='环境')      # 外键

    times = models.ForeignKey(RecordingTime, on_delete=models.CASCADE, verbose_name='时间')  # 外键

    type = models.SmallIntegerField(choices=TYPE_CHOICES2, default=0, verbose_name='服务器类型')

    class Meta:

        db_table = 'ipinfo'


class AllData(models.Model):

    # 图表展示数据
    TYPE_CHOICES = (
        (0, 'service'),
        (1, 'big_data')
    )
    type = models.SmallIntegerField(choices=TYPE_CHOICES, default=0, verbose_name='服务类型')

    memorytotal = models.IntegerField(verbose_name='内存总量')

    memoryuse = models.IntegerField(verbose_name='内存使用量',default=0)

    memoryrate = models.CharField(max_length=10,verbose_name='内存使用率')

    disktotal = models.DecimalField(max_digits=10,decimal_places=1,verbose_name='硬盘总量')

    diskuse = models.IntegerField(verbose_name='硬盘使用量',default=0)

    diskrate = models.CharField(max_length=10,verbose_name='硬盘使用率')

    env = models.ForeignKey(Environment, on_delete=models.CASCADE, verbose_name='环境')

    time = models.ForeignKey(RecordingTime, on_delete=models.CASCADE, verbose_name='时间')

    class Meta:

        db_table = 'alldata'

class IpConfig(models.Model):
    TYPE_CHOICES = (
        (0, 'service'),
        (1, 'big_data')
    )
    TYPE_CHOICES2 = (
        (0, '虚拟机'),
        (1, '物理机')
    )
    ip = models.CharField(max_length=20,verbose_name='ip名称')
    type = models.SmallIntegerField(choices=TYPE_CHOICES, default=0, verbose_name='服务器类型')
    env = models.ForeignKey(Environment,on_delete=models.CASCADE, verbose_name='环境')
    servertype = models.SmallIntegerField(choices=TYPE_CHOICES2, default=0, verbose_name='类型')


    class  Meta:
        db_table = 'ipconfig'
        verbose_name = 'IP配置'
        verbose_name_plural = verbose_name


