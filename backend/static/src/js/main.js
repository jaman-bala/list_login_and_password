$(document).ready(function() {
    $('#bootstrapdatatable').DataTable({
      "aLengthMenu": [[3, 5, 10, 25, -1], [3, 5, 10, 25, "All"]],
        "iDisplayLength": 3
       }
    );
} );
console.log("main.js загружен");

$(document).ready(function() {
    if (!$.fn.DataTable.isDataTable('#bootstrapdatatable')) {
        $('#bootstrapdatatable').DataTable();
    }
});