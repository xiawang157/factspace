(function(){
	
    globalConfig = {
        Q:"#Q_attribute",
        T:"#T_attribute",
        N:"#N_attribute",
        visContainer: "#outputVisContainer",
        jsonContainer: "#outputJSONContainer",
        extractedAttributesContainer: "#extractedAttributesContainer",
        extractedTasksContainer: "#extractedTasksContainer",
        extractedMetaDataContainer: "#metaDataTableContainer",
        inputQueryContainer: "#inputQueryContainer",
        queryInput: "#queryInput",
        queryBtn: "#queryBtn",
        testBtn: "#testBtn",
        datasetSelect: "#datasetSelect",
        executionTimeViz: "#executionTimeViz",
        dataTablesOptions:  {
            paging: false,
            searching: false,
            ordering: false,
            select: false,
            bInfo : false,
            language: {
              emptyTable: "No data"
            },
//            rowGroup: {
//                dataSrc: 0 // attribute
//            },
//            columnDefs: [
//                { "visible": false, "targets": 0 }
//            ],
            scrollX: false,
        }
    };
})()
