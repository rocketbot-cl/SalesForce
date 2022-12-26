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
        realResult = []
        for each in resultList:
            realResult.append(each)

        whereToStore = GetParams("whereToStore")
        SetVar(whereToStore, realResult)
    
    if (module == "getListObjects"):

        resource = GetParams("resource")

        resultListObjects = salesforce_I.getListObjects(resource)
        #resultListObjects = str(resultListObjects).replace("false", "\"false\"").replace("true", "\"true\"").replace("null", "\"null\"")
        #resultListObjects = eval(resultListObjects)
        
        realResult = []

        for each in resultListObjects["sobjects"]:
            realResult.append(each["name"])

        whereToStore = GetParams("whereToStore")
        SetVar(whereToStore, realResult)

    if (module == "getMetadata"):

        resource = GetParams("resource")
        theObject = GetParams("theObject")

        resultMetadata = salesforce_I.getMetadata(resource, theObject)
        # resultMetadata = resultMetadata.replace("false", "\"false\"").replace("true", "\"true\"").replace("null", "\"null\"")
        # resultMetadata = eval(resultMetadata)
        realResult = []

        for each in resultMetadata["recentItems"]:
            realResult.append(each)

        whereToStore = GetParams("whereToStore")
        SetVar(whereToStore, realResult)

    if (module == "createRecord"):

        resource = GetParams("resource")
        theObject = GetParams("theObject")
        data = GetParams("data")

        data = data.replace("'", "\"").encode()

        whereToStore = GetParams("whereToStore")
        SetVar(whereToStore, False)

        resultCreation = salesforce_I.createRecord(resource, theObject, data)

        SetVar(whereToStore, resultCreation)
    
    if (module == "updateRecord"):

        resource = GetParams("resource")
        theObject = GetParams("theObject")
        record = GetParams("record")
        data = GetParams("data")

        data = data.replace("'", "\"").encode()

        whereToStore = GetParams("whereToStore")
        SetVar(whereToStore, False)

        resultUpdate = salesforce_I.updateRecord(resource, theObject, record, data)

        SetVar(whereToStore, resultUpdate)

    if (module == "deleteRecord"):

        resource = GetParams("resource")
        theObject = GetParams("theObject")
        record = GetParams("record")

        whereToStore = GetParams("whereToStore")
        SetVar(whereToStore, False)

        resultDelete = salesforce_I.deleteRecord(resource, theObject, record)

        SetVar(whereToStore, resultDelete)

    if (module == "queryOnRecord"):
        
        resource = GetParams("resource")
        theObject = GetParams("theObject")
        record = GetParams("record")
        query = GetParams("query")

        whereToStore = GetParams("whereToStore")
        SetVar(whereToStore, False)

        resultQuery = salesforce_I.queryOnRecord(resource, theObject, record, query)

        SetVar(whereToStore, resultQuery)

except Exception as e:
    print("\x1B[" + "31;40mAn error occurred\x1B[" + "0m")
    PrintException()
    raise e