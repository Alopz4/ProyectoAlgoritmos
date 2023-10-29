import sqlite3

class Comunicacion():
  def __init__(self):
    self.conexion = sqlite3.connect('base_datos.db')
    
  
  def inserta_datos(self,Nombre, Asunto, Correo, Telefono, Fecha):
    cursor = self.conexion.cursor()
    bd = '''INSERT INTO pacientes (Nombre, Asunto, Correo, Telefono, Fecha)
    VALUES ('{}','{}', '{}','{}','{}')'''.format(Nombre, Asunto, Correo, Telefono, Fecha)
    cursor.execute(bd)
    self.conexion.commit()
    cursor.close()
    
    
  def mostrar_datos(self):
    cursor = self.conexion.cursor()
    bd = "SELECT * FROM pacientes "
    cursor.execute(bd)
    datos = cursor.fetchall()
    return datos
  
  def eliminar_datos(self, Nombre):
    cursor = self.conexion.cursor()
    bd = '''DELETE FROM pacientes WHERE Nombre = '{}' '''.format(Nombre)
    cursor.execute(bd)
    self.conexion.commit()
    cursor.close()
    
  def actualizar_datos(self,ID, Nombre, Asunto, Correo, Telefono, Fecha):
    cursor = self.conexion.cursor()
    bd = '''UPDATE pacientes SET Nombre = '{}', Asunto = '{}', Correo = '{}', Telefono = '{}',
    Fecha = '{}' WHERE ID = '{}' '''.format(Nombre, Asunto, Correo, Telefono, Fecha, ID)
    cursor.execute(bd)
    dato = cursor.rowcount
    self.conexion.commit()
    cursor.close()
    return dato