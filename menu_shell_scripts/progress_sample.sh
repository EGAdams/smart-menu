#!/bin/sh
#A gauge Box example with dialog
(
c=10
while [ $c -ne 110 ]
    do
        echo $c
        echo "###"
        echo "$c %"
        echo "###"
        #((c+=10))
        c=$((c+10))
        sleep .2
done
) |
dialog --title "A Test Gauge With dialog" --gauge "Please wait ...." 10 60 0

echo "done."

