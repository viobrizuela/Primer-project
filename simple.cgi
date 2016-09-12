#!/bin/bash

echo "Content-type: text/html"
echo ""

echo "<html>"
echo "<head>"
echo "<link rel="stylesheet" type="text/css" href="simplestyle.css">"
echo "<title>Simple cgi project</title>"
echo "</head>"
echo "<body>"
echo "<h1>Testing simple cgi project</h1>"

if [ -n "${QUERY_STRING}" ]; then
        /usr/bin/curl -s ${QUERY_STRING}
fi
echo "</body>"
echo "</html>"
