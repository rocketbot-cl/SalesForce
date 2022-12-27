



# Salesforce
  
Interactuar con el ecosistema de Salesforce.  
  
![banner](imgs/Banner_Salesforce.png)
## Como instalar este módulo
  
__Descarga__ e __instala__ el contenido en la carpeta 'modules' en la ruta de Rocketbot.  




## Como usar este modulo
  
Antes de usar este módulo, necesitará de SalesForce:

 * Username.
 * Password.
 * Consumer Key (se obtiene de App Manager | Setup -> App Manager -> "Ver" su aplicación API).
 * Consumer Secret (se obtiene de App Manager | Setup -> App Manager -> "Ver" su aplicación API).
 * Security Token (se obtiene de My Personal Information | Profile -> Settings -> Resetear My Security Token).


## Descripción de los comandos

### Conectar a Salesforce
  
Conectar tu cuenta de Salesforce
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Username||usuario|
|Password||********|
|client_id||3MVG9ayzKZt5EleHsI9aFM|
|client_secret||E6F1E861EED2E92DB0DA70131307C738D91|
|token||4Tl3VbIRSYMNTs4|
|domain||rocketbot.my|
|Asignar resultado a variable||Variable|

### Obtener lista de recursos
  
Obtiene la lista de recursos de Salesfroce
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Asignar resultado a variable||Variable|

### Obtener lista de objetos
  
Obtiene la lista de objetos de Salesfroce
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Recurso a utilizar||sobjects|
|Asignar resultado a variable||Variable|

### Obtener metadata
  
Obtiene metadata de objetos de Salesfroce
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Recurso a utilizar||sobjects|
|Objeto a utilizar||Account|
|Asignar resultado a variable||Variable|

### Crear un registro
  
Permite crear un registro en SalesForce
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Recurso a utilizar||sobjects|
|Objeto a utilizar||Account|
|Datos para asignar al registro||data|
|Asignar resultado a variable||Variable|

### Modificar un registro
  
Permite modificar un registro en SalesForce
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Recurso a utilizar||sobjects|
|Objeto a utilizar||Account|
|Registro a modificar||001D000000INjVe|
|Datos para asignar al registro||data|
|Asignar resultado a variable||Variable|

### Eliminar un registro
  
Permite eliminar un registro en SalesForce
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Recurso a utilizar||sobjects|
|Objeto a utilizar||Account|
|Registro a elminar||001D000000INjVe|
|Asignar resultado a variable||Variable|

### Obtener campos especificos
  
Permite obtener campos de un record en SalesForce
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Recurso a utilizar||sobjects|
|Objeto a utilizar||Account|
|Registro a consultar||001D000000INjVe|
|Campos||Cuenta,Nombre,Fecha|
|Asignar resultado a variable||Variable|
