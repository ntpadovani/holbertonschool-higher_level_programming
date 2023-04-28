#!/usr/bin/node
$("#add_item").on("click", function(event) {
    $( ".my_list" ).append('<li>Item</li>');
});