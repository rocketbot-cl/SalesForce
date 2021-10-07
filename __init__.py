# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"
    
    pip install <package> -t .

"""

import os
import sys

base_path = tmp_global_obj["basepath"]
cur_path = base_path + 'modules' + os.sep + 'Salesforce' + os.sep + 'libs' + os.sep
if cur_path not in sys.path:
    sys.path.append(cur_path)

from salesforceObj import SalesforceObj

global salesforce_I

module = GetParams("module")

try:

    if (module == "connectToSalesforce"):

        username = GetParams("username")
        password = GetParams("password")
        client_id = GetParams("client_id")
        client_secret = GetParams("client_secret")
        token = GetParams("token")
        domain = GetParams("domain")

        salesforce_I = SalesforceObj(username, password, client_id, client_secret, token, domain)

        resultConnection = False

        if salesforce_I.accessToken != "":
            resultConnection = True
        
        whereToStore = GetParams("whereToStore")
        SetVar(whereToStore, resultConnection)

    if (module == "getListResources"):

        resultList = salesforce_I.getListResources()

        whereToStore = GetParams("whereToStore")
        SetVar(whereToStore, resultList)
    
    if (module == "getListObjects"):

        resource = GetParams("resource")

        resultListObjects = salesforce_I.getListObjects(resource)

        whereToStore = GetParams("whereToStore")
        SetVar(whereToStore, resultListObjects)

    if (module == "getMetadata"):

        resource = GetParams("resource")
        theObject = GetParams("theObject")

        resultMetadata = salesforce_I.getListObjects(resource, theObject)

        whereToStore = GetParams("whereToStore")
        SetVar(whereToStore, resultMetadata)

    if (module == "createRecord"):

        resource = GetParams("resource")
        theObject = GetParams("theObject")
        data = GetParams("data")

        resultCreation = salesforce_I.createRecord(resource, theObject, data)

        whereToStore = GetParams("whereToStore")
        SetVar(whereToStore, resultCreation)

    if (module == "updateRecord"):

        resource = GetParams("resource")
        theObject = GetParams("theObject")
        record = GetParams("record")
        data = GetParams("data")

        resultUpdate = salesforce_I.updateRecord(resource, theObject, record, data)

        whereToStore = GetParams("whereToStore")
        SetVar(whereToStore, resultUpdate)

    if (module == "deleteRecord"):

        resource = GetParams("resource")
        theObject = GetParams("theObject")
        record = GetParams("record")

        resultDelete = salesforce_I.deleteRecord(resource, theObject, record)

        whereToStore = GetParams("whereToStore")
        SetVar(whereToStore, resultDelete)

except Exception as e:
    print("\x1B[" + "31;40mAn error occurred\x1B[" + "0m")
    PrintException()
    raise e