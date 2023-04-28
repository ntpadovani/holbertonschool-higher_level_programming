#!/usr/bin/node
const web_url = 'https://stefanbohacek.com/hellosalut/?lang=fr'
$(function() { $.getJSON(web_url, function(greeting) {
    $("#hello").append(greeting.hello)
}) });
