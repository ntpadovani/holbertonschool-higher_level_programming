#!/usr/bin/node
$("DIV#toggle_header").on("click", function(event) {
    $( "header" ).toggleClass('red green');
});