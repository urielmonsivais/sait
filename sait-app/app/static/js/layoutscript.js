$(document).ready(function() {
    $('#sidebarCollapse').on('click', function() {
        $('#sidebar').toggleClass('active');
    });
});
$(function() {
    $('#logout').popover({
        placement: "left",
        trigger: "hover"
    })
});
$(function() {
    $('#pop').popover({
        placement: "top",
        trigger: "hover"
    })
});